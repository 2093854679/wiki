# 中断函数中使用延时和printf的问题

> **Source:** [05-浅谈中断函数中调用延时函数与printf()的问题及解决方法.md](../../raw/Study_Note/02-嵌入式开发/MCU基础/05-浅谈中断函数中调用延时函数与printf()的问题及解决方法.md)
> **TLDR:** 中断服务程序（ISR）中调用阻塞函数（delay/printf）的危害——中断延迟增大、系统卡死、堆栈溢出；正确的做法是用标志位+主循环或任务处理。

## Key Points

- **问题根源**：ISR必须快速执行完毕以响应下一次中断；delay占用CPU空转阻塞中断返回，printf依赖UART发送（慢速外设+可能使用中断），在ISR中调用会导致严重阻塞
- **delay在ISR中的问题**：①阻塞其他中断（尤其同优先级和低优先级） ②破坏实时性 ③硬件定时器/指令循环delay可能依赖中断才能计时，在ISR中失效
- **printf在ISR中的问题**：①UART发送速度慢（115200bps≈10KB/s），发送"hello"需约0.5ms ②printf常依赖中断驱动UART，在ISR中被阻塞形成死锁 ③printf内部有锁机制，可能导致优先级反转
- **正确方案**：ISR中只做紧急处理（读外设寄存器、清中断标志、设置标志位），把耗时操作放到主循环或低优先级任务
- **设计模式**：ISR→置标志位→主循环/Deferred Task轮询标志并处理；或者使用FreeRTOS的Deferred Interrupt（ISR→发送信号量/消息队列→任务处理）

## Related Concepts

- [[freertos-task-management]] — FreeRTOS任务与中断管理
- [[embedded-registration-patterns]] — 嵌入式设计模式
