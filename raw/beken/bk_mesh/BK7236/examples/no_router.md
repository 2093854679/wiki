---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/examples/no_router.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="no-router"></a>

# 自行组网示例（no\_router）

<a id="id1"></a>

## **概述**

本示例演示在无外部路由器的环境下构建 BK Wi-Fi Mesh 网络。根节点负责获取空闲节点、下发配网信息并建立网络；非根节点等待接收配网信息入网后，可向根节点发送单播数据。

<a id="id2"></a>

## **代码流程**

**根节点流程** （CONFIG\_MESH\_ROOT 使能时）：

<a id="id5"></a>

根节点主流程（自上而下顺序执行）

```
① 初始化与回调注册
           |
           v
② clear_flash
           |
           v
③ set_net_mode(2) + set_api_mode
           |
           v
④ semaphore_init
           |
           v
⑤ get_idle_node（循环获取空闲节点）
           |
           v
⑥ bk_wifi_mesh_net_cfg（配网）
           |
           v
⑦ get_topo（等待入网完成）
           |
           v
⑧ send_broadcast_data
```

**非根节点流程** （CONFIG\_MESH\_ROOT 未使能时）：

<a id="id6"></a>

非根节点主流程

```
① 初始化与回调注册
           |
           v
② bk_wifi_mesh_status_info（轮询状态）
           |
           v
③ state == NETWORKED（已入网）
           |
           v
④ bk_wifi_mesh_comm_mac_get（取根节点 MAC）
           |
           v
⑤ bk_wifi_mesh_data_send（单播发至根节点）
```

<a id="api"></a>

## **API 使用说明**

**1\. 公共初始化（根节点与非根节点相同）**

<a id="id7"></a>

初始化 API 调用顺序


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_mesh_enable_bcn_tx_by_high_rate(true)` | 节点数超过 20 时启用高速 beacon 发送 |
| 2 | `bk_wifi_mesh_register_node_event_cb()` | 注册节点事件回调 |
| 3 | `bk_wifi_mesh_register_rcv_cb()` | 注册单播数据接收回调 |
| 4 | `bk_wifi_mesh_register_rcv_broadcast_cb()` | 注册广播数据接收回调 |
| 5 | `bk_wifi_mesh_set_free_ap_ssid("bk_mesh_apfx")` | 设置空闲节点 AP 的 SSID |
| 6 | `bk_wifi_mesh_set_free_ap_channel(1)` | 设置空闲节点 AP 的信道 |
| 7 | `bk_wifi_mesh_clear_flash()` | 清除历史组网信息 |
| 8 | `bk_wifi_mesh_node_init()` | 初始化 Mesh 节点 |
| 9 | `bk_wifi_mesh_set_net_mode(2)` | 设为局域网模式（2），不连接路由器 |
| 10 | `bk_wifi_mesh_set_api_mode(bk_wifi_mesh_net_event_cb)` | 注册网络事件回调，用于接收空闲节点列表、拓扑等 |

**2\. 根节点流程**

<a id="id8"></a>

根节点流程 API


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_mesh_get_idle_node()` | 请求获取空闲节点列表；通过 `BK_MESH_EVENT_GET_IDLE_NODE` 事件返回结果 |
| 2 | `bk_wifi_mesh_net_cfg(&config)` | 下发配网信息；本示例为无路由器组网，故不填写 `router_ssid`、`router_pw`；若为带路由器组网则需填写 |
| 3 | `bk_wifi_mesh_get_topo()` | 请求拓扑；通过 `BK_MESH_EVENT_GET_TOPO` 返回；轮询直到 `mesh_topo_list_num == mesh_idle_node_num` 表示全部入网 |
| 4 | `bk_wifi_mesh_send_broadcast_data(data, len)` | 组网完成后发送广播数据 |

**3\. 非根节点流程**

<a id="id9"></a>

非根节点流程 API


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_mesh_status_info(&link_status)` | 轮询获取连接状态，等待根节点下发配网信息并完成入网；当 `link_status.state == BK_MESH_LINKSTATE_NETWORKED` 时表示已入网 |
| 2 | `bk_wifi_mesh_comm_mac_get(my_mac, root_mac)` | 获取本机 MAC 与根节点 MAC |
| 3 | `bk_wifi_mesh_data_send(root_mac, data, len, 0)` | 向根节点发送单播数据 |

**4\. 网络事件回调**

<a id="id10"></a>

网络事件


| event\_id | 说明 |
| --- | --- |
| BK\_MESH\_EVENT\_GET\_IDLE\_NODE | 空闲节点列表返回 |
| BK\_MESH\_EVENT\_GET\_TOPO | 拓扑列表返回 |

**5\. 配网参数 bk\_wifi\_mesh\_net\_cfg\_t**

本示例配置要点：本示例为无路由器组网，故不填写 `router_ssid`、`router_pw`；`sap_ssid`、`sap_pw` 为 Mesh SoftAP 凭证；`design_root` 为配网信息中指定的根节点 MAC。若为带路由器组网则需填写路由器信息。

<a id="id3"></a>

## **项目结构**

```
no_router/main/armino_main.c
```

<a id="id4"></a>

## **编译与烧录**

```
make bk7236 PROJECT=examples/no_router
```
