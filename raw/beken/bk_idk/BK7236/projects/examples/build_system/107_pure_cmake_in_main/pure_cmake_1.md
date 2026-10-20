---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/projects/examples/build_system/107_pure_cmake_in_main/pure_cmake_1.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="pure-cmake-1"></a>

<a id="project-pure-cmake-1"></a>

# Pure CMake 1

<a id="overview"></a>

## Overview

In the example, foo is built using pure CMake, placed in the main component, and can be imported as follows:

```
armino_component_register(SRCS "main.c" INCLUDE_DIRS .)
add_subdirectory(foo)
target_link_libraries(${COMPONENT_LIB} PUBLIC foo)
```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/107_pure_cmake_in_main)

## 模块导航

- [简介](../../../../introduction.md)
- [快速入门](../../../../get-started.md)
- [H/W 参考手册](../../../../hw-reference.md)
- [API 参考手册](../../../../api-reference.md)
- [开发者指南](../../../../developer-guide.md)
- [安全](../../../../security.md)
- [OS 相关参考](../../../../os.md)
- [购买 BK7236 开发板](../../../../boards.md)
- [工程与示例](../../../projects.md)
- [app](../../../app/app.md)
- [Bluetooth](../../../bluetooth/bluetooth.md)
- [Examples](../../examples.md)
- [Build System](../build_system.md)
- [Minimum Project](../001_simplest_proj/minimum_project.md)
- [Add Component Dir](../002_add_components_dir/add_components_dir.md)
- [Exclude Component Dir](../003_exclude_components/exclude_components_dir.md)
- [Build Specific Components](../004_set_components/set_components.md)
- [Override Default Compile Options](../005_proj_build_options/proj_build_options.md)
- [Minimum Component](../101_simplest_component/simplest_component.md)
- [Set Component Build Option](../102_build_options/component_build_options.md)
- [Components Dependency](../104_dependency/component_dependency.md)
- [Customize Component Name](../105_customize_component_name/customize_component_name.md)
- [Pure Cmake Component](../106_pure_cmake_component/pure_cmake_component.md)
- [Pure CMake 2](../108_pure_cmake_in_component/pure_cmake_2.md)
- [CMake Uses Armino Lib](../110_use_armino_lib_in_pure_cmake/cmake_use_armino_lib.md)
- [Import GNU Makefile Project 1](../111_integrate_makefile_project/import_gnu_makefile_project_1.md)
- [Import GNU Makefile Project 2](../112_use_gnu_make_project2/import_gnu_makefile_project_2.md)
- [Minimum Component Kconfig](../201_simplest_kconfig/minimum_kconfig.md)
- [Add Global Kconfig](../202_global_kconfig/global_kconfig.md)
- [Pure Config Kconfig](../203_config_only/pure_config_kconfig.md)
- [SoC Common Config](../204_project_common_config/common_kconfig.md)
- [SoC Common Config](../205_project_per_soc_config/per_soc_kconfig.md)
- [Disable Component](../207_disable_components/disable_components.md)
- [Peripherals](../../peripherals/peripherals.md)
- [Security](../../../security/security.md)
- [Wi-Fi](../../../wifi/wifi.md)
- [样例 CLI 演示](../../../../examples.md)
- [开发与贡献代码流程](../../../../process.md)
