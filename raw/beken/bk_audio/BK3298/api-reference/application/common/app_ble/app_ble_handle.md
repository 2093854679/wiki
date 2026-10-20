---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ble/app_ble_handle.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ble-application-handle-functions"></a>

# BLE Application Handle Functions

<a id="app-ble-handle-api-brief"></a>

## APP\_BLE\_HANDLE API Brief

| Application | Brief |
| --- | --- |
| [`app_ble_handle_init()`](#_CPPv419app_ble_handle_initv "app_ble_handle_init") | Initialize the BLE application handles |

<a id="app-ble-handle-api-reference"></a>

## APP\_BLE\_HANDLE API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ble/app\_ble\_handle.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ble/app_ble_handle.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419app_ble_handle_initv"></a>

<a id="_CPPv319app_ble_handle_initv"></a> <a id="_CPPv219app_ble_handle_initv"></a> <a id="app_ble_handle_init__void"></a> <a id="app__ble__handle_8h_1a3d1b665edcce7b37ae886f034a1cea7e"></a> void app\_ble\_handle\_init(void)
:   Initialize the BLE application handles.

    Register a callback function for the BLE application to handle HCI events. Execute this before the APP task starts.

    返回:
    :   N/A

## 模块导航

- [快速入门](../../../../get-started.md)
- [API 参考手册](../../../../api-reference.md)
- [概述](../../../api_overview.md)
- [蓝牙应用层](../../../application.md)
- [BOOTROOM](../../bootrom.md)
- [COMMON](../../common.md)
- [APP_BT](../app_bt.md)
- [APP_BLE](../app_ble.md)
- [APP_AUDIO](../app_audio.md)
- [APP_COMPONENT](../app_component.md)
- [APP_ENV](../app_env.md)
- [APP_OTA](../app_ota.md)
- [APP_SYS](../app_sys.md)
- [APP_THREAD](../app_thread.md)
- [TWS](../../tws.md)
- [蓝牙介面层](../../../btif.md)
- [蓝牙音频代理层](../../../bt_audio_proxy.md)
- [中间件层](../../../component.md)
- [驱动层](../../../driver.md)
- [系统](../../../system.md)
- [开发者指南](../../../../developer-guide.md)
