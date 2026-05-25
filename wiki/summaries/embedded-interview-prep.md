# 嵌入式面经

> **Source:** [面经.md](../../raw/Study_Note/06-职业发展/实习记录/my_doc/八股文/面经.md)
> **TLDR:** 嵌入式软件岗位面试题全集——覆盖C语言（struct对齐/volatile/static/内存管理）、RTOS（FreeRTOS移植/上下文切换/优先级反转/互斥量vs信号量）、通信协议（I2C/CAN/SPI/WiFi）、系统架构和开发工具（GDB/CMake/Makefile/OTA）。

## Key Points

- **C语言高频**：struct内存对齐（`#pragma pack`/`__attribute__((packed))`）、volatile含义和应用场景、static三种用法、指针vs数组、strlen vs sizeof、堆vs栈
- **RTOS高频**：FreeRTOS移植要点（portable层/SysTick/PendSV）、上下文切换过程（寄存器保存→TCB切换→恢复）、优先级反转与解决（优先级继承）、互斥量vs信号量在ISR中的使用限制
- **协议高频**：I2C死锁原因与恢复（SDA被从机拉低→软件复位/时钟连续脉冲解锁）、CAN总线仲裁机制、采样点配置、SPI四种模式
- **源码到可执行**：预处理→编译→汇编→链接全流程，.bin vs .elf vs .hex区别
- **内存屏障**：多核MCU中的volatile不足以保证可见性，需要DSB/DMB/ISB指令
- **GDB调试**：断点(breakpoint)、观察点(watchpoint)、条件断点、coredump分析
- **OTA升级**：双区/差分升级、回滚机制、CRC校验时机
- **Linux基础**：uboot到Linux启动流程、USB设备挂载过程、内核裁剪

## Related Concepts

- [[i2c-protocol]]
- [[freertos-deep-dive]]
- [[c-memory-management]]
- [[spi-protocol]]
- [[ble-protocol-overview]]
