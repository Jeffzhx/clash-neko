# U4 内核级真实测活报告

- 生成时间：2026-11-20T10:45:13+00:00
- 引擎：mihomo external-controller `/proxies/{name}/delay`（内核 v1.19.34）
- 测活 URL：`http://www.gstatic.com/generate_204`；单节点超时 8000ms
- 判定：alive 45 / dead 576 / unknown 0
- 预校验剔除非法节点：4（内核 -t 检出的坏字段节点，不进测活也不进订阅）

## 逐节点（server:port / 判定 / 延迟 / 依据）

| # | server:port | 判定 | 延迟(ms) | 依据 |
|---|-------------|------|----------|------|
| 1 | `167.88.61.85:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 2 | `167.88.61.193:443` | True | 245 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 245ms |
| 3 | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 4 | `150.241.83.223:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 5 | `216.152.155.50:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 6 | `216.106.186.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 7 | `167.88.61.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 8 | `66.163.112.171:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 9 | `169.197.140.171:443` | True | 1321 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1321ms |
| 10 | `45.138.100.248:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 11 | `216.152.156.49:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 12 | `198.247.127.131:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 13 | `170.101.101.131:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 14 | `167.88.61.198:443` | True | 232 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 232ms |
| 15 | `167.17.69.171:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 16 | `66.163.122.26:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 17 | `170.101.101.19:443` | True | 1886 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1886ms |
| 18 | `170.101.101.112:443` | True | 1856 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1856ms |
| 19 | `170.101.101.211:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 20 | `216.152.155.131:443` | True | 1338 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1338ms |
| 21 | `169.197.140.169:443` | True | 1202 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1202ms |
| 22 | `216.152.156.159:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 23 | `167.88.61.20:443` | True | 226 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 226ms |
| 24 | `147.45.60.136:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 25 | `69.48.201.136:30016` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 26 | `45.144.112.55:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 27 | `159.89.87.21:28190` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 28 | `15.204.97.195:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 29 | `170.101.101.53:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 30 | `66.163.114.45:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 31 | `ww13.levikogjgfdd.ir:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 32 | `216.152.156.81:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 33 | `170.101.101.237:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 34 | `216.152.156.212:443` | True | 152 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 152ms |
| 35 | `66.163.112.31:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 36 | `179.254.191.251:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 37 | `bl1.nexfile.net:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 38 | `66.163.112.13:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 39 | `34.24.25.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 40 | `167.88.61.175:443` | True | 217 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 217ms |
| 41 | `render.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 42 | `15.204.97.206:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 43 | `192.200.160.42:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 44 | `swo2.nexfile.net:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 45 | `104.168.109.213:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 46 | `leviko-pl7089.shopingggg.ir:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 47 | `179.253.80.175:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 48 | `bl1.nexfile.net:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 49 | `179.254.191.251:4443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 50 | `5.34.178.120:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 51 | `216.152.155.158:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 52 | `201.34.142.108:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 53 | `66.23.203.21:59689` | True | 195 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 195ms |
| 54 | `48.102.218.118:8443` | True | 743 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 743ms |
| 55 | `216.152.156.42:443` | True | 174 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 174ms |
| 56 | `206.189.229.48:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 57 | `47.89.232.46:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 58 | `66.94.121.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 59 | `vpn-hk-004.fastervpn.world:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 60 | `24.233.8.109:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 61 | `69.164.240.85:50875` | True | 41 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 41ms |
| 62 | `216.219.92.130:25155` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 63 | `104.18.138.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 64 | `104.18.141.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 65 | `104.18.140.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 66 | `104.18.137.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 67 | `104.18.139.67:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 68 | `38.76.150.108:36712` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 69 | `142.249.78.7:10696` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 70 | `5.78.51.198:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 71 | `172.67.67.89:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 72 | `162.159.237.118:2083` | True | 7852 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 7852ms |
| 73 | `162.159.160.117:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 74 | `104.18.63.135:2083` | True | 7057 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 7057ms |
| 75 | `104.17.145.145:2083` | True | 6412 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 6412ms |
| 76 | `162.35.38.156:25155` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 77 | `13.219.53.87:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 78 | `user.betust.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 79 | `31.57.185.176:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 80 | `leviko-us2057.shopingggg.ir:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 81 | `169.197.140.208:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 82 | `15.204.97.216:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 83 | `148.135.86.162:10000` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 84 | `23.19.231.244:61019` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 85 | `render.com:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 86 | `18.227.151.228:34675` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 87 | `38.244.5.231:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 88 | `47.251.108.158:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 89 | `2.24.124.64:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 90 | `104.17.3.81:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 91 | `45.138.100.248:10443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 92 | `panel.apexkey.store:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 93 | `147.224.54.25:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 94 | `pl.galacticworld.online:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 95 | `143.246.60.254:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 96 | `143.246.62.191:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 97 | `edge.bookmai.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 98 | `de01.node.qixi.best:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 99 | `198.202.24.142:2083` | True | 5482 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 5482ms |
| 100 | `199.242.185.178:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 101 | `64.178.113.127:443` | True | 6912 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 6912ms |
| 102 | `3.147.205.191:21801` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 103 | `45.138.100.248:10444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 104 | `104.19.180.169:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 105 | `154.12.49.239:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 106 | `179.254.92.190:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 107 | `it01.node.qixi.best:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 108 | `104.19.33.237:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 109 | `leviko-de6003.shopingggg.ir:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 110 | `66.163.122.81:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 111 | `129.153.128.162:853` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 112 | `13.143.187.220:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 113 | `uspanel.unixzone.us:30016` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 114 | `45.61.186.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 115 | `150.241.87.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 116 | `172.64.79.163:2083` | True | 7137 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 7137ms |
| 117 | `50.7.169.243:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 118 | `195.123.240.65:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 119 | `144.31.28.228:2096` | True | 515 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 515ms |
| 120 | `170.114.46.6:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 121 | `199.7.140.201:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 122 | `179.254.92.134:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 123 | `162.35.101.177:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 124 | `47.251.25.74:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 125 | `47.253.226.114:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 126 | `ujp.xn--ghqu5fm27b67w.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 127 | `170.101.101.67:443` | True | 2527 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2527ms |
| 128 | `48.102.214.171:4444` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 129 | `lists.soloramtin.cyou:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 130 | `50.117.15.225:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 131 | `66.163.112.242:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 132 | `156.229.167.109:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 133 | `104.16.10.100:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 134 | `104.16.144.131:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 135 | `104.16.150.108:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 136 | `104.16.172.173:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 137 | `104.16.174.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 138 | `104.16.174.34:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 139 | `104.16.174.36:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 140 | `104.16.174.37:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 141 | `104.16.174.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 142 | `104.16.25.21:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 143 | `104.16.38.60:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 144 | `104.16.40.145:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 145 | `104.16.6.70:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 146 | `104.16.79.73:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 147 | `104.17.104.23:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 148 | `104.17.148.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 149 | `104.17.162.123:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 150 | `104.17.217.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 151 | `104.17.54.188:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 152 | `104.18.109.147:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 153 | `104.18.152.133:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 154 | `104.18.152.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 155 | `104.18.152.161:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 156 | `104.18.152.210:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 157 | `104.18.152.225:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 158 | `104.18.155.229:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 159 | `104.18.22.208:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 160 | `104.18.46.234:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 161 | `104.19.229.21:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 162 | `104.19.250.20:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 163 | `104.21.16.1:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 164 | `104.21.16.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 165 | `104.21.33.59:443` | True | 5038 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 5038ms |
| 166 | `104.21.39.30:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 167 | `104.21.74.214:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 168 | `104.21.79.246:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 169 | `104.24.248.85:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 170 | `104.24.85.213:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 171 | `104.26.14.137:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 172 | `104.26.4.230:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 173 | `104.26.4.60:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 174 | `104.26.6.89:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 175 | `108.162.194.165:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 176 | `108.162.198.178:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 177 | `141.193.27.4:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 178 | `146.75.59.186:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 179 | `151.101.1.57:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 180 | `151.101.109.223:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 181 | `151.101.110.219:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 182 | `151.101.129.57:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 183 | `151.101.2.219:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 184 | `162.159.130.234:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 185 | `162.159.198.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 186 | `162.159.24.39:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 187 | `162.159.3.176:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 188 | `162.159.43.187:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 189 | `162.159.60.167:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 190 | `162.159.91.211:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 191 | `167.82.64.7:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 192 | `167.82.76.31:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 193 | `167.82.79.164:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 194 | `172.64.144.198:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 195 | `172.64.149.54:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 196 | `172.64.157.230:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 197 | `172.64.159.64:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 198 | `172.64.229.114:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 199 | `172.64.52.230:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 200 | `172.64.53.74:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 201 | `172.64.86.167:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 202 | `172.65.90.52:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 203 | `172.66.214.247:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 204 | `172.67.143.56:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 205 | `172.67.149.60:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 206 | `172.67.155.199:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 207 | `172.67.155.65:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 208 | `172.67.158.89:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 209 | `172.67.204.84:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 210 | `172.67.208.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 211 | `172.67.209.127:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 212 | `172.67.213.218:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 213 | `173.245.49.157:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 214 | `188.114.96.3:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 215 | `188.114.96.37:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 216 | `188.114.97.2:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 217 | `188.114.97.4:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 218 | `188.114.97.6:2082` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 219 | `188.114.97.6:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 220 | `188.114.98.0:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 221 | `192.0.54.181:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 222 | `199.232.20.113:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 223 | `199.232.245.94:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 224 | `199.232.77.215:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 225 | `199.232.78.150:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 226 | `208.103.161.5:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 227 | `69.46.46.106:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 228 | `69.46.46.109:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 229 | `69.46.46.113:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 230 | `69.46.46.114:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 231 | `69.46.46.121:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 232 | `69.46.46.142:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 233 | `69.46.46.144:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 234 | `8.6.112.6:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 235 | `103.133.1.160:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 236 | `104.16.10.104:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 237 | `104.16.10.121:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 238 | `104.16.10.9:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 239 | `104.16.107.139:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 240 | `104.16.171.121:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 241 | `104.16.174.117:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 242 | `104.16.174.12:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 243 | `104.16.174.124:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 244 | `104.16.174.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 245 | `104.16.174.148:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 246 | `104.16.174.185:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 247 | `104.16.174.44:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 248 | `104.16.174.46:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 249 | `104.16.174.81:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 250 | `104.16.183.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 251 | `104.16.183.83:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 252 | `104.16.184.194:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 253 | `104.16.19.242:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 254 | `104.16.203.166:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 255 | `104.16.209.187:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 256 | `104.16.214.14:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 257 | `104.16.233.169:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 258 | `104.16.241.253:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 259 | `104.16.7.70:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 260 | `104.16.7.70:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 261 | `104.16.71.213:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 262 | `104.16.8.237:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 263 | `104.16.80.73:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 264 | `104.17.107.134:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 265 | `104.17.121.43:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 266 | `104.17.121.71:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 267 | `104.17.148.111:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 268 | `104.17.161.24:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 269 | `104.17.177.143:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 270 | `104.17.23.106:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 271 | `104.17.26.230:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 272 | `104.18.11.110:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 273 | `104.18.12.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 274 | `104.18.15.19:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 275 | `104.18.151.172:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 276 | `104.18.152.113:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 277 | `104.18.152.144:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 278 | `104.18.152.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 279 | `104.18.152.155:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 280 | `104.18.152.159:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 281 | `104.18.152.187:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 282 | `104.18.152.208:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 283 | `104.18.152.219:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 284 | `104.18.152.229:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 285 | `104.18.152.233:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 286 | `104.18.152.244:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 287 | `104.18.152.77:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 288 | `104.18.26.90:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 289 | `104.18.28.234:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 290 | `104.18.33.162:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 291 | `104.18.35.86:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 292 | `104.18.39.91:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 293 | `104.18.4.138:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 294 | `104.18.43.29:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 295 | `104.18.46.234:2082` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 296 | `104.19.141.129:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 297 | `104.19.144.99:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 298 | `104.19.214.98:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 299 | `104.19.229.21:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 300 | `104.19.64.105:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 301 | `104.20.6.134:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 302 | `104.21.12.87:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 303 | `104.21.23.29:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 304 | `104.21.236.63:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 305 | `104.21.32.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 306 | `104.21.38.220:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 307 | `104.21.38.220:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 308 | `104.21.48.1:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 309 | `104.21.60.109:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 310 | `104.21.63.28:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 311 | `104.21.64.1:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 312 | `104.21.70.21:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 313 | `104.21.74.8:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 314 | `104.21.80.1:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 315 | `104.21.80.209:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 316 | `104.21.89.181:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 317 | `104.21.91.244:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 318 | `104.24.140.39:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 319 | `104.24.167.96:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 320 | `104.24.172.153:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 321 | `104.24.189.102:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 322 | `104.24.196.67:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 323 | `104.24.198.111:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 324 | `104.24.218.13:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 325 | `104.24.219.162:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 326 | `104.24.247.189:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 327 | `104.24.52.41:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 328 | `104.24.66.98:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 329 | `104.24.87.230:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 330 | `104.24.91.178:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 331 | `104.25.0.1:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 332 | `104.25.122.72:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 333 | `104.26.0.32:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 334 | `104.26.13.31:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 335 | `104.26.13.40:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 336 | `104.26.13.54:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 337 | `104.26.15.137:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 338 | `104.26.4.57:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 339 | `104.27.88.172:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 340 | `108.162.198.178:2095` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 341 | `108.162.198.178:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 342 | `108.162.198.178:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 343 | `108.162.198.178:2086` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 344 | `141.101.90.101:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 345 | `15.204.210.176:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 346 | `151.101.36.88:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 347 | `159.246.55.251:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 348 | `162.159.12.212:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 349 | `162.159.15.39:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 350 | `162.159.153.4:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 351 | `162.159.156.214:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 352 | `162.159.253.41:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 353 | `162.159.39.153:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 354 | `162.159.42.163:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 355 | `162.159.46.0:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 356 | `165.215.250.14:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 357 | `167.68.4.199:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 358 | `172.64.148.165:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 359 | `172.64.148.248:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 360 | `172.64.150.28:2082` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 361 | `172.64.153.100:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 362 | `172.64.153.105:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 363 | `172.64.154.113:8443` | True | 64 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 64ms |
| 364 | `172.64.154.8:2052` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 365 | `172.64.38.50:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 366 | `172.64.88.168:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 367 | `172.64.88.251:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 368 | `172.64.92.243:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 369 | `172.66.140.62:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 370 | `172.66.170.53:8880` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 371 | `172.66.40.99:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 372 | `172.67.139.85:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 373 | `172.67.139.85:80` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 374 | `172.67.148.163:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 375 | `172.67.172.95:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 376 | `172.67.208.118:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 377 | `172.67.68.248:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 378 | `172.67.74.10:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 379 | `172.67.74.2:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 380 | `173.245.49.114:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 381 | `173.245.58.183:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 382 | `188.114.96.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 383 | `162.35.38.156:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 384 | `163.192.14.135:50160` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 385 | `155.248.209.237:33333` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 386 | `us.mi11o4ka.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 387 | `104.19.164.155:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 388 | `support.zoom.us:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 389 | `188.114.98.0:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 390 | `104.19.12.94:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 391 | `n04.jinggai.online:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 392 | `170.114.45.6:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 393 | `45.76.172.197:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 394 | `104.17.50.227:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 395 | `129.213.91.185:35013` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 396 | `45.32.69.110:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 397 | `51.81.203.63:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 398 | `31.172.69.31:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 399 | `198.46.146.118:36720` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 400 | `66.163.112.121:443` | True | 2253 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 2253ms |
| 401 | `us007.zestapp778.com:42314` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 402 | `104.21.70.21:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 403 | `104.16.10.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 404 | `104.18.40.171:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 405 | `170.114.46.6:8080` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 406 | `188.114.97.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 407 | `104.17.50.53:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 408 | `104.21.6.186:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 409 | `154.26.188.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 410 | `15.204.97.214:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 411 | `162.159.254.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 412 | `144.202.126.147:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 413 | `185.168.208.190:47443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 414 | `fast.145779.xyz:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 415 | `45.138.100.248:14430` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 416 | `167.148.201.99:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 417 | `66.163.114.132:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 418 | `104.16.0.1:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 419 | `104.16.10.185:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 420 | `104.16.10.56:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 421 | `saas.sin.fan:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 422 | `172.67.217.240:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 423 | `saas.sin.fan:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 424 | `us1.oh-node.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 425 | `162.35.8.62:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 426 | `104.16.10.2:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 427 | `104.19.48.107:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 428 | `15.204.97.219:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 429 | `195.211.98.43:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 430 | `104.24.31.89:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 431 | `66.163.114.245:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 432 | `66.163.114.114:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 433 | `66.163.114.166:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 434 | `66.163.112.76:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 435 | `66.163.114.106:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 436 | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 437 | `66.163.114.126:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 438 | `216.152.156.65:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 439 | `216.152.155.59:443` | True | 1301 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1301ms |
| 440 | `104.17.210.74:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 441 | `104.21.34.106:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 442 | `www.speedtest.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 443 | `us3.oh-node.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 444 | `104.21.0.87:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 445 | `45.63.53.81:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 446 | `108.61.119.63:18580` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 447 | `195.123.235.183:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 448 | `xray1-direct-mci1-fs-ce.freesocks.work:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 449 | `54.71.51.243:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 450 | `66.163.112.142:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 451 | `216.152.155.23:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 452 | `169.197.140.245:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 453 | `169.197.140.218:443` | True | 935 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 935ms |
| 454 | `104.21.70.228:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 455 | `172.64.152.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 456 | `104.18.42.98:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 457 | `104.16.205.65:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
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
| 468 | `172.233.142.149:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 469 | `216.106.186.82:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 470 | `66.163.112.147:443` | True | 3437 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 3437ms |
| 471 | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | True | 293 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 293ms |
| 472 | `66.163.122.30:443` | True | 1564 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1564ms |
| 473 | `sclass-01.catcat321.com:20103` | True | 1246 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1246ms |
| 474 | `107.191.58.86:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 475 | `172.236.241.130:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 476 | `172.235.63.167:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 477 | `172.233.129.65:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 478 | `66.163.114.106:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 479 | `172.236.227.60:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 480 | `172.235.37.168:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 481 | `45.32.70.42:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 482 | `172.235.48.245:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 483 | `172.233.129.172:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 484 | `172.236.233.130:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 485 | `66.163.112.171:` | True | 230 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 230ms |
| 486 | `66.163.112.31:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 487 | `172.233.142.149:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 488 | `66.163.112.242:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 489 | `170.101.101.211:` | True | 379 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 379ms |
| 490 | `216.106.186.82:` | True | 338 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 338ms |
| 491 | `66.163.112.147:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 492 | `blog.findlocaljobnetworkandbuildcommunityconnections.com:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 493 | `216.106.186.46:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 494 | `66.163.122.30:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 495 | `sclass-01.catcat321.com:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 496 | `172.67.217.241:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 497 | `104.17.145.138:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 498 | `172.64.153.109:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 499 | `104.18.38.159:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 500 | `104.18.14.19:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 501 | `104.19.46.190:2096` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 502 | `www.visa.com:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 503 | `cf.3666888.xyz:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 504 | `192.236.151.43:443` | True | 189 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 189ms |
| 505 | `13.143.187.220:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 506 | `172.64.153.205:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 507 | `104.17.22.231:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 508 | `146.75.57.120:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 509 | `172.64.153.205:2087` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 510 | `104.17.22.231:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 511 | `1405-4-19-ansooyefilter-telegram.up.railway.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 512 | `04b51566-9333-492b-b680-8f80752411f9.fly.dev:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 513 | `1579e6d9-6b57-4fb1-b080-9c9a6da46ae5.fly.dev:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 514 | `app.streamru13.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 515 | `38.47.119.139:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 516 | `15.204.97.198:23576` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 517 | `154.40.59.238:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 518 | `209.94.90.47:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 519 | `xray2-direct-mci1-fs-ce.freesocks.work:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 520 | `pscresearch.faculty.ucdavis.edu:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 521 | `python-graysongon.wasmer.app:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 522 | `sw1.hidenet.xyz:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 523 | `t11.qifei.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 524 | `t12.qifei.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 525 | `t17.qifei.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 526 | `14.102.228.76:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 527 | `bwdraper.faculty.ucdavis.edu:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 528 | `199.232.78.187:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 529 | `crewmen-grittier.freevideochats.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 530 | `zmaoz.faculty.ucdavis.edu:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 531 | `69.46.46.145:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 532 | `piracy-android.video-streams.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 533 | `s226.okgg.top:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 534 | `s2318.okgg.top:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 535 | `speedtest.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 536 | `earthpro.wasmer.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 537 | `199.232.78.159:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 538 | `199.232.78.199:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 539 | `grimness-backlogs.cdn-content.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 540 | `adheres-scruple.quick-cdn.net:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 541 | `Zmaoz.Faculty.Ucdavis.Edu:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 542 | `spiderpanel-development-g5884.lucity.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 543 | `86153507-1976-48f1-ac86-e8ab274470a8.fly.dev:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 544 | `bounded-crammed.video-streams.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 545 | `frfx.pafaktalaei.ir:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 546 | `gcore.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 547 | `minimize-evenness.cdn-content.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 548 | `sclass-c2.catcat321.com:20051` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 549 | `199.232.11.52:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 550 | `199.232.9.254:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 551 | `t14.qifei.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 552 | `69.46.46.22:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 553 | `104.245.240.3:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 554 | `104.245.240.6:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 555 | `151.101.215.69:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 556 | `clash.ddm4.cn:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 557 | `209.94.90.201:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 558 | `2.26.187.132:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 559 | `176.126.122.168:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 560 | `caudal-reason.freevideochats.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 561 | `131.143.180.53:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 562 | `198.202.24.214:2083` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 563 | `hiccuped-tacos.sports-streams.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 564 | `tuic.moxin1245.win:8443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 565 | `coughed-gongs.freevideochats.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 566 | `barbered-mattocks.video-streams.org:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 567 | `guessable-turnpikes.cdn-content.com:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 568 | `ir.vnexjet.ir:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 569 | `www.arizona.edu:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 570 | `s868.okgg.top:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 571 | `s9601.okgg.top:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 572 | `rodekors.dk:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 573 | `www.hivenet.com:2053` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 574 | `t-panel.wasmer.app:443` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 575 | `167.17.69.171:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 576 | `45.63.53.81:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 577 | `69.164.240.85:` | True | 48 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 48ms |
| 578 | `206.189.229.48:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 579 | `216.227.161.95:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 504: Gateway Timeout |
| 580 | `179.254.92.134:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 581 | `179.254.92.190:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 582 | `216.152.156.65:` | True | 1185 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1185ms |
| 583 | `172.235.48.213:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 584 | `170.101.101.67:` | True | 132 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 132ms |
| 585 | `170.101.101.112:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 586 | `216.152.155.59:` | True | 1019 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1019ms |
| 587 | `172.235.53.103:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 588 | `172.236.239.126:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 589 | `104.168.109.213:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 590 | `172.233.157.18:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 591 | `172.233.140.139:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 592 | `172.235.40.143:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 593 | `156.229.167.109:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 594 | `172.235.50.209:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 595 | `172.235.32.253:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 596 | `172.233.146.140:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 597 | `172.233.156.229:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 598 | `66.94.121.46:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 599 | `172.233.139.212:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 600 | `216.152.156.42:` | True | 206 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 206ms |
| 601 | `172.233.139.98:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 602 | `172.236.238.71:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 603 | `172.233.129.179:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 604 | `216.152.155.23:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 605 | `172.236.231.45:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 606 | `167.88.61.193:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 607 | `159.89.87.21:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 608 | `172.235.36.11:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 609 | `172.235.37.163:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 610 | `172.233.129.46:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 611 | `34.24.25.1:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 612 | `216.152.155.131:` | True | 1134 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 1134ms |
| 613 | `167.88.61.198:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 614 | `170.101.101.53:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 615 | `216.152.156.212:` | True | 178 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 178ms |
| 616 | `198.247.127.131:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 617 | `170.101.101.19:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 618 | `216.106.186.32:` | True | 392 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 392ms |
| 619 | `170.101.101.131:` | False | - | 有据（协议级负向）：内核测活失败：HTTPError: HTTP Error 503: Service Unavailable |
| 620 | `167.88.61.85:` | True | 231 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 231ms |
| 621 | `66.23.203.21:` | True | 195 | 有据（协议级正向）：内核协议级测活通过：协议握手 + HTTP http://www.gstatic.com/generate_204 返回 200/204，延迟 195ms |

## 说明

- 本报告为**协议级**测活：内核真实完成所选协议握手并经代理发起 HTTP 请求，
  比端口级 TCP/UDP 探测可靠得多；alive 的节点经客户端导入理应可用。
- 国内用户仍可能受本地网络/GFW 影响，最终以客户端实测为准。

