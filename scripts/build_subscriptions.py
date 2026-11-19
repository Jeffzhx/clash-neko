#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
订阅生成器（单格式：Clash YAML）。

背景：项目原为双格式 main.yaml(mihomo) + nekobox.json(sing-box)，但 NekoBox 的
「从链接导入订阅」按内容嗅探，不认完整 sing-box JSON 配置；Clash YAML 订阅则能识别。
经用户确认改为单格式——两个订阅 URL 都返回同一份 Clash YAML 内容：
  - main.yaml     主订阅
  - nekobox.json  兼容地址（文件名沿用，内容是 Clash YAML；NekoBox 按内容识别）

用法（脚本按 __file__ 推导项目根，任意 cwd 均可运行）：
    C:/Users/35637/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe scripts/build_subscriptions.py

输入（只读，绝不覆盖）：
    <root>/alive_nodes.json    U4/U4+ 产出的 alive_nodes 数组

输出（覆盖写本单元自己的产物，不动他人文件）：
    <root>/main.yaml
    <root>/nekobox.json        （内容为 Clash YAML，与 main.yaml 一致）
    <root>/probe/subscription-build-report.md

设计要点：
    1. 红线：只输出 type ∈ {hysteria, hysteria2, anytls, tuic, vless, trojan} 的节点（6 种；naive 已被移除因 mihomo 内核不支持）；
       其它协议过滤并在报告登记。VLESS Reality 仍是 vless 类型，靠 reality-opts 字段区分。
    2. 单格式：一份 Clash YAML 同时写到两个订阅路径，节点集合天然一致。
    3. 空输入（alive_nodes=[]）也产出合法空订阅（proxies=[] + 基础 group），不是坏文件。
    4. 本机无内核时只做结构校验（yaml.safe_load），不做内核级 -t，报告如实注明。
    5. 不伪造节点、不塞入 unknown/dead 节点。
