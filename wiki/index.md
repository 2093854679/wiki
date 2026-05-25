# Wiki Index

*Auto-generated dashboard for 77 articles - 58 summaries, 19 concepts.*

---

## Semantic Map

- [Concept Map](concepts/concept-map.md) - LLM routing layer across domains, concepts, summaries, and raw sources


## Categories


- [BK Docs](categories/bk-doc.md) - 6 summaries

- [Desktop Pet](categories/desktop-pet.md) - 10 summaries

- [Study Note](categories/study-note.md) - 42 summaries




## Doc Families


- [BK AVDK](categories/bk-avdk.md)




## Core Concepts


- [FreeRTOS 任务管理](concepts/freertos-task-management.md) - > **TLDR:** FreeRTOS 任务管理围绕 TCB、优先级、状态机、调度触发和上下文切换展开，是理解延时、ISR、队列、低功耗唤醒和多任务架构的入口。

- [嵌入式编码规范](concepts/embedded-coding-standards.md) - > **TLDR:** 嵌入式编码规范的核心是可读、可测、可追踪和可维护，覆盖命名、格式、模块边界、错误处理、日志、提交和文档。

- [ARM Cortex-M嵌入式开发基础](concepts/arm-cortex-m-embedded-fundamentals.md) - > **TLDR:** ARM Cortex-M嵌入式开发的三层基础：硬件层（寄存器R0-R15、CPSR、异常模式）、启动层（上电→SP初始化→SystemInit→数据搬移→main）和链接层（分散加载LR/ER、map文件分析、内存布局）。

- [C语言核心知识体系](concepts/c-language-core-system.md) - > **TLDR:** C语言的三大支柱——内存模型（栈/堆/全局区/代码段）、指针体系（多级指针/函数指针/数组指针）和编译链接（预处理→编译→汇编→链接）；掌握这三块即掌握C语言本质。

- [FreeRTOS 内存管理](concepts/freertos-memory-management.md) - > **TLDR:** FreeRTOS 内存问题通常要同时看任务栈、heap 实现、碎片、生命周期和 ISR/任务边界；`heap_4` 是通用场景里最常见的合并空闲块方案。

- [物联网通信协议全景](concepts/iot-communication-protocols.md) - > **TLDR:** 从板级总线到云端的完整 IoT 通信协议栈——板级用 I2C/SPI/UART、传输层选 WebSocket 或 MQTT+UDP、应用层统一用 MCP（JSON-RPC 2.0）实现设备能力发现和远程调用。

- [BK ARMINO 开发框架](concepts/bk-armino-framework.md) - > **TLDR:** ARMINO 是博通集成(Beken)的新一代 AIoT 软件开发框架，基于 CMake+Kconfig 构建系统，支持多芯片(BK7235/7236/7236N/7239)、多 RTOS(FreeRTOS/AliOS/LiteOS/RT-Thread)、WiFi+BT+低功耗+多媒体+安全启动的全功能 IoT 开发平台。

- [FreeRTOS内核机制全景](concepts/freertos-kernel-mechanisms.md) - > **TLDR:** FreeRTOS内核的四大核心机制——任务管理（TCB+优先级+状态切换）、调度器（SysTick+ PendSV+上下文切换）、IPC（消息队列+信号量+互斥量）和内存管理（heap_1到heap_5五种方案）。



## Concepts (19)


- [ARM Cortex-M嵌入式开发基础](concepts/arm-cortex-m-embedded-fundamentals.md) - > **TLDR:** ARM Cortex-M嵌入式开发的三层基础：硬件层（寄存器R0-R15、CPSR、异常模式）、启动层（上电→SP初始化→SystemInit→数据搬移→main）和链接层（分散加载LR/ER、map文件分析、内存布局）。

- [BK ARMINO 开发框架](concepts/bk-armino-framework.md) - > **TLDR:** ARMINO 是博通集成(Beken)的新一代 AIoT 软件开发框架，基于 CMake+Kconfig 构建系统，支持多芯片(BK7235/7236/7236N/7239)、多 RTOS(FreeRTOS/AliOS/LiteOS/RT-Thread)、WiFi+BT+低功耗+多媒体+安全启动的全功能 IoT 开发平台。

- [BK WiFi-BLE 共存与功耗权衡](concepts/bk-wifi-ble-coexistence.md) - > **TLDR:** BK7235/7236 的 WiFi 和 BLE 是独立驱动，可以同时运行。PM 模块通过独立休眠投票机制协调两者——只有当 WiFi 和 BLE 都投票睡眠后 MCU 才进入低电压模式。同时开启意味着 MCU 更难深度睡眠，不需要 BLE 时应关闭以降功耗。

- [C语言核心知识体系](concepts/c-language-core-system.md) - > **TLDR:** C语言的三大支柱——内存模型（栈/堆/全局区/代码段）、指针体系（多级指针/函数指针/数组指针）和编译链接（预处理→编译→汇编→链接）；掌握这三块即掌握C语言本质。

