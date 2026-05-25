# 面试记录

> **Source:** [博坦面试.md](../../../raw/Study_Note/06-职业发展/面试记录/博坦面试.md), [博通集成实习面试.md](../../../raw/Study_Note/06-职业发展/面试记录/博通集成实习面试.md), [邦普面试.md](../../../raw/Study_Note/06-职业发展/面试记录/邦普面试.md)
> **TLDR:** 三场嵌入式面试的QA实录——博坦（TCP握手/I2C/OTA/FreeRTOS栈/端序）、博通集成（项目经验/静态变量/.bss段/短路求值）、邦普（SDK对比/I2C细节/OTA Flash分区/调试方法）。

## Key Points

### 博坦面试
- TCP三次握手（SYN→SYN-ACK→ACK）和四次挥手（FIN→ACK→FIN→ACK，半关闭导致额外一次）
- I2C地址长度：7位→112可用设备，10位→约1000设备
- OTA双区升级：乒乓分区、CRC校验时机、掉电恢复机制
- STM32端序为小端（Little Endian）
- FreeRTOS MSP（主堆栈指针）vs PSP（进程堆栈指针）在上下文切换中的角色
- FreeRTOS优先级：0为最低优先级，数值越大优先级越高

### 博通集成实习面试
- 智能送药小车项目：OpenMV→STM32通过UART+IDLE中断+消息队列通信
- 局部变量存储在栈（Stack）上
- .bss段存储未初始化的全局/静态变量（不占Flash空间）
- static关键字三种用法：限文件作用域、延长生命周期、保持值
- 短路求值：`&&`左侧false则不执行右侧；`||`左侧true则不执行右侧（应用：`if(p != NULL && p->value > 0)`安全判断）

### 邦普面试
- 实习中SDK代码与自写代码的编程技巧差异
- STM32F103C8T6：Flash 64KB, RAM 20KB
- 编译后代码大小查看：.map文件各段分析（Code/RO-data/RW-data/ZI-data）
- OTA升级中Flash分区设计：Bootloader+App+App备份+用户数据区
- 常见调试方法：串口打印、LED指示、逻辑分析仪、HardFault分析

## Related Concepts

- [[embedded-interview-prep]] — 完整面经题库
- [[watch-rtos-architecture]] — OV-Watch项目详解
- [[i2c-protocol]] — I2C知识点
- [[tcp-protocol-basics]] — TCP知识点