"""

from __future__ import annotations

import collections
import datetime
import hashlib
import json
import os
import sys

import yaml

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIVE_PATH = os.path.join(PROJECT, "alive_nodes.json")
MAIN_PATH = os.path.join(PROJECT, "main.yaml")
NEKO_PATH = os.path.join(PROJECT, "nekobox.json")
REPORT_PATH = os.path.join(PROJECT, "probe", "subscription-build-report.md")

# 红线：仅收 7 种协议（VLESS Reality 仍归属 vless）
ALLOWED_PROTOCOLS = ("hysteria", "hysteria2", "anytls", "tuic", "vless", "trojan")  # naive 已移除：mihomo 内核不支持

# hysteria v1 带宽占位默认值（非节点真实性数据，仅保证配置可用）
DEFAULT_UP = "100 Mbps"
DEFAULT_DOWN = "200 Mbps"


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def load_alive_nodes() -> tuple[list[dict], dict]:
    """读取 alive_nodes.json 的 alive_nodes 数组（只读）。返回 (nodes, 原文件元信息)。"""
    with open(ALIVE_PATH, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    nodes = data.get("alive_nodes", [])
    if not isinstance(nodes, list):
        nodes = []
    nodes = [n for n in nodes if isinstance(n, dict)]
    return nodes, data


def filter_by_protocol(nodes: list[dict]) -> tuple[list[dict], list[dict]]:
    """白名单过滤：返回 (保留节点, 被拒节点[{type,server,port,reason}])。"""
    kept, rejected = [], []
    for node in nodes:
        ntype = str(node.get("type", "")).strip().lower()
        if ntype in ALLOWED_PROTOCOLS:
            kept.append(node)
        else:
            rejected.append(
                {
                    "type": ntype or "(空)",
                    "server": str(node.get("server", "")),
                    "port": node.get("port"),
                    "reason": "type 不在白名单 {hysteria,hysteria2,anytls,tuic,vless,trojan}",
                }
            )
    return kept, rejected


def assign_names(nodes: list[dict]) -> list[str]:
    """生成唯一可读的 name：US-{type}-{server}-{port}，冲突追加序号。"""
    used: set[str] = set()
    names: list[str] = []
    for node in nodes:
        ntype = str(node.get("type", "")).strip().lower()
        server = str(node.get("server", "")).strip()
        port = node.get("port", 443)
        base = f"US-{ntype}-{server}-{port}"
        name = base
        idx = 2
        while name in used:
            name = f"{base}-{idx}"
            idx += 1
        used.add(name)
        names.append(name)
    return names


def _first(node: dict, *keys: str, default: str = "") -> str:
    """按 keys 顺序取第一个非空字符串值。"""
    for k in keys:
        v = node.get(k)
        if v is not None and str(v).strip() != "":
            return str(v).strip()
    return default


def _obfs_of(node: dict) -> str:
    return _first(node, "obfs", default="")


def _alpn_of(node: dict) -> list[str]:
    """alpn 兼容 list 与逗号分隔字符串两种来源。"""
    v = node.get("alpn")
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    return []


def to_mihomo_proxy(node: dict, name: str) -> dict:
    """把一个节点映射为 mihomo/Clash proxy（按协议分支，兼容字段别名）。

    与 kernel_probe.to_mihomo_proxy 逐字一致：内核测活注入同一份字段，
    字段错了测活就假。支持 tuic / vless(含 Reality+ws/grpc) / trojan（naive 分支保留兼容但白名单已移除）。
    """
    ntype = str(node.get("type", "")).strip().lower()
    server = str(node.get("server", "")).strip()
    port = int(node.get("port", 443) or 443)
    sni = _first(node, "sni", "server_name", "host", default="")
    skip = bool(node.get("skip-cert-verify", True))
    obfs = _obfs_of(node)

    proxy: dict = {"name": name, "type": ntype, "server": server, "port": port}

    if ntype == "hysteria2":
        proxy["auth"] = _first(node, "auth", "password", "auth_str")
        if sni:
            proxy["sni"] = sni
        proxy["skip-cert-verify"] = skip
        if obfs:
            proxy["obfs"] = obfs

    elif ntype == "hysteria":
        proxy["auth"] = _first(node, "auth", "auth_str", "password")
        if obfs:
            proxy["obfs"] = obfs
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


def build_clash_config(names: list[str], nodes: list[dict]) -> dict:
    """组装 Clash 配置：proxies / proxy-groups / rules。空输入时 proxies=[] 仍合法。"""
    proxies = [to_mihomo_proxy(node, name) for node, name in zip(nodes, names)]
    group_proxies = ["DIRECT", "REJECT"] + [p["name"] for p in proxies]
    return {
        "proxies": proxies,
        "proxy-groups": [
            {"name": "PROXY", "type": "select", "proxies": group_proxies},
        ],
        "rules": [
            "GEOIP,private,DIRECT,no-resolve",
            "MATCH,PROXY",
        ],
    }


def validate_structures(paths: list[str]) -> dict:
    """结构校验：重新 safe_load 自己的产物，确认可解析且关键字段存在。"""
    results = {}
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                doc = yaml.safe_load(fh)
            ok = (
                isinstance(doc, dict)
                and isinstance(doc.get("proxies"), list)
                and isinstance(doc.get("proxy-groups"), list)
                and isinstance(doc.get("rules"), list)
            )
        except Exception:
            ok = False
        results[os.path.basename(path)] = ok
    return results


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_report(now: str, *, input_count: int, kept: list[dict], rejected: list[dict],
                 validation: dict) -> None:
    """覆盖写报告，含输入/输出计数、协议分布、单格式说明、校验、空列表说明。"""
    dist = collections.Counter(str(n.get("type", "")).strip().lower() for n in kept)
    dist_lines = "\n".join(f"  - {k}: {v}" for k, v in sorted(dist.items())) or "  - （无）"
    rejected_lines = "\n".join(
        f"  - type={r['type']} server={r['server']} port={r['port']} —— {r['reason']}"
        for r in rejected
    ) or "  - （无，输入未混入非白名单协议）"

    empty_note = (
        "当前 alive_nodes=[]，按红线生成**合法空订阅**（proxies=[]），"
        "这是合法结果，不是错误；本单元未塞入 unknown/dead 节点、未编造节点。"
        if input_count == 0 and not kept
        else "输入非空，按节点字段一一映射输出。"
    )

    all_valid = all(validation.values())
    val_lines = "\n".join(f"  - `{name}`：{'通过' if ok else '失败'}" for name, ok in validation.items())

    report = f"""# 订阅构建报告（单格式·覆盖写，不追加）

- 生成时间：{now}
- 输入文件：`{ALIVE_PATH}`
- 输入节点数（alive_nodes）：{input_count}
- 输出节点数：{len(kept)}（白名单过滤后）
- 被过滤节点数：{len(rejected)}
- 协议分布（输出）：
{dist_lines}

