---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/camera/uvc_camera_introduction/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uvc-camera"></a>

# UVC Camera 详解

<a id="uvc"></a>

## 1 UVC简介

> UVC(USB Video Control)是属于USB行业规范中的USB设备类规范，用于USB接口的视频设备的一个统一的数据交换规范。在UVC规范中明确要求，其必须具备两种接口：
> VC Interface（视频控制类接口）和VS Interface（视频流接口）。VC接口负责UVC设备的配置，VS接口负责视频流数据的传输，两者相互配合完成UVC的设备功能。
> 当前硬件支持USB2.0，包括Full-speed和High-speed，USB2.0除了拥有USB1.1中规定的1.5Mbps和12Mbps两个传输模式外，还增加了480Mbps高速传输模式。
> USB1.1的单位数据传输时间是1毫秒，而USB2.0的单位数据传输时间是125微秒。UVC输出的数据格式是由其本身固件决定，可能支持的是H264、MJPEG、H265等。

<a id="id1"></a>

## 2 UVC目前支持的类型与规格

| USB规格 | UVC规格 | 传输方式 | 传输速度 | MaxPacketSize | 分辨率 | 帧率 | 输出格式 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| USB2.0 | UVC1.5/UVC1.1 | ISO/BULK | High(Full)-speed | 1024及以下 | 1280X720及以下 | 30及以下 | JPEG/H264/H265 |

<a id="id2"></a>

## 3 UVC的使用流程

- 1、 初始化USB硬件模块，即初始化host，并启动其工作的usb\_task；
- 2、host检测device是否有接入，并进行枚举；
- 3、上层检测到连接成功后，读取设备描述符，并据此配置UVC参数
- 4、启动UVC
- 5、对UVC数据包进行处理
- 6、暂停UVC传输
- 7、恢复UVC的传输等，做好状态机的切换

## 模块导航

- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [API 参考](../api-reference.md)
- [支持外设](../support_peripherals.md)
- [摄像头](../camera.md)
- [Camera 概述](camera_introduction.md)
- [DVP Camera 详解](dvp_camera_introduction.md)
- [DISPLAY](../display.md)
- [PSRAM内存分配](../psram_config.md)
- [视频编解码](../video_codec.md)
- [图形用户界面](../gui.md)
- [参考工程](../projects.md)
- [低功耗](../power_save.md)
- [音频算法](../audio_algorithms.md)
- [FAQ](../FAQ.md)
