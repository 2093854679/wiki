# Study Note

*42 summaries from `Study_Note`.*

## 01-编程语言 (6)

- [源代码、目标文件、可执行文件、静态库、动态库](../summaries/embedded/c-compilation-pipeline.md) - > **TLDR:** C语言编译链接全流程：预处理→编译→汇编→链接，以及静态库(.a/.lib)和动态库(.so/.dll)的原理、制作和使用。
- [函数指针](../summaries/embedded/c-function-pointers.md) - > **TLDR:** 函数指针本质是指向代码段函数入口地址的指针变量，用于实现回调、OOP模拟和动态行为绑定。
- [C语言基础语法](../summaries/embedded/c-language-basics.md) - > **TLDR:** 系统梳理C语言20个核心语法点：数据类型、变量、常量、数组、函数、控制语句、结构体、指针、函数指针与回调、字符串、内存管理、预处理、typedef、枚举、联合体、位域、位操作、关键字、可变参数及高级模式（泛型/OOP模拟）。
- [C语言内存管理](../summaries/embedded/c-memory-management.md) - > **TLDR:** C语言内存模型：栈/堆/全局区/代码段的划分、malloc/free的使用与常见陷阱、内存泄漏和野指针的防范。
- [栈（Stack）详解](../summaries/embedded/c-stack-mechanism.md) - > **TLDR:** 栈是LIFO的后进先出数据结构，程序执行的核心内存区域，支撑函数调用、参数传递、局部变量分配和返回地址保存。
- [Python3学习笔记](../summaries/tools/python3-study-notes.md) - > **TLDR:** Python3系统学习笔记，涵盖解释器安装、基本语法、数据类型、控制流、函数（参数传递/闭包/装饰器/生成器/迭代器）、数据结构（列表/字典/集合/元组）、模块和包管理。

## 02-嵌入式开发 (16)

- [ARM寄存器 R0-R15详解](../summaries/embedded/arm-registers.md) - > **TLDR:** ARM处理器37个寄存器（31通用+6状态）的完整功能说明：R0-R15的用途、CPSR/SPSR状态寄存器、不同处理器模式下的寄存器映射、ATPCS调用约定。
- [bin & map文件分析](../summaries/embedded/bin-map-analysis.md) - > **TLDR:** 编译产出的.bin和.map文件解读方法——通过map文件分析代码/数据/符号的空间分布，定位内存溢出和优化目标。
- [嵌入式设计模式：模块注册机制](../summaries/embedded/embedded-registration-patterns.md) - > **TLDR:** 四层递进的模块注册机制——从Switch-Case硬编码到列表式、动态注册式、链接器驱动的静态注册式，再到发布/订阅事件驱动模式，展示嵌入式软件架构的解耦演进之路。
- [中断函数中使用延时和printf的问题](../summaries/embedded/isr-delay-printf-issue.md) - > **TLDR:** 中断服务程序（ISR）中调用阻塞函数（delay/printf）的危害——中断延迟增大、系统卡死、堆栈溢出；正确的做法是用标志位+主循环或任务处理。
- [加载区LR和执行区ER](../summaries/embedded/lr-er-load-execute-regions.md) - > **TLDR:** ARM分散加载机制——Load Region（LR，加载域）是程序在ROM中的存储位置，Execute Region（ER，执行域）是运行时在RAM中的执行位置；链接器脚本控制LR到ER的映射和自动搬移。
- [MCU启动流程](../summaries/embedded/mcu-startup-flow.md) - > **TLDR:** ARM Cortex-M上电后的完整启动序列：复位→SP/PC初始化→SystemInit→__main（数据段搬移+BSS清零）→main()。理解启动流程是嵌入式底层开发的基础。
- [OV-Watch代码风格学习](../summaries/embedded/ovwatch-code-style.md) - > **TLDR:** 基于接口聚合的硬件中间层设计——为每类硬件定义包含函数指针的接口结构体，用总结构体`HW_InterfaceTypeDef`聚合所有设备接口，实现UI/业务与BSP解耦。
- [PID控制原理](../summaries/embedded/pid-control.md) - > **TLDR:** PID是最经典的控制算法——比例(P)响应当前误差、积分(I)消除稳态误差、微分(D)预判趋势抑制超调；核心是三个参数的整定和离散化实现。
- [PWM脉宽调制](../summaries/embedded/pwm-overview.md) - > **TLDR:** PWM通过调节方波的占空比（高电平时间/周期）来控制模拟量输出，广泛应用于电机调速、LED调光、舵机控制和音频输出。
- [TIM定时器](../summaries/embedded/tim-timer-overview.md) - > **TLDR:** MCU定时器外设的全面介绍：基本定时、输入捕获（测频/测脉宽）、输出比较/PWM、编码器模式、定时器级联和中断/DMA配合。
- [小智AI机器人 — 代码框架](../summaries/projects/xiaozhi-ai-framework.md) - > **TLDR:** 小智AI是基于ESP32的开源嵌入式AI项目，采用ESP-IDF构建系统，包含多板卡硬件抽象层、OTA升级、MQTT/WebSocket协议栈和多语言资源管理。
- [I2C通信协议](../summaries/protocols/i2c-protocol.md) - > **TLDR:** I2C是两线制（SCL+SDA）同步半双工串行总线，支持多主多从、100kHz-3.4MHz速率、7/10位地址、开漏+上拉的线与逻辑、硬件仲裁和时钟拉伸机制。
- [SPI通信协议](../summaries/protocols/spi-protocol.md) - > **TLDR:** SPI是四线制（SCLK/MISO/MOSI/CS）全双工同步串行总线，高速（可达数十MHz）、无应答、单主多从，通过时钟极性和相位（CPOL/CPHA）配置四种工作模式。
- [TCP协议基础](../summaries/protocols/tcp-protocol-basics.md) - > **TLDR:** TCP是面向连接的可靠传输协议，通过三次握手建立连接、四次挥手断开、序列号/确认号保证可靠、滑动窗口控制流量、拥塞控制适应网络。
- [UART串口通信](../summaries/protocols/uart-protocol.md) - > **TLDR:** UART是异步串行通信协议，两根线（TX/RX），无时钟信号，通过约定波特率和帧格式（起始位+数据位+校验位+停止位）实现数据交换，是最基础、最广泛使用的嵌入式通信方式。
- [串口接收代码实现](../summaries/protocols/uart-receive-code.md) - > **TLDR:** STM32 UART接收的完整代码实现：HAL库中断接收、DMA+空闲中断不定长接收、环形缓冲区、超时判断、协议解析框架。

