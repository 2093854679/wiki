# Customize Component Name[](#customize-component-name "永久链接至标题")


## Overview[](#overview "永久链接至标题")

When compiling source files for a specific component,you can use `armino_component_register_ex` command to customize component mame.:


```
set(config_component_name bk_demo_ex)

armino_component_register_ex(INTERNAL_LIB
                        SRCS "${srcs}"
                        INCLUDE_DIRS "${incs}"
                        CONFIG_COMPONENT_NAME "${config_component_name}")

```

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/105_customize_component_name "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/105_customize_component_name")
