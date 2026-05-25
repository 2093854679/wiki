---
description: 硬件接口开发规则
globs:
  - **/*.c
  - **/*.h
alwaysApply: false
---

### 硬件接口开发规则

#### 1. 硬件抽象层 (HAL)
- 所有硬件操作必须通过硬件抽象层实现，避免直接操作硬件寄存器。
- HAL 函数命名格式：`hal_<module>_<function>()`，例如：`hal_gpio_read(int pin);`

#### 2. 硬件初始化
- 在系统启动时，必须调用硬件初始化函数，例如：`void hal_init(void);`
- 初始化函数必须检查硬件状态，确保硬件正常工作。

#### 3. 中断处理
- 中断服务例程 (ISR) 必须以`isr_`开头，例如：`void isr_timer(void);`
- ISR 中避免使用复杂的逻辑，尽量将任务委派给主程序。

#### 实例应用

硬件抽象层函数定义：

```c
// GPIO读取函数
int hal_gpio_read(int pin) {
    // 读取GPIO引脚状态逻辑
    return gpio_status;
}
```

硬件初始化函数：

```c
// 硬件初始化函数
void hal_init(void) {
    // 初始化逻辑
    // 检查硬件状态
}
```

中断服务例程：

```c
// 定时器中断服务例程
void isr_timer(void) {
    // 简单处理逻辑
    // 将复杂任务委派给主程序
}
```
