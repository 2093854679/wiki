# Pure Cmake Component[](#pure-cmake-component "永久链接至标题")


## Overview[](#overview "永久链接至标题")

Usually the components on the ARMINO component search path should be registered according to ARMINO requirements, but if you want to change the components on the ARMINO component search path to pure CMake components,
the code is as follows:


```
if (CMAKE_BUILD_EARLY_EXPANSION)
        return()
endif()

add_library(c1 STATIC c1.c)
target_include_directories(c1 PUBLIC include)

```

The first three lines of code are used to tell the ARMINO build system not to add this component, and the c1 component will be built in pure CMake. In addition, you also need to add this component to the build system in the way of CMake, This example is to add the c1 component to the build tree in the top-level CMakeLists.txt of the project:


```
cmake_minimum_required(VERSION 3.5)
include($ENV{ARMINO_PATH}/tools/build_toos/cmake_project.cmake)
project(cmake_exam)

add_subdirectory(components/c1)

```

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/106_pure_cmake_component "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/106_pure_cmake_component")

备注

In general, components in the ARMINO search path should call armino_component_register() to write components in the way that ARMINO requires. When you have a specific reason to write your own pure CMake components, you can choose to press _<import third-party CMake components in ARMINO components> or a relative path relative to the project directory. _<Import 3rd party CMake components anywhere> way to import your pure CMake components.
