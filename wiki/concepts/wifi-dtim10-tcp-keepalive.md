---
type: concept
aliases:
  - WiFi DTIM10 TCP 保活
  - 低功耗 TCP 保活
---

# WiFi DTIM10 TCP 保活

> **TLDR:** DTIM10 + TCP keepalive 是在低功耗和可达性之间做权衡：设备降低 WiFi 唤醒频率，同时用 TCP 心跳维持服务端连接状态。

## 关键链路

- WiFi 侧：DTIM 间隔变大，设备减少监听 Beacon 的频率。
- TCP 侧：定期发送 keepalive 或应用层心跳，避免连接被服务端清理。
- 业务侧：服务端命令需要等设备下一次唤醒窗口才能被及时处理。
- 功耗侧：DTIM 越大越省电，但实时性越弱。

## 判断点

- 如果实时性优先，降低 DTIM 或增加主动唤醒。
- 如果续航优先，增加 DTIM 并降低心跳频率。
- 如果连接经常断，检查 NAT、服务端超时和心跳间隔。
- 如果功耗偏高，检查 WiFi/BLE/外设是否都投票进入低功耗。

## Related

- [[wifi-basics]]
- [[tcp-protocol-basics]]
- [[bk-wifi-ble-coexistence]]
- [[task-development-records]]
