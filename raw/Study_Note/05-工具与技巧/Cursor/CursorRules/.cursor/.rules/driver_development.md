---
description: 驱动开发规则
globs:
  - **/*.c
  - **/*.h
alwaysApply: false
---

### 驱动开发规则

#### 1. 驱动结构
- 每个驱动必须有初始化、读取、写入和关闭函数。
- 驱动函数命名格式：`driver_<module>_<function>()`，例如：`void driver_uart_init(void);`

#### 2. 错误处理
- 驱动函数必须返回状态码，例如：`int driver_sensor_read(int *value);`
- 状态码必须明确表示成功或失败的原因。

#### 3. 硬件依赖
- 驱动必须通过硬件抽象层 (HAL) 访问硬件，避免直接操作硬件寄存器。

#### 实例应用

驱动初始化函数：

```c
// UART驱动初始化函数
void driver_uart_init(void) {
    // 初始化UART逻辑
    hal_uart_configure(); // 通过HAL配置UART
}
```

驱动读取函数：

```c
// 传感器驱动读取函数，返回状态码
int driver_sensor_read(int *value) {
    if (value == NULL) {
        return ERROR_INVALID_PARAMETER;
    }
    // 读取传感器逻辑，通过HAL操作硬件
    return SUCCESS;
}
```

驱动关闭函数：

```c
// UART驱动关闭函数
void driver_uart_close(void) {
    // 关闭UART逻辑
    hal_uart_deinit(); // 通过HAL去初始化UART
}
```
