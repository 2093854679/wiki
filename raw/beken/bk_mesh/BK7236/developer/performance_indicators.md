---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/developer/performance_indicators.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 性能指标

<a id="id2"></a>

## **概述**

BK Wi-Fi Mesh 的性能指标包括组网时长、添加单个节点的入网时间、子节点故障后的网络恢复时长、根节点故障后的网络恢复时长、每跳时延、OTA升级时长等。

以下性能数据基于 20 个节点的 3 层网络测试环境。

<a id="bridge"></a>

## **Bridge 模式性能指标**

<a id="id4"></a>

Bridge 模式


| 指标项 | 数值 |
| --- | --- |
| **组网时长** | — |
| 指定根节点组网时长 | 223s |
| 选举根节点组网 | 45s |
| 增加单个节点的入网时长 | 5s |
| **中间子节点掉电后的网络恢复时长** | — |
| 从节点感知网络故障到网络恢复的时长 | 5s |
| 从节点掉电到网络恢复的时长 | 20s |
| **根节点掉电后的网络恢复时长** | — |
| 从节点感知网络故障到网络恢复的时长 | 47s |
| 从节点掉电到网络恢复的时长 | 62s |
| **时延** | — |
| 每跳时延 | 2ms |

<a id="napt"></a>

## **NAPT 模式性能指标**

<a id="id5"></a>

NAPT 模式


| 指标项 | 数值 |
| --- | --- |
| **组网时长** | — |
| 局域网指定根节点 | 13s |
| 广域网指定根节点 | 17s |
| 广域网选举根节点 | 32s |
| 增加单个节点的入网时长 | 5s |
| **中间子节点掉电后的网络恢复时长** | — |
| 从节点感知网络故障到网络恢复的时长 | 5s |
| 从节点掉电到网络恢复的时长 | 20s |
| **根节点掉电后的网络恢复时长** | — |
| 局域网指定根节点掉电后网络不恢复，等待指定根节点上线 | N/A |
| 从节点感知网络故障到网络恢复的时长（选举根节点） | 30s |
| 从节点掉电到网络恢复的时长（选举根节点） | 45s |

<a id="id3"></a>

## **说明**

BK Wi-Fi Mesh 的性能参数和网络环境密切相关。

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [开发者指南](../developer.md)
- [网络介绍](mesh_net_introduction.md)
- [配网和网络控制](mesh_net_distribution_and_control.md)
- [组网和网络恢复](mesh_net_build_and_restore.md)
- [数据传输](mesh_data_transmission.md)
- [网络版本升级（OTA）](bk_mesh_ota.md)
- [配网及网络控制API使用说明](mesh_net_api.md)
- [API参考](../api-reference.md)
- [示例演示](../examples.md)
