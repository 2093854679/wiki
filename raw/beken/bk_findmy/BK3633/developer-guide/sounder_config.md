---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_findmy/bk3633/zh_CN/v2.0.1/developer-guide/sounder_config/index.html
sdk_family: bk_findmy
chip: BK3633
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 蜂鸣器配置

<a id="id2"></a>

## 1、蜂鸣器配置

> FindMy如果支持play sound需要外接蜂鸣器。目前外接的是SD116蜂鸣器芯片，规格书详见:`/docs/hw/SD116_V1.5.pdf`，需要配置两路GPIO控制信号和一路PWM。
> :   - GPIO控制信号通过GPIO\_EN1和GPIO\_EN2这两个宏来配置(默认配置为0x05和0x04，对应GPIO5和GPIO4),控制音量大小
>     - PWM使用的GPIO通过GPIO\_PWM这个宏来配置(默认配置为0x14，对应GPIO12)

## 模块导航

- [快速入门](../get-started.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [出厂信息配置](factory_config.md)
- [配件信息配置](accessory_information.md)
- [加速度传感器配置](gsensor_config.md)
- [按键配置](key_config.md)
- [OTA](ota.md)
- [Apple UARP升级](apple_uarp.md)
- [Apple FindMy测试说明](apple_test_instruction.md)
- [Google FindMy测试说明](google_test_instruction.md)
- [Apple&Google FindMy测试说明](apple%26google_test_instruction.md)
- [硬件资料](hw.md)
- [软件常见问题](software_faq.md)
