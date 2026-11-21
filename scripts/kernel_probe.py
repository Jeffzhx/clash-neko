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
# 出口校验：delay 只证明「有东西回了 204」，中间盒/白名单假节点同样能秒回。
# 开启后对已 alive 的节点再发一次真实 HTTPS 请求，记录它出网时被看到的公网 IP；
# 出口落在中国大陆（loc=CN）或取不到出口的节点判为不可用。设 0 关闭。
VERIFY_EGRESS = os.environ.get("MIHOMO_VERIFY_EGRESS", "1").strip().lower() not in ("0", "false", "no", "off")
# 默认用明文 HTTP 的回显服务：慢节点上 TLS 握手经常超过 mihomo 的 5s 拨号上限，
# 用 https 当靶子会把「慢但能用」的节点误判成不可用（实测 56/59 都在 5s 处被砍）。
# 2026-11-20 实测本机 http://api.ipify.org 已不可达（curl 直接返回 000、0 字节），
# 换成 AWS 的明文回显（只回 IP，无速率限制、无 TLS）；归属国仍由本地 mmdb 判定。
EGRESS_URL = os.environ.get("MIHOMO_EGRESS_URL", "").strip() or "http://checkip.amazonaws.com"
# 一级兜底：明文 JSON，直接带 countryCode（免费额度 45 次/分，故只作兜底，不作首选）。
EGRESS_FALLBACK_JSON = "http://ip-api.com/json/?fields=status,query,countryCode"
# 二级兜底：trace 明文；但走 https 且可能返回 IPv6，仅在前面都失败时用。
EGRESS_FALLBACK = "https://www.cloudflare.com/cdn-cgi/trace"
EGRESS_MAX = int(os.environ.get("MIHOMO_EGRESS_MAX", "200") or 200)
EGRESS_MMDB = os.environ.get("GEOIP_MMDB", "").strip() or \
    r"D:/AI/2026-09-16-02-16-43/clash-nodes/kernel-test/Country.mmdb"

GOOD_TYPES = {"hysteria", "hysteria2", "anytls", "tuic", "vless", "trojan"}  # naive 已移除：mihomo 内核不支持
DEFAULT_UP = "100 Mbps"
DEFAULT_DOWN = "200 Mbps"
BOOT_WAIT_SEC = 20  # CI 上内核启动可能比本机慢，放宽等待；失败会打印内核日志尾部诊断

# 对内核 external-controller（127.0.0.1）的请求必须**绕开系统代理**：
# 实测本机设了 http_proxy=http://127.0.0.1:10809 时，urllib.request.proxy_bypass('127.0.0.1')
# 返回 False，请求被系统代理接管，拿回来的是代理自己的 504/503 而不是内核的判定
# （2026-11-20 实证：首跑 201 个节点全 dead、明细全是代理错误码，详见 D23）。
_DIRECT_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


# 本机若开着 TUN（mihomo/Clash 的虚拟网卡默认占 198.18.0.0/15），内核发出的测活流量会被
# 再转发一层到当前出口，于是「只有经由当前出口才连得上」的节点也会被判 alive —— 假阳性。
TUN_HINT_PREFIXES = ("198.18.", "198.19.")


def _default_gateway() -> str:
    """尽力取默认网关；取不到返回空串（不影响测活，只影响环境提示）。"""
    try:
        if os.name == "nt":
            out = subprocess.run(["route", "print", "-4"], capture_output=True, text=True,
                                 timeout=8, errors="replace").stdout
            best = None
            for line in out.splitlines():
                parts = line.split()
                if len(parts) >= 5 and parts[0] == "0.0.0.0" and parts[1] == "0.0.0.0":
                    gw, metric = parts[2], parts[4]
                    if metric.isdigit() and (best is None or int(metric) < best[1]):
                        best = (gw, int(metric))
            return best[0] if best else ""
        out = subprocess.run(["ip", "route", "show", "default"], capture_output=True, text=True,
                             timeout=8, errors="replace").stdout
        for line in out.splitlines():
            parts = line.split()
            if "via" in parts:
                return parts[parts.index("via") + 1]
    except Exception:
        pass
    return ""


def detect_environment() -> dict:
    """记录测活机器的网络环境，并在疑似被本机 TUN/系统代理再转发时给出明确警告。"""
    proxy_env = {k: v for k, v in os.environ.items()
                 if k.lower() in ("http_proxy", "https_proxy", "all_proxy") and v.strip()}
    gw = _default_gateway()
    tun = bool(gw) and gw.startswith(TUN_HINT_PREFIXES)
    return {"default_gateway": gw, "tun_suspected": tun, "proxy_env_set": bool(proxy_env)}


