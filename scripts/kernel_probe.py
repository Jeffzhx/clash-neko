#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U4+ 内核级真实测活（mihomo external-controller API）。

与 liveness_check.py 的区别：
  - liveness_check.py：纯 Python TCP/UDP 端口探测（端口级，不能证明 hysteria2 握手成功）。
  - 本脚本：启动真正的 mihomo 内核，对每个节点调 /proxies/{name}/delay，
            内核会完成 6 种协议（hysteria/hysteria2/anytls/tuic/vless/trojan）握手；naive 因 mihomo 不支持已移除
            并通过代理发一个 HTTP 请求，拿到 200/204 才算 alive（协议级证据）。

用法（CI 中下载内核后设置 MIHOMO_BIN）：
    MIHOMO_BIN=/path/to/mihomo python scripts/kernel_probe.py
    MIHOMO_TEST_URL=http://www.gstatic.com/generate_204 MIHOMO_BIN=... python scripts/kernel_probe.py

环境变量：
    MIHOMO_BIN       mihomo 内核可执行文件路径（必填；未设置 → exit 2 表示缺内核，调用方应降级）
    MIHOMO_TEST_URL  测活目标 URL（默认 http://www.gstatic.com/generate_204）
    MIHOMO_TIMEOUT    单节点超时毫秒（默认 8000）
    MIHOMO_VERSION    仅用于报告标注内核版本字符串

产出（与 liveness_check.py 同格式，供 build_subscriptions.py 消费）：
    <root>/alive_nodes.json
    <root>/probe/liveness-report.md
