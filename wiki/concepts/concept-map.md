---
type: concept-map
aliases:
  - 知识库语义地图
  - LLM 路由图
---

# 知识库语义地图

> **TLDR:** 这是给 LLM 和人一起用的总路由页：先定位问题属于哪个主题簇，再进入概念 hub，最后落到 summary 和 raw 原文。

## 快速路由

- 问官网产品分类、SDK 版本、BK7258/BK7259 SMP 与 AP/CP：先看 [Beken 官方文档分类](../categories/beken-official.md)，架构边界看 [[bk-smp-ap-cp-boundaries]]。

- 问 BK 芯片、ARMINO、WiFi API、低功耗、OTA、安全启动：先看 [[bk-armino-framework]]，再到 [[bk-wifi-ble-coexistence]]、[[wifi-networking-stack]]、[[freertos-kernel-mechanisms]] 或 [BK Docs](../categories/bk-doc.md)。
- 问 C 语言、指针、内存、编译链接、启动流程：先看 [[c-language-core-system]]，再到 [[arm-cortex-m-embedded-fundamentals]]。
- 问 RTOS 任务、调度、上下文切换、IPC、堆内存：先看 [[freertos-kernel-mechanisms]]、[[freertos-task-management]]、[[freertos-memory-management]]。
- 问 I2C/SPI/UART/TCP/WiFi/MQTT/WebSocket/MCP：先看 [[embedded-communication-protocols]] 和 [[iot-communication-protocols]]。
- 问项目实践、实习任务、配网、AT 指令、保活、上传：先看 [[task-development-records]]，再到 [[softap-provisioning-task]]、[[tcp-uart-at-task]]、[[wifi-dtim10-tcp-keepalive]]、[[spi-task-dev]]、[[http-upload-task]]。
- 问桌面宠物、小智 AI、ESP-IDF、MCP 设备控制：先看 [[desktop-pet-docs]]、[[xiaozhi-ai-framework]]、[[mcp-protocol]]。

## 核心概念簇

### BK / ARMINO

- [[bk-armino-framework]] - ARMINO 框架、芯片矩阵、构建系统和模块划分
- [[bk-wifi-ble-coexistence]] - WiFi/BLE 共存和功耗投票
- [[wifi-networking-stack]] - WiFi 连接、安全、抓包和应用栈
- [[freertos-kernel-mechanisms]] - RTOS 作为 BK 应用运行底座

### C / MCU 基础

- [[c-language-core-system]] - C 语言、指针、内存和编译链接
- [[arm-cortex-m-embedded-fundamentals]] - ARM 寄存器、启动流程、链接脚本和 map 分析
- [[embedded-software-design-patterns]] - 模块注册、接口聚合、发布订阅
- [[embedded-coding-standards]] - 命名、格式、提交和文档规范

### RTOS

- [[freertos-kernel-mechanisms]] - 调度器、IPC、内存管理总览
- [[freertos-task-management]] - 任务状态、优先级、上下文切换、ISR 交互
- [[freertos-memory-management]] - heap_1 到 heap_5、碎片、栈/堆边界
- [[watch-rtos-architecture]] - 项目里的任务拓扑实践

### 通信协议

- [[embedded-communication-protocols]] - I2C/SPI/UART/TCP 对比
- [[iot-communication-protocols]] - MQTT、WebSocket、MCP 和设备能力调用
- [[i2c-interview-qa]] - I2C 面试问答入口
- [[wifi-networking-stack]] - WiFi 网络技术栈

### 项目实践

- [[softap-provisioning-task]] - SoftAP 配网
- [[tcp-uart-at-task]] - TCP UART AT 指令
- [[wifi-dtim10-tcp-keepalive]] - DTIM10 + TCP keepalive
- [[spi-task-dev]] - SPI 主从通信
- [[http-upload-task]] - HTTP 文件上传

## 使用约定

- `concepts/` 是 LLM 的语义路由层，优先读这里。
- `summaries/` 是单篇或一组 raw 的摘要层，负责提供证据和细节。
- `raw/` 是原文层，只有需要核对 API、流程、参数和原始上下文时再读。
- 分类页负责导航，不承担概念解释。
