---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/thirdparty/doorbell_cs2_720p/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="doorbell-cs2-720p"></a>

# Doorbell\_cs2\_720p

<a id="id1"></a>

## 1\. 简介

本工程是USB摄像头门锁的一个demo，支持端（BK7258设备）到端（手机APP端）的演示。默认支持尚云传输1280X720分辨率码流。

<a id="id2"></a>

### 1.1 规格

> 请参考 [规格](../media/doorbell.md#id2)

<a id="id4"></a>

### 1.2 路径

> \<bk\_avdk源代码路径\>/projects/thirdparty/doorbell\_cs2\_720p

<a id="id5"></a>

## 2\. 框架图

> 请参考 [框架图](../media/doorbell.md#id4)

<a id="id7"></a>

## 3\. 配置

> 请参考 [配置](../media/doorbell.md#id7)

<a id="id9"></a>

### 3.1 区别

> doorbell\_CS2\_720p与doorbell\_720p的区别在于，请一个不仅支持UDP、TCP图传，还支持CS2尚云图传，后一个只支持UDP/TCP。
>
> 支持尚云的宏在CPU0上配置，两个工程的宏配置区别如下：
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | project | marco | value | implication |
> | doorbell\_720p | CONFIG\_INTEGRATION\_DOORBELL\_CS2 | N | 不启用CS2云传输 |
> | doorbell\_CS2\_720p | CONFIG\_INTEGRATION\_DOORBELL\_CS2 | Y | 启用CS2云传输 |

<a id="id10"></a>

## 4\. 演示说明

> 请访问
> [APP使用文档](../../../bk_toolkit/iotapp/app_usage/app_usage_guide.md#debug)
> 查看。
>
> 演示结果：运行时会启动UVC，LCD和AUDIO，LCD显示UVC输出JPEG（1281X720）图像经过解码和旋转90°后显示到LCD(480X854)上，
> 解码后的YUV经过H264编码后，经CS2云到手机上显示(1280X720)。

提示

如果您没有云账号权限，可以使用debug模式，设置局域网TCP图传方式。

<a id="id11"></a>

## 5\. 代码讲解

> 请参考 [代码讲解](../media/doorbell.md#id13)
