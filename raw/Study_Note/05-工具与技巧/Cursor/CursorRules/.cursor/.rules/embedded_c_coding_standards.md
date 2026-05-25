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
