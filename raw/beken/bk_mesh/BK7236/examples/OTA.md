---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/examples/OTA.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ota"></a>

# OTA 升级示例

<a id="id1"></a>

## **概述**

本示例演示 Mesh 组网成功后由根节点发起 OTA 升级。根节点需先完成组网（详见 no\_router 示例），再通过 URL 拉取方式发起 OTA；非根节点上电后等待入网，接收根节点 OTA 指令并执行升级。以下侧重介绍 OTA 相关流程与 API。

<a id="id2"></a>

## **代码流程**

**根节点流程**：初始化 → 组网（启动根节点、获取空闲节点、加入节点）→ **OTA（设置上报粒度、发起 OTA）**

**非根节点流程**：完成初始化后自动加入 Mesh，通过 `BK_WIFI_MESH_NODE_OTA_PROGRESS` 事件接收 OTA 进度并执行升级。

<a id="id6"></a>

根节点 OTA 相关流程（在组网完成之后）

```
① 初始化
       |
       v
② 组网（根节点拉网、空闲节点、加节点、拓扑确认）
       |
       v
③ ota_set_report_granularity（进度上报粒度）
       |
       v
④ bk_wifi_mesh_ota_start（按 URL 等方式发起 OTA）
```

1. **初始化** — 与 no\_router 相同，注册回调并完成节点初始化（见下文「公共初始化」小节）。
2. **组网** — 与 no\_router 相同，广域网模式下需配置路由器（见「组网过程」小节）。
3. **ota\_set\_report\_granularity** — 设置 OTA 进度上报粒度，便于根节点侧观察。
4. **bk\_wifi\_mesh\_ota\_start** — 由根节点发起整网或指定节点升级（见「OTA 过程」小节）。

<a id="api"></a>

## **API 使用说明**

**1\. 公共初始化**

与 no\_router 类似，需调用：`bk_wifi_mesh_enable_bcn_tx_by_high_rate`、`bk_wifi_mesh_register_node_event_cb`、`bk_wifi_mesh_register_rcv_cb`、`bk_wifi_mesh_register_rcv_broadcast_cb`、`bk_wifi_mesh_set_free_ap_ssid`、`bk_wifi_mesh_clear_flash`、`bk_wifi_mesh_node_init`、`bk_wifi_mesh_set_api_mode`。

本示例使用 `bk_wifi_mesh_set_net_mode(1)`，表示广域网模式（需连接路由器以访问 OTA URL）。

**2\. 组网过程**

组网流程与 no\_router 相同：根节点通过 `bk_wifi_mesh_net_cfg` 启动，再依次调用 `bk_wifi_mesh_get_idle_node`、`bk_wifi_mesh_add_node`、`bk_wifi_mesh_get_topo` 完成节点入网。本示例为广域网组网，config 中需填写 `router_ssid`、`router_pw`。具体说明请参考 no\_router 示例。

**3\. OTA 过程（根节点）**

<a id="id7"></a>

OTA 相关 API


| 序号 | API | 说明 |
| --- | --- | --- |
| 1 | `bk_wifi_mesh_ota_set_report_granularity(granularity)` | 设置 OTA 进度上报粒度（示例为 10%） |
| 2 | `bk_wifi_mesh_ota_start(&ota_cfg)` | 发起 OTA；`ota_type=1` 为云端/URL 拉取；`upgrade_type=0` 为全部升级；`url_ptr` 指向 `.rbl` 地址 |

**4\. OTA 配置 bk\_wifi\_mesh\_ota\_t**

<a id="id8"></a>

主要字段


| 字段 | 说明 |
| --- | --- |
| ota\_type | 1：Cloud/URL 拉取；2：APP 升级；3：串口升级 |
| upgrade\_type | 0：全部升级；1：单个节点；2：部分节点 |
| node\_num / node\_mac\_list | 升级目标节点列表（示例使用拓扑列表） |
| url\_ptr / url\_len | OTA 资源 URL（需设备可访问） |

**5\. 非根节点**

非根节点无需额外 API，收到根节点 OTA 指令后自动执行。进度通过 `BK_WIFI_MESH_NODE_OTA_PROGRESS` 事件上报，`is_downloading` 表示下载中，`ota_progress` 为进度百分比，`ota_rbl_state==0` 表示成功。

<a id="id3"></a>

## **OTA 方式对比**

<a id="id9"></a>

OTA 方式


| 方式 | ota\_type | 适用场景 |
| --- | --- | --- |
| Cloud upgrade | 1 | 广域网，需配置 router\_ssid/router\_pw |
| App upgrade | 2 | 局域网，配合 BK Mesh APP |
| Serial port upgrade | 3 | 通过串口将 .rbl 下载到根节点 |

<a id="id4"></a>

## **项目结构**

```
ota/main/armino_main.c
```

<a id="id5"></a>

## **编译与烧录**

```
make bk7236 PROJECT=examples/ota
```
