# U3 GeoIP / 美国判定报告

- 生成时间：2026-11-19T20:13:20+00:00
- 查询日期：2026-11-19（本地）；UTC 2026-11-19
- 输入：`nodes_raw.json`（1205 节点）；背景：`sources.json`（23 个低星来源）
- mmdb 路径：`/home/runner/work/_temp/Country.mmdb`
- mmdb 版本元数据：database_type=GeoLite2-Country；build_epoch=1794932458（2026-11-17T16:20:58+00:00）；ip_version=6；record_size=24
- 优质协议白名单：anytls, hysteria, hysteria2, trojan, tuic, vless
- 结果：**US 优质节点 435** / 输入 1205 / 过滤 770

## 逐节点判定（server / type / cc / cc_basis / 是否入选）

| # | server | type | cc | cc_basis | 是否入选 | 说明 |
|---|--------|------|----|----------|----------|------|
| 1 | `169.40.42.168` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.168 -> DE |
| 2 | `169.40.42.74` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.74 -> DE |
| 3 | `216.152.155.23` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.23 -> US |
| 4 | `216.152.147.85` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.85 -> CA |
| 5 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 6 | `185.95.231.156` | vless | IL | ip-literal | 否 | mmdb 命中 185.95.231.156 -> IL |
| 7 | `169.40.42.163` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.163 -> DE |
| 8 | `169.40.42.231` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.231 -> DE |
| 9 | `216.106.186.82` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.82 -> US |
| 10 | `169.40.42.90` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.90 -> DE |
| 11 | `216.152.156.81` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.81 -> US |
| 12 | `216.152.147.48` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.48 -> CA |
| 13 | `66.163.112.121` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.121 -> US |
| 14 | `167.88.61.175` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.175 -> US |
| 15 | `167.88.61.52` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.52 -> US |
| 16 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 17 | `216.152.155.59` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.59 -> US |
| 18 | `167.88.61.193` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.193 -> US |
| 19 | `www.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.66 -> US |
| 20 | `130.12.242.106` | vless | NL | ip-literal | 否 | mmdb 命中 130.12.242.106 -> NL |
| 21 | `38.107.232.36` | vless | US | ip-literal | 是 | mmdb 命中 38.107.232.36 -> US |
| 22 | `167.88.61.85` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.85 -> US |
| 23 | `216.152.155.158` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.158 -> US |
| 24 | `167.88.61.198` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.198 -> US |
| 25 | `216.106.186.155` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.155 -> US |
| 26 | `66.163.112.31` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.31 -> US |
| 27 | `104.168.109.213` | vless | US | ip-literal | 是 | mmdb 命中 104.168.109.213 -> US |
| 28 | `66.163.114.45` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.45 -> US |
| 29 | `66.163.112.76` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.76 -> US |
| 30 | `169.40.42.35` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.35 -> DE |
| 31 | `216.152.147.93` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.93 -> CA |
| 32 | `216.152.155.50` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.50 -> US |
| 33 | `169.40.42.229` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.229 -> DE |
| 34 | `nl.point.cookie-line.cc` | vless | NL | domain-resolved | 否 | 解析到 87.58.201.5 -> NL |
| 35 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 36 | `66.163.112.142` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.142 -> US |
| 37 | `198.247.127.131` | vless | US | ip-literal | 是 | mmdb 命中 198.247.127.131 -> US |
| 38 | `147.45.47.101` | vless | RU | ip-literal | 否 | mmdb 命中 147.45.47.101 -> RU |
| 39 | `167.88.61.20` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.20 -> US |
| 40 | `leviko-fr5882.shopingggg.ir` | vless | FR | domain-resolved | 否 | 解析到 158.220.113.176 -> FR |
| 41 | `159.89.87.21` | vless | US | ip-literal | 是 | mmdb 命中 159.89.87.21 -> US |
| 42 | `ww13.levikogjgfdd.ir` | vless | US | domain-resolved | 是 | 解析到 15.204.97.206 -> US |
| 43 | `170.101.101.67` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.67 -> US |
| 44 | `blog.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.32 -> US |
| 45 | `45.144.112.55` | vless | US | ip-literal | 是 | mmdb 命中 45.144.112.55 -> US |
| 46 | `66.163.112.13` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.13 -> US |
| 47 | `216.106.186.33` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.33 -> US |
| 48 | `216.152.147.201` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.201 -> CA |
| 49 | `51.158.206.80` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.80 -> NL |
| 50 | `169.197.140.169` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.169 -> US |
| 51 | `187.7.206.179` | vless | DE | ip-literal | 否 | mmdb 命中 187.7.206.179 -> DE |
| 52 | `195.123.240.65` | vless | US | ip-literal | 是 | mmdb 命中 195.123.240.65 -> US |
| 53 | `169.40.42.202` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.202 -> DE |
| 54 | `15.204.97.195` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.195 -> US |
| 55 | `51.158.206.34` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.34 -> NL |
| 56 | `193.108.119.96` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.96 -> DE |
| 57 | `51.158.206.20` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.20 -> NL |
| 58 | `177.177.215.45` | vless | NL | ip-literal | 否 | mmdb 命中 177.177.215.45 -> NL |
| 59 | `169.197.140.171` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.171 -> US |
| 60 | `212.34.137.105` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 212.34.137.105 -> NL |
| 61 | `51.158.206.25` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.25 -> NL |
| 62 | `216.106.186.32` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.32 -> US |
| 63 | `179.254.191.251` | hysteria2 | US | ip-literal | 是 | mmdb 命中 179.254.191.251 -> US |
| 64 | `free-amsterdam-node-1.cloudwidecdn.com` | vless | NL | domain-resolved | 否 | 解析到 86.54.28.75 -> NL |
| 65 | `37.235.247.81` | vless | RU | ip-literal | 否 | mmdb 命中 37.235.247.81 -> RU |
| 66 | `50.7.38.243` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 50.7.38.243 -> SE |
| 67 | `66.163.122.25` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.25 -> US |
| 68 | `138.124.86.230` | vless | CH | ip-literal | 否 | mmdb 命中 138.124.86.230 -> CH |
| 69 | `187.7.206.176` | vless | DE | ip-literal | 否 | mmdb 命中 187.7.206.176 -> DE |
| 70 | `51.158.206.87` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.87 -> NL |
| 71 | `51.158.206.12` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.12 -> NL |
| 72 | `189.74.115.27` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.115.27 -> RU |
| 73 | `148.135.86.162` | vless | US | ip-literal | 是 | mmdb 命中 148.135.86.162 -> US |
| 74 | `94.183.164.119` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 75 | `193.108.119.193` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.193 -> DE |
| 76 | `uspanel.unixzone.us` | vless | US | domain-resolved | 是 | 解析到 69.48.201.136 -> US |
| 77 | `ams2.shtil.io` | vless | NL | domain-resolved | 否 | 解析到 177.177.215.45 -> NL |
| 78 | `66.163.122.26` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.26 -> US |
| 79 | `66.163.114.106` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.106 -> US |
| 80 | `216.152.155.131` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.131 -> US |
| 81 | `64.176.7.205` | trojan | CL | ip-literal | 否 | mmdb 命中 64.176.7.205 -> CL |
| 82 | `69.48.201.136` | vless | US | ip-literal | 是 | mmdb 命中 69.48.201.136 -> US |
| 83 | `45.63.30.142` | trojan | AU | ip-literal | 否 | mmdb 命中 45.63.30.142 -> AU |
| 84 | `78.17.215.136` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.136 -> DE |
| 85 | `78.17.215.137` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.137 -> DE |
| 86 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 87 | `86.38.247.109` | trojan | SG | ip-literal | 否 | mmdb 命中 86.38.247.109 -> SG |
| 88 | `steel7.hadsvpn.com` | hysteria2 | DE | domain-resolved | 否 | 解析到 201.58.142.83 -> DE |
| 89 | `216.106.186.46` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.46 -> US |
| 90 | `91.107.188.129` | vless | DE | ip-literal | 否 | mmdb 命中 91.107.188.129 -> DE |
| 91 | `216.152.147.152` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.152 -> CA |
| 92 | `51.158.206.103` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.103 -> NL |
| 93 | `138.124.70.41` | vless | FR | ip-literal | 否 | mmdb 命中 138.124.70.41 -> FR |
| 94 | `216.152.155.176` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.176 -> US |
| 95 | `143.246.60.254` | vless | US | ip-literal | 是 | mmdb 命中 143.246.60.254 -> US |
| 96 | `51.158.206.19` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.19 -> NL |
| 97 | `212.102.38.25` | vless | CZ | ip-literal | 否 | mmdb 命中 212.102.38.25 -> CZ |
| 98 | `216.152.156.42` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.42 -> US |
| 99 | `216.152.155.54` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.54 -> US |
| 100 | `31.59.169.225` | hysteria2 | AE | ip-literal | 否 | mmdb 命中 31.59.169.225 -> AE |
| 101 | `141.227.170.220` | vless | FR | ip-literal | 否 | mmdb 命中 141.227.170.220 -> FR |
| 102 | `51.158.206.96` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.96 -> NL |
| 103 | `195.211.98.43` | vless | US | ip-literal | 是 | mmdb 命中 195.211.98.43 -> US |
| 104 | `resources.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.33 -> US |
| 105 | `216.238.104.154` | trojan | BR | ip-literal | 否 | mmdb 命中 216.238.104.154 -> BR |
| 106 | `95.143.196.32` | trojan | SE | ip-literal | 否 | mmdb 命中 95.143.196.32 -> SE |
| 107 | `167.17.179.207` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 167.17.179.207 -> JP |
| 108 | `51.158.206.98` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.98 -> NL |
| 109 | `66.163.122.30` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.30 -> US |
| 110 | `51.158.206.86` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.86 -> NL |
| 111 | `169.40.42.89` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.89 -> DE |
| 112 | `87.58.201.5` | vless | NL | ip-literal | 否 | mmdb 命中 87.58.201.5 -> NL |
| 113 | `169.197.140.214` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.214 -> US |
| 114 | `88.216.214.159` | vless | SE | ip-literal | 否 | mmdb 命中 88.216.214.159 -> SE |
| 115 | `66.163.114.245` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.245 -> US |
| 116 | `216.152.156.212` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.212 -> US |
| 117 | `216.152.156.159` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.159 -> US |
| 118 | `216.152.147.79` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.79 -> CA |
| 119 | `66.23.203.21` | trojan | US | ip-literal | 是 | mmdb 命中 66.23.203.21 -> US |
| 120 | `69.164.240.85` | trojan | US | ip-literal | 是 | mmdb 命中 69.164.240.85 -> US |
| 121 | `158.220.113.176` | vless | FR | ip-literal | 否 | mmdb 命中 158.220.113.176 -> FR |
| 122 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 123 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 124 | `18.193.79.104` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.193.79.104 -> DE |
| 125 | `167.17.69.171` | vless | US | ip-literal | 是 | mmdb 命中 167.17.69.171 -> US |
| 126 | `82.39.171.12` | vless | GB | ip-literal | 否 | mmdb 命中 82.39.171.12 -> GB |
| 127 | `157.254.38.210` | trojan | US | ip-literal | 是 | mmdb 命中 157.254.38.210 -> US |
| 128 | `sclass-c2.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 129 | `119.28.90.128` | vless | HK | ip-literal | 否 | mmdb 命中 119.28.90.128 -> HK |
| 130 | `in.smrtai.top` | vless | IN | domain-resolved | 否 | 解析到 178.212.35.198 -> IN |
| 131 | `83.141.92.168` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.92.168 -> IE |
| 132 | `GozargahAzad&security=reality&encryption=none&pbk=ZSmetD4e9QG5CiXhniHg5HJB68L4kwbgAkJmMHtVwEE&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=7aa271t.es1.h1clayd.click&sid=42426c882c5fcd41` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 133 | `87.120.92.68` | vless | BG | ip-literal | 否 | mmdb 命中 87.120.92.68 -> BG |
| 134 | `slot3.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.253.106 -> DE |
| 135 | `slot1.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.252.238 -> DE |
| 136 | `85.192.49.30` | vless | FI | ip-literal | 否 | mmdb 命中 85.192.49.30 -> FI |
| 137 | `94.183.164.176` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.176 -> NL |
| 138 | `leviko-cl7123.shopingggg.ir` | trojan | CL | domain-resolved | 否 | 解析到 64.176.7.205 -> CL |
| 139 | `31.58.117.133` | hysteria2 | PL | ip-literal | 否 | mmdb 命中 31.58.117.133 -> PL |
| 140 | `146.19.254.171` | vless | NL | ip-literal | 否 | mmdb 命中 146.19.254.171 -> NL |
| 141 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 142 | `191.217.204.101` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 191.217.204.101 -> DE |
| 143 | `158.247.253.243` | trojan | KR | ip-literal | 否 | mmdb 命中 158.247.253.243 -> KR |
| 144 | `66.163.122.46` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.46 -> US |
| 145 | `139.84.231.142` | trojan | ZA | ip-literal | 否 | mmdb 命中 139.84.231.142 -> ZA |
| 146 | `15.235.184.127` | trojan | SG | ip-literal | 否 | mmdb 命中 15.235.184.127 -> SG |
| 147 | `51.158.206.97` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.97 -> NL |
| 148 | `62.210.91.2` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.91.2 -> FR |
| 149 | `free.fugui.lol` | vless | TW | domain-resolved | 否 | 解析到 1.160.12.70 -> TW |
| 150 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 151 | `185.176.9.26` | vless | ES | ip-literal | 否 | mmdb 命中 185.176.9.26 -> ES |
| 152 | `45.137.201.211` | hysteria2 | IT | ip-literal | 否 | mmdb 命中 45.137.201.211 -> IT |
| 153 | `185.65.202.122` | vless | DE | ip-literal | 否 | mmdb 命中 185.65.202.122 -> DE |
| 154 | `172.233.197.235` | vless | US | ip-literal | 是 | mmdb 命中 172.233.197.235 -> US |
| 155 | `150.241.92.23` | vless | NL | ip-literal | 否 | mmdb 命中 150.241.92.23 -> NL |
| 156 | `78.17.215.141` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.141 -> DE |
| 157 | `143.246.62.191` | vless | US | ip-literal | 是 | mmdb 命中 143.246.62.191 -> US |
| 158 | `94.183.164.96` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.96 -> NL |
| 159 | `213.199.57.127` | vless | FR | ip-literal | 否 | mmdb 命中 213.199.57.127 -> FR |
| 160 | `217.60.25.100` | vless | PL | ip-literal | 否 | mmdb 命中 217.60.25.100 -> PL |
| 161 | `138.124.9.201` | vless | CH | ip-literal | 否 | mmdb 命中 138.124.9.201 -> CH |
| 162 | `62.60.232.250` | vless | HK | ip-literal | 否 | mmdb 命中 62.60.232.250 -> HK |
| 163 | `5.35.44.218` | vless | NL | ip-literal | 否 | mmdb 命中 5.35.44.218 -> NL |
| 164 | `89.125.175.172` | vless | AE | ip-literal | 否 | mmdb 命中 89.125.175.172 -> AE |
| 165 | `dfsto.whitenw.net` | vless | RU | domain-resolved | 否 | 解析到 188.225.42.130 -> RU |
| 166 | `leviko-ru1148.shopingggg.ir` | vless | RU | domain-resolved | 否 | 解析到 37.235.247.81 -> RU |
| 167 | `47.89.232.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 47.89.232.46 -> US |
| 168 | `8.211.175.236` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.211.175.236 -> JP |
| 169 | `152.70.237.123` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.70.237.123 -> KR |
| 170 | `129.225.181.46` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 129.225.181.46 -> JP |
| 171 | `staticxfastline.taymaztest.ir` | trojan | LU | domain-resolved | 否 | 解析到 193.57.88.100 -> LU |
| 172 | `sclass-00.catcat321.com` | trojan | HK | domain-resolved | 否 | 解析到 16.106.31.174 -> HK |
| 173 | `sclass-b1.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 174 | `147.224.54.25` | vless | US | ip-literal | 是 | mmdb 命中 147.224.54.25 -> US |
| 175 | `152.228.139.33` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.139.33 -> FR |
| 176 | `control-shared.78778m.cn` | trojan | CN | domain-resolved | 否 | 解析到 222.79.111.139 -> CN |
| 177 | `66.94.121.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 66.94.121.46 -> US |
| 178 | `34.24.25.1` | hysteria2 | US | ip-literal | 是 | mmdb 命中 34.24.25.1 -> US |
| 179 | `vpn-us-001.fastervpn.world` | hysteria2 | US | domain-resolved | 是 | 解析到 3.12.74.205 -> US |
| 180 | `GozargahAzad&sni=www.microsoft.com&insecure=1` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 181 | `8.209.247.109` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.209.247.109 -> JP |
| 182 | `starlink-ft.251313.xyz` | hysteria2 | US | domain-resolved | 是 | 解析到 192.9.142.40 -> US |
| 183 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 184 | `18.194.242.173` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.194.242.173 -> DE |
| 185 | `3.69.232.199` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.69.232.199 -> DE |
| 186 | `vpn-tw-002.fastervpn.world` | hysteria2 | TW | domain-resolved | 否 | 解析到 160.187.100.109 -> TW |
| 187 | `103.115.109.49` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 103.115.109.49 -> TW |
| 188 | `160.187.100.109` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 160.187.100.109 -> TW |
| 189 | `202.146.222.89` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.89 -> HK |
| 190 | `202.146.222.174` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.174 -> HK |
| 191 | `82.40.63.138` | hysteria2 | PL | ip-literal | 否 | mmdb 命中 82.40.63.138 -> PL |
| 192 | `47.129.241.99` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 47.129.241.99 -> SG |
| 193 | `vpn-sg-001.fastervpn.world` | hysteria2 | SG | domain-resolved | 否 | 解析到 13.212.215.138 -> SG |
| 194 | `3.76.221.4` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.221.4 -> DE |
| 195 | `vpn-hk-004.fastervpn.world` | hysteria2 | HK | domain-resolved | 否 | 解析到 202.146.222.54 -> HK |
| 196 | `80.47.10.106` | vless | PL | ip-literal | 否 | mmdb 命中 80.47.10.106 -> PL |
| 197 | `5.129.235.85` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 5.129.235.85 -> NL |
| 198 | `87.121.112.83` | hysteria2 | BG | ip-literal | 否 | mmdb 命中 87.121.112.83 -> BG |
| 199 | `136.176.68.34` | vless | GB | ip-literal | 否 | mmdb 命中 136.176.68.34 -> GB |
| 200 | `45.192.12.92` | vless | PL | ip-literal | 否 | mmdb 命中 45.192.12.92 -> PL |
| 201 | `ee.veltrosub.com` | vless | US | domain-resolved | 是 | 解析到 187.55.172.33 -> US |
| 202 | `93.123.101.198` | vless | DE | ip-literal | 否 | mmdb 命中 93.123.101.198 -> DE |
| 203 | `SC-TheNetherlands2.09vpn.com` | vless | NL | domain-resolved | 否 | 解析到 163.172.213.174 -> NL |
| 204 | `57.129.132.223` | vless | GB | ip-literal | 否 | mmdb 命中 57.129.132.223 -> GB |
| 205 | `sc-thenetherlands1.09vpn.com` | vless | NL | domain-resolved | 否 | 解析到 163.172.214.188 -> NL |
| 206 | `sajed.kdns.fr` | vless | SE | domain-resolved | 否 | 解析到 13.60.56.123 -> SE |
| 207 | `57.129.41.216` | vless | DE | ip-literal | 否 | mmdb 命中 57.129.41.216 -> DE |
| 208 | `platform117.golnamakcert.top` | vless | BR | domain-resolved | 否 | 解析到 202.61.73.205 -> BR |
| 209 | `platform101.golnamakcert.top` | vless | BR | domain-resolved | 否 | 解析到 202.61.73.196 -> BR |
| 210 | `platform102.golnamakcert.top` | vless | BR | domain-resolved | 否 | 解析到 202.61.73.152 -> BR |
| 211 | `15.204.97.206` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.206 -> US |
| 212 | `15.204.97.198` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.198 -> US |
| 213 | `138.124.125.193` | vless | GB | ip-literal | 否 | mmdb 命中 138.124.125.193 -> GB |
| 214 | `107.148.76.243` | vless | JP | ip-literal | 否 | mmdb 命中 107.148.76.243 -> JP |
| 215 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 216 | `51.158.206.8` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.8 -> NL |
| 217 | `51.158.206.93` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.93 -> NL |
| 218 | `51.158.206.29` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.29 -> NL |
| 219 | `leviko-de3504.shopingggg.ir` | vless | DE | domain-resolved | 否 | 解析到 185.44.64.166 -> DE |
| 220 | `185.44.64.166` | vless | DE | ip-literal | 否 | mmdb 命中 185.44.64.166 -> DE |
| 221 | `2.27.174.182` | vless | TW | ip-literal | 否 | mmdb 命中 2.27.174.182 -> TW |
| 222 | `157.180.98.124` | vless | FI | ip-literal | 否 | mmdb 命中 157.180.98.124 -> FI |
| 223 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 224 | `2.26.204.46` | vless | HK | ip-literal | 否 | mmdb 命中 2.26.204.46 -> HK |
| 225 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 226 | `103.106.229.177` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.177 -> SG |
| 227 | `free.fugui.lol` | vless | TW | domain-resolved | 否 | 解析到 1.160.12.70 -> TW |
| 228 | `157.22.240.62` | vless | RU | ip-literal | 否 | mmdb 命中 157.22.240.62 -> RU |
| 229 | `147.45.66.208` | vless | DE | ip-literal | 否 | mmdb 命中 147.45.66.208 -> DE |
| 230 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 231 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 232 | `13.210.14.142` | vless | AU | ip-literal | 否 | mmdb 命中 13.210.14.142 -> AU |
| 233 | `46.28.69.123` | vless | DE | ip-literal | 否 | mmdb 命中 46.28.69.123 -> DE |
| 234 | `leviko-de8370.shopingggg.ir` | vless | DE | domain-resolved | 否 | 解析到 78.17.215.133 -> DE |
| 235 | `2.27.14.247` | vless | SE | ip-literal | 否 | mmdb 命中 2.27.14.247 -> SE |
| 236 | `144.31.215.223` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.223 -> DE |
| 237 | `144.31.215.231` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.231 -> DE |
| 238 | `81.90.21.200` | vless | SE | ip-literal | 否 | mmdb 命中 81.90.21.200 -> SE |
| 239 | `84.32.83.197` | vless | LT | ip-literal | 否 | mmdb 命中 84.32.83.197 -> LT |
| 240 | `62.210.91.10` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.91.10 -> FR |
| 241 | `Fear_Config---&headerType=none&type=tcp&flow=xtls-rprx-vision&sni=fuck.rkn&sid=01` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 242 | `support.zoom.us` | vless | US | domain-resolved | 是 | 解析到 170.114.46.6 -> US |
| 243 | `154.90.62.70` | trojan | KR | ip-literal | 否 | mmdb 命中 154.90.62.70 -> KR |
| 244 | `178.94.25.73` | vless | SG | ip-literal | 否 | mmdb 命中 178.94.25.73 -> SG |
| 245 | `vps3.nemnogogo.com` | vless | RU | domain-resolved | 否 | 解析到 201.51.12.98 -> RU |
| 246 | `84.32.209.118` | vless | LT | ip-literal | 否 | mmdb 命中 84.32.209.118 -> LT |
| 247 | `187.52.45.183` | trojan | PL | ip-literal | 否 | mmdb 命中 187.52.45.183 -> PL |
| 248 | `flawers.shop` | trojan | PL | domain-resolved | 否 | 解析到 187.52.45.183 -> PL |
| 249 | `130.78.30.147` | vless | NL | ip-literal | 否 | mmdb 命中 130.78.30.147 -> NL |
| 250 | `66.163.118.113` | vless | ES | ip-literal | 否 | mmdb 命中 66.163.118.113 -> ES |
| 251 | `206.189.229.48` | hysteria2 | US | ip-literal | 是 | mmdb 命中 206.189.229.48 -> US |
| 252 | `152.67.115.203` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 152.67.115.203 -> AU |
| 253 | `193.108.119.29` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.29 -> DE |
| 254 | `87.199.205.28` | vless | NL | ip-literal | 否 | mmdb 命中 87.199.205.28 -> NL |
| 255 | `46.29.255.123` | vless | SC | ip-literal | 否 | mmdb 命中 46.29.255.123 -> SC |
| 256 | `188.225.57.185` | vless | RU | ip-literal | 否 | mmdb 命中 188.225.57.185 -> RU |
| 257 | `195.206.235.121` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.121 -> NL |
| 258 | `195.206.235.44` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.44 -> NL |
| 259 | `62.210.7.139` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.7.139 -> FR |
| 260 | `62.210.147.2` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.147.2 -> FR |
| 261 | `62.210.124.146` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.124.146 -> FR |
| 262 | `138.3.208.26` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 138.3.208.26 -> JP |
| 263 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 264 | `82.152.161.146` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 82.152.161.146 -> HK |
| 265 | `152.67.200.82` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.67.200.82 -> KR |
| 266 | `13.55.52.44` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 13.55.52.44 -> AU |
| 267 | `outh.yandex-cloud.org` | hysteria2 | RU | domain-resolved | 否 | 解析到 189.74.106.171 -> RU |
| 268 | `138.2.73.238` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.73.238 -> SG |
| 269 | `132.226.226.189` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 132.226.226.189 -> KR |
| 270 | `48.102.214.171` | hysteria2 | US | ip-literal | 是 | mmdb 命中 48.102.214.171 -> US |
| 271 | `31.57.248.176` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 31.57.248.176 -> HK |
| 272 | `189.30.65.203` | vless | AE | ip-literal | 否 | mmdb 命中 189.30.65.203 -> AE |
| 273 | `201.51.12.98` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.12.98 -> RU |
| 274 | `152.69.231.175` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.69.231.175 -> KR |
| 275 | `srv-17e124.21freedom.net` | hysteria2 | RU | domain-resolved | 否 | 解析到 103.88.243.142 -> RU |
| 276 | `82.118.16.187` | vless | IT | ip-literal | 否 | mmdb 命中 82.118.16.187 -> IT |
| 277 | `143.246.41.214` | vless | EE | ip-literal | 否 | mmdb 命中 143.246.41.214 -> EE |
| 278 | `195.123.245.241` | vless | CZ | ip-literal | 否 | mmdb 命中 195.123.245.241 -> CZ |
| 279 | `o685y.save-node.com` | vless | DE | domain-resolved | 否 | 解析到 88.216.70.125 -> DE |
| 280 | `104.16.111.195` | vless | US | ip-literal | 是 | mmdb 命中 104.16.111.195 -> US |
| 281 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 282 | `104.24.0.1` | vless | US | ip-literal | 是 | mmdb 命中 104.24.0.1 -> US |
| 283 | `104.21.34.106` | vless | US | ip-literal | 是 | mmdb 命中 104.21.34.106 -> US |
| 284 | `104.18.42.98` | vless | US | ip-literal | 是 | mmdb 命中 104.18.42.98 -> US |
| 285 | `104.16.10.9` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.9 -> US |
| 286 | `104.16.10.234` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.234 -> US |
| 287 | `104.24.31.89` | vless | US | ip-literal | 是 | mmdb 命中 104.24.31.89 -> US |
| 288 | `104.16.10.22` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.22 -> US |
| 289 | `104.19.33.237` | vless | US | ip-literal | 是 | mmdb 命中 104.19.33.237 -> US |
| 290 | `152.228.139.33` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.139.33 -> FR |
| 291 | `147.45.175.81` | vless | RU | ip-literal | 否 | mmdb 命中 147.45.175.81 -> RU |
| 292 | `48.103.133.47` | vless | RU | ip-literal | 否 | mmdb 命中 48.103.133.47 -> RU |
| 293 | `66.163.118.62` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.62 -> ES |
| 294 | `www.zoom.us` | vless | US | domain-resolved | 是 | 解析到 170.114.52.2 -> US |
| 295 | `177.202.78.111` | vless | NL | ip-literal | 否 | mmdb 命中 177.202.78.111 -> NL |
| 296 | `213.176.92.168` | vless | HK | ip-literal | 否 | mmdb 命中 213.176.92.168 -> HK |
| 297 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 298 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 299 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 300 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 301 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 302 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 303 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 304 | `94.183.195.176` | vless | AE | ip-literal | 否 | mmdb 命中 94.183.195.176 -> AE |
| 305 | `217.60.94.115` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.94.115 -> DE |
| 306 | `almanac.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 201.24.49.215 -> RU |
| 307 | `bl1.nexfile.net` | vless | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 308 | `leviko-pl7089.shopingggg.ir` | vless | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 309 | `179.254.191.251` | vless | US | ip-literal | 是 | mmdb 命中 179.254.191.251 -> US |
| 310 | `swo2.nexfile.net` | vless | US | domain-resolved | 是 | 解析到 179.253.80.175 -> US |
| 311 | `179.253.80.175` | vless | US | ip-literal | 是 | mmdb 命中 179.253.80.175 -> US |
| 312 | `8.217.1.203` | vless | HK | ip-literal | 否 | mmdb 命中 8.217.1.203 -> HK |
| 313 | `ip.sb` | vless | US | domain-resolved | 是 | 解析到 172.67.75.172 -> US |
| 314 | `skk.moe` | vless | US | domain-resolved | 是 | 解析到 172.67.174.37 -> US |
| 315 | `time.is` | vless | US | domain-resolved | 是 | 解析到 172.67.68.157 -> US |
| 316 | `84.32.108.7` | vless | NL | ip-literal | 否 | mmdb 命中 84.32.108.7 -> NL |
| 317 | `45.88.176.223` | vless | CY | ip-literal | 否 | mmdb 命中 45.88.176.223 -> CY |
| 318 | `185.86.145.173` | vless | RU | ip-literal | 否 | mmdb 命中 185.86.145.173 -> RU |
| 319 | `nursery.elvano.website` | vless | RU | domain-resolved | 否 | 解析到 5.42.96.196 -> RU |
| 320 | `31.76.32.122` | vless | US | ip-literal | 是 | mmdb 命中 31.76.32.122 -> US |
| 321 | `169.197.140.224` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.224 -> US |
| 322 | `47.253.226.114` | vless | US | ip-literal | 是 | mmdb 命中 47.253.226.114 -> US |
| 323 | `201.24.116.192` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.116.192 -> RU |
| 324 | `bl1.nexfile.net` | hysteria2 | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 325 | `tun2.minoosell.ir` | vless | PL | domain-resolved | 否 | 解析到 45.144.49.138 -> PL |
| 326 | `45.144.49.138` | vless | PL | ip-literal | 否 | mmdb 命中 45.144.49.138 -> PL |
| 327 | `178.17.53.154` | vless | FI | ip-literal | 否 | mmdb 命中 178.17.53.154 -> FI |
| 328 | `free.fugui.lol` | vless | TW | domain-resolved | 否 | 解析到 1.160.12.70 -> TW |
| 329 | `91.107.191.188` | vless | DE | ip-literal | 否 | mmdb 命中 91.107.191.188 -> DE |
| 330 | `kala.bestsellers1.site` | vless | DE | domain-resolved | 否 | 解析到 91.107.191.188 -> DE |
| 331 | `94.241.172.107` | vless | GR | ip-literal | 否 | mmdb 命中 94.241.172.107 -> GR |
| 332 | `api.ferrin.uk` | vless | NL | domain-resolved | 否 | 解析到 50.7.123.174 -> NL |
| 333 | `germanyhetz.onlineblog.ir` | vless | DE | domain-resolved | 否 | 解析到 49.12.36.119 -> DE |
| 334 | `eecdn.fius.dev` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 335 | `chcdn.fius.dev` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 336 | `185.210.155.38` | vless | ES | ip-literal | 否 | mmdb 命中 185.210.155.38 -> ES |
| 337 | `de.gvtop.net` | vless | DE | domain-resolved | 否 | 解析到 31.76.101.136 -> DE |
| 338 | `196.199.122.2` | vless | SC | ip-literal | 否 | mmdb 命中 196.199.122.2 -> SC |
| 339 | `196.196.149.80` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.149.80 -> SC |
| 340 | `83.141.95.147` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.95.147 -> IE |
| 341 | `food.ebaniyautist.com` | vless | RU | domain-resolved | 否 | 解析到 194.55.239.10 -> RU |
| 342 | `hazel.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 343 | `rowan.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 344 | `gain.novacelestia.live` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 345 | `poplar.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 346 | `monte.quantumveritas.monster` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 347 | `231ccd11c72e7354.topology.gslb.yccdn.ru` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 348 | `owl.zentaris.website` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 349 | `birch.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 350 | `juniper.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 351 | `188.72.112.1` | vless | RU | ip-literal | 否 | mmdb 命中 188.72.112.1 -> RU |
| 352 | `elm.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 353 | `cedar.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 354 | `linden.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 355 | `alder.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 356 | `maple.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 357 | `488e167c4c27.vps.myjino.ru` | vless | RU | domain-resolved | 否 | 解析到 195.161.55.25 -> RU |
| 358 | `nep.cryptoventura.online` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 359 | `tenet.ultraveltrion.cyou` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 360 | `willow.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 361 | `marsh.moltex.click` | vless | RU | domain-resolved | 否 | 解析到 201.24.49.215 -> RU |
| 362 | `31.6.1.115` | vless | RO | ip-literal | 否 | mmdb 命中 31.6.1.115 -> RO |
| 363 | `willowbank.moltex.click` | vless | RU | domain-resolved | 否 | 解析到 201.24.49.215 -> RU |
| 364 | `193.122.106.29` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 193.122.106.29 -> KR |
| 365 | `vpnjey` | hysteria2 | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 366 | `5.178.109.174` | vless | SE | ip-literal | 否 | mmdb 命中 5.178.109.174 -> SE |
| 367 | `178.94.25.73` | vless | SG | ip-literal | 否 | mmdb 命中 178.94.25.73 -> SG |
| 368 | `62.210.24.143` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.24.143 -> FR |
| 369 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 370 | `85.208.69.43` | vless | CH | ip-literal | 否 | mmdb 命中 85.208.69.43 -> CH |
| 371 | `217.60.27.93` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.93 -> DE |
| 372 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 373 | `31.77.144.255` | vless | SE | ip-literal | 否 | mmdb 命中 31.77.144.255 -> SE |
| 374 | `62.210.70.194` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.70.194 -> FR |
| 375 | `se2.h1cloud.net` | vless | PL | domain-resolved | 否 | 解析到 201.58.139.254 -> PL |
| 376 | `38.180.206.44` | vless | KZ | ip-literal | 否 | mmdb 命中 38.180.206.44 -> KZ |
| 377 | `ch5.h1cloud.net` | vless | NL | domain-resolved | 否 | 解析到 13.141.51.227 -> NL |
| 378 | `94.26.35.241` | vless | CH | ip-literal | 否 | mmdb 命中 94.26.35.241 -> CH |
| 379 | `83.141.92.82` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.92.82 -> IE |
| 380 | `201.10.91.216` | vless | PL | ip-literal | 否 | mmdb 命中 201.10.91.216 -> PL |
| 381 | `83.141.79.238` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.79.238 -> IE |
| 382 | `87.120.92.186` | vless | BG | ip-literal | 否 | mmdb 命中 87.120.92.186 -> BG |
| 383 | `48.103.231.2` | vless | DE | ip-literal | 否 | mmdb 命中 48.103.231.2 -> DE |
| 384 | `193.160.208.240` | vless | RU | ip-literal | 否 | mmdb 命中 193.160.208.240 -> RU |
| 385 | `slot3.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.253.106 -> DE |
| 386 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 387 | `95.163.153.141` | vless | AT | ip-literal | 否 | mmdb 命中 95.163.153.141 -> AT |
| 388 | `178.17.52.31` | vless | IQ | ip-literal | 否 | mmdb 命中 178.17.52.31 -> IQ |
| 389 | `136.148.83.132` | vless | RU | ip-literal | 否 | mmdb 命中 136.148.83.132 -> RU |
| 390 | `95.85.232.83` | vless | CZ | ip-literal | 否 | mmdb 命中 95.85.232.83 -> CZ |
| 391 | `trips.blog-forme.ru` | vless | CZ | domain-resolved | 否 | 解析到 95.85.232.83 -> CZ |
| 392 | `95.85.231.3` | vless | CZ | ip-literal | 否 | mmdb 命中 95.85.231.3 -> CZ |
| 393 | `guide.blog-forme.ru` | vless | CZ | domain-resolved | 否 | 解析到 95.85.231.3 -> CZ |
| 394 | `leviko-nl2559.shopingggg.ir` | vless | NL | domain-resolved | 否 | 解析到 146.19.254.171 -> NL |
| 395 | `9.247.54.228` | vless | NL | ip-literal | 否 | mmdb 命中 9.247.54.228 -> NL |
| 396 | `185.14.29.29` | vless | NL | ip-literal | 否 | mmdb 命中 185.14.29.29 -> NL |
| 397 | `152.228.162.19` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.162.19 -> FR |
| 398 | `62.106.75.37` | vless | JP | ip-literal | 否 | mmdb 命中 62.106.75.37 -> JP |
| 399 | `94.183.164.119` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 400 | `217.60.27.93` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.93 -> DE |
| 401 | `94.183.164.96` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.96 -> NL |
| 402 | `185.248.141.233` | vless | DE | ip-literal | 否 | mmdb 命中 185.248.141.233 -> DE |
| 403 | `195.206.235.110` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.110 -> NL |
| 404 | `79.182.70.81` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.81 -> NL |
| 405 | `132.243.67.228` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.67.228 -> EE |
| 406 | `143.246.211.240` | vless | FR | ip-literal | 否 | mmdb 命中 143.246.211.240 -> FR |
| 407 | `194.60.228.97` | vless | IR | ip-literal | 否 | mmdb 命中 194.60.228.97 -> IR |
| 408 | `leviko-ir8553.shopingggg.ir` | vless | IR | domain-resolved | 否 | 解析到 194.60.228.97 -> IR |
| 409 | `138.124.180.137` | vless | LV | ip-literal | 否 | mmdb 命中 138.124.180.137 -> LV |
| 410 | `pl.galacticworld.online` | vless | US | domain-resolved | 是 | 解析到 150.241.87.52 -> US |
| 411 | `132.243.212.204` | vless | CY | ip-literal | 否 | mmdb 命中 132.243.212.204 -> CY |
| 412 | `NUFiLTER` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 413 | `ipfast.kingmna.com` | trojan | US | domain-resolved | 是 | 解析到 167.82.76.31 -> US |
| 414 | `.networld_vpn-&fp=chrome&security=reality&pbk=1y5h2FGWKXTJ9xLPCqPo6Mw7RxoZzh6fGkEQKNxpZ3s&sid=01` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 415 | `15.204.97.216` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.216 -> US |
| 416 | `s1.berluno.ir` | vless | DE | domain-resolved | 否 | 解析到 138.199.220.226 -> DE |
| 417 | `51.170.191.10` | vless | NL | ip-literal | 否 | mmdb 命中 51.170.191.10 -> NL |
| 418 | `162.252.199.207` | vless | US | ip-literal | 是 | mmdb 命中 162.252.199.207 -> US |
| 419 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 420 | `39.109.111.23` | vless | HK | ip-literal | 否 | mmdb 命中 39.109.111.23 -> HK |
| 421 | `185.122.167.103` | vless | GB | ip-literal | 否 | mmdb 命中 185.122.167.103 -> GB |
| 422 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 423 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 424 | `88.216.211.36` | vless | DE | ip-literal | 否 | mmdb 命中 88.216.211.36 -> DE |
| 425 | `87.248.149.50` | vless | IR | ip-literal | 否 | mmdb 命中 87.248.149.50 -> IR |
| 426 | `38.107.236.166` | vless | US | ip-literal | 是 | mmdb 命中 38.107.236.166 -> US |
| 427 | `15.204.97.198` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.198 -> US |
| 428 | `103.75.118.228` | vless | JP | ip-literal | 否 | mmdb 命中 103.75.118.228 -> JP |
| 429 | `43.255.157.53` | vless | US | ip-literal | 是 | mmdb 命中 43.255.157.53 -> US |
| 430 | `216.152.147.74` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.74 -> CA |
| 431 | `45.61.186.3` | vless | US | ip-literal | 是 | mmdb 命中 45.61.186.3 -> US |
| 432 | `179.254.92.134` | vless | US | ip-literal | 是 | mmdb 命中 179.254.92.134 -> US |
| 433 | `31.76.91.98` | vless | JP | ip-literal | 否 | mmdb 命中 31.76.91.98 -> JP |
| 434 | `185.112.59.157` | vless | NL | ip-literal | 否 | mmdb 命中 185.112.59.157 -> NL |
| 435 | `user.betust.net` | vless | US | domain-resolved | 是 | 解析到 50.7.169.243 -> US |
| 436 | `50.7.169.243` | vless | US | ip-literal | 是 | mmdb 命中 50.7.169.243 -> US |
| 437 | `152.53.236.182` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.236.182 -> DE |
| 438 | `leviko-us2057.shopingggg.ir` | vless | US | domain-resolved | 是 | 解析到 2.24.124.64 -> US |
| 439 | `195.123.245.241` | vless | CZ | ip-literal | 否 | mmdb 命中 195.123.245.241 -> CZ |
| 440 | `195.123.213.28` | vless | LV | ip-literal | 否 | mmdb 命中 195.123.213.28 -> LV |
| 441 | `2.26.251.236` | vless | DE | ip-literal | 否 | mmdb 命中 2.26.251.236 -> DE |
| 442 | `ru7e2bab87cc39.eu-cdn539.com` | vless | RU | domain-resolved | 否 | 解析到 129.101.98.60 -> RU |
| 443 | `193.163.203.170` | vless | LV | ip-literal | 否 | mmdb 命中 193.163.203.170 -> LV |
| 444 | `5.180.27.134` | vless | KZ | ip-literal | 否 | mmdb 命中 5.180.27.134 -> KZ |
| 445 | `129.101.98.60` | vless | RU | ip-literal | 否 | mmdb 命中 129.101.98.60 -> RU |
| 446 | `94.183.234.245` | vless | LV | ip-literal | 否 | mmdb 命中 94.183.234.245 -> LV |
| 447 | `83.217.201.82` | vless | RU | ip-literal | 否 | mmdb 命中 83.217.201.82 -> RU |
| 448 | `76574ct.nl8.h1clayd.click` | vless | SK | domain-resolved | 否 | 解析到 196.245.153.111 -> SK |
| 449 | `tgfree.rush-server.com` | vless | RU | domain-resolved | 否 | 解析到 104.171.133.209 -> RU |
| 450 | `leviko-nl0448.shopingggg.ir` | vless | GB | domain-resolved | 否 | 解析到 104.222.183.180 -> GB |
| 451 | `185.242.247.252` | vless | FI | ip-literal | 否 | mmdb 命中 185.242.247.252 -> FI |
| 452 | `195.123.226.21` | vless | BG | ip-literal | 否 | mmdb 命中 195.123.226.21 -> BG |
| 453 | `152.70.58.201` | vless | NL | ip-literal | 否 | mmdb 命中 152.70.58.201 -> NL |
| 454 | `161.97.66.16` | vless | FR | ip-literal | 否 | mmdb 命中 161.97.66.16 -> FR |
| 455 | `83.136.210.129` | vless | FR | ip-literal | 否 | mmdb 命中 83.136.210.129 -> FR |
| 456 | `13.143.187.220` | vless | US | ip-literal | 是 | mmdb 命中 13.143.187.220 -> US |
| 457 | `46.28.67.55` | vless | RO | ip-literal | 否 | mmdb 命中 46.28.67.55 -> RO |
| 458 | `150.40.126.187` | vless | RS | ip-literal | 否 | mmdb 命中 150.40.126.187 -> RS |
| 459 | `bh1.vpnjantit.com` | vless | BH | domain-resolved | 否 | 解析到 38.54.2.189 -> BH |
| 460 | `201.8.64.226` | vless | NL | ip-literal | 否 | mmdb 命中 201.8.64.226 -> NL |
| 461 | `82.118.16.189` | vless | IT | ip-literal | 否 | mmdb 命中 82.118.16.189 -> IT |
| 462 | `89.125.100.150` | vless | NL | ip-literal | 否 | mmdb 命中 89.125.100.150 -> NL |
| 463 | `79.182.70.192` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.192 -> NL |
| 464 | `153.52.85.198` | vless | DE | ip-literal | 否 | mmdb 命中 153.52.85.198 -> DE |
| 465 | `f0d7aft.nl13.h1clayd.click` | vless | PL | domain-resolved | 否 | 解析到 201.58.139.252 -> PL |
| 466 | `78.17.215.138` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.138 -> DE |
| 467 | `38.244.5.231` | vless | US | ip-literal | 是 | mmdb 命中 38.244.5.231 -> US |
| 468 | `38.244.5.231` | vless | US | ip-literal | 是 | mmdb 命中 38.244.5.231 -> US |
| 469 | `47.251.108.158` | vless | US | ip-literal | 是 | mmdb 命中 47.251.108.158 -> US |
| 470 | `31.76.91.248` | vless | JP | ip-literal | 否 | mmdb 命中 31.76.91.248 -> JP |
| 471 | `138.124.251.98` | vless | FR | ip-literal | 否 | mmdb 命中 138.124.251.98 -> FR |
| 472 | `138.124.80.29` | vless | CH | ip-literal | 否 | mmdb 命中 138.124.80.29 -> CH |
| 473 | `67.159.52.81` | vless | SG | ip-literal | 否 | mmdb 命中 67.159.52.81 -> SG |
| 474 | `152.53.239.182` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.239.182 -> DE |
| 475 | `jdwacdi.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.236.182 -> DE |
| 476 | `2.24.124.64` | vless | US | ip-literal | 是 | mmdb 命中 2.24.124.64 -> US |
| 477 | `nl-06.neverspy.tech` | vless | NL | domain-resolved | 否 | 解析到 185.112.59.157 -> NL |
| 478 | `193.233.198.117` | vless | DE | ip-literal | 否 | mmdb 命中 193.233.198.117 -> DE |
| 479 | `jdwadgw.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.239.182 -> DE |
| 480 | `152.53.127.214` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.127.214 -> DE |
| 481 | `de-03.neverspy.tech` | vless | DE | domain-resolved | 否 | 解析到 193.233.198.117 -> DE |
| 482 | `51.161.204.242` | vless | AU | ip-literal | 否 | mmdb 命中 51.161.204.242 -> AU |
| 483 | `5.34.177.164` | vless | SG | ip-literal | 否 | mmdb 命中 5.34.177.164 -> SG |
| 484 | `188.166.182.158` | vless | SG | ip-literal | 否 | mmdb 命中 188.166.182.158 -> SG |
| 485 | `86.107.179.250` | vless | RO | ip-literal | 否 | mmdb 命中 86.107.179.250 -> RO |
| 486 | `86.54.28.75` | vless | NL | ip-literal | 否 | mmdb 命中 86.54.28.75 -> NL |
| 487 | `187.55.172.33` | vless | US | ip-literal | 是 | mmdb 命中 187.55.172.33 -> US |
| 488 | `104.171.133.209` | vless | RU | ip-literal | 否 | mmdb 命中 104.171.133.209 -> RU |
| 489 | `netx.smrtai.top` | vless | UA | domain-resolved | 否 | 解析到 31.222.235.81 -> UA |
| 490 | `201.58.134.155` | vless | DE | ip-literal | 否 | mmdb 命中 201.58.134.155 -> DE |
| 491 | `177.1.193.28` | vless | PL | ip-literal | 否 | mmdb 命中 177.1.193.28 -> PL |
| 492 | `148.113.5.22` | vless | IN | ip-literal | 否 | mmdb 命中 148.113.5.22 -> IN |
| 493 | `109.71.245.99` | vless | RU | ip-literal | 否 | mmdb 命中 109.71.245.99 -> RU |
| 494 | `201.58.155.64` | vless | US | ip-literal | 是 | mmdb 命中 201.58.155.64 -> US |
| 495 | `201.58.155.53` | vless | US | ip-literal | 是 | mmdb 命中 201.58.155.53 -> US |
| 496 | `147.45.60.136` | vless | US | ip-literal | 是 | mmdb 命中 147.45.60.136 -> US |
| 497 | `89.169.2.136` | vless | RU | ip-literal | 否 | mmdb 命中 89.169.2.136 -> RU |
| 498 | `195.206.235.119` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.119 -> NL |
| 499 | `lists.soloramtin.cyou` | vless | US | domain-resolved | 是 | 解析到 50.117.15.225 -> US |
| 500 | `31.59.148.132` | vless | NL | ip-literal | 否 | mmdb 命中 31.59.148.132 -> NL |
| 501 | `48.102.172.114` | vless | SE | ip-literal | 否 | mmdb 命中 48.102.172.114 -> SE |
| 502 | `195.206.235.34` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.34 -> NL |
| 503 | `150.251.141.246` | vless | NL | ip-literal | 否 | mmdb 命中 150.251.141.246 -> NL |
| 504 | `195.206.235.215` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.215 -> NL |
| 505 | `music.3apes.online` | vless | DE | domain-resolved | 否 | 解析到 217.60.27.153 -> DE |
| 506 | `13.141.51.2` | vless | NL | ip-literal | 否 | mmdb 命中 13.141.51.2 -> NL |
| 507 | `179.253.85.127` | vless | US | ip-literal | 是 | mmdb 命中 179.253.85.127 -> US |
| 508 | `222.167.245.16` | vless | PL | ip-literal | 否 | mmdb 命中 222.167.245.16 -> PL |
| 509 | `85.237.207.221` | vless | TW | ip-literal | 否 | mmdb 命中 85.237.207.221 -> TW |
| 510 | `66.163.114.114` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.114 -> US |
| 511 | `201.24.121.243` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.121.243 -> RU |
| 512 | `144.31.28.228` | vless | US | ip-literal | 是 | mmdb 命中 144.31.28.228 -> US |
| 513 | `95.143.196.97` | trojan | SE | ip-literal | 否 | mmdb 命中 95.143.196.97 -> SE |
| 514 | `217.60.27.153` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.153 -> DE |
| 515 | `200.169.179.233` | vless | RU | ip-literal | 否 | mmdb 命中 200.169.179.233 -> RU |
| 516 | `3h-unitedstates1.09vpn.com` | vless | US | domain-resolved | 是 | 解析到 38.107.232.36 -> US |
| 517 | `150.241.87.52` | vless | US | ip-literal | 是 | mmdb 命中 150.241.87.52 -> US |
| 518 | `95.174.68.188` | vless | AE | ip-literal | 否 | mmdb 命中 95.174.68.188 -> AE |
| 519 | `fuji.etherhub.cc` | vless | JP | domain-resolved | 否 | 解析到 31.76.91.98 -> JP |
| 520 | `158.101.151.157` | vless | JP | ip-literal | 否 | mmdb 命中 158.101.151.157 -> JP |
| 521 | `138.124.245.102` | vless | NL | ip-literal | 否 | mmdb 命中 138.124.245.102 -> NL |
| 522 | `152.53.236.22` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.236.22 -> DE |
| 523 | `jdwabxe.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.236.22 -> DE |
| 524 | `jdvymxi.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.127.214 -> DE |
| 525 | `209.200.246.148` | vless | CA | ip-literal | 否 | mmdb 命中 209.200.246.148 -> CA |
| 526 | `188.225.25.35` | vless | RU | ip-literal | 否 | mmdb 命中 188.225.25.35 -> RU |
| 527 | `188.225.82.6` | vless | RU | ip-literal | 否 | mmdb 命中 188.225.82.6 -> RU |
| 528 | `195.63.128.21` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 529 | `152.69.226.63` | vless | KR | ip-literal | 否 | mmdb 命中 152.69.226.63 -> KR |
| 530 | `50.117.15.225` | vless | US | ip-literal | 是 | mmdb 命中 50.117.15.225 -> US |
| 531 | `ov-france1.09vpn.com` | vless | FR | domain-resolved | 否 | 解析到 152.228.162.19 -> FR |
| 532 | `62.144.51.70` | vless | DE | ip-literal | 否 | mmdb 命中 62.144.51.70 -> DE |
| 533 | `150.241.92.9` | vless | NL | ip-literal | 否 | mmdb 命中 150.241.92.9 -> NL |
| 534 | `66.163.118.166` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.166 -> ES |
| 535 | `157.245.129.175` | vless | US | ip-literal | 是 | mmdb 命中 157.245.129.175 -> US |
| 536 | `13.219.53.87` | vless | US | ip-literal | 是 | mmdb 命中 13.219.53.87 -> US |
| 537 | `143.244.159.16` | vless | US | ip-literal | 是 | mmdb 命中 143.244.159.16 -> US |
| 538 | `157.230.87.125` | vless | US | ip-literal | 是 | mmdb 命中 157.230.87.125 -> US |
| 539 | `178.128.145.101` | vless | US | ip-literal | 是 | mmdb 命中 178.128.145.101 -> US |
| 540 | `67.205.135.247` | vless | US | ip-literal | 是 | mmdb 命中 67.205.135.247 -> US |
| 541 | `104.248.62.43` | vless | US | ip-literal | 是 | mmdb 命中 104.248.62.43 -> US |
| 542 | `137.184.153.238` | vless | US | ip-literal | 是 | mmdb 命中 137.184.153.238 -> US |
| 543 | `178.62.55.220` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.55.220 -> GB |
| 544 | `178.62.123.138` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.123.138 -> GB |
| 545 | `157.245.41.8` | vless | GB | ip-literal | 否 | mmdb 命中 157.245.41.8 -> GB |
| 546 | `139.59.186.194` | vless | GB | ip-literal | 否 | mmdb 命中 139.59.186.194 -> GB |
| 547 | `178.62.10.95` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.10.95 -> GB |
| 548 | `161.35.37.106` | vless | GB | ip-literal | 否 | mmdb 命中 161.35.37.106 -> GB |
| 549 | `167.172.55.211` | vless | GB | ip-literal | 否 | mmdb 命中 167.172.55.211 -> GB |
| 550 | `134.209.24.190` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.24.190 -> GB |
| 551 | `178.62.83.89` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.83.89 -> GB |
| 552 | `46.101.84.198` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.84.198 -> GB |
| 553 | `165.22.126.209` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.126.209 -> GB |
| 554 | `18.175.151.189` | vless | GB | ip-literal | 否 | mmdb 命中 18.175.151.189 -> GB |
| 555 | `209.97.178.40` | vless | GB | ip-literal | 否 | mmdb 命中 209.97.178.40 -> GB |
| 556 | `46.101.5.211` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.5.211 -> GB |
| 557 | `178.62.83.160` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.83.160 -> GB |
| 558 | `178.62.84.226` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.84.226 -> GB |
| 559 | `139.59.166.177` | vless | GB | ip-literal | 否 | mmdb 命中 139.59.166.177 -> GB |
| 560 | `178.62.102.130` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.102.130 -> GB |
| 561 | `178.62.37.247` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.37.247 -> GB |
| 562 | `46.101.32.24` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.32.24 -> GB |
| 563 | `46.101.38.178` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.38.178 -> GB |
| 564 | `165.232.40.73` | vless | GB | ip-literal | 否 | mmdb 命中 165.232.40.73 -> GB |
| 565 | `178.62.13.251` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.13.251 -> GB |
| 566 | `206.189.7.180` | vless | NL | ip-literal | 否 | mmdb 命中 206.189.7.180 -> NL |
| 567 | `46.101.48.109` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.48.109 -> GB |
| 568 | `165.232.35.216` | vless | GB | ip-literal | 否 | mmdb 命中 165.232.35.216 -> GB |
| 569 | `46.101.56.189` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.56.189 -> GB |
| 570 | `46.101.62.114` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.62.114 -> GB |
| 571 | `46.101.90.178` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.90.178 -> GB |
| 572 | `209.97.139.63` | vless | GB | ip-literal | 否 | mmdb 命中 209.97.139.63 -> GB |
| 573 | `159.65.48.135` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.48.135 -> GB |
| 574 | `178.62.17.195` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.17.195 -> GB |
| 575 | `178.62.62.63` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.62.63 -> GB |
| 576 | `46.101.44.79` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.44.79 -> GB |
| 577 | `159.65.94.43` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.94.43 -> GB |
| 578 | `16.61.186.153` | vless | GB | ip-literal | 否 | mmdb 命中 16.61.186.153 -> GB |
| 579 | `142.93.38.165` | vless | GB | ip-literal | 否 | mmdb 命中 142.93.38.165 -> GB |
| 580 | `138.68.132.7` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.132.7 -> GB |
| 581 | `142.93.238.232` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.238.232 -> NL |
| 582 | `164.92.150.238` | vless | NL | ip-literal | 否 | mmdb 命中 164.92.150.238 -> NL |
| 583 | `165.22.122.173` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.122.173 -> GB |
| 584 | `46.101.39.169` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.39.169 -> GB |
| 585 | `46.101.61.61` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.61.61 -> GB |
| 586 | `138.68.155.168` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.155.168 -> GB |
| 587 | `146.190.21.145` | vless | NL | ip-literal | 否 | mmdb 命中 146.190.21.145 -> NL |
| 588 | `164.90.229.165` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.229.165 -> DE |
| 589 | `144.126.226.214` | vless | GB | ip-literal | 否 | mmdb 命中 144.126.226.214 -> GB |
| 590 | `178.62.53.190` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.53.190 -> GB |
| 591 | `46.101.24.252` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.24.252 -> GB |
| 592 | `178.62.119.162` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.119.162 -> GB |
| 593 | `178.62.22.50` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.22.50 -> GB |
| 594 | `178.128.249.168` | vless | NL | ip-literal | 否 | mmdb 命中 178.128.249.168 -> NL |
| 595 | `164.92.208.207` | vless | NL | ip-literal | 否 | mmdb 命中 164.92.208.207 -> NL |
| 596 | `188.166.25.185` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.25.185 -> NL |
| 597 | `165.22.192.182` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.192.182 -> NL |
| 598 | `104.248.17.166` | vless | DE | ip-literal | 否 | mmdb 命中 104.248.17.166 -> DE |
| 599 | `138.68.161.73` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.161.73 -> GB |
| 600 | `68.183.15.210` | vless | NL | ip-literal | 否 | mmdb 命中 68.183.15.210 -> NL |
| 601 | `104.248.197.227` | vless | NL | ip-literal | 否 | mmdb 命中 104.248.197.227 -> NL |
| 602 | `167.99.92.118` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.92.118 -> GB |
| 603 | `178.62.212.162` | vless | NL | ip-literal | 否 | mmdb 命中 178.62.212.162 -> NL |
| 604 | `178.62.80.77` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.80.77 -> GB |
| 605 | `46.101.34.217` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.34.217 -> GB |
| 606 | `13.37.183.129` | vless | FR | ip-literal | 否 | mmdb 命中 13.37.183.129 -> FR |
| 607 | `178.62.95.43` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.95.43 -> GB |
| 608 | `64.225.107.97` | vless | DE | ip-literal | 否 | mmdb 命中 64.225.107.97 -> DE |
| 609 | `159.89.6.42` | vless | DE | ip-literal | 否 | mmdb 命中 159.89.6.42 -> DE |
| 610 | `178.62.115.140` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.115.140 -> GB |
| 611 | `52.50.131.53` | vless | IE | ip-literal | 否 | mmdb 命中 52.50.131.53 -> IE |
| 612 | `144.126.206.217` | vless | GB | ip-literal | 否 | mmdb 命中 144.126.206.217 -> GB |
| 613 | `46.101.114.149` | vless | DE | ip-literal | 否 | mmdb 命中 46.101.114.149 -> DE |
| 614 | `178.62.15.117` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.15.117 -> GB |
| 615 | `161.35.80.144` | vless | NL | ip-literal | 否 | mmdb 命中 161.35.80.144 -> NL |
| 616 | `161.35.198.36` | vless | DE | ip-literal | 否 | mmdb 命中 161.35.198.36 -> DE |
| 617 | `144.126.237.191` | vless | GB | ip-literal | 否 | mmdb 命中 144.126.237.191 -> GB |
| 618 | `201.79.92.222` | vless | DE | ip-literal | 否 | mmdb 命中 201.79.92.222 -> DE |
| 619 | `164.90.218.120` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.218.120 -> DE |
| 620 | `167.71.50.162` | vless | DE | ip-literal | 否 | mmdb 命中 167.71.50.162 -> DE |
| 621 | `206.189.101.147` | vless | NL | ip-literal | 否 | mmdb 命中 206.189.101.147 -> NL |
| 622 | `164.90.171.97` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.171.97 -> DE |
| 623 | `134.122.88.64` | vless | DE | ip-literal | 否 | mmdb 命中 134.122.88.64 -> DE |
| 624 | `164.90.187.70` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.187.70 -> DE |
| 625 | `134.209.29.237` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.29.237 -> GB |
| 626 | `139.59.152.166` | vless | DE | ip-literal | 否 | mmdb 命中 139.59.152.166 -> DE |
| 627 | `64.226.89.93` | vless | DE | ip-literal | 否 | mmdb 命中 64.226.89.93 -> DE |
| 628 | `134.122.87.3` | vless | DE | ip-literal | 否 | mmdb 命中 134.122.87.3 -> DE |
| 629 | `178.62.84.120` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.84.120 -> GB |
| 630 | `188.166.167.54` | vless | DE | ip-literal | 否 | mmdb 命中 188.166.167.54 -> DE |
| 631 | `64.226.126.84` | vless | DE | ip-literal | 否 | mmdb 命中 64.226.126.84 -> DE |
| 632 | `164.92.204.150` | vless | DE | ip-literal | 否 | mmdb 命中 164.92.204.150 -> DE |
| 633 | `161.35.79.143` | vless | DE | ip-literal | 否 | mmdb 命中 161.35.79.143 -> DE |
| 634 | `207.154.252.182` | vless | DE | ip-literal | 否 | mmdb 命中 207.154.252.182 -> DE |
| 635 | `64.226.90.73` | vless | DE | ip-literal | 否 | mmdb 命中 64.226.90.73 -> DE |
| 636 | `164.90.233.137` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.233.137 -> DE |
| 637 | `207.154.252.164` | vless | DE | ip-literal | 否 | mmdb 命中 207.154.252.164 -> DE |
| 638 | `164.90.166.34` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.166.34 -> DE |
| 639 | `139.59.135.128` | vless | DE | ip-literal | 否 | mmdb 命中 139.59.135.128 -> DE |
| 640 | `139.59.157.144` | vless | DE | ip-literal | 否 | mmdb 命中 139.59.157.144 -> DE |
| 641 | `178.62.89.144` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.89.144 -> GB |
| 642 | `206.189.7.6` | vless | NL | ip-literal | 否 | mmdb 命中 206.189.7.6 -> NL |
| 643 | `188.166.76.92` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.76.92 -> NL |
| 644 | `165.245.240.61` | vless | DE | ip-literal | 否 | mmdb 命中 165.245.240.61 -> DE |
| 645 | `104.248.204.45` | vless | NL | ip-literal | 否 | mmdb 命中 104.248.204.45 -> NL |
| 646 | `164.92.148.72` | vless | NL | ip-literal | 否 | mmdb 命中 164.92.148.72 -> NL |
| 647 | `159.223.209.68` | vless | NL | ip-literal | 否 | mmdb 命中 159.223.209.68 -> NL |
| 648 | `167.99.214.98` | vless | NL | ip-literal | 否 | mmdb 命中 167.99.214.98 -> NL |
| 649 | `188.166.92.133` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.92.133 -> NL |
| 650 | `165.232.85.242` | vless | NL | ip-literal | 否 | mmdb 命中 165.232.85.242 -> NL |
| 651 | `164.92.203.8` | vless | DE | ip-literal | 否 | mmdb 命中 164.92.203.8 -> DE |
| 652 | `178.62.111.227` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.111.227 -> GB |
| 653 | `46.101.192.61` | vless | DE | ip-literal | 否 | mmdb 命中 46.101.192.61 -> DE |
| 654 | `159.89.111.109` | vless | DE | ip-literal | 否 | mmdb 命中 159.89.111.109 -> DE |
| 655 | `138.197.187.76` | vless | DE | ip-literal | 否 | mmdb 命中 138.197.187.76 -> DE |
| 656 | `167.71.59.76` | vless | DE | ip-literal | 否 | mmdb 命中 167.71.59.76 -> DE |
| 657 | `207.154.200.25` | vless | DE | ip-literal | 否 | mmdb 命中 207.154.200.25 -> DE |
| 658 | `207.154.199.235` | vless | DE | ip-literal | 否 | mmdb 命中 207.154.199.235 -> DE |
| 659 | `108.131.111.181` | vless | IE | ip-literal | 否 | mmdb 命中 108.131.111.181 -> IE |
| 660 | `178.62.112.73` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.112.73 -> GB |
| 661 | `167.172.169.27` | vless | DE | ip-literal | 否 | mmdb 命中 167.172.169.27 -> DE |
| 662 | `64.227.67.30` | vless | NL | ip-literal | 否 | mmdb 命中 64.227.67.30 -> NL |
| 663 | `209.38.22.140` | vless | AU | ip-literal | 否 | mmdb 命中 209.38.22.140 -> AU |
| 664 | `34.244.156.228` | vless | IE | ip-literal | 否 | mmdb 命中 34.244.156.228 -> IE |
| 665 | `161.35.213.134` | vless | DE | ip-literal | 否 | mmdb 命中 161.35.213.134 -> DE |
| 666 | `168.144.175.179` | vless | AU | ip-literal | 否 | mmdb 命中 168.144.175.179 -> AU |
| 667 | `35.176.64.96` | vless | GB | ip-literal | 否 | mmdb 命中 35.176.64.96 -> GB |
| 668 | `165.22.201.231` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.201.231 -> NL |
| 669 | `3.8.106.252` | vless | GB | ip-literal | 否 | mmdb 命中 3.8.106.252 -> GB |
| 670 | `159.89.3.39` | vless | DE | ip-literal | 否 | mmdb 命中 159.89.3.39 -> DE |
| 671 | `108.129.55.148` | vless | IE | ip-literal | 否 | mmdb 命中 108.129.55.148 -> IE |
| 672 | `164.90.170.50` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.170.50 -> DE |
| 673 | `164.92.204.250` | vless | DE | ip-literal | 否 | mmdb 命中 164.92.204.250 -> DE |
| 674 | `15.237.187.151` | vless | FR | ip-literal | 否 | mmdb 命中 15.237.187.151 -> FR |
| 675 | `165.227.154.16` | vless | DE | ip-literal | 否 | mmdb 命中 165.227.154.16 -> DE |
| 676 | `56.228.138.205` | vless | SE | ip-literal | 否 | mmdb 命中 56.228.138.205 -> SE |
| 677 | `51.24.193.242` | vless | GB | ip-literal | 否 | mmdb 命中 51.24.193.242 -> GB |
| 678 | `165.22.93.196` | vless | DE | ip-literal | 否 | mmdb 命中 165.22.93.196 -> DE |
| 679 | `51.21.14.210` | vless | SE | ip-literal | 否 | mmdb 命中 51.21.14.210 -> SE |
| 680 | `159.89.98.53` | vless | DE | ip-literal | 否 | mmdb 命中 159.89.98.53 -> DE |
| 681 | `138.197.190.212` | vless | DE | ip-literal | 否 | mmdb 命中 138.197.190.212 -> DE |
| 682 | `164.90.160.198` | vless | DE | ip-literal | 否 | mmdb 命中 164.90.160.198 -> DE |
| 683 | `178.62.47.132` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.47.132 -> GB |
| 684 | `63.185.91.151` | vless | DE | ip-literal | 否 | mmdb 命中 63.185.91.151 -> DE |
| 685 | `3.123.25.103` | vless | DE | ip-literal | 否 | mmdb 命中 3.123.25.103 -> DE |
| 686 | `178.128.195.57` | vless | DE | ip-literal | 否 | mmdb 命中 178.128.195.57 -> DE |
| 687 | `165.232.71.243` | vless | DE | ip-literal | 否 | mmdb 命中 165.232.71.243 -> DE |
| 688 | `138.68.77.218` | vless | DE | ip-literal | 否 | mmdb 命中 138.68.77.218 -> DE |
| 689 | `178.62.5.37` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.5.37 -> GB |
| 690 | `164.92.129.129` | vless | DE | ip-literal | 否 | mmdb 命中 164.92.129.129 -> DE |
| 691 | `13.37.98.224` | vless | FR | ip-literal | 否 | mmdb 命中 13.37.98.224 -> FR |
| 692 | `164.92.142.230` | vless | DE | ip-literal | 否 | mmdb 命中 164.92.142.230 -> DE |
| 693 | `15.224.221.83` | vless | FR | ip-literal | 否 | mmdb 命中 15.224.221.83 -> FR |
| 694 | `184.107.179.150` | vless | CA | ip-literal | 否 | mmdb 命中 184.107.179.150 -> CA |
| 695 | `188.166.182.158` | vless | SG | ip-literal | 否 | mmdb 命中 188.166.182.158 -> SG |
| 696 | `48.102.170.205` | vless | NL | ip-literal | 否 | mmdb 命中 48.102.170.205 -> NL |
| 697 | `164.37.110.126` | vless | GB | ip-literal | 否 | mmdb 命中 164.37.110.126 -> GB |
| 698 | `150.241.92.15` | vless | NL | ip-literal | 否 | mmdb 命中 150.241.92.15 -> NL |
| 699 | `216.227.161.95` | vless | US | ip-literal | 是 | mmdb 命中 216.227.161.95 -> US |
| 700 | `37.18.14.246` | vless | RU | ip-literal | 否 | mmdb 命中 37.18.14.246 -> RU |
| 701 | `ch.outforyou.ir` | vless | CH | domain-resolved | 否 | 解析到 143.246.202.91 -> CH |
| 702 | `2.27.174.132` | vless | TW | ip-literal | 否 | mmdb 命中 2.27.174.132 -> TW |
| 703 | `77.83.245.79` | vless | TR | ip-literal | 否 | mmdb 命中 77.83.245.79 -> TR |
| 704 | `216.152.147.89` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.89 -> CA |
| 705 | `196.196.148.63` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.148.63 -> SC |
| 706 | `196.196.148.90` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.148.90 -> SC |
| 707 | `132.243.163.253` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.253 -> GB |
| 708 | `162.35.101.177` | vless | US | ip-literal | 是 | mmdb 命中 162.35.101.177 -> US |
| 709 | `67.220.73.204` | vless | US | ip-literal | 是 | mmdb 命中 67.220.73.204 -> US |
| 710 | `156.229.167.109` | vless | US | ip-literal | 是 | mmdb 命中 156.229.167.109 -> US |
| 711 | `104.16.183.101` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.183.101 -> US |
| 712 | `104.16.80.73` | vless | US | ip-literal | 是 | mmdb 命中 104.16.80.73 -> US |
| 713 | `104.17.104.23` | vless | US | ip-literal | 是 | mmdb 命中 104.17.104.23 -> US |
| 714 | `104.17.72.206` | vless | US | ip-literal | 是 | mmdb 命中 104.17.72.206 -> US |
| 715 | `104.18.152.208` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.208 -> US |
| 716 | `v2ray_phoenix` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 717 | `configprxy` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 718 | `159.246.55.251` | vless | US | ip-literal | 是 | mmdb 命中 159.246.55.251 -> US |
| 719 | `162.159.12.212` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.12.212 -> US |
| 720 | `ai_duet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 721 | `KAFING_2` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 722 | `Tarkshodeh` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 723 | `v2ray313` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 724 | `chillguy_vpn` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 725 | `104.16.10.100` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.100 -> US |
| 726 | `104.16.10.104` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.104 -> US |
| 727 | `104.16.10.121` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.121 -> US |
| 728 | `Shh_Proxy-New⁷` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 729 | `Shh_Proxy-New⁸` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 730 | `104.16.107.139` | vless | US | ip-literal | 是 | mmdb 命中 104.16.107.139 -> US |
| 731 | `pPal03🙃Join🙃` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 732 | `104.16.144.131` | vless | US | ip-literal | 是 | mmdb 命中 104.16.144.131 -> US |
| 733 | `104.16.150.108` | vless | US | ip-literal | 是 | mmdb 命中 104.16.150.108 -> US |
| 734 | `Azarakhsh_Proxy+🩷` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 735 | `104.16.171.121` | vless | US | ip-literal | 是 | mmdb 命中 104.16.171.121 -> US |
| 736 | `104.16.172.173` | vless | US | ip-literal | 是 | mmdb 命中 104.16.172.173 -> US |
| 737 | `104.16.174.117` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.117 -> US |
| 738 | `104.16.174.12` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.12 -> US |
| 739 | `104.16.174.124` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.124 -> US |
| 740 | `104.16.174.143` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.143 -> US |
| 741 | `104.16.174.148` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.148 -> US |
| 742 | `104.16.174.185` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.185 -> US |
| 743 | `104.16.174.22` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.22 -> US |
| 744 | `104.16.174.34` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.34 -> US |
| 745 | `104.16.174.37` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.37 -> US |
| 746 | `104.16.174.44` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.44 -> US |
| 747 | `104.16.174.46` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.46 -> US |
| 748 | `104.16.174.6` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.6 -> US |
| 749 | `104.16.174.81` | vless | US | ip-literal | 是 | mmdb 命中 104.16.174.81 -> US |
| 750 | `104.16.183.83` | vless | US | ip-literal | 是 | mmdb 命中 104.16.183.83 -> US |
| 751 | `104.16.184.194` | vless | US | ip-literal | 是 | mmdb 命中 104.16.184.194 -> US |
| 752 | `104.16.19.242` | vless | US | ip-literal | 是 | mmdb 命中 104.16.19.242 -> US |
| 753 | `104.16.203.166` | vless | US | ip-literal | 是 | mmdb 命中 104.16.203.166 -> US |
| 754 | `104.16.209.187` | vless | US | ip-literal | 是 | mmdb 命中 104.16.209.187 -> US |
| 755 | `104.16.214.14` | vless | US | ip-literal | 是 | mmdb 命中 104.16.214.14 -> US |
| 756 | `104.16.233.169` | vless | US | ip-literal | 是 | mmdb 命中 104.16.233.169 -> US |
| 757 | `104.16.241.253` | vless | US | ip-literal | 是 | mmdb 命中 104.16.241.253 -> US |
| 758 | `104.16.25.21` | vless | US | ip-literal | 是 | mmdb 命中 104.16.25.21 -> US |
| 759 | `104.16.38.60` | vless | US | ip-literal | 是 | mmdb 命中 104.16.38.60 -> US |
| 760 | `104.16.40.145` | vless | US | ip-literal | 是 | mmdb 命中 104.16.40.145 -> US |
| 761 | `104.16.52.89` | vless | US | ip-literal | 是 | mmdb 命中 104.16.52.89 -> US |
| 762 | `104.16.6.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.6.70 -> US |
| 763 | `104.16.63.239` | vless | US | ip-literal | 是 | mmdb 命中 104.16.63.239 -> US |
| 764 | `DemonVpn🔻` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 765 | `8r<[9` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 766 | `104.16.7.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.7.70 -> US |
| 767 | `104.16.7.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.7.70 -> US |
| 768 | `104.16.71.213` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.71.213 -> US |
| 769 | `ThePackageCom` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 770 | `104.16.72.70` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.72.70 -> US |
| 771 | `104.16.75.207` | vless | US | ip-literal | 是 | mmdb 命中 104.16.75.207 -> US |
| 772 | `leviconfigs🪐-29` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 773 | `104.16.79.73` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.79.73 -> US |
| 774 | `104.16.8.237` | vless | US | ip-literal | 是 | mmdb 命中 104.16.8.237 -> US |
| 775 | `leviconfigs🪐-15` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 776 | `104.16.89.120` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.89.120 -> US |
| 777 | `v2rayng3` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 778 | `pass_net🍁🌧️` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 779 | `Alfred_Config` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 780 | `104.17.107.134` | vless | US | ip-literal | 是 | mmdb 命中 104.17.107.134 -> US |
| 781 | `Vpn_Mafia` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 782 | `104.17.121.43` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.121.43 -> US |
| 783 | `104.17.121.71` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.121.71 -> US |
| 784 | `104.17.145.145` | vless | US | ip-literal | 是 | mmdb 命中 104.17.145.145 -> US |
| 785 | `104.17.148.22` | vless | US | ip-literal | 是 | mmdb 命中 104.17.148.22 -> US |
| 786 | `104.17.161.24` | vless | US | ip-literal | 是 | mmdb 命中 104.17.161.24 -> US |
| 787 | `104.17.162.123` | vless | US | ip-literal | 是 | mmdb 命中 104.17.162.123 -> US |
| 788 | `104.17.177.143` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.177.143 -> US |
| 789 | `104.17.23.106` | vless | US | ip-literal | 是 | mmdb 命中 104.17.23.106 -> US |
| 790 | `104.17.26.230` | vless | US | ip-literal | 是 | mmdb 命中 104.17.26.230 -> US |
| 791 | `V2rayNPVTConfig` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 792 | `104.17.54.188` | vless | US | ip-literal | 是 | mmdb 命中 104.17.54.188 -> US |
| 793 | `hopev2ray🧡` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 794 | `104.18.109.147` | vless | US | ip-literal | 是 | mmdb 命中 104.18.109.147 -> US |
| 795 | `104.18.11.110` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.11.110 -> US |
| 796 | `proSSH)` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 797 | `104.18.12.149` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.12.149 -> US |
| 798 | `VPsave` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 799 | `104.18.141.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.141.67 -> US |
| 800 | `104.18.15.19` | vless | US | ip-literal | 是 | mmdb 命中 104.18.15.19 -> US |
| 801 | `104.18.151.172` | vless | US | ip-literal | 是 | mmdb 命中 104.18.151.172 -> US |
| 802 | `v2ray_configs_pools` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 803 | `ConfigV2RayNG` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 804 | `104.18.152.113` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.113 -> US |
| 805 | `104.18.152.133` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.133 -> US |
| 806 | `104.18.152.144` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.144 -> US |
| 807 | `104.18.152.149` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.149 -> US |
| 808 | `104.18.152.155` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.155 -> US |
| 809 | `104.18.152.159` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.159 -> US |
| 810 | `104.18.152.161` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.161 -> US |
| 811 | `104.18.152.187` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.187 -> US |
| 812 | `104.18.152.219` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.219 -> US |
| 813 | `104.18.152.225` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.225 -> US |
| 814 | `104.18.152.229` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.229 -> US |
| 815 | `104.18.152.233` | vless | US | ip-literal | 是 | mmdb 命中 104.18.152.233 -> US |
| 816 | `104.18.152.244` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.244 -> US |
| 817 | `104.18.152.77` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.77 -> US |
| 818 | `ConfigV2rayForFree` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 819 | `104.18.155.229` | vless | US | ip-literal | 是 | mmdb 命中 104.18.155.229 -> US |
| 820 | `104.18.22.208` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.22.208 -> US |
| 821 | `hopev2ray❤️‍🩹` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 822 | `104.18.26.90` | vless | US | ip-literal | 是 | mmdb 命中 104.18.26.90 -> US |
| 823 | `104.18.28.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.28.234 -> US |
| 824 | `104.18.33.162` | vless | US | ip-literal | 是 | mmdb 命中 104.18.33.162 -> US |
| 825 | `104.18.35.86` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.35.86 -> US |
| 826 | `v2ray313` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 827 | `leviconfigs🪐-11` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 828 | `104.18.39.55` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.39.55 -> US |
| 829 | `104.18.39.91` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.39.91 -> US |
| 830 | `cephalon_ala` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 831 | `CUSTOMVPNSERVER` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 832 | `104.18.4.138` | vless | US | ip-literal | 是 | mmdb 命中 104.18.4.138 -> US |
| 833 | `104.18.43.29` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.43.29 -> US |
| 834 | `pass_net🎃🕸️🎃` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 835 | `104.18.46.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.46.234 -> US |
| 836 | `104.18.46.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.46.234 -> US |
| 837 | `v2rayng3` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 838 | `104.19.144.99` | vless | US | ip-literal | 是 | mmdb 命中 104.19.144.99 -> US |
| 839 | `sora1co` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 840 | `104.19.214.98` | vless | US | ip-literal | 是 | mmdb 命中 104.19.214.98 -> US |
| 841 | `104.19.229.21` | vless | US | ip-literal | 是 | mmdb 命中 104.19.229.21 -> US |
| 842 | `104.19.229.21` | trojan | US | ip-literal | 是 | mmdb 命中 104.19.229.21 -> US |
| 843 | `104.19.250.20` | vless | US | ip-literal | 是 | mmdb 命中 104.19.250.20 -> US |
| 844 | `Tanhanet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 845 | `104.19.64.105` | trojan | US | ip-literal | 是 | mmdb 命中 104.19.64.105 -> US |
| 846 | `ConfigV2RayNG` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 847 | `proSSH` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 848 | `104.20.6.134` | vless | US | ip-literal | 是 | mmdb 命中 104.20.6.134 -> US |
| 849 | `MARAMBASHI` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 850 | `104.21.12.87` | trojan | US | ip-literal | 是 | mmdb 命中 104.21.12.87 -> US |
| 851 | `104.21.16.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.16.1 -> US |
| 852 | `104.21.16.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.16.1 -> US |
| 853 | `prrofile_purple` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 854 | `104.21.227.134` | vless | US | ip-literal | 是 | mmdb 命中 104.21.227.134 -> US |
| 855 | `104.21.236.63` | vless | US | ip-literal | 是 | mmdb 命中 104.21.236.63 -> US |
| 856 | `104.21.32.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.32.1 -> US |
| 857 | `104.21.38.220` | vless | US | ip-literal | 是 | mmdb 命中 104.21.38.220 -> US |
| 858 | `104.21.38.220` | vless | US | ip-literal | 是 | mmdb 命中 104.21.38.220 -> US |
| 859 | `hopev2ray💕` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 860 | `104.21.60.109` | vless | US | ip-literal | 是 | mmdb 命中 104.21.60.109 -> US |
| 861 | `Fear_Config---&security=tls&alpn=h3,h2,http` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 862 | `104.21.63.28` | vless | US | ip-literal | 是 | mmdb 命中 104.21.63.28 -> US |
| 863 | `GozargahAzad&allowInsecure=1&alpn=http` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 864 | `Shh_Proxy-New⁶` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 865 | `leviconfigs🪐-10` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 866 | `104.21.74.214` | vless | US | ip-literal | 是 | mmdb 命中 104.21.74.214 -> US |
| 867 | `104.21.74.8` | vless | US | ip-literal | 是 | mmdb 命中 104.21.74.8 -> US |
| 868 | `104.21.79.246` | trojan | US | ip-literal | 是 | mmdb 命中 104.21.79.246 -> US |
| 869 | `Tarkahodeh` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 870 | `104.21.80.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.80.1 -> US |
| 871 | `104.21.80.209` | vless | US | ip-literal | 是 | mmdb 命中 104.21.80.209 -> US |
| 872 | `hopev2ray💚` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 873 | `104.21.89.181` | vless | US | ip-literal | 是 | mmdb 命中 104.21.89.181 -> US |
| 874 | `104.21.91.244` | vless | US | ip-literal | 是 | mmdb 命中 104.21.91.244 -> US |
| 875 | `104.24.0.184` | vless | US | ip-literal | 是 | mmdb 命中 104.24.0.184 -> US |
| 876 | `104.24.140.39` | vless | US | ip-literal | 是 | mmdb 命中 104.24.140.39 -> US |
| 877 | `104.24.167.96` | vless | US | ip-literal | 是 | mmdb 命中 104.24.167.96 -> US |
| 878 | `104.24.172.153` | vless | US | ip-literal | 是 | mmdb 命中 104.24.172.153 -> US |
| 879 | `104.24.189.102` | vless | US | ip-literal | 是 | mmdb 命中 104.24.189.102 -> US |
| 880 | `Fear_Config---&security=tls&encryption=none&insecure=0&host=fs.qicai99.com&type=ws&allowInsecure=0&sni=fs.qicai99.com` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 881 | `104.24.196.67` | vless | US | ip-literal | 是 | mmdb 命中 104.24.196.67 -> US |
| 882 | `104.24.198.111` | vless | US | ip-literal | 是 | mmdb 命中 104.24.198.111 -> US |
| 883 | `104.24.218.13` | vless | US | ip-literal | 是 | mmdb 命中 104.24.218.13 -> US |
| 884 | `104.24.219.162` | vless | US | ip-literal | 是 | mmdb 命中 104.24.219.162 -> US |
| 885 | `Hope_Net-join-us-on-Telegram` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 886 | `104.24.247.189` | vless | US | ip-literal | 是 | mmdb 命中 104.24.247.189 -> US |
| 887 | `104.24.248.85` | vless | US | ip-literal | 是 | mmdb 命中 104.24.248.85 -> US |
| 888 | `104.24.52.41` | vless | US | ip-literal | 是 | mmdb 命中 104.24.52.41 -> US |
| 889 | `104.24.66.98` | vless | US | ip-literal | 是 | mmdb 命中 104.24.66.98 -> US |
| 890 | `104.24.85.213` | vless | US | ip-literal | 是 | mmdb 命中 104.24.85.213 -> US |
| 891 | `104.24.87.230` | vless | US | ip-literal | 是 | mmdb 命中 104.24.87.230 -> US |
| 892 | `104.24.91.178` | vless | US | ip-literal | 是 | mmdb 命中 104.24.91.178 -> US |
| 893 | `104.25.122.72` | vless | US | ip-literal | 是 | mmdb 命中 104.25.122.72 -> US |
| 894 | `nofiltering2` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 895 | `104.25.95.49` | trojan | US | ip-literal | 是 | mmdb 命中 104.25.95.49 -> US |
| 896 | `104.26.0.32` | vless | US | ip-literal | 是 | mmdb 命中 104.26.0.32 -> US |
| 897 | `leviconfigs🪐-23` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 898 | `104.26.13.31` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.31 -> US |
| 899 | `104.26.13.40` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.40 -> US |
| 900 | `104.26.13.54` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.54 -> US |
| 901 | `leviconfigs🪐-6` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 902 | `leviconfigs🪐-22` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 903 | `104.26.15.137` | trojan | US | ip-literal | 是 | mmdb 命中 104.26.15.137 -> US |
| 904 | `104.26.4.230` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.230 -> US |
| 905 | `104.26.4.57` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.57 -> US |
| 906 | `104.26.4.60` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.60 -> US |
| 907 | `104.26.6.89` | vless | US | ip-literal | 是 | mmdb 命中 104.26.6.89 -> US |
| 908 | `pass_net🎃🕸️🎃🇨🇦` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 909 | `tanhanet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 910 | `soskeynets` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 911 | `108.162.194.165` | vless | US | ip-literal | 是 | mmdb 命中 108.162.194.165 -> US |
| 912 | `hopev2ray💛` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 913 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 914 | `pass_net🎃🕸️🎃🇪🇸` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 915 | `141.193.27.4` | vless | US | ip-literal | 是 | mmdb 命中 141.193.27.4 -> US |
| 916 | `146.75.57.111` | vless | US | ip-literal | 是 | mmdb 命中 146.75.57.111 -> US |
| 917 | `MiTiVPN&security=tls&fp=chrome&sni=cdn.akamai.steamstatic.com&alpn=http` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 918 | `146.75.59.186` | vless | US | ip-literal | 是 | mmdb 命中 146.75.59.186 -> US |
| 919 | `hopev2ray🤍` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 920 | `vmesskhodam` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 921 | `V2ray_confiig` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 922 | `Napsternetvirani` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 923 | `probabblynot-mci4` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 924 | `oneclickvpnkeys` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 925 | `162.159.15.39` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.15.39 -> US |
| 926 | `162.159.153.4` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.153.4 -> US |
| 927 | `162.159.156.214` | vless | US | ip-literal | 是 | mmdb 命中 162.159.156.214 -> US |
| 928 | `162.159.198.1` | vless | US | ip-literal | 是 | mmdb 命中 162.159.198.1 -> US |
| 929 | `162.159.24.39` | vless | US | ip-literal | 是 | mmdb 命中 162.159.24.39 -> US |
| 930 | `162.159.3.176` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.3.176 -> US |
| 931 | `162.159.42.163` | vless | US | ip-literal | 是 | mmdb 命中 162.159.42.163 -> US |
| 932 | `162.159.43.187` | vless | US | ip-literal | 是 | mmdb 命中 162.159.43.187 -> US |
| 933 | `162.159.46.0` | vless | US | ip-literal | 是 | mmdb 命中 162.159.46.0 -> US |
| 934 | `162.159.60.167` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.60.167 -> US |
| 935 | `162.159.91.211` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.91.211 -> US |
| 936 | `164.38.155.135` | vless | GB | ip-literal | 否 | mmdb 命中 164.38.155.135 -> GB |
| 937 | `167.68.4.199` | trojan | US | ip-literal | 是 | mmdb 命中 167.68.4.199 -> US |
| 938 | `sora1co` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 939 | `pirozi_ArGaP` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 940 | `Tarkshodeh` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 941 | `172.64.144.198` | vless | US | ip-literal | 是 | mmdb 命中 172.64.144.198 -> US |
| 942 | `172.64.148.165` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.148.165 -> US |
| 943 | `172.64.148.248` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.148.248 -> US |
| 944 | `172.64.149.54` | vless | US | ip-literal | 是 | mmdb 命中 172.64.149.54 -> US |
| 945 | `ATLAS_V2VPN🆓️📶🛰️684🌐🆕` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 946 | `172.64.150.28` | vless | US | ip-literal | 是 | mmdb 命中 172.64.150.28 -> US |
| 947 | `KAFING_2` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 948 | `172.64.154.8` | vless | US | ip-literal | 是 | mmdb 命中 172.64.154.8 -> US |
| 949 | `mehrosaboran` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 950 | `172.64.157.230` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.157.230 -> US |
| 951 | `172.64.159.64` | vless | US | ip-literal | 是 | mmdb 命中 172.64.159.64 -> US |
| 952 | `172.64.38.50` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.38.50 -> US |
| 953 | `172.64.52.230` | vless | US | ip-literal | 是 | mmdb 命中 172.64.52.230 -> US |
| 954 | `172.64.86.167` | vless | US | ip-literal | 是 | mmdb 命中 172.64.86.167 -> US |
| 955 | `172.64.88.168` | vless | US | ip-literal | 是 | mmdb 命中 172.64.88.168 -> US |
| 956 | `172.64.88.251` | vless | US | ip-literal | 是 | mmdb 命中 172.64.88.251 -> US |
| 957 | `172.64.92.243` | vless | US | ip-literal | 是 | mmdb 命中 172.64.92.243 -> US |
| 958 | `172.65.90.52` | vless | US | ip-literal | 是 | mmdb 命中 172.65.90.52 -> US |
| 959 | `172.66.140.62` | vless | US | ip-literal | 是 | mmdb 命中 172.66.140.62 -> US |
| 960 | `172.66.170.53` | vless | US | ip-literal | 是 | mmdb 命中 172.66.170.53 -> US |
| 961 | `172.66.40.99` | vless | US | ip-literal | 是 | mmdb 命中 172.66.40.99 -> US |
| 962 | `Selinc` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 963 | `172.67.131.125` | vless | US | ip-literal | 是 | mmdb 命中 172.67.131.125 -> US |
| 964 | `172.67.139.85` | vless | US | ip-literal | 是 | mmdb 命中 172.67.139.85 -> US |
| 965 | `172.67.139.85` | vless | US | ip-literal | 是 | mmdb 命中 172.67.139.85 -> US |
| 966 | `172.67.143.24` | vless | US | ip-literal | 是 | mmdb 命中 172.67.143.24 -> US |
| 967 | `172.67.143.56` | vless | US | ip-literal | 是 | mmdb 命中 172.67.143.56 -> US |
| 968 | `172.67.148.163` | vless | US | ip-literal | 是 | mmdb 命中 172.67.148.163 -> US |
| 969 | `172.67.149.60` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.149.60 -> US |
| 970 | `172.67.155.199` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.155.199 -> US |
| 971 | `AZARBAYJAB1)` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 972 | `172.67.155.65` | vless | US | ip-literal | 是 | mmdb 命中 172.67.155.65 -> US |
| 973 | `172.67.158.89` | vless | US | ip-literal | 是 | mmdb 命中 172.67.158.89 -> US |
| 974 | `172.67.172.95` | vless | US | ip-literal | 是 | mmdb 命中 172.67.172.95 -> US |
| 975 | `172.67.204.84` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.204.84 -> US |
| 976 | `172.67.208.1` | vless | US | ip-literal | 是 | mmdb 命中 172.67.208.1 -> US |
| 977 | `172.67.209.127` | vless | US | ip-literal | 是 | mmdb 命中 172.67.209.127 -> US |
| 978 | `172.67.213.218` | vless | US | ip-literal | 是 | mmdb 命中 172.67.213.218 -> US |
| 979 | `hopev2ray💯` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 980 | `172.67.217.240` | vless | US | ip-literal | 是 | mmdb 命中 172.67.217.240 -> US |
| 981 | `172.67.222.117` | vless | US | ip-literal | 是 | mmdb 命中 172.67.222.117 -> US |
| 982 | `172.67.65.56` | vless | US | ip-literal | 是 | mmdb 命中 172.67.65.56 -> US |
| 983 | `172.67.68.248` | vless | US | ip-literal | 是 | mmdb 命中 172.67.68.248 -> US |
| 984 | `Azarakhsh_Proxy+🩷` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 985 | `leviconfigs🪐-3` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 986 | `172.67.74.10` | vless | US | ip-literal | 是 | mmdb 命中 172.67.74.10 -> US |
| 987 | `Fear_Config---&security=tls&encryption=none&insecure=0&host=fs.qicai99.com&fp=chrome&type=ws&allowInsecure=0&sni=fs.qicai99.com` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 988 | `172.67.74.2` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.74.2 -> US |
| 989 | `173.245.49.114` | vless | US | ip-literal | 是 | mmdb 命中 173.245.49.114 -> US |
| 990 | `173.245.49.157` | vless | US | ip-literal | 是 | mmdb 命中 173.245.49.157 -> US |
| 991 | `173.245.58.183` | trojan | US | ip-literal | 是 | mmdb 命中 173.245.58.183 -> US |
| 992 | `173.245.58.75` | vless | US | ip-literal | 是 | mmdb 命中 173.245.58.75 -> US |
| 993 | `185.146.173.58` | vless | SE | ip-literal | 否 | mmdb 命中 185.146.173.58 -> SE |
| 994 | `185.146.173.59` | vless | SE | ip-literal | 否 | mmdb 命中 185.146.173.59 -> SE |
| 995 | `185.18.250.127` | vless | CH | ip-literal | 否 | mmdb 命中 185.18.250.127 -> CH |
| 996 | `JavidnamanIran` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 997 | `185.18.250.245` | trojan | CH | ip-literal | 否 | mmdb 命中 185.18.250.245 -> CH |
| 998 | `188.114.96.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.3 -> US |
| 999 | `188.114.96.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.3 -> US |
| 1000 | `188.114.96.37` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.37 -> US |
| 1001 | `188.114.97.2` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.2 -> US |
| 1002 | `tootffarangi🍓-2` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1003 | `188.114.97.3` | trojan | US | ip-literal | 是 | mmdb 命中 188.114.97.3 -> US |
| 1004 | `188.114.97.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.3 -> US |
| 1005 | `188.114.97.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.3 -> US |
| 1006 | `188.114.97.4` | trojan | US | ip-literal | 是 | mmdb 命中 188.114.97.4 -> US |
| 1007 | `188.114.97.6` | trojan | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1008 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1009 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1010 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1011 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1012 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1013 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1014 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1015 | `188.114.97.8` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.8 -> US |
| 1016 | `188.114.98.0` | trojan | US | ip-literal | 是 | mmdb 命中 188.114.98.0 -> US |
| 1017 | `188.114.98.0` | vless | US | ip-literal | 是 | mmdb 命中 188.114.98.0 -> US |
| 1018 | `188.114.98.112` | vless | US | ip-literal | 是 | mmdb 命中 188.114.98.112 -> US |
| 1019 | `188.114.99.137` | vless | US | ip-literal | 是 | mmdb 命中 188.114.99.137 -> US |
| 1020 | `188.164.248.122` | trojan | NL | ip-literal | 否 | mmdb 命中 188.164.248.122 -> NL |
| 1021 | `188.42.89.118` | vless | LU | ip-literal | 否 | mmdb 命中 188.42.89.118 -> LU |
| 1022 | `pass_net🎃🕸️🎃🇨🇷` | trojan | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1023 | `probabblynot-mci5` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1024 | `198.62.62.23` | trojan | US | ip-literal | 是 | mmdb 命中 198.62.62.23 -> US |
| 1025 | `199.232.245.94` | vless | US | ip-literal | 是 | mmdb 命中 199.232.245.94 -> US |
| 1026 | `Selinc` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1027 | `162.35.38.156` | vless | US | ip-literal | 是 | mmdb 命中 162.35.38.156 -> US |
| 1028 | `sclass-b1.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 1029 | `sclass-b1.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 1030 | `zfapi.zalolink.com` | vless | JP | domain-resolved | 否 | 解析到 3.115.11.119 -> JP |
| 1031 | `,` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1032 | `your-proxy-link...` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1033 | `vp3.yysyy.online` | hysteria2 | JP | domain-resolved | 否 | 解析到 45.32.10.7 -> JP |
| 1034 | `freedom.chenlan.top` | hysteria2 | JP | domain-resolved | 否 | 解析到 85.121.123.197 -> JP |
| 1035 | `45.32.10.7` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 45.32.10.7 -> JP |
| 1036 | `202.146.222.29` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.29 -> HK |
| 1037 | `163.192.14.135` | hysteria2 | US | ip-literal | 是 | mmdb 命中 163.192.14.135 -> US |
| 1038 | `155.248.209.237` | hysteria2 | US | ip-literal | 是 | mmdb 命中 155.248.209.237 -> US |
| 1039 | `us.mi11o4ka.com` | hysteria2 | US | domain-resolved | 是 | 解析到 167.148.201.99 -> US |
| 1040 | `149.28.130.108` | trojan | SG | ip-literal | 否 | mmdb 命中 149.28.130.108 -> SG |
| 1041 | `139.180.146.200` | trojan | SG | ip-literal | 否 | mmdb 命中 139.180.146.200 -> SG |
| 1042 | `45.76.98.127` | vless | JP | ip-literal | 否 | mmdb 命中 45.76.98.127 -> JP |
| 1043 | `ga1data.xyy123.bid` | vless | JP | domain-resolved | 否 | 解析到 103.232.213.114 -> JP |
| 1044 | `104.19.164.155` | vless | US | ip-literal | 是 | mmdb 命中 104.19.164.155 -> US |
| 1045 | `165.154.63.139` | vless | HK | ip-literal | 否 | mmdb 命中 165.154.63.139 -> HK |
| 1046 | `support.zoom.us` | vless | US | domain-resolved | 是 | 解析到 170.114.46.6 -> US |
| 1047 | `172.237.88.103` | vless | SG | ip-literal | 否 | mmdb 命中 172.237.88.103 -> SG |
| 1048 | `18.183.215.124` | vless | JP | ip-literal | 否 | mmdb 命中 18.183.215.124 -> JP |
| 1049 | `3.39.4.109` | vless | KR | ip-literal | 否 | mmdb 命中 3.39.4.109 -> KR |
| 1050 | `54.169.200.246` | vless | SG | ip-literal | 否 | mmdb 命中 54.169.200.246 -> SG |
| 1051 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1052 | `45.32.52.173` | trojan | JP | ip-literal | 否 | mmdb 命中 45.32.52.173 -> JP |
| 1053 | `kr002.zestapp778.com` | trojan | KR | domain-resolved | 否 | 解析到 141.164.63.80 -> KR |
| 1054 | `in002.zestapp778.com` | trojan | IN | domain-resolved | 否 | 解析到 139.84.139.150 -> IN |
| 1055 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1056 | `188.114.98.0` | vless | US | ip-literal | 是 | mmdb 命中 188.114.98.0 -> US |
| 1057 | `104.19.12.94` | vless | US | ip-literal | 是 | mmdb 命中 104.19.12.94 -> US |
| 1058 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1059 | `134.185.81.5` | vless | SG | ip-literal | 否 | mmdb 命中 134.185.81.5 -> SG |
| 1060 | `3.39.4.109` | vless | KR | ip-literal | 否 | mmdb 命中 3.39.4.109 -> KR |
| 1061 | `n04.jinggai.online` | vless | US | domain-resolved | 是 | 解析到 172.67.165.32 -> US |
| 1062 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1063 | `54.251.9.130` | vless | SG | ip-literal | 否 | mmdb 命中 54.251.9.130 -> SG |
| 1064 | `170.114.45.6` | vless | US | ip-literal | 是 | mmdb 命中 170.114.45.6 -> US |
| 1065 | `151.245.106.49` | vless | KR | ip-literal | 否 | mmdb 命中 151.245.106.49 -> KR |
| 1066 | `45.76.172.197` | vless | US | ip-literal | 是 | mmdb 命中 45.76.172.197 -> US |
| 1067 | `104.17.50.227` | vless | US | ip-literal | 是 | mmdb 命中 104.17.50.227 -> US |
| 1068 | `129.213.91.185` | hysteria2 | US | ip-literal | 是 | mmdb 命中 129.213.91.185 -> US |
| 1069 | `43.167.186.78` | trojan | JP | ip-literal | 否 | mmdb 命中 43.167.186.78 -> JP |
| 1070 | `216.238.80.100` | trojan | MX | ip-literal | 否 | mmdb 命中 216.238.80.100 -> MX |
| 1071 | `45.132.75.213` | vless | SG | ip-literal | 否 | mmdb 命中 45.132.75.213 -> SG |
| 1072 | `206.206.76.75` | vless | SG | ip-literal | 否 | mmdb 命中 206.206.76.75 -> SG |
| 1073 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1074 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1075 | `45.32.69.110` | vless | US | ip-literal | 是 | mmdb 命中 45.32.69.110 -> US |
| 1076 | `51.81.203.63` | vless | US | ip-literal | 是 | mmdb 命中 51.81.203.63 -> US |
| 1077 | `31.172.69.31` | vless | US | ip-literal | 是 | mmdb 命中 31.172.69.31 -> US |
| 1078 | `91.196.33.157` | vless | RU | ip-literal | 否 | mmdb 命中 91.196.33.157 -> RU |
| 1079 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 1080 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 1081 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 1082 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 1083 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 1084 | `103.106.229.37` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.37 -> SG |
| 1085 | `198.46.146.118` | hysteria2 | US | ip-literal | 是 | mmdb 命中 198.46.146.118 -> US |
| 1086 | `3.64.194.247` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.64.194.247 -> DE |
| 1087 | `125.227.86.45` | trojan | TW | ip-literal | 否 | mmdb 命中 125.227.86.45 -> TW |
| 1088 | `us007.zestapp778.com` | trojan | US | domain-resolved | 是 | 解析到 45.63.78.241 -> US |
| 1089 | `104.21.70.21` | vless | US | ip-literal | 是 | mmdb 命中 104.21.70.21 -> US |
| 1090 | `104.18.40.171` | vless | US | ip-literal | 是 | mmdb 命中 104.18.40.171 -> US |
| 1091 | `170.114.46.6` | vless | US | ip-literal | 是 | mmdb 命中 170.114.46.6 -> US |
| 1092 | `104.17.50.53` | vless | US | ip-literal | 是 | mmdb 命中 104.17.50.53 -> US |
| 1093 | `139.162.27.96` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.27.96 -> SG |
| 1094 | `sg2-8sb.6121999.dpdns.org` | vless | SG | domain-resolved | 否 | 解析到 146.235.16.130 -> SG |
| 1095 | `104.21.6.186` | vless | US | ip-literal | 是 | mmdb 命中 104.21.6.186 -> US |
| 1096 | `154.26.188.52` | vless | US | ip-literal | 是 | mmdb 命中 154.26.188.52 -> US |
| 1097 | `15.204.97.214` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.214 -> US |
| 1098 | `162.159.254.3` | vless | US | ip-literal | 是 | mmdb 命中 162.159.254.3 -> US |
| 1099 | `144.202.126.147` | vless | US | ip-literal | 是 | mmdb 命中 144.202.126.147 -> US |
| 1100 | `5.253.42.164` | vless | CY | ip-literal | 否 | mmdb 命中 5.253.42.164 -> CY |
| 1101 | `185.168.208.190` | vless | US | ip-literal | 是 | mmdb 命中 185.168.208.190 -> US |
| 1102 | `fast.145779.xyz` | vless | US | domain-resolved | 是 | 解析到 172.67.199.126 -> US |
| 1103 | `152.69.200.216` | vless | JP | ip-literal | 否 | mmdb 命中 152.69.200.216 -> JP |
| 1104 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 1105 | `169.40.42.235` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.235 -> DE |
| 1106 | `169.40.42.104` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.104 -> DE |
| 1107 | `189.74.114.119` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.114.119 -> RU |
| 1108 | `66.70.179.198` | vless | CA | ip-literal | 否 | mmdb 命中 66.70.179.198 -> CA |
| 1109 | `169.40.42.225` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.225 -> DE |
| 1110 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 1111 | `31.56.189.208` | vless | DE | ip-literal | 否 | mmdb 命中 31.56.189.208 -> DE |
| 1112 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1113 | `connect.hondamotor.site` | vless | DE | domain-resolved | 否 | 解析到 178.83.45.226 -> DE |
| 1114 | `rb.mangshe.xyz` | hysteria2 | JP | domain-resolved | 否 | 解析到 89.125.244.249 -> JP |
| 1115 | `167.148.201.99` | hysteria2 | US | ip-literal | 是 | mmdb 命中 167.148.201.99 -> US |
| 1116 | `66.163.112.242` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.242 -> US |
| 1117 | `66.163.114.132` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.132 -> US |
| 1118 | `2.27.109.179` | trojan | HK | ip-literal | 否 | mmdb 命中 2.27.109.179 -> HK |
| 1119 | `104.16.0.1` | vless | US | ip-literal | 是 | mmdb 命中 104.16.0.1 -> US |
| 1120 | `112.169.175.199` | vless | KR | ip-literal | 否 | mmdb 命中 112.169.175.199 -> KR |
| 1121 | `104.16.10.185` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.185 -> US |
| 1122 | `104.16.10.56` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.56 -> US |
| 1123 | `saas.sin.fan` | vless | US | domain-resolved | 是 | 解析到 162.159.135.234 -> US |
| 1124 | `154.31.114.162` | vless | JP | ip-literal | 否 | mmdb 命中 154.31.114.162 -> JP |
| 1125 | `saas.sin.fan` | vless | US | domain-resolved | 是 | 解析到 162.159.135.234 -> US |
| 1126 | `us1.oh-node.com` | vless | US | domain-resolved | 是 | 解析到 173.255.249.76 -> US |
| 1127 | `162.35.8.62` | vless | US | ip-literal | 是 | mmdb 命中 162.35.8.62 -> US |
| 1128 | `104.16.10.2` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.2 -> US |
| 1129 | `104.19.48.107` | vless | US | ip-literal | 是 | mmdb 命中 104.19.48.107 -> US |
| 1130 | `15.204.97.219` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.219 -> US |
| 1131 | `103.238.227.211` | vless | HK | ip-literal | 否 | mmdb 命中 103.238.227.211 -> HK |
| 1132 | `45.154.26.63` | vless | TH | ip-literal | 否 | mmdb 命中 45.154.26.63 -> TH |
| 1133 | `103.238.227.211` | vless | HK | ip-literal | 否 | mmdb 命中 103.238.227.211 -> HK |
| 1134 | `526.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 195.172.138.26 -> SG |
| 1135 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 1136 | `169.40.42.224` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.224 -> DE |
| 1137 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1138 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1139 | `177.7.51.29` | vless | BR | ip-literal | 否 | mmdb 命中 177.7.51.29 -> BR |
| 1140 | `83.147.232.69` | vless | NL | ip-literal | 否 | mmdb 命中 83.147.232.69 -> NL |
| 1141 | `193.233.253.180` | vless | RU | ip-literal | 否 | mmdb 命中 193.233.253.180 -> RU |
| 1142 | `178.212.35.198` | vless | IN | ip-literal | 否 | mmdb 命中 178.212.35.198 -> IN |
| 1143 | `th001.zestapp778.com` | trojan | TH | domain-resolved | 否 | 解析到 38.60.233.126 -> TH |
| 1144 | `66.163.114.166` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.166 -> US |
| 1145 | `216.152.156.49` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.49 -> US |
| 1146 | `66.163.114.126` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.126 -> US |
| 1147 | `216.152.156.65` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.65 -> US |
| 1148 | `170.101.101.19` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.19 -> US |
| 1149 | `mx001.zestapp778.com` | trojan | MX | domain-resolved | 否 | 解析到 149.104.87.125 -> MX |
| 1150 | `208.69.78.19` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.19 -> CH |
| 1151 | `104.17.210.74` | vless | US | ip-literal | 是 | mmdb 命中 104.17.210.74 -> US |
| 1152 | `31.76.91.31` | vless | JP | ip-literal | 否 | mmdb 命中 31.76.91.31 -> JP |
| 1153 | `www.speedtest.net` | vless | US | domain-resolved | 是 | 解析到 104.17.147.22 -> US |
| 1154 | `us3.oh-node.com` | vless | US | domain-resolved | 是 | 解析到 64.227.91.141 -> US |
| 1155 | `104.21.0.87` | vless | US | ip-literal | 是 | mmdb 命中 104.21.0.87 -> US |
| 1156 | `5.253.28.224` | vless | CY | ip-literal | 否 | mmdb 命中 5.253.28.224 -> CY |
| 1157 | `45.63.53.81` | vless | US | ip-literal | 是 | mmdb 命中 45.63.53.81 -> US |
| 1158 | `108.61.119.63` | vless | US | ip-literal | 是 | mmdb 命中 108.61.119.63 -> US |
| 1159 | `154.21.203.106` | vless | HK | ip-literal | 否 | mmdb 命中 154.21.203.106 -> HK |
| 1160 | `195.123.235.183` | vless | US | ip-literal | 是 | mmdb 命中 195.123.235.183 -> US |
| 1161 | `5.149.249.94` | vless | NL | ip-literal | 否 | mmdb 命中 5.149.249.94 -> NL |
| 1162 | `5.34.178.120` | vless | US | ip-literal | 是 | mmdb 命中 5.34.178.120 -> US |
| 1163 | `connect.wecantos.site` | vless | DE | domain-resolved | 否 | 解析到 178.83.45.226 -> DE |
| 1164 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1165 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1166 | `xray1-direct-mci1-fs-ce.freesocks.work` | vless | US | domain-resolved | 是 | 解析到 23.191.200.206 -> US |
| 1167 | `site.teslamotor.site` | vless | DE | domain-resolved | 否 | 解析到 178.83.45.226 -> DE |
| 1168 | `178.83.45.226` | vless | DE | ip-literal | 否 | mmdb 命中 178.83.45.226 -> DE |
| 1169 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1170 | `54.71.51.243` | vless | US | ip-literal | 是 | mmdb 命中 54.71.51.243 -> US |
| 1171 | `208.69.78.217` | vless | CH | ip-literal | 否 | mmdb 命中 208.69.78.217 -> CH |
| 1172 | `sg2-xr.zgrelay.com` | vless | - | unknown | 否 | DNS 解析失败或超时 |
| 1173 | `9.247.23.209` | vless | DE | ip-literal | 否 | mmdb 命中 9.247.23.209 -> DE |
| 1174 | `edge.bookmai.com` | vless | DE | domain-resolved | 否 | 解析到 163.245.42.85 -> DE |
| 1175 | `milo.rubinaz.xyz` | vless | DE | domain-resolved | 否 | 解析到 168.222.43.53 -> DE |
| 1176 | `51.77.217.70` | vless | FR | ip-literal | 否 | mmdb 命中 51.77.217.70 -> FR |
| 1177 | `212.227.235.66` | vless | ES | ip-literal | 否 | mmdb 命中 212.227.235.66 -> ES |
| 1178 | `51.89.194.151` | vless | GB | ip-literal | 否 | mmdb 命中 51.89.194.151 -> GB |
| 1179 | `13.140.56.100` | vless | IN | ip-literal | 否 | mmdb 命中 13.140.56.100 -> IN |
| 1180 | `192.142.23.46` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 192.142.23.46 -> SE |
| 1181 | `ca001.zestapp778.com` | trojan | CA | domain-resolved | 否 | 解析到 149.248.50.252 -> CA |
| 1182 | `169.197.140.245` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.245 -> US |
| 1183 | `169.197.140.218` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.218 -> US |
| 1184 | `70.34.252.255` | trojan | PL | ip-literal | 否 | mmdb 命中 70.34.252.255 -> PL |
| 1185 | `104.21.33.59` | vless | US | ip-literal | 是 | mmdb 命中 104.21.33.59 -> US |
| 1186 | `46.250.250.149` | vless | GB | ip-literal | 否 | mmdb 命中 46.250.250.149 -> GB |
| 1187 | `104.21.70.228` | vless | US | ip-literal | 是 | mmdb 命中 104.21.70.228 -> US |
| 1188 | `46.137.202.178` | vless | SG | ip-literal | 否 | mmdb 命中 46.137.202.178 -> SG |
| 1189 | `43.170.8.95` | vless | SG | ip-literal | 否 | mmdb 命中 43.170.8.95 -> SG |
| 1190 | `172.64.152.52` | vless | US | ip-literal | 是 | mmdb 命中 172.64.152.52 -> US |
| 1191 | `139.162.27.96` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.27.96 -> SG |
| 1192 | `172.237.88.103` | vless | SG | ip-literal | 否 | mmdb 命中 172.237.88.103 -> SG |
| 1193 | `ryanserver.ir` | vless | - | unknown | 否 | DNS 解析失败或超时 |
| 1194 | `191.217.206.147` | vless | SE | ip-literal | 否 | mmdb 命中 191.217.206.147 -> SE |
| 1195 | `191.217.206.147` | vless | SE | ip-literal | 否 | mmdb 命中 191.217.206.147 -> SE |
| 1196 | `gold.jafarghasemiturkk.ir` | vless | - | unknown | 否 | DNS 解析失败或超时 |
| 1197 | `191.217.206.147` | vless | SE | ip-literal | 否 | mmdb 命中 191.217.206.147 -> SE |
| 1198 | `104.18.138.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.138.67 -> US |
| 1199 | `191.217.206.147` | vless | SE | ip-literal | 否 | mmdb 命中 191.217.206.147 -> SE |
| 1200 | `xray-ckc68nno-swift-harbor-8.cloady.io` | vless | GB | domain-resolved | 否 | 解析到 94.72.100.12 -> GB |
| 1201 | `961ec0g.nl17.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 93.123.85.189 -> DE |
| 1202 | `104.18.139.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.139.67 -> US |
| 1203 | `8a2e72t.nl20.h1clayd.shop` | vless | DE | domain-resolved | 否 | 解析到 153.56.230.52 -> DE |
| 1204 | `5.129.202.80` | vless | RU | ip-literal | 否 | mmdb 命中 5.129.202.80 -> RU |
| 1205 | `88.216.60.73` | vless | SE | ip-literal | 否 | mmdb 命中 88.216.60.73 -> SE |

