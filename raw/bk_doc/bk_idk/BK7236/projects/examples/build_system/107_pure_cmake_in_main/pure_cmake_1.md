# Pure CMake 1[](#pure-cmake-1 "永久链接至标题")


## Overview[](#overview "永久链接至标题")

In the example, foo is built using pure CMake, placed in the main component, and can be imported as follows:


```
armino_component_register(SRCS "main.c" INCLUDE_DIRS .)
add_subdirectory(foo)
target_link_libraries(${COMPONENT_LIB} PUBLIC foo)

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/107_pure_cmake_in_main "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/107_pure_cmake_in_main")
