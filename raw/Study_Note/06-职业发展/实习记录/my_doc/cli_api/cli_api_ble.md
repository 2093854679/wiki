# BLE相关CLI命令与常用API速查

本笔记整理了projects/bluetooth下各例程main目录中注册的CLI命令，以及常用BLE API，便于开发和调试。

---

## gatt_server 例程
- **编译命令**：`make bk7236 PROJECT=bluetooth/gatt_server`
- **命令名**：`ble_gatts`
- **用法**：`ble_gatts 子命令 [参数]`
- **常用子命令示例**：
    - `ble_gatts help` —— 显示帮助信息和命令列表
    - `ble_gatts notify` —— 发送GATT通知（需先建立BLE连接）
    - `ble_gatts adv_en [1|0]` —— 启动(1)或停止(0)BLE广播
    - `ble_gatts bond` —— 建立BLE配对/绑定（需先建立BLE连接）
- **说明**：GATT Server相关操作，具体子命令和参数详见源码和help。

---

## gatt_client 例程
- **编译命令**：`make bk7236 PROJECT=bluetooth/gatt_client`
- **命令名**：`ble_gattc`
- **用法**：`ble_gattc 子命令 [参数]`
- **常用子命令示例**：
    - `ble_gattc help` —— 显示帮助信息和命令列表
    - `ble_gattc scan [1|0]` —— 开始(1)或停止(0)BLE扫描
    - `ble_gattc conn [addr]` —— 连接指定BLE设备
    - `ble_gattc disconn` —— 断开当前BLE连接
    - `ble_gattc notifyindcate_en [enable|disable] [desc_handle]` —— 使能/关闭通知或指示
    - `ble_gattc write [val_handle] [data]` —— 向指定句柄写数据
    - `ble_gattc read [val_handle]` —— 读取指定句柄数据
- **说明**：GATT Client相关操作，支持扫描、连接、读写等，具体子命令和参数详见源码和help。

---

## spp 例程
- **编译命令**：`make bk7236 PROJECT=bluetooth/spp`
- **命令名**：`spp`
- **用法**：`spp 子命令 [参数]`
- **常用子命令示例**：
    - `spp init` —— 初始化SPP
    - `spp deinit` —— 反初始化SPP
    - `spp conn [remote_addr]` —— 连接远端SPP设备
    - `spp disconn [remote_addr] [spp_handle]` —— 断开SPP连接
    - `spp start_server` —— 启动SPP服务端
    - `spp stop_server [local_channel]` —— 停止SPP服务端
    - `spp write [handle][data]` —— 发送数据
    - `spp rate [length]` —— 速率测试
    - `spp conn1 [remote_addr] [remote_channel]` —— 指定通道连接
- **说明**：SPP串口透传相关操作，具体子命令和参数详见源码和help。

---

## bt_hidd 例程
- **编译命令**：`make bk7236 PROJECT=bluetooth/bt_hidd`
- **命令名**：`bt_hidd`
- **用法**：`bt_hidd 子命令 [参数]`
- **常用子命令示例**：
    - `bt_hidd help` —— 显示帮助信息和命令列表
    - `bt_hidd key_report [key]` —— 发送按键报告
    - `bt_hidd unplug` —— 虚拟线缆断开
    - `bt_hidd disconnect` —— 断开HID连接
    - `bt_hidd connect [addr]` —— 连接指定蓝牙地址
- **说明**：HID Device相关操作，具体子命令和参数详见源码和help。

---

## mesh 例程
- **编译命令**：`make bk7236 PROJECT=bluetooth/mesh`
- **命令名**：`ble_mesh`
- **用法**：`ble_mesh 子命令 [参数]`
- **常用子命令示例**：
    - `ble_mesh provision init provisioner` —— 初始化为provisioner
    - `ble_mesh provision init provisionee` —— 初始化为provisionee
    - `ble_mesh provision send_count 1500` —— 发送指定数量数据
    - `ble_mesh led ...` —— 控制mesh灯相关功能
    - `ble_mesh tmall ...` —— 天猫精灵mesh相关
    - `ble_mesh shell mesh help` —— 进入mesh shell帮助
    - `ble_mesh shell bt help` —— 进入蓝牙shell帮助
    - `ble_mesh -h` —— 显示帮助信息
- **说明**：Mesh相关操作，具体子命令和参数详见源码和help。

---

## BLE常用API速查

### 1. BLE初始化与回调注册
- `bk_ble_init()` / `bk_ble_deinit()` —— 初始化/反初始化BLE协议栈
- `bk_ble_set_notice_cb(ble_notice_cb_t cb)` —— 注册BLE事件通知回调
- `bk_ble_register_app_sdp_charac_callback(app_sdp_charac_callback cb)` —— 注册GATT特征操作回调
- `bk_ble_register_app_sdp_common_callback(app_sdp_comm_callback cb)` —— 注册GATT数据库信息回调

### 2. GATT数据库与服务
- `bk_ble_create_db(struct bk_ble_db_cfg* ble_db_cfg)` —— 创建GATT数据库（服务/特征/描述符）
- `bk_ble_delete_service(struct bk_ble_db_cfg* ble_db_cfg)` —— 删除GATT服务

### 3. 广播与扫描
- `bk_ble_create_advertising()` / `bk_ble_delete_advertising()` —— 创建/删除广播
- `bk_ble_start_advertising()` / `bk_ble_stop_advertising()` —— 启动/停止广播
- `bk_ble_set_adv_data()` / `bk_ble_set_scan_rsp_data()` —— 设置广播/扫描响应数据
- `bk_ble_create_scaning()` / `bk_ble_delete_scaning()` —— 创建/删除扫描
- `bk_ble_start_scaning()` / `bk_ble_stop_scaning()` —— 启动/停止扫描

### 4. 连接与参数
- `bk_ble_create_init()` —— 创建主机连接
- `bk_ble_init_start_conn()` / `bk_ble_init_stop_conn()` —— 启动/停止主机连接
- `bk_ble_disconnect()` —— 断开连接
- `bk_ble_update_param()` —— 更新连接参数

### 5. GATT操作
- `bk_ble_send_noti_value()` —— 发送通知
- `bk_ble_send_ind_value()` —— 发送指示
- `bk_ble_gatt_write_value()` —— 写特征值
- `bk_ble_read_response_value()` —— 读特征值响应
- `bk_ble_gattc_read()` / `bk_ble_gattc_write()` —— 客户端读/写操作

### 6. 安全与配对
- `bk_ble_create_bond()` —— 发起配对/绑定
- `bk_ble_passkey_send()` —— 发送配对密钥
- `bk_ble_number_compare_send()` —— 发送数字比较确认

### 7. 其它常用API
- `bk_ble_get_mac()` —— 获取本地BLE MAC地址
- `bk_ble_appm_set_dev_name()` / `bk_ble_appm_get_dev_name()` —— 设置/获取设备名
- `bk_ble_read_phy()` / `bk_ble_set_phy()` —— 读/设置PHY参数
- `bk_ble_read_rssi()` —— 读取RSSI

### 8. 常用结构体与类型
- `ble_attm_desc_t` —— GATT数据库属性描述
- `ble_adv_param_t` —— 广播参数
- `ble_scan_param_t` —— 扫描参数
- `ble_conn_param_t` —— 连接参数
- `ble_notice_t` —— BLE事件类型
- `ble_cmd_cb_t` / `ble_notice_cb_t` —— 命令/事件回调类型

---

> 说明：
> - 以上命令和API均为常用BLE开发接口，具体参数和用法请参考头文件和官方文档。
> - 如需补充其它BLE相关CLI命令或API，请告知具体例程或接口。
