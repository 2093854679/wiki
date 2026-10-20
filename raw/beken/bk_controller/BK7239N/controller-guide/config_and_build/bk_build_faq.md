---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/config_and_build/bk_build_faq.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 常见问题

<a id="config"></a>

## 001 \- 使用CONFIG宏控制组件注册

下面是错误的禁用组件方法。因为 armino 构建系统在生成组件列表阶段（即早期扩充阶段）依赖 `armino_component_register()`
来生成该组件，而只有先生成该组件才会在组件处理阶段加载组件的 Kconfig 配置:

```
if (CONFIG_C1)
    armino_component_register(SRCS ${src} INCLUDE_DIRS ${inc})
endif()
```

下述写法也可能带来问题，当组件使用CONFIG宏来控制组件注册:

```
if (CONFIG_C1)
    armino_component_register(SRCS ${src} INCLUDE_DIRS ${inc} REQUIRES c2 c3 c4)
else()
    armino_component_register()
endif()
```

<a id="id2"></a>

## 002 \- 工程中找不到函数定义

在工程main目录下的源文件中，如果出现某个组件的函数或者宏未定义的情况，往往是由于这个工程未被添加到main组件中，应该在main目录下的CMakeLists.txt中加上组件依赖，如添加 `dependency_component` 组件:

```
armino_component_register(SRCS "${srcs}" INCLUDE_DIRS "${incs}" PRIV_REQUIRES dependency_component)
```

<a id="id3"></a>

## 003 \- 编译工具链和编译参数查看

在编译目录下相应工程目录里面中compile\_commands.json文件，其中包含所有源文件的编译命令，可以查看每个源文件编译工具链和编译参数。
如bk7239的app工程，在build/app/bk7239/compile\_commands.json中可以查看相应的编译命令。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [硬件开发指南](../../hw-reference.md)
- [Controller软件开发指南](../../controller-guide.md)
- [软件架构](../sw_arch.md)
- [配置与构建](../config_and_build.md)
- [构建概述](bk_build_overview.md)
- [构建示例](bk_build_example.md)
- [构建api](bk_build_api.md)
- [构建设计](bk_build_design.md)
- [Kconfig 配置](bk_config_kconfig.md)
- [系统配置](bk_config_kconfig.md)
- [分区配置](bk_config_partitions.md)
- [安全配置](bk_config_security.md)
- [OTA 配置](bk_config_ota.md)
- [非安全版本OTP使用介绍](bk_config_otp_efuse.md)
- [API参考手册](../api-reference.md)
- [平台开发指南](../platform_guide.md)
- [Wi-Fi开发指南](../wifi_guide.md)
- [蓝牙开发指南](../bluetooth_guide.md)
- [网络协议开发指南](../network_protocol_guide.md)
- [低功耗开发指南](../low_power_guide.md)
- [外设开发指南](../peripheral_guide.md)
- [主控平台软件开发指南](../../host-guide.md)
- [工程与示例](../../project-example.md)
- [开发工具介绍](../../dev-tool.md)
- [调测指导](../../debug-guide.md)
- [产测指导](../../production-test-guide.md)
- [常见问题解答](../../faq.md)