- [FreeRTOS 任务管理](concepts/freertos-task-management.md) - > **TLDR:** FreeRTOS 任务管理围绕 TCB、优先级、状态机、调度触发和上下文切换展开，是理解延时、ISR、队列、低功耗唤醒和多任务架构的入口。

- [FreeRTOS 内存管理](concepts/freertos-memory-management.md) - > **TLDR:** FreeRTOS 内存问题通常要同时看任务栈、heap 实现、碎片、生命周期和 ISR/任务边界；`heap_4` 是通用场景里最常见的合并空闲块方案。

- [FreeRTOS内核机制全景](concepts/freertos-kernel-mechanisms.md) - > **TLDR:** FreeRTOS内核的四大核心机制——任务管理（TCB+优先级+状态切换）、调度器（SysTick+ PendSV+上下文切换）、IPC（消息队列+信号量+互斥量）和内存管理（heap_1到heap_5五种方案）。

- [HTTP 文件上传任务](concepts/http-upload-task.md) - > **TLDR:** HTTP 文件上传任务把网络服务、表单解析、文件系统和 Flash 存储串起来，核心是流式接收、边界解析、容量检查和错误恢复。

- [I2C 面试问答](concepts/i2c-interview-qa.md) - > **TLDR:** I2C 面试通常围绕两根线、开漏上拉、起停条件、ACK/NACK、地址、速率、仲裁、时钟拉伸和常见故障展开。

- [SoftAP 配网任务](concepts/softap-provisioning-task.md) - > **TLDR:** SoftAP 配网通过设备临时开启热点，让手机连接后提交目标 WiFi 凭据，设备再切换到 STA 模式连接目标 AP。

- [SPI 主从通信任务](concepts/spi-task-dev.md) - > **TLDR:** SPI 主从通信任务关注 CPOL/CPHA、片选、速率、收发缓冲和逻辑分析仪验证，是外设通信开发的典型入口。

- [TCP UART AT 指令任务](concepts/tcp-uart-at-task.md) - > **TLDR:** TCP UART AT 任务把串口 AT 命令解析成 TCP socket 操作，是 UART 接收、命令状态机、lwIP 调用和错误响应格式的综合练习。

- [WiFi DTIM10 TCP 保活](concepts/wifi-dtim10-tcp-keepalive.md) - > **TLDR:** DTIM10 + TCP keepalive 是在低功耗和可达性之间做权衡：设备降低 WiFi 唤醒频率，同时用 TCP 心跳维持服务端连接状态。

- [WiFi网络技术栈](concepts/wifi-networking-stack.md) - > **TLDR:** 嵌入式WiFi开发的完整技术栈：从802.11物理层帧结构、连接与安全（扫描→认证→关联→四次握手）、IP层（lwIP/TCP/UDP）、到应用层（MQTT/HTTP/AT指令）和调试工具（Omnipeek/Wireshark抓包分析）。

- [嵌入式外设通信协议全景对比](concepts/embedded-communication-protocols.md) - > **TLDR:** I2C、SPI、UART三大基础串行总线各有适用场景：I2C适合多设备低速（2线、有地址、带应答）、SPI适合高速全双工（4线、无地址、主控全权）、UART适合点对点异步（2线、无时钟、最简洁）。加上TCP形成从板级到网络的完整通信栈。

- [嵌入式编码规范](concepts/embedded-coding-standards.md) - > **TLDR:** 嵌入式编码规范的核心是可读、可测、可追踪和可维护，覆盖命名、格式、模块边界、错误处理、日志、提交和文档。

- [嵌入式软件设计模式](concepts/embedded-software-design-patterns.md) - > **TLDR:** 嵌入式软件架构中实现低耦合高内聚的三种核心设计模式——模块注册（IoC控制反转，从Switch-Case到链接器静态注册的演进）、接口聚合（硬件抽象层，含函数指针的结构体统一访问入口）和发布/订阅（事件驱动，时空解耦）。

- [物联网通信协议全景](concepts/iot-communication-protocols.md) - > **TLDR:** 从板级总线到云端的完整 IoT 通信协议栈——板级用 I2C/SPI/UART、传输层选 WebSocket 或 MQTT+UDP、应用层统一用 MCP（JSON-RPC 2.0）实现设备能力发现和远程调用。

- [知识库语义地图](concepts/concept-map.md) - > **TLDR:** 这是给 LLM 和人一起用的总路由页：先定位问题属于哪个主题簇，再进入概念 hub，最后落到 summary 和 raw 原文。



## Maintenance

- `python -m tools.kb ingest --status new` - detect new raw files
- `python -m tools.kb index` - rebuild this dashboard and category pages
- `python -m tools.kb graph-health` - inspect unresolved links, orphans, and manifest drift
- `python -m tools.kb stats` - count current wiki articles

---
*Run `kb index` to regenerate.*