## 格式口径（已按用户决定改为单格式）
- 只输出 **Clash YAML** 一种格式。
- `main.yaml`（主订阅）与 `nekobox.json`（兼容地址，文件名沿用）写入**同一份 Clash YAML 内容**。
- 原因：NekoBox 的「从链接导入订阅」按内容嗅探，不认完整 sing-box JSON 配置，但能识别 Clash YAML；
  单格式避免双份维护与格式不识别，两个订阅 URL 均保持可用、节点集合天然一致。

## 白名单过滤（红线）
- 仅输出 type ∈ {{hysteria, hysteria2, anytls, tuic, vless, trojan}}（6 种）；其它协议过滤并登记：
{rejected_lines}

## 字段映射表（7 种协议 → mihomo/Clash.Meta）
| 协议 | 关键字段 |
|------|----------|
| hysteria | auth / obfs / protocol(udp) / sni / skip-cert-verify / up / down |
| hysteria2 | auth / obfs / sni / skip-cert-verify |
| anytls | password / sni / skip-cert-verify |
| tuic | uuid / password(v5) 或 token(v4) / alpn / sni / skip-cert-verify / congestion-controller / udp-relay-mode / disable-sni / reduce-rtt |
| vless | uuid / flow / servername(sni) / tls:true / alpn / client-fingerprint / reality-opts(public-key,short-id) / ws-opts 或 grpc-opts |
| trojan | password / sni / alpn / skip-cert-verify / network |
| naive | username / password / sni / alpn / skip-cert-verify |
- VLESS Reality 仍是 vless 类型，靠 `reality-opts` / `security=reality` 区分；URI 的 `type=ws/grpc` 归一为 `network`。
- 与 `kernel_probe.to_mihomo_proxy` 逐字一致，保证内核测活注入字段与订阅一致。

## 结构校验（有据，附出处）
- 两个订阅文件均以 `yaml.safe_load` 重解析（proxies/proxy-groups/rules 均为合法结构）：
{val_lines}
- 内容指纹（SHA-256，便于幂等比对）：
  - main.yaml：`{sha256_file(MAIN_PATH)}`
  - nekobox.json：`{sha256_file(NEKO_PATH)}`（应与 main.yaml 一致）
- **局限（如实注明）**：本机无 mihomo/sing-box 内核二进制，未做内核级配置校验（`-t` / `check`）；
  本报告仅证明 YAML 结构合法、两地址内容一致，不证明节点可在内核中实际连通。

## 节点 name 规则
- `US-{{type}}-{{server}}-{{port}}`，冲突追加序号，保证唯一可读。
- 输出节点列表：{', '.join(to_mihomo_proxy(n, nm)['name'] for n, nm in zip(kept, assign_names(kept))) or '（空）'}

## 空列表说明
- {empty_note}

## 合规声明
- 未修改 `.handoff/`；未覆盖他人产出（alive_nodes.json / us_nodes.json / nodes_raw.json / 其它 scripts 均未动）。
- 未写 token/PAT；未执行 push/发布/对外发送。
"""
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write(report)


def main() -> int:
    now = utc_now_iso()
    print(f"[build] 开始 {now}")

    nodes, _meta = load_alive_nodes()
    print(f"[build] 输入 alive_nodes {len(nodes)} 个，读取自 {ALIVE_PATH}")

    kept, rejected = filter_by_protocol(nodes)
    print(f"[build] 白名单过滤：保留 {len(kept)} / 拒绝 {len(rejected)}")

    names = assign_names(kept)
    clash_cfg = build_clash_config(names, kept)
    yaml_text = yaml.safe_dump(clash_cfg, allow_unicode=True, sort_keys=False)

    # 单格式：同一份 Clash YAML 写到两个订阅路径（nekobox.json 仅文件名沿用）
    for path in (MAIN_PATH, NEKO_PATH):
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(yaml_text)

    validation = validate_structures([MAIN_PATH, NEKO_PATH])
    identical = sha256_file(MAIN_PATH) == sha256_file(NEKO_PATH)
    write_report(now, input_count=len(nodes), kept=kept, rejected=rejected,
                 validation=validation)

    dist = collections.Counter(str(n.get("type", "")).strip().lower() for n in kept)
    print(f"[build] 协议分布：{dict(dist)}")
    print(f"[build] 结构校验：{validation}；两地址内容一致：{'是' if identical else '否'}")
    print(f"[build] 产出：{MAIN_PATH}")
    print(f"[build] 产出：{NEKO_PATH}")
    print(f"[build] 产出：{REPORT_PATH}")
    print(f"[build] 完成")
    return 0 if all(validation.values()) and identical else 1


if __name__ == "__main__":
    sys.exit(main())
