# FreeRTOS数据结构 — 链表

> **Source:** [02-数据结构.md](../../../raw/Study_Note/04-操作系统/FreeRTOS/02-数据结构.md)
> **TLDR:** FreeRTOS核心数据结构——双向循环链表（ListItem_t/List_t），用根节点+有序插入实现任务就绪列表、延时列表和事件列表的高效管理。

## Key Points

- **C语言链表基础**：单链表（一个next指针）、双向链表（prev+next）、根节点机制简化边界处理；链表离散存储vs数组连续存储
- **FreeRTOS实现**：`list.h`/`list.c`两个文件；`ListItem_t`包含`xItemValue`（排序键值）和`pxNext`/`pxPrevious`指针
- **List_t结构**：`xListEnd`作为哨兵节点，`uxNumberOfItems`记录元素个数，`pxIndex`用于遍历
- **关键操作**：`vListInitialise()`初始化列表、`vListInsert()`按值升序插入、`vListInsertEnd()`添加到末尾、`uxListRemove()`删除元素
- **应用场景**：就绪列表（按优先级分组）、延时列表（按唤醒时间排序）、事件列表（任务等待信号量/队列时挂入）

## Related Concepts

- [[freertos-project-setup]] — FreeRTOS工程创建
- [[freertos-task-management]] — 任务管理与调度
- [[c-language-basics]] — C语言链表基础
