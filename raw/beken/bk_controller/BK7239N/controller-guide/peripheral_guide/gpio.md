---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/gpio.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="gpio"></a>

# GPIO 驱动

<a id="id1"></a>

## 概述

GPIO（General Purpose Input/Output）通用输入输出接口是微控制器最基本的数字接口，用于控制外部设备和读取外部信号。BK7239N 提供丰富的 GPIO 资源，支持多种配置和功能。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 GPIO 通道同时工作
- **输入输出模式**：支持输入和输出模式配置
- **上拉下拉**：支持内部上拉、下拉电阻配置
- **中断支持**：支持上升沿、下降沿、双边沿中断
- **唤醒功能**：支持 GPIO 唤醒低功耗模式
- **复用功能**：支持 GPIO 复用为其他外设功能
- **驱动能力**：支持多种驱动能力配置
- **低功耗保持**：支持低功耗模式下状态保持
- **外部 LDO 控制**：支持外部 LDO 控制功能
- **时钟控制**：支持时钟引脚控制

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_gpio\_driver\_init() 初始化 GPIO 驱动
   \- 配置 GPIO 模式（输入/输出）
   \- 根据需要配置上拉/下拉电阻
   \- 配置中断和唤醒功能
2. **基本使用**
   \- 使用 bk\_gpio\_enable\_output() 配置为输出模式
   \- 使用 bk\_gpio\_enable\_input() 配置为输入模式
   \- 使用 bk\_gpio\_set\_output\_high() 和 bk\_gpio\_set\_output\_low() 控制输出
   \- 使用 bk\_gpio\_get\_input() 读取输入状态
3. **中断处理**
   \- 配置中断类型（上升沿/下降沿/双边沿）
   \- 注册中断服务函数
   \- 启用/禁用中断
4. **唤醒功能**
   \- 配置 GPIO 为唤醒源
   \- 设置唤醒条件
   \- 处理唤醒事件

<a id="id4"></a>

## 注意事项

- 确保在调用其他 GPIO API 前先调用 bk\_gpio\_driver\_init()
- GPIO 复用功能需要与硬件设计匹配
- 中断配置需要与硬件连接匹配
- 使用唤醒功能时注意功耗管理
- 注意 GPIO 的电气特性和驱动能力
- 低功耗模式下 GPIO 状态可能改变

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_gpio\_driver\_init() \- 初始化 GPIO 驱动
- bk\_gpio\_driver\_deinit() \- 反初始化 GPIO 驱动
- bk\_gpio\_set\_value() \- 设置 GPIO 值
- bk\_gpio\_get\_value() \- 获取 GPIO 值
- bk\_gpio\_enable\_output() \- 启用输出模式
- bk\_gpio\_disable\_output() \- 禁用输出模式
- bk\_gpio\_enable\_input() \- 启用输入模式
- bk\_gpio\_disable\_input() \- 禁用输入模式
- bk\_gpio\_pull\_up() \- 配置上拉
- bk\_gpio\_pull\_down() \- 配置下拉
- bk\_gpio\_set\_config() \- 设置 GPIO 配置
- bk\_gpio\_set\_output\_high() \- 设置输出高电平
- bk\_gpio\_set\_output\_low() \- 设置输出低电平
- bk\_gpio\_get\_input() \- 获取输入状态
- bk\_gpio\_set\_capacity() \- 设置驱动能力
- bk\_gpio\_set\_interrupt\_type() \- 设置中断类型
- bk\_gpio\_enable\_interrupt() \- 启用中断
- bk\_gpio\_disable\_interrupt() \- 禁用中断
- bk\_gpio\_clear\_interrupt() \- 清除中断
- bk\_gpio\_register\_isr() \- 注册中断服务函数
- bk\_gpio\_unregister\_isr() \- 注销中断服务函数
- bk\_gpio\_set\_wakeup\_source() \- 设置唤醒源
- bk\_gpio\_clear\_wakeup\_source() \- 清除唤醒源
- bk\_gpio\_low\_power\_keep\_status() \- 低功耗保持状态
- bk\_gpio\_external\_ldo\_control() \- 外部 LDO 控制
- bk\_gpio\_clock\_pin\_control() \- 时钟引脚控制
- bk\_gpio\_retention() \- GPIO 保持功能

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/gpio.h>

