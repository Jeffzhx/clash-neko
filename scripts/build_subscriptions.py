#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U5 —— 双格式订阅输出（main.yaml mihomo/Clash Verge + nekobox.json sing-box/NekoBox）

用法（脚本按 __file__ 推导项目根，任意 cwd 均可运行）：
    C:/Users/35637/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe scripts/build_subscriptions.py

输入（只读，绝不覆盖）：
    <root>/alive_nodes.json    U4 产出的 alive_nodes 数组

输出（覆盖写本单元自己的产物，不动他人文件）：
    <root>/main.yaml
    <root>/nekobox.json
    <root>/probe/subscription-build-report.md

设计要点：
    1. 红线：只输出 type ∈ {hysteria, hysteria2, anytls} 的节点；其它协议一律过滤并在报告登记。
    2. 同一份过滤后的节点列表同时生成两份订阅，保证两格式节点集合完全一致。
    3. 空输入（alive_nodes=[]）也产出合法订阅：YAML proxies=[] + 基础 group；JSON 仅 direct+block。
    4. 本单元只做结构校验（yaml.safe_load / json.load），本机无 mihomo/sing-box 内核，
       不做内核级 `-t` 校验，报告如实注明该局限。
    5. 不伪造节点、不塞入 unknown/dead 节点；缺失的非身份配置字段（如 hysteria up/down）
       使用保守占位默认值并在报告"字段映射说明"中标注。
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

# 红线：仅收三种优质协议
ALLOWED_PROTOCOLS = ("hysteria", "hysteria2", "anytls")

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
    # 只保留 dict 项，避免脏数据导致后续崩溃
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
                    "reason": "type 不在白名单 {hysteria,hysteria2,anytls}",
                }
            )
    return kept, rejected


def assign_names(nodes: list[dict]) -> list[str]:
    """生成唯一可读的 name/tag：US-{type}-{server}-{port}，冲突追加序号。"""
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


def to_mihomo_proxy(node: dict, name: str) -> dict:
    """把一个节点映射为 mihomo/Clash Verge proxy（按协议分支，兼容字段别名）。"""
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

    return proxy


def to_singbox_outbound(node: dict, name: str) -> dict:
    """把一个节点映射为 sing-box/NekoBox outbound（按协议分支，兼容字段别名）。"""
    ntype = str(node.get("type", "")).strip().lower()
    server = str(node.get("server", "")).strip()
    port = int(node.get("port", 443) or 443)
    sni = _first(node, "sni", "server_name", "host", default="")
    server_name = sni or server  # sni 为空时用 server 作 SNI 保守占位
    skip = bool(node.get("skip-cert-verify", True))
    obfs = _obfs_of(node)

    outbound: dict = {"type": ntype, "tag": name, "server": server, "server_port": port}
    tls = {"enabled": True, "server_name": server_name, "insecure": skip}

    if ntype == "hysteria2":
        outbound["auth_str"] = _first(node, "auth", "password", "auth_str")
        if sni:
            outbound["sni"] = sni
        if obfs:
            outbound["obfs"] = {"type": "salamander", "password": obfs}
        outbound["tls"] = tls

    elif ntype == "hysteria":
        outbound["auth_str"] = _first(node, "auth", "auth_str", "password")
        outbound["up"] = _first(node, "up", default=DEFAULT_UP)
        outbound["down"] = _first(node, "down", default=DEFAULT_DOWN)
        if obfs:
            outbound["obfs"] = {"type": "salamander", "password": obfs}
        outbound["tls"] = tls

    elif ntype == "anytls":
        outbound["password"] = _first(node, "password", "auth", "auth_str")
        outbound["tls"] = tls

    return outbound


def build_mihomo_config(names: list[str], nodes: list[dict]) -> dict:
    """组装 mihomo 配置：proxies / proxy-groups / rules。空输入时 proxies=[] 仍合法。"""
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


def build_singbox_config(names: list[str], nodes: list[dict]) -> dict:
    """组装 sing-box 配置：outbounds / dns / route。空输入时 outbounds 仅 direct+block。"""
    node_outbounds = [to_singbox_outbound(node, name) for node, name in zip(nodes, names)]
    outbounds = [
        {"type": "direct", "tag": "direct"},
        {"type": "block", "tag": "block"},
    ] + node_outbounds
    return {
        "outbounds": outbounds,
        "dns": {
            "servers": [
                {"tag": "dns-local", "type": "udp", "server": "223.5.5.5"},
            ],
            "rules": [],
        },
        "route": {
            "rules": [],
            "default": "direct",
        },
    }