def warn_environment(env: dict) -> None:
    if env.get("tun_suspected"):
        print("[kernel-probe] 警告：默认网关 %s 落在 TUN 网段（198.18/198.19），"
              "测活流量会被本机代理再转发一层 —— 结果可能把「只在你当前出口才连得上」的节点"
              "误判为可用。做「国内能不能用」的结论前，请先关闭 TUN/系统代理再跑。"
              % env["default_gateway"], file=sys.stderr, flush=True)
    if env.get("proxy_env_set"):
        print("[kernel-probe] 提示：环境变量里存在 http(s)_proxy（内核走自己出口、不受其影响，"
              "但用 curl 手工复测时会被它接管）。", file=sys.stderr, flush=True)


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


def build_config(nodes: list[dict], controller_port: int, workdir: str,
                 mixed_port: int | None = None) -> str:
    """生成最小 mihomo 配置：只跑 external-controller；需要出口校验时才开一个本地 mixed-port。"""
    import yaml
    proxies = [to_mihomo_proxy(n, f"K{i}") for i, n in enumerate(nodes)]
    cfg = {
        # 有 mixed-port 时必须 rule 模式：direct 会让出口校验的请求绕过代理直连，
        # 测出来的出口是本机出口（假结果）。没有 mixed-port 时不监听，direct 不影响 delay。
        "mode": "rule" if mixed_port else "direct",
        "external-controller": f"127.0.0.1:{controller_port}",
        "proxies": proxies,
        "rules": [],
    }
    if mixed_port:
        # 仅给出口校验用：一个 select 组按需切到某个节点，真实请求经 mixed-port 出去。
        cfg["mixed-port"] = mixed_port
        cfg["proxy-groups"] = [{
            "name": EGRESS_GROUP,
            "type": "select",
            "proxies": [p["name"] for p in proxies] or ["DIRECT"],
        }]
        cfg["rules"] = [f"MATCH,{EGRESS_GROUP}"]
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


EGRESS_GROUP = "__egress__"
UA_HTTP = "Mozilla/5.0 (compatible; kernel-probe/1.0)"
_MMDB_HOLDER: dict = {}


def _cc_from_record(rec) -> str:
    """从 mmdb 记录里取两字母国家码；取不到返回空串（不猜）。

    同一个库可能有三种记录形状，必须都认——否则 `except` 一吞，整道闸门就静默失效：
      - GeoLite2 标准库：`{"country": {"iso_code": "us"}}`
      - mihomo Meta-geoip：`"cn"`（纯字符串）
      - mihomo Meta-geoip 多标签：`["us", "google"]`
    """
    if not rec:
        return ""
    if isinstance(rec, str):
        s = rec.strip()
        return s.upper() if len(s) == 2 and s.isalpha() else ""
    if isinstance(rec, (list, tuple)):
        for item in rec:
            cc = _cc_from_record(item)
            if cc:
                return cc
        return ""
    if isinstance(rec, dict):
        for key in ("country", "registered_country"):
            sub = rec.get(key)
            if isinstance(sub, str) and len(sub.strip()) == 2:
                return sub.strip().upper()
            if isinstance(sub, dict):
                cc = str(sub.get("iso_code") or "").strip().upper()
                if len(cc) == 2:
                    return cc
        # 有些精简库把国家码直接摊平在顶层
        cc = str(rec.get("iso_code") or rec.get("country_code") or "").strip().upper()
        return cc if len(cc) == 2 else ""
    return ""


def _open_mmdb(path: str):
    """打开 mmdb，返回 (db, 原因)。失败时 db 为 None，原因写进报告便于定位。

    两个坑（2026-11-20 本机复现）：
      1) maxminddb 的 C 扩展会把 str 路径 fsencode 后交给 open()，Windows 上路径含中文时
         直接抛 FileNotFoundError（本项目路径就含中文）。传 **文件对象** 可绕开。
      2) mihomo 自带的 geoip.metadb 是 Meta-geoip0 格式，`get()` 返回纯字符串/列表，
         不是 `{"country": {"iso_code": ...}}`——交给 _cc_from_record 统一处理。
    """
    if not path or not os.path.isfile(path):
        return None, f"mmdb 不存在：{path or '(未设置 GEOIP_MMDB)'}"
    try:
        import maxminddb
    except Exception as e:
        return None, f"未安装 maxminddb（{type(e).__name__}）"
    try:
        with open(path, "rb") as f:
            return maxminddb.open_database(f), ""
    except Exception as e:
        return None, f"mmdb 打开失败：{type(e).__name__}: {e}"


