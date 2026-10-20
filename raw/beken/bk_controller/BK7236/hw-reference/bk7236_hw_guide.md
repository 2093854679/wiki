---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7236/zh_CN/v2.0.1/hw-reference/bk7236_hw_guide.html
sdk_family: bk_controller
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7236"></a>

# BK7236 硬件设计指南

<a id="id1"></a>

## **BK7236 技术规格书**

[BK7236 技术规格书](../../../_assets/faf9fc9a51a6535b32cc-BK7236-Datasheet.pdf)

<a id="id3"></a>

## **硬件设计注意事项**

<a id="sdio"></a>

### SDIO上拉电阻配置

BK7236 SDIO需要使用上拉电阻以增强驱动能力，请在SDIO CMD/D0/D1/D2/D3几个管脚上贴推荐的上拉电阻。
不同客户可能根据具体主控平台I/O的驱动电流（6mA/8mA/10mA/12mA）和SDIO使用的电压（3.3v/1.8v）情况进行动态适配。
推荐阻值可以参考以下表格：

<a id="id4"></a>
![Voltage-current matching relationship with resistance](../../../_assets/ce8f57dddf1e267dc4a4-current.png)


Figure 1\. Voltage-current matching relationship with resistance

重要

*为了确保SDIO通信正常，务必根据上述建议配置合适的上拉电阻*

实际阻值需要万用表量取确认，方法如下：
电阻档分别量取VDDIO与各SDIO\_DATA之间的阻值。

<a id="id5"></a>
![SDIO GPIO](../../../_assets/1cd19aa2a2cf9e2984ad-sdio_gpio.png)


Figure 2\. SDIO GPIO \& VDDIO

备注

*上拉电阻可以放在主控侧，也可以放在BK7236模组侧。但低功耗场景主控通常掉电，为了确保整个系统不通过上拉电阻漏电，推荐将上拉电阻放在主控侧*

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [硬件设计指南](../hw-reference.md)
- [软件方案介绍](../sw-detail.md)
- [主控开发适配指南](../host-guide.md)
- [Controller开发指南](../controller-guide.md)
- [常见问题解答](../frequently-asked-questions.md)
