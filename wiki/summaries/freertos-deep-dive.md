# FreeRTOS深度分析

> **Source:** [freertos学习.md](../../raw/Study_Note/06-职业发展/实习记录/my_doc/freertos学习.md)
> **TLDR:** FreeRTOS内核源码深度剖析——任务优先级管理（链表操作与TCB切换）、调度器启动、Tick与延时唤醒、FromISR机制、五种内存管理方案（heap_1-heap_5）和RISC-V移植（上下文保存与恢复）。

## Key Points

- **优先级管理**：`vTaskPrioritySet()`→`uxListRemove()`从旧链表移除→更新TCB优先级→`prvAddTaskToReadyList()`加入新优先级就绪列表→可能触发任务切换
- **链表核心操作**：`ListItem_t.xItemValue`排序键值；`vListInsert()`按值升序插入到双向循环链表；临界区保护（`taskENTER_CRITICAL()`/`taskEXIT_CRITICAL()`）
- **TCB（任务控制块）**：包含栈指针（pxTopOfStack）、优先级（uxPriority）、状态（eCurrentState）、事件链表项（xEventListItem）、延时链表项（xStateListItem）
- **调度器启动**：`vTaskStartScheduler()`→创建Idle Task→配置SysTick→启动第一个任务（SVCall/PendSV实现上下文切换）
- **Tick机制**：SysTick中断→`xTaskIncrementTick()`→检查延时列表→到期任务移入就绪列表→需要时触发任务切换
- **延时唤醒**：`vTaskDelay(ticks)`→将当前任务从就绪列表移到延时列表（按唤醒时间排序）→调用`portYIELD()`切换
- **FromISR API**：以`FromISR`后缀的函数不阻塞，仅操作队列/信号量数据结构后返回；若需任务切换则设置`pxHigherPriorityTaskWoken`标志，退出ISR后执行
- **内存管理**：heap_1（仅分配不释放）、heap_2（简单链表，有碎片）、heap_3（封装malloc/free）、heap_4（合并相邻空闲块，减少碎片）、heap_5（跨多块非连续内存）；BK7236使用自定义best-fit分配器
- **RISC-V移植**：mepc保存返回地址、mcause区分异常/中断、MSTATUS控制全局中断；PendSV处理任务切换
- **上下文切换**：保存Caller-saved寄存器(R0-R12等)→保存SP到TCB→加载新任务TCB→恢复SP→恢复寄存器→mret返回

## Related Concepts

- [[freertos-data-structures]] — 链表基础结构
- [[freertos-project-setup]] — FreeRTOS工程创建
- [[arm-registers]] — ARM寄存器在上下文切换中的作用
- [[watch-rtos-architecture]] — OV-Watch中的FreeRTOS实践
