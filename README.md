# clash-neko

每天自动从 GitHub **stars < 100** 的低星代理/订阅仓库抓取节点，只保留**美国**、**优质协议**（hysteria / hysteria2 / anytls）并**测活**的节点，生成同一批节点的**双格式订阅**，推送到 `Jeffzhx/clash-neko` 通过 jsDelivr 分发。

## 订阅地址

- Clash Verge / mihomo（YAML）：
  `https://cdn.jsdelivr.net/gh/Jeffzhx/clash-neko@main/main.yaml`
- NekoBox / sing-box（JSON）：
  `https://cdn.jsdelivr.net/gh/Jeffzhx/clash-neko@main/nekobox.json`

> jsDelivr 缓存可能延迟几分钟；手动触发 Actions 后可加 `?` 时间戳参数强制刷新。

## 特性与口径

- **来源**：GitHub stars < 100 的代理/订阅仓库（见 `sources.json`）。
- **协议**：仅 hysteria / hysteria2 / anytls；ss / vmess / vless / trojan 等一律不收。
- **地区**：仅美国。IP 字面量直查 GeoIP 库；域名解析后查；非标准 ISO 码与无效域名一律排除。
- **测活**：TCP + UDP 多手段探测，只接受有正向证据的节点；**当日 + 历史全失败时生成空列表**，绝不静默保留失效旧节点。
- **双格式**：`main.yaml`（mihomo）与 `nekobox.json`（sing-box）为**同一批节点的两种格式**，节点集合严格一致。
- **定时**：每天 UTC 03:00（北京时间 11:00）自动运行，也可在 Actions 页手动触发。

## 空订阅说明

若某次运行拿不到通过测活的美国节点，订阅会是**合法空列表**（YAML `proxies: []`、JSON 仅 direct/block）。这是符合口径的结果，不是故障；网络条件恢复后会自动重填。

## 流水线（`scripts/`）

1. `fetch_sources.py` — 用 GitHub contents API + `GITHUB_TOKEN` 抓取源，产出 `nodes_raw.json`（`.cache/` 缓存，重跑省额度）。
2. `geoip_filter.py` — GeoIP 判定，产出 `us_nodes.json` + `probe/geoip-report.md`。mmdb 路径由环境变量 `GEOIP_MMDB` 覆盖。
3. `liveness_check.py` — 测活，产出 `alive_nodes.json` + `probe/liveness-report.md`。
4. `build_subscriptions.py` — 双格式输出，产出 `main.yaml` + `nekobox.json` + `probe/subscription-build-report.md`。

## 部署（仓库维护者）

单仓方案：源码与产物都在 `Jeffzhx/clash-neko`（**必须公开**，否则 jsDelivr 分发失败），分支 `main`。

- 仓库可见性设为 **Public**（Settings → General → Danger Zone → Change visibility）。
- Actions 权限：Settings → Actions → General → Workflow permissions → 选 **Read and write permissions**（内置 `GITHUB_TOKEN` 才能 push）。
- 无需自建 PAT / Secrets；抓取提额与产物 push 都用内置 `GITHUB_TOKEN`。
- 仓库 Variables（可选）：`MMDB_URL` — GeoLite2-Country.mmdb 下载镜像地址；未设时用默认公开镜像。
- 把本项目的 `scripts/`、`probe/`、`sources.json`、`.github/workflows/build.yml`、`README.md` 提交到该仓 `main`，Actions 即按计划运行。

> token 只经 GitHub 内置机制注入，不写入任何文件。改可见性、首次 push 等不可逆步骤由维护者手动完成，agent 不代为执行。详细步骤见 `repo-setup-notes.md`。
