# UVC[](#uvc "永久链接至标题")



## 1. 简介[](#id1 "永久链接至标题")

本工程是UVC默认调试工程，可以用来测试插入的UVC工作是否正常，默认使用16M PSRAM。


### 1.1 规格[](#id2 "永久链接至标题")

> 请参考 [规格](../../media/doorbell/index.md#id2 "../../media/doorbell/index.md#id2")


### 1.2 路径[](#id4 "永久链接至标题")

> <bk_avdk源代码路径>/projects/peripheral/uvc


## 2. 框架图[](#id5 "永久链接至标题")

> 请参考 [框架图](../../media/doorviewer/index.md#id4 "../../media/doorviewer/index.md#id4")


## 3. 配置[](#id7 "永久链接至标题")


### 3.1 蓝牙与多媒体内存复用[](#id8 "永久链接至标题")

> 使用此工程，只是单纯验证uvc，故内存不需要与蓝牙共用。
>
> |  |  |  |
> | --- | --- | --- |
> | marco | value | implication |
> | CONFIG_BT_REUSE_MEDIA_MEMORY | N | 多媒体和蓝牙共用一块sram（分时复用） |


#### 3.1.1 卸载蓝牙[](#id9 "永久链接至标题")


```
#ifdef CONFIG_BT_REUSE_MEDIA_MEMORY
#if CONFIG_BLUETOOTH
    bk_bluetooth_deinit();
#endif
#endif

```


#### 3.1.2 初始化蓝牙[](#id10 "永久链接至标题")


```
bk_bluetooth_init();

```


### 3.2 区别[](#id11 "永久链接至标题")

> uvc与doorbell的区别在于：
> :   - uvc默认上电启动外设uvc，并通过软件解码器，分析输出的JPEG图像原始数据格式YUV422/YUV420，和输出分辨率。其他外设不参与，不支持图传，LCD显示，语音传输等。
>     - doorbell是一个完整的门锁方案。


## 4. 演示说明[](#id12 "永久链接至标题")

> 默认上电自启动，不需要额外操作，会打印如下log。


```
(4736):##MJPEG: frame_id:113, length:56922, frame_addr:0x6020fba0
video_co:I(4736):4:2:2, YUV:
(4736):##DECODE:pixel_x:864, pixel_y:480
(4736):rotate_angle:0(0:0 1:90 2:180 3:270)
(4736):byte_order:0(0:little endian 1:big endian)
(4736):out_fmt:YUYV

```


## 5. 代码讲解[](#id13 "永久链接至标题")

> 请参考 [代码讲解](../../media/doorbell/index.md#id13 "../../media/doorbell/index.md#id13")
