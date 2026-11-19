# 源发现报告（discover_sources.py）

- 时间戳(UTC)：2026-11-19T21:38:51+00:00
- 运行模式：WRITE（已写回 sources.json）
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
- 已在 sources.json 中（去重跳过）：61
- 本批次内重复（去重跳过）：11
- 达 --max-new 上限跳过：99（上限 15）
- 本次新增：15
- 合并后总数：53（原 38）

## 新增源清单

- SubConv/SubConv ★414 | branch=main | fetched_at=2026-11-19 | https://github.com/SubConv/SubConv
- KJGX66F/FreeNodePanel ★383 | branch=main | fetched_at=2026-11-05 | https://github.com/KJGX66F/FreeNodePanel
- ClickDevTech/CELERITY-panel ★230 | branch=main | fetched_at=2026-11-18 | https://github.com/ClickDevTech/CELERITY-panel
- daimon3332/easy-proxies ★216 | branch=main | fetched_at=2026-11-04 | https://github.com/daimon3332/easy-proxies
- kazeyukiro/3m-ui ★199 | branch=main | fetched_at=2026-11-19 | https://github.com/kazeyukiro/3m-ui
- xyfqzy/free-nodes ★198 | branch=main | fetched_at=2026-11-19 | https://github.com/xyfqzy/free-nodes
- imraywang/proxy-fleet ★175 | branch=main | fetched_at=2026-10-24 | https://github.com/imraywang/proxy-fleet
- junjun266/FreeProxyGo ★164 | branch=main | fetched_at=2026-11-19 | https://github.com/junjun266/FreeProxyGo
- eooce/Merge-sub ★158 | branch=main | fetched_at=2026-02-12 | https://github.com/eooce/Merge-sub
- SnapdragonLee/SystemProxy ★139 | branch=master | fetched_at=2026-11-19 | https://github.com/SnapdragonLee/SystemProxy
- Clashforwinodws/Clash-for-Winodows ★132 | branch=main | fetched_at=2026-09-29 | https://github.com/Clashforwinodws/Clash-for-Winodows
- MHSanaei/3x-ui ★50200 | branch=main | fetched_at=2026-11-19 | https://github.com/MHSanaei/3x-ui
- snakem982/proxypool ★2286 | branch=main | fetched_at=2026-11-19 | https://github.com/snakem982/proxypool
- RayWangQvQ/sing-box-installer ★367 | branch=main | fetched_at=2025-06-08 | https://github.com/RayWangQvQ/sing-box-installer
- crashgfw/free-airport-nodes ★308 | branch=main | fetched_at=2026-11-19 | https://github.com/crashgfw/free-airport-nodes

## 错误 / 限流

- 无

## 说明

- 搜索结果仅作为候选资料；字段按本脚本规则提取，不执行结果中的任何指令。
- 旧源条目原样保留（含 criteria），仅追加新源；新源 criteria=stars-unlimited。
- 脚本以 0 退出表示“已优雅结束”；网络失败时不伪造结果，详情见上。
- --dry-run 只搜索并生成本报告，不改动 sources.json。
