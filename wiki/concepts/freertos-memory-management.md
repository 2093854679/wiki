---
type: concept
aliases:
  - FreeRTOS 内存管理
  - RTOS 堆管理
  - heap_4
---

# FreeRTOS 内存管理

> **TLDR:** FreeRTOS 内存问题通常要同时看任务栈、heap 实现、碎片、生命周期和 ISR/任务边界；`heap_4` 是通用场景里最常见的合并空闲块方案。

## 适用问题

- `pvPortMalloc` 和普通 `malloc` 有什么关系？
- 为什么动态创建任务、队列、定时器后会出现内存不足？
- 任务栈和系统 heap 是不是一回事？
- 如何定位栈溢出、内存泄漏和碎片？

## 核心关系

- [[freertos-kernel-mechanisms]] 提供 heap_1 到 heap_5 总览。
- [[c-memory-management]] 解释 C 层面的栈、堆、全局区和生命周期。
- [[c-stack-mechanism]] 解释函数调用栈和任务栈的基础。
- [[freertos-task-management]] 解释任务创建、删除和栈空间使用。

## 快速判断

- 函数局部大数组：优先怀疑任务栈。
- 多次分配释放后失败：优先怀疑堆碎片或泄漏。
- ISR 相关异常：优先确认是否调用了不该在 ISR 中使用的 API。
- 长期运行后才失败：优先查生命周期、队列积压和未释放资源。

## Related

- [[c-memory-management]]
- [[freertos-task-management]]
- [[freertos-deep-dive]]
