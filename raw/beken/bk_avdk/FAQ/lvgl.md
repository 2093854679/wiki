---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/FAQ/lvgl/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lvgl"></a>

# lvgl常见问题

本节主要描述LVGL绘制UI功能常遇到的问题和解决方法。

> Q：屏幕能显示UI但是颜色不正常
>
> A：检查下工程中是否打开宏CONFIG\_LV\_COLOR\_16\_SWAP，该宏通常是用于解决QSPI/SPI LCD颜色异常的问题。

---

> Q：工程上电执行立马出现死机问题
>
> A：可先用add2line命令定位死机的位置，若死机在lvgl源码内部通常是申请不到内存或者内存被踩导致，具体可将log dump全进行现场还原分析。此外，lvgl的线程是不安全的，若在其他task中绘制UI，需要使用 `lv_vendor_disp_lock()` 和 `lv_vendor_disp_unlock()` 的接口进行代码保护。

---

> Q：工程上电后log正常但是屏幕黑屏无显示
>
> A：检查代码中使用的LCD类型和分辨率是否和实际LCD型号一致，且查看config文件中是否将选用的LCD宏打开，若log中lvgl的数值不为0则表示lvgl工作正常，需要重点排除LCD的问题。

---

> Q：使用JPEG硬件解码提前解码到psram然后使用LVGL显示该图片显示异常。
>
> A：硬件解码模块使用有限制，JEPG图像必须是YUV422图片，且图像的行数必须是32的倍数，列数必须是8的倍数。

---

> Q：如何提高LVGL的帧率？
>
> A：draw\_buffer使用sram内存并使用双draw\_buffer，同时打开 `CONFIG_CACHE_ENABLE` 以及 `CONFIG_LV_ATTRIBUTE_FAST_MEM` 。

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
- [qspi_lcd常见问题](qspi_lcd.md)
- [audio常见问题](audio.md)
- [lcd常见问题](lcd.md)
