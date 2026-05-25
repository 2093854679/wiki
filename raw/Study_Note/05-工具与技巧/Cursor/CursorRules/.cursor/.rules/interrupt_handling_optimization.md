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
