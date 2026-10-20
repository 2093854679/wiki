---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/pwm.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="pwm"></a>

# PWM 驱动

<a id="id1"></a>

## 概述

PWM（Pulse Width Modulation）脉宽调制是一种通过改变脉冲宽度来控制输出功率的技术，广泛应用于电机控制、LED 调光、音频输出等场景。BK7239N 支持多个 PWM 通道，提供灵活的脉宽调制解决方案。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 PWM 通道同时工作
- **周期占空比**：支持灵活的周期和占空比配置
- **相移功能**：支持多通道相移输出
- **渐变功能**：支持占空比渐变输出
- **中断支持**：支持 PWM 完成中断
- **频率控制**：支持多种频率设置
- **占空比控制**：支持 0-100% 占空比控制
- **相位控制**：支持相位偏移控制
- **低功耗**：支持低功耗模式，节省功耗

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_pwm\_driver\_init() 初始化 PWM 驱动
   \- 配置 PWM 参数（周期、占空比、频率等）
   \- 调用 bk\_pwm\_init() 初始化具体 PWM 通道
   \- 根据需要配置中断
2. **基本使用**
   \- 使用 bk\_pwm\_set\_period\_duty() 设置周期和占空比
   \- 使用 bk\_pwm\_start() 启动 PWM 输出
   \- 使用 bk\_pwm\_stop() 停止 PWM 输出
   \- 使用 bk\_pwm\_set\_duty() 动态调整占空比
3. **相移功能**
   \- 使用 bk\_pwm\_phase\_shift\_init() 初始化相移模式
   \- 配置多个通道的占空比和相位
   \- 使用 bk\_pwm\_phase\_shift\_start() 启动相移输出
4. **渐变功能**
   \- 使用 bk\_pwm\_fade\_init() 初始化渐变模式
   \- 设置渐变参数（起始/结束占空比、渐变时间）
   \- 使用 bk\_pwm\_fade\_start() 启动渐变输出

<a id="id4"></a>

## 注意事项

- 确保在调用其他 PWM API 前先调用 bk\_pwm\_driver\_init()
- 占空比不能超过周期值
- 频率设置需要考虑硬件限制
- 使用中断模式时注意中断优先级设置
- 注意 PWM 信号线的电气特性
- 低功耗模式下 PWM 可能被关闭，需要重新初始化

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_pwm\_driver\_init() \- 初始化 PWM 驱动
- bk\_pwm\_driver\_deinit() \- 反初始化 PWM 驱动
- bk\_pwm\_init() \- 初始化 PWM 通道
- bk\_pwm\_deinit() \- 反初始化 PWM 通道
- bk\_pwm\_start() \- 启动 PWM 输出
- bk\_pwm\_stop() \- 停止 PWM 输出
- bk\_pwm\_set\_period\_duty() \- 设置周期和占空比
- bk\_pwm\_set\_duty() \- 设置占空比
- bk\_pwm\_set\_frequency() \- 设置频率
- bk\_pwm\_set\_phase() \- 设置相位
- bk\_pwm\_phase\_shift\_init() \- 初始化相移模式
- bk\_pwm\_phase\_shift\_start() \- 启动相移输出
- bk\_pwm\_phase\_shift\_stop() \- 停止相移输出
- bk\_pwm\_fade\_init() \- 初始化渐变模式
- bk\_pwm\_fade\_start() \- 启动渐变输出
- bk\_pwm\_fade\_stop() \- 停止渐变输出
- bk\_pwm\_register\_isr() \- 注册中断服务函数
- bk\_pwm\_unregister\_isr() \- 注销中断服务函数
- bk\_pwm\_enable\_interrupt() \- 启用中断
- bk\_pwm\_disable\_interrupt() \- 禁用中断

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/pwm.h>

