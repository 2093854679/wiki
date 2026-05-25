# Set Component Build Option[](#set-component-build-option "永久链接至标题")


## Overview[](#overview "永久链接至标题")

When compiling source files for a specific component,you can use `target_compile_options` command to pass compiler options:


```
target_compile_options(${COMPONENT_LIB} PRIVATE -Wno-unused-variable)

```

If you specify compiler flags for a single source file, you can use CMake’s [set_source_files_properties](https://cmake.org/cmake/help/latest/command/set_source_files_properties.html "https://cmake.org/cmake/help/latest/command/set_source_files_properties.html") command:


```
set_source_files_properties(compile_options.c
    PROPERTIES COMPILE_FLAGS

    -Wno-unused-variable
)

```

Note that, the above two commands can only be called after the `armino_component_register` command in the component CMakeLists file.

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/102_build_options "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/102_build_options")
