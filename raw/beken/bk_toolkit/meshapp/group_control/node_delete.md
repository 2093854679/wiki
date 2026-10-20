---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/app/zh_CN/latest/group_control/node_delete/index.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 5.4. 删除节点

在群组页面中，选择想要删除的节点，在底部持操作视图中，点击删除，被删除的设备会重新成为空闲节点， `层级指示灯` 会变成白色、无闪烁状态, `控制指示灯` 将熄灭，如下图。

<a id="id2"></a>
[![file_tree](../../../_assets/c06b9e350263c59fca32-idle_led.jpg)](../../../_assets/c06b9e350263c59fca32-idle_led.jpg)


删除完成

如果该节点下面有子节点，将进行网络重组，子节点将重新寻找新的父节点， `层级指示灯` 显示为白色闪烁状态，当所有设备状态稳定后，表示重组网完成。

## 模块导航

- [1. 简介](../summary.md)
- [2. 下载安装](../download.md)
- [3. 硬件准备](../device_prepare.md)
- [4. 新建群组](../new_group.md)
- [5. 群组控制](../group_control.md)
- [5.1. 概览](desc.md)
- [5.2. 添加节点](node_add.md)
- [5.3. 灯光控制](light_control.md)
- [6. 群组拓扑](../group_topology.md)
- [7. ota](../ota.md)
