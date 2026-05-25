# benchmark性能跑分工程[](#benchmark "永久链接至标题")



## 1. 简介[](#id1 "永久链接至标题")

本工程是基于lvgl实现官方提供的benchmark性能跑分测试。


### 1.1 规格[](#id2 "永久链接至标题")

> - 硬件配置：
>   :   - 核心板，**BK7258_QFN88_9X9_V3.2**
>       - 屏幕转接板，**BEKEN_LCD_V3**
>       - PSRAM 8M/16M
>       - 屏幕，**ST7701S**，480 * 480 RGB LCD


### 1.2 路径[](#id3 "永久链接至标题")

> 工程路径: `<bk_avdk源代码路径>/project/lvgl/benchmark`


## 2. 框架图[](#id4 "永久链接至标题")


### 2.1 软件模块架构图[](#id5 "永久链接至标题")

软件模块架构图见 [图形用户界面](../../../gui/lvgl/index.md "../../../gui/lvgl/index.md") 中的lvgl framework图。


### 2.2 代码模块关系图[](#id7 "永久链接至标题")

LVGL的接口都定义在 **lv_vendor.h** 和 **lvgl.h** 中。


## 3. 演示说明[](#id8 "永久链接至标题")

> 烧录上电后lvgl ui会自动启动运行，LCD上会显示benchmark的每个测试case UI，并在最后生成总的得分页面。
