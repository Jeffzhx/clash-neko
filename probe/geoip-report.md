# U3 GeoIP / 美国判定报告

- 生成时间：2026-11-20T10:44:31+00:00
- 查询日期：2026-11-20（本地）；UTC 2026-11-20
- 输入：`nodes_raw.json`（2020 节点）；背景：`sources.json`（68 个低星来源）
- mmdb 路径：`/home/runner/work/_temp/Country.mmdb`
- mmdb 版本元数据：database_type=GeoLite2-Country；build_epoch=1794932458（2026-11-17T16:20:58+00:00）；ip_version=6；record_size=24
- 优质协议白名单：anytls, hysteria, hysteria2, trojan, tuic, vless
- 结果：**US 优质节点 625** / 输入 2020 / 过滤 1395

## 逐节点判定（server / type / cc / cc_basis / 是否入选）

| # | server | type | cc | cc_basis | 是否入选 | 说明 |
|---|--------|------|----|----------|----------|------|
| 1 | `167.88.61.85` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.85 -> US |
| 2 | `167.88.61.193` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.193 -> US |
| 3 | `resources.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.33 -> US |
| 4 | `150.241.83.223` | vless | US | ip-literal | 是 | mmdb 命中 150.241.83.223 -> US |
| 5 | `216.152.155.50` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.50 -> US |
| 6 | `216.106.186.46` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.46 -> US |
| 7 | `167.88.61.52` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.52 -> US |
| 8 | `169.40.42.168` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.168 -> DE |
| 9 | `66.163.112.171` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.171 -> US |
| 10 | `169.197.140.171` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.171 -> US |
| 11 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 12 | `216.152.156.49` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.49 -> US |
| 13 | `198.247.127.131` | vless | US | ip-literal | 是 | mmdb 命中 198.247.127.131 -> US |
| 14 | `170.101.101.131` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.131 -> US |
| 15 | `167.88.61.198` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.198 -> US |
| 16 | `167.17.69.171` | vless | US | ip-literal | 是 | mmdb 命中 167.17.69.171 -> US |
| 17 | `66.163.122.26` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.26 -> US |
| 18 | `170.101.101.19` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.19 -> US |
| 19 | `170.101.101.112` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.112 -> US |
| 20 | `170.101.101.211` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.211 -> US |
| 21 | `216.152.155.131` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.131 -> US |
| 22 | `51.158.206.20` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.20 -> NL |
| 23 | `169.197.140.169` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.169 -> US |
| 24 | `216.152.156.159` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.159 -> US |
| 25 | `193.108.119.34` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.34 -> DE |
| 26 | `167.88.61.20` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.20 -> US |
| 27 | `147.45.60.136` | vless | US | ip-literal | 是 | mmdb 命中 147.45.60.136 -> US |
| 28 | `51.158.206.26` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.26 -> NL |
| 29 | `169.40.42.90` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.90 -> DE |
| 30 | `69.48.201.136` | vless | US | ip-literal | 是 | mmdb 命中 69.48.201.136 -> US |
| 31 | `45.144.112.55` | vless | US | ip-literal | 是 | mmdb 命中 45.144.112.55 -> US |
| 32 | `159.89.87.21` | vless | US | ip-literal | 是 | mmdb 命中 159.89.87.21 -> US |
| 33 | `15.204.97.195` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.195 -> US |
| 34 | `steel7.hadsvpn.com` | hysteria2 | DE | domain-resolved | 否 | 解析到 201.58.142.83 -> DE |
| 35 | `93.123.101.198` | vless | DE | ip-literal | 否 | mmdb 命中 93.123.101.198 -> DE |
| 36 | `170.101.101.53` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.53 -> US |
| 37 | `169.40.42.35` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.35 -> DE |
| 38 | `66.163.114.45` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.45 -> US |
| 39 | `216.152.147.152` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.152 -> CA |
| 40 | `91.107.188.129` | vless | DE | ip-literal | 否 | mmdb 命中 91.107.188.129 -> DE |
| 41 | `94.183.164.119` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 42 | `vps3.nemnogogo.com` | vless | RU | domain-resolved | 否 | 解析到 201.51.12.98 -> RU |
| 43 | `193.108.119.78` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.78 -> DE |
| 44 | `ww13.levikogjgfdd.ir` | vless | US | domain-resolved | 是 | 解析到 15.204.97.206 -> US |
| 45 | `216.152.156.81` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.81 -> US |
| 46 | `170.101.101.237` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.237 -> US |
| 47 | `51.158.206.96` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.96 -> NL |
| 48 | `177.177.215.45` | vless | NL | ip-literal | 否 | mmdb 命中 177.177.215.45 -> NL |
| 49 | `51.158.206.87` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.87 -> NL |
| 50 | `51.158.206.25` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.25 -> NL |
| 51 | `130.12.242.106` | vless | NL | ip-literal | 否 | mmdb 命中 130.12.242.106 -> NL |
| 52 | `169.40.42.229` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.229 -> DE |
| 53 | `216.152.156.212` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.212 -> US |
| 54 | `212.102.38.25` | vless | CZ | ip-literal | 否 | mmdb 命中 212.102.38.25 -> CZ |
| 55 | `201.24.116.192` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.116.192 -> RU |
| 56 | `201.51.12.98` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.12.98 -> RU |
| 57 | `ams2.shtil.io` | vless | NL | domain-resolved | 否 | 解析到 177.177.215.45 -> NL |
| 58 | `66.163.112.31` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.31 -> US |
| 59 | `2.59.183.167` | vless | NL | ip-literal | 否 | mmdb 命中 2.59.183.167 -> NL |
| 60 | `152.70.58.201` | vless | NL | ip-literal | 否 | mmdb 命中 152.70.58.201 -> NL |
| 61 | `143.246.41.214` | vless | EE | ip-literal | 否 | mmdb 命中 143.246.41.214 -> EE |
| 62 | `185.255.115.118` | vless | DE | ip-literal | 否 | mmdb 命中 185.255.115.118 -> DE |
| 63 | `185.255.115.181` | vless | DE | ip-literal | 否 | mmdb 命中 185.255.115.181 -> DE |
| 64 | `76574ct.nl8.h1clayd.click` | vless | SK | domain-resolved | 否 | 解析到 196.245.153.111 -> SK |
| 65 | `196.245.153.111` | vless | SK | ip-literal | 否 | mmdb 命中 196.245.153.111 -> SK |
| 66 | `7aa271t.es9.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.67.148 -> EE |
| 67 | `201.8.64.226` | vless | NL | ip-literal | 否 | mmdb 命中 201.8.64.226 -> NL |
| 68 | `195.206.235.222` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.222 -> NL |
| 69 | `185.95.231.156` | vless | IL | ip-literal | 否 | mmdb 命中 185.95.231.156 -> IL |
| 70 | `179.254.191.251` | hysteria2 | US | ip-literal | 是 | mmdb 命中 179.254.191.251 -> US |
| 71 | `139.84.231.142` | trojan | ZA | ip-literal | 否 | mmdb 命中 139.84.231.142 -> ZA |
| 72 | `50.7.38.243` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 50.7.38.243 -> SE |
| 73 | `147.45.47.101` | vless | RU | ip-literal | 否 | mmdb 命中 147.45.47.101 -> RU |
| 74 | `kuruish.org` | vless | CA | domain-resolved | 否 | 解析到 66.163.113.9 -> CA |
| 75 | `193.108.119.96` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.96 -> DE |
| 76 | `136.176.68.34` | vless | GB | ip-literal | 否 | mmdb 命中 136.176.68.34 -> GB |
| 77 | `169.40.42.231` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.231 -> DE |
| 78 | `138.124.86.230` | vless | CH | ip-literal | 否 | mmdb 命中 138.124.86.230 -> CH |
| 79 | `187.7.206.179` | vless | DE | ip-literal | 否 | mmdb 命中 187.7.206.179 -> DE |
| 80 | `45.137.201.211` | hysteria2 | IT | ip-literal | 否 | mmdb 命中 45.137.201.211 -> IT |
| 81 | `184.107.179.150` | vless | CA | ip-literal | 否 | mmdb 命中 184.107.179.150 -> CA |
| 82 | `45.63.30.142` | trojan | AU | ip-literal | 否 | mmdb 命中 45.63.30.142 -> AU |
| 83 | `152.228.139.33` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.139.33 -> FR |
| 84 | `144.31.140.125` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.140.125 -> DE |
| 85 | `bl1.nexfile.net` | hysteria2 | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 86 | `66.163.112.13` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.13 -> US |
| 87 | `82.39.171.12` | vless | GB | ip-literal | 否 | mmdb 命中 82.39.171.12 -> GB |
| 88 | `34.24.25.1` | hysteria2 | US | ip-literal | 是 | mmdb 命中 34.24.25.1 -> US |
| 89 | `18.193.79.104` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.193.79.104 -> DE |
| 90 | `51.170.191.10` | vless | NL | ip-literal | 否 | mmdb 命中 51.170.191.10 -> NL |
| 91 | `167.88.61.175` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.175 -> US |
| 92 | `158.247.253.243` | trojan | KR | ip-literal | 否 | mmdb 命中 158.247.253.243 -> KR |
| 93 | `15.235.184.127` | trojan | SG | ip-literal | 否 | mmdb 命中 15.235.184.127 -> SG |
| 94 | `render.com` | vless | US | domain-resolved | 是 | 解析到 216.24.57.1 -> US |
| 95 | `15.204.97.206` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.206 -> US |
| 96 | `138.16.141.59` | vless | NL | ip-literal | 否 | mmdb 命中 138.16.141.59 -> NL |
| 97 | `150.251.112.45` | vless | PL | ip-literal | 否 | mmdb 命中 150.251.112.45 -> PL |
| 98 | `de2.fusetea.ir` | vless | DE | domain-resolved | 否 | 解析到 167.233.40.53 -> DE |
| 99 | `leviko-de3504.shopingggg.ir` | vless | DE | domain-resolved | 否 | 解析到 185.44.64.166 -> DE |
| 100 | `185.44.64.166` | vless | DE | ip-literal | 否 | mmdb 命中 185.44.64.166 -> DE |
| 101 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 102 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 103 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 104 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 105 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 106 | `152.228.162.19` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.162.19 -> FR |
| 107 | `188.42.89.118` | vless | LU | ip-literal | 否 | mmdb 命中 188.42.89.118 -> LU |
| 108 | `192.200.160.42` | vless | US | ip-literal | 是 | mmdb 命中 192.200.160.42 -> US |
| 109 | `185.133.35.86` | vless | BR | ip-literal | 否 | mmdb 命中 185.133.35.86 -> BR |
| 110 | `185.18.250.147` | vless | CH | ip-literal | 否 | mmdb 命中 185.18.250.147 -> CH |
| 111 | `45.135.235.90` | vless | BZ | ip-literal | 否 | mmdb 命中 45.135.235.90 -> BZ |
| 112 | `141.11.203.165` | vless | FR | ip-literal | 否 | mmdb 命中 141.11.203.165 -> FR |
| 113 | `31.6.1.115` | vless | RO | ip-literal | 否 | mmdb 命中 31.6.1.115 -> RO |
| 114 | `114.129.43.105` | vless | NZ | ip-literal | 否 | mmdb 命中 114.129.43.105 -> NZ |
| 115 | `89.116.46.150` | vless | DE | ip-literal | 否 | mmdb 命中 89.116.46.150 -> DE |
| 116 | `31.43.179.196` | vless | KZ | ip-literal | 否 | mmdb 命中 31.43.179.196 -> KZ |
| 117 | `185.86.145.173` | vless | RU | ip-literal | 否 | mmdb 命中 185.86.145.173 -> RU |
| 118 | `orchard.elvano.website` | vless | RU | domain-resolved | 否 | 解析到 201.24.122.189 -> RU |
| 119 | `swo2.nexfile.net` | vless | US | domain-resolved | 是 | 解析到 179.253.80.175 -> US |
| 120 | `193.106.220.103` | vless | AM | ip-literal | 否 | mmdb 命中 193.106.220.103 -> AM |
| 121 | `83.141.91.211` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.91.211 -> IE |
| 122 | `at-40-xckh.wave-inside.online` | vless | AM | domain-resolved | 否 | 解析到 193.106.220.103 -> AM |
| 123 | `fr-41-tapy.wave-inside.online` | vless | IE | domain-resolved | 否 | 解析到 83.141.91.211 -> IE |
| 124 | `193.108.119.29` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.29 -> DE |
| 125 | `200.169.179.233` | vless | RU | ip-literal | 否 | mmdb 命中 200.169.179.233 -> RU |
| 126 | `104.168.109.213` | vless | US | ip-literal | 是 | mmdb 命中 104.168.109.213 -> US |
| 127 | `MARAMBASHI—MARAMBASHI—MARAMBASHI—MARAMBASHI` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 128 | `84.32.108.7` | vless | NL | ip-literal | 否 | mmdb 命中 84.32.108.7 -> NL |
| 129 | `45.88.176.223` | vless | CY | ip-literal | 否 | mmdb 命中 45.88.176.223 -> CY |
| 130 | `193.160.208.240` | vless | RU | ip-literal | 否 | mmdb 命中 193.160.208.240 -> RU |
| 131 | `leviko-pl7089.shopingggg.ir` | vless | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 132 | `179.253.80.175` | vless | US | ip-literal | 是 | mmdb 命中 179.253.80.175 -> US |
| 133 | `bl1.nexfile.net` | vless | US | domain-resolved | 是 | 解析到 179.254.191.251 -> US |
| 134 | `179.254.191.251` | vless | US | ip-literal | 是 | mmdb 命中 179.254.191.251 -> US |
| 135 | `OV-France1.09vpn.com` | vless | FR | domain-resolved | 否 | 解析到 152.228.162.19 -> FR |
| 136 | `5.34.178.120` | vless | US | ip-literal | 是 | mmdb 命中 5.34.178.120 -> US |
| 137 | `216.152.155.158` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.158 -> US |
| 138 | `169.40.42.74` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.74 -> DE |
| 139 | `169.40.42.202` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.202 -> DE |
| 140 | `f0d7aft.nl13.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 48.103.231.82 -> DE |
| 141 | `fre.guren1.me` | hysteria2 | HK | domain-resolved | 否 | 解析到 156.224.78.11 -> HK |
| 142 | `201.34.142.108` | vless | US | ip-literal | 是 | mmdb 命中 201.34.142.108 -> US |
| 143 | `51.158.206.12` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.12 -> NL |
| 144 | `144.31.215.223` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.223 -> DE |
| 145 | `66.23.203.21` | trojan | US | ip-literal | 是 | mmdb 命中 66.23.203.21 -> US |
| 146 | `173.234.15.84` | trojan | SG | ip-literal | 否 | mmdb 命中 173.234.15.84 -> SG |
| 147 | `48.102.218.118` | trojan | US | ip-literal | 是 | mmdb 命中 48.102.218.118 -> US |
| 148 | `216.152.156.42` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.42 -> US |
| 149 | `185.255.115.96` | vless | DE | ip-literal | 否 | mmdb 命中 185.255.115.96 -> DE |
| 150 | `9ed8a8t.se4.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 185.255.115.169 -> DE |
| 151 | `217.60.94.115` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.94.115 -> DE |
| 152 | `178.172.227.228` | vless | BY | ip-literal | 否 | mmdb 命中 178.172.227.228 -> BY |
| 153 | `51.158.206.86` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.86 -> NL |
| 154 | `94.183.164.119` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 155 | `47.242.93.89` | trojan | HK | ip-literal | 否 | mmdb 命中 47.242.93.89 -> HK |
| 156 | `154.90.62.70` | trojan | KR | ip-literal | 否 | mmdb 命中 154.90.62.70 -> KR |
| 157 | `matrix.phonicsindia.mobi` | trojan | SG | domain-resolved | 否 | 解析到 173.234.15.84 -> SG |
| 158 | `206.189.229.48` | hysteria2 | US | ip-literal | 是 | mmdb 命中 206.189.229.48 -> US |
| 159 | `47.89.232.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 47.89.232.46 -> US |
| 160 | `212.34.137.105` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 212.34.137.105 -> NL |
| 161 | `13.36.234.11` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 13.36.234.11 -> FR |
| 162 | `5.129.235.85` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 5.129.235.85 -> NL |
| 163 | `18.153.65.67` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.153.65.67 -> DE |
| 164 | `3.76.203.180` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.203.180 -> DE |
| 165 | `18.194.242.173` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 18.194.242.173 -> DE |
| 166 | `3.69.232.199` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.69.232.199 -> DE |
| 167 | `152.67.75.161` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 152.67.75.161 -> CH |
| 168 | `82.40.63.138` | hysteria2 | PL | ip-literal | 否 | mmdb 命中 82.40.63.138 -> PL |
| 169 | `3.76.221.4` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.76.221.4 -> DE |
| 170 | `87.121.112.83` | hysteria2 | BG | ip-literal | 否 | mmdb 命中 87.121.112.83 -> BG |
| 171 | `35.221.91.82` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 35.221.91.82 -> JP |
| 172 | `66.94.121.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 66.94.121.46 -> US |
| 173 | `vpn-43-165-180-220.sslip.io` | hysteria2 | JP | domain-resolved | 否 | 解析到 43.165.180.220 -> JP |
| 174 | `8.209.247.109` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.209.247.109 -> JP |
| 175 | `34.64.134.170` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 34.64.134.170 -> KR |
| 176 | `8.211.175.236` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 8.211.175.236 -> JP |
| 177 | `51.15.19.206` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 51.15.19.206 -> NL |
| 178 | `160.187.100.109` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 160.187.100.109 -> TW |
| 179 | `vpn-tw-002.fastervpn.world` | hysteria2 | TW | domain-resolved | 否 | 解析到 160.187.100.109 -> TW |
| 180 | `152.70.237.123` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.70.237.123 -> KR |
| 181 | `54.179.113.70` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 54.179.113.70 -> SG |
| 182 | `13.212.78.215` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 13.212.78.215 -> SG |
| 183 | `176.108.240.182` | hysteria2 | RU | ip-literal | 否 | mmdb 命中 176.108.240.182 -> RU |
| 184 | `152.67.115.203` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 152.67.115.203 -> AU |
| 185 | `47.129.241.99` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 47.129.241.99 -> SG |
| 186 | `202.146.222.29` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.29 -> HK |
| 187 | `202.146.222.89` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.89 -> HK |
| 188 | `202.146.222.174` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 202.146.222.174 -> HK |
| 189 | `vpn-hk-004.fastervpn.world` | hysteria2 | US | domain-resolved | 是 | 解析到 192.253.229.199 -> US |
| 190 | `129.225.181.46` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 129.225.181.46 -> JP |
| 191 | `vpn-sg-001.fastervpn.world` | hysteria2 | SG | domain-resolved | 否 | 解析到 13.212.58.68 -> SG |
| 192 | `hysteria.udpgw.com` | hysteria2 | NL | domain-resolved | 否 | 解析到 51.15.19.206 -> NL |
| 193 | `24.233.8.109` | hysteria2 | US | ip-literal | 是 | mmdb 命中 24.233.8.109 -> US |
| 194 | `193.108.119.15` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.15 -> DE |
| 195 | `94.183.164.119` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 196 | `69.164.240.85` | trojan | US | ip-literal | 是 | mmdb 命中 69.164.240.85 -> US |
| 197 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 198 | `cb8b18x.es15.h1clayd.shop` | vless | EE | domain-resolved | 否 | 解析到 143.246.41.199 -> EE |
| 199 | `164.37.224.246` | vless | NL | ip-literal | 否 | mmdb 命中 164.37.224.246 -> NL |
| 200 | `132.243.67.137` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.67.137 -> EE |
| 201 | `216.219.92.130` | vless | US | ip-literal | 是 | mmdb 命中 216.219.92.130 -> US |
| 202 | `91.107.191.188` | vless | DE | ip-literal | 否 | mmdb 命中 91.107.191.188 -> DE |
| 203 | `kala.bestsellers1.site` | vless | DE | domain-resolved | 否 | 解析到 91.107.191.188 -> DE |
| 204 | `monte.quantumveritas.monster` | vless | - | unknown | 否 | DNS 解析失败或超时 |
| 205 | `maple.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 206 | `birch.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 207 | `willow.kryonix.space` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 208 | `nep.cryptoventura.online` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 209 | `chcdn.fius.dev` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 210 | `104.18.138.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.138.67 -> US |
| 211 | `104.18.141.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.141.67 -> US |
| 212 | `104.18.140.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.140.67 -> US |
| 213 | `104.18.137.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.137.67 -> US |
| 214 | `104.18.139.67` | vless | US | ip-literal | 是 | mmdb 命中 104.18.139.67 -> US |
| 215 | `193.108.119.134` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.134 -> DE |
| 216 | `94.182.134.170` | vless | IR | ip-literal | 否 | mmdb 命中 94.182.134.170 -> IR |
| 217 | `food.ebaniyautist.com` | vless | RU | domain-resolved | 否 | 解析到 194.55.239.10 -> RU |
| 218 | `38.76.150.108` | hysteria2 | US | ip-literal | 是 | mmdb 命中 38.76.150.108 -> US |
| 219 | `142.249.78.7` | hysteria2 | US | ip-literal | 是 | mmdb 命中 142.249.78.7 -> US |
| 220 | `62.210.7.139` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.7.139 -> FR |
| 221 | `62.210.124.146` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.124.146 -> FR |
| 222 | `62.210.147.2` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.147.2 -> FR |
| 223 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 224 | `140.238.213.114` | hysteria2 | CH | ip-literal | 否 | mmdb 命中 140.238.213.114 -> CH |
| 225 | `91.108.247.47` | hysteria2 | GB | ip-literal | 否 | mmdb 命中 91.108.247.47 -> GB |
| 226 | `129.159.156.109` | hysteria2 | IL | ip-literal | 否 | mmdb 命中 129.159.156.109 -> IL |
| 227 | `150-230-252-217.liao.kdns.fr` | hysteria2 | KR | domain-resolved | 否 | 解析到 150.230.252.217 -> KR |
| 228 | `132.226.226.189` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 132.226.226.189 -> KR |
| 229 | `152.69.231.175` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.69.231.175 -> KR |
| 230 | `152-69-231-175.liao.kdns.fr` | hysteria2 | KR | domain-resolved | 否 | 解析到 152.69.231.175 -> KR |
| 231 | `152.67.200.82` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 152.67.200.82 -> KR |
| 232 | `13.55.52.44` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 13.55.52.44 -> AU |
| 233 | `138.2.73.238` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.73.238 -> SG |
| 234 | `31.57.248.176` | hysteria2 | HK | ip-literal | 否 | mmdb 命中 31.57.248.176 -> HK |
| 235 | `137.175.82.43` | hysteria | US | ip-literal | 是 | mmdb 命中 137.175.82.43 -> US |
| 236 | `tun2.minoosell.ir` | vless | PL | domain-resolved | 否 | 解析到 45.144.49.138 -> PL |
| 237 | `45.144.49.138` | vless | PL | ip-literal | 否 | mmdb 命中 45.144.49.138 -> PL |
| 238 | `5.83.129.90` | hysteria | DE | ip-literal | 否 | mmdb 命中 5.83.129.90 -> DE |
| 239 | `38.180.206.44` | vless | KZ | ip-literal | 否 | mmdb 命中 38.180.206.44 -> KZ |
| 240 | `185.210.155.38` | vless | ES | ip-literal | 否 | mmdb 命中 185.210.155.38 -> ES |
| 241 | `trips.blog-forme.ru` | vless | CZ | domain-resolved | 否 | 解析到 95.85.232.83 -> CZ |
| 242 | `217.60.27.93` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.93 -> DE |
| 243 | `95.163.153.141` | vless | AT | ip-literal | 否 | mmdb 命中 95.163.153.141 -> AT |
| 244 | `185.248.141.233` | vless | DE | ip-literal | 否 | mmdb 命中 185.248.141.233 -> DE |
| 245 | `94.183.164.96` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.96 -> NL |
| 246 | `5.78.51.198` | vless | US | ip-literal | 是 | mmdb 命中 5.78.51.198 -> US |
| 247 | `94.183.164.119` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 248 | `143.246.211.240` | vless | FR | ip-literal | 否 | mmdb 命中 143.246.211.240 -> FR |
| 249 | `79.182.70.190` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.190 -> NL |
| 250 | `summit.blog-forme.ru` | vless | CZ | domain-resolved | 否 | 解析到 95.85.231.3 -> CZ |
| 251 | `guide.blog-forme.ru` | vless | CZ | domain-resolved | 否 | 解析到 95.85.231.3 -> CZ |
| 252 | `95.85.231.3` | vless | CZ | ip-literal | 否 | mmdb 命中 95.85.231.3 -> CZ |
| 253 | `153.80.206.130` | vless | KZ | ip-literal | 否 | mmdb 命中 153.80.206.130 -> KZ |
| 254 | `9.247.54.228` | vless | NL | ip-literal | 否 | mmdb 命中 9.247.54.228 -> NL |
| 255 | `slot3.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.253.106 -> DE |
| 256 | `132.243.67.228` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.67.228 -> EE |
| 257 | `slot6.ipoxxo.online` | vless | FI | domain-resolved | 否 | 解析到 65.109.212.49 -> FI |
| 258 | `196.245.52.187` | vless | SC | ip-literal | 否 | mmdb 命中 196.245.52.187 -> SC |
| 259 | `136.148.83.132` | vless | RU | ip-literal | 否 | mmdb 命中 136.148.83.132 -> RU |
| 260 | `164.37.224.51` | vless | NL | ip-literal | 否 | mmdb 命中 164.37.224.51 -> NL |
| 261 | `196.245.52.183` | vless | SC | ip-literal | 否 | mmdb 命中 196.245.52.183 -> SC |
| 262 | `0ef47cx.se4.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 185.255.115.169 -> DE |
| 263 | `144.31.215.244` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.244 -> DE |
| 264 | `172.67.67.89` | vless | US | ip-literal | 是 | mmdb 命中 172.67.67.89 -> US |
| 265 | `162.159.237.118` | vless | US | ip-literal | 是 | mmdb 命中 162.159.237.118 -> US |
| 266 | `162.159.160.117` | vless | US | ip-literal | 是 | mmdb 命中 162.159.160.117 -> US |
| 267 | `104.18.63.135` | vless | US | ip-literal | 是 | mmdb 命中 104.18.63.135 -> US |
| 268 | `104.17.145.145` | vless | US | ip-literal | 是 | mmdb 命中 104.17.145.145 -> US |
| 269 | `62.210.24.143` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.24.143 -> FR |
| 270 | `62.210.70.194` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.70.194 -> FR |
| 271 | `132.243.163.114` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.114 -> GB |
| 272 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 273 | `217.60.27.93` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.93 -> DE |
| 274 | `85.208.69.43` | vless | CH | ip-literal | 否 | mmdb 命中 85.208.69.43 -> CH |
| 275 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 276 | `201.58.139.254` | vless | PL | ip-literal | 否 | mmdb 命中 201.58.139.254 -> PL |
| 277 | `31.77.144.255` | vless | SE | ip-literal | 否 | mmdb 命中 31.77.144.255 -> SE |
| 278 | `93.183.127.54` | vless | NL | ip-literal | 否 | mmdb 命中 93.183.127.54 -> NL |
| 279 | `13.143.239.236` | vless | EE | ip-literal | 否 | mmdb 命中 13.143.239.236 -> EE |
| 280 | `us12.h1cloud.net` | vless | DE | domain-resolved | 否 | 解析到 153.56.230.77 -> DE |
| 281 | `pl9.h1cloud.net` | vless | NL | domain-resolved | 否 | 解析到 195.206.235.216 -> NL |
| 282 | `13.141.51.100` | vless | NL | ip-literal | 否 | mmdb 命中 13.141.51.100 -> NL |
| 283 | `162.35.38.156` | vless | US | ip-literal | 是 | mmdb 命中 162.35.38.156 -> US |
| 284 | `94.241.172.107` | vless | GR | ip-literal | 否 | mmdb 命中 94.241.172.107 -> GR |
| 285 | `51.158.206.98` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.98 -> NL |
| 286 | `154.197.64.252` | vless | SC | ip-literal | 否 | mmdb 命中 154.197.64.252 -> SC |
| 287 | `138.2.89.249` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 138.2.89.249 -> SG |
| 288 | `64.176.7.205` | trojan | CL | ip-literal | 否 | mmdb 命中 64.176.7.205 -> CL |
| 289 | `95.85.231.3` | hysteria2 | CZ | ip-literal | 否 | mmdb 命中 95.85.231.3 -> CZ |
| 290 | `193.233.198.117` | vless | DE | ip-literal | 否 | mmdb 命中 193.233.198.117 -> DE |
| 291 | `87.199.205.28` | vless | NL | ip-literal | 否 | mmdb 命中 87.199.205.28 -> NL |
| 292 | `51.158.206.103` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.103 -> NL |
| 293 | `OV-Germany1.09vpn.com` | vless | DE | domain-resolved | 否 | 解析到 57.129.41.216 -> DE |
| 294 | `94.183.164.119` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 295 | `13.219.53.87` | vless | US | ip-literal | 是 | mmdb 命中 13.219.53.87 -> US |
| 296 | `108.132.46.58` | vless | IE | ip-literal | 否 | mmdb 命中 108.132.46.58 -> IE |
| 297 | `108.128.70.192` | vless | IE | ip-literal | 否 | mmdb 命中 108.128.70.192 -> IE |
| 298 | `99.80.74.18` | vless | IE | ip-literal | 否 | mmdb 命中 99.80.74.18 -> IE |
| 299 | `34.249.113.229` | vless | IE | ip-literal | 否 | mmdb 命中 34.249.113.229 -> IE |
| 300 | `108.131.131.21` | vless | IE | ip-literal | 否 | mmdb 命中 108.131.131.21 -> IE |
| 301 | `54.72.196.211` | vless | IE | ip-literal | 否 | mmdb 命中 54.72.196.211 -> IE |
| 302 | `34.248.195.6` | vless | IE | ip-literal | 否 | mmdb 命中 34.248.195.6 -> IE |
| 303 | `3.254.228.253` | vless | IE | ip-literal | 否 | mmdb 命中 3.254.228.253 -> IE |
| 304 | `51.200.58.31` | vless | GB | ip-literal | 否 | mmdb 命中 51.200.58.31 -> GB |
| 305 | `54.246.157.211` | vless | IE | ip-literal | 否 | mmdb 命中 54.246.157.211 -> IE |
| 306 | `18.132.14.113` | vless | GB | ip-literal | 否 | mmdb 命中 18.132.14.113 -> GB |
| 307 | `18.168.17.115` | vless | GB | ip-literal | 否 | mmdb 命中 18.168.17.115 -> GB |
| 308 | `167.99.205.185` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.205.185 -> GB |
| 309 | `178.62.56.43` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.56.43 -> GB |
| 310 | `178.62.9.48` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.9.48 -> GB |
| 311 | `46.101.2.155` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.2.155 -> GB |
| 312 | `134.209.27.89` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.27.89 -> GB |
| 313 | `165.22.125.106` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.125.106 -> GB |
| 314 | `165.232.46.76` | vless | GB | ip-literal | 否 | mmdb 命中 165.232.46.76 -> GB |
| 315 | `178.128.35.8` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.35.8 -> GB |
| 316 | `178.62.21.44` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.21.44 -> GB |
| 317 | `188.166.147.118` | vless | GB | ip-literal | 否 | mmdb 命中 188.166.147.118 -> GB |
| 318 | `206.189.125.47` | vless | GB | ip-literal | 否 | mmdb 命中 206.189.125.47 -> GB |
| 319 | `46.101.0.247` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.0.247 -> GB |
| 320 | `46.101.78.246` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.78.246 -> GB |
| 321 | `104.248.166.106` | vless | GB | ip-literal | 否 | mmdb 命中 104.248.166.106 -> GB |
| 322 | `138.68.144.90` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.144.90 -> GB |
| 323 | `165.22.124.21` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.124.21 -> GB |
| 324 | `167.99.84.88` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.84.88 -> GB |
| 325 | `167.99.87.123` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.87.123 -> GB |
| 326 | `178.128.32.127` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.32.127 -> GB |
| 327 | `178.62.111.230` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.111.230 -> GB |
| 328 | `178.62.20.40` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.20.40 -> GB |
| 329 | `178.62.23.182` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.23.182 -> GB |
| 330 | `178.62.48.15` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.48.15 -> GB |
| 331 | `206.189.124.131` | vless | GB | ip-literal | 否 | mmdb 命中 206.189.124.131 -> GB |
| 332 | `138.68.133.126` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.133.126 -> GB |
| 333 | `138.68.160.82` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.160.82 -> GB |
| 334 | `15.224.228.143` | vless | FR | ip-literal | 否 | mmdb 命中 15.224.228.143 -> FR |
| 335 | `159.65.57.104` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.57.104 -> GB |
| 336 | `165.22.113.42` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.113.42 -> GB |
| 337 | `178.128.175.210` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.175.210 -> GB |
| 338 | `178.62.103.139` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.103.139 -> GB |
| 339 | `209.97.131.199` | vless | GB | ip-literal | 否 | mmdb 命中 209.97.131.199 -> GB |
| 340 | `104.248.161.70` | vless | GB | ip-literal | 否 | mmdb 命中 104.248.161.70 -> GB |
| 341 | `134.209.22.71` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.22.71 -> GB |
| 342 | `138.68.145.16` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.145.16 -> GB |
| 343 | `138.68.145.254` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.145.254 -> GB |
| 344 | `144.126.194.91` | vless | GB | ip-literal | 否 | mmdb 命中 144.126.194.91 -> GB |
| 345 | `157.245.39.214` | vless | GB | ip-literal | 否 | mmdb 命中 157.245.39.214 -> GB |
| 346 | `165.22.120.20` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.120.20 -> GB |
| 347 | `167.99.203.60` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.203.60 -> GB |
| 348 | `178.62.44.92` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.44.92 -> GB |
| 349 | `178.62.77.199` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.77.199 -> GB |
| 350 | `178.62.78.16` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.78.16 -> GB |
| 351 | `178.62.84.236` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.84.236 -> GB |
| 352 | `46.101.32.31` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.32.31 -> GB |
| 353 | `46.101.77.161` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.77.161 -> GB |
| 354 | `139.59.164.30` | vless | GB | ip-literal | 否 | mmdb 命中 139.59.164.30 -> GB |
| 355 | `159.65.57.52` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.57.52 -> GB |
| 356 | `167.172.61.186` | vless | GB | ip-literal | 否 | mmdb 命中 167.172.61.186 -> GB |
| 357 | `167.99.194.3` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.194.3 -> GB |
| 358 | `178.62.110.142` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.110.142 -> GB |
| 359 | `178.62.117.200` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.117.200 -> GB |
| 360 | `46.101.56.175` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.56.175 -> GB |
| 361 | `46.101.61.103` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.61.103 -> GB |
| 362 | `138.68.165.114` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.165.114 -> GB |
| 363 | `165.22.120.187` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.120.187 -> GB |
| 364 | `165.232.32.247` | vless | GB | ip-literal | 否 | mmdb 命中 165.232.32.247 -> GB |
| 365 | `167.99.91.114` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.91.114 -> GB |
| 366 | `178.128.41.216` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.41.216 -> GB |
| 367 | `178.62.112.73` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.112.73 -> GB |
| 368 | `188.166.145.184` | vless | GB | ip-literal | 否 | mmdb 命中 188.166.145.184 -> GB |
| 369 | `46.101.39.122` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.39.122 -> GB |
| 370 | `46.101.72.167` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.72.167 -> GB |
| 371 | `64.227.44.70` | vless | GB | ip-literal | 否 | mmdb 命中 64.227.44.70 -> GB |
| 372 | `159.65.21.125` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.21.125 -> GB |
| 373 | `178.62.113.211` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.113.211 -> GB |
| 374 | `178.62.119.166` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.119.166 -> GB |
| 375 | `178.62.33.169` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.33.169 -> GB |
| 376 | `46.101.76.217` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.76.217 -> GB |
| 377 | `46.101.86.20` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.86.20 -> GB |
| 378 | `46.101.90.127` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.90.127 -> GB |
| 379 | `138.68.131.114` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.131.114 -> GB |
| 380 | `142.93.47.134` | vless | GB | ip-literal | 否 | mmdb 命中 142.93.47.134 -> GB |
| 381 | `167.172.62.145` | vless | GB | ip-literal | 否 | mmdb 命中 167.172.62.145 -> GB |
| 382 | `178.62.71.46` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.71.46 -> GB |
| 383 | `188.166.168.96` | vless | GB | ip-literal | 否 | mmdb 命中 188.166.168.96 -> GB |
| 384 | `209.97.178.204` | vless | GB | ip-literal | 否 | mmdb 命中 209.97.178.204 -> GB |
| 385 | `46.101.41.222` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.41.222 -> GB |
| 386 | `104.248.163.126` | vless | GB | ip-literal | 否 | mmdb 命中 104.248.163.126 -> GB |
| 387 | `134.209.25.239` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.25.239 -> GB |
| 388 | `165.227.239.130` | vless | GB | ip-literal | 否 | mmdb 命中 165.227.239.130 -> GB |
| 389 | `178.128.46.52` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.46.52 -> GB |
| 390 | `142.93.239.171` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.239.171 -> NL |
| 391 | `161.35.35.0` | vless | GB | ip-literal | 否 | mmdb 命中 161.35.35.0 -> GB |
| 392 | `165.227.225.34` | vless | GB | ip-literal | 否 | mmdb 命中 165.227.225.34 -> GB |
| 393 | `18.170.218.17` | vless | GB | ip-literal | 否 | mmdb 命中 18.170.218.17 -> GB |
| 394 | `46.101.53.170` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.53.170 -> GB |
| 395 | `46.101.72.212` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.72.212 -> GB |
| 396 | `152.42.132.250` | vless | NL | ip-literal | 否 | mmdb 命中 152.42.132.250 -> NL |
| 397 | `159.65.18.205` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.18.205 -> GB |
| 398 | `159.65.92.52` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.92.52 -> GB |
| 399 | `188.166.172.177` | vless | GB | ip-literal | 否 | mmdb 命中 188.166.172.177 -> GB |
| 400 | `64.225.66.46` | vless | NL | ip-literal | 否 | mmdb 命中 64.225.66.46 -> NL |
| 401 | `139.59.186.154` | vless | GB | ip-literal | 否 | mmdb 命中 139.59.186.154 -> GB |
| 402 | `157.245.37.123` | vless | GB | ip-literal | 否 | mmdb 命中 157.245.37.123 -> GB |
| 403 | `165.22.202.108` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.202.108 -> NL |
| 404 | `178.62.107.51` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.107.51 -> GB |
| 405 | `178.62.5.242` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.5.242 -> GB |
| 406 | `46.101.5.217` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.5.217 -> GB |
| 407 | `138.68.173.114` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.173.114 -> GB |
| 408 | `143.110.171.7` | vless | GB | ip-literal | 否 | mmdb 命中 143.110.171.7 -> GB |
| 409 | `157.245.32.47` | vless | GB | ip-literal | 否 | mmdb 命中 157.245.32.47 -> GB |
| 410 | `159.65.28.182` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.28.182 -> GB |
| 411 | `159.65.53.22` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.53.22 -> GB |
| 412 | `178.62.116.50` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.116.50 -> GB |
| 413 | `178.62.38.28` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.38.28 -> GB |
| 414 | `178.62.9.51` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.9.51 -> GB |
| 415 | `142.93.32.80` | vless | GB | ip-literal | 否 | mmdb 命中 142.93.32.80 -> GB |
| 416 | `144.126.235.32` | vless | GB | ip-literal | 否 | mmdb 命中 144.126.235.32 -> GB |
| 417 | `159.65.29.123` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.29.123 -> GB |
| 418 | `167.71.139.180` | vless | GB | ip-literal | 否 | mmdb 命中 167.71.139.180 -> GB |
| 419 | `167.99.206.217` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.206.217 -> GB |
| 420 | `178.62.219.174` | vless | NL | ip-literal | 否 | mmdb 命中 178.62.219.174 -> NL |
| 421 | `178.62.240.6` | vless | NL | ip-literal | 否 | mmdb 命中 178.62.240.6 -> NL |
| 422 | `188.166.101.67` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.101.67 -> NL |
| 423 | `209.38.165.75` | vless | GB | ip-literal | 否 | mmdb 命中 209.38.165.75 -> GB |
| 424 | `104.248.161.164` | vless | GB | ip-literal | 否 | mmdb 命中 104.248.161.164 -> GB |
| 425 | `138.68.143.226` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.143.226 -> GB |
| 426 | `146.190.26.193` | vless | NL | ip-literal | 否 | mmdb 命中 146.190.26.193 -> NL |
| 427 | `159.223.234.56` | vless | NL | ip-literal | 否 | mmdb 命中 159.223.234.56 -> NL |
| 428 | `159.65.49.180` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.49.180 -> GB |
| 429 | `178.62.115.66` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.115.66 -> GB |
| 430 | `178.62.59.189` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.59.189 -> GB |
| 431 | `178.62.98.100` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.98.100 -> GB |
| 432 | `188.166.14.157` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.14.157 -> NL |
| 433 | `188.166.42.100` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.42.100 -> NL |
| 434 | `46.101.57.7` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.57.7 -> GB |
| 435 | `134.209.88.96` | vless | NL | ip-literal | 否 | mmdb 命中 134.209.88.96 -> NL |
| 436 | `159.223.238.143` | vless | NL | ip-literal | 否 | mmdb 命中 159.223.238.143 -> NL |
| 437 | `63.182.53.195` | vless | DE | ip-literal | 否 | mmdb 命中 63.182.53.195 -> DE |
| 438 | `139.59.176.166` | vless | GB | ip-literal | 否 | mmdb 命中 139.59.176.166 -> GB |
| 439 | `46.101.3.34` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.3.34 -> GB |
| 440 | `157.245.75.182` | vless | NL | ip-literal | 否 | mmdb 命中 157.245.75.182 -> NL |
| 441 | `178.62.113.49` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.113.49 -> GB |
| 442 | `142.93.231.102` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.231.102 -> NL |
| 443 | `142.93.233.27` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.233.27 -> NL |
| 444 | `164.92.212.196` | vless | NL | ip-literal | 否 | mmdb 命中 164.92.212.196 -> NL |
| 445 | `68.183.4.148` | vless | NL | ip-literal | 否 | mmdb 命中 68.183.4.148 -> NL |
| 446 | `152.42.139.237` | vless | NL | ip-literal | 否 | mmdb 命中 152.42.139.237 -> NL |
| 447 | `159.223.238.109` | vless | NL | ip-literal | 否 | mmdb 命中 159.223.238.109 -> NL |
| 448 | `165.22.193.187` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.193.187 -> NL |
| 449 | `167.99.203.248` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.203.248 -> GB |
| 450 | `178.62.8.40` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.8.40 -> GB |
| 451 | `209.38.47.105` | vless | NL | ip-literal | 否 | mmdb 命中 209.38.47.105 -> NL |
| 452 | `143.110.169.131` | vless | GB | ip-literal | 否 | mmdb 命中 143.110.169.131 -> GB |
| 453 | `165.232.95.11` | vless | NL | ip-literal | 否 | mmdb 命中 165.232.95.11 -> NL |
| 454 | `64.225.72.144` | vless | NL | ip-literal | 否 | mmdb 命中 64.225.72.144 -> NL |
| 455 | `138.68.153.227` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.153.227 -> GB |
| 456 | `139.59.152.166` | vless | DE | ip-literal | 否 | mmdb 命中 139.59.152.166 -> DE |
| 457 | `159.65.201.57` | vless | NL | ip-literal | 否 | mmdb 命中 159.65.201.57 -> NL |
| 458 | `167.99.205.29` | vless | GB | ip-literal | 否 | mmdb 命中 167.99.205.29 -> GB |
| 459 | `46.101.58.123` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.58.123 -> GB |
| 460 | `46.101.31.162` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.31.162 -> GB |
| 461 | `68.183.42.150` | vless | GB | ip-literal | 否 | mmdb 命中 68.183.42.150 -> GB |
| 462 | `142.93.236.138` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.236.138 -> NL |
| 463 | `165.232.91.75` | vless | NL | ip-literal | 否 | mmdb 命中 165.232.91.75 -> NL |
| 464 | `167.172.35.64` | vless | NL | ip-literal | 否 | mmdb 命中 167.172.35.64 -> NL |
| 465 | `167.172.45.208` | vless | NL | ip-literal | 否 | mmdb 命中 167.172.45.208 -> NL |
| 466 | `178.128.243.145` | vless | NL | ip-literal | 否 | mmdb 命中 178.128.243.145 -> NL |
| 467 | `178.128.36.72` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.36.72 -> GB |
| 468 | `138.68.169.0` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.169.0 -> GB |
| 469 | `165.22.194.136` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.194.136 -> NL |
| 470 | `167.99.39.190` | vless | NL | ip-literal | 否 | mmdb 命中 167.99.39.190 -> NL |
| 471 | `188.166.118.243` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.118.243 -> NL |
| 472 | `46.101.0.105` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.0.105 -> GB |
| 473 | `161.35.92.133` | vless | NL | ip-literal | 否 | mmdb 命中 161.35.92.133 -> NL |
| 474 | `207.154.221.24` | vless | DE | ip-literal | 否 | mmdb 命中 207.154.221.24 -> DE |
| 475 | `46.101.2.240` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.2.240 -> GB |
| 476 | `142.93.44.5` | vless | GB | ip-literal | 否 | mmdb 命中 142.93.44.5 -> GB |
| 477 | `159.223.234.178` | vless | NL | ip-literal | 否 | mmdb 命中 159.223.234.178 -> NL |
| 478 | `178.62.33.43` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.33.43 -> GB |
| 479 | `188.166.120.52` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.120.52 -> NL |
| 480 | `138.68.128.148` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.128.148 -> GB |
| 481 | `167.71.7.55` | vless | NL | ip-literal | 否 | mmdb 命中 167.71.7.55 -> NL |
| 482 | `46.101.47.23` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.47.23 -> GB |
| 483 | `165.22.116.245` | vless | GB | ip-literal | 否 | mmdb 命中 165.22.116.245 -> GB |
| 484 | `178.128.174.27` | vless | GB | ip-literal | 否 | mmdb 命中 178.128.174.27 -> GB |
| 485 | `188.166.70.24` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.70.24 -> NL |
| 486 | `104.248.201.63` | vless | NL | ip-literal | 否 | mmdb 命中 104.248.201.63 -> NL |
| 487 | `159.65.16.87` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.16.87 -> GB |
| 488 | `134.209.28.80` | vless | GB | ip-literal | 否 | mmdb 命中 134.209.28.80 -> GB |
| 489 | `157.245.77.100` | vless | NL | ip-literal | 否 | mmdb 命中 157.245.77.100 -> NL |
| 490 | `157.245.39.223` | vless | GB | ip-literal | 否 | mmdb 命中 157.245.39.223 -> GB |
| 491 | `164.90.198.246` | vless | NL | ip-literal | 否 | mmdb 命中 164.90.198.246 -> NL |
| 492 | `165.22.195.202` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.195.202 -> NL |
| 493 | `165.22.198.215` | vless | NL | ip-literal | 否 | mmdb 命中 165.22.198.215 -> NL |
| 494 | `167.172.57.125` | vless | GB | ip-literal | 否 | mmdb 命中 167.172.57.125 -> GB |
| 495 | `188.166.63.71` | vless | NL | ip-literal | 否 | mmdb 命中 188.166.63.71 -> NL |
| 496 | `164.92.150.92` | vless | NL | ip-literal | 否 | mmdb 命中 164.92.150.92 -> NL |
| 497 | `46.101.19.198` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.19.198 -> GB |
| 498 | `64.226.66.216` | vless | DE | ip-literal | 否 | mmdb 命中 64.226.66.216 -> DE |
| 499 | `146.190.16.218` | vless | NL | ip-literal | 否 | mmdb 命中 146.190.16.218 -> NL |
| 500 | `178.62.117.126` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.117.126 -> GB |
| 501 | `51.24.49.169` | vless | GB | ip-literal | 否 | mmdb 命中 51.24.49.169 -> GB |
| 502 | `15.237.191.96` | vless | FR | ip-literal | 否 | mmdb 命中 15.237.191.96 -> FR |
| 503 | `178.62.245.167` | vless | NL | ip-literal | 否 | mmdb 命中 178.62.245.167 -> NL |
| 504 | `142.93.40.71` | vless | GB | ip-literal | 否 | mmdb 命中 142.93.40.71 -> GB |
| 505 | `138.68.128.76` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.128.76 -> GB |
| 506 | `3.64.11.204` | vless | DE | ip-literal | 否 | mmdb 命中 3.64.11.204 -> DE |
| 507 | `68.183.36.183` | vless | GB | ip-literal | 否 | mmdb 命中 68.183.36.183 -> GB |
| 508 | `18.169.216.210` | vless | GB | ip-literal | 否 | mmdb 命中 18.169.216.210 -> GB |
| 509 | `146.190.227.8` | vless | NL | ip-literal | 否 | mmdb 命中 146.190.227.8 -> NL |
| 510 | `46.101.8.97` | vless | GB | ip-literal | 否 | mmdb 命中 46.101.8.97 -> GB |
| 511 | `178.62.212.162` | vless | NL | ip-literal | 否 | mmdb 命中 178.62.212.162 -> NL |
| 512 | `134.209.200.187` | vless | NL | ip-literal | 否 | mmdb 命中 134.209.200.187 -> NL |
| 513 | `134.122.51.229` | vless | NL | ip-literal | 否 | mmdb 命中 134.122.51.229 -> NL |
| 514 | `138.68.159.143` | vless | GB | ip-literal | 否 | mmdb 命中 138.68.159.143 -> GB |
| 515 | `165.232.86.202` | vless | NL | ip-literal | 否 | mmdb 命中 165.232.86.202 -> NL |
| 516 | `3.71.101.64` | vless | DE | ip-literal | 否 | mmdb 命中 3.71.101.64 -> DE |
| 517 | `13.48.162.22` | vless | SE | ip-literal | 否 | mmdb 命中 13.48.162.22 -> SE |
| 518 | `3.69.66.115` | vless | DE | ip-literal | 否 | mmdb 命中 3.69.66.115 -> DE |
| 519 | `3.72.62.187` | vless | DE | ip-literal | 否 | mmdb 命中 3.72.62.187 -> DE |
| 520 | `142.93.234.114` | vless | NL | ip-literal | 否 | mmdb 命中 142.93.234.114 -> NL |
| 521 | `51.45.67.180` | vless | FR | ip-literal | 否 | mmdb 命中 51.45.67.180 -> FR |
| 522 | `18.153.206.195` | vless | DE | ip-literal | 否 | mmdb 命中 18.153.206.195 -> DE |
| 523 | `18.196.13.36` | vless | DE | ip-literal | 否 | mmdb 命中 18.196.13.36 -> DE |
| 524 | `165.227.230.41` | vless | GB | ip-literal | 否 | mmdb 命中 165.227.230.41 -> GB |
| 525 | `51.20.83.55` | vless | SE | ip-literal | 否 | mmdb 命中 51.20.83.55 -> SE |
| 526 | `18.200.147.246` | vless | IE | ip-literal | 否 | mmdb 命中 18.200.147.246 -> IE |
| 527 | `170.64.214.132` | vless | AU | ip-literal | 否 | mmdb 命中 170.64.214.132 -> AU |
| 528 | `52.47.107.91` | vless | FR | ip-literal | 否 | mmdb 命中 52.47.107.91 -> FR |
| 529 | `168.144.174.238` | vless | AU | ip-literal | 否 | mmdb 命中 168.144.174.238 -> AU |
| 530 | `170.64.175.121` | vless | AU | ip-literal | 否 | mmdb 命中 170.64.175.121 -> AU |
| 531 | `209.38.30.56` | vless | AU | ip-literal | 否 | mmdb 命中 209.38.30.56 -> AU |
| 532 | `209.97.177.173` | vless | GB | ip-literal | 否 | mmdb 命中 209.97.177.173 -> GB |
| 533 | `35.156.27.93` | vless | DE | ip-literal | 否 | mmdb 命中 35.156.27.93 -> DE |
| 534 | `178.62.84.65` | vless | GB | ip-literal | 否 | mmdb 命中 178.62.84.65 -> GB |
| 535 | `165.232.107.165` | vless | GB | ip-literal | 否 | mmdb 命中 165.232.107.165 -> GB |
| 536 | `13.37.4.113` | vless | FR | ip-literal | 否 | mmdb 命中 13.37.4.113 -> FR |
| 537 | `35.180.214.137` | vless | FR | ip-literal | 否 | mmdb 命中 35.180.214.137 -> FR |
| 538 | `51.158.206.8` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.8 -> NL |
| 539 | `user.betust.net` | vless | US | domain-resolved | 是 | 解析到 50.7.169.243 -> US |
| 540 | `185.112.59.157` | vless | NL | ip-literal | 否 | mmdb 命中 185.112.59.157 -> NL |
| 541 | `31.57.185.176` | vless | US | ip-literal | 是 | mmdb 命中 31.57.185.176 -> US |
| 542 | `195.123.245.241` | vless | CZ | ip-literal | 否 | mmdb 命中 195.123.245.241 -> CZ |
| 543 | `185.176.9.26` | vless | ES | ip-literal | 否 | mmdb 命中 185.176.9.26 -> ES |
| 544 | `82.118.19.153` | vless | DE | ip-literal | 否 | mmdb 命中 82.118.19.153 -> DE |
| 545 | `153.56.229.207` | vless | DE | ip-literal | 否 | mmdb 命中 153.56.229.207 -> DE |
| 546 | `185.255.115.103` | vless | DE | ip-literal | 否 | mmdb 命中 185.255.115.103 -> DE |
| 547 | `GozargahAzad&encryption=none&security=reality&flow=xtls-rprx-vision&type=tcp&sni=mirror-50.topp-con.xyz&fp=chrome&pbk=NY2bvH4IFKTstWkBWwyU5MmlzuKk0nU08cBoHlti2S8&sid=2ef2b10d5143d798` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 548 | `5.180.27.134` | vless | KZ | ip-literal | 否 | mmdb 命中 5.180.27.134 -> KZ |
| 549 | `195.206.235.234` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.234 -> NL |
| 550 | `31.77.199.15` | vless | FI | ip-literal | 否 | mmdb 命中 31.77.199.15 -> FI |
| 551 | `7aa271t.es1.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.67.148 -> EE |
| 552 | `leviko-us2057.shopingggg.ir` | vless | US | domain-resolved | 是 | 解析到 2.24.124.64 -> US |
| 553 | `188.116.27.6` | vless | NL | ip-literal | 否 | mmdb 命中 188.116.27.6 -> NL |
| 554 | `107.181.151.128` | vless | GB | ip-literal | 否 | mmdb 命中 107.181.151.128 -> GB |
| 555 | `94.183.234.245` | vless | LV | ip-literal | 否 | mmdb 命中 94.183.234.245 -> LV |
| 556 | `swe4.mlbaz.ir` | vless | SE | domain-resolved | 否 | 解析到 89.22.236.19 -> SE |
| 557 | `152.228.139.33` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.139.33 -> FR |
| 558 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 559 | `flawers.shop` | trojan | PL | domain-resolved | 否 | 解析到 187.52.45.183 -> PL |
| 560 | `187.52.45.183` | trojan | PL | ip-literal | 否 | mmdb 命中 187.52.45.183 -> PL |
| 561 | `169.197.140.208` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.208 -> US |
| 562 | `51.158.206.93` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.93 -> NL |
| 563 | `du5g.altheora.ir` | vless | DE | domain-resolved | 否 | 解析到 116.202.184.184 -> DE |
| 564 | `15.204.97.216` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.216 -> US |
| 565 | `148.135.86.162` | vless | US | ip-literal | 是 | mmdb 命中 148.135.86.162 -> US |
| 566 | `51.158.206.19` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.19 -> NL |
| 567 | `51.158.206.29` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.29 -> NL |
| 568 | `51.158.206.80` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.80 -> NL |
| 569 | `51.158.206.97` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.97 -> NL |
| 570 | `51.158.206.34` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.34 -> NL |
| 571 | `23.19.231.244` | vless | US | ip-literal | 是 | mmdb 命中 23.19.231.244 -> US |
| 572 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 573 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 574 | `178.172.227.228` | vless | BY | ip-literal | 否 | mmdb 命中 178.172.227.228 -> BY |
| 575 | `2.27.174.182` | vless | TW | ip-literal | 否 | mmdb 命中 2.27.174.182 -> TW |
| 576 | `37.221.76.116` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.116 -> TR |
| 577 | `Kir3.crackerbinam.org` | vless | VN | domain-resolved | 否 | 解析到 103.163.24.22 -> VN |
| 578 | `leviko-vn7739.shopingggg.ir` | vless | VN | domain-resolved | 否 | 解析到 103.163.24.22 -> VN |
| 579 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 580 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 581 | `185.71.216.177` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.177 -> TR |
| 582 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 583 | `37.221.76.116` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.116 -> TR |
| 584 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 585 | `185.71.216.177` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.177 -> TR |
| 586 | `37.221.76.117` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.117 -> TR |
| 587 | `37.221.76.116` | vless | TR | ip-literal | 否 | mmdb 命中 37.221.76.116 -> TR |
| 588 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 589 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 590 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 591 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 592 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 593 | `158.101.151.157` | vless | JP | ip-literal | 否 | mmdb 命中 158.101.151.157 -> JP |
| 594 | `78.17.215.141` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.141 -> DE |
| 595 | `176.98.176.60` | vless | RU | ip-literal | 否 | mmdb 命中 176.98.176.60 -> RU |
| 596 | `n4.steptofsvo.com` | vless | NO | domain-resolved | 否 | 解析到 80.86.215.46 -> NO |
| 597 | `render.com` | vless | US | domain-resolved | 是 | 解析到 216.24.57.1 -> US |
| 598 | `promo.betust.net` | hysteria2 | SE | domain-resolved | 否 | 解析到 50.7.38.243 -> SE |
| 599 | `78.159.250.83` | vless | RU | ip-literal | 否 | mmdb 命中 78.159.250.83 -> RU |
| 600 | `95.85.232.83` | vless | CZ | ip-literal | 否 | mmdb 命中 95.85.232.83 -> CZ |
| 601 | `185.255.115.169` | vless | DE | ip-literal | 否 | mmdb 命中 185.255.115.169 -> DE |
| 602 | `185.14.29.29` | vless | NL | ip-literal | 否 | mmdb 命中 185.14.29.29 -> NL |
| 603 | `79.182.70.220` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.220 -> NL |
| 604 | `62.210.91.10` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.91.10 -> FR |
| 605 | `18.227.151.228` | vless | US | ip-literal | 是 | mmdb 命中 18.227.151.228 -> US |
| 606 | `31.59.169.225` | hysteria2 | AE | ip-literal | 否 | mmdb 命中 31.59.169.225 -> AE |
| 607 | `38.244.5.231` | vless | US | ip-literal | 是 | mmdb 命中 38.244.5.231 -> US |
| 608 | `47.251.108.158` | vless | US | ip-literal | 是 | mmdb 命中 47.251.108.158 -> US |
| 609 | `189.74.106.46` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.106.46 -> RU |
| 610 | `163.245.42.87` | vless | DE | ip-literal | 否 | mmdb 命中 163.245.42.87 -> DE |
| 611 | `9.247.23.209` | vless | DE | ip-literal | 否 | mmdb 命中 9.247.23.209 -> DE |
| 612 | `163.245.42.56` | vless | DE | ip-literal | 否 | mmdb 命中 163.245.42.56 -> DE |
| 613 | `152.53.239.182` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.239.182 -> DE |
| 614 | `78.17.215.137` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.137 -> DE |
| 615 | `de166.mech-pro.online` | vless | DE | domain-resolved | 否 | 解析到 187.7.206.49 -> DE |
| 616 | `189.74.115.29` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.115.29 -> RU |
| 617 | `217.60.179.166` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.179.166 -> DE |
| 618 | `nl-06.neverspy.tech` | vless | NL | domain-resolved | 否 | 解析到 185.112.59.157 -> NL |
| 619 | `152.53.127.214` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.127.214 -> DE |
| 620 | `178.130.46.188` | vless | RU | ip-literal | 否 | mmdb 命中 178.130.46.188 -> RU |
| 621 | `jdwadgw.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.239.182 -> DE |
| 622 | `189.74.116.28` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.116.28 -> RU |
| 623 | `2.26.251.236` | vless | DE | ip-literal | 否 | mmdb 命中 2.26.251.236 -> DE |
| 624 | `104.171.133.209` | vless | RU | ip-literal | 否 | mmdb 命中 104.171.133.209 -> RU |
| 625 | `150.251.143.253` | vless | NL | ip-literal | 否 | mmdb 命中 150.251.143.253 -> NL |
| 626 | `89.169.2.136` | vless | RU | ip-literal | 否 | mmdb 命中 89.169.2.136 -> RU |
| 627 | `195.206.235.202` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.202 -> NL |
| 628 | `4935e4t.de25.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 185.255.115.181 -> DE |
| 629 | `51.161.204.242` | vless | AU | ip-literal | 否 | mmdb 命中 51.161.204.242 -> AU |
| 630 | `67.159.52.81` | vless | SG | ip-literal | 否 | mmdb 命中 67.159.52.81 -> SG |
| 631 | `82.139.235.44` | vless | DE | ip-literal | 否 | mmdb 命中 82.139.235.44 -> DE |
| 632 | `188.166.182.158` | vless | SG | ip-literal | 否 | mmdb 命中 188.166.182.158 -> SG |
| 633 | `148.113.5.22` | vless | IN | ip-literal | 否 | mmdb 命中 148.113.5.22 -> IN |
| 634 | `177.1.193.28` | vless | PL | ip-literal | 否 | mmdb 命中 177.1.193.28 -> PL |
| 635 | `195.206.235.99` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.99 -> NL |
| 636 | `145.223.68.58` | vless | FR | ip-literal | 否 | mmdb 命中 145.223.68.58 -> FR |
| 637 | `45.192.12.92` | vless | PL | ip-literal | 否 | mmdb 命中 45.192.12.92 -> PL |
| 638 | `189.74.117.12` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.117.12 -> RU |
| 639 | `130.17.15.75` | vless | DE | ip-literal | 否 | mmdb 命中 130.17.15.75 -> DE |
| 640 | `213.165.39.134` | vless | NL | ip-literal | 否 | mmdb 命中 213.165.39.134 -> NL |
| 641 | `music.3apes.online` | vless | DE | domain-resolved | 否 | 解析到 217.60.27.153 -> DE |
| 642 | `2.24.124.64` | vless | US | ip-literal | 是 | mmdb 命中 2.24.124.64 -> US |
| 643 | `31.59.148.132` | vless | NL | ip-literal | 否 | mmdb 命中 31.59.148.132 -> NL |
| 644 | `217.69.174.175` | vless | DE | ip-literal | 否 | mmdb 命中 217.69.174.175 -> DE |
| 645 | `91.238.123.9` | vless | DE | ip-literal | 否 | mmdb 命中 91.238.123.9 -> DE |
| 646 | `37.235.247.81` | vless | RU | ip-literal | 否 | mmdb 命中 37.235.247.81 -> RU |
| 647 | `45.90.59.15` | vless | CH | ip-literal | 否 | mmdb 命中 45.90.59.15 -> CH |
| 648 | `198.200.57.142` | hysteria | US | ip-literal | 是 | mmdb 命中 198.200.57.142 -> US |
| 649 | `137.175.82.44` | hysteria | US | ip-literal | 是 | mmdb 命中 137.175.82.44 -> US |
| 650 | `62.210.124.132` | hysteria | FR | ip-literal | 否 | mmdb 命中 62.210.124.132 -> FR |
| 651 | `62.210.28.175` | hysteria | FR | ip-literal | 否 | mmdb 命中 62.210.28.175 -> FR |
| 652 | `fc82dfx.nl8.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 13.143.239.6 -> EE |
| 653 | `196.196.204.148` | vless | FI | ip-literal | 否 | mmdb 命中 196.196.204.148 -> FI |
| 654 | `193.233.199.30` | vless | RU | ip-literal | 否 | mmdb 命中 193.233.199.30 -> RU |
| 655 | `217.60.25.100` | vless | PL | ip-literal | 否 | mmdb 命中 217.60.25.100 -> PL |
| 656 | `62.144.51.70` | vless | DE | ip-literal | 否 | mmdb 命中 62.144.51.70 -> DE |
| 657 | `48.103.231.2` | vless | DE | ip-literal | 否 | mmdb 命中 48.103.231.2 -> DE |
| 658 | `163.172.214.188` | vless | NL | ip-literal | 否 | mmdb 命中 163.172.214.188 -> NL |
| 659 | `104.17.3.81` | vless | US | ip-literal | 是 | mmdb 命中 104.17.3.81 -> US |
| 660 | `155.103.71.207` | vless | TR | ip-literal | 否 | mmdb 命中 155.103.71.207 -> TR |
| 661 | `147.45.116.64` | vless | BR | ip-literal | 否 | mmdb 命中 147.45.116.64 -> BR |
| 662 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 663 | `85.237.207.221` | vless | TW | ip-literal | 否 | mmdb 命中 85.237.207.221 -> TW |
| 664 | `panel.apexkey.store` | vless | US | domain-resolved | 是 | 解析到 147.224.54.25 -> US |
| 665 | `147.224.54.25` | vless | US | ip-literal | 是 | mmdb 命中 147.224.54.25 -> US |
| 666 | `89.163.239.238` | vless | DE | ip-literal | 否 | mmdb 命中 89.163.239.238 -> DE |
| 667 | `cadrin.wtf` | vless | RU | domain-resolved | 否 | 解析到 188.225.78.178 -> RU |
| 668 | `ledger.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 80.242.57.69 -> RU |
| 669 | `46.28.69.123` | vless | DE | ip-literal | 否 | mmdb 命中 46.28.69.123 -> DE |
| 670 | `66.163.118.113` | vless | ES | ip-literal | 否 | mmdb 命中 66.163.118.113 -> ES |
| 671 | `138.124.251.98` | vless | FR | ip-literal | 否 | mmdb 命中 138.124.251.98 -> FR |
| 672 | `guide.blog-forme.ru` | hysteria2 | CZ | domain-resolved | 否 | 解析到 95.85.231.3 -> CZ |
| 673 | `tjzx49io.zibayeman.com` | hysteria2 | SE | domain-resolved | 否 | 解析到 65.20.114.110 -> SE |
| 674 | `92.118.206.217` | vless | DE | ip-literal | 否 | mmdb 命中 92.118.206.217 -> DE |
| 675 | `5.35.44.218` | vless | NL | ip-literal | 否 | mmdb 命中 5.35.44.218 -> NL |
| 676 | `179.254.169.116` | vless | FI | ip-literal | 否 | mmdb 命中 179.254.169.116 -> FI |
| 677 | `durov.sky-vault.top` | vless | FI | domain-resolved | 否 | 解析到 179.254.169.116 -> FI |
| 678 | `188.166.182.158` | vless | SG | ip-literal | 否 | mmdb 命中 188.166.182.158 -> SG |
| 679 | `16.176.175.171` | vless | AU | ip-literal | 否 | mmdb 命中 16.176.175.171 -> AU |
| 680 | `sc-thenetherlands1.09vpn.com` | vless | NL | domain-resolved | 否 | 解析到 163.172.214.188 -> NL |
| 681 | `sajed.kdns.fr` | vless | SE | domain-resolved | 否 | 解析到 13.60.56.123 -> SE |
| 682 | `ov-germany1.09vpn.com` | vless | DE | domain-resolved | 否 | 解析到 57.129.41.216 -> DE |
| 683 | `196.196.149.81` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.149.81 -> SC |
| 684 | `196.196.149.80` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.149.80 -> SC |
| 685 | `almanac.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 5.42.105.128 -> RU |
| 686 | `pl.galacticworld.online` | vless | US | domain-resolved | 是 | 解析到 150.241.87.52 -> US |
| 687 | `51.15.16.68` | vless | NL | ip-literal | 否 | mmdb 命中 51.15.16.68 -> NL |
| 688 | `143.246.60.254` | vless | US | ip-literal | 是 | mmdb 命中 143.246.60.254 -> US |
| 689 | `leviko-cl7123.shopingggg.ir` | trojan | CL | domain-resolved | 否 | 解析到 64.176.7.205 -> CL |
| 690 | `143.246.62.191` | vless | US | ip-literal | 是 | mmdb 命中 143.246.62.191 -> US |
| 691 | `48.103.133.47` | vless | RU | ip-literal | 否 | mmdb 命中 48.103.133.47 -> RU |
| 692 | `89.125.175.181` | vless | AE | ip-literal | 否 | mmdb 命中 89.125.175.181 -> AE |
| 693 | `94.183.164.119` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.119 -> NL |
| 694 | `94.183.164.96` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.96 -> NL |
| 695 | `213.199.57.127` | vless | FR | ip-literal | 否 | mmdb 命中 213.199.57.127 -> FR |
| 696 | `213.165.53.128` | vless | DE | ip-literal | 否 | mmdb 命中 213.165.53.128 -> DE |
| 697 | `31.76.39.156` | vless | GB | ip-literal | 否 | mmdb 命中 31.76.39.156 -> GB |
| 698 | `dfsto.whitenw.net` | vless | RU | domain-resolved | 否 | 解析到 188.225.42.18 -> RU |
| 699 | `leviko-ru1148.shopingggg.ir` | vless | RU | domain-resolved | 否 | 解析到 37.235.247.81 -> RU |
| 700 | `edge.bookmai.com` | vless | US | domain-resolved | 是 | 解析到 104.164.82.0 -> US |
| 701 | `193.108.119.193` | trojan | DE | ip-literal | 否 | mmdb 命中 193.108.119.193 -> DE |
| 702 | `de01.node.qixi.best` | trojan | US | domain-resolved | 是 | 解析到 172.64.144.52 -> US |
| 703 | `136.148.83.69` | vless | RU | ip-literal | 否 | mmdb 命中 136.148.83.69 -> RU |
| 704 | `198.202.24.142` | vless | US | ip-literal | 是 | mmdb 命中 198.202.24.142 -> US |
| 705 | `13.140.253.35` | vless | IN | ip-literal | 否 | mmdb 命中 13.140.253.35 -> IN |
| 706 | `187.7.206.49` | vless | DE | ip-literal | 否 | mmdb 命中 187.7.206.49 -> DE |
| 707 | `slot3.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.253.106 -> DE |
| 708 | `slot1.ipoxxo.online` | vless | DE | domain-resolved | 否 | 解析到 91.107.252.238 -> DE |
| 709 | `176.120.17.194` | vless | IR | ip-literal | 否 | mmdb 命中 176.120.17.194 -> IR |
| 710 | `45.86.158.53` | vless | DE | ip-literal | 否 | mmdb 命中 45.86.158.53 -> DE |
| 711 | `199.242.185.178` | vless | US | ip-literal | 是 | mmdb 命中 199.242.185.178 -> US |
| 712 | `64.178.113.127` | vless | US | ip-literal | 是 | mmdb 命中 64.178.113.127 -> US |
| 713 | `3.147.205.191` | vless | US | ip-literal | 是 | mmdb 命中 3.147.205.191 -> US |
| 714 | `Fear_Config---&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=fuck.rkn&sid=01` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 715 | `169.40.42.89` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.89 -> DE |
| 716 | `95.174.68.188` | vless | AE | ip-literal | 否 | mmdb 命中 95.174.68.188 -> AE |
| 717 | `de-03.neverspy.tech` | vless | DE | domain-resolved | 否 | 解析到 193.233.198.117 -> DE |
| 718 | `167.17.179.207` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 167.17.179.207 -> JP |
| 719 | `717252g.nl8.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 13.143.239.6 -> EE |
| 720 | `0592efg.us8.h1clayd.click` | vless | NL | domain-resolved | 否 | 解析到 13.141.51.197 -> NL |
| 721 | `15b171g.nl7.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 143.246.41.226 -> EE |
| 722 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 723 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 724 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 725 | `o685y.save-node.com` | vless | DE | domain-resolved | 否 | 解析到 88.216.70.125 -> DE |
| 726 | `104.19.180.169` | trojan | US | ip-literal | 是 | mmdb 命中 104.19.180.169 -> US |
| 727 | `31.59.179.215` | vless | DE | ip-literal | 否 | mmdb 命中 31.59.179.215 -> DE |
| 728 | `13.143.232.161` | vless | NL | ip-literal | 否 | mmdb 命中 13.143.232.161 -> NL |
| 729 | `103.88.243.142` | hysteria2 | RU | ip-literal | 否 | mmdb 命中 103.88.243.142 -> RU |
| 730 | `95.85.243.72` | vless | EE | ip-literal | 否 | mmdb 命中 95.85.243.72 -> EE |
| 731 | `95.128.157.245` | vless | DE | ip-literal | 否 | mmdb 命中 95.128.157.245 -> DE |
| 732 | `154.12.49.239` | vless | US | ip-literal | 是 | mmdb 命中 154.12.49.239 -> US |
| 733 | `179.254.92.190` | vless | US | ip-literal | 是 | mmdb 命中 179.254.92.190 -> US |
| 734 | `it01.node.qixi.best` | trojan | US | domain-resolved | 是 | 解析到 104.17.188.61 -> US |
| 735 | `45.135.235.255` | vless | BZ | ip-literal | 否 | mmdb 命中 45.135.235.255 -> BZ |
| 736 | `185.18.250.2` | vless | CH | ip-literal | 否 | mmdb 命中 185.18.250.2 -> CH |
| 737 | `88.216.70.125` | vless | DE | ip-literal | 否 | mmdb 命中 88.216.70.125 -> DE |
| 738 | `104.19.33.237` | vless | US | ip-literal | 是 | mmdb 命中 104.19.33.237 -> US |
| 739 | `195.63.128.21` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 740 | `leviko-de6003.shopingggg.ir` | vless | US | domain-resolved | 是 | 解析到 31.76.32.122 -> US |
| 741 | `66.163.122.81` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.81 -> US |
| 742 | `195.123.213.28` | vless | LV | ip-literal | 否 | mmdb 命中 195.123.213.28 -> LV |
| 743 | `78.17.215.138` | vless | DE | ip-literal | 否 | mmdb 命中 78.17.215.138 -> DE |
| 744 | `141.227.170.220` | vless | FR | ip-literal | 否 | mmdb 命中 141.227.170.220 -> FR |
| 745 | `138.124.80.29` | vless | CH | ip-literal | 否 | mmdb 命中 138.124.80.29 -> CH |
| 746 | `81.90.21.163` | vless | SE | ip-literal | 否 | mmdb 命中 81.90.21.163 -> SE |
| 747 | `157.180.98.124` | vless | FI | ip-literal | 否 | mmdb 命中 157.180.98.124 -> FI |
| 748 | `xray-dmr3b3hy-calm-maple-7.cloady.io` | vless | IN | domain-resolved | 否 | 解析到 13.140.253.35 -> IN |
| 749 | `tel.shnovps.cyou` | vless | IR | domain-resolved | 否 | 解析到 81.12.57.72 -> IR |
| 750 | `srv-17e124.21freedom.net` | hysteria2 | RU | domain-resolved | 否 | 解析到 103.88.243.142 -> RU |
| 751 | `146.19.254.171` | vless | NL | ip-literal | 否 | mmdb 命中 146.19.254.171 -> NL |
| 752 | `129.153.128.162` | vless | US | ip-literal | 是 | mmdb 命中 129.153.128.162 -> US |
| 753 | `59.125.69.23` | vless | TW | ip-literal | 否 | mmdb 命中 59.125.69.23 -> TW |
| 754 | `sg.fasti.win` | vless | SG | domain-resolved | 否 | 解析到 67.159.52.81 -> SG |
| 755 | `46.28.71.247` | vless | ES | ip-literal | 否 | mmdb 命中 46.28.71.247 -> ES |
| 756 | `169.40.42.163` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.163 -> DE |
| 757 | `143.246.41.199` | vless | EE | ip-literal | 否 | mmdb 命中 143.246.41.199 -> EE |
| 758 | `13.143.187.220` | vless | US | ip-literal | 是 | mmdb 命中 13.143.187.220 -> US |
| 759 | `213.176.92.168` | vless | HK | ip-literal | 否 | mmdb 命中 213.176.92.168 -> HK |
| 760 | `163.172.214.188` | vless | NL | ip-literal | 否 | mmdb 命中 163.172.214.188 -> NL |
| 761 | `195.63.128.21` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 762 | `uspanel.unixzone.us` | vless | US | domain-resolved | 是 | 解析到 69.48.201.136 -> US |
| 763 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 764 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 765 | `150.230.229.100` | hysteria2 | BR | ip-literal | 否 | mmdb 命中 150.230.229.100 -> BR |
| 766 | `82.118.16.189` | vless | IT | ip-literal | 否 | mmdb 命中 82.118.16.189 -> IT |
| 767 | `91.224.74.146` | vless | KZ | ip-literal | 否 | mmdb 命中 91.224.74.146 -> KZ |
| 768 | `191.217.204.28` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 191.217.204.28 -> DE |
| 769 | `45.61.186.3` | vless | US | ip-literal | 是 | mmdb 命中 45.61.186.3 -> US |
| 770 | `193.122.106.29` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 193.122.106.29 -> KR |
| 771 | `201.51.11.65` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.11.65 -> RU |
| 772 | `43.108.48.169` | vless | KR | ip-literal | 否 | mmdb 命中 43.108.48.169 -> KR |
| 773 | `45.192.193.54` | vless | HK | ip-literal | 否 | mmdb 命中 45.192.193.54 -> HK |
| 774 | `196.245.153.156` | vless | SK | ip-literal | 否 | mmdb 命中 196.245.153.156 -> SK |
| 775 | `188.225.42.18` | vless | RU | ip-literal | 否 | mmdb 命中 188.225.42.18 -> RU |
| 776 | `82.118.16.187` | vless | IT | ip-literal | 否 | mmdb 命中 82.118.16.187 -> IT |
| 777 | `77.83.245.79` | vless | TR | ip-literal | 否 | mmdb 命中 77.83.245.79 -> TR |
| 778 | `144.31.125.60` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.125.60 -> DE |
| 779 | `150.241.87.52` | vless | US | ip-literal | 是 | mmdb 命中 150.241.87.52 -> US |
| 780 | `172.64.79.163` | vless | US | ip-literal | 是 | mmdb 命中 172.64.79.163 -> US |
| 781 | `66.163.118.166` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.166 -> ES |
| 782 | `161.97.66.16` | vless | FR | ip-literal | 否 | mmdb 命中 161.97.66.16 -> FR |
| 783 | `195.206.235.232` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.232 -> NL |
| 784 | `62.210.91.2` | vless | FR | ip-literal | 否 | mmdb 命中 62.210.91.2 -> FR |
| 785 | `77.67.18.254` | vless | JP | ip-literal | 否 | mmdb 命中 77.67.18.254 -> JP |
| 786 | `2.56.127.202` | vless | CY | ip-literal | 否 | mmdb 命中 2.56.127.202 -> CY |
| 787 | `216.238.104.154` | trojan | BR | ip-literal | 否 | mmdb 命中 216.238.104.154 -> BR |
| 788 | `free-amsterdam-node-1.cloudwidecdn.com` | vless | NL | domain-resolved | 否 | 解析到 86.54.28.75 -> NL |
| 789 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 790 | `195.63.138.212` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 791 | `5.178.109.174` | vless | SE | ip-literal | 否 | mmdb 命中 5.178.109.174 -> SE |
| 792 | `quay.gerqix.online` | vless | RU | domain-resolved | 否 | 解析到 194.87.131.9 -> RU |
| 793 | `linen.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 194.87.131.9 -> RU |
| 794 | `193.188.21.253` | vless | SE | ip-literal | 否 | mmdb 命中 193.188.21.253 -> SE |
| 795 | `159.13.55.48` | hysteria2 | AU | ip-literal | 否 | mmdb 命中 159.13.55.48 -> AU |
| 796 | `194.135.22.186` | vless | CH | ip-literal | 否 | mmdb 命中 194.135.22.186 -> CH |
| 797 | `SC-TheNetherlands1.09vpn.com` | vless | NL | domain-resolved | 否 | 解析到 163.172.214.188 -> NL |
| 798 | `83.147.18.3` | vless | ES | ip-literal | 否 | mmdb 命中 83.147.18.3 -> ES |
| 799 | `50.7.169.243` | vless | US | ip-literal | 是 | mmdb 命中 50.7.169.243 -> US |
| 800 | `jdwabxe.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.236.22 -> DE |
| 801 | `152.53.236.22` | vless | DE | ip-literal | 否 | mmdb 命中 152.53.236.22 -> DE |
| 802 | `jdvymxi.cvewfjg.shop` | vless | DE | domain-resolved | 否 | 解析到 152.53.127.214 -> DE |
| 803 | `138.124.245.102` | vless | NL | ip-literal | 否 | mmdb 命中 138.124.245.102 -> NL |
| 804 | `ww2.levikogjgfdd.ir` | vless | DE | domain-resolved | 否 | 解析到 144.31.125.60 -> DE |
| 805 | `209.200.246.148` | vless | CA | ip-literal | 否 | mmdb 命中 209.200.246.148 -> CA |
| 806 | `81.12.57.72` | vless | IR | ip-literal | 否 | mmdb 命中 81.12.57.72 -> IR |
| 807 | `45.144.234.157` | vless | FI | ip-literal | 否 | mmdb 命中 45.144.234.157 -> FI |
| 808 | `193.233.89.130` | vless | RU | ip-literal | 否 | mmdb 命中 193.233.89.130 -> RU |
| 809 | `95.143.196.97` | trojan | SE | ip-literal | 否 | mmdb 命中 95.143.196.97 -> SE |
| 810 | `leviko-se3078.shopingggg.ir` | vless | SC | domain-resolved | 否 | 解析到 46.29.255.123 -> SC |
| 811 | `48.102.170.205` | vless | NL | ip-literal | 否 | mmdb 命中 48.102.170.205 -> NL |
| 812 | `78.159.245.147` | vless | RU | ip-literal | 否 | mmdb 命中 78.159.245.147 -> RU |
| 813 | `86.54.28.75` | vless | NL | ip-literal | 否 | mmdb 命中 86.54.28.75 -> NL |
| 814 | `195.63.128.21` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.128.21 -> NL |
| 815 | `185.86.145.183` | vless | RU | ip-literal | 否 | mmdb 命中 185.86.145.183 -> RU |
| 816 | `tochkacdn.top` | vless | RU | domain-resolved | 否 | 解析到 185.178.208.167 -> RU |
| 817 | `201.51.2.188` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.2.188 -> RU |
| 818 | `pssdwynorv.newwl.pro` | vless | RU | domain-resolved | 否 | 解析到 31.177.111.107 -> RU |
| 819 | `leviko-by6237.shopingggg.ir` | vless | BY | domain-resolved | 否 | 解析到 178.172.227.228 -> BY |
| 820 | `103.106.229.37` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.37 -> SG |
| 821 | `94.183.164.176` | vless | NL | ip-literal | 否 | mmdb 命中 94.183.164.176 -> NL |
| 822 | `196.196.149.30` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.149.30 -> SC |
| 823 | `195.206.235.44` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.44 -> NL |
| 824 | `48.103.230.81` | vless | NL | ip-literal | 否 | mmdb 命中 48.103.230.81 -> NL |
| 825 | `87.120.92.68` | vless | BG | ip-literal | 否 | mmdb 命中 87.120.92.68 -> BG |
| 826 | `83.217.201.82` | vless | RU | ip-literal | 否 | mmdb 命中 83.217.201.82 -> RU |
| 827 | `195.123.240.65` | vless | US | ip-literal | 是 | mmdb 命中 195.123.240.65 -> US |
| 828 | `144.48.11.146` | vless | RU | ip-literal | 否 | mmdb 命中 144.48.11.146 -> RU |
| 829 | `13.140.91.65` | vless | DE | ip-literal | 否 | mmdb 命中 13.140.91.65 -> DE |
| 830 | `179.43.187.67` | vless | CH | ip-literal | 否 | mmdb 命中 179.43.187.67 -> CH |
| 831 | `144.31.28.228` | vless | US | ip-literal | 是 | mmdb 命中 144.31.28.228 -> US |
| 832 | `170.114.46.6` | vless | US | ip-literal | 是 | mmdb 命中 170.114.46.6 -> US |
| 833 | `103.163.24.22` | vless | VN | ip-literal | 否 | mmdb 命中 103.163.24.22 -> VN |
| 834 | `tun5.speedfast99.ir` | vless | IR | domain-resolved | 否 | 解析到 5.202.14.174 -> IR |
| 835 | `201.8.64.254` | vless | NL | ip-literal | 否 | mmdb 命中 201.8.64.254 -> NL |
| 836 | `46.29.255.123` | vless | SC | ip-literal | 否 | mmdb 命中 46.29.255.123 -> SC |
| 837 | `31.222.235.81` | vless | UA | ip-literal | 否 | mmdb 命中 31.222.235.81 -> UA |
| 838 | `87.76.154.28` | vless | UA | ip-literal | 否 | mmdb 命中 87.76.154.28 -> UA |
| 839 | `13.143.239.94` | vless | EE | ip-literal | 否 | mmdb 命中 13.143.239.94 -> EE |
| 840 | `2.26.204.46` | vless | HK | ip-literal | 否 | mmdb 命中 2.26.204.46 -> HK |
| 841 | `132.243.67.224` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.67.224 -> EE |
| 842 | `199.7.140.201` | vless | US | ip-literal | 是 | mmdb 命中 199.7.140.201 -> US |
| 843 | `179.254.92.134` | vless | US | ip-literal | 是 | mmdb 命中 179.254.92.134 -> US |
| 844 | `ai.smrtai.top` | vless | FR | domain-resolved | 否 | 解析到 161.97.66.16 -> FR |
| 845 | `79.182.39.131` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.39.131 -> NL |
| 846 | `196.196.148.63` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.148.63 -> SC |
| 847 | `961ec0g.nl13.h1clayd.click` | vless | DE | domain-resolved | 否 | 解析到 48.103.231.82 -> DE |
| 848 | `b3cd32g.es9.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.67.148 -> EE |
| 849 | `162.35.101.177` | vless | US | ip-literal | 是 | mmdb 命中 162.35.101.177 -> US |
| 850 | `47.251.25.74` | vless | US | ip-literal | 是 | mmdb 命中 47.251.25.74 -> US |
| 851 | `47.253.226.114` | vless | US | ip-literal | 是 | mmdb 命中 47.253.226.114 -> US |
| 852 | `217.60.27.153` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.27.153 -> DE |
| 853 | `185.246.155.91` | vless | NL | ip-literal | 否 | mmdb 命中 185.246.155.91 -> NL |
| 854 | `5d0319t.nl7.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 143.246.41.226 -> EE |
| 855 | `88.216.214.159` | vless | SE | ip-literal | 否 | mmdb 命中 88.216.214.159 -> SE |
| 856 | `132.243.66.95` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.66.95 -> EE |
| 857 | `201.24.121.243` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.121.243 -> RU |
| 858 | `185.246.155.91` | vless | NL | ip-literal | 否 | mmdb 命中 185.246.155.91 -> NL |
| 859 | `13.141.51.2` | vless | NL | ip-literal | 否 | mmdb 命中 13.141.51.2 -> NL |
| 860 | `178.212.35.198` | vless | IN | ip-literal | 否 | mmdb 命中 178.212.35.198 -> IN |
| 861 | `38.107.234.57` | vless | KZ | ip-literal | 否 | mmdb 命中 38.107.234.57 -> KZ |
| 862 | `193.188.21.253` | vless | SE | ip-literal | 否 | mmdb 命中 193.188.21.253 -> SE |
| 863 | `178.172.227.124` | vless | BY | ip-literal | 否 | mmdb 命中 178.172.227.124 -> BY |
| 864 | `ujp.xn--ghqu5fm27b67w.com` | vless | US | domain-resolved | 是 | 解析到 104.18.10.153 -> US |
| 865 | `178.94.25.73` | vless | SG | ip-literal | 否 | mmdb 命中 178.94.25.73 -> SG |
| 866 | `woodgrain.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 89.169.44.210 -> RU |
| 867 | `147.45.66.208` | vless | DE | ip-literal | 否 | mmdb 命中 147.45.66.208 -> DE |
| 868 | `83.243.86.129` | vless | DE | ip-literal | 否 | mmdb 命中 83.243.86.129 -> DE |
| 869 | `178.172.227.124` | vless | BY | ip-literal | 否 | mmdb 命中 178.172.227.124 -> BY |
| 870 | `ov-france1.09vpn.com` | vless | FR | domain-resolved | 否 | 解析到 152.228.162.19 -> FR |
| 871 | `193.163.203.170` | vless | LV | ip-literal | 否 | mmdb 命中 193.163.203.170 -> LV |
| 872 | `109.248.170.119` | vless | KZ | ip-literal | 否 | mmdb 命中 109.248.170.119 -> KZ |
| 873 | `willow.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 201.24.122.189 -> RU |
| 874 | `leviko-nl2559.shopingggg.ir` | vless | NL | domain-resolved | 否 | 解析到 146.19.254.171 -> NL |
| 875 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 876 | `bookend.filnex.baby` | vless | RU | domain-resolved | 否 | 解析到 80.242.57.69 -> RU |
| 877 | `leviko-tr3098.shopingggg.ir` | vless | DE | domain-resolved | 否 | 解析到 147.45.66.208 -> DE |
| 878 | `170.101.101.67` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.67 -> US |
| 879 | `45.86.60.174` | vless | CY | ip-literal | 否 | mmdb 命中 45.86.60.174 -> CY |
| 880 | `103.106.229.177` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.177 -> SG |
| 881 | `193.8.114.28` | vless | ES | ip-literal | 否 | mmdb 命中 193.8.114.28 -> ES |
| 882 | `195.206.235.48` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.48 -> NL |
| 883 | `195.206.235.110` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.110 -> NL |
| 884 | `b3cd32g.es1.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.67.148 -> EE |
| 885 | `164.37.224.245` | vless | NL | ip-literal | 否 | mmdb 命中 164.37.224.245 -> NL |
| 886 | `201.8.71.230` | vless | DE | ip-literal | 否 | mmdb 命中 201.8.71.230 -> DE |
| 887 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 888 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 889 | `103.106.229.177` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.177 -> SG |
| 890 | `196.245.153.92` | vless | SK | ip-literal | 否 | mmdb 命中 196.245.153.92 -> SK |
| 891 | `103.106.229.37` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.37 -> SG |
| 892 | `13.140.56.100` | vless | IN | ip-literal | 否 | mmdb 命中 13.140.56.100 -> IN |
| 893 | `103.106.229.37` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.37 -> SG |
| 894 | `84.235.244.108` | vless | AE | ip-literal | 否 | mmdb 命中 84.235.244.108 -> AE |
| 895 | `103.106.229.177` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.177 -> SG |
| 896 | `48.102.214.171` | hysteria2 | US | ip-literal | 是 | mmdb 命中 48.102.214.171 -> US |
| 897 | `103.75.118.228` | vless | JP | ip-literal | 否 | mmdb 命中 103.75.118.228 -> JP |
| 898 | `147.135.213.72` | vless | FR | ip-literal | 否 | mmdb 命中 147.135.213.72 -> FR |
| 899 | `179.254.115.111` | vless | DE | ip-literal | 否 | mmdb 命中 179.254.115.111 -> DE |
| 900 | `511.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.37 -> SG |
| 901 | `146.103.118.189` | vless | NL | ip-literal | 否 | mmdb 命中 146.103.118.189 -> NL |
| 902 | `185.138.90.27` | vless | PL | ip-literal | 否 | mmdb 命中 185.138.90.27 -> PL |
| 903 | `139.162.27.96` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.27.96 -> SG |
| 904 | `196.196.148.90` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.148.90 -> SC |
| 905 | `132.243.163.253` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.253 -> GB |
| 906 | `168.110.21.56` | vless | JP | ip-literal | 否 | mmdb 命中 168.110.21.56 -> JP |
| 907 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 908 | `79.182.70.232` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.232 -> NL |
| 909 | `150.251.141.246` | vless | NL | ip-literal | 否 | mmdb 命中 150.251.141.246 -> NL |
| 910 | `103.106.229.177` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.177 -> SG |
| 911 | `178.172.227.124` | vless | BY | ip-literal | 否 | mmdb 命中 178.172.227.124 -> BY |
| 912 | `510.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 103.106.229.177 -> SG |
| 913 | `132.243.163.125` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.125 -> GB |
| 914 | `152.69.226.63` | vless | KR | ip-literal | 否 | mmdb 命中 152.69.226.63 -> KR |
| 915 | `in.smrtai.top` | vless | IN | domain-resolved | 否 | 解析到 178.212.35.198 -> IN |
| 916 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 917 | `195.206.235.74` | vless | NL | ip-literal | 否 | mmdb 命中 195.206.235.74 -> NL |
| 918 | `164.37.224.238` | vless | NL | ip-literal | 否 | mmdb 命中 164.37.224.238 -> NL |
| 919 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 920 | `kir3.crackerbinam.org` | vless | VN | domain-resolved | 否 | 解析到 103.163.24.22 -> VN |
| 921 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 922 | `webdisk.jaggyslawa.org` | vless | GB | domain-resolved | 否 | 解析到 107.181.151.128 -> GB |
| 923 | `132.243.66.153` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.66.153 -> EE |
| 924 | `85.90.197.220` | vless | GR | ip-literal | 否 | mmdb 命中 85.90.197.220 -> GR |
| 925 | `196.199.122.2` | vless | SC | ip-literal | 否 | mmdb 命中 196.199.122.2 -> SC |
| 926 | `185.71.216.177` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.177 -> TR |
| 927 | `185.71.216.177` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.177 -> TR |
| 928 | `185.71.216.95` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.95 -> TR |
| 929 | `185.71.216.94` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.94 -> TR |
| 930 | `213.176.92.168` | vless | HK | ip-literal | 否 | mmdb 命中 213.176.92.168 -> HK |
| 931 | `185.71.216.177` | vless | TR | ip-literal | 否 | mmdb 命中 185.71.216.177 -> TR |
| 932 | `lists.soloramtin.cyou` | vless | US | domain-resolved | 是 | 解析到 50.117.15.225 -> US |
| 933 | `103.106.229.37` | vless | SG | ip-literal | 否 | mmdb 命中 103.106.229.37 -> SG |
| 934 | `132.243.66.220` | vless | EE | ip-literal | 否 | mmdb 命中 132.243.66.220 -> EE |
| 935 | `189.30.65.203` | vless | AE | ip-literal | 否 | mmdb 命中 189.30.65.203 -> AE |
| 936 | `147.135.213.72` | vless | FR | ip-literal | 否 | mmdb 命中 147.135.213.72 -> FR |
| 937 | `201.8.64.253` | vless | NL | ip-literal | 否 | mmdb 命中 201.8.64.253 -> NL |
| 938 | `50.117.15.225` | vless | US | ip-literal | 是 | mmdb 命中 50.117.15.225 -> US |
| 939 | `66.163.112.242` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.242 -> US |
| 940 | `216.152.147.74` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.74 -> CA |
| 941 | `216.152.147.85` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.85 -> CA |
| 942 | `156.229.167.109` | vless | US | ip-literal | 是 | mmdb 命中 156.229.167.109 -> US |
| 943 | `208.69.78.33` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.33 -> CH |
| 944 | `208.69.78.208` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.208 -> CH |
| 945 | `208.69.78.222` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.222 -> CH |
| 946 | `104.16.10.100` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.100 -> US |
| 947 | `104.16.144.131` | vless | US | ip-literal | 是 | mmdb 命中 104.16.144.131 -> US |
| 948 | `104.16.150.108` | vless | US | ip-literal | 是 | mmdb 命中 104.16.150.108 -> US |
| 949 | `104.16.172.173` | vless | US | ip-literal | 是 | mmdb 命中 104.16.172.173 -> US |
| 950 | `104.16.174.22` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.22 -> US |
| 951 | `104.16.174.34` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.34 -> US |
| 952 | `104.16.174.36` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.36 -> US |
| 953 | `104.16.174.37` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.37 -> US |
| 954 | `104.16.174.6` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.6 -> US |
| 955 | `104.16.25.21` | vless | US | ip-literal | 是 | mmdb 命中 104.16.25.21 -> US |
| 956 | `104.16.38.60` | vless | US | ip-literal | 是 | mmdb 命中 104.16.38.60 -> US |
| 957 | `104.16.40.145` | vless | US | ip-literal | 是 | mmdb 命中 104.16.40.145 -> US |
| 958 | `104.16.6.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.6.70 -> US |
| 959 | `leviconfigs🪐-29` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 960 | `104.16.79.73` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.79.73 -> US |
| 961 | `104.17.104.23` | vless | US | ip-literal | 是 | mmdb 命中 104.17.104.23 -> US |
| 962 | `VPNine1` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 963 | `104.17.148.22` | vless | US | ip-literal | 是 | mmdb 命中 104.17.148.22 -> US |
| 964 | `104.17.162.123` | vless | US | ip-literal | 是 | mmdb 命中 104.17.162.123 -> US |
| 965 | `104.17.217.1` | vless | US | ip-literal | 是 | mmdb 命中 104.17.217.1 -> US |
| 966 | `104.17.54.188` | vless | US | ip-literal | 是 | mmdb 命中 104.17.54.188 -> US |
| 967 | `104.18.109.147` | vless | US | ip-literal | 是 | mmdb 命中 104.18.109.147 -> US |
| 968 | `KAFING_2` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 969 | `proSSH)` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 970 | `104.18.152.133` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.133 -> US |
| 971 | `104.18.152.143` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.143 -> US |
| 972 | `104.18.152.161` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.161 -> US |
| 973 | `104.18.152.210` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.210 -> US |
| 974 | `104.18.152.225` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.225 -> US |
| 975 | `104.18.155.229` | vless | US | ip-literal | 是 | mmdb 命中 104.18.155.229 -> US |
| 976 | `104.18.22.208` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.22.208 -> US |
| 977 | `hopev2ray❤️‍🩹` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 978 | `leviconfigs🪐-11` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 979 | `v2ray_phoenix` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 980 | `104.18.46.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.46.234 -> US |
| 981 | `CUSTOMVPNSERVER` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 982 | `VPsave` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 983 | `104.19.229.21` | vless | US | ip-literal | 是 | mmdb 命中 104.19.229.21 -> US |
| 984 | `104.19.250.20` | vless | US | ip-literal | 是 | mmdb 命中 104.19.250.20 -> US |
| 985 | `104.21.16.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.16.1 -> US |
| 986 | `104.21.16.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.16.1 -> US |
| 987 | `104.21.33.59` | vless | US | ip-literal | 是 | mmdb 命中 104.21.33.59 -> US |
| 988 | `104.21.39.30` | vless | US | ip-literal | 是 | mmdb 命中 104.21.39.30 -> US |
| 989 | `104.21.74.214` | vless | US | ip-literal | 是 | mmdb 命中 104.21.74.214 -> US |
| 990 | `104.21.79.246` | trojan | US | ip-literal | 是 | mmdb 命中 104.21.79.246 -> US |
| 991 | `hopev2ray💚` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 992 | `104.24.248.85` | vless | US | ip-literal | 是 | mmdb 命中 104.24.248.85 -> US |
| 993 | `104.24.85.213` | vless | US | ip-literal | 是 | mmdb 命中 104.24.85.213 -> US |
| 994 | `104.26.14.137` | trojan | US | ip-literal | 是 | mmdb 命中 104.26.14.137 -> US |
| 995 | `leviconfigs🪐-6` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 996 | `104.26.4.230` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.230 -> US |
| 997 | `104.26.4.60` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.60 -> US |
| 998 | `104.26.6.89` | vless | US | ip-literal | 是 | mmdb 命中 104.26.6.89 -> US |
| 999 | `108.162.194.165` | vless | US | ip-literal | 是 | mmdb 命中 108.162.194.165 -> US |
| 1000 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 1001 | `oneclickvpnkeys` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1002 | `tanhanet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1003 | `141.193.27.4` | vless | US | ip-literal | 是 | mmdb 命中 141.193.27.4 -> US |
| 1004 | `MDvpnSEC` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1005 | `146.75.59.186` | vless | US | ip-literal | 是 | mmdb 命中 146.75.59.186 -> US |
| 1006 | `151.101.1.57` | vless | US | ip-literal | 是 | mmdb 命中 151.101.1.57 -> US |
| 1007 | `151.101.109.223` | vless | US | ip-literal | 是 | mmdb 命中 151.101.109.223 -> US |
| 1008 | `151.101.110.219` | trojan | US | ip-literal | 是 | mmdb 命中 151.101.110.219 -> US |
| 1009 | `151.101.129.57` | vless | US | ip-literal | 是 | mmdb 命中 151.101.129.57 -> US |
| 1010 | `151.101.2.219` | vless | US | ip-literal | 是 | mmdb 命中 151.101.2.219 -> US |
| 1011 | `Tarkshodeh` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1012 | `162.159.130.234` | vless | US | ip-literal | 是 | mmdb 命中 162.159.130.234 -> US |
| 1013 | `v2rayng3` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1014 | `162.159.198.1` | vless | US | ip-literal | 是 | mmdb 命中 162.159.198.1 -> US |
| 1015 | `162.159.24.39` | vless | US | ip-literal | 是 | mmdb 命中 162.159.24.39 -> US |
| 1016 | `v2rayngsupbot` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1017 | `162.159.3.176` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.3.176 -> US |
| 1018 | `162.159.43.187` | vless | US | ip-literal | 是 | mmdb 命中 162.159.43.187 -> US |
| 1019 | `162.159.60.167` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.60.167 -> US |
| 1020 | `162.159.91.211` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.91.211 -> US |
| 1021 | `164.38.155.135` | vless | GB | ip-literal | 否 | mmdb 命中 164.38.155.135 -> GB |
| 1022 | `pirozi_ArGaP` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1023 | `Fear_Config---&security=tls&encryption=none&extra={` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1024 | `167.82.64.7` | vless | US | ip-literal | 是 | mmdb 命中 167.82.64.7 -> US |
| 1025 | `167.82.76.31` | vless | US | ip-literal | 是 | mmdb 命中 167.82.76.31 -> US |
| 1026 | `167.82.79.164` | vless | US | ip-literal | 是 | mmdb 命中 167.82.79.164 -> US |
| 1027 | `172.64.144.198` | vless | US | ip-literal | 是 | mmdb 命中 172.64.144.198 -> US |
| 1028 | `172.64.149.54` | vless | US | ip-literal | 是 | mmdb 命中 172.64.149.54 -> US |
| 1029 | `172.64.157.230` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.157.230 -> US |
| 1030 | `172.64.159.64` | vless | US | ip-literal | 是 | mmdb 命中 172.64.159.64 -> US |
| 1031 | `172.64.229.114` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.229.114 -> US |
| 1032 | `172.64.52.230` | vless | US | ip-literal | 是 | mmdb 命中 172.64.52.230 -> US |
| 1033 | `172.64.53.74` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.53.74 -> US |
| 1034 | `172.64.86.167` | vless | US | ip-literal | 是 | mmdb 命中 172.64.86.167 -> US |
| 1035 | `172.65.90.52` | vless | US | ip-literal | 是 | mmdb 命中 172.65.90.52 -> US |
| 1036 | `172.66.214.247` | vless | US | ip-literal | 是 | mmdb 命中 172.66.214.247 -> US |
| 1037 | `172.67.143.56` | vless | US | ip-literal | 是 | mmdb 命中 172.67.143.56 -> US |
| 1038 | `172.67.149.60` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.149.60 -> US |
| 1039 | `172.67.155.199` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.155.199 -> US |
| 1040 | `172.67.155.65` | vless | US | ip-literal | 是 | mmdb 命中 172.67.155.65 -> US |
| 1041 | `172.67.158.89` | vless | US | ip-literal | 是 | mmdb 命中 172.67.158.89 -> US |
| 1042 | `V2rayNPVTConfig` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1043 | `172.67.204.84` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.204.84 -> US |
| 1044 | `172.67.208.1` | vless | US | ip-literal | 是 | mmdb 命中 172.67.208.1 -> US |
| 1045 | `172.67.209.127` | vless | US | ip-literal | 是 | mmdb 命中 172.67.209.127 -> US |
| 1046 | `172.67.213.218` | vless | US | ip-literal | 是 | mmdb 命中 172.67.213.218 -> US |
| 1047 | `hopev2ray💯` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1048 | `Azarakhsh_Proxy+🩷` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1049 | `173.245.49.157` | vless | US | ip-literal | 是 | mmdb 命中 173.245.49.157 -> US |
| 1050 | `ai_duet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1051 | `cephalon_ala` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1052 | `Hope_Net-join-us-on-Telegram` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1053 | `185.146.173.58` | vless | SE | ip-literal | 否 | mmdb 命中 185.146.173.58 -> SE |
| 1054 | `JavidnamanIran` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1055 | `185.18.250.245` | trojan | CH | ip-literal | 否 | mmdb 命中 185.18.250.245 -> CH |
| 1056 | `188.114.96.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.3 -> US |
| 1057 | `188.114.96.37` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.37 -> US |
| 1058 | `188.114.97.2` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.2 -> US |
| 1059 | `leviconfigs🪐-10` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1060 | `188.114.97.4` | trojan | US | ip-literal | 是 | mmdb 命中 188.114.97.4 -> US |
| 1061 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1062 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1063 | `188.114.98.0` | vless | US | ip-literal | 是 | mmdb 命中 188.114.98.0 -> US |
| 1064 | `v2ray313` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1065 | `192.0.54.181` | vless | US | ip-literal | 是 | mmdb 命中 192.0.54.181 -> US |
| 1066 | `Shh_Proxy-New¹⁰` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1067 | `199.232.20.113` | vless | US | ip-literal | 是 | mmdb 命中 199.232.20.113 -> US |
| 1068 | `Alfred_Config` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1069 | `CloudVPNchannel&security=tls&encryption=none&extra={` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1070 | `199.232.245.94` | vless | US | ip-literal | 是 | mmdb 命中 199.232.245.94 -> US |
| 1071 | `199.232.77.215` | vless | US | ip-literal | 是 | mmdb 命中 199.232.77.215 -> US |
| 1072 | `sora1co` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1073 | `prrofile_purple` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1074 | `199.232.78.150` | vless | US | ip-literal | 是 | mmdb 命中 199.232.78.150 -> US |
| 1075 | `configprxy` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1076 | `leviconfigs🪐-2` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1077 | `hopev2ray❤️‍🔥` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1078 | `208.103.161.5` | vless | US | ip-literal | 是 | mmdb 命中 208.103.161.5 -> US |
| 1079 | `ConfigV2RayNG` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1080 | `23.227.38.11` | trojan | CA | ip-literal | 否 | mmdb 命中 23.227.38.11 -> CA |
| 1081 | `27.50.48.6` | vless | SG | ip-literal | 否 | mmdb 命中 27.50.48.6 -> SG |
| 1082 | `daredevil_404&security=tls&encryption=mlkem768x25519plus.random.0rtt.H4TEngoua4IvSuVQm_V-eUtsc1ZWzAyp47V-OJqFjcdJbRw56QiP3-JTtphA3iR7JfpNKWu9szw2gsu_sKR0xeVZTTZ8uGYADlwN82cqYCY_gqCFCpe4VWA_nkTDioJtc8Na1Fxg8BMe3JGY5yIC9Sdjjgo8Bqtg5eBkP7UX6YLLGlySAJKYT8hbTKTAhfEZQYnN4BySxowU46PCWasPBqkgSLvI_0QuGOtR0Uo2HrCufroBU9o0Iok8b4SIpMoCv4shPhTEo-CCOFiEQJEM9skBN9du7bMR3TLE1MB4SPNQASkIAEirTIa4xZBOwFrF8Pg9EBV8MWJq2fsVjbqRFyQt87VbY3MZyvCKsiokOOR2DyWIejKXPude-AE8IvJfnhITCoRtpHIS48toDYQ07zpVYoqRCCUKhLAEdmdIFSbGQbE9EBwSBfSmmeVPrruT0OrIMIQYRXo58jZWuJaGTekgSCZ77MxRE5SDzbamFDQvRkUmDypaLYjKh5FBnzduzXHJfKB61iWCHgeTVseyXVCSRBRVxHSC0PXAt2Wh_AmEAG26JcTNelm6NuIqPzk8sipqd3gxLOKtiDCAw4UftWwKfEgyWajALRxJYJDDTAi2UTygohMZ8_lpKstfKvkeZqXPFYw30lxDXfXJZ-aDZciTt1kV7sdNooKYEXJg9cOHQIdGIcaI6nq8_9Iln3SKnJMxKqzK-ElMDzysekOZ84ybqhFcWHaDu7J_rfp0bNlcyubDaQAjHtFdB5FTKzZcxJGAGhS0LHd4ABQS_Xe42iGQGbkh37O0LUK6rLlzRiF7ITAcbDOsN-OBUvpCFRa1OfOoWtMCuel_UQIgmHJwPrYH7tp4CzM_LsSDIUEqxhsvBPMAOujDYVNk-coGJaWtRmFK79KwYotiJUu1S3KAT9E94VIuLaQYDDQlwPidxVMbLEpefJEU1QgbkRAtBmAvIBMgnoEKEJEj6AoMZ3o1RroKzHOBH2pun8YRVMKgotSHtyOfWfBVjpy7_qyuQOFj4LdsCKAjEHIuGlpPNMyB8fXNkEyxI1Y6whVd1bqejQJPEOUED-RZA7jGr3JuTaJE_oi08HcenfyP4rESRZY8W6MxZTSnpimJx1lbzePBBIJYf_F298sOYfGqQ3otzTNFOWA_gGaqAisN0ibAOPa98MOtx_xtHrSMfgW-h5KnOVaE0OKRFcMX7-l7jYZ4dtl6YyYQBmMP8uh2nCFdH8B-gMYXncQSBpvJNegv3NqZIZFkW2c9ShCO79Z0FQB9kqA5KJukeobOs2W21pSG2kI6guFZZbtMgXaLmCYM85a1nKuvwRMdLUQEtmJbtOWyxpovqwDE7kiKwgKFUMCvJ1B4o9Je2xZ6zmdnlpmWDKkZEjcTKYwoQRwZh5pZDSsl6YcwbBE0zowBOgsHFpIc4gwqyBp2NLS-9ciTf0NdALGRDdZRr8GkfOUYQ6tlQstzFaqLh0VRiVGGE0BL-tJmGEeUd9iF7hJTsMN7vEQDpftABBN4ZUNGWli22XZxRDIUo1NJ05L8j4oSuULGbBjA8jhXNdBI_XE1SXoXdocbtybkz00&extra={` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1083 | `45.130.125.112` | trojan | SC | ip-literal | 否 | mmdb 命中 45.130.125.112 -> SC |
| 1084 | `45.130.125.126` | vless | SC | ip-literal | 否 | mmdb 命中 45.130.125.126 -> SC |
| 1085 | `45.130.125.201` | vless | SC | ip-literal | 否 | mmdb 命中 45.130.125.201 -> SC |
| 1086 | `𝐓𝐮𝐧𝐧𝐞𝐥𝐜𝐫𝟕🇩🇪` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1087 | `45.130.125.66` | vless | SC | ip-literal | 否 | mmdb 命中 45.130.125.66 -> SC |
| 1088 | `45.130.125.75` | trojan | SC | ip-literal | 否 | mmdb 命中 45.130.125.75 -> SC |
| 1089 | `confiig_hub` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1090 | `69.46.46.106` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.106 -> US |
| 1091 | `69.46.46.109` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.109 -> US |
| 1092 | `69.46.46.113` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.113 -> US |
| 1093 | `69.46.46.114` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.114 -> US |
| 1094 | `69.46.46.121` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.121 -> US |
| 1095 | `69.46.46.142` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.142 -> US |
| 1096 | `69.46.46.144` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.144 -> US |
| 1097 | `8.6.112.6` | vless | US | ip-literal | 是 | mmdb 命中 8.6.112.6 -> US |
| 1098 | `V2rayng_market_1378_bot` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1099 | `DemonVpn🔻` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1100 | `103.133.1.160` | vless | US | ip-literal | 是 | mmdb 命中 103.133.1.160 -> US |
| 1101 | `104.16.10.104` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.104 -> US |
| 1102 | `104.16.10.121` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.121 -> US |
| 1103 | `Shh_Proxy-New⁷` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1104 | `Shh_Proxy-New⁸` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1105 | `104.16.10.9` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.9 -> US |
| 1106 | `104.16.107.139` | vless | US | ip-literal | 是 | mmdb 命中 104.16.107.139 -> US |
| 1107 | `pPal03🙃Join🙃` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1108 | `104.16.171.121` | vless | US | ip-literal | 是 | mmdb 命中 104.16.171.121 -> US |
| 1109 | `104.16.174.117` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.117 -> US |
| 1110 | `104.16.174.12` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.12 -> US |
| 1111 | `104.16.174.124` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.124 -> US |
| 1112 | `104.16.174.143` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.143 -> US |
| 1113 | `104.16.174.148` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.148 -> US |
| 1114 | `104.16.174.185` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.185 -> US |
| 1115 | `104.16.174.44` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.44 -> US |
| 1116 | `104.16.174.46` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.174.46 -> US |
| 1117 | `104.16.174.81` | vless | US | ip-literal | 是 | mmdb 命中 104.16.174.81 -> US |
| 1118 | `104.16.183.101` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.183.101 -> US |
| 1119 | `104.16.183.83` | vless | US | ip-literal | 是 | mmdb 命中 104.16.183.83 -> US |
| 1120 | `104.16.184.194` | vless | US | ip-literal | 是 | mmdb 命中 104.16.184.194 -> US |
| 1121 | `104.16.19.242` | vless | US | ip-literal | 是 | mmdb 命中 104.16.19.242 -> US |
| 1122 | `104.16.203.166` | vless | US | ip-literal | 是 | mmdb 命中 104.16.203.166 -> US |
| 1123 | `104.16.209.187` | vless | US | ip-literal | 是 | mmdb 命中 104.16.209.187 -> US |
| 1124 | `104.16.214.14` | vless | US | ip-literal | 是 | mmdb 命中 104.16.214.14 -> US |
| 1125 | `104.16.233.169` | vless | US | ip-literal | 是 | mmdb 命中 104.16.233.169 -> US |
| 1126 | `104.16.241.253` | vless | US | ip-literal | 是 | mmdb 命中 104.16.241.253 -> US |
| 1127 | `104.16.7.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.7.70 -> US |
| 1128 | `104.16.7.70` | vless | US | ip-literal | 是 | mmdb 命中 104.16.7.70 -> US |
| 1129 | `104.16.71.213` | trojan | US | ip-literal | 是 | mmdb 命中 104.16.71.213 -> US |
| 1130 | `104.16.8.237` | vless | US | ip-literal | 是 | mmdb 命中 104.16.8.237 -> US |
| 1131 | `104.16.80.73` | vless | US | ip-literal | 是 | mmdb 命中 104.16.80.73 -> US |
| 1132 | `104.17.107.134` | vless | US | ip-literal | 是 | mmdb 命中 104.17.107.134 -> US |
| 1133 | `Vpn_Mafia` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1134 | `104.17.121.43` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.121.43 -> US |
| 1135 | `104.17.121.71` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.121.71 -> US |
| 1136 | `104.17.148.111` | vless | US | ip-literal | 是 | mmdb 命中 104.17.148.111 -> US |
| 1137 | `104.17.161.24` | vless | US | ip-literal | 是 | mmdb 命中 104.17.161.24 -> US |
| 1138 | `104.17.177.143` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.177.143 -> US |
| 1139 | `104.17.23.106` | vless | US | ip-literal | 是 | mmdb 命中 104.17.23.106 -> US |
| 1140 | `104.17.26.230` | vless | US | ip-literal | 是 | mmdb 命中 104.17.26.230 -> US |
| 1141 | `104.18.11.110` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.11.110 -> US |
| 1142 | `104.18.12.149` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.12.149 -> US |
| 1143 | `104.18.15.19` | vless | US | ip-literal | 是 | mmdb 命中 104.18.15.19 -> US |
| 1144 | `104.18.151.172` | vless | US | ip-literal | 是 | mmdb 命中 104.18.151.172 -> US |
| 1145 | `v2ray_configs_pools` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1146 | `104.18.152.113` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.113 -> US |
| 1147 | `104.18.152.144` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.144 -> US |
| 1148 | `104.18.152.149` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.149 -> US |
| 1149 | `104.18.152.155` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.155 -> US |
| 1150 | `104.18.152.159` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.159 -> US |
| 1151 | `104.18.152.187` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.187 -> US |
| 1152 | `104.18.152.208` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.208 -> US |
| 1153 | `104.18.152.219` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.219 -> US |
| 1154 | `104.18.152.229` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.229 -> US |
| 1155 | `104.18.152.233` | vless | US | ip-literal | 是 | mmdb 命中 104.18.152.233 -> US |
| 1156 | `104.18.152.244` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.244 -> US |
| 1157 | `104.18.152.77` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.152.77 -> US |
| 1158 | `104.18.26.90` | vless | US | ip-literal | 是 | mmdb 命中 104.18.26.90 -> US |
| 1159 | `104.18.28.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.28.234 -> US |
| 1160 | `104.18.33.162` | vless | US | ip-literal | 是 | mmdb 命中 104.18.33.162 -> US |
| 1161 | `104.18.35.86` | vless | US | ip-literal | 是 | mmdb 命中 104.18.35.86 -> US |
| 1162 | `104.18.39.91` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.39.91 -> US |
| 1163 | `104.18.4.138` | vless | US | ip-literal | 是 | mmdb 命中 104.18.4.138 -> US |
| 1164 | `104.18.43.29` | trojan | US | ip-literal | 是 | mmdb 命中 104.18.43.29 -> US |
| 1165 | `104.18.46.234` | vless | US | ip-literal | 是 | mmdb 命中 104.18.46.234 -> US |
| 1166 | `104.19.141.129` | vless | US | ip-literal | 是 | mmdb 命中 104.19.141.129 -> US |
| 1167 | `104.19.144.99` | vless | US | ip-literal | 是 | mmdb 命中 104.19.144.99 -> US |
| 1168 | `104.19.214.98` | vless | US | ip-literal | 是 | mmdb 命中 104.19.214.98 -> US |
| 1169 | `104.19.229.21` | trojan | US | ip-literal | 是 | mmdb 命中 104.19.229.21 -> US |
| 1170 | `Tanhanet` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1171 | `104.19.64.105` | trojan | US | ip-literal | 是 | mmdb 命中 104.19.64.105 -> US |
| 1172 | `proSSH` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1173 | `104.20.6.134` | vless | US | ip-literal | 是 | mmdb 命中 104.20.6.134 -> US |
| 1174 | `104.21.12.87` | trojan | US | ip-literal | 是 | mmdb 命中 104.21.12.87 -> US |
| 1175 | `104.21.23.29` | vless | US | ip-literal | 是 | mmdb 命中 104.21.23.29 -> US |
| 1176 | `104.21.236.63` | vless | US | ip-literal | 是 | mmdb 命中 104.21.236.63 -> US |
| 1177 | `104.21.32.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.32.1 -> US |
| 1178 | `104.21.38.220` | vless | US | ip-literal | 是 | mmdb 命中 104.21.38.220 -> US |
| 1179 | `104.21.38.220` | vless | US | ip-literal | 是 | mmdb 命中 104.21.38.220 -> US |
| 1180 | `104.21.48.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.48.1 -> US |
| 1181 | `hopev2ray💕` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1182 | `104.21.60.109` | vless | US | ip-literal | 是 | mmdb 命中 104.21.60.109 -> US |
| 1183 | `Fear_Config---&security=tls&alpn=h3,h2,http` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1184 | `104.21.63.28` | vless | US | ip-literal | 是 | mmdb 命中 104.21.63.28 -> US |
| 1185 | `104.21.64.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.64.1 -> US |
| 1186 | `GozargahAzad&allowInsecure=1&alpn=http` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1187 | `104.21.70.21` | vless | US | ip-literal | 是 | mmdb 命中 104.21.70.21 -> US |
| 1188 | `104.21.74.8` | vless | US | ip-literal | 是 | mmdb 命中 104.21.74.8 -> US |
| 1189 | `Tarkahodeh` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1190 | `104.21.80.1` | vless | US | ip-literal | 是 | mmdb 命中 104.21.80.1 -> US |
| 1191 | `104.21.80.209` | vless | US | ip-literal | 是 | mmdb 命中 104.21.80.209 -> US |
| 1192 | `104.21.89.181` | vless | US | ip-literal | 是 | mmdb 命中 104.21.89.181 -> US |
| 1193 | `104.21.91.244` | vless | US | ip-literal | 是 | mmdb 命中 104.21.91.244 -> US |
| 1194 | `104.24.140.39` | vless | US | ip-literal | 是 | mmdb 命中 104.24.140.39 -> US |
| 1195 | `104.24.167.96` | vless | US | ip-literal | 是 | mmdb 命中 104.24.167.96 -> US |
| 1196 | `104.24.172.153` | vless | US | ip-literal | 是 | mmdb 命中 104.24.172.153 -> US |
| 1197 | `104.24.189.102` | vless | US | ip-literal | 是 | mmdb 命中 104.24.189.102 -> US |
| 1198 | `Fear_Config---&security=tls&encryption=none&insecure=0&host=fs.qicai99.com&type=ws&allowInsecure=0&sni=fs.qicai99.com` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1199 | `104.24.196.67` | vless | US | ip-literal | 是 | mmdb 命中 104.24.196.67 -> US |
| 1200 | `104.24.198.111` | vless | US | ip-literal | 是 | mmdb 命中 104.24.198.111 -> US |
| 1201 | `104.24.218.13` | vless | US | ip-literal | 是 | mmdb 命中 104.24.218.13 -> US |
| 1202 | `104.24.219.162` | vless | US | ip-literal | 是 | mmdb 命中 104.24.219.162 -> US |
| 1203 | `104.24.247.189` | vless | US | ip-literal | 是 | mmdb 命中 104.24.247.189 -> US |
| 1204 | `104.24.52.41` | vless | US | ip-literal | 是 | mmdb 命中 104.24.52.41 -> US |
| 1205 | `104.24.66.98` | vless | US | ip-literal | 是 | mmdb 命中 104.24.66.98 -> US |
| 1206 | `104.24.87.230` | vless | US | ip-literal | 是 | mmdb 命中 104.24.87.230 -> US |
| 1207 | `104.24.91.178` | vless | US | ip-literal | 是 | mmdb 命中 104.24.91.178 -> US |
| 1208 | `104.25.0.1` | vless | US | ip-literal | 是 | mmdb 命中 104.25.0.1 -> US |
| 1209 | `104.25.122.72` | vless | US | ip-literal | 是 | mmdb 命中 104.25.122.72 -> US |
| 1210 | `104.26.0.32` | vless | US | ip-literal | 是 | mmdb 命中 104.26.0.32 -> US |
| 1211 | `leviconfigs🪐-23` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1212 | `104.26.13.31` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.31 -> US |
| 1213 | `104.26.13.40` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.40 -> US |
| 1214 | `104.26.13.54` | vless | US | ip-literal | 是 | mmdb 命中 104.26.13.54 -> US |
| 1215 | `leviconfigs🪐-22` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1216 | `104.26.15.137` | trojan | US | ip-literal | 是 | mmdb 命中 104.26.15.137 -> US |
| 1217 | `104.26.4.57` | vless | US | ip-literal | 是 | mmdb 命中 104.26.4.57 -> US |
| 1218 | `104.27.88.172` | vless | US | ip-literal | 是 | mmdb 命中 104.27.88.172 -> US |
| 1219 | `soskeynets` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1220 | `hopev2ray💛` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1221 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 1222 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 1223 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 1224 | `108.162.198.178` | vless | US | ip-literal | 是 | mmdb 命中 108.162.198.178 -> US |
| 1225 | `141.101.90.101` | trojan | US | ip-literal | 是 | mmdb 命中 141.101.90.101 -> US |
| 1226 | `15.204.210.176` | trojan | US | ip-literal | 是 | mmdb 命中 15.204.210.176 -> US |
| 1227 | `151.101.36.88` | vless | US | ip-literal | 是 | mmdb 命中 151.101.36.88 -> US |
| 1228 | `probabblynot-mci4` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1229 | `159.246.55.251` | vless | US | ip-literal | 是 | mmdb 命中 159.246.55.251 -> US |
| 1230 | `162.159.12.212` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.12.212 -> US |
| 1231 | `162.159.15.39` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.15.39 -> US |
| 1232 | `162.159.153.4` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.153.4 -> US |
| 1233 | `162.159.156.214` | vless | US | ip-literal | 是 | mmdb 命中 162.159.156.214 -> US |
| 1234 | `162.159.253.41` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.253.41 -> US |
| 1235 | `162.159.39.153` | trojan | US | ip-literal | 是 | mmdb 命中 162.159.39.153 -> US |
| 1236 | `162.159.42.163` | vless | US | ip-literal | 是 | mmdb 命中 162.159.42.163 -> US |
| 1237 | `162.159.46.0` | vless | US | ip-literal | 是 | mmdb 命中 162.159.46.0 -> US |
| 1238 | `165.215.250.14` | trojan | US | ip-literal | 是 | mmdb 命中 165.215.250.14 -> US |
| 1239 | `167.68.4.199` | trojan | US | ip-literal | 是 | mmdb 命中 167.68.4.199 -> US |
| 1240 | `172.64.148.165` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.148.165 -> US |
| 1241 | `172.64.148.248` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.148.248 -> US |
| 1242 | `ATLAS_V2VPN🆓️📶🛰️684🌐🆕` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1243 | `172.64.150.28` | vless | US | ip-literal | 是 | mmdb 命中 172.64.150.28 -> US |
| 1244 | `172.64.153.100` | vless | US | ip-literal | 是 | mmdb 命中 172.64.153.100 -> US |
| 1245 | `172.64.153.105` | vless | US | ip-literal | 是 | mmdb 命中 172.64.153.105 -> US |
| 1246 | `172.64.154.113` | vless | US | ip-literal | 是 | mmdb 命中 172.64.154.113 -> US |
| 1247 | `172.64.154.8` | vless | US | ip-literal | 是 | mmdb 命中 172.64.154.8 -> US |
| 1248 | `mehrosaboran` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1249 | `172.64.38.50` | trojan | US | ip-literal | 是 | mmdb 命中 172.64.38.50 -> US |
| 1250 | `172.64.88.168` | vless | US | ip-literal | 是 | mmdb 命中 172.64.88.168 -> US |
| 1251 | `172.64.88.251` | vless | US | ip-literal | 是 | mmdb 命中 172.64.88.251 -> US |
| 1252 | `172.64.92.243` | vless | US | ip-literal | 是 | mmdb 命中 172.64.92.243 -> US |
| 1253 | `172.66.140.62` | vless | US | ip-literal | 是 | mmdb 命中 172.66.140.62 -> US |
| 1254 | `172.66.170.53` | vless | US | ip-literal | 是 | mmdb 命中 172.66.170.53 -> US |
| 1255 | `172.66.40.99` | vless | US | ip-literal | 是 | mmdb 命中 172.66.40.99 -> US |
| 1256 | `172.67.131.125` | vless | US | ip-literal | 是 | mmdb 命中 172.67.131.125 -> US |
| 1257 | `172.67.139.85` | vless | US | ip-literal | 是 | mmdb 命中 172.67.139.85 -> US |
| 1258 | `172.67.139.85` | vless | US | ip-literal | 是 | mmdb 命中 172.67.139.85 -> US |
| 1259 | `172.67.148.163` | vless | US | ip-literal | 是 | mmdb 命中 172.67.148.163 -> US |
| 1260 | `AZARBAYJAB1)` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1261 | `172.67.172.95` | vless | US | ip-literal | 是 | mmdb 命中 172.67.172.95 -> US |
| 1262 | `172.67.208.118` | vless | US | ip-literal | 是 | mmdb 命中 172.67.208.118 -> US |
| 1263 | `172.67.68.248` | vless | US | ip-literal | 是 | mmdb 命中 172.67.68.248 -> US |
| 1264 | `leviconfigs🪐-3` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1265 | `172.67.74.10` | vless | US | ip-literal | 是 | mmdb 命中 172.67.74.10 -> US |
| 1266 | `Fear_Config---&security=tls&encryption=none&insecure=0&host=fs.qicai99.com&fp=chrome&type=ws&allowInsecure=0&sni=fs.qicai99.com` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1267 | `172.67.74.2` | trojan | US | ip-literal | 是 | mmdb 命中 172.67.74.2 -> US |
| 1268 | `173.245.49.114` | vless | US | ip-literal | 是 | mmdb 命中 173.245.49.114 -> US |
| 1269 | `173.245.58.183` | trojan | US | ip-literal | 是 | mmdb 命中 173.245.58.183 -> US |
| 1270 | `185.18.250.127` | vless | CH | ip-literal | 否 | mmdb 命中 185.18.250.127 -> CH |
| 1271 | `188.114.96.3` | vless | US | ip-literal | 是 | mmdb 命中 188.114.96.3 -> US |
| 1272 | `162.35.38.156` | vless | US | ip-literal | 是 | mmdb 命中 162.35.38.156 -> US |
| 1273 | `sclass-b1.catcat321.com` | trojan | DE | domain-resolved | 否 | 解析到 217.217.222.230 -> DE |
| 1274 | `sclass-b1.catcat321.com` | trojan | DE | domain-resolved | 否 | 解析到 217.217.222.230 -> DE |
| 1275 | `zfapi.zalolink.com` | vless | JP | domain-resolved | 否 | 解析到 3.115.11.119 -> JP |
| 1276 | `,` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1277 | `your-proxy-link...` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1278 | `vp3.yysyy.online` | hysteria2 | JP | domain-resolved | 否 | 解析到 45.32.10.7 -> JP |
| 1279 | `138.3.208.26` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 138.3.208.26 -> JP |
| 1280 | `freedom.chenlan.top` | hysteria2 | JP | domain-resolved | 否 | 解析到 85.121.123.197 -> JP |
| 1281 | `103.115.109.49` | hysteria2 | TW | ip-literal | 否 | mmdb 命中 103.115.109.49 -> TW |
| 1282 | `45.32.10.7` | hysteria2 | JP | ip-literal | 否 | mmdb 命中 45.32.10.7 -> JP |
| 1283 | `163.192.14.135` | hysteria2 | US | ip-literal | 是 | mmdb 命中 163.192.14.135 -> US |
| 1284 | `155.248.209.237` | hysteria2 | US | ip-literal | 是 | mmdb 命中 155.248.209.237 -> US |
| 1285 | `us.mi11o4ka.com` | hysteria2 | US | domain-resolved | 是 | 解析到 167.148.201.99 -> US |
| 1286 | `149.28.130.108` | trojan | SG | ip-literal | 否 | mmdb 命中 149.28.130.108 -> SG |
| 1287 | `139.180.146.200` | trojan | SG | ip-literal | 否 | mmdb 命中 139.180.146.200 -> SG |
| 1288 | `45.76.98.127` | vless | JP | ip-literal | 否 | mmdb 命中 45.76.98.127 -> JP |
| 1289 | `ga1data.xyy123.bid` | vless | JP | domain-resolved | 否 | 解析到 103.232.213.114 -> JP |
| 1290 | `104.19.164.155` | vless | US | ip-literal | 是 | mmdb 命中 104.19.164.155 -> US |
| 1291 | `165.154.63.139` | vless | HK | ip-literal | 否 | mmdb 命中 165.154.63.139 -> HK |
| 1292 | `support.zoom.us` | vless | US | domain-resolved | 是 | 解析到 170.114.46.6 -> US |
| 1293 | `172.237.88.103` | vless | SG | ip-literal | 否 | mmdb 命中 172.237.88.103 -> SG |
| 1294 | `18.183.215.124` | vless | JP | ip-literal | 否 | mmdb 命中 18.183.215.124 -> JP |
| 1295 | `3.39.4.109` | vless | KR | ip-literal | 否 | mmdb 命中 3.39.4.109 -> KR |
| 1296 | `54.169.200.246` | vless | SG | ip-literal | 否 | mmdb 命中 54.169.200.246 -> SG |
| 1297 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1298 | `45.32.52.173` | trojan | JP | ip-literal | 否 | mmdb 命中 45.32.52.173 -> JP |
| 1299 | `kr002.zestapp778.com` | trojan | KR | domain-resolved | 否 | 解析到 141.164.63.80 -> KR |
| 1300 | `in002.zestapp778.com` | trojan | IN | domain-resolved | 否 | 解析到 139.84.139.150 -> IN |
| 1301 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1302 | `188.114.98.0` | vless | US | ip-literal | 是 | mmdb 命中 188.114.98.0 -> US |
| 1303 | `104.19.12.94` | vless | US | ip-literal | 是 | mmdb 命中 104.19.12.94 -> US |
| 1304 | `3.114.220.22` | vless | JP | ip-literal | 否 | mmdb 命中 3.114.220.22 -> JP |
| 1305 | `134.185.81.5` | vless | SG | ip-literal | 否 | mmdb 命中 134.185.81.5 -> SG |
| 1306 | `3.39.4.109` | vless | KR | ip-literal | 否 | mmdb 命中 3.39.4.109 -> KR |
| 1307 | `n04.jinggai.online` | vless | US | domain-resolved | 是 | 解析到 104.21.11.38 -> US |
| 1308 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1309 | `54.251.9.130` | vless | SG | ip-literal | 否 | mmdb 命中 54.251.9.130 -> SG |
| 1310 | `170.114.45.6` | vless | US | ip-literal | 是 | mmdb 命中 170.114.45.6 -> US |
| 1311 | `151.245.106.49` | vless | KR | ip-literal | 否 | mmdb 命中 151.245.106.49 -> KR |
| 1312 | `45.76.172.197` | vless | US | ip-literal | 是 | mmdb 命中 45.76.172.197 -> US |
| 1313 | `104.17.50.227` | vless | US | ip-literal | 是 | mmdb 命中 104.17.50.227 -> US |
| 1314 | `129.213.91.185` | hysteria2 | US | ip-literal | 是 | mmdb 命中 129.213.91.185 -> US |
| 1315 | `43.167.186.78` | trojan | JP | ip-literal | 否 | mmdb 命中 43.167.186.78 -> JP |
| 1316 | `216.238.80.100` | trojan | MX | ip-literal | 否 | mmdb 命中 216.238.80.100 -> MX |
| 1317 | `45.132.75.213` | vless | SG | ip-literal | 否 | mmdb 命中 45.132.75.213 -> SG |
| 1318 | `206.206.76.75` | vless | SG | ip-literal | 否 | mmdb 命中 206.206.76.75 -> SG |
| 1319 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1320 | `3.0.111.82` | vless | SG | ip-literal | 否 | mmdb 命中 3.0.111.82 -> SG |
| 1321 | `45.32.69.110` | vless | US | ip-literal | 是 | mmdb 命中 45.32.69.110 -> US |
| 1322 | `51.81.203.63` | vless | US | ip-literal | 是 | mmdb 命中 51.81.203.63 -> US |
| 1323 | `31.172.69.31` | vless | US | ip-literal | 是 | mmdb 命中 31.172.69.31 -> US |
| 1324 | `91.196.33.157` | vless | RU | ip-literal | 否 | mmdb 命中 91.196.33.157 -> RU |
| 1325 | `198.46.146.118` | hysteria2 | US | ip-literal | 是 | mmdb 命中 198.46.146.118 -> US |
| 1326 | `3.64.194.247` | hysteria2 | DE | ip-literal | 否 | mmdb 命中 3.64.194.247 -> DE |
| 1327 | `125.227.86.45` | trojan | TW | ip-literal | 否 | mmdb 命中 125.227.86.45 -> TW |
| 1328 | `66.163.112.121` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.121 -> US |
| 1329 | `us007.zestapp778.com` | trojan | US | domain-resolved | 是 | 解析到 45.63.78.241 -> US |
| 1330 | `104.21.70.21` | vless | US | ip-literal | 是 | mmdb 命中 104.21.70.21 -> US |
| 1331 | `104.16.10.22` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.22 -> US |
| 1332 | `104.18.40.171` | vless | US | ip-literal | 是 | mmdb 命中 104.18.40.171 -> US |
| 1333 | `170.114.46.6` | vless | US | ip-literal | 是 | mmdb 命中 170.114.46.6 -> US |
| 1334 | `188.114.97.6` | vless | US | ip-literal | 是 | mmdb 命中 188.114.97.6 -> US |
| 1335 | `104.17.50.53` | vless | US | ip-literal | 是 | mmdb 命中 104.17.50.53 -> US |
| 1336 | `139.162.27.96` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.27.96 -> SG |
| 1337 | `sg2-8sb.6121999.dpdns.org` | vless | SG | domain-resolved | 否 | 解析到 146.235.16.130 -> SG |
| 1338 | `104.21.6.186` | vless | US | ip-literal | 是 | mmdb 命中 104.21.6.186 -> US |
| 1339 | `154.26.188.52` | vless | US | ip-literal | 是 | mmdb 命中 154.26.188.52 -> US |
| 1340 | `15.204.97.214` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.214 -> US |
| 1341 | `162.159.254.3` | vless | US | ip-literal | 是 | mmdb 命中 162.159.254.3 -> US |
| 1342 | `144.202.126.147` | vless | US | ip-literal | 是 | mmdb 命中 144.202.126.147 -> US |
| 1343 | `5.253.42.164` | vless | CY | ip-literal | 否 | mmdb 命中 5.253.42.164 -> CY |
| 1344 | `185.168.208.190` | vless | US | ip-literal | 是 | mmdb 命中 185.168.208.190 -> US |
| 1345 | `fast.145779.xyz` | vless | US | domain-resolved | 是 | 解析到 104.21.58.37 -> US |
| 1346 | `152.69.200.216` | vless | JP | ip-literal | 否 | mmdb 命中 152.69.200.216 -> JP |
| 1347 | `169.40.42.235` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.235 -> DE |
| 1348 | `169.40.42.104` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.104 -> DE |
| 1349 | `189.74.114.119` | vless | RU | ip-literal | 否 | mmdb 命中 189.74.114.119 -> RU |
| 1350 | `66.70.179.198` | vless | CA | ip-literal | 否 | mmdb 命中 66.70.179.198 -> CA |
| 1351 | `169.40.42.225` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.225 -> DE |
| 1352 | `45.138.100.248` | vless | US | ip-literal | 是 | mmdb 命中 45.138.100.248 -> US |
| 1353 | `31.56.189.208` | vless | DE | ip-literal | 否 | mmdb 命中 31.56.189.208 -> DE |
| 1354 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1355 | `connect.hondamotor.site` | vless | FR | domain-resolved | 否 | 解析到 155.117.5.208 -> FR |
| 1356 | `rb.mangshe.xyz` | hysteria2 | JP | domain-resolved | 否 | 解析到 89.125.244.249 -> JP |
| 1357 | `167.148.201.99` | hysteria2 | US | ip-literal | 是 | mmdb 命中 167.148.201.99 -> US |
| 1358 | `66.163.114.132` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.132 -> US |
| 1359 | `2.27.109.179` | trojan | HK | ip-literal | 否 | mmdb 命中 2.27.109.179 -> HK |
| 1360 | `216.152.147.48` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.48 -> CA |
| 1361 | `104.16.0.1` | vless | US | ip-literal | 是 | mmdb 命中 104.16.0.1 -> US |
| 1362 | `112.169.175.199` | vless | KR | ip-literal | 否 | mmdb 命中 112.169.175.199 -> KR |
| 1363 | `104.16.10.185` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.185 -> US |
| 1364 | `104.16.10.56` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.56 -> US |
| 1365 | `saas.sin.fan` | vless | US | domain-resolved | 是 | 解析到 162.159.135.234 -> US |
| 1366 | `154.31.114.162` | vless | JP | ip-literal | 否 | mmdb 命中 154.31.114.162 -> JP |
| 1367 | `172.67.217.240` | vless | US | ip-literal | 是 | mmdb 命中 172.67.217.240 -> US |
| 1368 | `saas.sin.fan` | vless | US | domain-resolved | 是 | 解析到 162.159.135.234 -> US |
| 1369 | `us1.oh-node.com` | vless | US | domain-resolved | 是 | 解析到 172.233.142.177 -> US |
| 1370 | `162.35.8.62` | vless | US | ip-literal | 是 | mmdb 命中 162.35.8.62 -> US |
| 1371 | `104.16.10.2` | vless | US | ip-literal | 是 | mmdb 命中 104.16.10.2 -> US |
| 1372 | `104.19.48.107` | vless | US | ip-literal | 是 | mmdb 命中 104.19.48.107 -> US |
| 1373 | `15.204.97.219` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.219 -> US |
| 1374 | `103.238.227.211` | vless | HK | ip-literal | 否 | mmdb 命中 103.238.227.211 -> HK |
| 1375 | `45.154.26.63` | vless | TH | ip-literal | 否 | mmdb 命中 45.154.26.63 -> TH |
| 1376 | `103.238.227.211` | vless | HK | ip-literal | 否 | mmdb 命中 103.238.227.211 -> HK |
| 1377 | `526.150333.xyz` | vless | SG | domain-resolved | 否 | 解析到 195.172.138.26 -> SG |
| 1378 | `169.40.42.224` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.224 -> DE |
| 1379 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1380 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1381 | `177.7.51.29` | vless | BR | ip-literal | 否 | mmdb 命中 177.7.51.29 -> BR |
| 1382 | `83.147.232.69` | vless | NL | ip-literal | 否 | mmdb 命中 83.147.232.69 -> NL |
| 1383 | `195.211.98.43` | vless | US | ip-literal | 是 | mmdb 命中 195.211.98.43 -> US |
| 1384 | `193.233.253.180` | vless | RU | ip-literal | 否 | mmdb 命中 193.233.253.180 -> RU |
| 1385 | `104.24.31.89` | vless | US | ip-literal | 是 | mmdb 命中 104.24.31.89 -> US |
| 1386 | `66.163.114.245` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.245 -> US |
| 1387 | `th001.zestapp778.com` | trojan | TH | domain-resolved | 否 | 解析到 38.60.233.126 -> TH |
| 1388 | `66.163.114.114` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.114 -> US |
| 1389 | `66.163.114.166` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.166 -> US |
| 1390 | `66.163.112.76` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.76 -> US |
| 1391 | `66.163.114.106` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.106 -> US |
| 1392 | `www.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.66 -> US |
| 1393 | `66.163.114.126` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.126 -> US |
| 1394 | `216.152.156.65` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.65 -> US |
| 1395 | `216.152.155.59` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.59 -> US |
| 1396 | `216.152.147.93` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.93 -> CA |
| 1397 | `mx001.zestapp778.com` | trojan | MX | domain-resolved | 否 | 解析到 149.104.87.125 -> MX |
| 1398 | `208.69.78.19` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.19 -> CH |
| 1399 | `104.17.210.74` | vless | US | ip-literal | 是 | mmdb 命中 104.17.210.74 -> US |
| 1400 | `104.21.34.106` | vless | US | ip-literal | 是 | mmdb 命中 104.21.34.106 -> US |
| 1401 | `31.76.91.31` | vless | JP | ip-literal | 否 | mmdb 命中 31.76.91.31 -> JP |
| 1402 | `www.speedtest.net` | vless | US | domain-resolved | 是 | 解析到 104.17.148.22 -> US |
| 1403 | `us3.oh-node.com` | vless | US | domain-resolved | 是 | 解析到 167.71.123.252 -> US |
| 1404 | `104.21.0.87` | vless | US | ip-literal | 是 | mmdb 命中 104.21.0.87 -> US |
| 1405 | `5.253.28.224` | vless | CY | ip-literal | 否 | mmdb 命中 5.253.28.224 -> CY |
| 1406 | `45.63.53.81` | vless | US | ip-literal | 是 | mmdb 命中 45.63.53.81 -> US |
| 1407 | `108.61.119.63` | vless | US | ip-literal | 是 | mmdb 命中 108.61.119.63 -> US |
| 1408 | `154.21.203.106` | vless | HK | ip-literal | 否 | mmdb 命中 154.21.203.106 -> HK |
| 1409 | `195.123.235.183` | vless | US | ip-literal | 是 | mmdb 命中 195.123.235.183 -> US |
| 1410 | `5.149.249.94` | vless | NL | ip-literal | 否 | mmdb 命中 5.149.249.94 -> NL |
| 1411 | `connect.wecantos.site` | vless | FR | domain-resolved | 否 | 解析到 155.117.5.208 -> FR |
| 1412 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1413 | `168.222.43.53` | vless | DE | ip-literal | 否 | mmdb 命中 168.222.43.53 -> DE |
| 1414 | `xray1-direct-mci1-fs-ce.freesocks.work` | vless | US | domain-resolved | 是 | 解析到 23.191.200.206 -> US |
| 1415 | `site.teslamotor.site` | vless | DE | domain-resolved | 否 | 解析到 178.83.45.226 -> DE |
| 1416 | `178.83.45.226` | vless | DE | ip-literal | 否 | mmdb 命中 178.83.45.226 -> DE |
| 1417 | `155.117.5.208` | vless | FR | ip-literal | 否 | mmdb 命中 155.117.5.208 -> FR |
| 1418 | `54.71.51.243` | vless | US | ip-literal | 是 | mmdb 命中 54.71.51.243 -> US |
| 1419 | `208.69.78.217` | vless | CH | ip-literal | 否 | mmdb 命中 208.69.78.217 -> CH |
| 1420 | `sg2-xr.zgrelay.com` | vless | - | unknown | 否 | DNS 解析失败或超时 |
| 1421 | `milo.rubinaz.xyz` | vless | FR | domain-resolved | 否 | 解析到 155.117.5.208 -> FR |
| 1422 | `51.77.217.70` | vless | FR | ip-literal | 否 | mmdb 命中 51.77.217.70 -> FR |
| 1423 | `212.227.235.66` | vless | ES | ip-literal | 否 | mmdb 命中 212.227.235.66 -> ES |
| 1424 | `51.89.194.151` | vless | GB | ip-literal | 否 | mmdb 命中 51.89.194.151 -> GB |
| 1425 | `192.142.23.46` | hysteria2 | SE | ip-literal | 否 | mmdb 命中 192.142.23.46 -> SE |
| 1426 | `66.163.112.142` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.142 -> US |
| 1427 | `ca001.zestapp778.com` | trojan | CA | domain-resolved | 否 | 解析到 149.248.50.252 -> CA |
| 1428 | `216.152.155.23` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.23 -> US |
| 1429 | `169.197.140.245` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.245 -> US |
| 1430 | `169.197.140.218` | trojan | US | ip-literal | 是 | mmdb 命中 169.197.140.218 -> US |
| 1431 | `70.34.252.255` | trojan | PL | ip-literal | 否 | mmdb 命中 70.34.252.255 -> PL |
| 1432 | `46.250.250.149` | vless | GB | ip-literal | 否 | mmdb 命中 46.250.250.149 -> GB |
| 1433 | `104.21.70.228` | vless | US | ip-literal | 是 | mmdb 命中 104.21.70.228 -> US |
| 1434 | `46.137.202.178` | vless | SG | ip-literal | 否 | mmdb 命中 46.137.202.178 -> SG |
| 1435 | `43.170.8.95` | vless | SG | ip-literal | 否 | mmdb 命中 43.170.8.95 -> SG |
| 1436 | `172.64.152.52` | vless | US | ip-literal | 是 | mmdb 命中 172.64.152.52 -> US |
| 1437 | `104.18.42.98` | vless | US | ip-literal | 是 | mmdb 命中 104.18.42.98 -> US |
| 1438 | `172.237.88.103` | vless | SG | ip-literal | 否 | mmdb 命中 172.237.88.103 -> SG |
| 1439 | `8.217.1.203` | vless | HK | ip-literal | 否 | mmdb 命中 8.217.1.203 -> HK |
| 1440 | `54.255.211.229` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 54.255.211.229 -> SG |
| 1441 | `est1s.dendi.best` | vless | EE | domain-resolved | 否 | 解析到 217.60.100.223 -> EE |
| 1442 | `217.156.64.64` | vless | MD | ip-literal | 否 | mmdb 命中 217.156.64.64 -> MD |
| 1443 | `38.102.125.3` | vless | CA | ip-literal | 否 | mmdb 命中 38.102.125.3 -> CA |
| 1444 | `201.24.49.215` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.49.215 -> RU |
| 1445 | `217.60.100.222` | vless | EE | ip-literal | 否 | mmdb 命中 217.60.100.222 -> EE |
| 1446 | `178.210.168.254` | vless | TR | ip-literal | 否 | mmdb 命中 178.210.168.254 -> TR |
| 1447 | `217.60.100.223` | vless | EE | ip-literal | 否 | mmdb 命中 217.60.100.223 -> EE |
| 1448 | `31.58.117.133` | hysteria2 | PL | ip-literal | 否 | mmdb 命中 31.58.117.133 -> PL |
| 1449 | `marsh.moltex.click` | vless | RU | domain-resolved | 否 | 解析到 80.242.57.69 -> RU |
| 1450 | `179.43.152.212` | vless | CH | ip-literal | 否 | mmdb 命中 179.43.152.212 -> CH |
| 1451 | `nursery.elvano.website` | vless | RU | domain-resolved | 否 | 解析到 72.56.238.90 -> RU |
| 1452 | `5.129.202.80` | vless | RU | ip-literal | 否 | mmdb 命中 5.129.202.80 -> RU |
| 1453 | `72.56.238.90` | vless | RU | ip-literal | 否 | mmdb 命中 72.56.238.90 -> RU |
| 1454 | `sunfield.moltex.click` | vless | RU | domain-resolved | 否 | 解析到 80.242.57.69 -> RU |
| 1455 | `161.35.37.106` | vless | GB | ip-literal | 否 | mmdb 命中 161.35.37.106 -> GB |
| 1456 | `pigment.merlano.monster` | vless | RU | domain-resolved | 否 | 解析到 5.42.105.128 -> RU |
| 1457 | `104.16.205.65` | vless | US | ip-literal | 是 | mmdb 命中 104.16.205.65 -> US |
| 1458 | `196.196.148.85` | vless | SC | ip-literal | 否 | mmdb 命中 196.196.148.85 -> SC |
| 1459 | `vellum.merlano.monster` | vless | RU | domain-resolved | 否 | 解析到 201.24.122.189 -> RU |
| 1460 | `ws3.falmero.store` | vless | RU | domain-resolved | 否 | 解析到 89.169.44.210 -> RU |
| 1461 | `107.191.58.86` | vless | US | ip-literal | 是 | mmdb 命中 107.191.58.86 -> US |
| 1462 | `172.236.241.130` | vless | US | ip-literal | 是 | mmdb 命中 172.236.241.130 -> US |
| 1463 | `172.235.63.167` | vless | US | ip-literal | 是 | mmdb 命中 172.235.63.167 -> US |
| 1464 | `172.233.129.65` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.65 -> US |
| 1465 | `172.236.227.60` | vless | US | ip-literal | 是 | mmdb 命中 172.236.227.60 -> US |
| 1466 | `172.235.37.168` | vless | US | ip-literal | 是 | mmdb 命中 172.235.37.168 -> US |
| 1467 | `45.32.70.42` | vless | US | ip-literal | 是 | mmdb 命中 45.32.70.42 -> US |
| 1468 | `172.235.48.245` | vless | US | ip-literal | 是 | mmdb 命中 172.235.48.245 -> US |
| 1469 | `172.233.129.172` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.172 -> US |
| 1470 | `172.236.233.130` | vless | US | ip-literal | 是 | mmdb 命中 172.236.233.130 -> US |
| 1471 | `172.233.142.149` | vless | US | ip-literal | 是 | mmdb 命中 172.233.142.149 -> US |
| 1472 | `216.106.186.82` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.82 -> US |
| 1473 | `66.163.112.147` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.147 -> US |
| 1474 | `blog.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.32 -> US |
| 1475 | `66.163.122.30` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.30 -> US |
| 1476 | `sclass-01.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 1477 | `139.162.91.239` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.239 -> JP |
| 1478 | `139.162.125.126` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.125.126 -> JP |
| 1479 | `172.105.203.15` | vless | JP | ip-literal | 否 | mmdb 命中 172.105.203.15 -> JP |
| 1480 | `172.104.86.181` | vless | JP | ip-literal | 否 | mmdb 命中 172.104.86.181 -> JP |
| 1481 | `45.76.222.108` | vless | JP | ip-literal | 否 | mmdb 命中 45.76.222.108 -> JP |
| 1482 | `139.180.221.53` | vless | SG | ip-literal | 否 | mmdb 命中 139.180.221.53 -> SG |
| 1483 | `139.162.20.241` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.20.241 -> SG |
| 1484 | `172.104.48.194` | vless | SG | ip-literal | 否 | mmdb 命中 172.104.48.194 -> SG |
| 1485 | `5.129.202.80` | vless | RU | ip-literal | 否 | mmdb 命中 5.129.202.80 -> RU |
| 1486 | `vellum.merlano.monster` | vless | RU | domain-resolved | 否 | 解析到 201.24.122.189 -> RU |
| 1487 | `ws3.falmero.store` | vless | RU | domain-resolved | 否 | 解析到 89.169.44.210 -> RU |
| 1488 | `107.191.58.86` | vless | US | ip-literal | 是 | mmdb 命中 107.191.58.86 -> US |
| 1489 | `172.236.241.130` | vless | US | ip-literal | 是 | mmdb 命中 172.236.241.130 -> US |
| 1490 | `172.235.63.167` | vless | US | ip-literal | 是 | mmdb 命中 172.235.63.167 -> US |
| 1491 | `172.233.129.65` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.65 -> US |
| 1492 | `66.163.114.106` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.114.106 -> US |
| 1493 | `172.236.227.60` | vless | US | ip-literal | 是 | mmdb 命中 172.236.227.60 -> US |
| 1494 | `172.235.37.168` | vless | US | ip-literal | 是 | mmdb 命中 172.235.37.168 -> US |
| 1495 | `45.32.70.42` | vless | US | ip-literal | 是 | mmdb 命中 45.32.70.42 -> US |
| 1496 | `172.235.48.245` | vless | US | ip-literal | 是 | mmdb 命中 172.235.48.245 -> US |
| 1497 | `172.233.129.172` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.172 -> US |
| 1498 | `172.236.233.130` | vless | US | ip-literal | 是 | mmdb 命中 172.236.233.130 -> US |
| 1499 | `66.163.112.171` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.171 -> US |
| 1500 | `66.163.112.31` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.31 -> US |
| 1501 | `172.233.142.149` | vless | US | ip-literal | 是 | mmdb 命中 172.233.142.149 -> US |
| 1502 | `66.163.112.242` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.242 -> US |
| 1503 | `170.101.101.211` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.211 -> US |
| 1504 | `216.106.186.82` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.82 -> US |
| 1505 | `66.163.112.147` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.112.147 -> US |
| 1506 | `blog.findlocaljobnetworkandbuildcommunityconnections.com` | trojan | US | domain-resolved | 是 | 解析到 216.106.186.32 -> US |
| 1507 | `216.106.186.46` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.46 -> US |
| 1508 | `66.163.122.30` | trojan | US | ip-literal | 是 | mmdb 命中 66.163.122.30 -> US |
| 1509 | `143.246.41.214` | vless | EE | ip-literal | 否 | mmdb 命中 143.246.41.214 -> EE |
| 1510 | `sclass-01.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 1511 | `8.217.1.203` | vless | HK | ip-literal | 否 | mmdb 命中 8.217.1.203 -> HK |
| 1512 | `139.84.231.142` | trojan | ZA | ip-literal | 否 | mmdb 命中 139.84.231.142 -> ZA |
| 1513 | `45.63.30.142` | trojan | AU | ip-literal | 否 | mmdb 命中 45.63.30.142 -> AU |
| 1514 | `158.247.253.243` | trojan | KR | ip-literal | 否 | mmdb 命中 158.247.253.243 -> KR |
| 1515 | `64.176.7.205` | trojan | CL | ip-literal | 否 | mmdb 命中 64.176.7.205 -> CL |
| 1516 | `139.162.91.239` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.239 -> JP |
| 1517 | `139.162.125.126` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.125.126 -> JP |
| 1518 | `172.105.203.15` | vless | JP | ip-literal | 否 | mmdb 命中 172.105.203.15 -> JP |
| 1519 | `172.104.86.181` | vless | JP | ip-literal | 否 | mmdb 命中 172.104.86.181 -> JP |
| 1520 | `45.76.222.108` | vless | JP | ip-literal | 否 | mmdb 命中 45.76.222.108 -> JP |
| 1521 | `139.180.221.53` | vless | SG | ip-literal | 否 | mmdb 命中 139.180.221.53 -> SG |
| 1522 | `139.162.20.241` | vless | SG | ip-literal | 否 | mmdb 命中 139.162.20.241 -> SG |
| 1523 | `172.104.48.194` | vless | SG | ip-literal | 否 | mmdb 命中 172.104.48.194 -> SG |
| 1524 | `xinbulongdong.com` | trojan | JP | domain-resolved | 否 | 解析到 47.245.38.62 -> JP |
| 1525 | `177.202.76.255` | vless | PL | ip-literal | 否 | mmdb 命中 177.202.76.255 -> PL |
| 1526 | `176.108.245.73` | vless | RU | ip-literal | 否 | mmdb 命中 176.108.245.73 -> RU |
| 1527 | `172.67.217.241` | vless | US | ip-literal | 是 | mmdb 命中 172.67.217.241 -> US |
| 1528 | `104.17.145.138` | vless | US | ip-literal | 是 | mmdb 命中 104.17.145.138 -> US |
| 1529 | `172.64.153.109` | vless | US | ip-literal | 是 | mmdb 命中 172.64.153.109 -> US |
| 1530 | `104.18.38.159` | vless | US | ip-literal | 是 | mmdb 命中 104.18.38.159 -> US |
| 1531 | `104.18.14.19` | vless | US | ip-literal | 是 | mmdb 命中 104.18.14.19 -> US |
| 1532 | `104.19.46.190` | vless | US | ip-literal | 是 | mmdb 命中 104.19.46.190 -> US |
| 1533 | `82.139.238.73` | vless | DE | ip-literal | 否 | mmdb 命中 82.139.238.73 -> DE |
| 1534 | `213.145.87.240` | vless | DE | ip-literal | 否 | mmdb 命中 213.145.87.240 -> DE |
| 1535 | `4.232.64.201` | vless | IT | ip-literal | 否 | mmdb 命中 4.232.64.201 -> IT |
| 1536 | `188.213.170.198` | vless | IT | ip-literal | 否 | mmdb 命中 188.213.170.198 -> IT |
| 1537 | `www.visa.com` | vless | US | domain-resolved | 是 | 解析到 104.18.15.19 -> US |
| 1538 | `cf.3666888.xyz` | vless | US | domain-resolved | 是 | 解析到 104.17.188.61 -> US |
| 1539 | `31.56.227.253` | vless | LV | ip-literal | 否 | mmdb 命中 31.56.227.253 -> LV |
| 1540 | `188.164.248.110` | vless | NL | ip-literal | 否 | mmdb 命中 188.164.248.110 -> NL |
| 1541 | `api.ferrin.uk` | vless | NL | domain-resolved | 否 | 解析到 89.41.181.167 -> NL |
| 1542 | `xxx` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1543 | `43.160.197.160` | trojan | SG | ip-literal | 否 | mmdb 命中 43.160.197.160 -> SG |
| 1544 | `18.179.31.199` | trojan | JP | ip-literal | 否 | mmdb 命中 18.179.31.199 -> JP |
| 1545 | `83.229.121.78` | trojan | HK | ip-literal | 否 | mmdb 命中 83.229.121.78 -> HK |
| 1546 | `192.236.151.43` | trojan | US | ip-literal | 是 | mmdb 命中 192.236.151.43 -> US |
| 1547 | `144.31.138.127` | trojan | DE | ip-literal | 否 | mmdb 命中 144.31.138.127 -> DE |
| 1548 | `152.53.228.86` | trojan | DE | ip-literal | 否 | mmdb 命中 152.53.228.86 -> DE |
| 1549 | `64.176.36.61` | trojan | JP | ip-literal | 否 | mmdb 命中 64.176.36.61 -> JP |
| 1550 | `152.53.138.238` | trojan | DE | ip-literal | 否 | mmdb 命中 152.53.138.238 -> DE |
| 1551 | `47.250.84.25` | trojan | MY | ip-literal | 否 | mmdb 命中 47.250.84.25 -> MY |
| 1552 | `sclass-b1.catcat321.com` | trojan | DE | domain-resolved | 否 | 解析到 217.217.222.230 -> DE |
| 1553 | `157.228.172.4` | vless | AE | ip-literal | 否 | mmdb 命中 157.228.172.4 -> AE |
| 1554 | `144.31.215.233` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.233 -> DE |
| 1555 | `144.31.215.244` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.244 -> DE |
| 1556 | `46.243.205.192` | vless | RU | ip-literal | 否 | mmdb 命中 46.243.205.192 -> RU |
| 1557 | `shop.ritmexo.ir` | vless | IR | domain-resolved | 否 | 解析到 78.109.199.222 -> IR |
| 1558 | `13.143.187.220` | vless | US | ip-literal | 是 | mmdb 命中 13.143.187.220 -> US |
| 1559 | `5.249.255.116` | trojan | DK | ip-literal | 否 | mmdb 命中 5.249.255.116 -> DK |
| 1560 | `31.59.169.225` | hysteria2 | AE | ip-literal | 否 | mmdb 命中 31.59.169.225 -> AE |
| 1561 | `47.242.93.89` | trojan | HK | ip-literal | 否 | mmdb 命中 47.242.93.89 -> HK |
| 1562 | `77.67.18.254` | vless | JP | ip-literal | 否 | mmdb 命中 77.67.18.254 -> JP |
| 1563 | `jpg1api.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.51 -> JP |
| 1564 | `jp2api.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.224 -> JP |
| 1565 | `43.203.227.42` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 43.203.227.42 -> KR |
| 1566 | `91.224.74.146` | vless | KZ | ip-literal | 否 | mmdb 命中 91.224.74.146 -> KZ |
| 1567 | `104.171.135.229` | vless | RU | ip-literal | 否 | mmdb 命中 104.171.135.229 -> RU |
| 1568 | `168.113.254.247` | hysteria2 | RU | ip-literal | 否 | mmdb 命中 168.113.254.247 -> RU |
| 1569 | `201.24.116.192` | vless | RU | ip-literal | 否 | mmdb 命中 201.24.116.192 -> RU |
| 1570 | `201.51.12.98` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.12.98 -> RU |
| 1571 | `201.51.2.188` | vless | RU | ip-literal | 否 | mmdb 命中 201.51.2.188 -> RU |
| 1572 | `78.159.245.147` | vless | RU | ip-literal | 否 | mmdb 命中 78.159.245.147 -> RU |
| 1573 | `vps3.nemnogogo.com` | vless | RU | domain-resolved | 否 | 解析到 201.51.12.98 -> RU |
| 1574 | `18.143.179.74` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 18.143.179.74 -> SG |
| 1575 | `free.fugui.lol` | vless | TW | domain-resolved | 否 | 解析到 1.160.33.215 -> TW |
| 1576 | `172.64.153.205` | vless | US | ip-literal | 是 | mmdb 命中 172.64.153.205 -> US |
| 1577 | `jpg1tts.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.51 -> JP |
| 1578 | `0592efg.us8.h1clayd.click` | vless | NL | domain-resolved | 否 | 解析到 13.141.51.197 -> NL |
| 1579 | `104.17.22.231` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.22.231 -> US |
| 1580 | `sdf65h46wr.df6h451rh.xin` | anytls | TW | domain-resolved | 否 | 解析到 111.246.55.93 -> TW |
| 1581 | `157.228.172.4` | vless | AE | ip-literal | 否 | mmdb 命中 157.228.172.4 -> AE |
| 1582 | `144.31.215.233` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.233 -> DE |
| 1583 | `144.31.215.244` | vless | DE | ip-literal | 否 | mmdb 命中 144.31.215.244 -> DE |
| 1584 | `146.75.57.120` | vless | US | ip-literal | 是 | mmdb 命中 146.75.57.120 -> US |
| 1585 | `46.243.205.192` | vless | RU | ip-literal | 否 | mmdb 命中 46.243.205.192 -> RU |
| 1586 | `shop.ritmexo.ir` | vless | IR | domain-resolved | 否 | 解析到 78.109.199.222 -> IR |
| 1587 | `5.249.255.116` | trojan | DK | ip-literal | 否 | mmdb 命中 5.249.255.116 -> DK |
| 1588 | `jpg1api.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.51 -> JP |
| 1589 | `jp2api.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.224 -> JP |
| 1590 | `43.203.227.42` | hysteria2 | KR | ip-literal | 否 | mmdb 命中 43.203.227.42 -> KR |
| 1591 | `104.171.135.229` | vless | RU | ip-literal | 否 | mmdb 命中 104.171.135.229 -> RU |
| 1592 | `168.113.254.247` | hysteria2 | RU | ip-literal | 否 | mmdb 命中 168.113.254.247 -> RU |
| 1593 | `18.143.179.74` | hysteria2 | SG | ip-literal | 否 | mmdb 命中 18.143.179.74 -> SG |
| 1594 | `free.fugui.lol` | vless | TW | domain-resolved | 否 | 解析到 1.160.33.215 -> TW |
| 1595 | `172.64.153.205` | vless | US | ip-literal | 是 | mmdb 命中 172.64.153.205 -> US |
| 1596 | `jpg1tts.jumpernode.site` | vless | JP | domain-resolved | 否 | 解析到 151.242.164.51 -> JP |
| 1597 | `104.17.22.231` | trojan | US | ip-literal | 是 | mmdb 命中 104.17.22.231 -> US |
| 1598 | `sdf65h46wr.df6h451rh.xin` | anytls | TW | domain-resolved | 否 | 解析到 111.246.55.93 -> TW |
| 1599 | `ru7e2bab87cc39.eu-cdn539.com` | vless | RU | domain-resolved | 否 | 解析到 129.101.98.60 -> RU |
| 1600 | `qq.utiltools.site` | vless | RU | domain-resolved | 否 | 解析到 78.159.240.192 -> RU |
| 1601 | `slowkd.sadiepinki.com` | vless | NL | domain-resolved | 否 | 解析到 212.46.33.164 -> NL |
| 1602 | `uk.extra-solutions.ru` | vless | GB | domain-resolved | 否 | 解析到 31.76.39.246 -> GB |
| 1603 | `s2.dipvpn.ru` | vless | PL | domain-resolved | 否 | 解析到 167.253.23.80 -> PL |
| 1604 | `xsru1.ddnsfree.com` | vless | RU | domain-resolved | 否 | 解析到 147.45.175.81 -> RU |
| 1605 | `161.97.160.224` | vless | FR | ip-literal | 否 | mmdb 命中 161.97.160.224 -> FR |
| 1606 | `s2.skullvpn.xyz` | vless | CZ | domain-resolved | 否 | 解析到 46.8.8.222 -> CZ |
| 1607 | `host.taghvimtime.ir` | vless | DE | domain-resolved | 否 | 解析到 91.107.191.188 -> DE |
| 1608 | `www.pixellow.online` | vless | CZ | domain-resolved | 否 | 解析到 185.32.183.55 -> CZ |
| 1609 | `unitedstates.avara.fit` | vless | RU | domain-resolved | 否 | 解析到 130.49.143.54 -> RU |
| 1610 | `185.189.58.195` | vless | DE | ip-literal | 否 | mmdb 命中 185.189.58.195 -> DE |
| 1611 | `uk1.fromblancwithlove.com` | vless | GB | domain-resolved | 否 | 解析到 152.233.28.198 -> GB |
| 1612 | `feed.onetimeok.com` | vless | MD | domain-resolved | 否 | 解析到 131.123.31.42 -> MD |
| 1613 | `plkrep.tgflow.me` | vless | PL | domain-resolved | 否 | 解析到 201.58.189.223 -> PL |
| 1614 | `pl.bubahero.com` | vless | TR | domain-resolved | 否 | 解析到 194.93.63.237 -> TR |
| 1615 | `lodizu.hagrid-connected.com` | vless | SE | domain-resolved | 否 | 解析到 103.177.249.143 -> SE |
| 1616 | `f0d7aft.nl17.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.66.221 -> EE |
| 1617 | `3h-kazakhstan1.09vpn.com` | vless | KZ | domain-resolved | 否 | 解析到 38.107.234.57 -> KZ |
| 1618 | `arvancloud.ir` | vless | IR | domain-resolved | 否 | 解析到 185.143.233.200 -> IR |
| 1619 | `a.samrayan.ir` | vless | IR | domain-resolved | 否 | 解析到 212.80.24.8 -> IR |
| 1620 | `www.zula.ir` | vless | IR | domain-resolved | 否 | 解析到 194.50.216.61 -> IR |
| 1621 | `www.tadartcom.com` | vless | FR | domain-resolved | 否 | 解析到 51.68.172.240 -> FR |
| 1622 | `vpn.zorixvpn.site` | vless | GB | domain-resolved | 否 | 解析到 194.150.166.119 -> GB |
| 1623 | `cloudfire.ir` | vless | NL | domain-resolved | 否 | 解析到 81.28.12.12 -> NL |
| 1624 | `cdnex.nztvpn.com` | vless | RU | domain-resolved | 否 | 解析到 188.72.112.1 -> RU |
| 1625 | `xray-ckc68nno-swift-harbor-8.cloady.io` | vless | GB | domain-resolved | 否 | 解析到 94.72.100.12 -> GB |
| 1626 | `foliose.merlano.monster` | vless | RU | domain-resolved | 否 | 解析到 195.58.34.112 -> RU |
| 1627 | `ru.sfasti.ru` | vless | GB | domain-resolved | 否 | 解析到 83.97.78.147 -> GB |
| 1628 | `1405-4-19-ansooyefilter-telegram.up.railway.app` | vless | US | domain-resolved | 是 | 解析到 153.52.255.35 -> US |
| 1629 | `www.tgju.org` | vless | FI | domain-resolved | 否 | 解析到 65.109.209.86 -> FI |
| 1630 | `beget-02.mansurchik.ru` | vless | RU | domain-resolved | 否 | 解析到 213.171.27.230 -> RU |
| 1631 | `harbor.gerqix.online` | vless | RU | domain-resolved | 否 | 解析到 5.42.96.100 -> RU |
| 1632 | `78ec29x.fi2.h1clayd.click` | vless | RU | domain-resolved | 否 | 解析到 83.171.241.173 -> RU |
| 1633 | `04b51566-9333-492b-b680-8f80752411f9.fly.dev` | vless | US | domain-resolved | 是 | 解析到 66.241.125.96 -> US |
| 1634 | `1579e6d9-6b57-4fb1-b080-9c9a6da46ae5.fly.dev` | vless | US | domain-resolved | 是 | 解析到 66.241.124.35 -> US |
| 1635 | `leviko-nl6411.shopingggg.ir` | vless | NL | domain-resolved | 否 | 解析到 45.86.61.133 -> NL |
| 1636 | `217.60.12.99` | vless | DE | ip-literal | 否 | mmdb 命中 217.60.12.99 -> DE |
| 1637 | `178.107.58.76` | vless | GB | ip-literal | 否 | mmdb 命中 178.107.58.76 -> GB |
| 1638 | `willowbank.moltex.click` | vless | RU | domain-resolved | 否 | 解析到 80.242.57.69 -> RU |
| 1639 | `fr.abbaas.net` | vless | FR | domain-resolved | 否 | 解析到 83.136.210.129 -> FR |
| 1640 | `222.167.245.16` | vless | PL | ip-literal | 否 | mmdb 命中 222.167.245.16 -> PL |
| 1641 | `66.163.118.251` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.251 -> ES |
| 1642 | `150.251.113.34` | vless | PL | ip-literal | 否 | mmdb 命中 150.251.113.34 -> PL |
| 1643 | `netx.smrtai.top` | vless | UA | domain-resolved | 否 | 解析到 31.222.235.81 -> UA |
| 1644 | `208.69.78.158` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.158 -> CH |
| 1645 | `sundaylanzgem.site` | vless | DE | domain-resolved | 否 | 解析到 212.80.7.119 -> DE |
| 1646 | `187.7.206.176` | vless | DE | ip-literal | 否 | mmdb 命中 187.7.206.176 -> DE |
| 1647 | `136.148.208.221` | vless | SE | ip-literal | 否 | mmdb 命中 136.148.208.221 -> SE |
| 1648 | `195.123.245.241` | vless | CZ | ip-literal | 否 | mmdb 命中 195.123.245.241 -> CZ |
| 1649 | `195.123.226.21` | vless | BG | ip-literal | 否 | mmdb 命中 195.123.226.21 -> BG |
| 1650 | `66.163.127.155` | trojan | NL | ip-literal | 否 | mmdb 命中 66.163.127.155 -> NL |
| 1651 | `212.46.33.5` | vless | NL | ip-literal | 否 | mmdb 命中 212.46.33.5 -> NL |
| 1652 | `179.254.115.118` | vless | DE | ip-literal | 否 | mmdb 命中 179.254.115.118 -> DE |
| 1653 | `159.195.137.29` | vless | DE | ip-literal | 否 | mmdb 命中 159.195.137.29 -> DE |
| 1654 | `66.163.118.115` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.115 -> ES |
| 1655 | `92.223.84.254` | vless | LU | ip-literal | 否 | mmdb 命中 92.223.84.254 -> LU |
| 1656 | `196.245.153.104` | vless | SK | ip-literal | 否 | mmdb 命中 196.245.153.104 -> SK |
| 1657 | `208.69.78.29` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.29 -> CH |
| 1658 | `31.77.168.192` | vless | DE | ip-literal | 否 | mmdb 命中 31.77.168.192 -> DE |
| 1659 | `163.245.42.85` | vless | DE | ip-literal | 否 | mmdb 命中 163.245.42.85 -> DE |
| 1660 | `130.78.30.147` | vless | NL | ip-literal | 否 | mmdb 命中 130.78.30.147 -> NL |
| 1661 | `66.163.127.225` | trojan | NL | ip-literal | 否 | mmdb 命中 66.163.127.225 -> NL |
| 1662 | `132.243.163.167` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.167 -> GB |
| 1663 | `185.246.155.91` | vless | NL | ip-literal | 否 | mmdb 命中 185.246.155.91 -> NL |
| 1664 | `179.254.115.200` | vless | DE | ip-literal | 否 | mmdb 命中 179.254.115.200 -> DE |
| 1665 | `51.158.206.97` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.97 -> NL |
| 1666 | `79.182.70.192` | vless | NL | ip-literal | 否 | mmdb 命中 79.182.70.192 -> NL |
| 1667 | `132.243.163.174` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.174 -> GB |
| 1668 | `93.123.85.59` | vless | DE | ip-literal | 否 | mmdb 命中 93.123.85.59 -> DE |
| 1669 | `66.163.127.9` | trojan | NL | ip-literal | 否 | mmdb 命中 66.163.127.9 -> NL |
| 1670 | `208.69.78.60` | trojan | CH | ip-literal | 否 | mmdb 命中 208.69.78.60 -> CH |
| 1671 | `45.95.232.233` | vless | CH | ip-literal | 否 | mmdb 命中 45.95.232.233 -> CH |
| 1672 | `54.37.136.194` | vless | FR | ip-literal | 否 | mmdb 命中 54.37.136.194 -> FR |
| 1673 | `107.181.151.128` | vless | GB | ip-literal | 否 | mmdb 命中 107.181.151.128 -> GB |
| 1674 | `pl-waw.dontblockmepls.com` | vless | HU | domain-resolved | 否 | 解析到 85.155.246.26 -> HU |
| 1675 | `71b840t.de7.h1clayd.click` | vless | NL | domain-resolved | 否 | 解析到 195.206.235.72 -> NL |
| 1676 | `138.124.125.193` | vless | GB | ip-literal | 否 | mmdb 命中 138.124.125.193 -> GB |
| 1677 | `51.38.71.147` | vless | GB | ip-literal | 否 | mmdb 命中 51.38.71.147 -> GB |
| 1678 | `82.118.16.187` | vless | IT | ip-literal | 否 | mmdb 命中 82.118.16.187 -> IT |
| 1679 | `31.76.119.123` | vless | DE | ip-literal | 否 | mmdb 命中 31.76.119.123 -> DE |
| 1680 | `138.124.180.137` | vless | LV | ip-literal | 否 | mmdb 命中 138.124.180.137 -> LV |
| 1681 | `89.35.14.30` | vless | MD | ip-literal | 否 | mmdb 命中 89.35.14.30 -> MD |
| 1682 | `pubsub.m2ip-video.cloud` | vless | CY | domain-resolved | 否 | 解析到 132.243.229.53 -> CY |
| 1683 | `66.163.118.131` | trojan | ES | ip-literal | 否 | mmdb 命中 66.163.118.131 -> ES |
| 1684 | `170.168.97.6` | vless | ES | ip-literal | 否 | mmdb 命中 170.168.97.6 -> ES |
| 1685 | `65.108.3.59` | vless | FI | ip-literal | 否 | mmdb 命中 65.108.3.59 -> FI |
| 1686 | `uk1.connectsuite.org` | vless | GB | domain-resolved | 否 | 解析到 51.38.71.147 -> GB |
| 1687 | `04535dt.us8.h1clayd.click` | vless | NL | domain-resolved | 否 | 解析到 13.141.51.197 -> NL |
| 1688 | `66.163.127.154` | trojan | NL | ip-literal | 否 | mmdb 命中 66.163.127.154 -> NL |
| 1689 | `8a2e72t.nl20.h1clayd.shop` | vless | NL | domain-resolved | 否 | 解析到 13.141.51.184 -> NL |
| 1690 | `153.56.229.218` | vless | DE | ip-literal | 否 | mmdb 命中 153.56.229.218 -> DE |
| 1691 | `gemsubbgem.world` | vless | DE | domain-resolved | 否 | 解析到 201.58.185.96 -> DE |
| 1692 | `83.141.92.168` | vless | IE | ip-literal | 否 | mmdb 命中 83.141.92.168 -> IE |
| 1693 | `89.124.122.19` | vless | NL | ip-literal | 否 | mmdb 命中 89.124.122.19 -> NL |
| 1694 | `38917fx.es1.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 132.243.67.148 -> EE |
| 1695 | `45.194.66.177` | vless | PL | ip-literal | 否 | mmdb 命中 45.194.66.177 -> PL |
| 1696 | `de-2.starsping.com` | vless | DE | domain-resolved | 否 | 解析到 109.71.253.152 -> DE |
| 1697 | `152.228.139.33` | vless | FR | ip-literal | 否 | mmdb 命中 152.228.139.33 -> FR |
| 1698 | `md1.univesalsrv.com` | vless | MD | domain-resolved | 否 | 解析到 89.35.14.30 -> MD |
| 1699 | `66.163.127.107` | trojan | NL | ip-literal | 否 | mmdb 命中 66.163.127.107 -> NL |
| 1700 | `ragnarok-vpn.ru` | vless | DE | domain-resolved | 否 | 解析到 193.135.137.12 -> DE |
| 1701 | `ch5.h1cloud.net` | vless | DE | domain-resolved | 否 | 解析到 48.103.231.107 -> DE |
| 1702 | `homestead-walloping.sports-streams.org` | vless | TR | domain-resolved | 否 | 解析到 87.120.106.95 -> TR |
| 1703 | `31.58.213.235` | vless | AE | ip-literal | 否 | mmdb 命中 31.58.213.235 -> AE |
| 1704 | `149.104.104.101` | trojan | PK | ip-literal | 否 | mmdb 命中 149.104.104.101 -> PK |
| 1705 | `185.18.250.252` | trojan | CH | ip-literal | 否 | mmdb 命中 185.18.250.252 -> CH |
| 1706 | `159.195.5.79` | vless | DE | ip-literal | 否 | mmdb 命中 159.195.5.79 -> DE |
| 1707 | `app.streamru13.net` | vless | US | domain-resolved | 是 | 解析到 50.7.95.221 -> US |
| 1708 | `216.152.147.79` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.79 -> CA |
| 1709 | `custom_config` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1710 | `178.17.53.154` | vless | FI | ip-literal | 否 | mmdb 命中 178.17.53.154 -> FI |
| 1711 | `38.47.119.139` | vless | US | ip-literal | 是 | mmdb 命中 38.47.119.139 -> US |
| 1712 | `alireza.karamoz1.ir` | trojan | DE | domain-resolved | 否 | 解析到 109.176.202.74 -> DE |
| 1713 | `15.204.97.198` | vless | US | ip-literal | 是 | mmdb 命中 15.204.97.198 -> US |
| 1714 | `154.40.59.238` | vless | US | ip-literal | 是 | mmdb 命中 154.40.59.238 -> US |
| 1715 | `216.152.147.201` | trojan | CA | ip-literal | 否 | mmdb 命中 216.152.147.201 -> CA |
| 1716 | `209.94.90.47` | vless | US | ip-literal | 是 | mmdb 命中 209.94.90.47 -> US |
| 1717 | `xray2-direct-mci1-fs-ce.freesocks.work` | vless | US | domain-resolved | 是 | 解析到 23.191.200.207 -> US |
| 1718 | `pscresearch.faculty.ucdavis.edu` | vless | US | domain-resolved | 是 | 解析到 140.248.150.228 -> US |
| 1719 | `45.130.125.76` | trojan | SC | ip-literal | 否 | mmdb 命中 45.130.125.76 -> SC |
| 1720 | `python-graysongon.wasmer.app` | vless | US | domain-resolved | 是 | 解析到 5.161.21.232 -> US |
| 1721 | `sw1.hidenet.xyz` | vless | US | domain-resolved | 是 | 解析到 144.31.240.66 -> US |
| 1722 | `45.130.125.69` | vless | SC | ip-literal | 否 | mmdb 命中 45.130.125.69 -> SC |
| 1723 | `t11.qifei.app` | vless | US | domain-resolved | 是 | 解析到 172.236.238.189 -> US |
| 1724 | `t12.qifei.app` | vless | US | domain-resolved | 是 | 解析到 172.236.253.215 -> US |
| 1725 | `t17.qifei.app` | vless | US | domain-resolved | 是 | 解析到 172.235.36.149 -> US |
| 1726 | `14.102.228.76` | trojan | US | ip-literal | 是 | mmdb 命中 14.102.228.76 -> US |
| 1727 | `bwdraper.faculty.ucdavis.edu` | vless | US | domain-resolved | 是 | 解析到 140.248.150.228 -> US |
| 1728 | `212.183.88.136` | trojan | AT | ip-literal | 否 | mmdb 命中 212.183.88.136 -> AT |
| 1729 | `88.216.220.88` | vless | DE | ip-literal | 否 | mmdb 命中 88.216.220.88 -> DE |
| 1730 | `65.109.118.175` | vless | FI | ip-literal | 否 | mmdb 命中 65.109.118.175 -> FI |
| 1731 | `213.130.137.160` | vless | FR | ip-literal | 否 | mmdb 命中 213.130.137.160 -> FR |
| 1732 | `213.130.137.190` | vless | FR | ip-literal | 否 | mmdb 命中 213.130.137.190 -> FR |
| 1733 | `206.238.239.245` | vless | SG | ip-literal | 否 | mmdb 命中 206.238.239.245 -> SG |
| 1734 | `xray-ikmqcro3-rapid-river-6.cloady.io` | vless | IN | domain-resolved | 否 | 解析到 13.140.253.35 -> IN |
| 1735 | `v2jp.k1.ssnss.live` | trojan | JP | domain-resolved | 否 | 解析到 18.179.6.184 -> JP |
| 1736 | `45.153.245.181` | vless | JP | ip-literal | 否 | mmdb 命中 45.153.245.181 -> JP |
| 1737 | `122.8.45.3` | vless | CN | ip-literal | 否 | mmdb 命中 122.8.45.3 -> CN |
| 1738 | `pq.aws51.yydjc.top` | vless | JP | domain-resolved | 否 | 解析到 35.78.243.38 -> JP |
| 1739 | `185.86.145.78` | vless | RU | ip-literal | 否 | mmdb 命中 185.86.145.78 -> RU |
| 1740 | `43.169.18.179` | trojan | SG | ip-literal | 否 | mmdb 命中 43.169.18.179 -> SG |
| 1741 | `199.232.78.187` | vless | US | ip-literal | 是 | mmdb 命中 199.232.78.187 -> US |
| 1742 | `crewmen-grittier.freevideochats.org` | vless | US | domain-resolved | 是 | 解析到 176.126.122.168 -> US |
| 1743 | `zmaoz.faculty.ucdavis.edu` | vless | US | domain-resolved | 是 | 解析到 140.248.150.228 -> US |
| 1744 | `69.46.46.145` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.145 -> US |
| 1745 | `piracy-android.video-streams.org` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1746 | `s226.okgg.top` | vless | US | domain-resolved | 是 | 解析到 45.62.109.93 -> US |
| 1747 | `s2318.okgg.top` | vless | US | domain-resolved | 是 | 解析到 45.62.109.93 -> US |
| 1748 | `speedtest.net` | vless | US | domain-resolved | 是 | 解析到 151.101.2.219 -> US |
| 1749 | `www.gameturk.bestvnxv.org` | vless | IR | domain-resolved | 否 | 解析到 185.10.240.21 -> IR |
| 1750 | `141.98.7.193` | vless | DE | ip-literal | 否 | mmdb 命中 141.98.7.193 -> DE |
| 1751 | `kala.fortresshost.ir` | vless | DE | domain-resolved | 否 | 解析到 91.107.247.173 -> DE |
| 1752 | `65.108.231.185` | vless | FI | ip-literal | 否 | mmdb 命中 65.108.231.185 -> FI |
| 1753 | `213.130.137.40` | vless | FR | ip-literal | 否 | mmdb 命中 213.130.137.40 -> FR |
| 1754 | `159.65.51.189` | vless | GB | ip-literal | 否 | mmdb 命中 159.65.51.189 -> GB |
| 1755 | `89.35.14.32` | vless | MD | ip-literal | 否 | mmdb 命中 89.35.14.32 -> MD |
| 1756 | `no.cnd.uk.1.mediasync-api.com` | vless | MD | domain-resolved | 否 | 解析到 143.246.219.215 -> MD |
| 1757 | `188.164.248.216` | vless | NL | ip-literal | 否 | mmdb 命中 188.164.248.216 -> NL |
| 1758 | `147.78.182.3` | vless | RU | ip-literal | 否 | mmdb 命中 147.78.182.3 -> RU |
| 1759 | `subgift.gcorecdn.com` | vless | LU | domain-resolved | 否 | 解析到 92.223.84.254 -> LU |
| 1760 | `pirozi_ArGaP&security=reality&encryption=none&pbk=gF44pErBRsCwFGY398I654T5EBhcB6sryObLgcqxTSI&fp=chrome&type=xhttp&sni=cira.ca&sid=41b779` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1761 | `de.gvtop.net` | vless | DE | domain-resolved | 否 | 解析到 31.76.101.136 -> DE |
| 1762 | `188.225.57.185` | vless | RU | ip-literal | 否 | mmdb 命中 188.225.57.185 -> RU |
| 1763 | `147.45.175.81` | vless | RU | ip-literal | 否 | mmdb 命中 147.45.175.81 -> RU |
| 1764 | `37.18.15.192` | vless | RU | ip-literal | 否 | mmdb 命中 37.18.15.192 -> RU |
| 1765 | `154.218.15.198` | vless | SC | ip-literal | 否 | mmdb 命中 154.218.15.198 -> SC |
| 1766 | `45.130.125.160` | trojan | SC | ip-literal | 否 | mmdb 命中 45.130.125.160 -> SC |
| 1767 | `45.130.125.69` | trojan | SC | ip-literal | 否 | mmdb 命中 45.130.125.69 -> SC |
| 1768 | `earthpro.wasmer.app` | vless | US | domain-resolved | 是 | 解析到 5.161.23.223 -> US |
| 1769 | `199.232.78.159` | vless | US | ip-literal | 是 | mmdb 命中 199.232.78.159 -> US |
| 1770 | `199.232.78.199` | vless | US | ip-literal | 是 | mmdb 命中 199.232.78.199 -> US |
| 1771 | `grimness-backlogs.cdn-content.com` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1772 | `adheres-scruple.quick-cdn.net` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1773 | `Zmaoz.Faculty.Ucdavis.Edu` | vless | US | domain-resolved | 是 | 解析到 140.248.150.228 -> US |
| 1774 | `spiderpanel-development-g5884.lucity.app` | vless | US | domain-resolved | 是 | 解析到 38.104.169.186 -> US |
| 1775 | `86153507-1976-48f1-ac86-e8ab274470a8.fly.dev` | vless | US | domain-resolved | 是 | 解析到 66.241.125.201 -> US |
| 1776 | `bounded-crammed.video-streams.org` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1777 | `frfx.pafaktalaei.ir` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1778 | `gcore.com` | vless | US | domain-resolved | 是 | 解析到 92.38.145.145 -> US |
| 1779 | `minimize-evenness.cdn-content.com` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1780 | `sclass-c2.catcat321.com` | trojan | US | domain-resolved | 是 | 解析到 157.254.38.210 -> US |
| 1781 | `140.225.199.38` | vless | AE | ip-literal | 否 | mmdb 命中 140.225.199.38 -> AE |
| 1782 | `89.47.55.5` | vless | AE | ip-literal | 否 | mmdb 命中 89.47.55.5 -> AE |
| 1783 | `122.8.45.2` | vless | CN | ip-literal | 否 | mmdb 命中 122.8.45.2 -> CN |
| 1784 | `lovesykun.cn` | vless | SG | domain-resolved | 否 | 解析到 43.174.246.25 -> SG |
| 1785 | `165.231.177.114` | vless | SC | ip-literal | 否 | mmdb 命中 165.231.177.114 -> SC |
| 1786 | `199.232.11.52` | vless | US | ip-literal | 是 | mmdb 命中 199.232.11.52 -> US |
| 1787 | `199.232.9.254` | vless | US | ip-literal | 是 | mmdb 命中 199.232.9.254 -> US |
| 1788 | `t14.qifei.app` | vless | US | domain-resolved | 是 | 解析到 172.233.138.7 -> US |
| 1789 | `69.46.46.22` | vless | US | ip-literal | 是 | mmdb 命中 69.46.46.22 -> US |
| 1790 | `104.245.240.3` | vless | US | ip-literal | 是 | mmdb 命中 104.245.240.3 -> US |
| 1791 | `104.245.240.6` | vless | US | ip-literal | 是 | mmdb 命中 104.245.240.6 -> US |
| 1792 | `151.101.215.69` | vless | US | ip-literal | 是 | mmdb 命中 151.101.215.69 -> US |
| 1793 | `87.120.92.186` | vless | BG | ip-literal | 否 | mmdb 命中 87.120.92.186 -> BG |
| 1794 | `95.217.206.161` | vless | FI | ip-literal | 否 | mmdb 命中 95.217.206.161 -> FI |
| 1795 | `WangCai2%20` | vless | - | invalid_server | 否 | URL编码碎片：'WangCai2%20' -> 'WangCai2 ' 非合法 hostname/IP |
| 1796 | `185.193.31.253` | vless | GB | ip-literal | 否 | mmdb 命中 185.193.31.253 -> GB |
| 1797 | `45.131.211.253` | vless | NL | ip-literal | 否 | mmdb 命中 45.131.211.253 -> NL |
| 1798 | `109.71.245.99` | vless | RU | ip-literal | 否 | mmdb 命中 109.71.245.99 -> RU |
| 1799 | `178.176.128.128` | vless | RU | ip-literal | 否 | mmdb 命中 178.176.128.128 -> RU |
| 1800 | `clash.ddm4.cn` | vless | US | domain-resolved | 是 | 解析到 64.186.233.233 -> US |
| 1801 | `5.42.96.100` | vless | RU | ip-literal | 否 | mmdb 命中 5.42.96.100 -> RU |
| 1802 | `5.42.96.196` | vless | RU | ip-literal | 否 | mmdb 命中 5.42.96.196 -> RU |
| 1803 | `209.94.90.201` | vless | US | ip-literal | 是 | mmdb 命中 209.94.90.201 -> US |
| 1804 | `45.95.98.139` | vless | FR | ip-literal | 否 | mmdb 命中 45.95.98.139 -> FR |
| 1805 | `2.26.187.132` | vless | US | ip-literal | 是 | mmdb 命中 2.26.187.132 -> US |
| 1806 | `81.90.21.200` | vless | SE | ip-literal | 否 | mmdb 命中 81.90.21.200 -> SE |
| 1807 | `185.222.43.175` | vless | JP | ip-literal | 否 | mmdb 命中 185.222.43.175 -> JP |
| 1808 | `188.72.112.2` | vless | RU | ip-literal | 否 | mmdb 命中 188.72.112.2 -> RU |
| 1809 | `213.156.152.233` | vless | TR | ip-literal | 否 | mmdb 命中 213.156.152.233 -> TR |
| 1810 | `leviko-ir8553.shopingggg.ir` | vless | IR | domain-resolved | 否 | 解析到 194.60.228.97 -> IR |
| 1811 | `206.238.239.20` | vless | SG | ip-literal | 否 | mmdb 命中 206.238.239.20 -> SG |
| 1812 | `103.219.195.65` | vless | HK | ip-literal | 否 | mmdb 命中 103.219.195.65 -> HK |
| 1813 | `185.232.204.116` | vless | FI | ip-literal | 否 | mmdb 命中 185.232.204.116 -> FI |
| 1814 | `154.218.15.1` | vless | SC | ip-literal | 否 | mmdb 命中 154.218.15.1 -> SC |
| 1815 | `176.126.122.168` | vless | US | ip-literal | 是 | mmdb 命中 176.126.122.168 -> US |
| 1816 | `caudal-reason.freevideochats.org` | vless | US | domain-resolved | 是 | 解析到 87.120.252.67 -> US |
| 1817 | `131.143.180.53` | vless | US | ip-literal | 是 | mmdb 命中 131.143.180.53 -> US |
| 1818 | `85.92.156.133` | vless | JP | ip-literal | 否 | mmdb 命中 85.92.156.133 -> JP |
| 1819 | `178.17.52.31` | vless | IQ | ip-literal | 否 | mmdb 命中 178.17.52.31 -> IQ |
| 1820 | `140.245.62.225` | vless | SG | ip-literal | 否 | mmdb 命中 140.245.62.225 -> SG |
| 1821 | `27.50.48.102` | vless | SG | ip-literal | 否 | mmdb 命中 27.50.48.102 -> SG |
| 1822 | `27.50.48.8` | vless | SG | ip-literal | 否 | mmdb 命中 27.50.48.8 -> SG |
| 1823 | `27.50.49.104` | vless | SG | ip-literal | 否 | mmdb 命中 27.50.49.104 -> SG |
| 1824 | `198.202.24.214` | vless | US | ip-literal | 是 | mmdb 命中 198.202.24.214 -> US |
| 1825 | `85.92.156.133` | vless | JP | ip-literal | 否 | mmdb 命中 85.92.156.133 -> JP |
| 1826 | `217.60.34.202` | vless | NL | ip-literal | 否 | mmdb 命中 217.60.34.202 -> NL |
| 1827 | `95.129.234.113` | vless | RU | ip-literal | 否 | mmdb 命中 95.129.234.113 -> RU |
| 1828 | `51.38.99.96` | trojan | FR | ip-literal | 否 | mmdb 命中 51.38.99.96 -> FR |
| 1829 | `app.streamru16.net` | vless | NL | domain-resolved | 否 | 解析到 84.32.185.50 -> NL |
| 1830 | `fr.abbaas.net` | vless | FR | domain-resolved | 否 | 解析到 83.136.210.129 -> FR |
| 1831 | `51.195.219.173` | trojan | FR | ip-literal | 否 | mmdb 命中 51.195.219.173 -> FR |
| 1832 | `app.streamru10.net` | vless | SE | domain-resolved | 否 | 解析到 84.32.154.75 -> SE |
| 1833 | `173.242.51.189` | trojan | UA | ip-literal | 否 | mmdb 命中 173.242.51.189 -> UA |
| 1834 | `209.250.236.93` | trojan | DE | ip-literal | 否 | mmdb 命中 209.250.236.93 -> DE |
| 1835 | `9bfbf9x.fi15.h1clayd.click` | vless | EE | domain-resolved | 否 | 解析到 179.254.126.220 -> EE |
| 1836 | `185.86.147.211` | vless | RU | ip-literal | 否 | mmdb 命中 185.86.147.211 -> RU |
| 1837 | `557e58g.pl8.h1clayd.click` | vless | RU | domain-resolved | 否 | 解析到 83.171.241.154 -> RU |
| 1838 | `95.179.246.122` | trojan | DE | ip-literal | 否 | mmdb 命中 95.179.246.122 -> DE |
| 1839 | `fr.test3.net` | trojan | FR | domain-resolved | 否 | 解析到 51.159.59.186 -> FR |
| 1840 | `51.158.146.183` | trojan | NL | ip-literal | 否 | mmdb 命中 51.158.146.183 -> NL |
| 1841 | `51.83.186.142` | trojan | PL | ip-literal | 否 | mmdb 命中 51.83.186.142 -> PL |
| 1842 | `95.129.234.108` | vless | RU | ip-literal | 否 | mmdb 命中 95.129.234.108 -> RU |
| 1843 | `185.178.208.140` | vless | RU | ip-literal | 否 | mmdb 命中 185.178.208.140 -> RU |
| 1844 | `app.streamru14.net` | vless | DE | domain-resolved | 否 | 解析到 88.216.70.62 -> DE |
| 1845 | `212.87.190.249` | vless | EE | ip-literal | 否 | mmdb 命中 212.87.190.249 -> EE |
| 1846 | `195.63.138.212` | vless | NL | ip-literal | 否 | mmdb 命中 195.63.138.212 -> NL |
| 1847 | `sub-edge-05-1g.whitenw.net` | vless | RU | domain-resolved | 否 | 解析到 185.86.145.223 -> RU |
| 1848 | `194.124.251.104` | vless | CH | ip-literal | 否 | mmdb 命中 194.124.251.104 -> CH |
| 1849 | `86.106.119.23` | trojan | AT | ip-literal | 否 | mmdb 命中 86.106.119.23 -> AT |
| 1850 | `143.246.41.205` | vless | EE | ip-literal | 否 | mmdb 命中 143.246.41.205 -> EE |
| 1851 | `88.216.69.253` | vless | LT | ip-literal | 否 | mmdb 命中 88.216.69.253 -> LT |
| 1852 | `Rayan_Config&security=tls&encryption=none&host=rayan-12.leila.dpdns.org&fp=chrome&type=ws&sni=rAyAn-12.LeIlA.DpDnS.OrG` | vless | - | unknown | 否 | 非合法域名/IP（疑似 README URI 碎片），不解析 DNS |
| 1853 | `31.57.62.75` | vless | LV | ip-literal | 否 | mmdb 命中 31.57.62.75 -> LV |
| 1854 | `193.181.209.210` | vless | DK | ip-literal | 否 | mmdb 命中 193.181.209.210 -> DK |
| 1855 | `84.32.209.118` | vless | LT | ip-literal | 否 | mmdb 命中 84.32.209.118 -> LT |
| 1856 | `linen.gerqix.online` | vless | RU | domain-resolved | 否 | 解析到 5.42.105.128 -> RU |
| 1857 | `5.175.249.117` | trojan | DE | ip-literal | 否 | mmdb 命中 5.175.249.117 -> DE |
| 1858 | `195.54.161.249` | trojan | GB | ip-literal | 否 | mmdb 命中 195.54.161.249 -> GB |
| 1859 | `132.243.163.154` | vless | GB | ip-literal | 否 | mmdb 命中 132.243.163.154 -> GB |
| 1860 | `185.107.56.55` | trojan | NL | ip-literal | 否 | mmdb 命中 185.107.56.55 -> NL |
| 1861 | `38.180.35.145` | trojan | RO | ip-literal | 否 | mmdb 命中 38.180.35.145 -> RO |
| 1862 | `94.103.91.22` | trojan | RU | ip-literal | 否 | mmdb 命中 94.103.91.22 -> RU |
| 1863 | `checkout.salu.lalibobi.online` | trojan | EE | domain-resolved | 否 | 解析到 217.60.182.19 -> EE |
| 1864 | `54.37.18.204` | trojan | FR | ip-literal | 否 | mmdb 命中 54.37.18.204 -> FR |
| 1865 | `51.38.65.155` | trojan | GB | ip-literal | 否 | mmdb 命中 51.38.65.155 -> GB |
| 1866 | `104.222.183.180` | vless | GB | ip-literal | 否 | mmdb 命中 104.222.183.180 -> GB |
| 1867 | `185.107.56.53` | trojan | NL | ip-literal | 否 | mmdb 命中 185.107.56.53 -> NL |
| 1868 | `37.153.171.4` | vless | NL | ip-literal | 否 | mmdb 命中 37.153.171.4 -> NL |
| 1869 | `d4a338t.pl8.h1clayd.click` | vless | RU | domain-resolved | 否 | 解析到 83.171.241.154 -> RU |
| 1870 | `195.72.62.7` | vless | SE | ip-literal | 否 | mmdb 命中 195.72.62.7 -> SE |
| 1871 | `swcdnmega.surverssss.pro` | vless | SE | domain-resolved | 否 | 解析到 163.245.43.57 -> SE |
| 1872 | `92.42.201.107` | vless | SI | ip-literal | 否 | mmdb 命中 92.42.201.107 -> SI |
| 1873 | `au2.pad-sservice.lat` | vless | CH | domain-resolved | 否 | 解析到 201.8.81.75 -> CH |
| 1874 | `193.8.169.74` | trojan | DE | ip-literal | 否 | mmdb 命中 193.8.169.74 -> DE |
| 1875 | `de-3.tr202605.com` | trojan | DE | domain-resolved | 否 | 解析到 193.8.169.97 -> DE |
| 1876 | `files.noneok.com` | vless | DE | domain-resolved | 否 | 解析到 88.216.220.88 -> DE |
| 1877 | `217.79.184.76` | trojan | DE | ip-literal | 否 | mmdb 命中 217.79.184.76 -> DE |
| 1878 | `45.139.194.60` | trojan | EE | ip-literal | 否 | mmdb 命中 45.139.194.60 -> EE |
| 1879 | `d58daft.plp1.h1cloud.net` | vless | EE | domain-resolved | 否 | 解析到 13.143.239.218 -> EE |
| 1880 | `ee-1.tr202604.com` | trojan | EE | domain-resolved | 否 | 解析到 45.139.194.68 -> EE |
| 1881 | `172.232.38.127` | trojan | FR | ip-literal | 否 | mmdb 命中 172.232.38.127 -> FR |
| 1882 | `188.165.25.135` | trojan | FR | ip-literal | 否 | mmdb 命中 188.165.25.135 -> FR |
| 1883 | `node-uk.connectsuite.org` | vless | GB | domain-resolved | 否 | 解析到 51.38.71.147 -> GB |
| 1884 | `uk1.test3.net` | trojan | GB | domain-resolved | 否 | 解析到 51.38.65.155 -> GB |
| 1885 | `157.245.45.54` | trojan | GB | ip-literal | 否 | mmdb 命中 157.245.45.54 -> GB |
| 1886 | `164.92.153.211` | trojan | NL | ip-literal | 否 | mmdb 命中 164.92.153.211 -> NL |
| 1887 | `185.130.225.218` | trojan | NL | ip-literal | 否 | mmdb 命中 185.130.225.218 -> NL |
| 1888 | `193.169.239.198` | trojan | NL | ip-literal | 否 | mmdb 命中 193.169.239.198 -> NL |
| 1889 | `78.142.194.96` | trojan | NL | ip-literal | 否 | mmdb 命中 78.142.194.96 -> NL |
| 1890 | `202.78.163.113` | trojan | PL | ip-literal | 否 | mmdb 命中 202.78.163.113 -> PL |
| 1891 | `64.176.75.215` | trojan | PL | ip-literal | 否 | mmdb 命中 64.176.75.215 -> PL |
| 1892 | `distinct-ibex.rooster465.autos` | trojan | PL | domain-resolved | 否 | 解析到 202.78.163.113 -> PL |
| 1893 | `45.147.200.44` | trojan | RU | ip-literal | 否 | mmdb 命中 45.147.200.44 -> RU |
| 1894 | `87.242.94.43` | vless | RU | ip-literal | 否 | mmdb 命中 87.242.94.43 -> RU |
| 1895 | `130.0.236.88` | trojan | UA | ip-literal | 否 | mmdb 命中 130.0.236.88 -> UA |
| 1896 | `brooded-plod.sports-streams.org` | vless | TR | domain-resolved | 否 | 解析到 87.120.106.21 -> TR |
| 1897 | `nl.private-ai.ir` | vless | NL | domain-resolved | 否 | 解析到 45.32.234.219 -> NL |
| 1898 | `hiccuped-tacos.sports-streams.org` | vless | US | domain-resolved | 是 | 解析到 176.126.122.236 -> US |
| 1899 | `tuic.moxin1245.win` | vless | US | domain-resolved | 是 | 解析到 45.78.14.137 -> US |
| 1900 | `coughed-gongs.freevideochats.org` | vless | US | domain-resolved | 是 | 解析到 162.216.231.214 -> US |
| 1901 | `barbered-mattocks.video-streams.org` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1902 | `guessable-turnpikes.cdn-content.com` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1903 | `ir.vnexjet.ir` | vless | US | domain-resolved | 是 | 解析到 140.248.149.242 -> US |
| 1904 | `www.arizona.edu` | vless | US | domain-resolved | 是 | 解析到 23.185.0.4 -> US |
| 1905 | `s868.okgg.top` | vless | US | domain-resolved | 是 | 解析到 45.62.109.93 -> US |
| 1906 | `s9601.okgg.top` | vless | US | domain-resolved | 是 | 解析到 45.62.109.93 -> US |
| 1907 | `195.123.208.48.tyr-agentstvo.tech` | vless | LV | domain-resolved | 否 | 解析到 195.123.208.48 -> LV |
| 1908 | `193.34.212.80.vhub.pro` | vless | PL | domain-resolved | 否 | 解析到 193.34.212.80 -> PL |
| 1909 | `official.taipeicitygovernment.chernovtsy.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.130 -> TW |
| 1910 | `official.taipeicitygovernment.com.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.31 -> TW |
| 1911 | `official.taipeicitygovernment.net.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.128.151 -> TW |
| 1912 | `official.taipeicitygovernment.org.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.152.229 -> TW |
| 1913 | `official.taipeicitygovernment.biz.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.128.151 -> TW |
| 1914 | `official.taipeicitygovernment.cn.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.135.193 -> TW |
| 1915 | `official.taipeicitygovernment.dp.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.135.193 -> TW |
| 1916 | `official.taipeicitygovernment.if.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.135.193 -> TW |
| 1917 | `official.taipeicitygovernment.kiev.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.152.229 -> TW |
| 1918 | `official.taipeicitygovernment.kyiv.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.130 -> TW |
| 1919 | `official.taipeicitygovernment.co.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.31 -> TW |
| 1920 | `official.taipeicitygovernment.ivano-frankivsk.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.152.229 -> TW |
| 1921 | `www.binodes.com` | vless | SG | domain-resolved | 否 | 解析到 43.174.247.25 -> SG |
| 1922 | `a01.taipeicitygovernment.biz.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.135.193 -> TW |
| 1923 | `a03.taipeicitygovernment.cn.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.31 -> TW |
| 1924 | `a10.taipeicitygovernment.kyiv.ua` | trojan | TW | domain-resolved | 否 | 解析到 220.128.135.193 -> TW |
| 1925 | `a12.taipeicitygovernment.org.ua` | trojan | TW | domain-resolved | 否 | 解析到 60.250.80.31 -> TW |
| 1926 | `fuji.etherhub.cc` | vless | JP | domain-resolved | 否 | 解析到 31.76.91.98 -> JP |
| 1927 | `msydjt.com` | vless | SG | domain-resolved | 否 | 解析到 43.174.247.63 -> SG |
| 1928 | `rodekors.dk` | vless | US | domain-resolved | 是 | 解析到 151.101.1.55 -> US |
| 1929 | `www.hivenet.com` | vless | US | domain-resolved | 是 | 解析到 198.202.211.1 -> US |
| 1930 | `netherrap.extraservices.ir` | vless | IR | domain-resolved | 否 | 解析到 176.120.17.202 -> IR |
| 1931 | `t-panel.wasmer.app` | vless | US | domain-resolved | 是 | 解析到 5.161.21.232 -> US |
| 1932 | `169.40.42.35` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.35 -> DE |
| 1933 | `169.40.42.202` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.202 -> DE |
| 1934 | `167.17.69.171` | vless | US | ip-literal | 是 | mmdb 命中 167.17.69.171 -> US |
| 1935 | `169.40.42.229` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.229 -> DE |
| 1936 | `169.40.42.89` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.89 -> DE |
| 1937 | `169.40.42.74` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.74 -> DE |
| 1938 | `45.63.53.81` | vless | US | ip-literal | 是 | mmdb 命中 45.63.53.81 -> US |
| 1939 | `169.40.42.90` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.90 -> DE |
| 1940 | `169.40.42.168` | vless | DE | ip-literal | 否 | mmdb 命中 169.40.42.168 -> DE |
| 1941 | `69.164.240.85` | trojan | US | ip-literal | 是 | mmdb 命中 69.164.240.85 -> US |
| 1942 | `206.189.229.48` | hysteria2 | US | ip-literal | 是 | mmdb 命中 206.189.229.48 -> US |
| 1943 | `216.227.161.95` | vless | US | ip-literal | 是 | mmdb 命中 216.227.161.95 -> US |
| 1944 | `179.254.92.134` | vless | US | ip-literal | 是 | mmdb 命中 179.254.92.134 -> US |
| 1945 | `179.254.92.190` | vless | US | ip-literal | 是 | mmdb 命中 179.254.92.190 -> US |
| 1946 | `216.152.156.65` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.65 -> US |
| 1947 | `172.235.48.213` | vless | US | ip-literal | 是 | mmdb 命中 172.235.48.213 -> US |
| 1948 | `170.101.101.67` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.67 -> US |
| 1949 | `170.101.101.112` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.112 -> US |
| 1950 | `216.152.155.59` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.59 -> US |
| 1951 | `172.235.53.103` | vless | US | ip-literal | 是 | mmdb 命中 172.235.53.103 -> US |
| 1952 | `172.236.239.126` | vless | US | ip-literal | 是 | mmdb 命中 172.236.239.126 -> US |
| 1953 | `104.168.109.213` | vless | US | ip-literal | 是 | mmdb 命中 104.168.109.213 -> US |
| 1954 | `86.54.28.75` | vless | NL | ip-literal | 否 | mmdb 命中 86.54.28.75 -> NL |
| 1955 | `172.233.157.18` | vless | US | ip-literal | 是 | mmdb 命中 172.233.157.18 -> US |
| 1956 | `172.233.140.139` | vless | US | ip-literal | 是 | mmdb 命中 172.233.140.139 -> US |
| 1957 | `172.235.40.143` | vless | US | ip-literal | 是 | mmdb 命中 172.235.40.143 -> US |
| 1958 | `156.229.167.109` | vless | US | ip-literal | 是 | mmdb 命中 156.229.167.109 -> US |
| 1959 | `172.235.50.209` | vless | US | ip-literal | 是 | mmdb 命中 172.235.50.209 -> US |
| 1960 | `172.235.32.253` | vless | US | ip-literal | 是 | mmdb 命中 172.235.32.253 -> US |
| 1961 | `172.233.146.140` | vless | US | ip-literal | 是 | mmdb 命中 172.233.146.140 -> US |
| 1962 | `172.233.156.229` | vless | US | ip-literal | 是 | mmdb 命中 172.233.156.229 -> US |
| 1963 | `66.94.121.46` | hysteria2 | US | ip-literal | 是 | mmdb 命中 66.94.121.46 -> US |
| 1964 | `172.233.139.212` | vless | US | ip-literal | 是 | mmdb 命中 172.233.139.212 -> US |
| 1965 | `216.152.156.42` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.42 -> US |
| 1966 | `172.233.139.98` | vless | US | ip-literal | 是 | mmdb 命中 172.233.139.98 -> US |
| 1967 | `172.236.238.71` | vless | US | ip-literal | 是 | mmdb 命中 172.236.238.71 -> US |
| 1968 | `172.233.129.179` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.179 -> US |
| 1969 | `216.152.155.23` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.23 -> US |
| 1970 | `172.236.231.45` | vless | US | ip-literal | 是 | mmdb 命中 172.236.231.45 -> US |
| 1971 | `167.88.61.193` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.193 -> US |
| 1972 | `159.89.87.21` | vless | US | ip-literal | 是 | mmdb 命中 159.89.87.21 -> US |
| 1973 | `172.235.36.11` | vless | US | ip-literal | 是 | mmdb 命中 172.235.36.11 -> US |
| 1974 | `172.235.37.163` | vless | US | ip-literal | 是 | mmdb 命中 172.235.37.163 -> US |
| 1975 | `172.233.129.46` | vless | US | ip-literal | 是 | mmdb 命中 172.233.129.46 -> US |
| 1976 | `34.24.25.1` | hysteria2 | US | ip-literal | 是 | mmdb 命中 34.24.25.1 -> US |
| 1977 | `216.152.155.131` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.155.131 -> US |
| 1978 | `167.88.61.198` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.198 -> US |
| 1979 | `170.101.101.53` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.53 -> US |
| 1980 | `216.152.156.212` | trojan | US | ip-literal | 是 | mmdb 命中 216.152.156.212 -> US |
| 1981 | `46.28.69.123` | vless | DE | ip-literal | 否 | mmdb 命中 46.28.69.123 -> DE |
| 1982 | `198.247.127.131` | vless | US | ip-literal | 是 | mmdb 命中 198.247.127.131 -> US |
| 1983 | `170.101.101.19` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.19 -> US |
| 1984 | `216.106.186.32` | trojan | US | ip-literal | 是 | mmdb 命中 216.106.186.32 -> US |
| 1985 | `82.40.63.138` | hysteria2 | PL | ip-literal | 否 | mmdb 命中 82.40.63.138 -> PL |
| 1986 | `48.103.231.2` | vless | DE | ip-literal | 否 | mmdb 命中 48.103.231.2 -> DE |
| 1987 | `93.123.101.198` | vless | DE | ip-literal | 否 | mmdb 命中 93.123.101.198 -> DE |
| 1988 | `195.123.226.21` | vless | BG | ip-literal | 否 | mmdb 命中 195.123.226.21 -> BG |
| 1989 | `157.180.98.124` | vless | FI | ip-literal | 否 | mmdb 命中 157.180.98.124 -> FI |
| 1990 | `91.107.169.224` | vless | DE | ip-literal | 否 | mmdb 命中 91.107.169.224 -> DE |
| 1991 | `170.101.101.131` | trojan | US | ip-literal | 是 | mmdb 命中 170.101.101.131 -> US |
| 1992 | `136.176.68.34` | vless | GB | ip-literal | 否 | mmdb 命中 136.176.68.34 -> GB |
| 1993 | `172.105.216.21` | vless | JP | ip-literal | 否 | mmdb 命中 172.105.216.21 -> JP |
| 1994 | `46.28.67.55` | vless | RO | ip-literal | 否 | mmdb 命中 46.28.67.55 -> RO |
| 1995 | `212.102.38.25` | vless | CZ | ip-literal | 否 | mmdb 命中 212.102.38.25 -> CZ |
| 1996 | `167.88.61.85` | trojan | US | ip-literal | 是 | mmdb 命中 167.88.61.85 -> US |
| 1997 | `62.210.124.146` | hysteria2 | FR | ip-literal | 否 | mmdb 命中 62.210.124.146 -> FR |
| 1998 | `139.162.91.250` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.250 -> JP |
| 1999 | `free-amsterdam-node-1.cloudwidecdn.com` | vless | NL | domain-resolved | 否 | 解析到 86.54.28.75 -> NL |
| 2000 | `103.75.118.228` | vless | JP | ip-literal | 否 | mmdb 命中 103.75.118.228 -> JP |
| 2001 | `193.233.198.117` | vless | DE | ip-literal | 否 | mmdb 命中 193.233.198.117 -> DE |
| 2002 | `66.23.203.21` | trojan | US | ip-literal | 是 | mmdb 命中 66.23.203.21 -> US |
| 2003 | `51.158.206.80` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.80 -> NL |
| 2004 | `205.237.111.245` | vless | RO | ip-literal | 否 | mmdb 命中 205.237.111.245 -> RO |
| 2005 | `138.124.70.41` | vless | FR | ip-literal | 否 | mmdb 命中 138.124.70.41 -> FR |
| 2006 | `162.249.127.165` | vless | RO | ip-literal | 否 | mmdb 命中 162.249.127.165 -> RO |
| 2007 | `139.162.91.202` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.202 -> JP |
| 2008 | `184.107.179.150` | vless | CA | ip-literal | 否 | mmdb 命中 184.107.179.150 -> CA |
| 2009 | `51.158.206.93` | vless | NL | ip-literal | 否 | mmdb 命中 51.158.206.93 -> NL |
| 2010 | `66.163.118.113` | vless | ES | ip-literal | 否 | mmdb 命中 66.163.118.113 -> ES |
| 2011 | `5.129.235.85` | hysteria2 | NL | ip-literal | 否 | mmdb 命中 5.129.235.85 -> NL |
| 2012 | `139.162.91.249` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.249 -> JP |
| 2013 | `139.162.91.224` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.224 -> JP |
| 2014 | `31.76.91.248` | vless | JP | ip-literal | 否 | mmdb 命中 31.76.91.248 -> JP |
| 2015 | `172.105.197.24` | vless | JP | ip-literal | 否 | mmdb 命中 172.105.197.24 -> JP |
| 2016 | `172.105.212.91` | vless | JP | ip-literal | 否 | mmdb 命中 172.105.212.91 -> JP |
| 2017 | `139.162.101.74` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.101.74 -> JP |
| 2018 | `198.13.53.39` | vless | JP | ip-literal | 否 | mmdb 命中 198.13.53.39 -> JP |
| 2019 | `45.77.8.233` | vless | JP | ip-literal | 否 | mmdb 命中 45.77.8.233 -> JP |
| 2020 | `139.162.91.137` | vless | JP | ip-literal | 否 | mmdb 命中 139.162.91.137 -> JP |

## 按 cc 分布统计

| cc | 节点数 |
|----|--------|
| US | 625 |
| NL | 199 |
| GB | 191 |
| DE | 180 |
| RU | 110 |
| (unknown) | 76 |
| SG | 69 |
| JP | 67 |
| FR | 56 |
| EE | 33 |
| TR | 33 |
| TW | 27 |
| CH | 25 |
| PL | 25 |
| SC | 24 |
| SE | 22 |
| HK | 20 |
| KR | 20 |
| CA | 15 |
| FI | 15 |
| CZ | 13 |
| ES | 13 |
| IE | 13 |
| IR | 13 |
| AE | 11 |
| AU | 11 |
| KZ | 9 |
| IN | 8 |
| LV | 7 |
| BY | 6 |
| CY | 6 |
| IT | 6 |
| MD | 6 |
| BG | 5 |
| BR | 5 |
| RO | 5 |
| SK | 5 |
| UA | 5 |
| VN | 4 |
| AT | 3 |
| CL | 3 |
| DK | 3 |
| LU | 3 |
| AM | 2 |
| BZ | 2 |
| CN | 2 |
| GR | 2 |
| IL | 2 |
| LT | 2 |
| MX | 2 |
| TH | 2 |
| ZA | 2 |
| HU | 1 |
| IQ | 1 |
| MY | 1 |
| NO | 1 |
| NZ | 1 |
| PK | 1 |
| SI | 1 |

## 过滤原因分类计数

| 原因类别 | 数量 | 含义 |
|----------|------|------|
| non_us_country | 1319 | mmdb 命中但国家码非 US |
| unknown | 75 | DNS失败/超时、URI碎片假域名、私有保留段、mmdb非标准ISO码 |
| invalid_server | 1 | URL 编码垃圾 / 空 server，解码后仍非合法 hostname/IP |

## URL 编码碎片节点（单独点名）

- 本次输入未发现 URL 编码碎片节点。

## 判定规则与依据

- IP 字面量（IPv4/IPv6）：`ipaddress` 识别 → 私有/回环/保留段直接排除 → 其余查 mmdb，`country.iso_code` 回退 `registered_country`。
- 域名：仅对合法 FQDN 做 `socket.getaddrinfo`，用 ThreadPoolExecutor + future.result(timeout=4s) 防卡死；超时/失败按 unknown；多 IP 取首个公网 IP。
- mmdb 非标准 ISO 码（如 8.8.8.8 返回 `GOOGLE`）不认定为 US，按 unknown 排除。
- README URI 解析出的碎片假 hostname（如 `23c82941`/`150`/`linlin`/`c3a8753e`/`vpn`/`srv`）不是合法域名，不做 DNS 解析，按 unknown 排除。
- URL 含 `%XX` 的 server 先 `urllib.parse.unquote`；解码后仍非合法 hostname/IP 判 invalid_server。
- 入选红线：`cc == "US"` 且 `type ∈ {anytls, hysteria, hysteria2, trojan, tuic, vless}`。

产出：`us_nodes.json`（US 节点 625）+ 本报告。
