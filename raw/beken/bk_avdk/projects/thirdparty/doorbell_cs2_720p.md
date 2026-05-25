# Doorbell_cs2_720p[](#doorbell-cs2-720p "永久链接至标题")



## 1. 简介[](#id1 "永久链接至标题")

本工程是USB摄像头门锁的一个demo，支持端（BK7258设备）到端（手机APP端）的演示。默认支持尚云传输1280X720分辨率码流。


### 1.1 规格[](#id2 "永久链接至标题")

> 请参考 [规格](../../media/doorbell/index.md#id2 "../../media/doorbell/index.md#id2")


### 1.2 路径[](#id4 "永久链接至标题")

> <bk_avdk源代码路径>/projects/thirdparty/doorbell_cs2_720p


## 2. 框架图[](#id5 "永久链接至标题")

> 请参考 [框架图](../../media/doorbell/index.md#id4 "../../media/doorbell/index.md#id4")


## 3. 配置[](#id7 "永久链接至标题")

> 请参考 [配置](../../media/doorbell/index.md#id7 "../../media/doorbell/index.md#id7")


### 3.1 区别[](#id9 "永久链接至标题")

> doorbell_CS2_720p与doorbell_720p的区别在于，请一个不仅支持UDP、TCP图传，还支持CS2尚云图传，后一个只支持UDP/TCP。
>
> 支持尚云的宏在CPU0上配置，两个工程的宏配置区别如下：
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | project | marco | value | implication |
> | doorbell_720p | CONFIG_INTEGRATION_DOORBELL_CS2 | N | 不启用CS2云传输 |
> | doorbell_CS2_720p | CONFIG_INTEGRATION_DOORBELL_CS2 | Y | 启用CS2云传输 |


## 4. 演示说明[](#id10 "永久链接至标题")

> 请访问
> [APP使用文档](https://docs.bekencorp.com/arminodoc/bk_app/app/zh_CN/v2.0.1/app_usage/app_usage_guide/index.html#debug "https://docs.bekencorp.com/arminodoc/bk_app/app/zh_CN/v2.0.1/app_usage/app_usage_guide/index.html#debug")
> 查看。
>
> 演示结果：运行时会启动UVC，LCD和AUDIO，LCD显示UVC输出JPEG（1281X720）图像经过解码和旋转90°后显示到LCD(480X854)上，
> 解码后的YUV经过H264编码后，经CS2云到手机上显示(1280X720)。

提示

如果您没有云账号权限，可以使用debug模式，设置局域网TCP图传方式。


## 5. 代码讲解[](#id11 "永久链接至标题")

> 请参考 [代码讲解](../../media/doorbell/index.md#id13 "../../media/doorbell/index.md#id13")
