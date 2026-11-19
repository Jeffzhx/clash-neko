# U3 GeoIP / 美国判定报告

- 生成时间：2026-11-19T16:51:05+00:00
- 查询日期：2026-11-20（本地）；UTC 2026-11-19
- 输入：`nodes_raw.json`（59 节点）；背景：`sources.json`（8 个低星来源）
- mmdb 路径：`D:/AI/2026-09-16-02-16-43/clash-nodes/kernel-test/Country.mmdb`
- mmdb 版本元数据：database_type=GeoLite2-Country；build_epoch=1784249267（2026-07-17T00:47:47+00:00）；ip_version=6；record_size=24
- 优质协议白名单：anytls, hysteria, hysteria2
- 结果：**US 优质节点 5** / 输入 59 / 过滤 54

## 逐节点判定（server / type / cc / cc_basis / 是否入选）

| # | server | type | cc | cc_basis | 是否入选 | 说明 |
|---|--------|------|----|----------|----------|------|
| 1 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 2 | `50.7.38.243` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 50.7.38.243 -> SE |
| 3 | `23c82941` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 4 | `a35c508f` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 5 | `549766c3` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 6 | `206.189.229.48` | hysteria2 | US | ip-literal | 是 | mmdb 命中 206.189.229.48 -> US |
| 7 | `47.89.232.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 47.89.232.46 -> US |
| 8 | `107.149.232.92` | hysteria2 | US | ip-literal | 是 | mmdb 命中 107.149.232.92 -> US |
| 9 | `66.94.121.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 66.94.121.46 -> US |
| 10 | `18.194.242.173` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.194.242.173 -> DE |
| 11 | `3.76.221.4` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.221.4 -> DE |
| 12 | `179.61.138.145` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 179.61.138.145 -> DE |
| 13 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 14 | `152.67.75.161` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 152.67.75.161 -> CH |
| 15 | `62.210.124.146` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.124.146 -> FR |
| 16 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 17 | `18.193.79.104` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.193.79.104 -> DE |
| 18 | `8.209.247.109` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.209.247.109 -> JP |
| 19 | `8.211.175.236` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.211.175.236 -> JP |
| 20 | `3.69.232.199` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.69.232.199 -> DE |
| 21 | `5.129.235.85` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 5.129.235.85 -> NL |
| 22 | `fa937345` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 23 | `152.70.237.123` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.70.237.123 -> KR |
| 24 | `129.159.156.109` | hysteria2 | IL | ip-literal | 否 | mmdb 命中 129.159.156.109 -> IL |
| 25 | `150` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 26 | `linlin` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 27 | `82.152.161.146` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 82.152.161.146 -> HK |
| 28 | `202.146.222.29` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.29 -> HK |
| 29 | `c3a8753e` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 30 | `202.146.222.174` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.174 -> HK |
| 31 | `vpn` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 32 | `202.146.222.89` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.89 -> HK |
| 33 | `srv` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 34 | `13.212.78.215` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 13.212.78.215 -> SG |
| 35 | `47.129.241.99` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 47.129.241.99 -> SG |
| 36 | `54.179.113.70` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 54.179.113.70 -> SG |
| 37 | `138.2.89.249` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.89.249 -> SG |
| 38 | `152.69.231.175` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.69.231.175 -> KR |
| 39 | `24.233.8.109` | hysteria2 | US | ip-literal | 是 | mmdb 命中 24.233.8.109 -> US |
| 40 | `138.2.73.238` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.73.238 -> SG |
| 41 | `77.90.15.183` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 77.90.15.183 -> DE |
| 42 | `31.57.248.176` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 31.57.248.176 -> HK |
| 43 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 44 | `549766c3` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 45 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 46 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 47 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 48 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 49 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 50 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 51 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 52 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 53 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 54 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 55 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 56 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 57 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 58 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 59 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |

## 按 cc 分布统计

| cc | 节点数 |
|----|--------|
| (unknown) | 14 |
| DE | 13 |
| HK | 5 |
| SG | 5 |
| US | 5 |
| CH | 4 |
| FR | 4 |
| SE | 3 |
| JP | 2 |
| KR | 2 |
| IL | 1 |
| NL | 1 |

## 过滤原因分类计数

| 原因类别 | 数量 | 含义 |
|----------|------|------|
| non_us_country | 40 | mmdb 命中但国家码非 US |
| unknown | 10 | DNS失败/超时、URI碎片假域名、私有保留段、mmdb非标准ISO码 |
| invalid_server | 4 | URL 编码垃圾 / 空 server，解码后仍非合法 hostname/IP |

## URL 编码碎片节点（单独点名）

- `github.com%2FAlvin9999` → 解码后 `github.com/Alvin9999`，非合法 hostname/IP，cc_basis=invalid_server，共 4 处，全部排除

## 判定规则与依据

- IP 字面量（IPv4/IPv6）：`ipaddress` 识别 → 私有/回环/保留段直接排除 → 其余查 mmdb，`country.iso_code` 回退 `registered_country`。
- 域名：仅对合法 FQDN 做 `socket.getaddrinfo`，用 ThreadPoolExecutor + future.result(timeout=4s) 防卡死；超时/失败按 unknown；多 IP 取首个公网 IP。
- mmdb 非标准 ISO 码（如 8.8.8.8 返回 `GOOGLE`）不认定为 US，按 unknown 排除。
- README URI 解析出的碎片假 hostname（如 `23c82941`/`150`/`linlin`/`c3a8753e`/`vpn`/`srv`）不是合法域名，不做 DNS 解析，按 unknown 排除。
- URL 含 `%XX` 的 server 先 `urllib.parse.unquote`；解码后仍非合法 hostname/IP 判 invalid_server。
- 入选红线：`cc == "US"` 且 `type ∈ {hysteria, hysteria2, anytls}`。

产出：`us_nodes.json`（US 节点 5）+ 本报告。