## 02-编程语言 (1)

- [C语言命名规范](../summaries/embedded/c-naming-conventions.md) - > **TLDR:** C语言项目命名规范总览——变量、函数、类型、宏、文件的命名规则与最佳实践，强调代码可读性和一致性。

## 03-网络协议 (1)

- [CRC循环冗余校验](../summaries/protocols/crc-checksum.md) - > **TLDR:** CRC用模2除法（异或运算）在数据帧后附加校验码，接收端验证余数是否为0来判断数据完整性。多项式选择决定检错能力，广泛应用于网络通信和存储校验。

## 04-操作系统 (2)

- [FreeRTOS数据结构 — 链表](../summaries/rtos/freertos-data-structures.md) - > **TLDR:** FreeRTOS核心数据结构——双向循环链表（ListItem_t/List_t），用根节点+有序插入实现任务就绪列表、延时列表和事件列表的高效管理。
- [FreeRTOS工程创建](../summaries/rtos/freertos-project-setup.md) - > **TLDR:** 从裸机到FreeRTOS的工程搭建：MDK项目配置、启动文件适配（解决堆栈符号错误）、裸机/前后台/多任务三种系统架构对比。

## 05-工具与技巧 (4)

- [CMake构建系统](../summaries/tools/cmake-build-system.md) - > **TLDR:** CMake跨平台构建系统教程——从基础的`CMakeLists.txt`编写，到库的创建和链接、接口需求传递、条件编译和安装导出。
- [Cursor嵌入式编码规则](../summaries/tools/cursor-embedded-rules.md) - > **TLDR:** Cursor AI辅助嵌入式开发的规则体系——5个专用规则文件覆盖驱动开发、固件开发、编码规范、硬件接口和中断优化，实现AI生成代码的质量控制。
- [Git版本控制](../summaries/tools/git-basics.md) - > **TLDR:** Git常用工作流和命令速查——仓库管理、分支操作、提交规范、合并与变基、日志查看、暂存与重置、标签管理。
- [Typora画图（Mermaid）](../summaries/tools/typora-mermaid-diagrams.md) - > **TLDR:** Typora通过Mermaid代码块支持流程图、时序图、类图、状态图、甘特图和饼图，渲染后可直接导出为图片或PDF。

