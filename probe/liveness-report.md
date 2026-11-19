# U4 内核级真实测活报告

- 生成时间：2026-11-19T21:39:38+00:00
- 引擎：mihomo external-controller `/proxies/{name}/delay`（内核 v1.19.34）
- 测活 URL：`http://www.gstatic.com/generate_204`；单节点超时 8000ms
- 判定：alive 82 / dead 414 / unknown 0
- 预校验剔除非法节点：2（内核 -t 检出的坏字段节点，不进测活也不进订阅）

## 逐节点（server:port / 判定 / 延迟 / 依据）

| # | server:port | 判定 | 延迟(ms) | 依据 |
|---|-------------|------|----------|------|
| 1 | `45.138.100.248:10443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 2 | `ww13.levikogjgfdd.ir:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 3 | `148.135.86.162:10000` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 4 | `167.88.61.85:443` | True | 202 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 202ms |
| 5 | `216.152.156.212:443` | True | 168 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 168ms |
| 6 | `147.224.54.25:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 7 | `45.138.100.248:14430` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 8 | `67.220.73.204:18662` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 9 | `104.168.109.213:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 10 | `45.144.112.55:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 11 | `66.163.122.30:443` | True | 35 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 35ms |
| 12 | `uspanel.unixzone.us:30016` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 13 | `198.247.127.131:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 14 | `167.88.61.198:443` | True | 195 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 195ms |
| 15 | `216.106.186.82:443` | True | 230 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 230ms |
| 16 | `167.88.61.52:443` | True | 251 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 251ms |
| 17 | `66.163.114.126:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 18 | `15.204.97.195:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 19 | `216.152.156.159:443` | True | 163 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 163ms |
| 20 | `216.106.186.32:443` | True | 241 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 241ms |
| 21 | `147.45.60.136:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 22 | `167.88.61.20:443` | True | 209 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 209ms |
| 23 | `66.23.203.21:59689` | True | 191 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 191ms |
| 24 | `66.163.112.142:443` | True | 178 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 178ms |
| 25 | `170.101.101.211:443` | True | 91 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 91ms |
| 26 | `179.254.191.251:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 27 | `216.152.155.54:443` | True | 84 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 84ms |
| 28 | `69.164.240.85:50875` | True | 45 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 45ms |
| 29 | `157.254.38.210:20103` | True | 2168 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2168ms |
| 30 | `45.138.100.248:10444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 31 | `47.253.226.114:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 32 | `66.163.112.13:443` | True | 190 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 190ms |
| 33 | `69.48.201.136:30016` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 34 | `sclass-01.catcat321.com:20103` | True | 3158 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 3158ms |
| 35 | `143.246.62.191:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 36 | `216.152.155.131:443` | True | 130 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 130ms |
| 37 | `15.204.97.198:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 38 | `143.246.60.254:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 39 | `66.163.122.26:443` | True | 40 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 40ms |
| 40 | `34.24.25.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 41 | `167.88.61.193:443` | True | 247 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 247ms |
| 42 | `c9na.mediastok.shop:2405` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 43 | `216.152.156.49:443` | True | 167 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 167ms |
| 44 | `66.94.121.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 45 | `leviko-pl7089.shopingggg.ir:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 46 | `179.254.191.251:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 47 | `bl1.nexfile.net:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 48 | `179.253.80.175:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 49 | `swo2.nexfile.net:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 50 | `47.89.232.46:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 51 | `206.189.229.48:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 52 | `107.149.232.92:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 53 | `starlink-ft.251313.xyz:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 54 | `support.zoom.us:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 55 | `24.233.8.109:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 56 | `ee.veltrosub.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 57 | `38.76.150.108:36712` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 58 | `167.88.61.175:443` | True | 368 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 368ms |
| 59 | `216.152.156.42:443` | True | 157 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 157ms |
| 60 | `48.102.214.171:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 61 | `201.34.142.108:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 62 | `www.zoom.us:443` | True | 1388 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1388ms |
| 63 | `216.106.186.46:443` | True | 206 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 206ms |
| 64 | `bl1.nexfile.net:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 65 | `skk.moe:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 66 | `time.is:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 67 | `104.18.141.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 68 | `104.18.140.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 69 | `104.18.138.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 70 | `104.18.137.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 71 | `104.18.139.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 72 | `chess.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 73 | `5.34.178.120:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 74 | `104.16.10.234:443` | True | 1166 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1166ms |
| 75 | `104.18.37.127:443` | True | 667 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 667ms |
| 76 | `104.21.70.228:443` | True | 3081 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 3081ms |
| 77 | `162.159.254.3:443` | True | 1381 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1381ms |
| 78 | `104.21.70.21:443` | True | 3017 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 3017ms |
| 79 | `104.21.0.87:443` | True | 1331 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1331ms |
| 80 | `104.19.33.237:443` | True | 836 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 836ms |
| 81 | `172.67.217.240:443` | True | 960 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 960ms |
| 82 | `104.18.42.98:443` | True | 656 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 656ms |
| 83 | `104.24.31.89:443` | True | 1247 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1247ms |
| 84 | `15.204.97.216:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 85 | `162.252.199.207:404` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 86 | `48.102.217.33:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 87 | `157.245.129.175:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 88 | `192.81.216.54:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 89 | `137.184.73.123:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 90 | `165.22.191.35:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 91 | `67.205.135.247:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 92 | `178.128.145.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 93 | `162.243.174.87:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 94 | `143.244.159.16:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 95 | `67.207.87.44:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 96 | `104.248.62.43:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 97 | `render.com:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 98 | `216.152.156.81:443` | True | 166 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 166ms |
| 99 | `31.57.185.176:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 100 | `user.betust.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 101 | `179.253.85.127:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 102 | `104.16.0.1:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 103 | `50.7.169.243:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 104 | `47.251.108.158:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 105 | `216.227.161.95:7443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 106 | `66.163.122.81:443` | True | 109 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 109ms |
| 107 | `195.123.240.65:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 108 | `172.233.197.235:63815` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 109 | `169.197.140.208:443` | True | 180 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 180ms |
| 110 | `216.152.155.50:443` | True | 111 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 111ms |
| 111 | `187.55.172.33:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 112 | `216.106.186.33:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 113 | `167.17.69.171:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 114 | `170.114.46.6:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 115 | `38.244.5.231:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 116 | `13.143.187.220:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 117 | `pl.galacticworld.online:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 118 | `leviko-de6003.shopingggg.ir:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 119 | `172.67.146.84:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 120 | `216.152.156.65:443` | True | 178 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 178ms |
| 121 | `172.64.150.43:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 122 | `150.241.87.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 123 | `179.254.92.190:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 124 | `45.61.186.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 125 | `104.19.48.107:443` | True | 1562 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1562ms |
| 126 | `104.19.33.25:443` | True | 2713 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2713ms |
| 127 | `104.19.164.155:443` | True | 1076 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1076ms |
| 128 | `clash.ddm4.cn:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 129 | `104.16.111.202:443` | True | 1750 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1750ms |
| 130 | `104.17.3.81:443` | True | 2708 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2708ms |
| 131 | `104.16.10.56:443` | True | 1753 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1753ms |
| 132 | `104.21.33.59:443` | True | 801 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 801ms |
| 133 | `104.16.111.102:443` | True | 3422 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 3422ms |
| 134 | `2.26.187.132:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 135 | `199.7.140.201:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 136 | `15.204.97.206:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 137 | `170.114.45.6:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 138 | `panel.apexkey.store:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 139 | `156.229.167.109:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 140 | `104.16.0.1:443` | True | 2248 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2248ms |
| 141 | `144.31.28.228:2096` | True | 517 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 517ms |
| 142 | `43.255.157.53:48158` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 143 | `ujp.xn--ghqu5fm27b67w.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 144 | `fr-free.fastestrelay.com:443` | True | 798 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 798ms |
| 145 | `172.67.156.147:443` | True | 1883 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1883ms |
| 146 | `162.35.101.177:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 147 | `lists.soloramtin.cyou:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 148 | `kuruish.org:443` | True | 478 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 478ms |
| 149 | `179.254.92.134:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 150 | `195.211.98.43:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 151 | `104.17.70.206:8443` | True | 1183 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1183ms |
| 152 | `67.220.73.204:16016` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 153 | `159.89.87.21:28190` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 154 | `50.117.15.225:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 155 | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 156 | `146.75.57.238:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 157 | `146.75.59.186:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 158 | `151.101.109.223:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 159 | `151.101.69.223:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 160 | `167.82.76.31:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 161 | `199.232.20.113:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 162 | `199.232.77.215:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 163 | `199.232.78.160:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 164 | `23.235.33.98:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 165 | `103.133.1.160:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 166 | `104.16.10.100:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 167 | `104.16.10.104:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 168 | `104.16.10.9:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 169 | `104.16.107.139:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 170 | `104.16.144.131:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 171 | `104.16.150.108:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 172 | `104.16.171.121:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 173 | `104.16.172.173:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 174 | `104.16.174.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 175 | `104.16.174.117:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 176 | `104.16.174.124:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 177 | `104.16.174.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 178 | `104.16.174.148:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 179 | `104.16.174.185:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 180 | `104.16.174.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 181 | `104.16.174.34:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 182 | `104.16.174.36:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 183 | `104.16.174.37:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 184 | `104.16.174.44:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 185 | `104.16.174.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 186 | `104.16.183.83:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 187 | `104.16.184.194:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 188 | `104.16.203.166:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 189 | `104.16.214.14:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 190 | `104.16.241.253:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 191 | `104.16.38.60:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 192 | `104.16.40.145:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 193 | `104.16.52.89:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 194 | `104.16.6.70:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 195 | `104.16.63.239:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 196 | `104.16.7.70:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 197 | `104.16.7.70:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 198 | `104.16.71.213:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 199 | `104.16.72.50:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 200 | `104.16.72.70:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 201 | `104.16.75.207:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 202 | `104.16.79.73:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 203 | `104.16.8.237:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 204 | `104.16.89.120:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 205 | `104.17.104.23:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 206 | `104.17.107.134:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 207 | `104.17.121.43:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 208 | `104.17.121.71:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 209 | `104.17.145.145:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 210 | `104.17.148.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 211 | `104.17.161.24:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 212 | `104.17.162.123:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 213 | `104.17.177.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 214 | `104.17.23.106:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 215 | `104.17.26.230:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 216 | `104.17.54.188:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 217 | `104.17.72.206:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 218 | `104.18.109.147:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 219 | `104.18.11.110:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 220 | `104.18.12.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 221 | `104.18.15.19:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 222 | `104.18.151.172:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 223 | `104.18.152.113:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 224 | `104.18.152.133:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 225 | `104.18.152.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 226 | `104.18.152.144:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 227 | `104.18.152.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 228 | `104.18.152.155:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 229 | `104.18.152.159:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 230 | `104.18.152.187:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 231 | `104.18.152.208:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 232 | `104.18.152.210:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 233 | `104.18.152.229:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 234 | `104.18.152.244:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 235 | `104.18.152.77:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 236 | `104.18.22.208:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 237 | `104.18.33.162:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 238 | `104.18.35.86:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 239 | `104.18.35.86:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 240 | `104.18.39.55:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 241 | `104.18.39.91:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 242 | `104.18.43.29:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 243 | `104.18.46.234:2082` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 244 | `104.18.46.234:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 245 | `104.19.141.129:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 246 | `104.19.144.99:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 247 | `104.19.214.98:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 248 | `104.19.229.21:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 249 | `104.19.229.21:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 250 | `104.19.64.105:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 251 | `104.20.6.134:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 252 | `104.21.12.87:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 253 | `104.21.16.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 254 | `104.21.227.134:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 255 | `104.21.236.63:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 256 | `104.21.48.1:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 257 | `104.21.60.109:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 258 | `104.21.70.21:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 259 | `104.21.74.8:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 260 | `104.21.80.1:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 261 | `104.21.80.209:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 262 | `104.24.0.184:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 263 | `104.24.167.96:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 264 | `104.24.189.102:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 265 | `104.24.196.67:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 266 | `104.24.198.111:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 267 | `104.24.218.13:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 268 | `104.24.219.162:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 269 | `104.24.248.204:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 270 | `104.24.248.85:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 271 | `104.24.52.41:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 272 | `104.24.66.98:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 273 | `104.24.85.213:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 274 | `104.24.87.230:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 275 | `104.25.0.1:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 276 | `104.25.122.72:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 277 | `104.25.95.49:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 278 | `104.26.0.32:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 279 | `104.26.13.40:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 280 | `104.26.13.54:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 281 | `104.26.14.137:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 282 | `104.26.15.137:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 283 | `104.26.4.60:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 284 | `108.162.194.165:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 285 | `108.162.198.178:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 286 | `108.162.198.178:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 287 | `108.162.198.178:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 288 | `108.162.198.178:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 289 | `108.162.198.178:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 290 | `141.101.90.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 291 | `146.75.57.7:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 292 | `151.101.1.57:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 293 | `151.101.110.219:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 294 | `151.101.129.57:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 295 | `151.101.2.219:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 296 | `151.101.36.88:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 297 | `159.246.55.251:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 298 | `162.159.12.212:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 299 | `162.159.15.39:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 300 | `162.159.153.4:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 301 | `162.159.156.214:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 302 | `162.159.198.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 303 | `162.159.24.39:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 304 | `162.159.39.153:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 305 | `162.159.42.163:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 306 | `162.159.43.187:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 307 | `162.159.46.0:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 308 | `162.159.60.167:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 309 | `162.159.91.211:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 310 | `165.215.250.14:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 311 | `167.68.4.199:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 312 | `167.82.101.159:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 313 | `167.82.64.7:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 314 | `167.82.79.164:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 315 | `170.114.45.6:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 316 | `172.64.149.54:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 317 | `172.64.150.28:2082` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 318 | `172.64.153.100:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 319 | `172.64.157.230:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 320 | `172.64.159.64:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 321 | `172.64.229.114:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 322 | `172.64.38.50:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 323 | `172.64.88.168:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 324 | `172.64.88.251:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 325 | `172.65.90.52:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 326 | `172.67.139.85:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 327 | `172.67.155.199:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 328 | `172.67.204.84:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 329 | `172.67.208.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 330 | `172.67.209.127:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 331 | `172.67.68.248:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 332 | `172.67.74.10:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 333 | `172.67.74.2:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 334 | `173.245.49.114:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 335 | `173.245.49.157:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 336 | `173.245.58.183:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 337 | `188.114.96.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 338 | `188.114.96.37:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 339 | `188.114.97.2:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 340 | `188.114.97.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 341 | `188.114.97.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 342 | `188.114.97.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 343 | `188.114.97.6:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 344 | `188.114.98.0:443` | True | 29 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 29ms |
| 345 | `192.0.54.181:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 346 | `198.202.211.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 347 | `199.181.197.176:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 348 | `199.232.245.94:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 349 | `199.232.249.131:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 350 | `199.232.78.150:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 351 | `208.103.161.5:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 352 | `216.24.57.1:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 353 | `8.6.112.6:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 354 | `80.66.196.231:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 355 | `104.16.10.121:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 356 | `104.16.174.12:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 357 | `104.16.174.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 358 | `104.16.174.81:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 359 | `104.16.183.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 360 | `104.16.19.242:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 361 | `104.16.209.187:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 362 | `104.16.233.169:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 363 | `104.16.25.21:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 364 | `104.16.80.73:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 365 | `104.17.217.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 366 | `104.18.152.161:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 367 | `104.18.152.219:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 368 | `104.18.152.225:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 369 | `104.18.152.233:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 370 | `104.18.155.229:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 371 | `104.18.26.90:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 372 | `104.18.28.234:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 373 | `104.19.250.20:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 374 | `104.24.140.39:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 375 | `104.24.172.153:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 376 | `104.24.247.189:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 377 | `104.24.91.178:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 378 | `104.26.13.31:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 379 | `104.26.4.230:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 380 | `104.26.4.57:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 381 | `104.26.6.89:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 382 | `141.193.27.4:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 383 | `162.159.253.41:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 384 | `162.159.3.176:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 385 | `172.64.144.198:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 386 | `172.64.148.165:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 387 | `172.64.148.248:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 388 | `172.64.154.8:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 389 | `172.66.170.172:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 390 | `172.66.170.53:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 391 | `172.66.40.99:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 392 | `162.35.38.156:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 393 | `sclass-b1.catcat321.com:20027` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 394 | `sclass-b1.catcat321.com:20028` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 395 | `163.192.14.135:50160` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 396 | `155.248.209.237:33333` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 397 | `us.mi11o4ka.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 398 | `support.zoom.us:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 399 | `188.114.98.0:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 400 | `104.19.12.94:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 401 | `n04.jinggai.online:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 402 | `170.114.45.6:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 403 | `45.76.172.197:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 404 | `104.17.50.227:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 405 | `129.213.91.185:35013` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 406 | `66.163.114.45:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 407 | `45.32.69.110:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 408 | `51.81.203.63:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 409 | `31.172.69.31:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 410 | `198.46.146.118:36720` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 411 | `66.163.112.121:443` | True | 180 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 180ms |
| 412 | `us007.zestapp778.com:42314` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 413 | `104.16.10.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 414 | `104.18.40.171:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 415 | `170.114.46.6:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 416 | `104.17.50.53:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 417 | `104.21.6.186:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 418 | `154.26.188.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 419 | `15.204.97.214:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 420 | `144.202.126.147:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 421 | `185.168.208.190:47443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 422 | `fast.145779.xyz:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 423 | `167.148.201.99:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 424 | `66.163.112.242:443` | True | 189 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 189ms |
| 425 | `66.163.114.132:443` | True | 173 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 173ms |
| 426 | `104.16.10.185:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 427 | `saas.sin.fan:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 428 | `saas.sin.fan:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 429 | `us1.oh-node.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 430 | `162.35.8.62:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 431 | `104.16.10.2:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 432 | `15.204.97.219:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 433 | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | True | 472 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 472ms |
| 434 | `66.163.114.245:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 435 | `66.163.114.114:443` | True | 153 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 153ms |
| 436 | `66.163.114.166:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 437 | `66.163.112.76:443` | True | 195 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 195ms |
| 438 | `66.163.114.106:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 439 | `216.152.155.59:443` | True | 111 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 111ms |
| 440 | `170.101.101.67:443` | True | 110 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 110ms |
| 441 | `170.101.101.19:443` | True | 89 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 89ms |
| 442 | `104.17.210.74:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 443 | `104.21.34.106:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 444 | `www.speedtest.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 445 | `us3.oh-node.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 446 | `45.63.53.81:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 447 | `108.61.119.63:18580` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 448 | `195.123.235.183:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 449 | `2.24.124.64:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 450 | `xray1-direct-mci1-fs-ce.freesocks.work:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 451 | `54.71.51.243:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 452 | `66.163.112.31:443` | True | 194 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 194ms |
| 453 | `216.152.155.23:443` | True | 63 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 63ms |
| 454 | `169.197.140.169:443` | True | 168 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 168ms |
| 455 | `169.197.140.245:443` | True | 170 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 170ms |
| 456 | `169.197.140.218:443` | True | 177 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 177ms |
| 457 | `172.64.152.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 458 | `107.191.58.86:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 459 | `172.236.241.130:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 460 | `172.235.63.167:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 461 | `172.233.129.65:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 462 | `172.236.227.60:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 463 | `172.235.37.168:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 464 | `45.32.70.42:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 465 | `172.235.48.245:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 466 | `172.233.129.172:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 467 | `172.236.233.130:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 468 | `66.163.112.171:443` | True | 194 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 194ms |
| 469 | `172.233.142.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 470 | `66.163.112.147:443` | True | 190 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 190ms |
| 471 | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | True | 224 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 224ms |
| 472 | `107.191.58.86:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 473 | `172.236.241.130:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 474 | `172.235.63.167:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 475 | `172.233.129.65:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 476 | `66.163.114.106:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 477 | `172.236.227.60:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 478 | `172.235.37.168:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 479 | `45.32.70.42:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 480 | `172.235.48.245:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 481 | `172.233.129.172:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 482 | `172.236.233.130:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 483 | `66.163.112.171:` | True | 200 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 200ms |
| 484 | `66.163.112.31:` | True | 202 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 202ms |
| 485 | `172.233.142.149:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 486 | `66.163.112.242:` | True | 174 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 174ms |
| 487 | `170.101.101.211:` | True | 1141 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1141ms |
| 488 | `216.106.186.82:` | True | 190 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 190ms |
| 489 | `66.163.112.147:` | True | 178 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 178ms |
| 490 | `blog.findlocaljobnetworkandbuildcommunityconnections.com:` | True | 194 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 194ms |
| 491 | `216.106.186.46:` | True | 195 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 195ms |
| 492 | `66.163.122.30:` | True | 34 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 34ms |
| 493 | `sclass-01.catcat321.com:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 494 | `179.255.132.69:443` | True | 186 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 186ms |
| 495 | `8f72d47c-tovmo0-tou0p4-1ji20.sj.gotochinatown.net:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 496 | `8f72d47c-tovmo0-tou0p4-1ji20.sj.gotochinatown.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |

## 说明

- 本报告为**协议级**测活：内核真实完成所选协议握手并经代理发起 HTTP 请求，
  比端口级 TCP/UDP 探测可靠得多；alive 的节点经客户端导入理应可用。
- 国内用户仍可能受本地网络/GFW 影响，最终以客户端实测为准。

