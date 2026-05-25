# C语言内存管理

> **Source:** [05-内存管理.md](../../../raw/Study_Note/01-编程语言/C语言/05-内存管理.md)
> **TLDR:** C语言内存模型：栈/堆/全局区/代码段的划分、malloc/free的使用与常见陷阱、内存泄漏和野指针的防范。

## Key Points

- **进程内存布局**：代码段(.text) → 数据段(.data, .bss) → 堆(heap, 向上增长) → ... → 栈(stack, 向下增长) → 内核空间
- **栈（Stack）**：由编译器自动管理，存储局部变量和函数返回地址；容量有限（通常8-16MB）；LIFO结构；不要返回局部变量的地址
- **堆（Heap）**：由程序员手动管理（`malloc`/`calloc`/`realloc`/`free`）；适合动态大小的数据；忘记释放→内存泄漏；释放后继续使用→悬垂指针
- **全局/静态区**：存储全局变量和static变量，程序运行期间一直存在；`.data`存已初始化的，`.bss`存未初始化的
- **常见陷阱**：①malloc/free不配对 ②多次free ③野指针（free后未置NULL） ④栈溢出（过大局部变量/深递归） ⑤内存碎片
- **工具**：Valgrind（Linux）检测内存泄漏；静态分析工具（Coverity/PC-lint）在编译期发现问题

## Main Arguments

C语言直接暴露内存管理给程序员，这是它高效和灵活的来源，也是最容易出错的环节。嵌入式系统中内存有限，更需要精确控制每一块内存的分配和释放。养成配对使用malloc/free、释放后置NULL的习惯是防范内存bug的基础。

## Related Concepts

- [[c-stack-mechanism]] — 栈的工作机制
- [[c-language-basics]] — C语言基础
- [[freertos-memory-management]] — FreeRTOS内存管理
