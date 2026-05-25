# Build Specific Components[](#build-specific-components "永久链接至标题")


## Overview[](#overview "永久链接至标题")

You can set COMPONENTS in the top-level CMakeLists.txt of the project to build only specific components.In the example, only c3_contain_main and dependent components are built:


```
cmake_minimum_required(VERSION 3.5)
set(COMPONENTS c3_contain_main)
include($ENV{ARMINO_PATH}/tools/build_tools/cmake/project.cmake)
project(myProject)

```

Notice：

> - All components and dependencies in the COMPONENTS list will be built.
> - Since all components depend on the common component, the common component is also built.
> - The `main()` function implementation must be included in the build component.

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/004_set_components "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/004_set_components")
