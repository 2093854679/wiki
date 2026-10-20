---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ble/app_bas.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="battery-application-handle-functions"></a>

# BATTERY Application Handle Functions

<a id="app-bas-api-brief"></a>

## APP\_BAS API Brief

| Application | Brief |
| --- | --- |
| [`app_bas_init()`](#_CPPv412app_bas_initv "app_bas_init") | Initialize BLE basery service (BAS) |
| [`_app_bas_update_batt_lvl()`](#_CPPv424_app_bas_update_batt_lvl7uint8_tb "_app_bas_update_batt_lvl") | BLE Battery Service (BAS) connection completed |

<a id="app-bas-api-reference"></a>

## APP\_BAS API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ble/app\_bas.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ble/app_bas.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412app_bas_initv"></a>

<a id="_CPPv312app_bas_initv"></a> <a id="_CPPv212app_bas_initv"></a> <a id="app_bas_init__void"></a> <a id="app__bas_8h_1a0479798870c96a6f270637fa31f2bf15"></a> void app\_bas\_init(void)
:   Initialize BLE battery service (BAS).

    Initialize and mount the BLE Battery Service (BAS).

    返回:
    :   N/A

<a id="_CPPv424_app_bas_update_batt_lvl7uint8_tb"></a>

<a id="_CPPv324_app_bas_update_batt_lvl7uint8_tb"></a> <a id="_CPPv224_app_bas_update_batt_lvl7uint8_tb"></a> <a id="_app_bas_update_batt_lvl__uint8_t.b"></a> <a id="app__bas_8h_1a661ed6c3965c86a4bbe4fba79b2db760"></a> void \_app\_bas\_update\_batt\_lvl(uint8\_t bat\_per, bool force\_update)
:   BLE Battery Service (BAS) connection completed.

    Launch the user’s battery application once the BLE Battery Service (BAS) connection is established.

    参数:
    :   - **bat\_per** – **\[in\]** battery percent value
        - **force\_update** – **\[in\]** force send notify to the remote device

    返回:
    :   N/A
