# SoC Common Config[](#soc-common-config "永久链接至标题")


## Overview[](#overview "永久链接至标题")

As the statement in example “soc common config”, we now have one common config file for project, two specific config files for soc,

> - if we conduct “make bk7231n PROJETC=/example/build_system/205_project_per_soc_config”, the print will be “CONFIG_FOO=100”
> - if we conduct “make bk7256 PROJETC=/example/build_system/205_project_per_soc_config”, the print will be “CONFIG_FOO=1000”

[example](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/205_project_per_soc_config "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system/205_project_per_soc_config")
