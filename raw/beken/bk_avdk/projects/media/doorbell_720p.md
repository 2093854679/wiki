# Doorbell_720p[](#doorbell-720p "永久链接至标题")



## 1. 简介[](#id1 "永久链接至标题")

本工程是USB摄像头门锁的一个demo，支持端（BK7258设备）到端（手机APP端）的演示。默认使用PSRAM为16Mbyte，支持UVC输出1280X720到手机，并缩放显示到480X854的本地LCD屏幕上。


### 1.1 规格[](#id2 "永久链接至标题")

> 请参考 [规格](../doorbell/index.md#id2 "../doorbell/index.md#id2")


### 1.2 路径[](#id4 "永久链接至标题")

> <bk_avdk源代码路径>/projects/media/doorbell_720p


## 2. 框架图[](#id5 "永久链接至标题")

> 请参考 [框架图](../doorbell/index.md#id4 "../doorbell/index.md#id4")


## 3. 配置[](#id7 "永久链接至标题")

> 请参考 [配置](../doorbell/index.md#id7 "../doorbell/index.md#id7")


### 3.1 区别[](#id9 "永久链接至标题")

> doorbell_720p与doorbell的区别在于：
> :   - 前一个配置使用的UVC输出分辨率为1280X720，后一个使用的UVC输出分辨率为864X480。
>
> 因为多媒体模块运行在CPU1上，两个工程的宏配置区别如下：
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | project | marco | value | implication |
> | doorbell | CONFIG_BT_REUSE_MEDIA_MEMORY | Y | 多媒体和蓝牙共用一块sram（分时复用） |
> | doorbell_720p | CONFIG_BT_REUSE_MEDIA_MEMORY | Y | 多媒体和蓝牙共用一块sram（分时复用） |
> | doorbell | CONFIG_BT_REUSE_MEDIA_MEM_SIZE | 0x1B000 | 多媒体和蓝牙共用一块sramd的大小 |
> | doorbell_720p | CONFIG_BT_REUSE_MEDIA_MEM_SIZE | 0x2F000 | 多媒体和蓝牙共用一块sramd的大小 |
> | doorbell | CONFIG_SUPPORTED_IMAGE_MAX_720P | N | 不支持图像最大分辨率1280X720 |
> | doorbell_720p | CONFIG_SUPPORTED_IMAGE_MAX_720P | Y | 支持图像最大分辨率1280X720 |


## 4. 演示说明[](#id10 "永久链接至标题")

> 请访问
> [APP使用文档](https://docs.bekencorp.com/arminodoc/bk_app/app/zh_CN/v2.0.1/app_usage/app_usage_guide/index.html#debug "https://docs.bekencorp.com/arminodoc/bk_app/app/zh_CN/v2.0.1/app_usage/app_usage_guide/index.html#debug")
> 查看。
>
> 演示结果：运行时会启动UVC，LCD和AUDIO，LCD显示UVC输出JPEG（1280X720）图像经过解码和缩放旋转90°后显示到LCD(480X854)上，
> 解码后的YUV经过H264编码后，经WIFI图传到手机上显示（1280X720）。

提示

如果您没有云账号权限，可以使用debug模式，设置局域网TCP图传方式。


## 5. 代码讲解[](#id11 "永久链接至标题")

> 请参考 [代码讲解](../doorbell/index.md#id13 "../doorbell/index.md#id13")
