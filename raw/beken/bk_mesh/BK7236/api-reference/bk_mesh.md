---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/api-reference/bk_mesh.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-wi-fi-mesh-api"></a>

# BK Wi-Fi Mesh API 参考

<a id="bk-wi-fi-mesh"></a>

## BK Wi-Fi Mesh 接口

**节点初始化**

> - `bk_wifi_mesh_node_init()` \- 初始化 Mesh 节点
> - `bk_wifi_mesh_clear_flash()` \- 清除 Mesh 节点 Flash 中的配置

**网络模式与回调**

> - `bk_wifi_mesh_set_net_mode()` \- 设置网络模式（广域网/局域网等）
> - `bk_wifi_mesh_set_api_mode()` \- 设置 API 模式及事件回调

**Mesh 配网**

> - `bk_wifi_mesh_get_idle_node()` \- 获取空闲节点列表
> - `bk_wifi_mesh_net_cfg()` \- 配置 Mesh 组网参数

**Mesh 网络构建**

> - `bk_wifi_mesh_config()` \- 配置 Mesh 参数（仅作用于单个节点，配网网络不使用）
> - `bk_wifi_mesh_start()` \- 启动 Mesh 节点（仅作用于单个节点，配网网络不使用）
> - `bk_wifi_mesh_stop()` \- 停止 Mesh 节点
> - `bk_wifi_mesh_status_info()` \- 获取 Mesh 节点链路状态
> - `bk_wifi_mesh_comm_mac_get()` \- 获取本机及根节点 MAC 地址
> - `bk_wifi_mesh_set_device_type()` \- 设置设备类型
> - `bk_wifi_mesh_get_device_type()` \- 获取设备类型
> - `bk_wifi_mesh_conn_rssi_thres_set()` \- 设置连接 RSSI 阈值
> - `bk_wifi_mesh_ap_specific_ssid_enable()` \- 启用各 Mesh AP 独立 SSID

**Mesh 网络控制**

> - `bk_wifi_mesh_get_topo()` \- 获取 Mesh 网络拓扑
> - `bk_wifi_mesh_add_node()` \- 添加节点到 Mesh 网络
> - `bk_wifi_mesh_remove_node()` \- 从 Mesh 网络移除节点
> - `bk_wifi_mesh_change_cfg()` \- 修改 Mesh 配置
> - `bk_wifi_mesh_conn_router()` \- 根节点连接路由器
> - `bk_wifi_mesh_reset_node()` \- 重置 Mesh 节点
> - `bk_wifi_mesh_reelect_enable()` \- 启用/禁用根节点掉电后重选

**Mesh 用户信息（Vendor）**

> - `bk_wifi_mesh_set_vendor_cb_reg()` \- 注册 set\_vendor 回调
> - `bk_wifi_mesh_get_vendor_cb_reg()` \- 注册 get\_vendor 回调
> - `bk_wifi_mesh_set_vendor()` \- 向指定节点下发用户数据
> - `bk_wifi_mesh_get_vendor()` \- 向指定节点请求用户数据

**Mesh OTA**

> - `bk_wifi_mesh_ota_start()` \- 发起 Mesh OTA 升级
> - `bk_wifi_mesh_ota_data_write()` \- 向根节点写入 OTA 固件数据（串口升级）
> - `bk_wifi_mesh_ota_finish()` \- 通知 OTA 固件下载完成
> - `bk_wifi_mesh_get_ota_state()` \- 获取 OTA 状态
> - `bk_wifi_mesh_ota_set_report_granularity()` \- 设置 OTA 进度上报粒度

**Mesh 数据传输**

> - `bk_wifi_mesh_data_send()` \- 向同一网络内节点发送单播数据
> - `bk_wifi_mesh_send_broadcast_data()` \- 发送广播数据
> - `bk_wifi_mesh_register_rcv_cb()` \- 注册单播数据接收回调
> - `bk_wifi_mesh_register_rcv_broadcast_cb()` \- 注册广播数据接收回调
> - `bk_wifi_mesh_send_data_use_base_rate()` \- 以基础速率（1 Mbps）发送数据

**Mesh 节点事件**

> - `bk_wifi_mesh_register_node_event_cb()` \- 注册节点事件回调

**其他**

