#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""单点分层诊断：一个 host:port 到底卡在哪一层（DNS / TCP / TLS）。

用途：同一个机场「有的能用、有的不能用」时，逐层看差异，而不是只看客户端的一句"超时"。
    python scripts/diagnose_endpoint.py 66.163.112.31:443
    python scripts/diagnose_endpoint.py harbor.gerqix.online:443 --sni harbor.gerqix.online
    python scripts/diagnose_endpoint.py example.com:443 --repeat 3

层次判读：
    DNS 失败        → 域名解析被污染/该域名已废
    TCP 三次都超时  → IP/端口被挡（或服务端不收你这条线路）—— 换端口/换 IP 才有用
    TCP 通但 TLS 挂 → TLS 握手被干扰，或服务端 SNI 不认这个域名
    TLS 通          → 链路本身没问题，问题在协议层（密码/端口对应关系/服务端限流）
"""
from __future__ import annotations

import argparse
import socket
import ssl
import sys
import time


def parse_target(s: str) -> tuple[str, int]:
    host, _, port = s.rpartition(":")
    if not host:
        host, port = s, "443"
    return host.strip("[]"), int(port)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="host:port")
    ap.add_argument("--sni", default="", help="TLS SNI（默认用 host）")
    ap.add_argument("--repeat", type=int, default=3, help="TCP 重试次数")
    ap.add_argument("--timeout", type=float, default=5.0)
    args = ap.parse_args()

    host, port = parse_target(args.target)
    sni = args.sni or (host if not host.replace(".", "").isdigit() else "")

    print(f"目标 {host}:{port}  SNI={sni or '(无，纯 IP)'}")
    try:
        addrs = sorted({ai[4][0] for ai in socket.getaddrinfo(host, None)})
        print(f"  DNS      OK  {', '.join(addrs[:4])}")
        ip = addrs[0]
    except Exception as e:
        print(f"  DNS      FAIL {type(e).__name__} —— 域名不可解析（被污染或已废弃）")
        return 1

    ok = 0
    for i in range(args.repeat):
        t0 = time.time()
        try:
            s = socket.create_connection((ip, port), timeout=args.timeout)
            dt = int((time.time() - t0) * 1000)
            print(f"  TCP #{i + 1}   OK  {dt}ms")
            ok += 1
            s.close()
        except Exception as e:
            print(f"  TCP #{i + 1}   FAIL {type(e).__name__}")
        time.sleep(0.3)
    if ok == 0:
        print("  结论：IP/端口层就不通 —— 这条线路到该地址被挡，或服务端主动拒绝。"
              "换密码/换客户端都没用，只能换 IP 或换端口。")
        return 2

    if not sni:
        print("  结论：TCP 通；该节点是纯 IP 无 SNI，协议层无法在客户端外验证。")
        return 0

    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        t0 = time.time()
        ss = ctx.wrap_socket(socket.create_connection((ip, port), timeout=args.timeout),
                             server_hostname=sni)
        dt = int((time.time() - t0) * 1000)
        cert = ss.getpeercert() or {}
        print(f"  TLS      OK  {dt}ms  {ss.version()}  证书={cert.get('subject', '未取到（自签/空）')}")
        ss.close()
        print("  结论：链路（TCP+TLS）没问题 —— 还能连不上就是协议层：密码/端口/传输参数对不上，"
              "或服务端把这个账号限流了。")
        return 0
    except Exception as e:
        print(f"  TLS      FAIL {type(e).__name__}: {str(e)[:80]}")
        print("  结论：TCP 通但 TLS 挂 —— SNI 被干扰，或服务端不认这个 SNI/证书。")
        return 3


if __name__ == "__main__":
    sys.exit(main())
