---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/video_codec/h264_encoding_hw/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="h264"></a>

# H264硬编码

<a id="id1"></a>

## 1、功能概述

> H264编码主要用于将YUV422的数据通过硬件编码，输出H264图像数据，并且压缩图像数据量

<a id="id2"></a>

## 2、开发资料

> 当前avdk提供了详细的sdk接口，参考文件路径：`.\bk_idk\middleware\driver\h264`
>
> 为了方便客户使用，重新封装了编码功能，当前只需要开关摄像头，然后针对图像质量，也提供一个api接口去调节，参考文件：`.\components\multimedia\app\media_app.c`

<a id="id3"></a>

## 3、接口说明

> 基于h264图像质量的调试说明：media\_app\_set\_compression\_ratio:
>
> 结构体参数说明：`compress_ratio_t`
>
> - yuv\_mode\_t mode: 当前需要调节的模式，仅支持JPEG和H264，此处应该选择H264
> - h264\_qp\_t h264\_qp： h264编码QP的调整，仅支持H264
> - uint8\_t enable: 启动压缩率调节，1/0：启动/关闭
> - uint16\_t jpeg\_up： 数据JPEG图像大小的上限值，单位byte，仅在JPEG模式下有效
> - uint16\_t jpeg\_low: 数据JPEG图像大小的下限值，单位byte，仅在JPEG模式下有效
> - uint16\_t imb\_bits： H264编码输出I帧宏块的大小，单位byte，仅在H264模式下有效，值越大，压缩率越小，图像质量越高，编码输出图像越大，范围\[1, 4095\]
> - uint16\_t pmb\_bits： H264编码输出P帧宏块的大小，单位byte，仅在H264模式下有效，值越大，压缩率越小，图像质量越高，编码输出图像越大，范围\[1, 4095\]
>
> 结构体参数说明：`h264_qp_t`
>
> - uint8\_t init\_qp; H264编码时初始化QP，范围\[0, 51\];
> - uint8\_t i\_min\_qp; I帧编码的QP最小值，范围\[0, 51\];
> - uint8\_t i\_max\_qp; I帧编码的QP最大值，范围\[0, 51\];
> - uint8\_t p\_min\_qp; P帧编码的QP最小值，范围\[0, 51\];
> - uint8\_t p\_max\_qp; P帧编码的QP最大值，范围\[0, 51\];

备注

上面的值除了需要注意在有效范围内之外，还需要注意，I/P帧编码的最大值一定要大于其最小值，方可生效。通过上面的接口可以调节图像质量，需要注意提高图像质量无疑会加大数据量，当前一帧yuv422数据编码完成的输出最大空间为64KB，如果调节图像质量，
编码输出的H264图像大于64K，会出现不稳定的问题。

<a id="id4"></a>

## 4、编码挡位调节

> 默认SDK提供了h264编码挡位调节的配置，通过配置宏来定义：`CONFIG_H264_QUALITY_LEVEL`，具体说明如下：
>
> - 取值范围：\[0, 3\]，定义三个挡位，定义的值分别为：1/2/3，分别对应h264压缩图像质量由低到高，图像越清晰。
> - 如果CONFIG\_H264\_QUALITY\_LEVEL\=0，不使用三个挡位的参数，而使用默认的值进行配置，默认值参考路径：`.\bk_idk\middleware\soc\bk7258\hal\h264_default_config.h`，可以通过修改默认值来达到预期效果。
> - 默认SDK的挡位定义在中间挡位，CONFIG\_H264\_QUALITY\_LEVEL\=2。用户可以在工程中的配置中将宏改为需要的值。
> - 随着值的增大，图像质量变高更清晰，码率变得更大。

<a id="p"></a>

## 5、P帧个数的调节

> 默认情况下，SDK配置的H264编码一个帧组（GOP）的P帧个数为5，可以通过宏CONFIG\_H264\_P\_FRAME\_CNT进行调节，其有效范围是\[0, 1023\]。
> 增加P帧的个数可以降低编码输出的整体码率。

<a id="id5"></a>

## 6、调整图像质量的一些建议

> SDK提供了三种H264图像质量的预设，通过宏CONFIG\_H264\_QUALITY\_LEVEL进行控制。调节图像质量主要涉及compress\_ratio\_t结构体中的参数。
>
> 调试步骤：
>
> 1、调整P帧个数：根据图像内容变化情况，增加P帧个数以降低码率。
>
> 2、调整frame\_buffer大小：默认为64K，根据需要调整以防止I帧过大导致不出图。建议将CONFIG\_H264\_FRAME\_SIZE的值调到102400(100K)。
>
> 3、配置H264图像质量等级：使用CONFIG\_H264\_QUALITY\_LEVEL\=0使用SDK原始编码参数。
>
> 4、实时调节压缩率：同步观察图像质量和码率，采用控制变量的方法一次只修改一个参数。
>
> 5、获取/配置编码参数：使用命令行工具获取编码参数，获取：media h264 get\_config，配置：media compress h264 init\_qp iframe\_max\_qp pframe\_max\_qp num\_ibits num\_pbits
>
> 6、调整初始量化参数（init\_qp）：从1开始，每次增加5，最大值不超过51，直到图像画面没有明显的宏块跳动。
>
> 7、调整I帧编码参数（num\_ibits）：增大此值，每次增加20，直到图像质量满意，但注意不要过高以避免码率增加，建议最大值不超过200。
>
> 8、调整P帧编码参数（num\_pbits）：与I帧调整类似，增大此值，每次增加20，但注意不要过高以避免码率增加，建议最大值不超过150。
>
> 9、循环步骤7-8：继续调整直到找到最佳参数。
>
> 10、调整I帧和P帧的最大量化参数（iframe\_max\_qp和pframe\_max\_qp）：减小这些值可以提高图像质量，也会增大码率，建议最低不应低于32。
>
> 11、调整frame\_buffer大小：达到最终效果后，如果I帧长度不超过64K，可将其还原为默认值CONFIG\_H264\_FRAME\_SIZE\=65536(64K)。
>
> 通过这些步骤，您可以优化H264编码过程中的P帧个数和图像质量，以满足特定的应用需求。
