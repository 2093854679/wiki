# FreeRTOS内核机制全景

> **TLDR:** FreeRTOS内核的四大核心机制——任务管理（TCB+优先级+状态切换）、调度器（SysTick+ PendSV+上下文切换）、IPC（消息队列+信号量+互斥量）和内存管理（heap_1到heap_5五种方案）。

## 一、任务管理

### TCB（任务控制块）
每个任务的核心数据结构，包含：
- `pxTopOfStack`：任务栈顶指针（上下文切换时保存/恢复SP）
- `uxPriority`：任务优先级（0=最低，数值越大优先级越高）
- `eCurrentState`：Running/Ready/Blocked/Suspended
- `xEventListItem`：事件等待列表的链表项
- `xStateListItem`：状态列表（就绪/延时）的链表项

### 优先级管理
- `vTaskPrioritySet()`核心流程：从旧优先级就绪列表移除→更新TCB优先级→插入新优先级就绪列表→若改变了任务顺序则触发切换
- 优先级继承：当低优先级任务持有互斥量而高优先级任务等待时，低优先级任务临时提升到等待任务优先级
- 就绪列表：`pxReadyTasksLists[configMAX_PRIORITIES]`，每个优先级一个链表

### 任务状态转换
```
创建 ──→ Ready ──→ Running ──→ Blocked (等待事件/延时)
             ↑         │              │
             └─────────┘              │
             (被抢占)                  │
                                      ▼
             Suspended ←──────────── (事件到达/超时)
```

## 二、调度器

### SysTick中断
- 每个Tick触发`xTaskIncrementTick()`：
  ① 检查当前任务时间片是否用完→若用完且同优先级有其他任务→切换
  ② 检查延时列表（`pxDelayedTaskList`）→唤醒到期的任务
  ③ 检查被抢占标志→执行任务切换

### PendSV（可悬起系统调用）
- 优先级最低的异常，确保所有高优先级中断处理完毕后才切换任务
- 上下文切换流程：保存R4-R11和SP到当前TCB→选择下一个最高优先级Ready任务→从该TCB恢复SP和R4-R11→返回

### 延时机制
- `vTaskDelay(ticks)`：将任务从就绪列表移到延时列表（按唤醒时间排序插入），然后切换
- `vTaskDelayUntil()`：绝对时间延时，保证固定周期执行（避免累积误差）

## 三、IPC（任务间通信）

### 消息队列
- 核心数据结构：环形缓冲区+FIFO+阻塞列表（发送满时的发送等待列表+接收空时的接收等待列表）
- `xQueueSend()`/`xQueueReceive()`：带超时的阻塞发送/接收
- FromISR版本：`xQueueSendFromISR()`不阻塞，若需切换则设置`pxHigherPriorityTaskWoken`

### 信号量（Semaphore）vs 互斥量（Mutex）
- 二值信号量：同步（ISR释放→任务获取）或互斥（不推荐，无优先级继承）
- 计数信号量：管理多个相同资源
- 互斥量：专用于互斥访问，含优先级继承机制，**不能在ISR中使用**
- 关键区别：互斥量用于资源互斥（谁来拿谁还），信号量用于同步（ISR释放→任务获取）

## 四、内存管理

| 方案 | 特点 | 适用场景 |
|------|------|---------|
| heap_1 | 仅分配不释放，简单确定 | 简单系统、无动态删除 |
| heap_2 | 简单链表，有碎片风险 | 小系统、分配次数少 |
| heap_3 | 封装标准malloc/free | 有OS的系统 |
| heap_4 | 相邻空闲块合并，减少碎片 | **最常用**，通用选择 |
| heap_5 | 跨多块不连续内存 | 多块RAM芯片 |

BK7236使用自定义best-fit分配器，基于`mmgmt_malloc()`/`mmgmt_free()`，支持内存池和泄漏检测。

## 五、RISC-V移植要点

- `mepc`：保存异常返回地址（类似ARM的LR）
- `mcause`：区分异常/中断原因
- `MSTATUS`：全局中断使能控制
- 上下文保存：Caller-saved寄存器→SP存入TCB→加载新TCB→恢复SP和寄存器→`mret`返回
- PendSV：软件触发中断实现延迟上下文切换

## Related

- [[freertos-data-structures]] — 链表数据结构
- [[freertos-project-setup]] — 工程创建与系统对比
- [[freertos-deep-dive]] — 内核源码深度分析
- [[watch-rtos-architecture]] — OV-Watch中的FreeRTOS实践
- [[arm-registers]] — ARM寄存器与上下文切换
