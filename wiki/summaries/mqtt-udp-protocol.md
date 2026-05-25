# MQTT + UDP 混合通信协议

> **Source:** [mqtt-udp.md](../../raw/智能桌面萌宠项目笔记/mqtt-udp.md)
> **TLDR:** 双通道设计——MQTT 负责控制消息和 JSON 交换，UDP 负责加密实时音频传输（AES-CTR）；序列号防重放，MQTT 断线自动重连。

## Key Points

- **MQTT 控制通道**：Hello 握手→设备声明 `transport: udp` + `features.mcp`→服务器返回 UDP 连接信息（server/port/key/nonce）
- **UDP 音频通道**：AES-CTR 加密 Opus 音频（16kHz 上行/24kHz 下行/单声道/60ms 帧）；包格式含 type/flags/payload_len/ssrc/timestamp/sequence
- **序列号管理**：`local_sequence_` 单调递增；`remote_sequence_` 验证连续性；拒绝过小序列号防重放
- **MQTT 消息类型**：Listen/Abort/MCP/Goodbye（设备→服务器）；STT/TTS/LLM/MCP/System/Custom（服务器→设备）
- **状态流转**：Disconnected→MqttConnecting→MqttConnected→RequestingChannel→ChannelOpened→UdpConnected→AudioStreaming
- **安全**：MQTT 支持 TLS（8883 端口）；UDP 密钥通过 MQTT 通道分发；超时默认 120 秒
- **vs WebSocket**：UDP 实时性更高但复杂度高、防火墙友好度低；WebSocket 简单可靠但实时性中等

## Related Concepts

- [[websocket-protocol]] — WebSocket 协议对比
- [[mcp-protocol]] — MCP 协议
- [[wifi-basics]] — WiFi 传输层
