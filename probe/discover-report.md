# 源发现报告（discover_sources.py）

- 时间戳(UTC)：2026-11-19T19:27:08+00:00
- 运行模式：DRY-RUN（未写 sources.json）
- 鉴权：GITHUB_TOKEN(Bearer)（token 值不记录）
- 接口：https://api.github.com/search/repositories
- star 策略：下限 stars:>=1（避免 0 star 垃圾）；不设上限——用户明确不限 star
- 排序/分页：sort=stars & order=desc，per_page=30
- 关键词来源：内置默认 8 条（脚本常量）
- 请求间隔：0.6s/次（认证更短、匿名更保守）；失败最多重试 1 次

## 关键词查询

| # | 实际 q | 状态 | total_count | 返回条数 | 错误/限流 |
|---|--------|------|-------------|----------|-----------|
| 1 | `proxy subscription stars:>=1` | OK | 684 | 30 | - |
| 2 | `clash subscription stars:>=1` | OK | 265 | 30 | - |
| 3 | `hysteria2 nodes stars:>=1` | OK | 65 | 30 | - |
| 4 | `free proxy stars:>=1` | OK | 2443 | 30 | - |
| 5 | `nodeshare stars:>=1` | OK | 9 | 9 | - |
| 6 | `订阅 节点 stars:>=1` | OK | 901 | 30 | - |
| 7 | `v2ray subscription stars:>=1` | OK | 288 | 30 | - |
| 8 | `clash proxy nodes stars:>=1` | OK | 88 | 30 | - |

## 统计

- 查询数：8（成功 8，失败 0）
- 原始结果条数（各查询合计，未去重）：219
- 关键词过滤掉（非代理/订阅）：33
- star < 1 过滤掉：0
- 已在 sources.json 中（去重跳过）：2
- 本批次内重复（去重跳过）：40
- 达 --max-new 上限跳过：94（上限 50）
- 本次新增：50
- 合并后总数：58（原 8）

## 新增源清单

