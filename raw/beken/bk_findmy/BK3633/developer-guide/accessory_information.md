---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_findmy/bk3633/zh_CN/v2.0.1/developer-guide/accessory_information/index.html
sdk_family: bk_findmy
chip: BK3633
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 配件信息配置

<a id="id2"></a>

## 1、苹果配件信息

> > 以下配件信息必须跟Product Plan保持一致：
>
> - ManufacturerName （修改FMNA\_MANUFACTURER\_NAME这个宏）
> - ModelName （修改FMNA\_MODEL\_NAME这个宏）
> - AccessoryCategory （修改ACCESSORY\_CATEGORY这个宏）
> - AccessoryCapabilities （在app\_fmna\_get\_accessory\_capability接口中配置相应support bit）

<a id="id3"></a>

## 2、安卓配件信息

> 编译前请替换google账号注册的Model ID和spoofingy private key, 否则可能无法使用。
>
> 文件路径：projects/google\_findmy/config/user\_config.h
>
> CONFIG\_USE\_STORAGE\_FLASH\_VALUE为1， Model ID和spoofingy private key通过出厂信息配置，从flash读取。
>
> CONFIG\_USE\_STORAGE\_FLASH\_VALUE为0， Model ID和spoofingy private key使用以下宏配置的默认值：
>
> - CONFIG\_GOOGLE\_MODLE\_ID
> - CONFIG\_GOOGLE\_ANTI\_SPOOFINGY\_PRIVATE\_KEY

## 模块导航

- [快速入门](../get-started.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [出厂信息配置](factory_config.md)
- [加速度传感器配置](gsensor_config.md)
- [蜂鸣器配置](sounder_config.md)
- [按键配置](key_config.md)
- [OTA](ota.md)
- [Apple UARP升级](apple_uarp.md)
- [Apple FindMy测试说明](apple_test_instruction.md)
- [Google FindMy测试说明](google_test_instruction.md)
- [Apple&Google FindMy测试说明](apple%26google_test_instruction.md)
- [硬件资料](hw.md)
- [软件常见问题](software_faq.md)