> - `bk_wifi_mesh_enable_bcn_tx_by_high_rate()` \- 启用高速 beacon 发送
> - `bk_wifi_mesh_ap_add_vendor_ie()` \- 添加 SoftAP 的 Vendor Specific IE
> - `bk_wifi_mesh_register_read_user_flash_cb()` \- 注册读取用户 Flash 回调
> - `bk_wifi_mesh_set_free_ap_ssid()` \- 设置空闲节点 AP 的 SSID
> - `bk_wifi_mesh_set_free_ap_channel()` \- 设置空闲节点 AP 的信道
> - `bk_wifi_mesh_set_delay_time()` \- 设置各层级 Mesh 启动延迟时间

<a id="id1"></a>

## **主要结构体**

<a id="id3"></a>

配置类结构体


| 结构体 | 说明 |
| --- | --- |
| `bk_wifi_mesh_cfg_t` | Mesh 配置参数：mesh\_id、router\_ssid、ap\_ssid、max\_mesh\_conn\_num、max\_level 等 |
| `bk_wifi_mesh_net_cfg_t` | 组网配置：net\_token、node\_num、node\_mac\_list、router\_ssid、sap\_ssid、design\_root 等 |
| `bk_wifi_mesh_add_node_t` | 添加节点配置：node\_num、node\_mac\_list、design\_parent |
| `bk_wifi_mesh_change_cfg_t` | 修改配置：node\_num、node\_mac\_list、design\_parent、design\_root、max\_mesh\_num 等 |
| `bk_wifi_mesh_vendor_t` | 用户信息配置：node\_num、node\_mac\_list、vendor\_len、vendort\_ptr |
| `bk_wifi_mesh_ota_t` | OTA 配置：ota\_type、upgrade\_type、node\_num、node\_mac\_list、url\_ptr 等 |
| `bk_wifi_mesh_conn_router_t` | 连接路由器配置：node\_num、root\_mac、router\_ssid、router\_pw |
| `bk_wifi_mesh_reset_node_t` | 重置节点配置：node\_num、node\_mac\_list |

<a id="id4"></a>

状态与事件结构体


| 结构体 | 说明 |
| --- | --- |
| `bk_wifi_mesh_status_t` | 链路状态：state、level、link\_mesh\_num、parent\_mac 等 |
| `bk_wifi_mesh_connect_success_t` | 连接成功事件参数：mac、parent\_mac、level |
| `bk_wifi_mesh_connect_fail_t` | 连接失败事件参数：mac |
| `bk_wifi_mesh_disconn_t` | 断开连接事件参数：mac |
| `bk_wifi_mesh_child_connect_t` | 子节点连接事件参数：mac、child\_mac |
| `bk_wifi_mesh_child_disconn_t` | 子节点断开事件参数：mac、child\_mac |
| `bk_wifi_mesh_evt_cfg_t` | 组网/添加节点配置事件参数 |
| `bk_wifi_mesh_evt_ch_cfg_t` | 配置变更事件参数 |
| `bk_wifi_mesh_evt_vendor_t` | 用户信息事件参数：mac、vendor\_len、vendor\_info |
| `bk_wifi_mesh_evt_remove_t` | 删除节点事件参数：mac |
| `bk_wifi_mesh_ota_progress_t` | OTA 进度事件参数：is\_downloading、ota\_progress、ota\_rbl\_state |
| `bk_wifi_mesh_write_flash_t` | 写 Flash 事件参数：flash\_info、len |

<a id="id5"></a>

枚举类型


| 枚举 | 说明 |
| --- | --- |
| `bk_mesh_link_state_t` | 链路状态：未组网、组网中、已组网、恢复中等 |
| `bk_wifi_mesh_node_event_type_t` | 节点事件类型：连接成功/失败、断开、子节点连接/断开、首次组网、添加节点、set/get vendor、OTA 进度等 |
| `bk_wifi_mesh_net_event_t` | 网络事件类型：GET\_IDLE\_NODE、GET\_TOPO、RM\_NODE、GET\_VENDOR、CONN\_ROUTER、OTA\_FINISH |

<a id="id2"></a>

## **编程原则**

重要

使用 API 时请遵循以下原则：
:   - 配置结构体的保留字段请初始化为 0
    - 使用 BK\_ERR\_CHECK 检查 API 返回值
    - 若不确定如何使用 API，请先参考示例代码
    - 若不确定配置结构体字段如何初始化，可先使用默认配置宏（如 WIFI\_DEFAULT\_BK\_MESH\_NET\_CONFIG()）初始化，再设置应用相关字段
    - 事件回调中不宜执行耗时操作，建议将事件转发到应用任务处理

<a id="api"></a>

## **API 参考**

bk\_wifi\_mesh.h 路径：`components/bk_wifi_mesh/inc`

bk\_wifi\_mesh\_types.h 路径：`components/bk_wifi_mesh/inc`
