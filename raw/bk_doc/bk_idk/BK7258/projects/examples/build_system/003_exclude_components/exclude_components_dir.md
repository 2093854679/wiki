# Exclude Component Dir[](#exclude-component-dir "永久链接至标题")


## Overview[](#overview "永久链接至标题")

EXCLUDE_COMPONENTS can be set in the top-level CMakeLists.txt of the project to exclude certain components from building:


```
cmake_minimum_required(VERSION 3.5)
set(EXCLUDE_COMPONENTS c1_not_build)
include($ENV{ARMINO_PATH}/tools/build_tools/cmake/project.cmake)
project(myProject)

```

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/003_exclude_components "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/003_exclude_components")
