---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/developer/mesh_net_distribution_and_control.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-wi-fi-mesh"></a>

<a id="mesh-net-distribution-and-control"></a>

# **BK Wi-Fi MESH配网及网络控制**

<a id="id1"></a>

## **1.简介**

Wi-Fi MESH配网提供APP配网和API配网两种方式，均可实现空闲MESH节点发现，MESH节点组网，查询网络拓扑，网络控制，OTA等功能。API接口配网主要用于云端配网。APP配网请参考文档《博通集成Wi-Fi Mesh App使用介绍文档》。

本文档主要介绍Wi-Fi Mesh配网及网络控制API的使用方法，供开发者参考。

备注

文档链接:[https://docs.bekencorp.com/arminodoc/bk\_mesh/app/zh\_CN/latest/index.html](../../../bk_toolkit/meshapp/index.md)

<a id="id2"></a>

## **2.配网流程**

BK MESH API提供接口，用于获取空闲节点列表，配置MESH网络的各项参数，以及查询网络拓扑(只支持树状)和控制设备等，通过BK MESH API实现对MESH网络的查询及控制。

BK MESH配网主要分为两种： （1）统一配网。先获取空闲节点列表，再分发配网信息对所有空闲节点进行配网；（2）分步配网。先对根节点进行配网，再添加其他节点进入网络。

**2.1 统一配网**

主要包括以下步骤：

> - **I 获取空闲节点**
>
>   > 可在网关节点或任意节点处调用API获取空闲节点，即可获得当前空口环境中全部符合条件的空闲MESH节点的信息，为下一步配网做准备；
> - **II 空闲节点配网**
>
>   > 获取到空闲节点后，可在网关节点或任意空闲MESH节点处调用API，向MESH节点发送配网信息，如配网节点数量，指定根节点等，实现空闲节点配网组网，形成MESH网络。
>   >
>   > API接口接收到配网请求后，验证配网信息的有效性，将配网信息传递给MESH节点，各节点根据配置信息开始执行配网操作，如扫描，连接，配置MESH网络等。

统一配网的example代码可参考：examplesno\_router中的配网实现。

**2.2 分步配网**

主要包括以下步骤：

> - **I 根节点配网**
>
>   > 可在网关节点处调用API对根节点进行配网；
> - **II 获取空闲节点**
>
>   > 可在网关节点处调用API获取空闲节点，即可获得当前空口环境中剩余的全部符合条件的空闲MESH节点的信息，为下一步添加节点做准备；
> - **III 添加节点**
>
>   > 获取到空闲节点后，可在网关节点处调用添加节点API，将添加节点进入网络。
>   >
>   > API接口接收到添加节点请求后，验证添加节点的有效性，将添加节点信息传递给MESH节点，各节点根据配置信息开始执行添加节点操作，如扫描，连接，配置MESH网络等。

分布配网的example代码可参考：examplesota中的配网实现。

<a id="id3"></a>

## **3.网络控制**

> MESH网络组网成功后，可在根节点调用API，进行查询网络拓扑(只支持树状)和控制设备等，对MESH网络进行查询或者控制。
> 相关API介绍见 [配网及网络控制API使用说明](mesh_net_api.md#mesh-net-api)
>
> - **查询网络拓扑**
>
>   > 在根节点处调用API，查询网络拓扑(只支持树状)，可获取到当前网络情况，如在线节点数，网络层级，节点拓扑关系等；
> - **修改MESH网络**
>
>   > 在根节点处调用API，可实现对MESH网络的控制，如增加MESH网络节点数量、删除MESH网络中部分节点或全部节点、修改网络配置等；
> - **设置用户信息/查询用户信息**
>
>   > 在根节点处调用API，配置或者查询用户信息；
>   >
>   > example代码可参考：examplesuser\_information。
> - **OTA升级**
>
>   > 在根节点处调用API，配置OTA升级信息，启动OTA升级或者通过查询OTA升级状态来确认升级是否完成；
>   >
>   > example代码可参考：examplesota。
> - **节点重置**
>
>   > 当存在某个节点从MESH网络断开且无法重新加入网络时，可使用节点重置功能将该节点Reset，使其恢复到空闲节点状态。
> - **获取节点状态信息**
>
>   > 查询节点的状态信息，如状态，层级，父节点以及与起相关联的节点数。
