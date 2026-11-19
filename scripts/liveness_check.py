#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U4 —— hysteria2 美国节点测活（多手段探测 + 保守判定）

用法（脚本按 __file__ 推导项目根，任意 cwd 均可运行）：
    C:/Users/35637/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe scripts/liveness_check.py

输入（只读，绝不覆盖）：
    <root>/us_nodes.json    U3 产出的 us_nodes 数组（5 个美国 hysteria2 节点）
输出（覆盖写本单元自己的产物，不动他人文件）：
    <root>/alive_nodes.json
    <root>/probe/liveness-report.md

【超时设置】每个网络动作都有硬超时，绝不挂起：
    DNS 解析 2s；TCP connect 3s；UDP send+recv 3s。
    5 节点串行最坏 5 * (2 + 3 + 3) = 40s，控制在 60s 内。

【hysteria2 的 UDP 特性】hysteria2 基于 QUIC/UDP，服务端通常不监听 TCP。
    所以「TCP connect 超时」是常态信号，绝不能单凭 TCP 失败判节点失效。
    本脚本只发一个 hysteria2/QUIC 风格的 UDP datagram（非合法 QUIC Initial，
    本机无 QUIC 内核/库，无法做完整握手），仅用于确认「该 UDP 端口是否有服务响应」。

【本机代理环境局限】当前环境已设置 HTTP_PROXY/HTTPS_PROXY（HTTP CONNECT 代理），
    用户实测直连境外 TCP 到 206.189.229.48:443、107.149.232.92:443 均 3s 超时。
    - HTTP CONNECT 代理只转发 TCP，不转发 UDP；UDP 探测同样可能受本机 NAT/策略阻断。
    - 因此「无正向证据」只说明本机无法确认，不等于节点本身失效。
    - 判定必须保守诚实：有正向证据才 alive=true；拿不到证据一律 unknown；
      只有双重明确负向证据才 dead=false；不得把 unknown 混入订阅或当 dead 静默删除。

【判定矩阵】
    UDP 收到响应                             -> alive=true  （正向证据 udp_reply）
    UDP=ICMP不可达 且 TCP=明确拒绝            -> alive=false （双重负向证据，dead）
    TCP 端口明确开放 且 无 UDP ICMP 负向       -> alive=true  （正向证据 tcp_port_open，
                                                  理由注明未完成 hysteria2 握手，需复核）
    其余（TCP 超时/拒绝 + UDP 无响应/ICMP）    -> alive="unknown"（本机环境无法确认）
