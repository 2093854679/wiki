---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/bk7236/zh_CN/v2.0.1/examples/app_provisioning.html
sdk_family: bk_mesh
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="app"></a>

# APP配网示例

<a id="id1"></a>

## **概述**

本示例演示如何通过 **BK Wi-Fi Mesh APP** 对 Mesh 设备进行配网。配网逻辑由 APP 完成，设备端仅需完成 Mesh 初始化并注册必要的回调即可。用户通过手机 APP 完成组网、查看拓扑、添加/删除节点、OTA 等操作。

<a id="api"></a>

## **代码流程与 API 使用**

app\_provisioning 示例的设备端逻辑较为简单，配网由 APP 负责，设备端只需按以下顺序完成初始化：

<a id="id8"></a>

设备端初始化流程

```
+---------------------------+
|        bk_init()          |
+-------------+-------------+
              |
              v
+---------------------------+
|         注册回调          |
+-------------+-------------+
              |
              v
+---------------------------+
| bk_wifi_mesh_node_init()  |
+---------------------------+
```

1. `bk_init()` — 平台与驱动初始化。
2. **注册回调** — 节点事件与数据收发，步骤见下文 **API 调用顺序** 一节。
3. `bk_wifi_mesh_node_init()` — 启动 Mesh 节点，设备随后等待 APP 配网。

<a id="id2"></a>

## **API 调用顺序**

1. **bk\_wifi\_mesh\_enable\_bcn\_tx\_by\_high\_rate(true)**
   \- 当节点数超过 20 时建议启用高速 beacon 发送
2. **bk\_wifi\_mesh\_register\_node\_event\_cb(bk\_wifi\_mesh\_node\_event\_handler)**
   \- 注册节点事件回调，接收 CONNECT\_SUCCESS、DISCONNECT、OTA\_PROGRESS 等事件
3. **bk\_wifi\_mesh\_register\_rcv\_cb(bk\_wifi\_mesh\_rcv\_data\_handler)**
   \- 注册单播数据接收回调
4. **bk\_wifi\_mesh\_register\_rcv\_broadcast\_cb(bk\_wifi\_mesh\_rcv\_broadcast\_handler)**
   \- 注册广播数据接收回调
5. **bk\_wifi\_mesh\_node\_init()**
   \- 初始化 Mesh 节点，启动后等待 APP 配网

<a id="id3"></a>

## **节点事件回调说明**

<a id="id9"></a>

节点事件


| 事件类型 | 说明 |
| --- | --- |
| BK\_WIFI\_MESH\_NODE\_CONNECT\_SUCCESS | 节点连接成功 |
| BK\_WIFI\_MESH\_NODE\_CONNECT\_FAIL | 节点连接失败 |
| BK\_WIFI\_MESH\_NODE\_DISCONNECT | 节点断开连接 |
| BK\_WIFI\_MESH\_NODE\_CHILD\_CONNECT/DISCONNECT | 子节点连接/断开 |
| BK\_WIFI\_MESH\_NODE\_FIRST\_NET | 首次组网配置 |
| BK\_WIFI\_MESH\_NODE\_ADD\_NODE | 添加节点配置 |
| BK\_WIFI\_MESH\_NODE\_OTA\_PROGRESS | OTA 升级进度 |
| BK\_WIFI\_MESH\_NODE\_SET\_VENDOR/GET\_VENDOR | 用户信息下发/获取 |

<a id="id4"></a>

## **配网操作步骤（APP 侧）**

1. 所有节点上电
2. 打开 BK Mesh APP，选择「New group」
3. 按 APP 指引连接根节点或扫描设备完成组网
4. 进入群组后可查看拓扑、修改网络、添加节点、删除节点、OTA 升级

<a id="id5"></a>

## **项目结构**

```
app_provisioning/
├── main/armino_main.c    # 主程序：回调注册、节点初始化
└── ...
```

<a id="id6"></a>

## **编译与烧录**

```
make bk7236 PROJECT=examples/app_provisioning
```

<a id="id7"></a>

## **常见问题**

- 无法发现设备：执行 `bk_wifi_mesh_clear_flash()` 清除历史配网并重启
- 配网失败：核对路由器 SSID/密码，确认 2.4GHz 可用
- 多设备冲突：一次配网建议不超过 40 个节点
