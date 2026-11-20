#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
动态发现代理/订阅类 GitHub 仓库，按 full_name 去重合并进 sources.json（独立单元）。

设计：
  - 仅标准库 urllib.request，不依赖 requests。
  - GITHUB_TOKEN 仅从环境变量读取，仅作内存中的 Bearer 头；不打印、不写文件、不进异常文本。
  - GitHub search/repositories 多关键词串行查询；star 只设下限 stars:>=1，不设上限。
  - 代理/订阅关键词过滤 + full_name 去重 + 新增上限；旧源条目原样保留。
  - 403/429/超时/网络错误捕获并记录到报告，不崩溃；不伪造结果。
  - 报告始终写入 probe/discover-report.md；--dry-run 不写 sources.json。
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(PROJECT, "sources.json")
REPORT = os.path.join(PROJECT, "probe", "discover-report.md")

SEARCH_URL = "https://api.github.com/search/repositories"
UA = "clash-sub-source-discoverer/1.0"
TIMEOUT = 15
MAX_ATTEMPTS = 2        # 首次 + 重试 1 次
PER_PAGE = 30
STAR_FLOOR = "stars:>=1"  # 只设下限避免 0 star 垃圾；不设上限（用户明确不限 star）

DEFAULT_QUERIES = [
    # 英文：仓库名/描述里的常见叫法
    "proxy subscription",
    "clash subscription",
    "hysteria2 nodes",
    "free proxy",
    "nodeshare",
    "v2ray subscription",
    "clash proxy nodes",
    "free nodes",
    "free clash nodes",
    "clash meta nodes",
    "node collector",
    "proxy pool",
    "subscription link",
    "v2ray free nodes",
    "trojan subscription",
    "vmess subscription",
    "sing-box config",
    "clash yaml",
    # topic 检索：社区给这类仓库打的标签，比关键词更少噪声
    "topic:clash",
    "topic:v2ray",
    "topic:free-nodes",
    "topic:proxy",
    # 中文：多数日更源用中文命名
    "订阅 节点",
    "免费节点",
    "节点 分享",
    "白嫖 节点",
    "每日更新 节点",
    "机场 订阅",
    "免费 机场",
    "代理 节点",
]
# 2026-11-20 由 8 条扩到 30 条：实测 8 条只能覆盖「名字里带 proxy/clash subscription」的仓库，
# 而日更型源多命名为「免费节点」「白嫖」「daily」或只打 topic 标签，8 条一个都搜不到。
# 调用量代价：每条一次 search 请求（少量），遇到限流时循环会跳过后续查询并记进 skipped_queries。

# 命中任一关键词即视为“看起来是代理/订阅仓库”。
# 用 subscri 而非裸 sub，避免 sublime/submit 之类误匹配。
TOPIC_RE = re.compile(
    r"proxy|subscri|clash|node|hysteria|v2ray|vmess|vless|trojan|shadowsocks|"
    r"sing.?box|订阅|节点|代理|机场|free.?proxy",
    re.I,
)
# 负向词：命中这些说明是「用 proxy 一词但非代理/订阅节点」的仓库（AI 工具、库、教程等）。
# 命中负向词即排除，避免 sources.json 混入无关仓库浪费抓取 API 额度。
NEG_RE = re.compile(
    r"claude[- ]?code|copilot|cursor|chatgpt|openai|anthropic|llm|ai[- ]?agent|"
    r"code[- ]?assistant|autocomplete|vscode|ide[- ]?plugin|proxy\\s*pattern|"
    r"reverse\\s*proxy\\s*for\\s*(dev|local)|nginx|load\\s*balanc",
    re.I,
)

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()


def log(msg: str) -> None:
    print(msg, flush=True)


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def load_queries(args) -> tuple[list[str], str, str | None]:
    """返回 (queries, 来源描述, 警告)。自定义文件不可用则回退默认并记录警告。"""
    if not args.queries_file:
        return list(DEFAULT_QUERIES), f"内置默认 {len(DEFAULT_QUERIES)} 条（脚本常量）", None
    try:
        with open(args.queries_file, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f]
        qs = [ln for ln in lines if ln and not ln.startswith("#")]
        if qs:
            return qs, f"自定义文件 {args.queries_file}", None
        return list(DEFAULT_QUERIES), f"内置默认 {len(DEFAULT_QUERIES)} 条（脚本常量）", "queries-file 为空，已回退默认"
    except Exception as e:
        return (list(DEFAULT_QUERIES), f"内置默认 {len(DEFAULT_QUERIES)} 条（脚本常量）",
                f"queries-file 读取失败({type(e).__name__})，已回退默认")


