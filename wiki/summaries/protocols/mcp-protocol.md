# MCP (Model Context Protocol) 交互流程

> **Source:** [mcp-protocol.md](../../../raw/智能桌面萌宠项目笔记/mcp-protocol.md)
> **TLDR:** MCP 协议用于后台 API 与 ESP32 设备之间的标准化通信——基于 JSON-RPC 2.0，通过 `initialize`→`tools/list`→`tools/call` 流程实现设备能力发现和远程调用。

## Key Points

- **协议封装**：MCP 消息嵌入基础协议（WebSocket/MQTT）消息体中，底层为 JSON-RPC 2.0 格式
- **交互流程**：
  1. 设备发送 Hello 消息声明 `"mcp": true` 能力
  2. 后台发送 `initialize` 请求，可携带摄像头视觉 URL 等客户端能力
  3. 后台 `tools/list` 获取设备工具列表（支持分页，`cursor`/`nextCursor`）
  4. 后台 `tools/call` 调用具体工具（参数为 JSON 对象），设备返回 `result`（含 `content` 和 `isError`）
- **Notification**：设备可主动发送无 `id` 的通知消息（如状态变化），后台不回复
- **工具注册**：`McpServer::AddTool(name, description, properties, callback)`；参数支持 bool/int/string
- **底层传输无关**：可在 WebSocket、MQTT 等多种协议上传输

## Related Concepts

- [[mcp-usage]] — MCP 物联网控制用法
- [[websocket-protocol]] — WebSocket 协议
- [[mqtt-udp-protocol]] — MQTT+UDP 协议
- [[desktop-pet-task-topology]] — 桌宠任务通信