void pwm_example(void)
{
    pwm_init_config_t config = {
        .period_cycle = 1000,
        .duty_cycle = 500,
        .freq = 1000
    };

    // 初始化 PWM 驱动
    bk_pwm_driver_init();

    // 初始化 PWM 通道 0
    bk_pwm_init(PWM_CHAN_0, &config);

    // 启动 PWM 输出
    bk_pwm_start(PWM_CHAN_0);

    // 动态调整占空比
    bk_pwm_set_duty(PWM_CHAN_0, 750);  // 75% 占空比
}
```

相移输出示例：

```
void pwm_phase_shift_example(void)
{
    pwm_phase_shift_config_t config = {
        .psc = 0,
        .period_cycle = 1000,
        .chan_num = 2,
        .duty_config = {
            {.chan = PWM_CHAN_0, .duty_cycle = 300},
            {.chan = PWM_CHAN_1, .duty_cycle = 300}
        }
    };

    // 初始化相移模式
    bk_pwm_phase_shift_init(&config);

    // 启动相移输出
    bk_pwm_phase_shift_start();
}
```

渐变输出示例：

```
void pwm_fade_example(void)
{
    pwm_fade_config_t config = {
        .chan = PWM_CHAN_0,
        .start_duty = 0,
        .end_duty = 1000,
        .fade_time_ms = 2000
    };

    // 初始化渐变模式
    bk_pwm_fade_init(&config);

    // 启动渐变输出
    bk_pwm_fade_start(PWM_CHAN_0, PWM_DUTY_DIR_INCREASE);
}
```

中断处理示例：

```
static void pwm_interrupt_handler(pwm_chan_t chan, void *param)
{
    printf("PWM channel %d interrupt\n", chan);
}

void pwm_interrupt_example(void)
{
    // 注册中断服务函数
    bk_pwm_register_isr(PWM_CHAN_0, pwm_interrupt_handler, NULL);

    // 启用中断
    bk_pwm_enable_interrupt(PWM_CHAN_0);
}
```

多通道控制示例：

```
void pwm_multi_channel_example(void)
{
    // 初始化多个通道
    pwm_init_config_t config = {
        .period_cycle = 1000,
        .duty_cycle = 500,
        .freq = 1000
    };

    bk_pwm_init(PWM_CHAN_0, &config);
    bk_pwm_init(PWM_CHAN_1, &config);
    bk_pwm_init(PWM_CHAN_2, &config);

    // 启动所有通道
    bk_pwm_start(PWM_CHAN_0);
    bk_pwm_start(PWM_CHAN_1);
    bk_pwm_start(PWM_CHAN_2);

    // 分别设置不同的占空比
    bk_pwm_set_duty(PWM_CHAN_0, 250);  // 25%
    bk_pwm_set_duty(PWM_CHAN_1, 500);  // 50%
    bk_pwm_set_duty(PWM_CHAN_2, 750);  // 75%
}
```

<a id="id6"></a>

## 常见问题

- **PWM 输出不正确**：检查周期和占空比设置、频率配置
- **相移不工作**：确认相移配置、通道数量、占空比设置
- **渐变不平滑**：调整渐变时间、起始/结束占空比
- **中断未触发**：确认中断注册和启用，检查中断优先级设置

<a id="id7"></a>

## 实战示例

1. 多通道相移输出

```
pwm_phase_shift_config_t sc = {
    .psc = 0,
    .period_cycle = 1000,
    .chan_num = 2,
    .duty_config = {
        { .chan = PWM_CH0, .duty_cycle = 300 },
        { .chan = PWM_CH1, .duty_cycle = 300 },
    },
};
bk_pwm_phase_shift_init(&sc);
bk_pwm_phase_shift_start();
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_PWM\_PERIOD\_DUTY：占空或周期配置非法
- BK\_ERR\_PWM\_PHASE\_SHIFT\_CHAN\_NUM：相移模式通道数不足
- BK\_ERR\_NO\_MEM：相移配置缓存分配失败