def cc_of_ip(ip: str) -> str:
    """用本地 mmdb 查出口 IP 的归属国；查不到返回空串（不猜）。"""
    if not ip:
        return ""
    if "db" not in _MMDB_HOLDER:
        db, why = _open_mmdb(EGRESS_MMDB)
        _MMDB_HOLDER["db"] = db
        _MMDB_HOLDER["why"] = why
        if db is None:
            # 出声不静默：这道闸门失效时，出口落在国内的假节点会被判成 alive。
            print(f"[kernel-probe] 出口归属国判定不可用（{why}）→ 「出口在国内即改判 dead」本轮不生效",
                  file=sys.stderr)
    db = _MMDB_HOLDER["db"]
    if db is None:
        return ""
    try:
        return _cc_from_record(db.get(ip))
    except Exception:
        return ""


def verify_egress(controller_port: int, mixed_port: int, records: list[dict]) -> None:
    """对已判 alive 的节点做真实 HTTPS 出口校验，就地写回 `_liveness.egress`。

    为什么需要：`/proxies/{name}/delay` 只证明「有东西回了 204」。国内中间盒、只放行
    探测 URL 的白名单节点，都能把 delay 测得很漂亮，但真实流量出不去 —— 这就是
    「测速 70ms 却打不开网页」的典型来源。这里改发一次真实 HTTPS，看它出网时
    被看到的公网 IP：取不到 → 只有探测应答；出口是国内 → 请求根本没出国。
    """
    targets = [i for i, r in enumerate(records) if r["_liveness"]["alive"] is True]
    if not targets:
        return
    if len(targets) > EGRESS_MAX:
        print(f"[kernel-probe] 出口校验跳过：alive {len(targets)} 超过上限 {EGRESS_MAX}"
              f"（用 MIHOMO_EGRESS_MAX 调大）", file=sys.stderr)
        for i in targets:
            records[i]["_liveness"]["egress"] = {"checked": False, "reason": "over_limit"}
        return

    # 只走内核 mixed-port，并清空环境代理：否则又会变成「经本机代理再转发」的假结果。
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({
        "http": f"http://127.0.0.1:{mixed_port}",
        "https": f"http://127.0.0.1:{mixed_port}",
    }))
    print(f"[kernel-probe] 出口校验开始：{len(targets)} 个 alive 节点，目标 {EGRESS_URL}", flush=True)
    for i in targets:
        rec = records[i]
        name = f"K{i}"
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{controller_port}/proxies/{urllib.parse.quote(EGRESS_GROUP)}",
                method="PUT", data=json.dumps({"name": name}).encode(),
                headers={"Content-Type": "application/json"})
            _DIRECT_OPENER.open(req, timeout=5).read()
        except Exception as e:
            rec["_liveness"]["egress"] = {"checked": False, "reason": f"switch_failed:{type(e).__name__}"}
            print(f"  [egress {i + 1}] {rec.get('server')} 切换失败 {type(e).__name__}", flush=True)
            continue

        t0 = time.time()
        ip = loc = ""
        err = ""
        for target in (EGRESS_URL, EGRESS_FALLBACK_JSON, EGRESS_FALLBACK):
            try:
                with opener.open(urllib.request.Request(target, headers={"User-Agent": UA_HTTP}),
                                 timeout=max(10, TIMEOUT_MS / 1000 + 4)) as r:
                    body = r.read(4096).decode("utf-8", "replace").strip()
            except Exception as e:
                err = f"{type(e).__name__}:{getattr(e, 'code', '')}"
                continue
            if body.startswith("{"):
                try:
                    doc = json.loads(body)
                    ip = str(doc.get("query") or doc.get("ip") or "").strip()
                    loc = str(doc.get("countryCode") or "").strip().upper()
                except Exception:
                    ip = ""
            elif "=" in body:
                for line in body.splitlines():
                    if line.startswith("ip="):
                        ip = line.split("=", 1)[1].strip()
                    elif line.startswith("loc="):
                        loc = line.split("=", 1)[1].strip().upper()
            else:
                ip = body.split()[0] if body else ""
            if ip:
                err = ""
                break
        if ip and not loc:
            loc = cc_of_ip(ip)  # 明文回显只给 IP，归属国用本地 mmdb 判定
        ms = int((time.time() - t0) * 1000)
        rec["_liveness"]["egress"] = {"checked": True, "ip": ip, "loc": loc,
                                      "latency_ms": ms, "error": err}
        if loc == "CN":
            rec["_liveness"]["alive"] = False
            rec["_liveness"]["evidence"] = "egress_cn"
            rec["_liveness"]["reason"] = (f"有据（负向）：delay 通，但真实流量出口在国内"
                                          f"（{ip}，{ms}ms），请求没真正出国")
        elif not ip:
            rec["_liveness"]["alive"] = False
            rec["_liveness"]["evidence"] = "egress_unreachable"
            rec["_liveness"]["reason"] = (f"有据（负向）：delay 通，但真实 HTTPS 取不到出口"
                                          f"（{err or '超时'}），说明只应答探测、无实际出网")
        else:
            rec["_liveness"]["reason"] += f"；真实出口 {ip}/{loc or '?'} {ms}ms"
            if not loc:
                # 拿得到 IP 但判不出归属国（IPv6 或 mmdb 无记录）：不算失败，但必须留痕，
                # 否则「出口在国内改判 dead」这道闸门会在这批节点上静默失效。
                rec["_liveness"]["reason"] += "；归属国未知（mmdb 无该 IP 记录，闸门对本节点未生效）"
        print(f"  [egress {i + 1}/{len(targets)}] {rec.get('server')}:{rec.get('port')} -> "
              f"{'OK' if rec['_liveness']['alive'] else 'DROP'} "
              f"{ip or '-'}/{loc or '-'} {ms}ms {err}", flush=True)


