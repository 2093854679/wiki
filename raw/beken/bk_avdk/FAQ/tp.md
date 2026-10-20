---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/FAQ/tp/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tp"></a>

# TP常见问题

本节主要描述调试LCD触摸功能过程中常遇到的问题和解决方法。

> Q：触摸位置与实际位置存在镜像关系如何解决？
>
> A：打开触摸功能的第三个参数可根据具体的镜像关系传入不同的值，具体可参考tp\_mirror\_type\_t的枚举值。

---

> Q：相同厂家相同型号的屏幕，部分屏幕的触摸功能位置有偏差是什么情况？
>
> A：若确认不是屏幕损坏异常且不是存在镜像关系的位置偏差，可读取触摸芯片的版本寄存器，虽然是相同厂家相同型号的产品，但是不同批次的屏幕触摸芯片烧录的版本可能不一致没有及时更新导致。

---

> Q：在新建的lvgl工程实现具体的UI，发现触摸功能不灵敏或触摸一次却不断触发。
>
> A：可检查一下TP\_INT引脚的中断服务函数是否正常触发，可在tp\_driver.c文件中的tp\_int\_gpio\_isr()函数中添加log打印查看时间间隔或者拉gpio查看间隔时间，正常应该是20ms触发一次，若存在触发间隔有时超过20ms，在工程config/bk7258和config/bk7258\_cp1文件夹里添加usr\_gpio\_cfg.h用于重新定义gpio\_map表，具体可参考示例工程中的文件，并在两个文件夹里的config文件里打开以下两个宏：
>
> |  |  |
> | --- | --- |
> | marco | value |
> | CONFIG\_GPIO\_DEFAULT\_SET\_SUPPORT | Y |
> | CONFIG\_USR\_GPIO\_CFG\_EN | Y |

## 模块导航

- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [API 参考](../api-reference.md)
- [支持外设](../support_peripherals.md)
- [摄像头](../camera.md)
- [DISPLAY](../display.md)
- [PSRAM内存分配](../psram_config.md)
- [视频编解码](../video_codec.md)
- [图形用户界面](../gui.md)
- [参考工程](../projects.md)
- [低功耗](../power_save.md)
- [音频算法](../audio_algorithms.md)
- [FAQ](../FAQ.md)
- [dvp常见问题](dvp.md)
- [uvc常见问题](uvc.md)
- [qspi_lcd常见问题](qspi_lcd.md)
- [audio常见问题](audio.md)
- [lcd常见问题](lcd.md)
- [lvgl常见问题](lvgl.md)
