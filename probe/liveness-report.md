# U4 内核级真实测活报告

- 生成时间：2026-11-19T19:05:06+00:00
- 引擎：mihomo external-controller `/proxies/{name}/delay`（内核 v1.19.34）
- 测活 URL：`http://www.gstatic.com/generate_204`；单节点超时 8000ms
- 判定：alive 0 / dead 7 / unknown 0

## 逐节点（server:port / 判定 / 延迟 / 依据）

| # | server:port | 判定 | 延迟(ms) | 依据 |
|---|-------------|------|----------|------|
| 1 | `107.149.232.92:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 2 | `206.189.229.48:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 3 | `47.89.232.46:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 4 | `34.24.25.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 5 | `38.76.150.108:36712` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 6 | `66.94.121.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 7 | `24.233.8.109:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |

## 说明

- 本报告为**协议级**测活：内核真实完成 hysteria2/anytls 握手并经代理发起 HTTP 请求，
  比端口级 TCP/UDP 探测可靠得多；alive 的节点经客户端导入理应可用。
- 国内用户仍可能受本地网络/GFW 影响，最终以客户端实测为准。

