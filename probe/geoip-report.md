# U3 GeoIP / 美国判定报告

- 生成时间：2026-11-19T18:12:06+00:00
- 查询日期：2026-11-19（本地）；UTC 2026-11-19
- 输入：`nodes_raw.json`（81 节点）；背景：`sources.json`（8 个低星来源）
- mmdb 路径：`/home/runner/work/_temp/Country.mmdb`
- mmdb 版本元数据：database_type=GeoLite2-Country；build_epoch=1794932458（2026-11-17T16:20:58+00:00）；ip_version=6；record_size=24
- 优质协议白名单：anytls, hysteria, hysteria2
- 结果：**US 优质节点 7** / 输入 81 / 过滤 74

## 逐节点判定（server / type / cc / cc_basis / 是否入选）

| # | server | type | cc | cc_basis | 是否入选 | 说明 |
|---|--------|------|----|----------|----------|------|
| 1 | `23c82941` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 2 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 3 | `50.7.38.243` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 50.7.38.243 -> SE |
| 4 | `a35c508f` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 5 | `549766c3` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 6 | `107.149.232.92` | hysteria2 | US | ip-literal | 是 | mmdb 命中 107.149.232.92 -> US |
| 7 | `206.189.229.48` | hysteria2 | US | ip-literal | 是 | mmdb 命中 206.189.229.48 -> US |
| 8 | `47.89.232.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 47.89.232.46 -> US |
| 9 | `34.24.25.1` | hysteria2 | US | ip-literal | 是 | mmdb 命中 34.24.25.1 -> US |
| 10 | `38.76.150.108` | hysteria2 | US | ip-literal | 是 | mmdb 命中 38.76.150.108 -> US |
| 11 | `66.94.121.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 66.94.121.46 -> US |
| 12 | `starlink` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 13 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 14 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 15 | `vpn` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 16 | `18.194.242.173` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.194.242.173 -> DE |
| 17 | `62.210.124.146` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.124.146 -> FR |
| 18 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 19 | `3.69.232.199` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.69.232.199 -> DE |
| 20 | `3.76.221.4` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.221.4 -> DE |
| 21 | `8.211.175.236` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.211.175.236 -> JP |
| 22 | `18.193.79.104` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.193.79.104 -> DE |
| 23 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 24 | `152.67.75.161` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 152.67.75.161 -> CH |
| 25 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 26 | `ca60984f` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 27 | `fa937345` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 28 | `152.70.237.123` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.70.237.123 -> KR |
| 29 | `132.226.226.189` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 132.226.226.189 -> KR |
| 30 | `138.3.208.26` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 138.3.208.26 -> JP |
| 31 | `linlin` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 32 | `150.230.252.217` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 150.230.252.217 -> KR |
| 33 | `152.67.115.203` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 152.67.115.203 -> AU |
| 34 | `82.152.161.146` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 82.152.161.146 -> HK |
| 35 | `c3a8753e` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 36 | `202.146.222.29` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.29 -> HK |
| 37 | `152.67.200.82` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.67.200.82 -> KR |
| 38 | `202.146.222.89` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.89 -> HK |
| 39 | `103.88.243.142` | hysteria2 | RU | ip-literal | 否 | mmdb 命中 103.88.243.142 -> RU |
| 40 | `103.115.109.49` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 103.115.109.49 -> TW |
| 41 | `srv` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 42 | `150` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 43 | `47.129.241.99` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 47.129.241.99 -> SG |
| 44 | `13.212.78.215` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 13.212.78.215 -> SG |
| 45 | `54.179.113.70` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 54.179.113.70 -> SG |
| 46 | `160.187.100.109` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 160.187.100.109 -> TW |
| 47 | `138.2.89.249` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.89.249 -> SG |
| 48 | `9a9f167d` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 49 | `129.159.156.109` | hysteria2 | IL | ip-literal | 否 | mmdb 命中 129.159.156.109 -> IL |
| 50 | `152.69.231.175` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.69.231.175 -> KR |
| 51 | `24.233.8.109` | hysteria2 | US | ip-literal | 是 | mmdb 命中 24.233.8.109 -> US |
| 52 | `138.2.73.238` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.73.238 -> SG |
| 53 | `5.129.235.85` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 5.129.235.85 -> NL |
| 54 | `31.57.248.176` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 31.57.248.176 -> HK |
| 55 | `8.209.247.109` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.209.247.109 -> JP |
| 56 | `274cf8bb` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 57 | `185.156.44.99` | hysteria2 | RO | ip-literal | 否 | mmdb 命中 185.156.44.99 -> RO |
| 58 | `1d1d36cd` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 59 | `167.17.179.207` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 167.17.179.207 -> JP |
| 60 | `150.230.229.100` | hysteria2 | BR | ip-literal | 否 | mmdb 命中 150.230.229.100 -> BR |
| 61 | `152.32.254.68` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 152.32.254.68 -> HK |
| 62 | `159.13.55.48` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 159.13.55.48 -> AU |
| 63 | `ca60984f` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 64 | `549766c3` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 65 | `9a9f167d` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 66 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 67 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 68 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 69 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 70 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 71 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 72 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 73 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 74 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 75 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 76 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 77 | `github.com%2FAlvin9999` | hysteria2 | - | invalid_server | 否 | URL编码碎片：'github.com%2FAlvin9999' -> 'github.com/Alvin9999' 非合法 hostname/IP |
| 78 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 79 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 80 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 81 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |

## 按 cc 分布统计

| cc | 节点数 |
|----|--------|
| (unknown) | 21 |
| DE | 12 |
| US | 7 |
| CH | 5 |
| FR | 5 |
| HK | 5 |
| KR | 5 |
| SG | 5 |
| JP | 4 |
| SE | 3 |
| AU | 2 |
| TW | 2 |
| BR | 1 |
| IL | 1 |
| NL | 1 |
| RO | 1 |
| RU | 1 |

## 过滤原因分类计数

| 原因类别 | 数量 | 含义 |
|----------|------|------|
| non_us_country | 53 | mmdb 命中但国家码非 US |
| unknown | 17 | DNS失败/超时、URI碎片假域名、私有保留段、mmdb非标准ISO码 |
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

产出：`us_nodes.json`（US 节点 7）+ 本报告。
