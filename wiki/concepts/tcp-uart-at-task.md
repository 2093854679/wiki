---
type: concept
aliases:
  - TCP UART AT 指令任务
  - AT 指令解析
---

# TCP UART AT 指令任务

> **TLDR:** TCP UART AT 任务把串口 AT 命令解析成 TCP socket 操作，是 UART 接收、命令状态机、lwIP 调用和错误响应格式的综合练习。

## 关键链路

- UART 接收：中断、DMA 或环形缓冲区收集命令。
- AT 解析：按行、超时或状态机切分命令。
- TCP 操作：`connect`、`send`、`recv`、`close` 对应 AT 子命令。
- 响应格式：统一返回 OK、ERROR、连接状态和数据长度。

## 易错点

- 串口分包和粘包没有处理。
- TCP 阻塞调用卡住 AT 解析任务。
- 错误码没有映射成清晰响应。
- 多连接状态和资源释放不完整。

## Related

- [[uart-protocol]]
- [[uart-receive-code]]
- [[tcp-protocol-basics]]
- [[task-development-records]]
