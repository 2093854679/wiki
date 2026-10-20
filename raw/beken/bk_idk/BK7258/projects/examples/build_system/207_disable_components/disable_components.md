---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/projects/examples/build_system/207_disable_components/disable_components.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="disable-component"></a>

<a id="project-disable-component"></a>

# Disable Component

<a id="overview"></a>

## Overview

There are several ways to disable a component, one of which is through the component enable configuration in Kconfig:

```
set(src)
set(inc)

if (CONFIG_C1)
    list(APPEND src c1.c)
    list(APPEND inc include)
endif()

armino_component_register(SRCS ${src} INCLUDE_DIRS ${inc})
```

Note that the following is the wrong way to disable a component. Because the armino build system relies on `armino_component_register()` to generate the component during the component list generation phase (ie, the early augmentation phase), and the component’s Kconfig configuration is loaded during the component processing phase only if the component is generated first:

```
if (CONFIG_C1)
    armino_component_register(SRCS ${src} INCLUDE_DIRS ${inc})
endif()
```

The following way of writing may also cause problems, value of CONFIG\_C1 will not be clarified until the component is registered

```
if (CONFIG_C1)
    armino_component_register(SRCS ${src} INCLUDE_DIRS ${inc} REQUIRES c2 c3 c4)
else()
    armino_component_register()
endif()
```

Other ways to disable components are:

> - Disable (TODO) via ARMINO\_SOC
> - Disable (TODO) with EXCLUDE\_COMPONENTS

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/207_disable_components)
