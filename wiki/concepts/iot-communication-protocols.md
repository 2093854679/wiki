# 物联网通信协议全景

> **TLDR:** 从板级总线到云端的完整 IoT 通信协议栈——板级用 I2C/SPI/UART、传输层选 WebSocket 或 MQTT+UDP、应用层统一用 MCP（JSON-RPC 2.0）实现设备能力发现和远程调用。

## 协议栈层次

```
应用层：   MCP (JSON-RPC 2.0) — 设备能力发现、工具调用、物联网控制
传输层：   WebSocket (全双工) / MQTT+UDP (控制与数据分离)
安全层：   TLS (MQTT 8883) / AES-CTR (UDP 音频) / WPA2 (WiFi)
网络层：   TCP/IP (lwIP)
链路层：   Wi-Fi MAC (802.11)
物理层：   I2C / SPI / UART (板级外设)
```

## 传输层对比

| 特性 | WebSocket | MQTT + UDP |
|------|-----------|------------|
| 控制通道 | WebSocket | MQTT |
| 音频通道 | WebSocket Binary | UDP (AES-CTR加密) |
| 实时性 | 中等 | 高（UDP） |
| 复杂度 | 低 | 高 |
| 防火墙友好 | 高 | 低（UDP 可能被拦） |
| 适用场景 | 简单快速部署 | 高实时音频+低延迟控制 |

## MCP 统一应用层

无论底层传输选择 WebSocket 还是 MQTT，上层都使用 MCP 协议（JSON-RPC 2.0）进行设备交互：

1. **Hello + initialize**：设备声明 MCP 能力 → 后台确认协议版本和会话信息
2. **tools/list**：后台获取设备注册的所有工具（名称、描述、参数 Schema）
3. **tools/call**：后台调用设备工具（带参数 JSON）→ 设备执行并返回结果
4. **Notifications**：设备主动推送状态变化（无 id 字段，后台不回复）

## 实际应用

### 小智AI / 桌面宠物
- WebSocket 或 MQTT+UDP 作为传输通道
- MCP 工具集：`self.pet.get_state`（养成状态）、`self.light.set_rgb`（灯光控制）、`self.audio_speaker.set_volume`（音量调节）
- LLM 通过 `tools/call` 控制设备行为（摸头/戳脸触发语音互动）

### OV-Watch
- 板级通过 BLE 广播传感器数据
- 内部 FreeRTOS 消息队列实现任务间通信
- 6 个消息队列覆盖按键→屏幕→传感器→存储的完整数据流

### BK7236 IoT
- lwIP TCP/IP 栈承载 MQTT/HTTP
- AT 指令（UART）或 CLI（串口）作为本地控制通道
- WiFi DTIM 省电模式平衡功耗和实时性

## 设计原则

1. **传输无关**：MCP 协议不绑定具体传输层，WebSocket/MQTT/HTTP 均可承载
2. **能力声明**：设备主动声明支持的功能（features.mcp），后台按需调用
3. **安全分层**：传输加密（TLS/AES）+ 认证（Bearer Token/用户名密码）+ 防重放（序列号）
4. **松耦合**：设备工具注册在代码中声明式定义，后台通过 `tools/list` 动态发现，无需硬编码

## Related

- [[mqtt-udp-protocol]] — MQTT+UDP 混合协议详解
- [[websocket-protocol]] — WebSocket 协议详解
- [[mcp-protocol]] — MCP JSON-RPC 交互流程
- [[mcp-usage]] — MCP 工具注册与调用示例
- [[embedded-communication-protocols]] — 板级协议（I2C/SPI/UART）
- [[wifi-networking-stack]] — WiFi 网络技术栈