## 06-职业发展 (12)

- [BK7236 CLI & API参考](../summaries/bk/bk7236-cli-api-reference.md) - > **TLDR:** BK7236 ARMINO SDK的CLI命令和API速查手册——覆盖WiFi、BLE、GPIO、UART、SPI、I2C、PWM、ADC、DMA、电源管理、安全启动和属性库的完整接口参考。
- [嵌入式面经](../summaries/embedded/embedded-interview-prep.md) - > **TLDR:** 嵌入式软件岗位面试题全集——覆盖C语言（struct对齐/volatile/static/内存管理）、RTOS（FreeRTOS移植/上下文切换/优先级反转/互斥量vs信号量）、通信协议（I2C/CAN/SPI/WiFi）、系统架构和开发工具（GDB/CMake/Makefile/OTA）。
- [黄国航 学习文档记录](../summaries/projects/huang-learning-log.md) - > **TLDR:** BK7236芯片实习期间的学习日志——包括四阶段学习计划、日常工作记录（SOFTAP配网/TCP AT指令/DTIM10保活）、CLI命令速查、项目开发规范和问题记录。
- [一周熟悉与开发计划](../summaries/projects/internship-plan.md) - > **TLDR:** 嵌入式实习前两周的详细计划——Phase 1（6天熟悉芯片SDK/外设/协议栈/文件系统/构建系统）过渡到Phase 2（5个task开发：SOFTAP配网、TCP AT指令、DTIM10保活、SPI通信、HTTP上传）。
- [面试记录](../summaries/projects/interview-records.md) - > **TLDR:** 三场嵌入式面试的QA实录——博坦（TCP握手/I2C/OTA/FreeRTOS栈/端序）、博通集成（项目经验/静态变量/.bss段/短路求值）、邦普（SDK对比/I2C细节/OTA Flash分区/调试方法）。
- [5个实习Task开发记录](../summaries/projects/task-development-records.md) - > **TLDR:** BK7236平台5个实习任务的完整开发文档——SOFTAP配网、TCP UART AT指令、WiFi DTIM10 TCP保活、SPI主从通信、HTTP文件上传；每项包含需求分析、技术设计、代码实现和测试要点。
- [BLE协议概述](../summaries/protocols/ble-protocol-overview.md) - > **TLDR:** BLE（蓝牙低功耗）协议栈分层架构——PHY/LL/HCI/GAP/L2CAP/SMP/ATT/GATT；核心概念包括GAP角色（Peripheral/Central）和GATT数据模型（Service/Characteristic/UUID）。
- [WiFi 802.11基础](../summaries/protocols/wifi-basics.md) - > **TLDR:** WiFi 802.11协议栈全景——从五层模型到帧结构、连接流程、安全机制、QoS、帧聚合、漫游和WPA3/SAE，嵌入式WiFi开发的完整知识地图。
- [WiFi四次握手详解](../summaries/protocols/wifi-four-way-handshake.md) - > **TLDR:** WPA/WPA2安全连接的核心流程——4次EAPOL握手完成ANonce/SNonce交换并生成PTK和GTK；涵盖了密钥层次结构、报文结构、抓包分析和SDK代码实现。
- [Wi-Fi抓包方法总结](../summaries/protocols/wifi-packet-capture.md) - > **TLDR:** Wi-Fi抓包两种方案——空中抓包用Omnipeek+专用无线网卡捕获802.11帧，有线端抓包用交换机端口镜像+Wireshark捕获WLAN口数据；含信道配置、解密密钥设置和分析技巧。
- [FreeRTOS深度分析](../summaries/rtos/freertos-deep-dive.md) - > **TLDR:** FreeRTOS内核源码深度剖析——任务优先级管理（链表操作与TCB切换）、调度器启动、Tick与延时唤醒、FromISR机制、五种内存管理方案（heap_1-heap_5）和RISC-V移植（上下文保存与恢复）。
- [OV-Watch RTOS任务架构](../summaries/rtos/watch-rtos-architecture.md) - > **TLDR:** OV-Watch智能手表的完整FreeRTOS任务和消息队列架构——9个任务（8级优先级）、6个消息队列、10+定时器协作，实现Active/Idle/Stop三种运行模式的自动切换。

---
*Generated by `kb index`.*