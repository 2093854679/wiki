# C语言基础语法

> **Source:** [01-C语言基础语法.md](../../raw/Study_Note/01-编程语言/C语言/01-C语言基础语法.md)
> **TLDR:** 系统梳理C语言20个核心语法点：数据类型、变量、常量、数组、函数、控制语句、结构体、指针、函数指针与回调、字符串、内存管理、预处理、typedef、枚举、联合体、位域、位操作、关键字、可变参数及高级模式（泛型/OOP模拟）。

## Key Points

- C是强类型语言，有`short`、`long`、`int`、`char`、`float`、`double`等基本类型，`struct`/`union`/`enum`为构造类型
- 指针是C语言的灵魂，本质是内存地址；32位系统占4字节，64位占8字节；支持多级指针、数组指针、函数指针、void指针
- 内存分为栈（局部变量，自动管理，8/16MB限制）和堆（`malloc`/`free`配对，手动管理）
- 函数指针用于回调（callback）和模拟OOP多态——带函数指针成员的结构体在运行时绑定
- 预处理阶段（`#define`/`#ifdef`/`#include`）做宏替换和条件编译，在编译前完成
- `typedef`为类型取别名；`enum`给有限取值的int命名；`union`让多个成员共享同一块内存
- `static`限模块作用域或延长生命周期；`volatile`禁止编译器优化；`sizeof`编译期求大小
- 位操作（`&`/`|`/`~`/`^`/`<<`/`>>`）在底层编程和网络协议处理中频繁使用

## Main Arguments

C语言语法虽简单但通过指针、函数指针、宏等机制可以实现非常灵活的编程模式。掌握基础概念（内存模型、指针语义、编译链接过程）是深入理解C语言和嵌入式系统的前提。

## Related Concepts

- [[c-memory-management]] — 内存管理深入
- [[c-stack-mechanism]] — 栈的工作原理
- [[c-function-pointers]] — 函数指针详解
- [[c-compilation-pipeline]] — 源代码到可执行文件全流程
