---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/examples/index.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# **实例演示**

<a id="id2"></a>

## **概述**

本节介绍 BK Wi-Fi Mesh 提供的四个示例工程，涵盖 APP 配网、无路由器自行组网、OTA 升级以及用户信息的传递与获取。每个示例均基于 BK7236 平台，可帮助开发者快速理解并搭建 Mesh 应用。

<a id="id3"></a>

示例概览


| 示例名称 | 功能说明 | 适用场景 |
| --- | --- | --- |
| APP配网 | 基于 BK Mesh APP 对设备进行配网、拓扑管理、添加/删除节点及 OTA | 需要手机 APP 进行配网和管理的产品 |
| 自行组网 | 不依赖外部路由器，设备间通过 SoftAP 自组织形成 Mesh 网络 | 无互联网、无路由器的局域 Mesh 通信 |
| OTA升级 | 根节点发起云端/URL 拉取升级，子节点接收并执行 OTA | 已组网的 Mesh 网络批量固件升级 |
| 用户信息 | 组网前后使用 Vendor IE 与 Mesh Vendor 在节点间传递自定义信息（如 RSSI、IP） | 需要在节点间交换用户自定义数据的应用 |

- [APP配网](examples/app_provisioning.md)
- [自行组网](examples/no_router.md)
- [OTA升级](examples/OTA.md)
- [用户信息](examples/user_information.md)

## 模块导航

- [简介](introduction.md)
- [快速入门](get-started.md)
- [开发者指南](developer.md)
- [API参考](api-reference.md)
- [APP配网](examples/app_provisioning.md)
- [自行组网](examples/no_router.md)
- [OTA升级](examples/OTA.md)
- [用户信息](examples/user_information.md)
