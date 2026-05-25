# WiFi四次握手详解

> **Source:** [WiFi四次握手详解.md](../../../raw/Study_Note/06-职业发展/实习记录/my_doc/WiFi四次握手详解.md)
> **TLDR:** WPA/WPA2安全连接的核心流程——4次EAPOL握手完成ANonce/SNonce交换并生成PTK和GTK；涵盖了密钥层次结构、报文结构、抓包分析和SDK代码实现。

## Key Points

- **密钥层次**：Password→PSK→PMK（PBKDF2派生）→PTK（PMK+ANonce+SNonce+MAC地址 PRF派生）→KCK（密钥确认）/KEK（密钥加密）/TK（临时加密密钥）
- **四次握手流程**：①AP→STA: ANonce ②STA→AP: SNonce+MIC（STA已生成PTK）③AP→STA: GTK+MIC（AP已验证，分发GTK）④STA→AP: ACK（确认安装密钥）
- **Nonce作用**：ANonce和SNonce确保每次连接的PTK唯一，防止重放攻击
- **MIC**：Message Integrity Code，用KCK加密的HMAC，每帧携带用于验证密钥一致性
- **GTK**：组临时密钥，用于广播/多播帧加密；用KEK加密后分发
- **Wireshark分析**：过滤`eapol`查看握手帧，可验证帧格式和时序
- **SDK实现**：ARMINO中`wpa_supplicant`负责四次握手，`wpa_sm_rx_eapol()`处理收到的EAPOL帧

## Related Concepts

- [[wifi-basics]] — 802.11帧结构与连接流程
- [[tcp-protocol-basics]] — 注意与TCP三次握手的区别
