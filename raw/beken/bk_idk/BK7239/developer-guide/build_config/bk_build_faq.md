---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/developer-guide/build_config/bk_build_faq.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
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
如bk7239n的app工程，在build/app/bk7239n/compile\_commands.json中可以查看相应的编译命令。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [概述](bk_build_overview.md)
- [示例](bk_build_example.md)
- [函数与属性](bk_build_api.md)
- [实现](bk_build_design.md)
- [配置与工具](../config_tools.md)
- [低功耗与电源管理](../power_save.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [安全](../../security.md)
- [OS 相关参考](../../os.md)
- [购买 BK7239 开发板](../../boards.md)
- [样例 CLI 演示](../../examples.md)
- [开发与贡献代码流程](../../process.md)
