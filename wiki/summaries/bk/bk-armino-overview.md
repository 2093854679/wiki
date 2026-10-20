---
type: summary
source_root: beken
sdk_family: bk_idk
chip: [BK7235, BK7236, BK7236N, BK7239, BK7256, BK7258]
sdk_version:
  BK7235: v1.5
  BK7236: v2.0.1
  BK7236N: v2.2.1
  BK7239: v2.2.1
  BK7256: v1.5
  BK7258: v2.0.1
processor: null
---

# ARMINO IDK 开发框架概述

> **TLDR:** Armino IDK 是面向 Beken AIoT 芯片的开发底座，提供 API、示例、构建配置与安全框架；跨芯片可共享开发方法，但芯片能力与配置规则必须按对应文档版本核验。
> **Source:** [BK7235 概述](../../../raw/beken/bk_idk/BK7235/introduction/bk_overview.md)、[BK7236 概述](../../../raw/beken/bk_idk/BK7236/introduction/bk_overview.md)、[BK7236N 概述](../../../raw/beken/bk_idk/BK7236N/introduction/bk_overview.md)、[BK7239 概述](../../../raw/beken/bk_idk/BK7239/introduction/bk_overview.md)、[BK7256 概述](../../../raw/beken/bk_idk/BK7256/introduction/bk_overview.md)、[BK7258 概述](../../../raw/beken/bk_idk/BK7258/introduction/bk_overview.md)

## 关键要点

- **框架定位。** 概述面向 Wi-Fi、BT、低功耗和多媒体应用，列出 API/Demo、灵活工程、安全框架及多种物联网操作系统等方向；这些是框架能力范围，不是每个芯片、工程都启用全部功能的保证。[BK7236 概述](../../../raw/beken/bk_idk/BK7236/introduction/bk_overview.md)
- **项目、组件、目标分开理解。** 构建文档将组件编译为静态库，再链接到应用；目标对应具体芯片，项目目录包含源码、配置、分区和引导程序等支持文件。[构建概述](../../../raw/beken/bk_idk/BK7236/developer-guide/build_config/bk_build_overview.md)
- **CMake 与 Kconfig 负责不同事项。** CMake 组织构建，Kconfig 定义配置项，工程及芯片配置文件覆盖默认值；所读 BK7236 v2.0.1 配置页明确不支持 menuconfig，不能泛称所有 Armino 都提供图形菜单配置。[BK7235 概述](../../../raw/beken/bk_idk/BK7235/introduction/bk_overview.md)／[BK7236 Kconfig](../../../raw/beken/bk_idk/BK7236/developer-guide/config_tools/bk_config_kconfig.md)
- **按问题下钻。** 原始文档将 API、开发指南、安全、OS 和工程示例分开；查函数参数读 API，查调用流程和工程配置同时读指南与示例。[BK7236 总入口](../../../raw/beken/bk_idk/BK7236.md)

## 适用范围

覆盖 frontmatter 列出的六个 IDK 默认中文文档版本。本文不建立“芯片代际演进表”，也不把某个芯片的 CPU、USB、多媒体、安全或 RTOS 配置推定为其它芯片的能力。

## Related

- [[bk-armino-framework]]
- [[bk-wifi-api-v2]]
- [[bk-security-framework]]
- [[bk-ai-solution-overview]]
