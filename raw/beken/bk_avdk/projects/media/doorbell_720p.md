---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/media/doorbell_720p/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="doorbell-720p"></a>

# Doorbell\_720p

<a id="id1"></a>

## 1\. 简介

本工程是USB摄像头门锁的一个demo，支持端（BK7258设备）到端（手机APP端）的演示。默认使用PSRAM为16Mbyte，支持UVC输出1280X720到手机，并缩放显示到480X854的本地LCD屏幕上。

<a id="id2"></a>

### 1.1 规格

> 请参考 [规格](doorbell.md#id2)

<a id="id4"></a>

### 1.2 路径

> \<bk\_avdk源代码路径\>/projects/media/doorbell\_720p

<a id="id5"></a>

## 2\. 框架图

> 请参考 [框架图](doorbell.md#id4)

<a id="id7"></a>

## 3\. 配置

> 请参考 [配置](doorbell.md#id7)

<a id="id9"></a>

### 3.1 区别

> doorbell\_720p与doorbell的区别在于：
> :   - 前一个配置使用的UVC输出分辨率为1280X720，后一个使用的UVC输出分辨率为864X480。
>
> 因为多媒体模块运行在CPU1上，两个工程的宏配置区别如下：
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | project | marco | value | implication |
> | doorbell | CONFIG\_BT\_REUSE\_MEDIA\_MEMORY | Y | 多媒体和蓝牙共用一块sram（分时复用） |
> | doorbell\_720p | CONFIG\_BT\_REUSE\_MEDIA\_MEMORY | Y | 多媒体和蓝牙共用一块sram（分时复用） |
> | doorbell | CONFIG\_BT\_REUSE\_MEDIA\_MEM\_SIZE | 0x1B000 | 多媒体和蓝牙共用一块sramd的大小 |
> | doorbell\_720p | CONFIG\_BT\_REUSE\_MEDIA\_MEM\_SIZE | 0x2F000 | 多媒体和蓝牙共用一块sramd的大小 |
> | doorbell | CONFIG\_SUPPORTED\_IMAGE\_MAX\_720P | N | 不支持图像最大分辨率1280X720 |
> | doorbell\_720p | CONFIG\_SUPPORTED\_IMAGE\_MAX\_720P | Y | 支持图像最大分辨率1280X720 |

<a id="id10"></a>

## 4\. 演示说明

> 请访问
> [APP使用文档](../../../bk_toolkit/iotapp/app_usage/app_usage_guide.md#debug)
> 查看。
>
> 演示结果：运行时会启动UVC，LCD和AUDIO，LCD显示UVC输出JPEG（1280X720）图像经过解码和缩放旋转90°后显示到LCD(480X854)上，
> 解码后的YUV经过H264编码后，经WIFI图传到手机上显示（1280X720）。

提示

如果您没有云账号权限，可以使用debug模式，设置局域网TCP图传方式。

<a id="id11"></a>

## 5\. 代码讲解

> 请参考 [代码讲解](doorbell.md#id13)