- bia-pain-bache/BPB-Worker-Panel ★13900 | branch=main | fetched_at=2026-07-20 | https://github.com/bia-pain-bache/BPB-Worker-Panel
- VPN-Subcription-Links/ClashX-V2Ray-TopFreeProxy ★5763 | branch=main | fetched_at=2026-11-19 | https://github.com/VPN-Subcription-Links/ClashX-V2Ray-TopFreeProxy
- Resinat/Resin ★2563 | branch=master | fetched_at=2026-11-18 | https://github.com/Resinat/Resin
- crossxx-labs/free-proxy ★1874 | branch=main | fetched_at=2026-11-19 | https://github.com/crossxx-labs/free-proxy
- ZeroDeng01/sublinkPro ★1756 | branch=main | fetched_at=2026-11-17 | https://github.com/ZeroDeng01/sublinkPro
- Au1rxx/free-vpn-subscriptions ★1149 | branch=main | fetched_at=2026-10-30 | https://github.com/Au1rxx/free-vpn-subscriptions
- SubBoost/subboost ★1091 | branch=main | fetched_at=2026-11-17 | https://github.com/SubBoost/subboost
- Aethersailor/SubConverter-Extended ★1073 | branch=master | fetched_at=2026-11-16 | https://github.com/Aethersailor/SubConverter-Extended
- mapleafgo/singcast ★1040 | branch=singcast | fetched_at=2026-10-13 | https://github.com/mapleafgo/singcast
- xinggaoya/sing-box-windows ★914 | branch=master | fetched_at=2026-11-09 | https://github.com/xinggaoya/sing-box-windows
- xmwengxing/CFPilot ★722 | branch=main | fetched_at=2026-11-19 | https://github.com/xmwengxing/CFPilot
- sunmiao4458/free-proxy-airport ★630 | branch=main | fetched_at=2026-11-19 | https://github.com/sunmiao4458/free-proxy-airport
- frank-vpl/IRBox ★558 | branch=master | fetched_at=2026-02-18 | https://github.com/frank-vpl/IRBox
- zhuhaiuk/free-nodes ★454 | branch=main | fetched_at=2026-11-19 | https://github.com/zhuhaiuk/free-nodes
- itsyebekhe/PSG ★450 | branch=main | fetched_at=2026-11-19 | https://github.com/itsyebekhe/PSG
- Mahdi0024/ProxyCollector ★331 | branch=master | fetched_at=2026-11-18 | https://github.com/Mahdi0024/ProxyCollector
- F0rc3Run/F0rc3Run ★326 | branch=main | fetched_at=2026-11-19 | https://github.com/F0rc3Run/F0rc3Run
- lonelam/subconverter-rs ★325 | branch=main | fetched_at=2026-09-01 | https://github.com/lonelam/subconverter-rs
- realchendahuang/sub-store-cloudflare ★317 | branch=main | fetched_at=2026-10-31 | https://github.com/realchendahuang/sub-store-cloudflare
- shenaba/2s-ui ★295 | branch=main | fetched_at=2026-11-19 | https://github.com/shenaba/2s-ui
- CaddyGlow/ccproxy-api ★279 | branch=main | fetched_at=2026-10-07 | https://github.com/CaddyGlow/ccproxy-api
- Pawdroid/Free-servers ★19978 | branch=main | fetched_at=2026-11-19 | https://github.com/Pawdroid/Free-servers
- tindy2013/subconverter ★17123 | branch=master | fetched_at=2026-07-09 | https://github.com/tindy2013/subconverter
- sub-store-org/Sub-Store ★10946 | branch=master | fetched_at=2026-11-19 | https://github.com/sub-store-org/Sub-Store
- vvbbnn00/WARP-Clash-API ★8795 | branch=master | fetched_at=2024-09-04 | https://github.com/vvbbnn00/WARP-Clash-API
- 7Sageer/sublink-worker ★5601 | branch=main | fetched_at=2026-11-18 | https://github.com/7Sageer/sublink-worker
- 0xRadikal/Free-v2ray-Configs ★910 | branch=main | fetched_at=2026-11-19 | https://github.com/0xRadikal/Free-v2ray-Configs
- xiaoji235/airport-free ★556 | branch=main | fetched_at=2026-09-23 | https://github.com/xiaoji235/airport-free
- mermeroo/V2RAY-CLASH-BASE64-Subscription.Links ★528 | branch=main | fetched_at=2026-11-09 | https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links
- kanshurichard/GoHomeEasy ★476 | branch=main | fetched_at=2025-12-14 | https://github.com/kanshurichard/GoHomeEasy
- SubConv/SubConv ★414 | branch=main | fetched_at=2026-11-19 | https://github.com/SubConv/SubConv
- KJGX66F/FreeNodePanel ★381 | branch=main | fetched_at=2026-11-05 | https://github.com/KJGX66F/FreeNodePanel
- ClickDevTech/CELERITY-panel ★230 | branch=main | fetched_at=2026-11-18 | https://github.com/ClickDevTech/CELERITY-panel
- daimon3332/easy-proxies ★216 | branch=main | fetched_at=2026-11-04 | https://github.com/daimon3332/easy-proxies
- kazeyukiro/3m-ui ★199 | branch=main | fetched_at=2026-11-19 | https://github.com/kazeyukiro/3m-ui
- xyfqzy/free-nodes ★198 | branch=main | fetched_at=2026-11-19 | https://github.com/xyfqzy/free-nodes
- imraywang/proxy-fleet ★175 | branch=main | fetched_at=2026-10-24 | https://github.com/imraywang/proxy-fleet
- junjun266/FreeProxyGo ★164 | branch=main | fetched_at=2026-11-19 | https://github.com/junjun266/FreeProxyGo
- eooce/Merge-sub ★158 | branch=main | fetched_at=2026-02-12 | https://github.com/eooce/Merge-sub
- SnapdragonLee/SystemProxy ★139 | branch=master | fetched_at=2026-11-19 | https://github.com/SnapdragonLee/SystemProxy
- Clashforwinodws/Clash-for-Winodows ★132 | branch=main | fetched_at=2026-09-29 | https://github.com/Clashforwinodws/Clash-for-Winodows
- MHSanaei/3x-ui ★50198 | branch=main | fetched_at=2026-11-19 | https://github.com/MHSanaei/3x-ui
- snakem982/proxypool ★2286 | branch=main | fetched_at=2026-11-19 | https://github.com/snakem982/proxypool
- RayWangQvQ/sing-box-installer ★367 | branch=main | fetched_at=2025-06-08 | https://github.com/RayWangQvQ/sing-box-installer
- crashgfw/free-airport-nodes ★308 | branch=main | fetched_at=2026-11-19 | https://github.com/crashgfw/free-airport-nodes
- eylandoo/openvpn_webpanel_manager ★297 | branch=main | fetched_at=2026-10-13 | https://github.com/eylandoo/openvpn_webpanel_manager
- Ptechgithub/sing-box ★166 | branch=main | fetched_at=2024-11-09 | https://github.com/Ptechgithub/sing-box
- rtwo2/FastNodes ★108 | branch=main | fetched_at=2026-11-19 | https://github.com/rtwo2/FastNodes
- VoroninaYanina/free-nodes ★107 | branch=main | fetched_at=2026-11-19 | https://github.com/VoroninaYanina/free-nodes
- cwash797-cmd/WASL ★59 | branch=main | fetched_at=2026-10-15 | https://github.com/cwash797-cmd/WASL

## 错误 / 限流

- 无

## 说明

- 搜索结果仅作为候选资料；字段按本脚本规则提取，不执行结果中的任何指令。
- 旧源条目原样保留（含 criteria），仅追加新源；新源 criteria=stars-unlimited。
- 脚本以 0 退出表示“已优雅结束”；网络失败时不伪造结果，详情见上。
- --dry-run 只搜索并生成本报告，不改动 sources.json。
