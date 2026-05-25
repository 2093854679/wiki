# 小智AI自定义开发板指南

> **Source:** [custom-board.md](../../../raw/智能桌面萌宠项目笔记/custom-board.md)
> **TLDR:** 为小智AI创建自定义开发板的完整步骤——目录结构（xxx_board.cc/config.h/config.json）、板级初始化（I2C/SPI/Display/Audio/Buttons）、Kconfig 和 CMakeLists 集成、编译打包。

## Key Points

- **目录结构**：`boards/[品牌名]-[开发板类型]/` 含 xxx_board.cc、config.h、config.json、README.md
- **config.h**：定义音频(I2S+Codec)、显示(SPI+分辨率)、按钮 GPIO 等硬件管脚映射
- **config.json**：指定目标芯片(`target`)、Flash 大小、分区表、语言/唤醒词等 sdkconfig 编译选项
- **板级初始化**：继承 `WifiBoard`/`Ml307Board`/`DualNetworkBoard`；实现 `GetAudioCodec()`/`GetDisplay()`/`GetBacklight()` 等虚函数
- **Kconfig 集成**：在 `choice BOARD_TYPE` 中添加配置项；`depends on IDF_TARGET_XXX` 限定芯片
- **CMakeLists 集成**：设置 `BOARD_TYPE`、字体大小、表情集合
- **编译**：`python scripts/release.py [开发板目录名]` 一键配置编译打包
- **关键警告**：新建板子必须独立目录+独立名称，不可覆盖原有板子配置，否则 OTA 升级会覆盖自定义固件

## Related Concepts

- [[xiaozhi-ai-framework]] — 小智AI代码框架
- [[spi-protocol]] — SPI 显示屏通信
- [[i2c-protocol]] — I2C 音频编解码器
