# FreeRTOS工程创建

> **Source:** [01-新建Freertos工程.md](../../raw/Study_Note/04-操作系统/FreeRTOS/01-新建Freertos工程.md)
> **TLDR:** 从裸机到FreeRTOS的工程搭建：MDK项目配置、启动文件适配（解决堆栈符号错误）、裸机/前后台/多任务三种系统架构对比。

## Key Points

- **工程配置**：添加FreeRTOS源码路径到Include Paths、添加portable目录的对应架构文件（ARM_CM3）、FreeRTOSConfig.h中配置
- **常见错误**：`Undefined symbol Image$$ARM_LIB_STACK$$ZI$$Limit`——链接器未生成堆栈边界符号，需在链接脚本中定义或指定正确的启动文件路径
- **裸机系统**：前后台简单，但多任务轮询效率低；适合简单控制逻辑
- **前后台系统**：中断处理紧急事件（前台），主循环轮询处理非紧急任务（后台）；中断执行时间长会影响轮询
- **多任务系统（RTOS）**：每个任务独立栈空间，抢占式调度保证实时性；增加RAM开销和调度开销
- **对比选择**：裸机适合<5个任务无实时要求的场景；RTOS适合复杂多任务、需实时响应的场景

## Related Concepts

- [[freertos-task-management]] — FreeRTOS任务管理
- [[freertos-data-structures]] — FreeRTOS链表数据结构
- [[mcu-startup-flow]] — MCU启动流程
