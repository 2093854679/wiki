# WebSocket 通信协议

> **Source:** [websocket.md](../../raw/智能桌面萌宠项目笔记/websocket.md)
> **TLDR:** 设备与服务器通过 WebSocket 进行全双工通信——JSON 文本帧承载控制消息（Hello/Listen/STT/TTS/MCP），二进制帧承载 Opus 音频流；支持 3 种二进制协议版本。

## Key Points

- **连接握手**：`Authorization: Bearer <token>` + `Protocol-Version` + `Device-Id` + `Client-Id` 头
- **Hello 消息**：设备声明 `transport: websocket` + `features.mcp` + audio_params（Opus/16000Hz/单声道/60ms）；服务器回复 `session_id` + 期望音频参数
- **JSON 消息类型（设备→服务器）**：Hello、Listen（start/stop/detect）、Abort、Wake Word Detected、MCP
- **JSON 消息类型（服务器→设备）**：Hello、STT（识别结果）、LLM（情感+表情）、TTS（start/stop/sentence_start+部分文本）、MCP、System（reboot）、Custom
- **二进制音频**：Opus 编码双向流；3 种协议版本——v1 直接 Opus、v2 带时间戳（服务器 AEC）、v3 简化元数据
- **状态流转**：Idle→Connecting→Listening→Speaking→Idle；手动/自动模式不同流转路径
- **错误处理**：连接失败→提示错误；异常断开→回到 Idle；JSON 缺失 type 字段→记录日志忽略

## Related Concepts

- [[mqtt-udp-protocol]] — MQTT+UDP 混合协议对比
- [[mcp-protocol]] — MCP 协议细节
- [[xiaozhi-ai-framework]] — 小智AI 框架