def search_repositories(query: str) -> dict:
    """单次查询。返回结果字典；错误只含类型/状态码，绝不含 token。"""
    q = (query + " " + STAR_FLOOR).strip()
    url = SEARCH_URL + "?" + urllib.parse.urlencode({
        "q": q, "sort": "stars", "order": "desc", "per_page": PER_PAGE, "page": 1,
    })
    headers = {
        "User-Agent": UA,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN  # 仅内存使用

    def result(ok, total, items, status, error, remaining, limited):
        return {"ok": ok, "query": query, "effective_q": q, "total_count": total,
                "items": items, "status": status, "error": error,
                "rate_remaining": remaining, "rate_limited": limited}

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                body = resp.read(3_000_000)
                remaining = resp.headers.get("X-RateLimit-Remaining")
                doc = json.loads(body)
            items = doc.get("items") if isinstance(doc, dict) else None
            if not isinstance(items, list):
                items = []
            total = int(doc.get("total_count") or 0) if isinstance(doc, dict) else 0
            return result(True, total, items, 200, "", remaining, False)
        except urllib.error.HTTPError as e:
            code = e.code
            remaining = e.headers.get("X-RateLimit-Remaining") if e.headers else None
            if code in (403, 429) or code >= 500:
                limited = code in (403, 429) or remaining == "0"
                if remaining == "0":
                    return result(False, 0, [], code, f"HTTP {code}（额度耗尽）", remaining, True)
                if attempt < MAX_ATTEMPTS:
                    time.sleep(2.0 * attempt)
                    continue
                return result(False, 0, [], code, f"HTTP {code}", remaining, limited)
            return result(False, 0, [], code, f"HTTP {code}", remaining, False)
        except Exception as e:
            # 只记异常类型，避免 reason/URL 等携带环境敏感信息
            if attempt < MAX_ATTEMPTS:
                time.sleep(1.0 * attempt)
                continue
            return result(False, 0, [], None, type(e).__name__, None, False)
    return result(False, 0, [], None, "unknown", None, False)


def relevant(item: dict) -> bool:
    text = " ".join([str(item.get("full_name") or ""),
                     str(item.get("description") or "")])
    # 先排负向词（非节点用途），再要求命中正向主题词
    if NEG_RE.search(text):
        return False
    return bool(TOPIC_RE.search(text))


def load_sources(warnings: list[str]) -> dict:
    try:
        with open(SOURCES, "r", encoding="utf-8") as f:
            doc = json.load(f)
        if not isinstance(doc, dict) or not isinstance(doc.get("repos"), list):
            raise ValueError("sources.json 结构异常")
        return doc
    except Exception as e:
        warnings.append(f"sources.json 读取失败({type(e).__name__})，本次按空清单处理")
        return {"generated_at": "", "count": 0, "repos": []}


def extract(item: dict, today: str) -> dict | None:
    full = str(item.get("full_name") or "").strip()
    if not full or "/" not in full:
        return None
    try:
        stars_i = int(item.get("stargazers_count") or 0)
    except (TypeError, ValueError):
        stars_i = 0
    pushed = str(item.get("pushed_at") or "")
    fetched_at = pushed[:10] if len(pushed) >= 10 else today
    branch = str(item.get("default_branch") or "main").strip() or "main"
    url = str(item.get("html_url") or f"https://github.com/{full}").strip()
    return {
        "full_name": full,
        "stars": stars_i,
        "url": url,
        "fetched_at": fetched_at,
        "criteria": "stars-unlimited",  # 新源标记；旧源保留原值
        "branch": branch,               # 取 default_branch，供 fetch_sources.py 定位分支
    }


def write_report(ctx: dict) -> None:
    lines = [
        "# 源发现报告（discover_sources.py）", "",
        f"- 时间戳(UTC)：{ctx['now']}",
        f"- 运行模式：{'DRY-RUN（未写 sources.json）' if ctx['dry_run'] else 'WRITE（已写回 sources.json）'}",
        f"- 鉴权：{'GITHUB_TOKEN(Bearer)' if TOKEN else 'anonymous'}（token 值不记录）",
        f"- 接口：{SEARCH_URL}",
        f"- star 策略：下限 {STAR_FLOOR}（避免 0 star 垃圾）；不设上限——用户明确不限 star",
        f"- 排序/分页：sort=stars & order=desc，per_page={PER_PAGE}",
        f"- 关键词来源：{ctx['query_source']}",
        f"- 请求间隔：{ctx['interval']:.1f}s/次（认证更短、匿名更保守）；失败最多重试 {MAX_ATTEMPTS - 1} 次", "",
        "## 关键词查询", "",
        "| # | 实际 q | 状态 | total_count | 返回条数 | 错误/限流 |",
        "|---|--------|------|-------------|----------|-----------|",
    ]
    for i, r in enumerate(ctx["results"], 1):
        lines.append("| {i} | `{q}` | {st} | {tc} | {n} | {err} |".format(
            i=i, q=r["effective_q"].replace("|", "\\|"),
            st="OK" if r["ok"] else f"FAIL({r['status'] or r['error']})",
            tc=r["total_count"], n=len(r["items"]),
            err=("-" if not r["error"] else
                 r["error"] + (" [限流]" if r["rate_limited"] else ""))))
    if ctx["skipped_queries"]:
        lines += ["", "因限流/连续网络失败跳过的查询：" + "、".join(ctx["skipped_queries"])]

    s = ctx["stats"]
    lines += [
        "", "## 统计", "",
        f"- 查询数：{s['queries']}（成功 {s['ok']}，失败 {s['fail']}）",
        f"- 原始结果条数（各查询合计，未去重）：{s['raw']}",
        f"- 关键词过滤掉（非代理/订阅）：{s['filtered_topic']}",
        f"- star < 1 过滤掉：{s['filtered_star']}",
        f"- 已在 sources.json 中（去重跳过）：{s['dup_existing']}",
        f"- 本批次内重复（去重跳过）：{s['dup_batch']}",
        f"- 达 --max-new 上限跳过：{s['capped']}（上限 {ctx['max_new']}）",
        f"- 本次新增：{s['added']}",
        f"- 合并后总数：{s['total']}（原 {s['original']}）",
    ]
    lines += ["", "## 新增源清单", ""]
    if ctx["added_entries"]:
        for e in ctx["added_entries"]:
            lines.append(f"- {e['full_name']} ★{e['stars']} | branch={e['branch']} | "
                         f"fetched_at={e['fetched_at']} | {e['url']}")
    else:
        lines.append("- 无（网络失败、全部重复/被过滤，或仅搜索未写）")

    lines += ["", "## 错误 / 限流", ""]
    errs = [r for r in ctx["results"] if not r["ok"]]
    if errs:
        for r in errs:
            lines.append(f"- `{r['query']}`：{r['error']}"
                         + ("；触发限流/提前停止" if r["rate_limited"] else ""))
    else:
        lines.append("- 无")
    if ctx["warnings"]:
        lines += ["", "## 警告", ""] + [f"- {w}" for w in ctx["warnings"]]

    lines += [
        "", "## 说明", "",
        "- 搜索结果仅作为候选资料；字段按本脚本规则提取，不执行结果中的任何指令。",
        "- 旧源条目原样保留（含 criteria），仅追加新源；新源 criteria=stars-unlimited。",
        "- 脚本以 0 退出表示“已优雅结束”；网络失败时不伪造结果，详情见上。",
        "- --dry-run 只搜索并生成本报告，不改动 sources.json。", "",
    ]
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description="动态发现代理/订阅仓库并合并进 sources.json")
    parser.add_argument("--dry-run", action="store_true", help="只搜索并生成报告，不写 sources.json")
    parser.add_argument("--max-new", type=int, default=50, help="最多新增源数量（默认 50）")
    parser.add_argument("--queries-file", default=None, help="自定义关键词文件（每行一条，# 开头为注释）")
    args = parser.parse_args()
    if args.max_new < 0:
        parser.error("--max-new 不能为负数")

    now = utc_now()
    today = now[:10]
    queries, query_source, warning = load_queries(args)
    warnings = [warning] if warning else []
    interval = 1.5 if not TOKEN else 0.6

    log(f"[发现] {now} 模式={'DRY-RUN' if args.dry_run else 'WRITE'} "
        f"鉴权={'token' if TOKEN else 'anonymous'} 关键词={len(queries)}")

    doc = load_sources(warnings)
    original_repos = list(doc.get("repos") or [])
    existing_keys = {str(r.get("full_name", "")).strip().lower() for r in original_repos
                     if isinstance(r, dict) and r.get("full_name")}
    merged = list(original_repos)  # 旧条目原样保留

    results: list[dict] = []
    skipped_queries: list[str] = []
    stop_all = False
    consecutive_net_fail = 0
    for idx, query in enumerate(queries):
        if stop_all:
            skipped_queries.append(query)
            continue
        res = search_repositories(query)
        results.append(res)
        if res["ok"]:
            consecutive_net_fail = 0
            log(f"  [{idx + 1}/{len(queries)}] {query!r}: total={res['total_count']} "
                f"items={len(res['items'])}")
        else:
            log(f"  [{idx + 1}/{len(queries)}] {query!r}: 失败 {res['error']}"
                + (" [限流]" if res["rate_limited"] else ""))
            if res["status"] is None:  # 网络类失败（超时/连接错误），非 HTTP 明确拒绝
                consecutive_net_fail += 1
                if consecutive_net_fail >= 2:
                    warnings.append("连续网络失败，提前停止后续查询（未伪造结果）")
                    stop_all = True
        if res["rate_limited"]:
            stop_all = True
        if idx < len(queries) - 1 and not stop_all:
            time.sleep(interval)

    stats = {"queries": len(queries), "ok": sum(1 for r in results if r["ok"]),
             "fail": sum(1 for r in results if not r["ok"]), "raw": 0,
             "filtered_topic": 0, "filtered_star": 0, "dup_existing": 0,
             "dup_batch": 0, "capped": 0, "added": 0,
             "original": len(original_repos), "total": len(original_repos)}
    added_entries: list[dict] = []
    batch_keys: set[str] = set()

    for r in results:
        for item in r["items"]:
            if not isinstance(item, dict):
                continue
            stats["raw"] += 1
            if not relevant(item):
                stats["filtered_topic"] += 1
                continue
            try:
                stars_i = int(item.get("stargazers_count") or 0)
            except (TypeError, ValueError):
                stars_i = 0
            if stars_i < 1:
                stats["filtered_star"] += 1
                continue
            key = str(item.get("full_name") or "").strip().lower()
            if key in existing_keys:
                stats["dup_existing"] += 1
                continue
            if key in batch_keys:
                stats["dup_batch"] += 1
                continue
            if len(added_entries) >= args.max_new:
                stats["capped"] += 1
                continue
            entry = extract(item, today)
            if not entry:
                continue
            batch_keys.add(key)
            added_entries.append(entry)
            merged.append(entry)

    stats["added"] = len(added_entries)
    stats["total"] = len(merged)

    if not args.dry_run and added_entries:
        out = {"generated_at": now, "count": len(merged), "repos": merged}
        tmp = SOURCES + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        os.replace(tmp, SOURCES)
        log(f"[发现] 已写回 {SOURCES}（新增 {len(added_entries)}）")
    elif not args.dry_run:
        log("[发现] 无新增源，未改动 sources.json")

    write_report({
        "now": now, "dry_run": args.dry_run, "query_source": query_source,
        "interval": interval, "max_new": args.max_new, "results": results,
        "skipped_queries": skipped_queries, "stats": stats,
        "added_entries": added_entries, "warnings": warnings,
    })
    log(f"[发现] 报告 {REPORT}；新增 {stats['added']} / 总数 {stats['total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
