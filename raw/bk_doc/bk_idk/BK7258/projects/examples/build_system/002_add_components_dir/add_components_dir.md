# Add Component Dir[](#add-component-dir "永久链接至标题")


## Overview[](#overview "永久链接至标题")

You can set EXTRA_COMPONENTS_DIRS in the top-level CMakeLists.txt of the project to import components other than the default component search directory:


```
cmake_minimum_required(VERSION 3.5)
set(EXTRA_COMPONENTS_DIRS my_component_dir)
include($ENV{ARMINO_PATH}/tools/build_tools/cmake/project.cmake)
project(myProject)

```

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/002_add_components_dir "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/002_add_components_dir")
