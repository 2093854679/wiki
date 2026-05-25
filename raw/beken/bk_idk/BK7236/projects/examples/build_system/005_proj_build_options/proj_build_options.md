# Override Default Compile Options[](#override-default-compile-options "永久链接至标题")


## Overview[](#overview "永久链接至标题")

After project() in the top-level CMakeLists.txt, use Wno-extra to override the default Wextra:


```
cmake_minimum_required(VERSION 3.5)
include($ENV{ARMINO_PATH}/tools/build_tools/cmake/project.cmake)
project(myProject)

armino_build_set_property(COMPILE_OPTIONS "-Wno-extra" APPEND)

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/005_proj_build_options "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/005_proj_build_options")
