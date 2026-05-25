# WiFi 802.11基础

> **Source:** [wifi基础介绍.md](../../raw/Study_Note/06-职业发展/实习记录/my_doc/wifi基础介绍.md)
> **TLDR:** WiFi 802.11协议栈全景——从五层模型到帧结构、连接流程、安全机制、QoS、帧聚合、漫游和WPA3/SAE，嵌入式WiFi开发的完整知识地图。

## Key Points

- **802.11帧结构**：Frame Control（类型/子类型/ToDS/FromDS）+ Duration + 4个Address字段（SA/DA/TA/RA，DS位决定含义）+ Sequence Control + Frame Body + FCS
- **帧类型**：Management（Beacon/Probe Req&Resp/Auth/Assoc Req&Resp）、Control（RTS/CTS/ACK）、Data
- **连接流程**：Scanning（主动/被动）→ Authentication（Open/Shared Key）→ Association → 4-Way Handshake → DHCP
- **安全机制**：WEP（已淘汰）→ WPA/TKIP（过渡）→ WPA2/CCMP(AES)（主流）→ WPA3/SAE（最新，防字典攻击）
- **帧间距**：SIFS(10μs) < PIFS(30μs) < DIFS(50μs) < EIFS；ACK和CTS用SIFS获得最高优先级
- **QoS（WMM）**：4个AC优先级（Voice/Video/Best Effort/Background），不同AIFS和CW竞争参数
- **帧聚合**：A-MSDU（多MSDU聚合到一个MAC帧）和A-MPDU（多MPDU聚合到一个PPDU），提升吞吐效率
- **漫游（802.11k/v/r）**：k（邻居报告）、v（BSS Transition Management）、r（Fast BSS Transition/FT）

## Related Concepts

- [[wifi-four-way-handshake]] — 四次握手
- [[wifi-packet-capture]] — WiFi抓包方法
- [[tcp-protocol-basics]] — 网络层TCP
