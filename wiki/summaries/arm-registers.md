# ARM寄存器 R0-R15详解

> **Source:** [01-ARM寄存器及功能介绍_R0-R15寄存器.md](../../raw/Study_Note/02-嵌入式开发/MCU基础/01-ARM寄存器及功能介绍_R0-R15寄存器.md)
> **TLDR:** ARM处理器37个寄存器（31通用+6状态）的完整功能说明：R0-R15的用途、CPSR/SPSR状态寄存器、不同处理器模式下的寄存器映射、ATPCS调用约定。

## Key Points

- **寄存器分类**：R0-R3（参数传递）、R4-R11（局部变量）、R12（IP，内部调用暂存）、R13（SP，堆栈指针）、R14（LR，链接寄存器）、R15（PC，程序计数器）
- **SP（R13）**：每个异常模式都有独立的SP，确保不同模式间堆栈隔离；不能用于其他用途
- **LR（R14）**：保存BL指令的返回地址；每种异常模式有独立LR；函数返回前必须恢复
- **PC（R15）**：ARM流水线导致读取PC=当前地址+8（ARM态）或+4（Thumb态）；不能直接修改
- **CPSR**：包含N（负）、Z（零）、C（进位）、V（溢出）标志位，以及中断使能位（I/F）、Thumb状态位（T）和模式位
- **7种处理器模式**：User、FIQ、IRQ、Supervisor、Abort、Undefined、System；每种模式有独立的R13/R14和SPSR（除User/System）
- **ATPCS调用约定**：R0-R3传参（调用者保存），R4-R11局部变量（被调用者保存），R12临时（调用者保存）
- **中断处理**：PUSH {R0-R3, LR}保存调用者寄存器（R4-R11编译器自动保存），POP恢复后BX LR返回

## Related Concepts

- [[mcu-startup-flow]] — MCU启动流程
- [[c-stack-mechanism]] — 栈机制
- [[freertos-task-management]] — FreeRTOS任务上下文切换
