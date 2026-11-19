# 订阅构建报告（单格式·覆盖写，不追加）

- 生成时间：2026-11-19T19:05:17+00:00
- 输入文件：`/home/runner/work/clash-neko/clash-neko/alive_nodes.json`
- 输入节点数（alive_nodes）：0
- 输出节点数：0（白名单过滤后）
- 被过滤节点数：0
- 协议分布（输出）：
  - （无）

## 格式口径（已按用户决定改为单格式）
- 只输出 **Clash YAML** 一种格式。
- `main.yaml`（主订阅）与 `nekobox.json`（兼容地址，文件名沿用）写入**同一份 Clash YAML 内容**。
- 原因：NekoBox 的「从链接导入订阅」按内容嗅探，不认完整 sing-box JSON 配置，但能识别 Clash YAML；
  单格式避免双份维护与格式不识别，两个订阅 URL 均保持可用、节点集合天然一致。

## 白名单过滤（红线）
- 仅输出 type ∈ {hysteria, hysteria2, anytls}；其它协议过滤并登记：
  - （无，输入未混入非白名单协议）

## 结构校验（有据，附出处）
- 两个订阅文件均以 `yaml.safe_load` 重解析（proxies/proxy-groups/rules 均为合法结构）：
  - `main.yaml`：通过
  - `nekobox.json`：通过
- 内容指纹（SHA-256，便于幂等比对）：
  - main.yaml：`f0b556650b9f189d85ec11b311cd86ee44f758a58b7aa5c9429833b66cbb6f32`
  - nekobox.json：`f0b556650b9f189d85ec11b311cd86ee44f758a58b7aa5c9429833b66cbb6f32`（应与 main.yaml 一致）
- **局限（如实注明）**：本机无 mihomo/sing-box 内核二进制，未做内核级配置校验（`-t` / `check`）；
  本报告仅证明 YAML 结构合法、两地址内容一致，不证明节点可在内核中实际连通。

## 节点 name 规则
- `US-{type}-{server}-{port}`，冲突追加序号，保证唯一可读。
- 输出节点列表：（空）

## 空列表说明
- 当前 alive_nodes=[]，按红线生成**合法空订阅**（proxies=[]），这是合法结果，不是错误；本单元未塞入 unknown/dead 节点、未编造节点。

## 合规声明
- 未修改 `.handoff/`；未覆盖他人产出（alive_nodes.json / us_nodes.json / nodes_raw.json / 其它 scripts 均未动）。
- 未写 token/PAT；未执行 push/发布/对外发送。
