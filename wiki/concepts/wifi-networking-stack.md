# WiFi网络技术栈

> **TLDR:** 嵌入式WiFi开发的完整技术栈：从802.11物理层帧结构、连接与安全（扫描→认证→关联→四次握手）、IP层（lwIP/TCP/UDP）、到应用层（MQTT/HTTP/AT指令）和调试工具（Omnipeek/Wireshark抓包分析）。

## 一、802.11协议基础

### 帧类型与应用场景
- **Management帧**：Beacon（AP周期性广播）、Probe Request/Response（扫描）、Authentication/Deauthentication、Association/Reassociation
- **Control帧**：RTS/CTS（虚拟载波侦听）、ACK（确认接收）、Block ACK Request/Response
- **Data帧**：普通数据、QoS Data（WMM优先级）、Null Data（省电通知）

### ToDS/FromDS与地址字段
| ToDS | FromDS | Address1 | Address2 | Address3 | 场景 |
|------|--------|----------|----------|----------|------|
| 0 | 0 | DA | SA | BSSID | Ad-hoc直连 |
| 0 | 1 | DA | BSSID | SA | AP→STA |
| 1 | 0 | BSSID | SA | DA | STA→AP |
| 1 | 1 | RA | TA | DA | WDS桥接 |

### 帧聚合提升效率
- A-MSDU：多个MSDU聚合到一个MAC帧（共享MAC头）→适合小包
- A-MPDU：多个MPDU聚合到一个PPDU（每个有独立MAC头和FCS）→适合大包，单个错误不影响其他

## 二、连接与安全

### 连接流程
```
AP周期性广播Beacon
  ↓
STA: 主动扫描(Probe Request)或被动扫描(监听Beacon)
  ↓
STA → AP: Authentication Request (Open System / Shared Key)
  ↓
AP → STA: Authentication Response
  ↓
STA → AP: Association Request (能力信息、SSID)
  ↓
AP → STA: Association Response (AID分配)
  ↓
四次握手 (WPA/WPA2) / SAE握手 (WPA3)
  ↓
DHCP 获取IP地址
```

### 四次握手（WPA2核心安全机制）
1. AP→STA: ANonce（Authenticator Nonce，防重放）
2. STA→AP: SNonce + MIC（STA已用PMK+ANonce+SNonce+MAC生成PTK）
3. AP→STA: GTK + MIC（AP验证PTK正确，分发组密钥GTK用于广播加密）
4. STA→AP: ACK（确认密钥安装完成）

### 安全演进
- **WEP**（已淘汰）：RC4加密，IV重用严重安全漏洞
- **WPA/TKIP**（过渡）：临时密钥完整性协议，兼容旧硬件
- **WPA2/CCMP(AES)**（主流）：AES-CCM加密+MIC完整性保护
- **WPA3/SAE**（最新）：Dragonfly密钥交换，防离线字典攻击

## 三、嵌入式TCP/IP：lwIP

- lwIP是轻量级TCP/IP协议栈，专为资源受限的嵌入式系统设计
- 核心API：`netconn`（基于conn的API）、`socket`（BSD兼容API）
- 关键配置：`TCP_MSS`（最大分段大小）、`TCP_WND`（窗口大小）、`MEM_SIZE`（内存池）
- 常见坑点：`mem_malloc()`耗尽→TCP发送失败；`netconn_write()`不返回错误但数据未送达（需确认机制）

## 四、抓包分析方法

### 工具选择
- **Omnipeek**：空中抓包（需Monitor模式网卡，如MTK/EDIMAX EW-7822UAC），捕获802.11原始帧
- **Wireshark**：有线抓包（交换机端口镜像），捕获WLAN口数据
- **Android抓包**：开启开发者选项中的WiFi详细日志

### 常用过滤
- `wlan.addr == xx:xx:xx:xx:xx:xx`：目标MAC所有帧
- `eapol`：四次握手帧
- `wlan.fc.type == 0`：Management帧；`== 1`：Control帧；`== 2`：Data帧
- `wlan.fc.type_subtype == 0x08`：Beacon帧

### 解密条件
- 必须捕获完整的4次EAPOL握手帧（缺任一步则无法解密）
- 需要知道PMK（抓包前或抓包后输入密码均可推导）
- 中文SSID需特殊处理编码

## Related

- [[wifi-basics]] — 802.11基础
- [[wifi-four-way-handshake]] — 四次握手详解
- [[wifi-packet-capture]] — 抓包方法
- [[tcp-protocol-basics]] — TCP协议
- [[task-development-records]] — WiFi相关开发实践
