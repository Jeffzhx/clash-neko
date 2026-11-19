#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U2 低星源发现 + 抓取模块（正式版）

环境依赖：
  - Python 3.9+
  - pyyaml（PyYAML）：解析订阅/配置里的 yaml proxies / outbounds
  - HTTP 仅用标准库 urllib，无需 requests

本地运行（使用已装 pyyaml 的 venv）：
  C:/Users/35637/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe scripts/fetch_sources.py

GitHub Actions 中需先安装依赖再运行：
  pip install pyyaml
  python scripts/fetch_sources.py

设计要点：
  - 源来自 <root>/sources.json 的 repos（full_name；branch 缺省 main），代码不硬编码源。
  - 只走 https://api.github.com；raw.githubusercontent.com 在本机代理下 HTTP 000 不通，绝不使用。
  - token 只从环境变量 GITHUB_TOKEN 读取：存在则加 Authorization: Bearer 头（额度 5000/h），
    否则匿名。token 绝不打印、绝不写文件、绝不进入异常信息。
  - 每个 contents/tree 响应按 repo+path 缓存到 <root>/.cache/，重跑命中缓存不再请求 GitHub
    （匿名场景也能靠缓存规避 60/h 限额）。
  - 源间并发抓取（ThreadPoolExecutor）；单源失败不影响其他源；有限重试 + 10s 超时；
    网络 IncompleteRead 时从已读部分抢救 base64 内容作为兜底。
  - 文件优先级：订阅/节点文件优先，README 最后（避免 README 挤占订阅文件名额）。
  - 解析复用 probe/u1_probe.py 已验证的 try_b64（直接 import）与同一套 URI 正则，
    扩展为统一节点结构：type / server / port / 协议专有字段(原始 proxy dict 原样保留) / _src / _file。
  - 只保留优质协议 hysteria / hysteria2 / anytls（红线）。
  - 不做 GeoIP / 美国判定，server 原样保留；cc / cc_basis 留空占位供 U3 填充。
  - 产出 <root>/nodes_raw.json。
