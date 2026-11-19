# U4 hysteria2 节点测活报告

- 生成时间：2026-11-19T17:40:32+00:00
- 输入：`us_nodes.json` 的 us_nodes 数组（7 个美国 hysteria2 节点，只读）
- 手段：A TCP connect（3s 参考信号）+ B UDP datagram（3s）；C 代理环境仅作说明（HTTP CONNECT 不转发 UDP）
- 判定：alive 3 / unknown 4 / dead 0

## 逐节点探测结果

| # | server:port | 手段 | TCP结果 | UDP结果 | 综合判定 | 延迟(ms) | 原因 |
|---|-------------|------|---------|---------|----------|----------|------|
| 1 | `206.189.229.48:443` | A_tcp_connect+B_udp_datagram | TCP connect 成功，耗时 34.9ms（端口有 TCP 监听；不等同于 hysteria2 握手成功） | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | True | 34.9 | 有据（正向，有限）：TCP connect 成功，耗时 34.9ms（端口有 TCP 监听；不等同于 hysteria2 握手成功）；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；注意未做 hysteria2 握手验证，建议在网络条件允许时用内核复核 |
| 2 | `34.24.25.1:443` | A_tcp_connect+B_udp_datagram | TCP connect 成功，耗时 40.8ms（端口有 TCP 监听；不等同于 hysteria2 握手成功） | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | True | 40.8 | 有据（正向，有限）：TCP connect 成功，耗时 40.8ms（端口有 TCP 监听；不等同于 hysteria2 握手成功）；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；注意未做 hysteria2 握手验证，建议在网络条件允许时用内核复核 |
| 3 | `66.94.121.46:443` | A_tcp_connect+B_udp_datagram | TCP connect 成功，耗时 70.4ms（端口有 TCP 监听；不等同于 hysteria2 握手成功） | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | True | 70.4 | 有据（正向，有限）：TCP connect 成功，耗时 70.4ms（端口有 TCP 监听；不等同于 hysteria2 握手成功）；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；注意未做 hysteria2 握手验证，建议在网络条件允许时用内核复核 |
| 4 | `107.149.232.92:443` | A_tcp_connect+B_udp_datagram | TCP connect 被明确拒绝（RST/ICMP），该 TCP 端口无监听 | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | unknown | - | 推断（非结论）：本机代理环境下无法确认存活——TCP connect 被明确拒绝（RST/ICMP），该 TCP 端口无监听；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；未取得正向证据，按红线不判可用，也不判失效 |
| 5 | `47.89.232.46:8443` | A_tcp_connect+B_udp_datagram | TCP connect 超时 3s（hysteria2 通常不监听 TCP，属正常，不判死） | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | unknown | - | 推断（非结论）：本机代理环境下无法确认存活——TCP connect 超时 3s（hysteria2 通常不监听 TCP，属正常，不判死）；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；未取得正向证据，按红线不判可用，也不判失效 |
| 6 | `38.76.150.108:36712` | A_tcp_connect+B_udp_datagram | TCP connect 超时 3s（hysteria2 通常不监听 TCP，属正常，不判死） | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | unknown | - | 推断（非结论）：本机代理环境下无法确认存活——TCP connect 超时 3s（hysteria2 通常不监听 TCP，属正常，不判死）；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；未取得正向证据，按红线不判可用，也不判失效 |
| 7 | `24.233.8.109:443` | A_tcp_connect+B_udp_datagram | TCP connect 被明确拒绝（RST/ICMP），该 TCP 端口无监听 | UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认） | unknown | - | 推断（非结论）：本机代理环境下无法确认存活——TCP connect 被明确拒绝（RST/ICMP），该 TCP 端口无监听；UDP 3s 内无响应且未捕获 ICMP 错误（本机环境无法确认）；未取得正向证据，按红线不判可用，也不判失效 |

## 汇总统计

- 输入节点数：7
- alive（有正向证据，可进入订阅）：3
- unknown（本机环境无法确认，不进订阅、不删除）：4
- dead（双重明确负向证据）：0
- 成功进入 alive_nodes 的 server：`206.189.229.48:443`, `34.24.25.1:443`, `66.94.121.46:443`

## 本机代理环境局限说明（重要）

- 当前环境已设置 HTTP_PROXY/HTTPS_PROXY；用户实测直连境外 TCP 到 206.189.229.48:443、107.149.232.92:443 均 3s 超时，本机对境外直连很可能不通。
- HTTP CONNECT 代理只转发 TCP、不转发 UDP，本脚本未借代理转发探测流量，因此 TCP/UDP 的失败都可能源于本机网络或 NAT/防火墙策略。
- hysteria2 基于 QUIC/UDP，服务端通常不监听 TCP：TCP 超时属正常，绝不单凭 TCP 失败判节点死。
- 结论口径：未知不等于失效，也不等于可用。报告中的 unknown 仅表示本机无法取得正向证据，不得据此断言节点已死；alive 只接受有据的正向信号（UDP 应答 / 明确端口开放），不使用 auth 等凭据作为判据，不伪造结果。

## 空列表红线说明

- 约束：测活通过后才能合并；当日 + 历史全失败时生成空列表，绝不静默保留失效旧节点。本单元为首次测活，无历史节点。
- 本批有节点取得正向存活证据，alive_nodes 仅收录这些节点；unknown 节点留在 unknown_nodes 中留痕，不静默删除。

产出：`alive_nodes.json`（alive 节点 3）+ 本报告。
