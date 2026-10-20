---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/FAQ/qspi_lcd/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="qspi-lcd"></a>

# QSPI\_LCD常见问题

本节主要描述调试QSPI\_LCD显示功能过程中常遇到的问题和解决方法。

> Q：上电执行后屏幕黑屏无显示如何排查？
>
> A：首先检查背光是否点亮，若不亮可先检查背光引脚是否一致，若背光亮检查QSPI的引脚是否与我们板子使用GPIO一致，并检查工程中是否打开所使用屏幕的CONFIG宏，若检查一切正常可用逻辑分析仪抓信号检查是否有信号出现以及初始化信号数据是否与发送的cmd一致；

---

> Q：QSPI屏可使用的最大时钟是多少？
>
> A：QSPI支持的最大稳定时钟为96M，可满足QSPI屏的显示需求。

---

> Q：按行刷数据的屏幕显示异常如何排查？
>
> A：请严格按照屏幕的spec刷屏时序图进行对比检查，尤其是一些时间的要求。

---

> Q：按行刷数据的屏幕显示一段时间后黑屏，过段时间后又能恢复是什么情况？
>
> A：E4寄存器设置的值表示帧与帧间隔最大的安全时间，若帧与帧间隔时间超过该时间会导致黑屏，需要缩减帧与帧之间的间隔，E4值具体如何设置需咨询屏厂支持。

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
- [tp常见问题](tp.md)
- [audio常见问题](audio.md)
- [lcd常见问题](lcd.md)
- [lvgl常见问题](lvgl.md)
