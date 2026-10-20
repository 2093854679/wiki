---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/display/sw_rotate_user_guide/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 软件旋转

<a id="id2"></a>

## 1、功能概述

本文档主要介绍了软件旋转的功能以及API使用。软件旋转可以实现YUV旋转和RGB565旋转。

<a id="id3"></a>

## 2、参考代码

> 参考工程为 [DOORBELL工程](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects_work/media/doorbell/index.html)
>
> 硬件旋转的组件代码请参考 `components/multimedia/lcd/lcd_rotate.c` 和 `components/image_codec_unit/src/pipeline/yuv_rotate_pipeline.c`
>
> 软件旋转算法参考 [软件算法](../api-reference/multi_media/image_algorithm.md)

<a id="api"></a>

## 3、API使用说明

软件旋转的使用比较简单，主要调用一个接口既可以实现。
软件旋转主要是弥补硬件旋转不能实现的功能，比如将数据旋转为YUV，所以一般使用的接口为：

```
yuyv_rotate_degree90_to_yuyv(unsigned char *yuyv, unsigned char *rotatedyuyv, int width, int height)
yuyv_rotate_degree270_to_yuyv(unsigned char *yuyv, unsigned char *rotatedYuyv, int width, int height)
yuyv_rotate_degree180_to_yuyv(unsigned char *yuyv, unsigned char *rotatedYuyv, int width, int height)
```

## 模块导航

- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [API 参考](../api-reference.md)
- [支持外设](../support_peripherals.md)
- [摄像头](../camera.md)
- [DISPLAY](../display.md)
- [DMA2D用户手册](dma2d_user_guide/dma2d_user_guide.md)
- [LCD用户手册](lcd_user_guide.md)
- [HW Rotate用户手册](hw_rotate_user_guide.md)
- [HW Scale用户手册](hw_scale_user_guide.md)
- [PSRAM内存分配](../psram_config.md)
- [视频编解码](../video_codec.md)
- [图形用户界面](../gui.md)
- [参考工程](../projects.md)
- [低功耗](../power_save.md)
- [音频算法](../audio_algorithms.md)
- [FAQ](../FAQ.md)
