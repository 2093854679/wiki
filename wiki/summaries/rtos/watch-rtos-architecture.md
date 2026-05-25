# OV-Watch RTOS任务架构

> **Source:** [watch.md](../../../raw/Study_Note/06-职业发展/面试记录/watch.md)
> **TLDR:** OV-Watch智能手表的完整FreeRTOS任务和消息队列架构——9个任务（8级优先级）、6个消息队列、10+定时器协作，实现Active/Idle/Stop三种运行模式的自动切换。

## Key Points

- **9个任务及优先级**：HardwareInitTask(osPriorityHigh3)→KeyTask/ChargCheckTask(High2)→ScrRenewTask/DataSaveTask(High1)→SensorDataUpdateTask/HRDataUpdateTask(Normal)→MessageSendTask(Normal)→StopEnterTask/IdleEnterTask(Low1)→LvHandlerTask(Low)
- **6个消息队列**：Key_MessageQueue（按键→屏幕更新）、Idle_MessageQueue（超时→息屏）、Stop_MessageQueue（深度睡眠触发）、IdleBreak_MessageQueue（交互→恢复亮度）、HomeUpdata_MessageQueue（唤醒→传感器刷新）、DataSave_MessageQueue（数据→EEPROM保存）
- **三模式切换**：Active（正常交互）→超时无操作→Idle（亮度降至5%节电）→进一步超时→Stop（深度睡眠，RTC/按键/充电/手腕抬起唤醒）
- **传感器刷新**：按需+周期结合；HomeUpdata消息触发立即刷新，RTC定时器提供周期性更新节拍
- **FreeRTOS定时器**：IdleTimer（空闲检测）、StopTimer（待机倒计时）、RTC保护定时器等10+个软件/硬件定时器
- **唤醒机制**：按键中断、充电检测、MPU手腕抬起检测、RTC定时唤醒（~1s周期性检查）
- **数据流**：传感器→SensorDataUpdateTask→DataSave_MessageQueue→DataSaveTask→EEPROM
- **LVGL集成**：LvHandlerTask处理GUI渲染（最低优先级，不影响传感器和通信的实时性）

## Related Concepts

- [[freertos-deep-dive]] — FreeRTOS内核机制
- [[ovwatch-code-style]] — 硬件接口层设计
- [[embedded-registration-patterns]] — 模块注册设计模式
