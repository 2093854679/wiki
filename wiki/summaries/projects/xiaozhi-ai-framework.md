# 小智AI机器人 — 代码框架

> **Source:** [小智AI机器人 - 代码框架梳理.md](../../../raw/Study_Note/02-嵌入式开发/小智ai机器人/小智AI机器人 - 代码框架梳理.md)
> **TLDR:** 小智AI是基于ESP32的开源嵌入式AI项目，采用ESP-IDF构建系统，包含多板卡硬件抽象层、OTA升级、MQTT/WebSocket协议栈和多语言资源管理。

## Key Points

- **项目结构**：CMakeLists.txt（ESP-IDF构建）、main.cc（应用入口）、application（主逻辑）、background_task（后台任务）、system_info/settings（配置管理）
- **构建系统**：`idf_build_set_property(MINIMAL_BUILD ON)` 最小化构建；`idf_components.yml`管理ESP-IDF组件依赖
- **多板卡支持**：boards/目录包含50+种硬件配置，每种板卡对应独立目录；sdkconfig.defaults.esp32c3/esp32s3分别适配不同芯片
- **分区表**：16MB Flash分区——nvs(OTA数据)、otadata、phy_init、ota_0/ota_1（双区OTA）、assets（SPIFFS，8MB语音资源）
- **硬件抽象层**：display/（LCD/OLED抽象）、boards/（板卡定义）、protocols/（MQTT/WebSocket）
- **多语言资源**：zh-CN/zh-TW/en-US/ja-JP语音包和language.json配置
- **代码架构**：面向对象设计，每个板子封装成类，共性提取为父类

## Related Concepts

- [[embedded-registration-patterns]] — 模块注册/硬件抽象设计模式
- [[freertos-task-management]] — FreeRTOS任务管理
