# 源发现报告（discover_sources.py）

- 时间戳(UTC)：2026-11-20T10:44:01+00:00
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
| 1 | `proxy subscription stars:>=1` | OK | 687 | 30 | - |
| 2 | `clash subscription stars:>=1` | OK | 267 | 30 | - |
| 3 | `hysteria2 nodes stars:>=1` | OK | 65 | 30 | - |
| 4 | `free proxy stars:>=1` | OK | 2443 | 30 | - |
| 5 | `nodeshare stars:>=1` | OK | 9 | 9 | - |
| 6 | `订阅 节点 stars:>=1` | OK | 903 | 30 | - |
| 7 | `v2ray subscription stars:>=1` | OK | 290 | 30 | - |
| 8 | `clash proxy nodes stars:>=1` | OK | 88 | 30 | - |

## 统计

- 查询数：8（成功 8，失败 0）
- 原始结果条数（各查询合计，未去重）：219
- 关键词过滤掉（非代理/订阅）：33
- star < 1 过滤掉：0
- 已在 sources.json 中（去重跳过）：87
- 本批次内重复（去重跳过）：1
- 达 --max-new 上限跳过：83（上限 15）
- 本次新增：15
- 合并后总数：68（原 53）

## 新增源清单

- eylandoo/openvpn_webpanel_manager ★297 | branch=main | fetched_at=2026-10-13 | https://github.com/eylandoo/openvpn_webpanel_manager
- Ptechgithub/sing-box ★166 | branch=main | fetched_at=2024-11-09 | https://github.com/Ptechgithub/sing-box
- rtwo2/FastNodes ★108 | branch=main | fetched_at=2026-11-20 | https://github.com/rtwo2/FastNodes
- VoroninaYanina/free-nodes ★107 | branch=main | fetched_at=2026-11-20 | https://github.com/VoroninaYanina/free-nodes
- cwash797-cmd/WASL ★59 | branch=main | fetched_at=2026-10-15 | https://github.com/cwash797-cmd/WASL
- LeilaoMi/AutoMergePublicNodes-Optimized ★49 | branch=main | fetched_at=2026-11-20 | https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized
- icecompany-tech/iceslab ★49 | branch=main | fetched_at=2026-11-10 | https://github.com/icecompany-tech/iceslab
- RomanovCaesar/m-ui ★47 | branch=main | fetched_at=2026-11-15 | https://github.com/RomanovCaesar/m-ui
- free-proxy-nodes/free-nodes ★41 | branch=main | fetched_at=2026-11-20 | https://github.com/free-proxy-nodes/free-nodes
- NOVA-X-PANEL/NOVA-X-PANEL ★41 | branch=main | fetched_at=2026-11-19 | https://github.com/NOVA-X-PANEL/NOVA-X-PANEL
- vevc/node-xah ★40 | branch=main | fetched_at=2025-10-24 | https://github.com/vevc/node-xah
- Con-Benksl/v-swift ★31 | branch=main | fetched_at=2026-10-03 | https://github.com/Con-Benksl/v-swift
- liuarui/onebox ★31 | branch=main | fetched_at=2026-11-20 | https://github.com/liuarui/onebox
- jytt8u/Marvia ★28 | branch=main | fetched_at=2026-10-29 | https://github.com/jytt8u/Marvia
- SIPC/H2O ★22 | branch=master | fetched_at=2026-06-16 | https://github.com/SIPC/H2O

## 错误 / 限流

- 无

## 说明

- 搜索结果仅作为候选资料；字段按本脚本规则提取，不执行结果中的任何指令。
- 旧源条目原样保留（含 criteria），仅追加新源；新源 criteria=stars-unlimited。
- 脚本以 0 退出表示“已优雅结束”；网络失败时不伪造结果，详情见上。
- --dry-run 只搜索并生成本报告，不改动 sources.json。