def wait_controller(port: int, proc: subprocess.Popen, deadline: int = BOOT_WAIT_SEC) -> bool:
    url = f"http://127.0.0.1:{port}/version"
    end = time.time() + deadline
    while time.time() < end:
        if proc.poll() is not None:
            return False
        try:
            with _DIRECT_OPENER.open(url, timeout=1) as r:
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
        with _DIRECT_OPENER.open(url, timeout=(TIMEOUT_MS / 1000) + 3) as r:
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
    env_info = detect_environment()
    warn_environment(env_info)
    nodes = load_us_nodes()
    print(f"[kernel-probe] 开始 {now}；内核={MIHOMO_BIN}；节点 {len(nodes)} 个；测试URL={TEST_URL}")

    with tempfile.TemporaryDirectory(prefix="kernel-probe-") as workdir:
        # 预校验：先用内核 -t 剔除会让配置 fatal 的坏节点（如非法 Reality 公钥），
        # 否则单个坏节点拖垮整个配置、全部无法测活。被剔除的节点不进测活、也不进最终订阅。
        nodes, dropped = precheck_config(nodes, workdir)
        port = free_port()
        mixed_port = free_port() if VERIFY_EGRESS else None
        cfg = build_config(nodes, port, workdir, mixed_port=mixed_port)
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

            if VERIFY_EGRESS and mixed_port:
                try:
                    verify_egress(port, mixed_port, records)
                except Exception as e:  # 校验失败不该让整轮失败：保留 delay 结论并在报告标注
                    print(f"[kernel-probe] 出口校验异常（{type(e).__name__}: {e}），"
                          f"仅保留 delay 结论", file=sys.stderr)
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
    egress_cn = [r for r in records if r["_liveness"].get("evidence") == "egress_cn"]
    egress_dead = [r for r in records if r["_liveness"].get("evidence") == "egress_unreachable"]
    out = {
        "generated_at": now,
        "unit": "U4-kernel",
        "methodology": {
            "engine": "mihomo external-controller /proxies/{name}/delay",
            "version": VERSION_LABEL or "unknown",
            "test_url": TEST_URL,
            "timeout_ms": TIMEOUT_MS,
            "egress_verify": bool(VERIFY_EGRESS and mixed_port),
            "egress_url": EGRESS_URL if (VERIFY_EGRESS and mixed_port) else None,
            "decision": "内核完成 7 种协议握手且 HTTP 200/204 → alive；否则 dead（协议级负向）。",
        },
        "environment": {"kernel_mode": True, "precheck_dropped": len(dropped), **env_info},
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
        f"- 预校验剔除非法节点：{len(dropped)}（内核 -t 检出的坏字段节点，不进测活也不进订阅）",
        (f"- 出口校验：开启（目标 `{EGRESS_URL}`）→ 真实流量取不到出口 {len(egress_dead)} 个、"
         f"出口在国内 {len(egress_cn)} 个，均已改判 dead"
         if (VERIFY_EGRESS and mixed_port) else "- 出口校验：未开启（`MIHOMO_VERIFY_EGRESS=0`）"),
        f"- 测活环境：默认网关 `{env_info['default_gateway'] or '取不到'}`"
        + ("（**TUN 网段，结果可能含假阳性：流量被本机代理再转发了一层**）"
           if env_info["tun_suspected"] else "（未见 TUN 网段网关）"), "",
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
