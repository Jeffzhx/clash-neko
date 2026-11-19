# 仓库上线待办（单仓方案，需维护者手动执行，不可逆）

> 你已选择**单仓方案**：源码与产物都在 `Jeffzhx/clash-neko`。
> 下列动作 agent **不代为执行**（建仓/改可见性/首次 push/启用 Actions 均不可逆或需密钥），
> 同样登记在 `.handoff/actions.pending.jsonl`，需你当面确认后由你自己完成。

## 第 1 步：改成公开仓库（必须，否则 jsDelivr 分发失败）

- 打开 `https://github.com/Jeffzhx/clash-neko` → **Settings** → 最底部 **Danger Zone** → **Change visibility** → 选 **Public** → 按提示确认。
- 原因：jsDelivr 的 `/gh/` 端点只服务公开仓库，没有私有仓/token 访问机制。节点是公开分享资源，公开无隐私损失。

## 第 2 步：开启 Actions 写权限（内置 GITHUB_TOKEN 才能 push）

- 同仓 **Settings** → 左侧 **Actions** → **General** → **Workflow permissions** → 选 **Read and write permissions** → 保存。
- 这样 workflow 最后一步 `git push` 能用内置 `GITHUB_TOKEN` 就地提交，**无需自建 PAT**。

## 第 3 步：首次 push（把本项目推上去）

- 本项目当前**无 git 仓库**，需你在本地：
  1. 进入项目目录，`git init`，`git remote add origin https://github.com/Jeffzhx/clash-neko.git`
  2. 先建 `.gitignore`（见下方），再 `git add scripts/ probe/ sources.json .github/ README.md repo-setup-notes.md`
  3. `git commit -m "init: subscription builder"` → `git push -u origin main`
- **不要**提交 `.handoff/`、`.longrun/`、`.cache/`、`__pycache__/`（长跑状态与缓存，非项目产物）。

建议的 `.gitignore`：
```
.handoff/
.longrun/
.workbuddy-ai/
.cache/
__pycache__/
*.pyc
```

## 第 4 步：启用并手动触发 Actions

- 同仓 **Actions** 页 → 若首次进入，点 **I understand my workflows, go ahead and enable them**。
- 左侧选 **Daily build US hysteria subscription** → **Run workflow** → 手动跑一次联调。
- 观察四步脚本 + Commit & push 是否全绿；失败就点进红色步骤看日志。

## 第 5 步：jsDelivr 验证

- 产物 push 后访问：
  - `https://cdn.jsdelivr.net/gh/Jeffzhx/clash-neko@main/main.yaml`
  - `https://cdn.jsdelivr.net/gh/Jeffzhx/clash-neko@main/nekobox.json`
- 首次可能有几分钟 CDN 缓存延迟；可在 URL 后加 `?t=时间戳` 强制刷新。
- 在 Clash Verge / NekoBox 中导入对应地址验证解析（当前为空订阅属正常，见下）。
- **单格式说明（2026-11-20 改）**：两个地址现在都是同一份 Clash YAML 内容；`nekobox.json` 只是文件名沿用，内容是 Clash（NekoBox 导入订阅按内容嗅探、不认 sing-box JSON）。两个地址都能导入，节点集合完全一致。

## 已知待复核项

- **mmdb 镜像**：本机代理下默认镜像不可达（本机网络限制）；GitHub Actions 境外 runner 应可达。若 CI 报下载失败，在仓库 **Settings → Variables → Actions** 新建 `MMDB_URL` 指向可用镜像。
- **空订阅**：若 runner 测活后无节点，`main.yaml` 会是 `proxies: []`——这是合规结果（红线：全失败生成空列表），不是故障；网络恢复后自动重填。
- **内核级校验**：本机无 mihomo/sing-box 内核，订阅只做了 YAML 结构校验，未做 `-t` / `check`；建议在客户端实际导入验证。
- **防止自触发循环**：内置 `GITHUB_TOKEN` 的 push **不会**再次触发 workflow（GitHub 默认行为），无需额外处理。

## 建设期完成后的运营滚动

U1–U6 达成后进入 `.handoff/ongoing.md` 运营期：U7 源健康度巡检、U8 解析器漂移适配、U9 订阅质量报告积累、U11 每约 30 天复核筛选条件（U10 空列表告警用户明确不要）。
