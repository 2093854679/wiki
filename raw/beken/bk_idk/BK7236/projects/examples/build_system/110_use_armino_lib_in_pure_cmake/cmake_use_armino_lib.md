# CMake Uses Armino Lib[](#cmake-uses-armino-lib "永久链接至标题")


## Overview[](#overview "永久链接至标题")

The way to reference armino components in pure CMake components is armino::component_name. In the example, the c1 component in the anywhere directory will use the armino component c component:


```
target_link_libraries(c1 armino::c)

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/110_use_armino_lib_in_pure_cmake "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/110_use_armino_lib_in_pure_cmake")
