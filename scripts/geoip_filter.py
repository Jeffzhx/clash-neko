#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U3 —— GeoIP / 美国判定（基于 U2 产出的 nodes_raw.json）

依赖（带依赖的本地 venv 已安装）：
    pip install maxminddb pyyaml
    - maxminddb：读取 Country.mmdb（GeoLite2-Country），本单元必需
    - pyyaml：项目订阅解析链路依赖；本单元输入为 JSON，仅声明不直接调用

本地运行命令（脚本按 __file__ 推导项目根，任意 cwd 均可）：
    C:/Users/35637/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe scripts/geoip_filter.py

输入：
    <root>/nodes_raw.json    nodes 数组（U2 产出，只读）
    <root>/sources.json      仅背景（只读，不参与判定）
mmdb（固定，注意是 D: 盘不是 C: 盘）：
    D:/AI/2026-09-16-02-16-43/clash-nodes/kernel-test/Country.mmdb
输出：
    <root>/us_nodes.json
    <root>/probe/geoip-report.md
"""

from __future__ import annotations

import concurrent.futures
import datetime
import ipaddress
import json
import os
import re
import socket
import sys
import urllib.parse

import maxminddb

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# mmdb 路径可用环境变量 GEOIP_MMDB 覆盖（GitHub Actions 内下载到 CI 路径后设置），
# 未设置时回退到本机开发路径，保证本地复跑行为不变。
MMDB = os.environ.get("GEOIP_MMDB", "").strip() or r"D:/AI/2026-09-16-02-16-43/clash-nodes/kernel-test/Country.mmdb"
GOOD_TYPES = {"hysteria", "hysteria2", "anytls", "tuic", "vless", "trojan"}  # naive 已移除：mihomo 内核不支持
DNS_TIMEOUT = 4  # 单域名解析最长等待秒数；本机代理下曾卡死，必须设限
FQDN_RE = re.compile(
    r"^(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}$"
)
ISO2_RE = re.compile(r"^[A-Z]{2}$")

# 过滤原因分类
R_NON_US = "non_us_country"
R_UNKNOWN = "unknown"
R_INVALID = "invalid_server"
R_BAD_PROTO = "bad_protocol"


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def is_public_ip(ip) -> bool:
    """私有/回环/保留/组播/链路本地/未指定地址一律排除，不查 mmdb。"""
    return not (ip.is_private or ip.is_loopback or ip.is_reserved
                or ip.is_multicast or ip.is_link_local or ip.is_unspecified)


def parse_ip(text: str):
    try:
        return ipaddress.ip_address(text)
    except ValueError:
        return None


def lookup_cc(mmdb, ip_str: str) -> str:
    """查 mmdb，只接受 2 字母 ISO 码；country 非标准值（如 GOOGLE）回退 registered_country。"""
    try:
        rec = mmdb.get(ip_str) or {}
    except Exception:
        return ""
    if not isinstance(rec, dict):
        return ""
    for key in ("country", "registered_country"):
        section = rec.get(key) or {}
        if not isinstance(section, dict):
            continue
        code = str(section.get("iso_code") or "").strip().upper()
        if ISO2_RE.match(code):
            return code
    return ""


def resolve_with_timeout(host: str, timeout: int = DNS_TIMEOUT) -> list[str]:
    """socket.getaddrinfo 加超时：超时/失败返回空列表，绝不让脚本挂住。"""
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    try:
        future = executor.submit(
            socket.getaddrinfo, host, None, socket.AF_UNSPEC, socket.SOCK_STREAM
        )
        try:
            infos = future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            return []
        except Exception:
            return []
        ips: list[str] = []
        for info in infos or []:
            try:
                addr = info[4][0]
            except (IndexError, TypeError):
                continue
            if addr not in ips:
                ips.append(addr)
        return ips
    finally:
        # wait=False：即使底层 DNS 仍在阻塞，也不在这里等待
        executor.shutdown(wait=False, cancel_futures=True)


def classify(server: str, mmdb, cache: dict) -> tuple[str, str, str, str]:
    """返回 (cc, cc_basis, reason_class, detail)。"""
    raw = str(server or "").strip()
    if not raw:
        return "", R_INVALID, R_INVALID, "server 为空"

    # URL 编码垃圾：先 unquote；解码后仍非合法 hostname/IP 则排除
    if "%" in raw:
        decoded = urllib.parse.unquote(raw)
        if decoded == raw or not (parse_ip(decoded) or FQDN_RE.match(decoded)):
            return ("", R_INVALID, R_INVALID,
                    f"URL编码碎片：{raw!r} -> {decoded!r} 非合法 hostname/IP")
        raw = decoded

    host = raw.strip().strip("[]").lower()
    if not host:
        return "", R_INVALID, R_INVALID, "server 规范化后为空"

    if host in cache:
        return cache[host]

    ip = parse_ip(host)
    if ip is not None:
        if not is_public_ip(ip):
            result = ("", R_UNKNOWN, R_UNKNOWN, "私有/回环/保留 IP 段，排除")
        else:
            cc = lookup_cc(mmdb, str(ip))
            basis = "ipv6-literal" if ip.version == 6 else "ip-literal"
            if cc:
                result = (cc, basis, "" if cc == "US" else R_NON_US,
                          f"mmdb 命中 {str(ip)} -> {cc}")
            else:
                result = ("", basis, R_UNKNOWN,
                          f"mmdb 无有效 ISO 码（{str(ip)}），按 unknown 排除")
    elif not FQDN_RE.match(host):
        # README URI 解析出的碎片假 hostname（23c82941/150/linlin/c3a8753e/vpn/srv）
        # 不是合法域名，不做 DNS 解析，直接 unknown
        result = ("", R_UNKNOWN, R_UNKNOWN,
                  "非合法域名/IP（疑似 README URI 碎片），不解析 DNS")
    else:
        ips = resolve_with_timeout(host)
        if not ips:
            result = ("", R_UNKNOWN, R_UNKNOWN, "DNS 解析失败或超时")
        else:
            picked = None
            for cand in ips:
                cip = parse_ip(cand)
                if cip is not None and is_public_ip(cip):
                    picked = cip
                    break
            if picked is None:
                result = ("", R_UNKNOWN, R_UNKNOWN,
                          f"DNS 结果均为私有/保留 IP（{', '.join(ips)}）")
            else:
                cc = lookup_cc(mmdb, str(picked))
                if cc:
                    result = (cc, "domain-resolved",
                              "" if cc == "US" else R_NON_US,
                              f"解析到 {str(picked)} -> {cc}")
                else:
                    result = ("", "domain-resolved", R_UNKNOWN,
                              f"解析到 {str(picked)} 但 mmdb 无有效 ISO 码")

    cache[host] = result
    return result


def load_json(path: str, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def main() -> int:
    now = utc_now_iso()
    query_date = datetime.datetime.now().date().isoformat()  # 本地日期，与运行环境显示日期一致
    utc_date = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    print(f"[U3] 开始 {now}")

    raw_doc = load_json(os.path.join(PROJECT, "nodes_raw.json"), {})
    nodes = raw_doc.get("nodes", []) if isinstance(raw_doc, dict) else []
    if not isinstance(nodes, list):
        nodes = []
    src_doc = load_json(os.path.join(PROJECT, "sources.json"), {})
    src_count = len(src_doc.get("repos", [])) if isinstance(src_doc, dict) else 0

    mmdb = maxminddb.open_database(MMDB)
    try:
        meta = mmdb.metadata()
        meta_info = {
            "path": MMDB,
            "database_type": str(meta.database_type),
            "build_epoch": int(meta.build_epoch),
            "build_date": datetime.datetime.fromtimestamp(
                int(meta.build_epoch), datetime.timezone.utc
            ).isoformat(timespec="seconds"),
            "ip_version": int(meta.ip_version),
            "record_size": int(meta.record_size),
        }
        cache: dict = {}
        us_nodes = []
        filtered = []
        rows = []
        for idx, node in enumerate(nodes, 1):
            if not isinstance(node, dict):
                continue
            server = node.get("server", "")
            ntype = str(node.get("type", "")).lower()
            cc, basis, reason, detail = classify(str(server), mmdb, cache)
            node["cc"] = cc
            node["cc_basis"] = basis
            good_proto = ntype in GOOD_TYPES
            selected = bool(cc == "US" and good_proto)
            if not good_proto:
                reason = R_BAD_PROTO
                detail = (detail + "；" if detail else "") + f"协议 {ntype or '(空)'} 不在白名单"
            if selected:
                us_nodes.append(node)
            else:
                filtered.append({
                    "server": server,
                    "type": ntype,
                    "cc": cc,
                    "cc_basis": basis,
                    "reason": reason or R_UNKNOWN,
                    "detail": detail,
                })
            rows.append((idx, server, ntype, cc, basis, selected, detail))
            if idx % 10 == 0:
                print(f"  [{idx}/{len(nodes)}] {server} -> {cc or '-'}/{basis}")
    finally:
        mmdb.close()

    out = {
        "generated_at": now,
        "unit": "U3",
        "mmdb": meta_info,
        "query_date": query_date,
        "input_node_count": len(nodes),
        "us_node_count": len(us_nodes),
        "filtered_count": len(filtered),
        "good_protocols": sorted(GOOD_TYPES),
        "us_nodes": us_nodes,
        "filtered": filtered,
    }
    out_path = os.path.join(PROJECT, "us_nodes.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # 统计
    cc_dist: dict[str, int] = {}
    for r in rows:
        key = r[3] or "(unknown)"
        cc_dist[key] = cc_dist.get(key, 0) + 1
    reason_cnt: dict[str, int] = {}
    for item in filtered:
        reason_cnt[item["reason"]] = reason_cnt.get(item["reason"], 0) + 1

    reason_mean = {
        R_NON_US: "mmdb 命中但国家码非 US",
        R_UNKNOWN: "DNS失败/超时、URI碎片假域名、私有保留段、mmdb非标准ISO码",
        R_INVALID: "URL 编码垃圾 / 空 server，解码后仍非合法 hostname/IP",
        R_BAD_PROTO: f"type 不在 {'/'.join(sorted(GOOD_TYPES))} 白名单",
    }
    lines = [
        "# U3 GeoIP / 美国判定报告", "",
        f"- 生成时间：{now}",
        f"- 查询日期：{query_date}（本地）；UTC {utc_date}",
        f"- 输入：`nodes_raw.json`（{len(nodes)} 节点）；背景：`sources.json`（{src_count} 个低星来源）",
        f"- mmdb 路径：`{MMDB}`",
        f"- mmdb 版本元数据：database_type={meta_info['database_type']}；"
        f"build_epoch={meta_info['build_epoch']}（{meta_info['build_date']}）；"
        f"ip_version={meta_info['ip_version']}；record_size={meta_info['record_size']}",
        f"- 优质协议白名单：{', '.join(sorted(GOOD_TYPES))}",
        f"- 结果：**US 优质节点 {len(us_nodes)}** / 输入 {len(nodes)} / 过滤 {len(filtered)}", "",
        "## 逐节点判定（server / type / cc / cc_basis / 是否入选）", "",
        "| # | server | type | cc | cc_basis | 是否入选 | 说明 |",
        "|---|--------|------|----|----------|----------|------|",
    ]
    for idx, server, ntype, cc, basis, selected, detail in rows:
        lines.append(
            f"| {idx} | `{server}` | {ntype} | {cc or '-'} | {basis or '-'} | "
            f"{'是' if selected else '否'} | {detail} |"
        )
    lines += [
        "", "## 按 cc 分布统计", "",
        "| cc | 节点数 |", "|----|--------|",
    ]
    for cc, cnt in sorted(cc_dist.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {cc} | {cnt} |")
    lines += [
        "", "## 过滤原因分类计数", "",
        "| 原因类别 | 数量 | 含义 |", "|----------|------|------|",
    ]
    for reason, cnt in sorted(reason_cnt.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {reason} | {cnt} | {reason_mean.get(reason, '')} |")
    if not reason_cnt:
        lines.append("| （无） | 0 | - |")

    url_frag_counts: dict[str, int] = {}
    for item in filtered:
        if item["cc_basis"] == R_INVALID and "%2f" in str(item["server"]).lower():
            key = str(item["server"])
            url_frag_counts[key] = url_frag_counts.get(key, 0) + 1
    lines += ["", "## URL 编码碎片节点（单独点名）", ""]
    if url_frag_counts:
        for server, count in url_frag_counts.items():
            lines.append(
                f"- `{server}` → 解码后 `{urllib.parse.unquote(server)}`，"
                f"非合法 hostname/IP，cc_basis=invalid_server，共 {count} 处，全部排除"
            )
    else:
        lines.append("- 本次输入未发现 URL 编码碎片节点。")
    lines += [
        "", "## 判定规则与依据", "",
        "- IP 字面量（IPv4/IPv6）：`ipaddress` 识别 → 私有/回环/保留段直接排除 → "
        "其余查 mmdb，`country.iso_code` 回退 `registered_country`。",
        "- 域名：仅对合法 FQDN 做 `socket.getaddrinfo`，用 ThreadPoolExecutor + "
        f"future.result(timeout={DNS_TIMEOUT}s) 防卡死；超时/失败按 unknown；多 IP 取首个公网 IP。",
        "- mmdb 非标准 ISO 码（如 8.8.8.8 返回 `GOOGLE`）不认定为 US，按 unknown 排除。",
        "- README URI 解析出的碎片假 hostname（如 `23c82941`/`150`/`linlin`/"
        "`c3a8753e`/`vpn`/`srv`）不是合法域名，不做 DNS 解析，按 unknown 排除。",
        "- URL 含 `%XX` 的 server 先 `urllib.parse.unquote`；解码后仍非合法 hostname/IP 判 invalid_server。",
        f"- 入选红线：`cc == \"US\"` 且 `type ∈ {{{', '.join(sorted(GOOD_TYPES))}}}`。", "",
        f"产出：`us_nodes.json`（US 节点 {len(us_nodes)}）+ 本报告。",
    ]
    report_path = os.path.join(PROJECT, "probe", "geoip-report.md")
    with open(report_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[U3] 完成：输入 {len(nodes)} / US {len(us_nodes)} / 过滤 {len(filtered)}")
    print(f"[U3] 产出：{out_path}")
    print(f"[U3] 产出：{report_path}")
    return 0


if __name__ == "__main__":
    _code = main()
    # 保底：DNS 底层线程若仍在阻塞，避免解释器退出时被非 daemon 线程拖住
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(_code)
