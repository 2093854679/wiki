# TCP协议基础

> **Source:** [04-TCP协议.md](../../raw/Study_Note/02-嵌入式开发/外设通信/04-TCP协议.md)
> **TLDR:** TCP是面向连接的可靠传输协议，通过三次握手建立连接、四次挥手断开、序列号/确认号保证可靠、滑动窗口控制流量、拥塞控制适应网络。

## Key Points

- **TCP特性**：面向连接、可靠传输（确认+超时重传+校验）、字节流、全双工、流量控制、拥塞控制
- **三次握手**：SYN→SYN-ACK→ACK；建立连接同时协商初始序列号（ISN）；防止旧连接请求
- **四次挥手**：FIN→ACK→FIN→ACK；TCP半关闭导致四次挥手（而非三次）；TIME_WAIT等待2MSL确保最后的ACK到达
- **序列号与确认号**：字节级别的编号和确认；累积确认（ACK N表示N-1及之前都已收到）
- **滑动窗口**：接收方通过Window字段告知可用缓冲区大小；发送方据此调整发送速率
- **拥塞控制**：慢启动→拥塞避免→快重传→快恢复；核心是CWND（拥塞窗口）的动态调整
- **嵌入式TCP/IP**：lwIP（轻量级TCP/IP栈，FreeRTOS生态常用）、uIP

## Related Concepts

- [[wifi-basics]] — WiFi基础与TCP/IP关系
- [[wifi-four-way-handshake]] — WiFi四次握手（区别于TCP四次握手）
- [[tcp-uart-at-task]] — TCP UART AT指令开发
