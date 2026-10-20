---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/peripheral/uvc/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uvc"></a>

# UVC

<a id="id1"></a>

## 1\. 简介

本工程是UVC默认调试工程，可以用来测试插入的UVC工作是否正常，默认使用16M PSRAM。

<a id="id2"></a>

### 1.1 规格

> 请参考 [规格](../media/doorbell.md#id2)

<a id="id4"></a>

### 1.2 路径

> \<bk\_avdk源代码路径\>/projects/peripheral/uvc

<a id="id5"></a>

## 2\. 框架图

> 请参考 [框架图](../media/doorviewer.md#id4)

<a id="id7"></a>

## 3\. 配置

<a id="id8"></a>

### 3.1 蓝牙与多媒体内存复用

> 使用此工程，只是单纯验证uvc，故内存不需要与蓝牙共用。
>
> |  |  |  |
> | --- | --- | --- |
> | marco | value | implication |
> | CONFIG\_BT\_REUSE\_MEDIA\_MEMORY | N | 多媒体和蓝牙共用一块sram（分时复用） |

<a id="id9"></a>

#### 3.1.1 卸载蓝牙

```
#ifdef CONFIG_BT_REUSE_MEDIA_MEMORY
#if CONFIG_BLUETOOTH
    bk_bluetooth_deinit();
#endif
#endif
```

<a id="id10"></a>

#### 3.1.2 初始化蓝牙

```
bk_bluetooth_init();
```

<a id="id11"></a>

### 3.2 区别

> uvc与doorbell的区别在于：
> :   - uvc默认上电启动外设uvc，并通过软件解码器，分析输出的JPEG图像原始数据格式YUV422/YUV420，和输出分辨率。其他外设不参与，不支持图传，LCD显示，语音传输等。
>     - doorbell是一个完整的门锁方案。

<a id="id12"></a>

## 4\. 演示说明

> 默认上电自启动，不需要额外操作，会打印如下log。

```
(4736):##MJPEG: frame_id:113, length:56922, frame_addr:0x6020fba0
video_co:I(4736):4:2:2, YUV:
(4736):##DECODE:pixel_x:864, pixel_y:480
(4736):rotate_angle:0(0:0 1:90 2:180 3:270)
(4736):byte_order:0(0:little endian 1:big endian)
(4736):out_fmt:YUYV
```

<a id="id13"></a>

## 5\. 代码讲解

> 请参考 [代码讲解](../media/doorbell.md#id13)
