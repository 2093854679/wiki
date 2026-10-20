---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/adc.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="adc"></a>

# ADC 驱动

<a id="id1"></a>

## 概述

ADC（Analog-to-Digital Converter）模数转换器是将模拟信号转换为数字信号的关键外设。BK7239N 内置高精度 ADC，支持多通道采样，广泛应用于传感器数据采集、电压监测等场景。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 ADC 通道同时工作
- **高精度转换**：提供高精度的模数转换能力
- **多种采样模式**：支持单次采样、连续采样等模式
- **中断支持**：支持转换完成中断，提高系统响应效率
- **时钟配置**：支持多种时钟源和采样率配置
- **滤波器**：内置数字滤波器，提高转换精度
- **校准功能**：支持 ADC 校准，提高转换精度
- **低功耗**：支持低功耗模式，节省功耗

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_adc\_driver\_init() 初始化 ADC 驱动
   \- 调用 bk\_adc\_init() 初始化具体 ADC 通道
   \- 配置采样参数（采样率、滤波器等）
   \- 根据需要注册中断回调
2. **基本使用**
   \- 使用 bk\_adc\_single\_read() 进行单次采样
   \- 使用 bk\_adc\_read\_raw() 读取原始数据
   \- 使用 bk\_adc\_read\_average() 读取平均值
   \- 使用 bk\_adc\_data\_calculate() 计算实际电压值
3. **中断处理**
   \- 注册转换完成中断回调
   \- 在中断中处理转换结果
   \- 根据需要启用/禁用中断
4. **校准使用**
   \- 调用 bk\_adc\_bypass\_calibration() 绕过校准
   \- 使用 bk\_adc\_data\_calculate() 进行数据换算

<a id="id4"></a>

## 注意事项

- 确保在调用其他 ADC API 前先调用 bk\_adc\_driver\_init()
- ADC 通道需要与硬件连接正确
- 采样率设置需要根据信号特性选择
- 使用中断模式时注意中断优先级设置
- 低功耗模式下 ADC 可能被关闭，需要重新初始化
- 注意 ADC 参考电压和输入范围

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_adc\_driver\_init() \- 初始化 ADC 驱动
- bk\_adc\_driver\_deinit() \- 反初始化 ADC 驱动
- bk\_adc\_init() \- 初始化 ADC 通道
- bk\_adc\_deinit() \- 反初始化 ADC 通道
- bk\_adc\_acquire() \- 锁定 ADC 通道
- bk\_adc\_release() \- 释放 ADC 通道
- bk\_adc\_single\_read() \- 单次采样
- bk\_adc\_read\_raw() \- 读取原始数据
- bk\_adc\_read\_average() \- 读取平均值
- bk\_adc\_start() \- 开始转换
- bk\_adc\_stop() \- 停止转换
- bk\_adc\_register\_isr() \- 注册中断服务函数
- bk\_adc\_set\_clock() \- 设置时钟
- bk\_adc\_set\_sample\_rate() \- 设置采样率
- bk\_adc\_set\_filter() \- 设置滤波器
- bk\_adc\_set\_steady\_time() \- 设置稳定时间
- bk\_adc\_set\_sample\_count() \- 设置采样次数
- bk\_adc\_set\_saturate\_mode() \- 设置饱和模式
- bk\_adc\_bypass\_calibration() \- 绕过校准
- bk\_adc\_config() \- 配置 ADC
- bk\_adc\_set\_mode() \- 设置模式
- bk\_adc\_data\_calculate() \- 数据换算

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/adc.h>

void adc_example(void)
{
    // 初始化 ADC 驱动
    bk_adc_driver_init();

    // 初始化 ADC 通道
    bk_adc_init(ADC_CHAN_0, 64);

    // 单次采样
    uint16_t value;
    bk_adc_single_read(&value);

    // 计算实际电压值
    float voltage = bk_adc_data_calculate(value, ADC_CHAN_0);
    printf("ADC Value: %d, Voltage: %.2fV\n", value, voltage);
}
```

连续采样示例：

```
void adc_continuous_example(void)
{
    uint16_t buffer[64];

    // 设置连续采样模式
    bk_adc_set_mode(ADC_CONTINUOUS_MODE);

    // 开始转换
    bk_adc_start();

    // 读取数据
    int len = bk_adc_read_raw(buffer, 64, 1000);
    if (len > 0) {
        // 处理采样数据
        for (int i = 0; i < len; i++) {
            float voltage = bk_adc_data_calculate(buffer[i], ADC_CHAN_0);
            printf("Sample %d: %d -> %.2fV\n", i, buffer[i], voltage);
        }
    }

    // 停止转换
    bk_adc_stop();
}
```

中断采样示例：

```
static void adc_isr_callback(adc_chan_t chan, void *param)
{
    uint16_t value;
    if (bk_adc_single_read(&value) == BK_OK) {
        float voltage = bk_adc_data_calculate(value, chan);
        printf("ADC Interrupt: %d -> %.2fV\n", value, voltage);
    }
}

void adc_interrupt_example(void)
{
    // 注册中断回调
    bk_adc_register_isr(ADC_CHAN_0, adc_isr_callback, NULL);

    // 设置中断模式
    bk_adc_set_mode(ADC_INTERRUPT_MODE);

    // 开始转换
    bk_adc_start();
}
```

<a id="id6"></a>

## 常见问题

- **转换精度不够**：检查参考电压、采样率设置，考虑使用校准功能
- **采样值不稳定**：检查信号源稳定性、滤波器设置、稳定时间配置
- **中断未触发**：确认中断注册和启用，检查中断优先级设置
- **数据换算错误**：确认 ADC 参考电压和输入范围设置正确

<a id="id7"></a>

## 实战示例

1. 单次转换读取并换算为电压

```
uint16_t raw = 0;
bk_adc_init(ADC_CHAN_X);
bk_adc_set_mode(ADC_SINGLE_MODE);
bk_adc_single_read(&raw);
float mv = bk_adc_data_calculate(raw, ADC_CHAN_X);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_ADC\_NOT\_INIT：未调用 bk\_adc\_driver\_init() 或通道未 bk\_adc\_init()
- BK\_ERR\_ADC\_INVALID\_MODE：不支持的 ADC 模式
- BK\_ERR\_ADC\_SIZE\_TOO\_BIG：读取长度超过内部缓冲限制
