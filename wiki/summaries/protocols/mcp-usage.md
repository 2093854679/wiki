# MCP 物联网控制用法

> **Source:** [mcp-usage.md](../../../raw/智能桌面萌宠项目笔记/mcp-usage.md)
> **TLDR:** 通过 MCP 协议的 `tools/call` 实现对 ESP32 设备的物联网控制——工具注册、参数定义、JSON-RPC 调用示例。

## Key Points

- `McpServer::AddTool()` 注册工具：name（`模块.功能`命名）、description（AI 理解用）、properties（参数类型/范围/默认值）、callback（执行逻辑）
- 参数类型：`kPropertyTypeBoolean`、`kPropertyTypeInteger`、`kPropertyTypeString`
- 无参数工具示例：`self.dog.forward`→机器人前进
- 带参数工具示例：`self.light.set_rgb(r,g,b)`→设置 RGB 颜色
- JSON-RPC 调用：`{"jsonrpc":"2.0","method":"tools/call","params":{"name":"...","arguments":{...}},"id":N}`
- 推荐所有新项目统一采用 MCP 协议进行物联网控制

## Related Concepts

- [[mcp-protocol]] — MCP 协议详细流程
- [[desktop-pet-task-topology]] — 桌宠 MCP 工具集成