## 按 cc 分布统计

| cc | 节点数 |
|----|--------|
| US | 435 |
| DE | 137 |
| NL | 99 |
| (unknown) | 93 |
| GB | 77 |
| RU | 59 |
| SG | 39 |
| FR | 29 |
| JP | 28 |
| SE | 21 |
| HK | 18 |
| PL | 15 |
| KR | 13 |
| CA | 12 |
| CH | 11 |
| AE | 10 |
| TW | 10 |
| IE | 8 |
| AU | 7 |
| CZ | 7 |
| TR | 7 |
| ES | 6 |
| BR | 5 |
| IN | 5 |
| SC | 5 |
| BG | 4 |
| CY | 4 |
| FI | 4 |
| LV | 4 |
| IR | 3 |
| IT | 3 |
| RO | 3 |
| CL | 2 |
| EE | 2 |
| KZ | 2 |
| LT | 2 |
| LU | 2 |
| MX | 2 |
| TH | 2 |
| AT | 1 |
| BH | 1 |
| CN | 1 |
| GR | 1 |
| IL | 1 |
| IQ | 1 |
| RS | 1 |
| SK | 1 |
| UA | 1 |
| ZA | 1 |

## 过滤原因分类计数

| 原因类别 | 数量 | 含义 |
|----------|------|------|
| non_us_country | 677 | mmdb 命中但国家码非 US |
| unknown | 93 | DNS失败/超时、URI碎片假域名、私有保留段、mmdb非标准ISO码 |

## URL 编码碎片节点（单独点名）

- 本次输入未发现 URL 编码碎片节点。

## 判定规则与依据

- IP 字面量（IPv4/IPv6）：`ipaddress` 识别 → 私有/回环/保留段直接排除 → 其余查 mmdb，`country.iso_code` 回退 `registered_country`。
- 域名：仅对合法 FQDN 做 `socket.getaddrinfo`，用 ThreadPoolExecutor + future.result(timeout=4s) 防卡死；超时/失败按 unknown；多 IP 取首个公网 IP。
- mmdb 非标准 ISO 码（如 8.8.8.8 返回 `GOOGLE`）不认定为 US，按 unknown 排除。
- README URI 解析出的碎片假 hostname（如 `23c82941`/`150`/`linlin`/`c3a8753e`/`vpn`/`srv`）不是合法域名，不做 DNS 解析，按 unknown 排除。
- URL 含 `%XX` 的 server 先 `urllib.parse.unquote`；解码后仍非合法 hostname/IP 判 invalid_server。
- 入选红线：`cc == "US"` 且 `type ∈ {anytls, hysteria, hysteria2, trojan, tuic, vless}`。

产出：`us_nodes.json`（US 节点 435）+ 本报告。
