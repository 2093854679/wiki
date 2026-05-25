---
type: concept
aliases:
  - FreeRTOS 任务管理
  - RTOS 任务调度
  - 上下文切换
---

# FreeRTOS 任务管理

> **TLDR:** FreeRTOS 任务管理围绕 TCB、优先级、状态机、调度触发和上下文切换展开，是理解延时、ISR、队列、低功耗唤醒和多任务架构的入口。

## 适用问题

- 任务为什么会从 Running 切到 Ready、Blocked 或 Suspended？
- `vTaskDelay`、事件等待、消息队列和中断唤醒如何影响调度？
- 为什么 ISR 里不适合做阻塞、延时或大量 `printf`？
- 项目里任务优先级和消息队列应该怎么设计？

## 核心关系

- [[freertos-kernel-mechanisms]] 提供调度器、IPC 和内存管理总览。
- [[freertos-data-structures]] 解释任务链表、延时链表和事件链表。
- [[freertos-deep-dive]] 进入源码层面的调度和上下文切换。
- [[arm-registers]]、[[c-stack-mechanism]] 解释上下文保存需要的寄存器和栈。
- [[isr-delay-printf-issue]] 是 ISR 误用阻塞 API 的典型反例。
- [[watch-rtos-architecture]]、[[desktop-pet-task-topology]] 是项目级任务拓扑。

## 判断口诀

- 时间相关：先看任务状态和延时链表。
- 数据相关：先看队列、信号量、事件组。
- 卡死相关：先看 ISR、优先级反转、栈溢出和死锁。
- 性能相关：先看上下文切换频率、临界区和任务优先级。

## Related

- [[freertos-kernel-mechanisms]]
- [[freertos-memory-management]]
- [[embedded-software-design-patterns]]
