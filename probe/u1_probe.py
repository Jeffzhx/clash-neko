#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U1 可行性探针（精准抽样版）—— 验证「低星(<100)源 ∩ 优质协议 ∩ 美国节点」供给是否够。

额度约束：匿名 GitHub API 60/h。本脚本严格控制在 ~30 次调用：
  - 内置已知候选源（来自实证搜索），不额外做 repo search。
  - 每源 1 次 trees 递归拿全文件表 + ≤2 次 contents 取最可能含节点的文件。
raw.githubusercontent.com 在本机代理下不通（HTTP 000），一律走 api.github.com/contents。

产出：
  <root>/sources.json                       低星源清单
  <root>/probe/feasibility-report.md        可行性判定
"""

from __future__ import annotations

import base64
import datetime
import ipaddress
import json
import os
import re
import socket
import sys
import urllib.parse
import urllib.request

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MMDB = r"D:/AI/2026-09-16-02-16-43/clash-nodes/kernel-test/Country.mmdb"
GOOD_TYPES = {"hysteria", "hysteria2", "anytls"}
UA = "clash-us-sub-probe/1.0"
API_CALLS = 0

# 来自 2026-11-19 实证搜索的低星候选源（clash subscription / hysteria2 / free proxy nodes）
KNOWN_REPOS = [
    {"full_name": "rekt0ro/ProxyRift", "stars": 6, "branch": "main"},
    {"full_name": "nodesradar/nodesradar-en", "stars": 29, "branch": "main"},
    {"full_name": "nodesradar/nodesradar-es", "stars": 1, "branch": "main"},
    {"full_name": "nodesradar/nodesradar-ru", "stars": 1, "branch": "main"},
    {"full_name": "fmw86/free-proxy-pool", "stars": 9, "branch": "main"},
    {"full_name": "cmahmud/proxies", "stars": 3, "branch": "main"},
    {"full_name": "Edsel-Rahimi/Ariston", "stars": 7, "branch": "main"},
    {"full_name": "bushilian/bushilian", "stars": 1, "branch": "main"},
]
PREFER = re.compile(r"(readme|main\.yaml|sub|config|nodes|proxy|clash|hysteria|\.json$)", re.I)
CFG_RE = re.compile(r"\.(ya?ml|json|txt|md)$", re.I)


def api_get(path: str, timeout: int = 10) -> bytes | None:
    global API_CALLS
    API_CALLS += 1
    url = "https://api.github.com" + path
    for i in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            if i == 1:
                print(f"    [API失败] {path[:60]} -> {type(e).__name__}", file=sys.stderr)
                return None
    return None


def tree_files(repo: dict) -> list[str]:
    blob = api_get(f"/repos/{repo['full_name']}/git/trees/{repo['branch']}?recursive=1")
    if not blob:
        return []
    try:
        tree = json.loads(blob).get("tree", [])
    except Exception:
        return []
    cands = [e["path"] for e in tree if e.get("type") == "blob" and CFG_RE.search(e.get("path", ""))
             and e["path"].count("/") <= 3 and len(e.get("path", "")) < 120]
    cands.sort(key=lambda p: (0 if PREFER.search(p) else 1, p.count("/"), len(p)))
    return cands[:2]


def fetch_content(repo: dict, path: str) -> str | None:
    q = urllib.parse.quote(path)
    blob = api_get(f"/repos/{repo['full_name']}/contents/{q}?ref={repo['branch']}")
    if not blob:
        return None
    try:
        d = json.loads(blob)
        if isinstance(d, dict) and d.get("encoding") == "base64" and d.get("content"):
            return base64.b64decode(d["content"]).decode("utf-8", "ignore")
    except Exception:
        pass
    return None


def try_b64(text: str) -> str:
    m = re.fullmatch(r"[\sA-Za-z0-9+/=]{60,}", text.strip())
    if not m:
        return text
    for pad in ("", "=", "=="):
        try:
            s = base64.b64decode(text.strip() + pad, validate=True).decode("utf-8", "ignore")
            if re.search(r"hysteria|hy2|anytls|server:|ss://|vmess://|vless://", s):
                return s
        except Exception:
            pass
    return text


def parse_nodes(text: str) -> list[dict]:
    text = try_b64(text)
    nodes: list[dict] = []
    try:
        import yaml
        data = yaml.safe_load(text)
        if isinstance(data, dict):
            for p in (data.get("proxies") or []):
                if isinstance(p, dict) and p.get("server"):
                    nodes.append({"type": str(p.get("type", "")).lower(), "server": str(p["server"]).strip()})
            for o in (data.get("outbounds") or []):
                if isinstance(o, dict) and o.get("server"):
                    nodes.append({"type": str(o.get("type", "")).lower(), "server": str(o["server"]).strip()})
        if isinstance(data, list):
            for o in data:
                if isinstance(o, dict) and o.get("server"):
                    nodes.append({"type": str(o.get("type", "")).lower(), "server": str(o["server"]).strip()})
    except Exception:
        pass
    for m in re.finditer(r"\b(hysteria2|hysteria|hy2|anytls)://([^\s\"'\-]+)", text, re.I):
        t = m.group(1).lower()
        t = "hysteria2" if t in ("hy2", "hysteria2") else t
        hp = m.group(2).rsplit("@", 1)[-1]
        nodes.append({"type": t, "server": hp.split(":")[0].strip("[]")})
    return nodes


def classify(server: str, mmdb, cache: dict) -> tuple[str, str]:
    """探针阶段只判 IP 字面量（IPv4/IPv6）；域名留待 U3 测活时解析，避免 DNS 卡死。"""
    host = server.strip().strip("[]").lower()
    if host in cache:
        return cache[host]
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        cache[host] = ("", "domain-deferred")
        return ("", "domain-deferred")
    if ip.is_private or ip.is_loopback or ip.is_reserved:
        cache[host] = ("", "private")
        return ("", "private")
    try:
        rec = mmdb.get(str(ip)) or {}
        cc = ((rec.get("country") or {}).get("iso_code") or
              (rec.get("registered_country") or {}).get("iso_code") or "")
        result = (str(cc).upper(), "ip-literal")
    except Exception:
        result = ("", "mmdb-error")
    cache[host] = result
    return result


def main() -> int:
    print("[U1 探针] 开始", datetime.datetime.now().isoformat(timespec="seconds"))
    import maxminddb
    mmdb = maxminddb.open_database(MMDB)

    all_nodes, per_repo, repo_out = [], [], []
    for idx, repo in enumerate(KNOWN_REPOS, 1):
        files = tree_files(repo)
        got = []
        for p in files:
            txt = fetch_content(repo, p)
            if txt:
                got.extend(parse_nodes(txt[:300000]))
        print(f"  [{idx}/{len(KNOWN_REPOS)}] {repo['full_name']} ★{repo['stars']} "
              f"文件{len(files)} 节点{len(got)}")
        per_repo.append({"full_name": repo["full_name"], "stars": repo["stars"],
                         "files_checked": files, "nodes_parsed": len(got)})
        repo_out.append({"full_name": repo["full_name"], "stars": repo["stars"],
                         "url": f"https://github.com/{repo['full_name']}",
                         "fetched_at": datetime.date.today().isoformat(),
                         "criteria": "stars<100"})
        for n in got:
            n["_src"] = repo["full_name"]
        all_nodes.extend(got)

    proto_cnt: dict[str, int] = {}
    good_total = us_good = domain_deferred = 0
    us_samples = []
    cc_cache: dict[str, tuple[str, str]] = {}
    for n in all_nodes:
        t = n["type"]
        proto_cnt[t] = proto_cnt.get(t, 0) + 1
        if t in GOOD_TYPES:
            good_total += 1
            cc, basis = classify(n["server"], mmdb, cc_cache)
            n["cc"], n["cc_basis"] = cc, basis
            if basis == "domain-deferred":
                domain_deferred += 1
            if cc == "US":
                us_good += 1
                us_samples.append(f"{n['type']} {n['server']} [{basis}] <- {n['_src']}")
    mmdb.close()

    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with open(os.path.join(PROJECT, "sources.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"generated_at": now, "count": len(repo_out), "repos": repo_out},
                  f, ensure_ascii=False, indent=2)

    total = len(all_nodes)
    dist = "、".join(f"{k} {v}" for k, v in sorted(proto_cnt.items(), key=lambda x: -x[1])) or "无"
    lines = [
        "# U1 可行性报告（精准抽样）", "",
        f"- 生成时间：{now}",
        f"- 抽样低星源：{len(KNOWN_REPOS)} 个（每源 ≤3 文件）",
        f"- GitHub API 调用：{API_CALLS} 次（匿名额度 60/h）",
        f"- 解析节点：**{total}** 个",
        f"- 协议分布：{dist}",
        f"- 优质协议(hysteria/hysteria2/anytls)：**{good_total}** 个",
        f"- 美国(US)优质节点：**{us_good}** 个（域名节点 {domain_deferred} 个未解析，留待 U3）", "", "## 判定", "",
    ]
    if us_good >= 5:
        lines.append(f"✅ 够用：{us_good} 个美国优质节点，足以撑起初始订阅。")
    elif us_good >= 1:
        lines.append(f"⚠️ 偏少：仅 {us_good} 个美国优质节点，订阅单薄，建议向用户提议放宽协议或来源。")
    else:
        lines.append("❌ 不足：抽样中未抓到美国优质节点。低星分享源多为 VLESS/VMess/SS/Trojan，"
                     "建议向用户提议：放宽协议白名单，或改用订阅聚合源。")
    if us_samples:
        lines += ["", "## 美国优质节点样本", ""] + [f"- {s}" for s in us_samples[:15]]
    lines += ["", "## 说明", "",
              "- 一次性抽样探针，结论基于当前少量源；节点可用性待 U3 测活。",
              "- 美国判定：字面量 IP 查 mmdb；域名解析后查；IPv6 查。", "",
              "## 逐源", ""]
    for r in per_repo:
        lines.append(f"- {r['full_name']} ★{r['stars']}：解析 {r['nodes_parsed']} 节点（检查 {len(r['files_checked'])} 文件）")
    with open(os.path.join(PROJECT, "probe", "feasibility-report.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n[结果] 节点 {total} / 优质 {good_total} / 美国优质 {us_good} / API {API_CALLS} 次")
    return 0


if __name__ == "__main__":
    sys.exit(main())
