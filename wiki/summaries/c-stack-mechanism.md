# 栈（Stack）详解

> **Source:** [06-栈.md](../../raw/Study_Note/01-编程语言/C语言/06-栈.md)
> **TLDR:** 栈是LIFO的后进先出数据结构，程序执行的核心内存区域，支撑函数调用、参数传递、局部变量分配和返回地址保存。

## Key Points

- **栈的本质**：一段连续内存区域，通过栈指针（SP）管理；入栈（push）SP减小（向下增长），出栈（pop）SP增大
- **栈帧（Stack Frame）**：每次函数调用创建一个栈帧，包含：返回地址、保存的EBP、局部变量、参数；函数返回时整个栈帧被销毁
- **调用约定**：cdecl（调用者清理参数）、stdcall（被调用者清理参数）、fastcall（寄存器传参）；ARM使用ATPCS/AAPCS标准
- **ARM栈操作**：`PUSH {reg_list}` / `POP {reg_list}`；SP指向最后入栈元素（满递减堆栈FD）
- **栈溢出**：递归过深、局部变量过大（大数组在函数内）、中断嵌套过深；后果是破坏堆数据或触发HardFault
- **栈与堆的区别**：栈由编译器自动管理，速度快但容量小；堆手动管理，速度慢但容量大
- **多任务栈**：RTOS中每个任务有独立栈，通过任务切换时切换SP实现

## Main Arguments

栈是理解程序执行的关键。几乎所有运行时bug——栈溢出、野指针、返回临时变量地址——都跟对栈机制理解不足有关。嵌入式开发者尤其需要关注任务栈大小的设置，太小导致溢出，太大浪费宝贵RAM。

## Related Concepts

- [[c-memory-management]] — 内存管理全景
- [[c-language-basics]] — C语言基础
- [[freertos-task-management]] — FreeRTOS任务栈管理
- [[arm-registers]] — ARM寄存器与栈指针
