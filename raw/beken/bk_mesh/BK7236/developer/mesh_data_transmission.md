---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/developer/mesh_data_transmission.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 数据传输

<a id="id2"></a>

## **数据传输**

BK Wi-Fi Mesh 数据平面提供 **NAPT** 与 **Bridge** 两种模式，**同一时刻只能启用其一**。二者在跨节点互通能力与建议规模上的对比如下。

**1\. NAPT 模式**

- **分支内互通**：ping、iperf 等仅适用于 Mesh 树形拓扑中的 **同一分支** （沿父子链的同一侧）；**不同分支** 上的节点之间无法互 ping、无法互跑 iperf。
- **规模**：适合节点较多的稳定组网与业务传输，典型可参考约 **40 个节点**。

在工程中启用 NAPT，需打开以下宏：

```
CONFIG_IP_FORWARD=y
CONFIG_IP_NAPT=y
```

**2\. Bridge 模式**

- **全网互通**：ping、iperf 可在 **任意两节点** 之间进行；节点间可使用 TCP/UDP 传输业务数据。
- **规模**：建议节点数 **不超过 20**。

在工程中启用 Bridge，需打开以下宏：

```
CONFIG_BRIDGE=y
CONFIG_MULTI_LEVEL_BRIDGE=y
CONFIG_WIFI_BRIDGE_MULTICAST_TO_UNICAST=y
```

**3\. 私有通信机制**

上述两种模式均支持 **Mesh 私有数据通道** （与 IP 层 NAPT/Bridge 无关）：任意节点均可通过专用 API 发送 **单播** 或 **广播** 数据。

**单播 API：**

`bk_err_t bk_wifi_mesh_data_send(uint8_t *rcv_mac_addr, uint8_t *data_buf, uint16_t data_len, uint16_t data_type);`

**广播 API：**

`bk_err_t bk_wifi_mesh_send_broadcast_data(uint8_t *data_buf, uint16_t data_len);`

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [开发者指南](../developer.md)
- [网络介绍](mesh_net_introduction.md)
- [配网和网络控制](mesh_net_distribution_and_control.md)
- [组网和网络恢复](mesh_net_build_and_restore.md)
- [网络版本升级（OTA）](bk_mesh_ota.md)
- [配网及网络控制API使用说明](mesh_net_api.md)
- [性能指标](performance_indicators.md)
- [API参考](../api-reference.md)
- [示例演示](../examples.md)