def check_consistency(mihomo_cfg: dict, neko_cfg: dict) -> dict:
    """校验两格式节点集合一致性：数量 / name↔tag / server:port 集合。空对空算一致。"""
    mp = mihomo_cfg["proxies"]
    so = [o for o in neko_cfg["outbounds"] if o.get("type") in ALLOWED_PROTOCOLS]

    names_m = [p["name"] for p in mp]
    tags_s = [o["tag"] for o in so]
    sp_m = sorted(f'{p["server"]}:{p["port"]}' for p in mp)
    sp_s = sorted(f'{o["server"]}:{o["server_port"]}' for o in so)

    count_ok = len(mp) == len(so)
    name_ok = names_m == tags_s
    sp_ok = sp_m == sp_s
    return {
        "mihomo_count": len(mp),
        "singbox_count": len(so),
        "names_mihomo": names_m,
        "tags_singbox": tags_s,
        "server_port_mihomo": sp_m,
        "server_port_singbox": sp_s,
        "count_ok": count_ok,
        "name_ok": name_ok,
        "server_port_ok": sp_ok,
        "consistent": count_ok and name_ok and sp_ok,
    }


def validate_structures(mihomo_cfg: dict, neko_cfg: dict) -> dict:
    """结构校验：重新 safe_load / json.load 自己的产物，确认可解析且关键字段存在。"""
    with open(MAIN_PATH, "r", encoding="utf-8") as fh:
        reparsed_yaml = yaml.safe_load(fh)
    with open(NEKO_PATH, "r", encoding="utf-8") as fh:
        reparsed_json = json.load(fh)

    yaml_ok = (
        isinstance(reparsed_yaml, dict)
        and isinstance(reparsed_yaml.get("proxies"), list)
        and isinstance(reparsed_yaml.get("proxy-groups"), list)
        and isinstance(reparsed_yaml.get("rules"), list)
    )
    json_ok = (
        isinstance(reparsed_json, dict)
        and isinstance(reparsed_json.get("outbounds"), list)
        and isinstance(reparsed_json.get("dns"), dict)
        and isinstance(reparsed_json.get("route"), dict)
        and reparsed_json.get("route", {}).get("default") == "direct"
    )
    return {"yaml_parse_ok": yaml_ok, "json_parse_ok": json_ok}


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_report(now: str, *, input_count: int, kept: list[dict], rejected: list[dict],
                 consistency: dict, validation: dict) -> None:
    """覆盖写报告，含输入/输出计数、协议分布、一致性、字段映射、校验局限、空列表说明。"""
    dist = collections.Counter(str(n.get("type", "")).strip().lower() for n in kept)
    dist_lines = "\n".join(f"  - {k}: {v}" for k, v in sorted(dist.items())) or "  - （无）"
    rejected_lines = "\n".join(
        f"  - type={r['type']} server={r['server']} port={r['port']} —— {r['reason']}"
        for r in rejected
    ) or "  - （无，输入未混入非白名单协议）"

    empty_note = (
        "当前 alive_nodes=[]，按红线生成**合法空订阅**（YAML proxies=[]、JSON 仅 direct+block），"
        "这是合法结果，不是错误；本单元未塞入 unknown/dead 节点、未编造节点。"
        if input_count == 0 and not kept
        else "输入非空，按节点字段一一映射输出。"
    )

    consistent = consistency["consistent"]
    verdict = "一致 ✅" if consistent else "不一致 ❌"
    report = f"""# U5 双格式订阅构建报告（覆盖写，不追加）

- 生成时间：{now}
- 输入文件：`{ALIVE_PATH}`
- 输入节点数（alive_nodes）：{input_count}
- 输出节点数：{len(kept)}（白名单过滤后）
- 被过滤节点数：{len(rejected)}
- 协议分布（输出）：
{dist_lines}

## 白名单过滤（红线）
- 仅输出 type ∈ {{hysteria, hysteria2, anytls}}；其它协议过滤并登记：
{rejected_lines}

## 两格式一致性校验
- 同一份过滤后的节点列表同时生成 main.yaml 与 nekobox.json。
- mihomo 节点数：{consistency['mihomo_count']}；sing-box 节点数：{consistency['singbox_count']}（数量{'一致' if consistency['count_ok'] else '不一致'}）
- name ↔ tag 顺序/取值一致：{'是' if consistency['name_ok'] else '否'}
- server:port 集合一致：{'是' if consistency['server_port_ok'] else '否'}
- **结论：{verdict}**（空对空亦计为一致）
- 节点 name/tag 列表：{', '.join(consistency['names_mihomo']) if consistency['names_mihomo'] else '（空）'}

## 结构校验方式（有据，附出处）
- main.yaml：`yaml.safe_load` 重解析 → {'通过' if validation['yaml_parse_ok'] else '失败'}（proxies/proxy-groups/rules 均为合法结构）
- nekobox.json：`json.load` 重解析 → {'通过' if validation['json_parse_ok'] else '失败'}（outbounds/dns/route 均为合法结构，route.default=direct）
- 内容指纹（SHA-256，便于幂等比对）：
  - main.yaml：`{sha256_file(MAIN_PATH)}`
  - nekobox.json：`{sha256_file(NEKO_PATH)}`
- **局限（如实注明）**：本机无 mihomo/sing-box 内核二进制，未做内核级配置校验（`-t` / `check`）；
  本报告仅证明 YAML/JSON 结构合法、两格式节点集合一致，不证明节点可在内核中实际连通用。

## 字段映射说明
| 协议 | mihomo proxy 字段 | sing-box outbound 字段 |
| --- | --- | --- |
| hysteria2 | name,type,server,port,auth,sni,skip-cert-verify,obfs(如有) | type,tag,server,server_port,auth_str,sni,tls{{enabled,server_name,insecure}},obfs(如有→salamander) |
| hysteria | name,type,server,port,auth,obfs(如有),protocol(默认udp),sni,skip-cert-verify,up,down | type,tag,server,server_port,auth_str,up,down,tls{{...}},obfs(如有→salamander) |
| anytls | name,type,server,port,password,sni,skip-cert-verify | type,tag,server,server_port,password,tls{{...}} |

- 字段兼容：auth/password/auth_str 互为别名；sni/server_name/host 互为别名；tls.server_name 在 sni 为空时退化为 server；tls.insecure 跟随 skip-cert-verify（默认 true）。
- 占位默认值：hysteria 的 up/down 缺失时填 `{DEFAULT_UP}` / `{DEFAULT_DOWN}`（推断，非节点真实性数据，仅保证配置可用）。
- name 规则：`US-{{type}}-{{server}}-{{port}}`，冲突追加序号，保证唯一可读。

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
    print(f"[U5] 开始 {now}")

    nodes, _meta = load_alive_nodes()
    print(f"[U5] 输入 alive_nodes {len(nodes)} 个，读取自 {ALIVE_PATH}")

    kept, rejected = filter_by_protocol(nodes)
    print(f"[U5] 白名单过滤：保留 {len(kept)} / 拒绝 {len(rejected)}")

    names = assign_names(kept)
    mihomo_cfg = build_mihomo_config(names, kept)
    neko_cfg = build_singbox_config(names, kept)

    # 覆盖写本单元自己的产物
    with open(MAIN_PATH, "w", encoding="utf-8") as fh:
        yaml.safe_dump(mihomo_cfg, fh, allow_unicode=True, sort_keys=False)
    with open(NEKO_PATH, "w", encoding="utf-8") as fh:
        json.dump(neko_cfg, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    consistency = check_consistency(mihomo_cfg, neko_cfg)
    validation = validate_structures(mihomo_cfg, neko_cfg)
    write_report(now, input_count=len(nodes), kept=kept, rejected=rejected,
                 consistency=consistency, validation=validation)

    dist = collections.Counter(str(n.get("type", "")).strip().lower() for n in kept)
    print(f"[U5] 协议分布：{dict(dist)}")
    print(f"[U5] 一致性：{'通过' if consistency['consistent'] else '失败'}；"
          f"结构校验：YAML={'OK' if validation['yaml_parse_ok'] else 'FAIL'} "
          f"JSON={'OK' if validation['json_parse_ok'] else 'FAIL'}")
    print(f"[U5] 产出：{MAIN_PATH}")
    print(f"[U5] 产出：{NEKO_PATH}")
    print(f"[U5] 产出：{REPORT_PATH}")
    print(f"[U5] 完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
