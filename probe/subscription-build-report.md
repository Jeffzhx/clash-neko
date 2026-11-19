# U5 双格式订阅构建报告（覆盖写，不追加）

- 生成时间：2026-11-19T18:41:52+00:00
- 输入文件：`/home/runner/work/clash-neko/clash-neko/alive_nodes.json`
- 输入节点数（alive_nodes）：0
- 输出节点数：0（白名单过滤后）
- 被过滤节点数：0
- 协议分布（输出）：
  - （无）

## 白名单过滤（红线）
- 仅输出 type ∈ {hysteria, hysteria2, anytls}；其它协议过滤并登记：
  - （无，输入未混入非白名单协议）

## 两格式一致性校验
- 同一份过滤后的节点列表同时生成 main.yaml 与 nekobox.json。
- mihomo 节点数：0；sing-box 节点数：0（数量一致）
- name ↔ tag 顺序/取值一致：是
- server:port 集合一致：是
- **结论：一致 ✅**（空对空亦计为一致）
- 节点 name/tag 列表：（空）

## 结构校验方式（有据，附出处）
- main.yaml：`yaml.safe_load` 重解析 → 通过（proxies/proxy-groups/rules 均为合法结构）
- nekobox.json：`json.load` 重解析 → 通过（outbounds/dns/route 均为合法结构，route.default=direct）
- 内容指纹（SHA-256，便于幂等比对）：
  - main.yaml：`f0b556650b9f189d85ec11b311cd86ee44f758a58b7aa5c9429833b66cbb6f32`
  - nekobox.json：`f30d6cfec3ceac045bb6550fd69927b94cd52ebe5d0aa71259c8c0f307c05c8e`
- **局限（如实注明）**：本机无 mihomo/sing-box 内核二进制，未做内核级配置校验（`-t` / `check`）；
  本报告仅证明 YAML/JSON 结构合法、两格式节点集合一致，不证明节点可在内核中实际连通用。

## 字段映射说明
| 协议 | mihomo proxy 字段 | sing-box outbound 字段 |
| --- | --- | --- |
| hysteria2 | name,type,server,port,auth,sni,skip-cert-verify,obfs(如有) | type,tag,server,server_port,auth_str,sni,tls{enabled,server_name,insecure},obfs(如有→salamander) |
| hysteria | name,type,server,port,auth,obfs(如有),protocol(默认udp),sni,skip-cert-verify,up,down | type,tag,server,server_port,auth_str,up,down,tls{...},obfs(如有→salamander) |
| anytls | name,type,server,port,password,sni,skip-cert-verify | type,tag,server,server_port,password,tls{...} |

- 字段兼容：auth/password/auth_str 互为别名；sni/server_name/host 互为别名；tls.server_name 在 sni 为空时退化为 server；tls.insecure 跟随 skip-cert-verify（默认 true）。
- 占位默认值：hysteria 的 up/down 缺失时填 `100 Mbps` / `200 Mbps`（推断，非节点真实性数据，仅保证配置可用）。
- name 规则：`US-{type}-{server}-{port}`，冲突追加序号，保证唯一可读。

## 空列表说明
- 当前 alive_nodes=[]，按红线生成**合法空订阅**（YAML proxies=[]、JSON 仅 direct+block），这是合法结果，不是错误；本单元未塞入 unknown/dead 节点、未编造节点。

## 合规声明
- 未修改 `.handoff/`；未覆盖他人产出（alive_nodes.json / us_nodes.json / nodes_raw.json / 其它 scripts 均未动）。
- 未写 token/PAT；未执行 push/发布/对外发送。
