# Minimum Component[](#minimum-component "永久链接至标题")


## Overview[](#overview "永久链接至标题")

The simplest component CMakeLists.txt is as follows, calling `armino_component_register()` Register the component with the build system:


```
armino_component_register(SRCS c1.c INCLUDE_DIRS include)

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/101_simplest_component "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/101_simplest_component")
