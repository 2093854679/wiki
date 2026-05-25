# 函数指针

> **Source:** [03-函数指针.md](../../raw/Study_Note/01-编程语言/C语言/03-函数指针.md)
> **TLDR:** 函数指针本质是指向代码段函数入口地址的指针变量，用于实现回调、OOP模拟和动态行为绑定。

## Key Points

- 函数编译后位于可执行文件的text段，加载到进程代码段，函数指针指向函数第一条指令的地址
- 定义语法：`ret_type (*func_ptr)(param_list)` — 括号必不可少
- 函数名本身代表函数地址，`func_ptr = &function` 与 `func_ptr = function` 等价
- 通过函数指针调用：`(*func_ptr)(args)` 或 `func_ptr(args)`（两种写法等价）
- 函数指针数组：`int (*ops[4])(int, int) = {add, sub, mul, div}` 实现操作表
- 回调函数（callback）是函数指针的主要应用场景——将函数A的指针传给B，B在适当时机调用A
- 用包含函数指针的结构体模拟OOP：`typedef struct { void (*print)(void*); void (*destroy)(void*); } Object;`
- `typedef`简化函数指针类型：`typedef void (*PF)(int);` 之后可以 `PF ptr;`

## Main Arguments

函数指针是C语言实现动态行为绑定的核心机制。虽然语法稍显复杂（尤其是指向函数指针的指针），但其在嵌入式系统、操作系统内核和框架设计中的重要性不可替代。

## Related Concepts

- [[c-language-basics]] — C语言基础
- [[embedded-registration-patterns]] — 嵌入式模块注册机制