"""

from __future__ import annotations

import base64
import concurrent.futures
import datetime
import hashlib
import http.client
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(PROJECT, ".cache")
SOURCES = os.path.join(PROJECT, "sources.json")
OUTPUT = os.path.join(PROJECT, "nodes_raw.json")

# 复用 probe/u1_probe.py 里已验证的 base64 解码逻辑，避免重造
_PROBE_DIR = os.path.join(PROJECT, "probe")
if _PROBE_DIR not in sys.path:
    sys.path.insert(0, _PROBE_DIR)
from u1_probe import try_b64  # noqa: E402

GOOD_TYPES = {"hysteria", "hysteria2", "anytls"}
UA = "clash-us-sub-fetcher/2.0"
MAX_RETRY = 10
TIMEOUT = 10
MAX_FILES_PER_REPO = 3
MAX_DOWNLOAD = 2_000_000      # GitHub contents API 单文件上限约 1MB，base64 膨胀后留足余量
MAX_WORKERS = 4
MAX_BYTES = 300000
# 订阅/节点类文件优先；README 最后（README 常无节点或只有示例链接）
SUB_PREFER = re.compile(r"(subscription|sub/|sub\.|all\.txt|node|proxy|clash|hysteria|anytls|\.ya?ml$|\.json$)", re.I)
README_RE = re.compile(r"(^|/)readme", re.I)
CFG_RE = re.compile(r"\.(ya?ml|json|txt|md)$", re.I)
# 与 u1_probe.py 一致的 URI 正则（复用已验证逻辑）
URI_RE = re.compile(r"\b(hysteria2|hysteria|hy2|anytls)://([^\s\"'\-]+)", re.I)

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
API_CALLS = 0
CACHE_HITS = 0
_COUNTER_LOCK = threading.Lock()


def log(msg: str) -> None:
    print(msg, flush=True)


# ------------------------------ 缓存 ------------------------------
def _cache_key(kind: str, *parts: str) -> str:
    raw = "|".join([kind, *parts])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest() + ".json"


def _cache_get(key: str):
    global CACHE_HITS
    path = os.path.join(CACHE_DIR, key)
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = json.load(f)
        with _COUNTER_LOCK:
            CACHE_HITS += 1
        return doc.get("data")
    except Exception:
        return None


def _cache_set(key: str, data) -> None:
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, key)
    tmp = path + ".tmp"
    doc = {
        "cached_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "key": key,
        "data": data,
    }
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, ensure_ascii=False)
    os.replace(tmp, path)


# ------------------------------ HTTP ------------------------------
def _extract_content_text(blob: bytes):
    """从 contents API 响应（完整 JSON 或 IncompleteRead 截断片段）中提取订阅原文。"""
    # 优先：完整 JSON
    try:
        d = json.loads(blob)
        if isinstance(d, dict) and d.get("encoding") == "base64" and d.get("content"):
            return base64.b64decode(d["content"]).decode("utf-8", "ignore")
    except Exception:
        pass
    # 回退：从截断 JSON 中用正则抢救 "content" 字段的 base64
    m = re.search(rb'"content"\s*:\s*"([A-Za-z0-9+/=\\n]+)', blob)
    if m:
        b64 = m.group(1).replace(b"\\n", b"").replace(b"\n", b"")
        b64 = b64[: len(b64) // 4 * 4]
        if len(b64) >= 64:
            try:
                return base64.b64decode(b64).decode("utf-8", "ignore")
            except Exception:
                pass
    # 最后：blob 本身已是解码原文
    try:
        s = blob.decode("utf-8", "ignore")
        if s and ("://" in s or "server:" in s or "proxies" in s):
            return s
    except Exception:
        pass
    return None


def api_get(path: str):
    """GET https://api.github.com + path，返回 bytes 或 None。有限重试，报错信息不含 token。"""
    global API_CALLS
    with _COUNTER_LOCK:
        API_CALLS += 1
    url = "https://api.github.com" + path
    headers = {
        "User-Agent": UA,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN  # 仅在内存中使用，不打印/落盘
    for attempt in range(1, MAX_RETRY + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.read(MAX_DOWNLOAD)
        except http.client.IncompleteRead as e:
            # 本机代理下长响应常被截断；最后一次失败时把已读片段交给解析器抢救 content
            if attempt == MAX_RETRY:
                if e.partial and b'"content"' in e.partial:
                    return e.partial
                log(f"    [API失败] IncompleteRead {path[:70]}")
                return None
            time.sleep(min(0.3 * attempt, 1.2))
        except urllib.error.HTTPError as e:
            code = e.code
            if attempt == MAX_RETRY:
                log(f"    [API失败] HTTP {code} {path[:70]}")
                return None
            if code in (403, 429) or code >= 500:
                time.sleep(min(0.3 * attempt, 1.2))
                continue
            return None  # 404/400 等无需重试
        except Exception as e:
            if attempt == MAX_RETRY:
                log(f"    [API失败] {type(e).__name__} {path[:70]}")
                return None
            time.sleep(min(0.3 * attempt, 1.2))
    return None


def _pick_files(cands: list) -> list:
    """按优先级排序候选文件并截断（订阅/节点文件优先，README 最后）。"""
    def rank(p: str) -> int:
        if SUB_PREFER.search(p):
            return 0
        if README_RE.search(p):
            return 2
        return 1

    ordered = sorted(cands, key=lambda p: (rank(p), p.count("/"), len(p)))
    return ordered[:MAX_FILES_PER_REPO]


def tree_files(full_name: str, branch: str):
    """返回候选文件路径列表；None 表示整源失败（tree 请求失败）。命中缓存不请求。"""
    key = _cache_key("tree_v2", full_name, branch)  # v2：缓存未排序的完整候选，读取时再按当前策略挑选
    cached = _cache_get(key)
    if cached is not None:
        return _pick_files(cached)
    blob = api_get(f"/repos/{full_name}/git/trees/{branch}?recursive=1")
    if blob is None:
        return None
    try:
        tree = json.loads(blob).get("tree", [])
    except Exception:
        return []
    cands = [
        e["path"] for e in tree
        if e.get("type") == "blob"
        and CFG_RE.search(e.get("path", ""))
        and e["path"].count("/") <= 3
        and len(e.get("path", "")) < 120
    ]
    cands.sort()  # 稳定基准顺序后缓存，挑选逻辑与缓存解耦
    _cache_set(key, cands)
    return _pick_files(cands)


def fetch_content(full_name: str, branch: str, path: str):
    """返回解码文本；None 表示失败或无内容。命中缓存不请求。"""
    key = _cache_key("content", full_name, branch, path)
    cached = _cache_get(key)
    if cached is not None:
        return cached
    q = urllib.parse.quote(path)
    blob = api_get(f"/repos/{full_name}/contents/{q}?ref={branch}")
    if blob is None:
        return None
    text = _extract_content_text(blob)
    if text is None:
        return None
    _cache_set(key, text)
    return text


# ------------------------------ 解析（扩展 u1_probe） ------------------------------
def _extract_port(port_val, hostport: str = ""):
    if port_val not in (None, ""):
        try:
            return int(port_val)
        except (TypeError, ValueError):
            return port_val
    tail = hostport.split("?", 1)[0].split("#", 1)[0]
    if tail.startswith("["):
        m = re.search(r"\]:(\d+)", tail)
        if m:
            return int(m.group(1))
    elif ":" in tail:
        p = tail.rsplit(":", 1)[1]
        if p.isdigit():
            return int(p)
    return ""


def _uri_extras(raw: str) -> dict:
    """从 hysteria/hy2/anytls URI 提取协议专有字段，供 U5 组配置用。"""
    extras: dict = {}
    userinfo = ""
    if "@" in raw:
        userinfo, raw = raw.rsplit("@", 1)
    if userinfo:
        extras["auth"] = urllib.parse.unquote(userinfo)
    if "?" in raw:
        qs = raw.split("?", 1)[1].split("#", 1)[0]
        allow = {"obfs", "obfs-password", "sni", "alpn", "insecure", "skip-cert-verify",
                 "auth", "password", "up", "down", "ports"}
        for k, v in urllib.parse.parse_qsl(qs, keep_blank_values=True):
            key = k.lower()
            if key not in allow:
                continue
            if key == "insecure":
                extras["skip-cert-verify"] = v.lower() in ("1", "true", "yes")
            elif key == "password":
                extras["auth"] = urllib.parse.unquote(v)
            elif key == "alpn":
                extras["alpn"] = [x for x in v.split(",") if x]
            else:
                extras[key] = urllib.parse.unquote(v)
    return extras


def parse_nodes_ext(text: str) -> list:
    """复用 u1_probe.parse_nodes 路径，扩展为统一节点结构（保留完整 proxy dict + port）。"""
    text = try_b64(text)
    nodes: list = []

    def add_from_dict(obj):
        if not isinstance(obj, dict) or not obj.get("server"):
            return
        t = str(obj.get("type", "")).lower()
        if t not in GOOD_TYPES:  # 红线：只收优质协议
            return
        n = dict(obj)  # 协议专有字段原样保留，供 U5 组配置
        n["type"] = t
        n["server"] = str(obj["server"]).strip()
        n["port"] = _extract_port(obj.get("port"))
        nodes.append(n)

    try:
        import yaml
        data = yaml.safe_load(text)
        if isinstance(data, dict):
            for p in (data.get("proxies") or []):
                add_from_dict(p)
            for o in (data.get("outbounds") or []):
                add_from_dict(o)
        elif isinstance(data, list):
            for o in data:
                add_from_dict(o)
    except Exception:
        pass

    for m in URI_RE.finditer(text):
        t = m.group(1).lower()
        t = "hysteria2" if t in ("hy2", "hysteria2") else t
        if t not in GOOD_TYPES:
            continue
        raw = m.group(2)
        userinfo, sep, hostpart = raw.rpartition("@")
        if not sep:
            hostpart = raw
        tail = hostpart.split("/", 1)[0].split("?", 1)[0].split("#", 1)[0]
        if tail.startswith("["):
            server = tail.split("]", 1)[0] + "]"
        elif ":" in tail:
            server = tail.rsplit(":", 1)[0]
        else:
            server = tail
        server = server.strip().strip("[]")
        if not server:
            continue
        node = {"type": t, "server": server, "port": _extract_port(None, hostpart)}
        node.update(_uri_extras(raw))
        nodes.append(node)

    # 按 (type, server, port) 去重（同一节点可能同时出现在 yaml 与 URI 中）
    seen = set()
    uniq = []
    for n in nodes:
        key = (n.get("type", ""), n.get("server", ""), str(n.get("port", "")))
        if key in seen:
            continue
        seen.add(key)
        uniq.append(n)
    return uniq


# ------------------------------ 主流程 ------------------------------
def load_sources() -> list:
    with open(SOURCES, "r", encoding="utf-8") as f:
        doc = json.load(f)
    repos = []
    for r in (doc.get("repos") or []):
        if isinstance(r, dict) and r.get("full_name"):
            repos.append({
                "full_name": str(r["full_name"]).strip(),
                "branch": str(r.get("branch") or "main").strip(),
            })
    return repos


def process_repo(idx: int, repo: dict, total: int) -> dict:
    """处理单个源；整源异常在此隔离，不影响其他源。"""
    full, branch = repo["full_name"], repo["branch"]
    result = {"idx": idx, "full": full, "files": [], "nodes": [], "failed": None}
    try:
        files = tree_files(full, branch)
        if files is None:
            result["failed"] = "tree-fetch-failed"
            log(f"  [{idx}/{total}] {full} 整源失败：tree 请求失败")
            return result
        got = []
        for path in files:
            text = fetch_content(full, branch, path)
            if not text:
                continue
            here = parse_nodes_ext(text[:MAX_BYTES])
            for n in here:
                n["_src"] = full
                n["_file"] = path
                n.setdefault("cc", "")
                n.setdefault("cc_basis", "")
            got.extend(here)
        result["files"] = files
        result["nodes"] = got
        log(f"  [{idx}/{total}] {full} 文件{len(files)} 节点{len(got)}")
    except Exception as e:
        # 单源失败不影响其他源；异常信息只记类型，不含 token/headers
        result["failed"] = type(e).__name__
        log(f"  [{idx}/{total}] {full} 异常：{type(e).__name__}")
    return result


def main() -> int:
    log(f"[U2] 抓取开始 {datetime.datetime.now().isoformat(timespec='seconds')}")
    repos = load_sources()
    log(f"[U2] 源数量：{len(repos)}（来自 sources.json）")
    log(f"[U2] 鉴权模式：{'GITHUB_TOKEN(Bearer)' if TOKEN else 'anonymous'}（token 不打印、不落盘）")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = [ex.submit(process_repo, i, r, len(repos)) for i, r in enumerate(repos, 1)]
        for fut in concurrent.futures.as_completed(futures):
            results.append(fut.result())
    results.sort(key=lambda x: x["idx"])

    all_nodes = []
    failed_sources = []
    per_repo = []
    for res in results:
        all_nodes.extend(res["nodes"])
        per_repo.append({"full_name": res["full"], "files_checked": res["files"],
                         "nodes": len(res["nodes"])})
        if res["failed"]:
            failed_sources.append({"full_name": res["full"], "reason": res["failed"]})

    log(f"[U2] GitHub API 实际请求 {API_CALLS} 次；缓存命中 {CACHE_HITS} 次（命中未发请求）")
    log(f"[U2] 节点合计 {len(all_nodes)}；失败源 {len(failed_sources)}")

    out = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "source_count": len(repos),
        "node_count": len(all_nodes),
        "api_calls": API_CALLS,
        "cache_hits": CACHE_HITS,
        "failed_sources": failed_sources,
        "per_repo": per_repo,
        "nodes": all_nodes,
    }
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    log(f"[U2] 已写出 {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
