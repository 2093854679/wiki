# Add Global Kconfig[](#add-global-kconfig "永久链接至标题")


## Overview[](#overview "永久链接至标题")

A Kconfig file can be defined for a component to implement global component configuration.If you want to add configuration options at the top level of menuconfig,rather than in the “Component Configuration” submenu, you can define these options in the KConfig.projbuild file in the same directory as the CMakeLists.txt file.

Usually a project-specific Kconfig.projbuild is added to the main component. But be careful when adding configurations in this file as these are included in the overall project configuration.
Where possible, create a KConfig file for component configuration.

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/202_global_kconfig "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/202_global_kconfig")