"""

from __future__ import annotations

import datetime
import ipaddress
import json
import os
import random
import socket
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_PATH = os.path.join(PROJECT, "us_nodes.json")
ALIVE_PATH = os.path.join(PROJECT, "alive_nodes.json")
REPORT_PATH = os.path.join(PROJECT, "probe", "liveness-report.md")

MIHOMO_BIN = os.environ.get("MIHOMO_BIN", "").strip()
TEST_URL = os.environ.get("MIHOMO_TEST_URL", "").strip() or "http://www.gstatic.com/generate_204"
TIMEOUT_MS = int(os.environ.get("MIHOMO_TIMEOUT", "8000") or 8000)
VERSION_LABEL = os.environ.get("MIHOMO_VERSION", "").strip()

GOOD_TYPES = {"hysteria", "hysteria2", "anytls", "tuic", "vless", "trojan"}  # naive 已移除：mihomo 内核不支持
DEFAULT_UP = "100 Mbps"
DEFAULT_DOWN = "200 Mbps"
BOOT_WAIT_SEC = 20  # CI 上内核启动可能比本机慢，放宽等待；失败会打印内核日志尾部诊断


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def _first(node: dict, *keys: str, default: str = "") -> str:
    """按 keys 顺序取第一个非空字符串值（与 build_subscriptions._first 一致）。"""
    for k in keys:
        v = node.get(k)
        if v is not None and str(v).strip() != "":
            return str(v).strip()
    return default


def _obfs_of(node: dict) -> str:
    return _first(node, "obfs", default="")


def _apply_obfs(node: dict, proxy: dict) -> None:
    """写 obfs 字段对；mihomo 要求 obfs 必须配 obfs-password，否则解析整个配置 fatal。
    源里只有 obfs 没有 password 时选择不开启混淆（丢弃 obfs），保证配置合法、不影响其它节点。
    """
    obfs = _obfs_of(node)
    if not obfs:
        return
    pwd = _first(node, "obfs-password", "obfs_password", "obfspwd", default="")
    if not pwd:
        return  # 缺密码→不开混淆，避免内核 fatal
    proxy["obfs"] = obfs
    proxy["obfs-password"] = pwd


def _alpn_of(node: dict) -> list[str]:
    """alpn 兼容 list 与逗号分隔字符串两种来源。"""
    v = node.get("alpn")
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    return []


# 兼容旧调用方（原 first() 与 _first 等价）
first = _first


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def to_mihomo_proxy(node: dict, name: str) -> dict:
    """把一个节点映射为 mihomo/Clash proxy（按协议分支，兼容字段别名）。

    与 build_subscriptions.to_mihomo_proxy 逐字一致：内核测活注入同一份字段，
    字段错了测活就假。支持 tuic / vless(含 Reality+ws/grpc) / trojan（naive 分支保留兼容但白名单已移除）。
    """
    ntype = str(node.get("type", "")).strip().lower()
    server = str(node.get("server", "")).strip()
    port = int(node.get("port", 443) or 443)
    sni = _first(node, "sni", "server_name", "host", default="")
    skip = bool(node.get("skip-cert-verify", True))

    proxy: dict = {"name": name, "type": ntype, "server": server, "port": port}

    if ntype == "hysteria2":
        proxy["auth"] = _first(node, "auth", "password", "auth_str")
        if sni:
            proxy["sni"] = sni
        proxy["skip-cert-verify"] = skip
        _apply_obfs(node, proxy)

    elif ntype == "hysteria":
        proxy["auth"] = _first(node, "auth", "auth_str", "password")
        _apply_obfs(node, proxy)
        proxy["protocol"] = _first(node, "protocol", default="udp")
        if sni:
            proxy["sni"] = sni
        proxy["skip-cert-verify"] = skip
        proxy["up"] = _first(node, "up", default=DEFAULT_UP)
        proxy["down"] = _first(node, "down", default=DEFAULT_DOWN)

    elif ntype == "anytls":
        proxy["password"] = _first(node, "password", "auth", "auth_str")
        if sni:
            proxy["sni"] = sni
        proxy["skip-cert-verify"] = skip

    elif ntype == "tuic":
        # TUIC v5：uuid + password；v4 token 仅在无 uuid 时兼容
        uuid = _first(node, "uuid")
        if uuid:
            proxy["uuid"] = uuid
            proxy["password"] = _first(node, "password", "auth")
        else:
            token = _first(node, "token")
            if token:
                proxy["token"] = token
        if sni:
            proxy["sni"] = sni
        proxy["skip-cert-verify"] = skip
        alpn = _alpn_of(node)
        if alpn:
            proxy["alpn"] = alpn
        for k in ("congestion-controller", "udp-relay-mode", "disable-sni", "reduce-rtt"):
            if k in node and node[k] not in (None, ""):
                proxy[k] = node[k]

    elif ntype == "vless":
        proxy["uuid"] = _first(node, "uuid")
        flow = _first(node, "flow")
        if flow:
            proxy["flow"] = flow
        servername = _first(node, "servername", "sni", "host")
        if servername:
            proxy["servername"] = servername
        proxy["skip-cert-verify"] = skip
        proxy["tls"] = True
        alpn = _alpn_of(node)
        if alpn:
            proxy["alpn"] = alpn
        fp = _first(node, "client-fingerprint", "fingerprint")
        if fp:
            proxy["client-fingerprint"] = fp

        # Reality：security=reality 或存在 public-key/pbk 即视为 Reality
        pbk = _first(node, "public-key", "pbk")
        sid = _first(node, "short-id", "sid")
        if _first(node, "security").lower() == "reality" or pbk:
            reality = {}
            if pbk:
                reality["public-key"] = pbk
            if sid:
                reality["short-id"] = sid
            proxy["reality-opts"] = reality
            proxy["tls"] = True

        # 传输层：URI 的 type=ws/grpc 在 fetch 阶段已归一为 network
        network = _first(node, "network").lower()
        if network in ("ws", "grpc"):
            proxy["network"] = network
            if network == "ws":
                ws_opts = {}
                path = _first(node, "path")
                host = _first(node, "host")
                if path:
                    ws_opts["path"] = path
                if host:
                    ws_opts["headers"] = {"Host": host}
                if ws_opts:
                    proxy["ws-opts"] = ws_opts
            else:
                grpc_opts = {}
                svc = _first(node, "serviceName", "service-name", "grpc-service-name")
                if svc:
                    grpc_opts["grpc-service-name"] = svc
                if grpc_opts:
                    proxy["grpc-opts"] = grpc_opts

    elif ntype == "trojan":
        proxy["password"] = _first(node, "password", "auth")
        if sni:
            proxy["sni"] = sni
        alpn = _alpn_of(node)
        if alpn:
            proxy["alpn"] = alpn
        proxy["skip-cert-verify"] = skip
        network = _first(node, "network")
        if network:
            proxy["network"] = network

    elif ntype == "naive":
        proxy["username"] = _first(node, "username", "user")
        proxy["password"] = _first(node, "password", "auth")
        if sni:
            proxy["sni"] = sni
        alpn = _alpn_of(node)
        if alpn:
            proxy["alpn"] = alpn
        proxy["skip-cert-verify"] = skip

    return proxy


def build_config(nodes: list[dict], controller_port: int, workdir: str) -> str:
    """生成最小 mihomo 配置：只跑 external-controller，不做任何代理监听。"""
    import yaml
    proxies = [to_mihomo_proxy(n, f"K{i}") for i, n in enumerate(nodes)]
    cfg = {
        "mode": "direct",
        "external-controller": f"127.0.0.1:{controller_port}",
        "proxies": proxies,
        "rules": [],
    }
    path = os.path.join(workdir, "config.yaml")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False)
    return path


def precheck_config(nodes: list[dict], workdir: str) -> tuple[list[dict], list[dict]]:
    """用内核 `-t` 预校验配置，自动剔除会让内核 fatal 的坏节点（如非法 Reality 公钥）。

    背景：单个非法字段（如 invalid REALITY public key）会让 mihomo 拒绝整个配置，
    导致所有节点都无法测活。内核 fatal 信息形如 `proxy 321: invalid ...`，
    其中 321 是 proxies 数组下标，正好对应这里 K321。逐个剔除并重验，直到配置通过。

    返回 (干净节点列表, 被剔除节点列表)。无法解析错误或达上限时停止剔除（保留剩余节点）。
    """
    import re
    import yaml

    MAX_DROP = 30
    clean = list(nodes)
    dropped: list[dict] = []
    fatal_re = re.compile(r"proxy\s+(\d+)\s*:", re.I)

    for _ in range(MAX_DROP):
        if not clean:
            break
        cfg = build_config(clean, 19999, workdir)  # 端口无关，-t 只校验不监听
        try:
            r = subprocess.run(
                [MIHOMO_BIN, "-t", "-f", cfg, "-d", workdir],
                capture_output=True, text=True, timeout=20,
            )
        except Exception:
            break  # 内核执行异常→不剔除，交给后续启动逻辑处理
        if r.returncode == 0:
            break  # 配置合法
        m = fatal_re.search((r.stdout or "") + (r.stderr or ""))
        if not m:
            break  # 无法定位坏节点→停止剔除
        idx = int(m.group(1))
        if idx < 0 or idx >= len(clean):
            break
        dropped.append(clean[idx])
        server = clean[idx].get("server", "?")
        print(f"[kernel-probe] 预校验剔除坏节点 K{idx} ({server}): "
              f"{(r.stdout + r.stderr).splitlines()[-1][:120]}", file=sys.stderr)
        clean.pop(idx)

    if dropped:
        print(f"[kernel-probe] 预校验共剔除 {len(dropped)} 个非法节点，剩余 {len(clean)} 个进入测活",
              file=sys.stderr)
    return clean, dropped


def wait_controller(port: int, proc: subprocess.Popen, deadline: int = BOOT_WAIT_SEC) -> bool:
    url = f"http://127.0.0.1:{port}/version"
    end = time.time() + deadline
    while time.time() < end:
        if proc.poll() is not None:
            return False
        try:
            with urllib.request.urlopen(url, timeout=1) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.3)
    return False


def proxy_delay(port: int, name: str) -> tuple[int | None, str]:
    """调 mihomo /proxies/{name}/delay，返回 (延迟ms, 说明)。成功=拿到 delay 数值。"""
    q = urllib.parse.urlencode({"url": TEST_URL, "timeout": str(TIMEOUT_MS),
                                 "expected": "200/204"})
    url = f"http://127.0.0.1:{port}/proxies/{urllib.parse.quote(name)}/delay?{q}"
    try:
        with urllib.request.urlopen(url, timeout=(TIMEOUT_MS / 1000) + 3) as r:
            body = r.read().decode("utf-8", "ignore")
        d = json.loads(body)
        delay = d.get("delay")
        if isinstance(delay, (int, float)) and delay >= 0:
            return int(delay), f"内核协议级测活通过：协议握手 + HTTP {TEST_URL} 返回 200/204，延迟 {int(delay)}ms"
        return None, f"内核返回无有效 delay：{body[:200]}"
    except Exception as e:
        return None, f"内核测活失败：{type(e).__name__}: {e}"


def load_us_nodes() -> list[dict]:
    with open(US_PATH, "r", encoding="utf-8") as f:
        doc = json.load(f)
    nodes = doc.get("us_nodes", []) if isinstance(doc, dict) else []
    return [n for n in nodes if isinstance(n, dict) and n.get("type", "").lower() in GOOD_TYPES]


def main() -> int:
    if not MIHOMO_BIN or not os.path.isfile(MIHOMO_BIN):
        print("[kernel-probe] MIHOMO_BIN 未设置或文件不存在 → 返回码 2（调用方应降级到端口级测活）",
              file=sys.stderr)
        return 2

    now = utc_now_iso()
    nodes = load_us_nodes()
    print(f"[kernel-probe] 开始 {now}；内核={MIHOMO_BIN}；节点 {len(nodes)} 个；测试URL={TEST_URL}")

    with tempfile.TemporaryDirectory(prefix="kernel-probe-") as workdir:
        # 预校验：先用内核 -t 剔除会让配置 fatal 的坏节点（如非法 Reality 公钥），
        # 否则单个坏节点拖垮整个配置、全部无法测活。被剔除的节点不进测活、也不进最终订阅。
        nodes, dropped = precheck_config(nodes, workdir)
        port = free_port()
        cfg = build_config(nodes, port, workdir)
        # 内核日志写到文件而不是丢弃：启动失败时能打印出来定位（CI 上曾因 DEVNULL 看不到原因）。
        kernel_log = os.path.join(workdir, "kernel.log")
        logf = open(kernel_log, "w", encoding="utf-8", errors="replace")
        try:
            proc = subprocess.Popen(
                [MIHOMO_BIN, "-f", cfg, "-d", workdir],
                stdout=logf, stderr=subprocess.STDOUT,
            )
        except Exception as e:
            # 内核文件存在但不是可执行的 mihomo（或权限/架构问题）→ 视为不可用，降级。
            print(f"[kernel-probe] 内核启动异常（{type(e).__name__}: {e}）→ 返回码 2（降级）", file=sys.stderr)
            logf.close()
            return 2
        try:
            if not wait_controller(port, proc):
                print("[kernel-probe] mihomo external-controller 未就绪 → 返回码 2（降级）", file=sys.stderr)
                # 打印内核日志尾部，便于看清是启动崩溃 / 配置错误 / 权限问题。
                try:
                    logf.flush()
                    with open(kernel_log, "r", encoding="utf-8", errors="replace") as f:
                        tail = f.read().splitlines()[-20:]
                    if tail:
                        print("[kernel-probe] 内核日志尾部（诊断）：", file=sys.stderr)
                        for line in tail:
                            print("  | " + line[:300], file=sys.stderr)
                except Exception as e:
                    print(f"[kernel-probe] 读取内核日志失败：{e}", file=sys.stderr)
                return 2
            # 并发测活：放宽协议后节点可达数百个，串行会超过 CI 时限；8 并发把它压到几分钟。
            import concurrent.futures
            workers = max(1, min(8, len(nodes) or 1))

            def probe_one(idx: int, node: dict):
                name = f"K{idx}"
                delay, detail = proxy_delay(port, name)
                return idx, node, delay, detail

            results: dict[int, tuple] = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
                futs = [ex.submit(probe_one, i, n) for i, n in enumerate(nodes)]
                for fut in concurrent.futures.as_completed(futs):
                    idx, node, delay, detail = fut.result()
                    results[idx] = (node, delay, detail)
                    print(f"  [{idx+1}/{len(nodes)}] {node.get('server')}:{node.get('port')} -> "
                          f"{'alive' if delay is not None else 'dead'} ({delay if delay is not None else '-'}ms)")

            records: list[dict] = []
            for idx in range(len(nodes)):  # 按原顺序输出，保证与配置里 K{i} 对齐
                node, delay, detail = results[idx]
                rec = dict(node)
                alive = delay is not None
                rec["_liveness"] = {
                    "alive": alive,
                    "method": ["kernel_uritest"],
                    "latency_ms": delay,
                    "evidence": "kernel_delay" if alive else "kernel_fail",
                    "reason": ("有据（协议级正向）：" if alive else "有据（协议级负向）：") + detail,
                    "tcp": {"status": "n/a", "ok": None, "latency_ms": None,
                            "detail": "内核模式不做独立 TCP 探测"},
                    "udp": {"status": "n/a", "latency_ms": None,
                            "detail": "内核模式不做独立 UDP 探测"},
                    "kernel_delay_ms": delay,
                }
                records.append(rec)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
            logf.close()

    alive = [r for r in records if r["_liveness"]["alive"] is True]
    dead = [r for r in records if r["_liveness"]["alive"] is False]
    unknown = [r for r in records if r["_liveness"]["alive"] == "unknown"]
    out = {
        "generated_at": now,
        "unit": "U4-kernel",
        "methodology": {
            "engine": "mihomo external-controller /proxies/{name}/delay",
            "version": VERSION_LABEL or "unknown",
            "test_url": TEST_URL,
            "timeout_ms": TIMEOUT_MS,
            "decision": "内核完成 7 种协议握手且 HTTP 200/204 → alive；否则 dead（协议级负向）。",
        },
        "environment": {"kernel_mode": True, "precheck_dropped": len(dropped)},
        "input_node_count": len(records),
        "alive_count": len(alive),
        "unknown_count": len(unknown),
        "dead_count": len(dead),
        "alive_nodes": alive,
        "unknown_nodes": unknown,
        "dead_nodes": dead,
    }
    with open(ALIVE_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    lines = [
        "# U4 内核级真实测活报告", "",
        f"- 生成时间：{now}",
        f"- 引擎：mihomo external-controller `/proxies/{{name}}/delay`（内核 {VERSION_LABEL or 'unknown'}）",
        f"- 测活 URL：`{TEST_URL}`；单节点超时 {TIMEOUT_MS}ms",
        f"- 判定：alive {len(alive)} / dead {len(dead)} / unknown {len(unknown)}",
        f"- 预校验剔除非法节点：{len(dropped)}（内核 -t 检出的坏字段节点，不进测活也不进订阅）", "",
        "## 逐节点（server:port / 判定 / 延迟 / 依据）", "",
        "| # | server:port | 判定 | 延迟(ms) | 依据 |",
        "|---|-------------|------|----------|------|",
    ]
    for idx, r in enumerate(records, 1):
        lv = r["_liveness"]
        lines.append(f"| {idx} | `{r.get('server')}:{r.get('port')}` | {lv['alive']} | "
                     f"{lv['latency_ms'] if lv['latency_ms'] is not None else '-'} | {lv['reason']} |")
    lines += ["", "## 说明", "",
              "- 本报告为**协议级**测活：内核真实完成所选协议握手并经代理发起 HTTP 请求，",
              "  比端口级 TCP/UDP 探测可靠得多；alive 的节点经客户端导入理应可用。",
              "- 国内用户仍可能受本地网络/GFW 影响，最终以客户端实测为准。", ""]
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[kernel-probe] 完成：alive {len(alive)} / dead {len(dead)} / unknown {len(unknown)}")
    print(f"[kernel-probe] 产出：{ALIVE_PATH} / {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
