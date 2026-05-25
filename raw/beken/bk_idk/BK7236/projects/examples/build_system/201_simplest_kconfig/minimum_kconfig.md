# Minimum Component Kconfig[](#minimum-component-kconfig "永久链接至标题")


## Overview[](#overview "永久链接至标题")

Each component can contain a `Kconfig` file that contains some configuration setting information to be added to the component.

The easiest way to create a Kconfig file for a component is to use an existing Kconfig file in ARMINO as a template and modify it based on that.

Simplest component Kconfig:


```
config C1
    bool "Enable component c1"
    default y

```

The build system will add the following configuration items to the generated sdkconfig:


```
CONFIG_C1=y

```

The build system will add the following configuration items to sdkconfig.h in the build root directory (usually the build directory):


```
#define CONFIG_C1 1

```

[example](https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/201_simplest_kconfig "https://github.com/bekencorp/armino/tree/main/projects/examples/build_system/201_simplest_kconfig")
