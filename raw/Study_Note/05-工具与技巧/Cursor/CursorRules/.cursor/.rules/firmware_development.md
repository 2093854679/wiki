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
