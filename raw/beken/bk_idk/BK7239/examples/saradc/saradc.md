---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/examples/saradc/saradc.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="saradc-cli"></a>

# SARADC Cli

<a id="id1"></a>

## 1、功能概述

> 为了方便验证SARADC功能，SDK提供了SARADC CMD示例。SARADC CMD命令以 `adc_test` 开头，后接具体命令和参数。执行命令，返回SARADC的采样值。

<a id="id2"></a>

## 2、代码路径

> 路径: `middleware\driver\saradc\adc_test.c`

<a id="saradc"></a>

## 3、saradc命令简介

支持的命令如下:

> 1.adc\_test
> :   - 功能说明
>       :   用来设置SARADC，获取采样值
>     - 命令格式
>       :   adc\_test param1 adc\_example
>
>           |  |  |
>           | --- | --- |
>           | param1 | adc channel |
>     - 测试用例
>       :   设置SARADC channel 3参数：`adc_test 3 adc_example`

<a id="api"></a>

## ４、API参考

> 网页API参考中外设里包含对saradc的API进行介绍:<https://docs.bekencorp.com/armino/bk7256/zh_CN/latest/api-reference/peripheral/bk_adc.html>

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [安全](../../security.md)
- [OS 相关参考](../../os.md)
- [购买 BK7239 开发板](../../boards.md)
- [样例 CLI 演示](../../examples.md)
- [命令](../cli.md)
- [外设](../peripheral.md)
- [平台](../platform.md)
- [VND_CAL](../vnd_cal/vnd_cal.md)
- [开发与贡献代码流程](../../process.md)
