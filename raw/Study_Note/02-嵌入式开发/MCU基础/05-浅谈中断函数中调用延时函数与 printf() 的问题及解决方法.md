

# 🚫 浅谈中断函数中调用延时函数与 printf() 的问题及解决方法

（以 STM32 为例）

在嵌入式开发中，中断（Interrupt）几乎无处不在。
 但许多初学者在中断服务函数（ISR）中调用 **延时函数（delay）** 或 **`printf()`** 时，常常会遇到一种现象：

> 程序卡死、系统无响应、甚至需要复位。

这些问题的根源并不复杂，但非常容易踩坑。
 本文将深入讲清楚：

1. 为什么中断中不能使用延时函数；
2. 为什么中断中不能使用 printf；
3. 以及安全、正确的替代方案。

------

## 一、现象：中断中使用延时导致系统卡死

例如下面的代码：

```c
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(GPIO_Pin == KEY_Pin)
    {
        HAL_Delay(20); // 想要做按键消抖
        if(HAL_GPIO_ReadPin(KEY_GPIO_Port, KEY_Pin) == GPIO_PIN_RESET)
        {
            // 执行按键操作
        }
    }
}
```

表面看起来没问题，但运行后你会发现：

- 程序一旦进入中断，就卡死；
- 系统不再响应；
- 有时重启还能运行一次，然后又挂掉。

------

## 二、原因：中断屏蔽了系统时基

在 STM32 HAL 库中，`HAL_Delay()` 依赖系统节拍 `SysTick` 实现计时。

```c
void HAL_Delay(uint32_t Delay)
{
    uint32_t tickstart = HAL_GetTick();
    while((HAL_GetTick() - tickstart) < Delay) { }
}
```

而 `HAL_GetTick()` 的值是由 `SysTick_Handler()` 每 1ms 递增的。
 但是：

> MCU 进入中断后，会屏蔽同级及以下优先级的中断。

结果就是：

- SysTick 中断被屏蔽；
- `HAL_GetTick()` 不再更新；
- 延时循环永远等不到时间过去；
- ❌ 程序卡死在中断里。

------

## 三、更隐蔽的情况：人为触发中断的不确定性

例如按键触发中断。
 人的操作时间不确定，当中断触发时：

- 延时逻辑（如 20ms 消抖）可能早已“超时”；
- 导致中断内等待的计时逻辑失效；
- 最终形成死循环或逻辑错乱。

------

## 四、错误的结论：不是“不能延时”，而是“延时位置不对”

中断内延时的本质问题在于**阻塞和时基丢失**。
 正确做法是把延时移到主循环或由定时器异步完成。

------

## 五、正确的解决方案 ✅

### ✅ 方法 1：中断内只置标志，主循环中执行延时逻辑

```c
volatile uint8_t key_flag = 0;

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(GPIO_Pin == KEY_Pin)
        key_flag = 1; // 仅置标志位
}

int main(void)
{
    HAL_Init();
    while(1)
    {
        if(key_flag)
        {
            key_flag = 0;
            HAL_Delay(20); // 主循环中可安全延时
            if(HAL_GPIO_ReadPin(KEY_GPIO_Port, KEY_Pin) == GPIO_PIN_RESET)
            {
                // 执行按键逻辑
            }
        }
    }
}
```

👉 中断快进快出，延时在主循环中执行，系统安全稳定。

------

### ✅ 方法 2：使用定时器计数实现“软延时”

```c
volatile uint8_t key_flag = 0;
volatile uint16_t delay_counter = 0;

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(GPIO_Pin == KEY_Pin)
    {
        key_flag = 1;
        delay_counter = 0; // 重新计时
    }
}

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
    if(key_flag)
    {
        delay_counter++;
        if(delay_counter >= 20)  // 计数20ms
        {
            key_flag = 0;
            delay_counter = 0;
            if(HAL_GPIO_ReadPin(KEY_GPIO_Port, KEY_Pin) == GPIO_PIN_RESET)
            {
                // 执行按键逻辑
            }
        }
    }
}
```

这里用定时器周期中断（如 1ms 周期）替代延时函数，避免阻塞。

------

### ✅ 方法 3：硬件层面消抖或滤波

硬件方案也可以从根本上减少中断触发频率：

- 在按键输入端串联 RC 滤波电路；
- 使用 GPIO 硬件滤波功能；
- 通过定时器输入捕获方式采样输入信号。

------

## 六、同类问题：中断中使用 `printf()` 也会出错 ❗

很多人喜欢在中断中调试打印：

```c
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    printf("Button Pressed!\r\n");
}
```

运行后你可能发现系统时不时卡死、复位或异常。
 这并不是偶然 —— 它的根本原因如下。

------

## 七、为什么中断中不能使用 `printf()`

### 1️⃣ `printf()` 实际上会调用 UART 发送函数

在 STM32 工程中，一般会重定向 `printf` 到串口：

```c
int fputc(int ch, FILE *f)
{
    HAL_UART_Transmit(&huart1, (uint8_t *)&ch, 1, HAL_MAX_DELAY);
    return ch;
}
```

而 `HAL_UART_Transmit()` 是**阻塞式发送**，会一直等待 UART 完成发送。

------

### 2️⃣ 在中断中执行会卡死或死锁

原因如下：

| 问题点           | 说明                    |
| ---------------- | ----------------------- |
| 串口发送是阻塞的 | 需要等待发送完成        |
| 中断屏蔽其他中断 | UART 的发送中断被屏蔽   |
| UART 状态为 BUSY | printf 在等待 UART 空闲 |
| 死锁产生         | UART 永远等不到完成信号 |

于是中断被卡住，系统挂死。

------

## 八、正确替代方法 ✅

### ✅ 方法 1：中断中只置标志，主循环打印

```c
volatile uint8_t uart_flag = 0;

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    uart_flag = 1; // 仅置标志
}

int main(void)
{
    while(1)
    {
        if(uart_flag)
        {
            uart_flag = 0;
            printf("Button Pressed!\r\n"); // 主循环打印
        }
    }
}
```

### ✅ 方法 2：建立异步日志系统（环形缓冲 + DMA）

可以设计一个日志模块，把中断内的信息放入缓冲区中，由后台 DMA 异步发送。

优点：

- 不阻塞；
- 中断可安全调用；
- 高速稳定。

------

## 九、总结 🔚

| 项目     | 不推荐做法               | 原因           | 推荐方案                         |
| -------- | ------------------------ | -------------- | -------------------------------- |
| 延时函数 | 中断中使用 `HAL_Delay()` | 阻塞、时基停止 | 中断中置标志 + 定时器/主循环判断 |
| printf   | 中断中直接 `printf()`    | 串口阻塞、死锁 | 中断中置标志 + 异步日志输出      |

------

## ✍️ 十、结语

> **中断函数应“快进快出”，绝不做阻塞操作。**

中断中禁止：

- 使用 `HAL_Delay()`；
- 使用 `printf()`；
- 使用长循环或等待标志的操作。

正确思路：

- 中断只做事件标记；
- 主循环或定时器中执行耗时逻辑；
- 需要打印就做异步输出。

这样你的系统才能真正稳定、可靠地运行。