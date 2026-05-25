# OV-Watch代码风格学习

> **Source:** [ovwatch代码风格学习.md](../../raw/Study_Note/02-嵌入式开发/代码风格/note/ovwatch代码风格学习.md)
> **TLDR:** 基于接口聚合的硬件中间层设计——为每类硬件定义包含函数指针的接口结构体，用总结构体`HW_InterfaceTypeDef`聚合所有设备接口，实现UI/业务与BSP解耦。

## Key Points

- **接口结构体设计**：每种硬件设备定义独立接口类型，包含状态变量+操作函数指针（Init/Enable/Disable/Read/Write等）
- **总结构体聚合**：`HW_InterfaceTypeDef`聚合所有设备接口——RTC/BLE/Power/LCD/IMU/AHT21/Barometer/Ecompass/HR_meter
- **全局实例化**：`HW_InterfaceTypeDef HWInterface = { .RealTimeClock = {...}, .BLE = {...}, ... }` 统一访问入口
- **运行时初始化**：`HardwareInitTask`内按设备执行`HWInterface.*.Init()`并设置运行参数
- **核心优势**：①解耦——UI层仅面对`HWInterface` ②可替换——换传感器只需改函数指针 ③便测试——可注入虚拟实现 ④可维护——集中管理设备状态
- **短路处理**：注意硬件接口函数的短路条件——设备未初始化或通信异常时的默认返回值

## Related Concepts

- [[embedded-registration-patterns]] — 模块注册机制的演进
- [[watch-rtos-architecture]] — OV-Watch RTOS任务架构
