# 订阅构建报告（单格式·覆盖写，不追加）

- 生成时间：2026-11-19T21:40:14+00:00
- 输入文件：`/home/runner/work/clash-neko/clash-neko/alive_nodes.json`
- 输入节点数（alive_nodes）：82
- 输出节点数：82（白名单过滤后）
- 被过滤节点数：0
- 协议分布（输出）：
  - trojan: 57
  - vless: 25

## 格式口径（已按用户决定改为单格式）
- 只输出 **Clash YAML** 一种格式。
- `main.yaml`（主订阅）与 `nekobox.json`（兼容地址，文件名沿用）写入**同一份 Clash YAML 内容**。
- 原因：NekoBox 的「从链接导入订阅」按内容嗅探，不认完整 sing-box JSON 配置，但能识别 Clash YAML；
  单格式避免双份维护与格式不识别，两个订阅 URL 均保持可用、节点集合天然一致。

## 白名单过滤（红线）
- 仅输出 type ∈ {hysteria, hysteria2, anytls, tuic, vless, trojan}（6 种）；其它协议过滤并登记：
  - （无，输入未混入非白名单协议）

## 字段映射表（7 种协议 → mihomo/Clash.Meta）
| 协议 | 关键字段 |
|------|----------|
| hysteria | auth / obfs / protocol(udp) / sni / skip-cert-verify / up / down |
| hysteria2 | auth / obfs / sni / skip-cert-verify |
| anytls | password / sni / skip-cert-verify |
| tuic | uuid / password(v5) 或 token(v4) / alpn / sni / skip-cert-verify / congestion-controller / udp-relay-mode / disable-sni / reduce-rtt |
| vless | uuid / flow / servername(sni) / tls:true / alpn / client-fingerprint / reality-opts(public-key,short-id) / ws-opts 或 grpc-opts |
| trojan | password / sni / alpn / skip-cert-verify / network |
| naive | username / password / sni / alpn / skip-cert-verify |
- VLESS Reality 仍是 vless 类型，靠 `reality-opts` / `security=reality` 区分；URI 的 `type=ws/grpc` 归一为 `network`。
- 与 `kernel_probe.to_mihomo_proxy` 逐字一致，保证内核测活注入字段与订阅一致。

## 结构校验（有据，附出处）
- 两个订阅文件均以 `yaml.safe_load` 重解析（proxies/proxy-groups/rules 均为合法结构）：
  - `main.yaml`：通过
  - `nekobox.json`：通过
- 内容指纹（SHA-256，便于幂等比对）：
  - main.yaml：`e56a391cf9e48a411e9f759e11537d8ccad8499f1891ac483cbd8fd72fa8396f`
  - nekobox.json：`e56a391cf9e48a411e9f759e11537d8ccad8499f1891ac483cbd8fd72fa8396f`（应与 main.yaml 一致）
- **局限（如实注明）**：本机无 mihomo/sing-box 内核二进制，未做内核级配置校验（`-t` / `check`）；
  本报告仅证明 YAML 结构合法、两地址内容一致，不证明节点可在内核中实际连通。

## 节点 name 规则
- `US-{type}-{server}-{port}`，冲突追加序号，保证唯一可读。
- 输出节点列表：US-trojan-167.88.61.85-443, US-trojan-216.152.156.212-443, US-trojan-66.163.122.30-443, US-trojan-167.88.61.198-443, US-trojan-216.106.186.82-443, US-trojan-167.88.61.52-443, US-trojan-216.152.156.159-443, US-trojan-216.106.186.32-443, US-trojan-167.88.61.20-443, US-trojan-66.23.203.21-59689, US-trojan-66.163.112.142-443, US-trojan-170.101.101.211-443, US-trojan-216.152.155.54-443, US-trojan-69.164.240.85-50875, US-trojan-157.254.38.210-20103, US-trojan-66.163.112.13-443, US-trojan-sclass-01.catcat321.com-20103, US-trojan-216.152.155.131-443, US-trojan-66.163.122.26-443, US-trojan-167.88.61.193-443, US-trojan-216.152.156.49-443, US-trojan-167.88.61.175-443, US-trojan-216.152.156.42-443, US-vless-www.zoom.us-443, US-trojan-216.106.186.46-443, US-vless-104.16.10.234-443, US-vless-104.18.37.127-443, US-vless-104.21.70.228-443, US-vless-162.159.254.3-443, US-vless-104.21.70.21-443, US-vless-104.21.0.87-443, US-vless-104.19.33.237-443, US-vless-172.67.217.240-443, US-vless-104.18.42.98-443, US-vless-104.24.31.89-443, US-trojan-216.152.156.81-443, US-trojan-66.163.122.81-443, US-trojan-169.197.140.208-443, US-trojan-216.152.155.50-443, US-trojan-216.152.156.65-443, US-vless-104.19.48.107-443, US-vless-104.19.33.25-443, US-vless-104.19.164.155-443, US-vless-104.16.111.202-443, US-vless-104.17.3.81-443, US-vless-104.16.10.56-443, US-vless-104.21.33.59-443, US-vless-104.16.111.102-443, US-vless-104.16.0.1-443, US-vless-144.31.28.228-2096, US-vless-fr-free.fastestrelay.com-443, US-vless-172.67.156.147-443, US-vless-kuruish.org-443, US-vless-104.17.70.206-8443, US-trojan-188.114.98.0-443, US-trojan-66.163.112.121-443, US-trojan-66.163.112.242-443, US-trojan-66.163.114.132-443, US-trojan-resources.findlocaljobnetworkandbuildcommunityconnections.com-443, US-trojan-66.163.114.114-443, US-trojan-66.163.112.76-443, US-trojan-216.152.155.59-443, US-trojan-170.101.101.67-443, US-trojan-170.101.101.19-443, US-trojan-66.163.112.31-443, US-trojan-216.152.155.23-443, US-trojan-169.197.140.169-443, US-trojan-169.197.140.245-443, US-trojan-169.197.140.218-443, US-trojan-66.163.112.171-443, US-trojan-66.163.112.147-443, US-trojan-blog.findlocaljobnetworkandbuildcommunityconnections.com-443, US-trojan-66.163.112.171-, US-trojan-66.163.112.31-, US-trojan-66.163.112.242-, US-trojan-170.101.101.211-, US-trojan-216.106.186.82-, US-trojan-66.163.112.147-, US-trojan-blog.findlocaljobnetworkandbuildcommunityconnections.com-, US-trojan-216.106.186.46-, US-trojan-66.163.122.30-, US-trojan-179.255.132.69-443

## 空列表说明
- 输入非空，按节点字段一一映射输出。

## 合规声明
- 未修改 `.handoff/`；未覆盖他人产出（alive_nodes.json / us_nodes.json / nodes_raw.json / 其它 scripts 均未动）。
- 未写 token/PAT；未执行 push/发布/对外发送。