void gpio_example(void)
{
    // 初始化 GPIO 驱动
    bk_gpio_driver_init();

    // 配置 GPIO0 为输出模式
    bk_gpio_enable_output(GPIO_0);
    bk_gpio_set_output_high(GPIO_0);

    // 配置 GPIO1 为输入模式
    bk_gpio_enable_input(GPIO_1);
    bk_gpio_pull_up(GPIO_1);

    // 读取输入状态
    uint32_t input_state = bk_gpio_get_input(GPIO_1);
    printf("GPIO1 Input: %d\n", input_state);
}
```

中断处理示例：

```
static void gpio_interrupt_handler(gpio_id_t id)
{
    printf("GPIO %d interrupt triggered\n", id);

    // 清除中断标志
    bk_gpio_clear_interrupt(id);
}

void gpio_interrupt_example(void)
{
    // 配置 GPIO2 为输入模式
    bk_gpio_enable_input(GPIO_2);
    bk_gpio_pull_up(GPIO_2);

    // 配置下降沿中断
    bk_gpio_set_interrupt_type(GPIO_2, GPIO_INT_TYPE_FALLING_EDGE);

    // 注册中断服务函数
    bk_gpio_register_isr(GPIO_2, gpio_interrupt_handler);

    // 启用中断
    bk_gpio_enable_interrupt(GPIO_2);
}
```

唤醒功能示例：

```
void gpio_wakeup_example(void)
{
    // 配置 GPIO3 为输入模式
    bk_gpio_enable_input(GPIO_3);
    bk_gpio_pull_up(GPIO_3);

    // 配置下降沿唤醒
    bk_gpio_set_interrupt_type(GPIO_3, GPIO_INT_TYPE_FALLING_EDGE);

    // 设置唤醒源
    bk_gpio_set_wakeup_source(GPIO_3);

    // 进入低功耗模式
    // 系统将在 GPIO3 下降沿时唤醒
}
```

复用功能示例：

```
void gpio_mux_example(void)
{
    // 配置 GPIO4 为 UART TX 功能
    bk_gpio_set_config(GPIO_4, GPIO_CONFIG_UART_TX);

    // 配置 GPIO5 为 SPI CLK 功能
    bk_gpio_set_config(GPIO_5, GPIO_CONFIG_SPI_CLK);
}
```

低功耗保持示例：

```
void gpio_low_power_example(void)
{
    // 设置 GPIO6 在低功耗模式下保持状态
    bk_gpio_low_power_keep_status(GPIO_6, true);

    // 进入低功耗模式
    // GPIO6 状态将被保持
}
```

<a id="id6"></a>

## 常见问题

- **GPIO 状态不正确**：检查 GPIO 模式配置、上拉/下拉设置
- **中断未触发**：确认中断类型设置、中断启用状态
- **唤醒失败**：检查唤醒源配置、GPIO 状态
- **复用功能不工作**：确认 GPIO 复用配置与硬件设计匹配

<a id="id7"></a>

## 实战示例

1. 外部中断按键示例（下降沿触发）

```
static void key_isr(gpio_id_t id) {
    // 处理按键事件
    bk_gpio_clear_interrupt(id);
}
bk_gpio_enable_input(GPIO_KEY);
bk_gpio_pull_up(GPIO_KEY);
bk_gpio_set_interrupt_type(GPIO_KEY, GPIO_INT_TYPE_FALLING_EDGE);
bk_gpio_register_isr(GPIO_KEY, key_isr);
bk_gpio_enable_interrupt(GPIO_KEY);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_GPIO\_CHAN\_ID：GPIO 号非法
- BK\_ERR\_GPIO\_NOT\_INPUT\_MODE：当前非输入模式却调用读取/中断等接口
- BK\_ERR\_GPIO\_INVALID\_INT\_TYPE：中断类型非法或不支持
