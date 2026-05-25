# MCU启动流程

> **Source:** [03-mcu的启动流程.md](../../../raw/Study_Note/02-嵌入式开发/MCU基础/03-mcu的启动流程.md)
> **TLDR:** ARM Cortex-M上电后的完整启动序列：复位→SP/PC初始化→SystemInit→__main（数据段搬移+BSS清零）→main()。理解启动流程是嵌入式底层开发的基础。

## Key Points

- **上电复位向量**：`0x00000000`存初始SP值，`0x00000004`存Reset_Handler地址；上电后硬件自动加载SP，跳转到Reset_Handler
- **Reset_Handler流程**：①调用SystemInit()——初始化时钟、PLL、Flash等待周期 ②调用__main()（C库初始化）
- **__main()内部**：①搬运.data段（从Flash的加载区拷贝到RAM的执行区） ②清零.bss段 ③初始化堆和栈 ④调用main()
- **中断向量表**：位于Flash起始处，包含所有异常和中断的入口地址；每个向量4字节
- **分散加载（Scatter Loading）**：用于复杂内存布局——代码在Flash执行，部分函数/数据搬移到RAM加速
- **启动文件（startup_xxx.s）**：汇编实现，定义向量表、Reset_Handler和默认中断处理函数
- **不同MCU差异**：STM32有boot引脚选择启动区域；ESP32有二级bootloader；ARM9/ARM11有更复杂的初始化流程

## Related Concepts

- [[lr-er-load-execute-regions]] — 加载区LR和执行区ER
- [[arm-registers]] — ARM寄存器
- [[c-compilation-pipeline]] — 编译到执行的完整链路
