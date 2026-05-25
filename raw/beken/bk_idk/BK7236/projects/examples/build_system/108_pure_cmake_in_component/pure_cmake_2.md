# Pure CMake 2[](#pure-cmake-2 "永久链接至标题")


## Overview[](#overview "永久链接至标题")

In the example, foo is built with pure CMake, placed in the c1 component, and can be imported using the following methods:


```
armino_component_register(SRCS "c1.c" INCLUDE_DIRS include)
add_subdirectory(foo)
target_link_libraries(${COMPONENT_LIB} PUBLIC foo)

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/108_pure_cmake_in_component "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/108_pure_cmake_in_component")
