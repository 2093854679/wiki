# Cursor 规则在嵌入式 C 项目中的深度应用与实例解析

## 摘要

本文深入剖析 Cursor 的规则系统，结合嵌入式 C 项目需求，展示如何创建、组织和应用规则以标准化代码风格、优化开发流程，同时提升代码质量，并为 AI 代理提供清晰上下文指导，助力团队高效协作与项目顺利推进。

## 规则在嵌入式 C 项目中的应用实例

### 项目规则目录规划

在嵌入式 C 项目中，合理规划项目规则目录至关重要。我们将规则分为项目范围规则、硬件相关规则、固件相关规则以及驱动开发规则等，分别存放在对应的目录中：

```
project/
  .cursor/rules/        # 项目范围规则
  hardware/
    .cursor/rules/      # 硬件相关规则
  firmware/
    .cursor/rules/      # 固件相关规则
  drivers/
    .cursor/rules/      # 驱动开发规则
```

### 代码风格与命名规范的实例化应用

以下是嵌入式 C 项目中代码风格与命名规范的规则示例：

---
description: 嵌入式C项目代码风格与命名规范
globs:
  - **/*.c
  - **/*.h
alwaysApply: true
---

#### 嵌入式C项目代码风格与命名规范

##### 1. 变量命名
- 使用小写字母和下划线分隔，例如：`int sensor_value;`
- 全局变量以`g_`开头，例如：`int g_system_state;`
- 局部变量直接使用小写字母和下划线。

##### 2. 函数命名
- 使用小写字母和下划线分隔，例如：`void initialize_sensor(void);`
- 系统级函数以`sys_`开头，例如：`void sys_init(void);`
- 驱动函数以模块名开头，例如：`void gpio_init(void);`

##### 3. 宏定义
- 使用大写字母和下划线分隔，例如：`#define MAX_SENSOR_COUNT 10`
- 条件编译宏以`CFG_`开头，例如：`#define CFG_DEBUG_MODE`

##### 4. 注释规范
- 每个函数必须有函数头注释，说明功能、参数和返回值。
- 重要变量和宏定义需要添加注释说明用途。
- 使用`//`或`/* */`注释，确保代码可读性。

#### 实例应用

在编写一个传感器初始化函数时，按照规则规范：

```c
// 传感器初始化函数
void initialize_sensor(void) {
    // 函数逻辑
}
```

全局变量定义：

```c
int g_system_state; // 全局系统状态变量
```

宏定义：

```c
#define MAX_SENSOR_COUNT 10 // 定义最大传感器数量
#define CFG_DEBUG_MODE   // 调试模式条件编译
```

## 硬件接口规则的实例化应用

以下是硬件接口开发规则示例：

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

## 固件开发规则的实例化应用

以下是固件开发规则示例：

---
description: 固件开发规则
globs:
  - **/*.c
  - **/*.h
alwaysApply: false
---

### 固件开发规则

#### 1. 任务调度
- 使用实时操作系统 (RTOS) 进行任务调度，避免使用轮询方式。
- 每个任务必须有明确的优先级和时间片。

#### 2. 内存管理
- 避免动态内存分配，使用静态内存分配。
- 如果必须使用动态内存，必须进行严格的内存检查和释放。

#### 3. 错误处理
- 所有函数必须返回状态码，例如：`int sensor_read(int *value);`
- 状态码必须明确表示成功或失败的原因。

#### 实例应用

任务调度示例：

```c
// RTOS任务调度示例
void main_task(void *pvParameters) {
    // 任务逻辑
    vTaskDelay(1000 / portTICK_PERIOD_MS); // 延时1秒
}
```

内存管理示例：

```c
// 静态内存分配示例
static uint8_t buffer[100]; // 静态分配100字节缓冲区
```

错误处理示例：

```c
// 传感器读取函数，返回状态码
int sensor_read(int *value) {
    if (value == NULL) {
        return ERROR_INVALID_PARAMETER;
    }
    // 读取传感器逻辑
    return SUCCESS;
}
```

## 驱动开发规则的实例化应用

以下是驱动开发规则示例：

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

## 自动生成规则的实例化应用

在开发过程中，我们可以通过聊天内容生成规则。例如，在讨论如何优化中断处理时，生成以下规则：

---
description: 中断处理优化规则
globs:
  - **/*.c
alwaysApply: false
---

### 中断处理优化规则

- 中断服务例程 (ISR) 必须尽量简洁，避免复杂逻辑。
- 在 ISR 中，尽量减少对全局变量的访问，使用局部变量。
- 如果 ISR 中需要执行复杂任务，建议将任务委派给主程序。

#### 实例应用

优化后的中断服务例程：

```c
// 定时器中断服务例程（优化后）
void isr_timer(void) {
    static uint32_t timer_count = 0; // 使用局部静态变量
    timer_count++;
    if (timer_count >= 1000) { // 简单逻辑判断
        timer_count = 0;
        // 设置主程序处理标志位
        g_main_task_flag = true;
    }
}
```

主程序处理：

```c
// 主程序
void main(void) {
    while (1) {
        if (g_main_task_flag) {
            g_main_task_flag = false;
            // 执行复杂任务逻辑
        }
        // 其他主程序逻辑
    }
}
```

## 使用方法总结

1. **创建规则**：在项目目录中创建`.cursor/rules`目录，并根据需要创建子目录（如hardware、firmware、drivers）。
2. **编写规则**：根据上述示例，将规则内容写入`.mdc`文件中。
3. **应用规则**：根据规则类型（如alwaysApply、globs等），规则将自动应用于相关文件或手动调用。
4. **生成规则**：在开发过程中，使用`/Generate Cursor Rules`命令根据聊天内容生成新的规则。

通过这些规则的创建、组织和应用，可以为嵌入式 C 项目提供清晰的开发指导，确保代码风格一致、开发流程规范，并为 AI 代理提供上下文支持，从而提升团队开发效率和代码质量。