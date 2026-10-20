---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/examples/user_information.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="user-information"></a>

# 用户信息示例（user\_information）

<a id="id1"></a>

## **概述**

本示例演示在组网\*\*前后\*\*如何传递用户自定义信息：组网前通过 **Vendor IE** 在 beacon/probe response 中携带信息并扫描获取；组网后通过 **Mesh Vendor set/get** 在节点间下发和回传数据（示例为 RSSI、IP）。

<a id="id2"></a>

## **代码流程**

<a id="id5"></a>

user\_information 主流程（组网前 Vendor IE → 组网 → 组网后 set/get）

```
① 初始化 + vendor set/get 回调注册
               |
               v
② bk_wifi_get_vendor_ie_cb（注册取 IE 回调）
               |
               v
③ bk_wifi_ap_add_vendor_ie（向 beacon 写入自定义 IE）
               |
               v
④ bk_wifi_scan_start（扫描对端 beacon，读 Vendor IE）
               |
               v
⑤ bk_wifi_ap_add_vendor_ie(NULL, 0)（组网前删除 IE）
               |
               v
⑥ 根节点：get_idle_node + bk_wifi_mesh_net_cfg 等完成组网
               |
               v
⑦ bk_wifi_mesh_set_vendor（根向节点下发用户数据）
               |
               v
⑧ bk_wifi_mesh_get_vendor（根读取节点回传数据）
```

1. **初始化** — Mesh 与 **vendor set/get 回调** （见「公共初始化」）。
2. **②～⑤** — **组网前** 通过 Vendor IE 携带与读取自定义信息（见「Vendor IE」小节）。
3. **⑥** — 仅根节点侧完成拉网、配网（与 no\_router 等示例类似）。
4. **⑦⑧** — **组网后** 根节点 set/get Mesh 用户数据（见「组网后：Mesh Vendor set/get」）。

<a id="api"></a>

## **API 使用说明**

**1\. 公共初始化**

除常规 Mesh 初始化外，需额外注册：

- `bk_wifi_mesh_set_vendor_cb_reg(bk_wifi_mesh_set_vendor_callback)` — 处理 set vendor 请求
- `bk_wifi_mesh_get_vendor_cb_reg(bk_mesh_net_get_vendor_callback)` — 处理 get vendor 请求，返回本机数据（如 RSSI、IP）

本示例使用 `bk_wifi_mesh_set_net_mode(2)`，局域网模式，无路由器。

**2\. 组网前：Vendor IE（beacon/probe response）**

<a id="id6"></a>

Vendor IE 相关 API


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_get_vendor_ie_cb(cb, oui, oui_len)` | 注册扫描回调，当扫描到匹配 OUI 的 Vendor IE 时触发 |
| 2 | `bk_wifi_ap_add_vendor_ie(buf, buf_len)` | 在 AP beacon/probe response 中添加 Vendor IE；格式：Element ID(221) \+ length \+ OUI(4) \+ content；示例中通过 `bk_wifi_mesh_ap_add_vendor()` 封装 |
| 3 | `bk_wifi_scan_start(NULL)` | 发起扫描，在回调中获取其他 AP 的 Vendor IE 内容 |
| 4 | `bk_wifi_ap_add_vendor_ie(NULL, 0)` | 删除已添加的 Vendor IE |

**3\. 组网后：Mesh Vendor set/get**

下发数据和请求数据的动作可由任意节点执行，本示例中由根节点操作。组网流程与 no\_router 相同：`bk_wifi_mesh_get_idle_node` → `bk_wifi_mesh_net_cfg` → 轮询 `bk_wifi_mesh_get_topo` 直至全部入网。

<a id="id7"></a>

Mesh Vendor API


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_mesh_set_vendor(&set_vendor)` | 向指定节点下发用户数据；`node_num`、`node_mac_list` 根据实际情况设置目标节点，本示例中来自拓扑；`vendort_ptr` 为下发内容 |
| 2 | `bk_wifi_mesh_get_vendor(&get_vendor)` | 向指定节点请求用户数据；`vendort_ptr` 中的 type 为用户自定义，本示例 type\=3 表示请求 IP\+RSSI 仅作示例；结果在 `BK_MESH_EVENT_GET_VENDOR` 事件中返回 |

**4\. get vendor 回调返回值说明**

`bk_mesh_net_get_vendor_callback(vendor_type)` 中的 type 为用户自定义，由请求方与响应方约定。本示例中按 type 返回不同内容：

<a id="id8"></a>

get vendor 返回值


| vendor\_type | 返回内容（本示例） |
| --- | --- |
| 1 | IP 地址（netif\_ip4\_config\_t） |
| 2 | RSSI |
| 3 | IP \+ RSSI |

本示例中 IP 通过 `bk_netif_get_ip4_config(NETIF_IF_AP/NETIF_IF_BRIDGE, &ip4_info)` 获取，RSSI 通过 `bk_wifi_sta_get_link_status()` 获取。用户可根据业务需求自定义 type 含义及返回内容。

**5\. 事件回调**

<a id="id9"></a>

事件


| 事件 | 说明 |
| --- | --- |
| BK\_WIFI\_MESH\_NODE\_SET\_VENDOR | 收到 set vendor，在 set\_vendor\_callback 中处理 |
| BK\_WIFI\_MESH\_NODE\_GET\_VENDOR | 收到 get vendor 请求，在 get\_vendor\_callback 中填充返回数据 |
| BK\_MESH\_EVENT\_GET\_VENDOR | 发起 get vendor 的节点收到各目标节点返回的数据后，在此事件中汇总 |

<a id="id3"></a>

## **项目结构**

```
user_information/main/
├── armino_main.c
├── vendor_flash.c
└── vendor_flash_partition.h
```

<a id="id4"></a>

## **编译与烧录**

```
make bk7236 PROJECT=examples/user_information
```