"""

from __future__ import annotations

import concurrent.futures
import datetime
import ipaddress
import json
import os
import socket
import sys
import time

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_NODES_PATH = os.path.join(PROJECT, "us_nodes.json")
ALIVE_PATH = os.path.join(PROJECT, "alive_nodes.json")
REPORT_PATH = os.path.join(PROJECT, "probe", "liveness-report.md")

DNS_TIMEOUT = 2.0
TCP_TIMEOUT = 3.0
UDP_TIMEOUT = 3.0

# hysteria2/QUIC 风格 UDP 探测载荷：仅用于触发服务端 UDP 端口响应，非合法 QUIC Initial。
UDP_PAYLOAD = b"\x00\x00HYSTERIA2-UDP-PROBE-v1" + bytes(range(16))

METHODS = ["A_tcp_connect", "B_udp_datagram"]
KNOWN_ICMP_CODES = {10054, 10061, 111, 104, 61}  # WSAECONNRESET/REFUSED, ECONNREFUSED 等


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def resolve_target(host: str):
    """返回 (addr, family, err)。IP 字面量直返，域名用线程池加超时解析，绝不挂住。"""
    host = str(host or "").strip()
    try:
        ip = ipaddress.ip_address(host)
        return host, (socket.AF_INET6 if ip.version == 6 else socket.AF_INET), None
    except ValueError:
        pass

    ex = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    try:
        fut = ex.submit(socket.getaddrinfo, host, None, socket.AF_UNSPEC, socket.SOCK_DGRAM)
        try:
            infos = fut.result(timeout=DNS_TIMEOUT)
        except concurrent.futures.TimeoutError:
            return None, None, f"DNS 解析超时 {DNS_TIMEOUT:g}s"
        except Exception as e:
            return None, None, f"DNS 解析失败：{type(e).__name__}: {e}"
        for info in infos or []:
            family, _, _, _, sa = info
            if family in (socket.AF_INET, socket.AF_INET6):
                return sa[0], family, None
        return None, None, "DNS 解析无可用 A/AAAA 结果"
    finally:
        ex.shutdown(wait=False, cancel_futures=True)


def probe_tcp(addr: str, family: int, port: int) -> dict:
    """手段A：TCP connect，硬超时 3s。仅作参考信号；hysteria2 不监听 TCP 时超时属正常。"""
    started = time.perf_counter()
    sock = socket.socket(family, socket.SOCK_STREAM)
    sock.settimeout(TCP_TIMEOUT)
    try:
        sock.connect((addr, port))
        ms = round((time.perf_counter() - started) * 1000, 1)
        return {
            "status": "open", "ok": True, "latency_ms": ms,
            "detail": f"TCP connect 成功，耗时 {ms}ms（端口有 TCP 监听；不等同于 hysteria2 握手成功）",
        }
    except socket.timeout:
        return {
            "status": "timeout", "ok": False, "latency_ms": None,
            "detail": f"TCP connect 超时 {TCP_TIMEOUT:g}s（hysteria2 通常不监听 TCP，属正常，不判死）",
        }
    except ConnectionRefusedError:
        return {
            "status": "refused", "ok": False, "latency_ms": None,
            "detail": "TCP connect 被明确拒绝（RST/ICMP），该 TCP 端口无监听",
        }
    except OSError as e:
        code = getattr(e, "winerror", None) or getattr(e, "errno", None)
        return {
            "status": "error", "ok": False, "latency_ms": None,
            "detail": f"TCP connect 异常 {type(e).__name__}(code={code}): {e}",
        }
    finally:
        sock.close()


def probe_udp(addr: str, family: int, port: int) -> dict:
    """手段B：发一个 UDP datagram 并等待响应，硬超时 3s。无响应不判死，仅标证据。"""
    started = time.perf_counter()
    sock = socket.socket(family, socket.SOCK_DGRAM)
    sock.settimeout(UDP_TIMEOUT)
    try:
        sock.sendto(UDP_PAYLOAD, (addr, port))
    except OSError as e:
        sock.close()
        return {
            "status": "send_error", "latency_ms": None,
            "detail": f"UDP sendto 失败：{type(e).__name__}: {e}",
        }
    try:
        data, peer = sock.recvfrom(2048)
        ms = round((time.perf_counter() - started) * 1000, 1)
        return {
            "status": "reply", "latency_ms": ms, "bytes": len(data),
            "peer": f"{peer[0]}:{peer[1]}",
            "detail": f"UDP 收到 {len(data)} 字节响应，来自 {peer[0]}:{peer[1]}，RTT {ms}ms（明确正向证据）",
        }
    except socket.timeout:
        return {
            "status": "no_response", "latency_ms": None,
            "detail": f"UDP {UDP_TIMEOUT:g}s 内无响应且未捕获 ICMP 错误（本机环境无法确认）",
        }
    except OSError as e:
        code = getattr(e, "winerror", None) or getattr(e, "errno", None)
        if isinstance(e, (ConnectionRefusedError, ConnectionResetError)) or code in KNOWN_ICMP_CODES:
            return {
                "status": "icmp_unreachable", "latency_ms": None,
                "detail": (f"UDP recvfrom 抛 {type(e).__name__}(code={code})，"
                           "疑似 ICMP port-unreachable；可能来自服务端，也可能来自本机 NAT/防火墙代理设备"),
            }
        return {
            "status": "error", "latency_ms": None,
            "detail": f"UDP recvfrom 异常 {type(e).__name__}(code={code}): {e}",
        }
    finally:
        sock.close()


def decide(resolve_err, tcp: dict, udp: dict) -> dict:
    """保守判定：正向证据才 alive=true；双重负向才 dead；其余 unknown。"""
    if resolve_err:
        return {
            "alive": "unknown", "latency_ms": None, "evidence": "resolve_failed",
            "reason": f"目标不可解析：{resolve_err}；本机环境无法确认，不判死也不视为可用",
        }

    # 1) 最强正向：UDP 端口确实有服务应答
    if udp["status"] == "reply":
        return {
            "alive": True, "latency_ms": udp.get("latency_ms"), "evidence": "udp_reply",
            "reason": "有据（正向）：" + udp["detail"],
        }

    # 2) 双重明确负向证据才判 dead，避免把本机网络失败误判为节点失效
    if udp["status"] == "icmp_unreachable" and tcp["status"] == "refused":
        return {
            "alive": False, "latency_ms": None, "evidence": "icmp_unreachable+tcp_refused",
            "reason": ("有据（负向）：" + udp["detail"] + "；" + tcp["detail"]
                       + "；两条独立证据均指向端口不开放。若本机安全策略伪造 ICMP，请在网络条件允许时重测"),
        }

    # 3) 题目认可的「明确端口开放」正向证据，但如实标注握手未验证
    if tcp["status"] == "open" and udp["status"] != "icmp_unreachable":
        return {
            "alive": True, "latency_ms": tcp.get("latency_ms"), "evidence": "tcp_port_open",
            "reason": ("有据（正向，有限）：" + tcp["detail"] + "；" + udp["detail"]
                       + "；注意未做 hysteria2 握手验证，建议在网络条件允许时用内核复核"),
        }

    # 4) 其余一律 unknown：本机代理环境下拿不到正向证据
    return {
        "alive": "unknown", "latency_ms": None, "evidence": "none",
        "reason": ("推断（非结论）：本机代理环境下无法确认存活——" + tcp["detail"]
                   + "；" + udp["detail"] + "；未取得正向证据，按红线不判可用，也不判失效"),
    }


def proxy_env() -> dict:
    """手段C（环境级参考，不参与判定）：HTTP CONNECT 代理不转发 UDP，仅作局限说明。"""
    hp = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy") or ""
    sp = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or ""
    return {
        "http_proxy_set": bool(hp),
        "https_proxy_set": bool(sp),
        "proxy_type": "HTTP CONNECT（仅转发 TCP，通常不转发 UDP）",
        "note": "本单元不通过代理转发探测流量；代理地址不写入报告，仅记录是否设置。",
    }


def load_us_nodes() -> list[dict]:
    try:
        with open(US_NODES_PATH, "r", encoding="utf-8") as f:
            doc = json.load(f)
    except Exception as e:
        print(f"[U4][错误] 无法读取 {US_NODES_PATH}: {e}", file=sys.stderr)
        return []
    nodes = doc.get("us_nodes", []) if isinstance(doc, dict) else []
    return [n for n in nodes if isinstance(n, dict)]


def write_alive_nodes(now: str, records: list[dict], env: dict) -> dict:
    alive = [r for r in records if r["_liveness"]["alive"] is True]
    unknown = [r for r in records if r["_liveness"]["alive"] == "unknown"]
    dead = [r for r in records if r["_liveness"]["alive"] is False]

    out = {
        "generated_at": now,
        "unit": "U4",
        "methodology": {
            "A_tcp_connect": f"socket connect，超时 {TCP_TIMEOUT:g}s；仅参考信号，hysteria2 不监听 TCP 时超时属正常，不单凭 TCP 失败判死。",
            "B_udp_datagram": f"发送 hysteria2/QUIC 风格 UDP datagram 并 recvfrom，超时 {UDP_TIMEOUT:g}s；收到响应=正向证据；未收到不判死。无 QUIC 内核/库，不做完整握手。",
            "C_proxy_channel": "仅读取 HTTP_PROXY/HTTPS_PROXY 作为局限说明；HTTP CONNECT 不转发 UDP，不参与判定。",
            "decision_rule": (
                "UDP 收到响应 -> alive=true；UDP=ICMP不可达 且 TCP=明确拒绝 -> alive=false；"
                "TCP 端口开放且无 UDP ICMP 负向 -> alive=true（有限证据）；其余 -> alive='unknown'。"
            ),
            "proxy_environment_limitation": (
                "本机已设置 HTTP(S)_PROXY，用户实测直连境外 TCP 443 均 3s 超时；"
                "无正向证据只代表本机网络/代理条件无法确认，不等于节点失效；网络条件允许时应重测。"
            ),
        },
        "environment": env,
        "timeouts_seconds": {"dns": DNS_TIMEOUT, "tcp_connect": TCP_TIMEOUT, "udp_recv": UDP_TIMEOUT},
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
    return out


def write_report(now: str, out: dict) -> None:
    def esc(s) -> str:
        return str(s).replace("|", "\\|").replace("\n", " ")

    lines = [
        "# U4 hysteria2 节点测活报告", "",
        f"- 生成时间：{now}",
        f"- 输入：`us_nodes.json` 的 us_nodes 数组（{out['input_node_count']} 个美国 hysteria2 节点，只读）",
        f"- 手段：A TCP connect（{TCP_TIMEOUT:g}s 参考信号）+ B UDP datagram（{UDP_TIMEOUT:g}s）"
        "；C 代理环境仅作说明（HTTP CONNECT 不转发 UDP）",
        f"- 判定：alive {out['alive_count']} / unknown {out['unknown_count']} / dead {out['dead_count']}", "",
        "## 逐节点探测结果", "",
        "| # | server:port | 手段 | TCP结果 | UDP结果 | 综合判定 | 延迟(ms) | 原因 |",
        "|---|-------------|------|---------|---------|----------|----------|------|",
    ]

    all_records = out["alive_nodes"] + out["unknown_nodes"] + out["dead_nodes"]
    for idx, rec in enumerate(all_records, 1):
        lv = rec["_liveness"]
        sp = f"{rec.get('server', '')}:{rec.get('port', '')}"
        latency = lv["latency_ms"] if lv["latency_ms"] is not None else "-"
        lines.append(
            f"| {idx} | `{esc(sp)}` | {'+'.join(METHODS)} | {esc(lv['tcp']['detail'])} | "
            f"{esc(lv['udp']['detail'])} | {lv['alive']} | {latency} | {esc(lv['reason'])} |"
        )

    lines += [
        "", "## 汇总统计", "",
        f"- 输入节点数：{out['input_node_count']}",
        f"- alive（有正向证据，可进入订阅）：{out['alive_count']}",
        f"- unknown（本机环境无法确认，不进订阅、不删除）：{out['unknown_count']}",
        f"- dead（双重明确负向证据）：{out['dead_count']}",
        f"- 成功进入 alive_nodes 的 server："
        + (", ".join(f"`{r.get('server')}:{r.get('port')}`" for r in out["alive_nodes"]) if out["alive_nodes"] else "（无）"),
        "", "## 本机代理环境局限说明（重要）", "",
        "- 当前环境已设置 HTTP_PROXY/HTTPS_PROXY；用户实测直连境外 TCP 到 206.189.229.48:443、"
        "107.149.232.92:443 均 3s 超时，本机对境外直连很可能不通。",
        "- HTTP CONNECT 代理只转发 TCP、不转发 UDP，本脚本未借代理转发探测流量，"
        "因此 TCP/UDP 的失败都可能源于本机网络或 NAT/防火墙策略。",
        "- hysteria2 基于 QUIC/UDP，服务端通常不监听 TCP：TCP 超时属正常，绝不单凭 TCP 失败判节点死。",
        "- 结论口径：未知不等于失效，也不等于可用。报告中的 unknown 仅表示本机无法取得正向证据，"
        "不得据此断言节点已死；alive 只接受有据的正向信号（UDP 应答 / 明确端口开放），"
        "不使用 auth 等凭据作为判据，不伪造结果。",
        "", "## 空列表红线说明", "",
        "- 约束：测活通过后才能合并；当日 + 历史全失败时生成空列表，绝不静默保留失效旧节点。"
        "本单元为首次测活，无历史节点。",
    ]

    if out["alive_count"] == 0:
        lines.append(
            "- **本机代理环境下无节点获正向存活证据，按红线生成空列表**；"
            "不代表节点本身失效，网络条件允许时可重测。"
        )
    else:
        lines.append(
            "- 本批有节点取得正向存活证据，alive_nodes 仅收录这些节点；"
            "unknown 节点留在 unknown_nodes 中留痕，不静默删除。"
        )

    lines += [
        "", f"产出：`alive_nodes.json`（alive 节点 {out['alive_count']}）+ 本报告。",
    ]

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def main() -> int:
    now = utc_now_iso()
    print(f"[U4] 开始 {now}")
    nodes = load_us_nodes()
    print(f"[U4] 输入节点 {len(nodes)} 个，读取自 {US_NODES_PATH}")

    records: list[dict] = []
    for idx, node in enumerate(nodes, 1):
        server = str(node.get("server", ""))
        port = int(node.get("port", 443) or 443)
        addr, family, resolve_err = resolve_target(server)
        if resolve_err:
            tcp = {"status": "unresolved", "ok": False, "latency_ms": None, "detail": resolve_err}
            udp = {"status": "unresolved", "latency_ms": None, "detail": resolve_err}
        else:
            tcp = probe_tcp(addr, family, port)
            udp = probe_udp(addr, family, port)
        verdict = decide(resolve_err, tcp, udp)

        rec = dict(node)  # 继承原节点全部字段（含 auth/sni/port/skip-cert-verify）
        rec["_liveness"] = {
            "alive": verdict["alive"],
            "method": METHODS,
            "latency_ms": verdict["latency_ms"],
            "reason": verdict["reason"],
            "evidence": verdict["evidence"],
            "tcp": tcp,
            "udp": udp,
        }
        records.append(rec)
        print(f"  [{idx}/{len(nodes)}] {server}:{port} -> {verdict['alive']} ({verdict['evidence']})")

    env = proxy_env()
    out = write_alive_nodes(now, records, env)
    write_report(now, out)
    print(f"[U4] 完成：alive {out['alive_count']} / unknown {out['unknown_count']} / dead {out['dead_count']}")
    print(f"[U4] 产出：{ALIVE_PATH}")
    print(f"[U4] 产出：{REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
