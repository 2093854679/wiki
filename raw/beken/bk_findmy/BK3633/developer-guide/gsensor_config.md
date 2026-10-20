---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_findmy/bk3633/zh_CN/v2.0.1/developer-guide/gsensor_config/index.html
sdk_family: bk_findmy
chip: BK3633
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 加速度传感器配置

<a id="id2"></a>

## 1、加速度传感器配置

> FindMy如果支持motion detector UT需要用到加速度传感器，则需要开启I2C功能（默认开启）。另外还需配置一个GPIO以接收外部加速度传感器的中断信号。该GPIO可以选配，可以通过更改GPIO\_INT1这个宏来实现(默认配置为0x12，对应GPIO9)。
>
> 目前外接的是LIS2DH12TR加速度传感器芯片，规格书详见:`/docs/hw/LIS2DH12TR_姿态传感器_陀螺仪规格书.PDF`

## 模块导航

- [快速入门](../get-started.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [出厂信息配置](factory_config.md)
- [配件信息配置](accessory_information.md)
- [蜂鸣器配置](sounder_config.md)
- [按键配置](key_config.md)
- [OTA](ota.md)
- [Apple UARP升级](apple_uarp.md)
- [Apple FindMy测试说明](apple_test_instruction.md)
- [Google FindMy测试说明](google_test_instruction.md)
- [Apple&Google FindMy测试说明](apple%26google_test_instruction.md)
- [硬件资料](hw.md)
- [软件常见问题](software_faq.md)
