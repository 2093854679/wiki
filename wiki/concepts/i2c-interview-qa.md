---
type: concept
aliases:
  - I2C 面试问答
  - IIC 面试
---

# I2C 面试问答

> **TLDR:** I2C 面试通常围绕两根线、开漏上拉、起停条件、ACK/NACK、地址、速率、仲裁、时钟拉伸和常见故障展开。

## 高频问题

- 为什么 I2C 需要上拉电阻？
- 起始条件和停止条件如何定义？
- ACK 和 NACK 分别由谁产生？
- 7 位地址和 R/W 位如何组成首字节？
- 多主机仲裁为什么不会破坏总线？
- 时钟拉伸是什么，哪些设备可能用到？
- I2C 通信失败通常从哪些方向排查？

## 快速答案

- 上拉：I2C 常用开漏输出，设备只能拉低，总线高电平靠上拉。
- 起停：SCL 高电平期间 SDA 下降是 Start，SDA 上升是 Stop。
- ACK：接收方在第 9 个时钟拉低 SDA 表示应答。
- 仲裁：发送 1 却读到 0 的主机输掉仲裁并退出。
- 故障：先查上拉、电平、地址、R/W、速率、线长、电容和初始化。

## Related

- [[i2c-protocol]]
- [[embedded-communication-protocols]]
- [[embedded-interview-prep]]
