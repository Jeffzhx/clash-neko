#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本机收官：把「哪些节点真的能用」的裁决放回使用地（国内本机）再做。

背景（D19）：CI 跑在 GitHub 美国 runner 上，它判出来的 alive 是「从美国能连」，
从国内看几乎全废。所以抓取/去重/地域过滤可以留在 CI，**最终 alive 裁决必须在
本机、在没有 TUN 抢路由的网络里做**。

用法：
    # 一条命令跑完整流程（抓取 → 地域过滤 → 本机内核测活 → 生成订阅）
    MIHOMO_BIN="D:/WinAPP/Proxy/Clash Verge Rev/verge-mihomo.exe" python scripts/local_finalize.py

    # 只重跑测活+生成（沿用上次抓取的 nodes_raw.json，省 API 额度）
    ... --skip-collect

    # 指定根目录（测试用）
    ... --root .localtest/cnpool

守卫：默认检测到默认网关落在 198.18/198.19（本机 TUN）就拒绝运行，避免又测出假数据。
     确认自己清楚后果时才用 --force。
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

TUN_HINT_PREFIXES = ("198.18.", "198.19.")
DEFAULT_KERNEL = r"D:/WinAPP/Proxy/Clash Verge Rev/verge-mihomo.exe"


def log(msg: str) -> None:
    print(msg, flush=True)


def default_gateway() -> str:
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


def summary(root: str) -> int:
    alive_path = os.path.join(root, "alive_nodes.json")
    if not os.path.isfile(alive_path):
        log("[finalize] 没有 alive_nodes.json，无法汇总")
        return 1
    doc = json.load(open(alive_path, encoding="utf-8"))
    alive = doc.get("alive_nodes") or []
    log(f"\n=== 结果 ===")
    log(f"输入 {doc.get('input_node_count')} 个 → 本机实测可用 {len(alive)} 个")
    for n in alive:
        lv = n.get("_liveness") or {}
        eg = lv.get("egress") or {}
        log(f"  {n.get('type'):<9} {n.get('server')}:{n.get('port')} "
            f"delay={lv.get('latency_ms')}ms 出口={eg.get('ip')}/{eg.get('loc')} "
            f"src={n.get('_src', '?')}")
    out = [p for p in ("main.yaml", "nekobox.json") if os.path.isfile(os.path.join(root, p))]
    if out:
        log("产物：" + "、".join(out) + "（两文件内容一致，导入客户端即可）")
    if not alive:
        log("今天这批源在你这条网络上 0 个可用 —— 发布空列表，不塞假活节点。")
    log("\n发布前自查：把产物推到 gh-pages 后调一次 jsDelivr purge，否则客户端仍读旧缓存。")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="项目根目录（默认本脚本上一级）")
    ap.add_argument("--skip-collect", action="store_true", help="跳过抓取+地域过滤，沿用现有 nodes_raw.json")
    ap.add_argument("--pull", action="store_true",
                    help="从 gh-pages 拉候选快照 us_nodes.json（CI 已做抓取+地域过滤时用）")
    ap.add_argument("--repo", default=os.environ.get("SUB_REPO", "Jeffzhx/clash-neko"),
                    help="候选快照所在仓库（owner/name），默认本项目")
    ap.add_argument("--force", action="store_true", help="检测到 TUN 时仍继续（结果可能假阳性）")
    ap.add_argument("--kernel", default=os.environ.get("MIHOMO_BIN", "") or DEFAULT_KERNEL)
    ap.add_argument("--timeout", default=os.environ.get("MIHOMO_TIMEOUT", "8000"))
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    py = sys.executable
    gw = default_gateway()
    log(f"[finalize] 根目录 {root}")
    log(f"[finalize] 默认网关 {gw or '取不到'}")
    if gw.startswith(TUN_HINT_PREFIXES) and not args.force:
        log("[finalize] 拒绝运行：默认网关落在 TUN 网段（198.18/198.19）。"
            "本机代理的 TUN 会把测活流量再转发一层，测出来的「可用」是假的。\n"
            "          请先关闭 Clash Verge/NekoBox 的 TUN 模式（或退出客户端）再跑；"
            "确实要硬跑请加 --force。", )
        return 3
    if not os.path.isfile(args.kernel):
        log(f"[finalize] 内核不存在：{args.kernel}（用 --kernel 指定，或设置 MIHOMO_BIN）")
        return 2

    env = dict(os.environ, MIHOMO_BIN=args.kernel, MIHOMO_TIMEOUT=str(args.timeout))
    env.pop("MIHOMO_VERIFY_EGRESS", None)  # 用脚本默认值（开启）

    def step(name, script, extra_env=None):
        e = dict(env, **(extra_env or {}))
        return subprocess.run([py, os.path.join(root, "scripts", script)], cwd=root, env=e).returncode

    if args.pull:
        url = f"https://raw.githubusercontent.com/{args.repo}/gh-pages/us_nodes.json"
        dest = os.path.join(root, "us_nodes.json")
        log(f"\n=== 拉取候选快照 ===\n{url}")
        try:
            import urllib.request
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read()
            doc = json.loads(data.decode("utf-8"))
            n = len(doc.get("us_nodes") or [])
            with open(dest, "wb") as f:
                f.write(data)
            log(f"候选 {n} 个 → {dest}")
            if n == 0:
                log("[finalize] 候选为 0，无需继续"); return 0
        except Exception as e:
            log(f"[finalize] 拉取失败（{type(e).__name__}: {getattr(e, 'code', '')}）。"
                f"若 gh-pages 上还没有 us_nodes.json，请先让 CI 跑一次。")
            return 1
    elif not args.skip_collect:
        if step("抓取", "fetch_sources.py"):
            log("[finalize] 抓取失败，终止"); return 1
        if step("地域过滤", "geoip_filter.py"):
            log("[finalize] 地域过滤失败，终止"); return 1

    rc = step("本机内核测活", "kernel_probe.py")
    if rc == 2:
        log("[finalize] 内核不可用（返回 2），终止"); return 2
    if rc != 0:
        log(f"[finalize] 测活返回 {rc}，终止"); return 1

    if step("生成订阅", "build_subscriptions.py"):
        log("[finalize] 生成订阅失败，终止"); return 1

    return summary(root)


if __name__ == "__main__":
    sys.exit(main())
