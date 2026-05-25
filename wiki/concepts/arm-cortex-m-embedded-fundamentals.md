# ARM Cortex-M嵌入式开发基础

> **TLDR:** ARM Cortex-M嵌入式开发的三层基础：硬件层（寄存器R0-R15、CPSR、异常模式）、启动层（上电→SP初始化→SystemInit→数据搬移→main）和链接层（分散加载LR/ER、map文件分析、内存布局）。

## 一、ARM寄存器体系

37个寄存器组成ARM的程序员模型：

- **通用寄存器 R0-R15**：R0-R3传参，R4-R11局部变量，R12临时（IP），R13堆栈指针（SP），R14链接寄存器（LR），R15程序计数器（PC）
- **状态寄存器 CPSR/SPSR**：N（负）/Z（零）/C（进位）/V（溢出）条件码 + 中断使能位 + 模式位
- **7种处理器模式**：User/FIQ/IRQ/Supervisor/Abort/Undefined/System；异常模式有独立SP/LR/SPSR
- **调用约定（ATPCS）**：调用者保存R0-R3/R12/LR，被调用者保存R4-R11，SP/PC由硬件管理

关键理解：
- ARM流水线效应：读取PC=当前地址+8（ARM态）或+4（Thumb态）
- 中断处理时编译器自动PUSH/POP R4-R11，程序员手动保存R0-R3/LR
- 每种异常模式有独立SP，确保异常处理的堆栈隔离

## 二、MCU启动流程

从复位向量到main()的完整路径：

```
上电/复位
  │
  ▼
硬件自动: SP = [0x00000000], PC = [0x00000004] = Reset_Handler
  │
  ▼
Reset_Handler (startup_xxx.s):
  ├── SystemInit()        ← 时钟/PLL/Flash等待周期初始化
  └── __main()            ← C库启动代码
       ├── 搬运.data段    ← Flash(LR) → RAM(ER)
       ├── 清零.bss段     ← 未初始化全局变量
       ├── 初始化堆/栈    ← __heap_base, __stack_top
       └── main()         ← 用户程序入口
```

- 中断向量表位于Flash起始处：`0x00000000`=SP初始值，`0x00000004`=Reset入口
- .data段搬运和.bss段清零由链接器生成的Copy Table自动完成
- 不同MCU厂商有各自的启动变体（STM32的boot引脚、ESP32的二级bootloader）

## 三、分散加载与内存映射

### LR（加载域）vs ER（执行域）
- LR = 程序在ROM/Flash中的存储位置（包括代码、只读数据、已初始化数据的初始值）
- ER = 程序运行时在RAM中的位置（读写数据必须在此）
- XIP（eXecute In Place）= 代码直接在Flash中执行，无需搬移到RAM
- .data段必须从LR搬到ER（因为全局变量需要可读写）
- .bss段只需在ER中清零（不需要在LR中占空间）

### map文件分析
- 查看每个段（.text/.data/.bss/.heap/.stack）的实际地址和大小
- 符号表按大小排序，定位占用大的函数和变量
- 验证 `RAM使用 = .data + .bss + heap + stack < RAM总大小` 和 `Flash使用 = .text + .rodata + .data(LR) < Flash总大小`
- 常见问题：RAM溢出（LR→ER搬移后超出RAM边界）、意外引入大库函数

## 四、中断处理最佳实践

- ISR必须快速执行：只做紧急操作（读寄存器、清标志、置标志位）
- 耗时操作延迟到主循环或低优先级任务（Deferred Interrupt模式）
- ISR中禁止调用阻塞函数（delay依赖中断计时会死锁，printf依赖UART中断会阻塞）
- FreeRTOS中ISR→发送信号量/消息队列→高优先级任务处理的标准模式
- 中断优先级分配：紧急硬件中断（如电机过流）> 通信中断 > 定时器中断

## Related

- [[arm-registers]] — ARM寄存器详解
- [[mcu-startup-flow]] — MCU启动流程
- [[lr-er-load-execute-regions]] — LR/ER机制
- [[bin-map-analysis]] — map文件分析
- [[c-compilation-pipeline]] — 编译链接全过程
- [[isr-delay-printf-issue]] — ISR中延时/printf的问题
- [[freertos-task-management]] — FreeRTOS任务上下文切换
