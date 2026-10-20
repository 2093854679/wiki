---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/api-reference/wifi/bk_wifi.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wi-fi-apis"></a>

# Wi-Fi APIs

重要

The WiFi API v2.0 is the lastest stable WiFi APIs, it’s used to deprecate the WiFi API v1.0. All new applications should use WiFi API v2.0.

<a id="wi-fi-interface"></a>

## Wi-Fi Interface

The BK WiFi Driver supports following logical WiFi interfaces:

> - BK STA interface
> - BK AP interface
> - BK Monitor interface

Each interface can be operated independently, so theretically all interfaces can be started independently. However because of performance and interference consideration, we limit the coexisting of some interfaces.

E.g. if the monitor interface is started, the starting of STA interface will fail, refer to API for detailed limitation of interface coexisting.

<a id="wi-fi-api-categories"></a>

## Wi-Fi API Categories

Most of WiFi APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk\_wifi, the APIs may be common for all interfaces or some interfaces, e.g. bk\_wifi\_init() etc.
> - Interface specific APIs.
>
>   The API name are prefixed with bk\_wifi\_interface, the interface can be sta, ap or monitor. e.g. bk\_wifi\_sta\_start() etc.
> - Module specific APIs
>
>   The API name are prefixed with bk\_wifi\_module, the module can be scan or filter etc, e.g. bk\_wifi\_scan\_start() etc. The API has no direct relationship with the interface, or the API caller don’t nedto care about on which interface the API is operated. E.g. the scan API can be based on STA interface, it can also based on AP interface, but the caller don’t care about it.

Common WiFi APIs:
:   - [`bk_wifi_init()`](#_CPPv412bk_wifi_initPK18wifi_init_config_t "bk_wifi_init") \- init WiFi
    - [`bk_wifi_deinit()`](#_CPPv414bk_wifi_deinitv "bk_wifi_deinit") \- deinit WiFi
    - [`bk_wifi_set_country()`](#_CPPv419bk_wifi_set_countryPK14wifi_country_t "bk_wifi_set_country") \- set country code
    - [`bk_wifi_get_country()`](#_CPPv419bk_wifi_get_countryP14wifi_country_t "bk_wifi_get_country") \- get country code
    - [`bk_wifi_send_raw()`](#_CPPv416bk_wifi_send_rawP7uint8_ti "bk_wifi_send_raw") \- send raw 802.11 frame

Interface specific WiFi APIs:
:   - [`bk_wifi_sta_start()`](#_CPPv417bk_wifi_sta_startv "bk_wifi_sta_start") \- start BK STA
    - [`bk_wifi_sta_stop()`](#_CPPv416bk_wifi_sta_stopv "bk_wifi_sta_stop") \- stop BK STA
    - [`bk_wifi_sta_set_config()`](#_CPPv422bk_wifi_sta_set_configPK17wifi_sta_config_t "bk_wifi_sta_set_config") \- set **basic** configurations BK STA, such as SSID etc
    - [`bk_wifi_sta_get_config()`](#_CPPv422bk_wifi_sta_get_configP17wifi_sta_config_t "bk_wifi_sta_get_config") \- get basic configuration of BK STA
    - [`bk_wifi_sta_get_linkstate_with_reason()`](#_CPPv437bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t "bk_wifi_sta_get_linkstate_with_reason") \- get actual link status of BK STA and reason code
    - [`bk_wifi_sta_get_link_status()`](#_CPPv427bk_wifi_sta_get_link_statusP18wifi_link_status_t "bk_wifi_sta_get_link_status") \- get link status of BK STA
    - [`bk_wifi_sta_connect()`](#_CPPv419bk_wifi_sta_connectv "bk_wifi_sta_connect") \- connect the BK STA to AP
    - [`bk_wifi_sta_disconnect()`](#_CPPv422bk_wifi_sta_disconnectv "bk_wifi_sta_disconnect") \- disconnect the Wi-Fi connection
    - [`bk_wifi_sta_pm_enable()`](#_CPPv421bk_wifi_sta_pm_enablev "bk_wifi_sta_pm_enable") \- enable STA power management
    - [`bk_wifi_sta_pm_disable()`](#_CPPv422bk_wifi_sta_pm_disablev "bk_wifi_sta_pm_disable") \- disable STA power management
    - [`bk_wifi_get_channel()`](#_CPPv419bk_wifi_get_channelv "bk_wifi_get_channel") \- get current channel ID
    - [`bk_wifi_set_mac_address()`](#_CPPv423bk_wifi_set_mac_addressPc "bk_wifi_set_mac_address") \- set Wi-Fi MAC address
    - [`bk_wifi_manual_cal_rfcali_status()`](#_CPPv432bk_wifi_manual_cal_rfcali_statusv "bk_wifi_manual_cal_rfcali_status") \- get Wi-Fi Calibration status
    - [`bk_wifi_ap_start()`](#_CPPv416bk_wifi_ap_startv "bk_wifi_ap_start") \- start BK AP
    - [`bk_wifi_ap_stop()`](#_CPPv415bk_wifi_ap_stopv "bk_wifi_ap_stop") \- stop BK AP
    - [`bk_wifi_ap_set_config()`](#_CPPv421bk_wifi_ap_set_configPK16wifi_ap_config_t "bk_wifi_ap_set_config") \- set the **basic** configuration of BK AP, such as SSID etc
    - [`bk_wifi_ap_get_config()`](#_CPPv421bk_wifi_ap_get_configP16wifi_ap_config_t "bk_wifi_ap_get_config") \- get the basic configuration of BK AP
    - [`bk_wifi_ap_get_sta_list()`](#_CPPv423bk_wifi_ap_get_sta_listP14wlan_ap_stas_t "bk_wifi_ap_get_sta_list") \- get the STAs connected to BK AP
    - [`bk_wifi_sta_get_mac()`](#_CPPv419bk_wifi_sta_get_macP7uint8_t "bk_wifi_sta_get_mac") \- get STA MAC address
    - [`bk_wifi_ap_get_mac()`](#_CPPv418bk_wifi_ap_get_macP7uint8_t "bk_wifi_ap_get_mac") \- get AP MAC address
    - [`bk_wifi_monitor_start()`](#_CPPv421bk_wifi_monitor_startv "bk_wifi_monitor_start") \- start the monitor
    - [`bk_wifi_monitor_stop()`](#_CPPv420bk_wifi_monitor_stopv "bk_wifi_monitor_stop") \- stop the monitor
    - [`bk_wifi_monitor_set_config()`](#_CPPv426bk_wifi_monitor_set_configPK21wifi_monitor_config_t "bk_wifi_monitor_set_config") \- set **basic** configuration of the monitor
    - [`bk_wifi_monitor_get_config()`](#_CPPv426bk_wifi_monitor_get_configP21wifi_monitor_config_t "bk_wifi_monitor_get_config") \- get basic configuration of the monitor
    - [`bk_wifi_monitor_register_cb()`](#_CPPv427bk_wifi_monitor_register_cbK17wifi_monitor_cb_t "bk_wifi_monitor_register_cb") \- register monitor callback function
    - [`bk_wifi_monitor_set_channel()`](#_CPPv427bk_wifi_monitor_set_channelPK14wifi_channel_t "bk_wifi_monitor_set_channel") \- set the channel of monitor
    - [`bk_wifi_send_listen_interval_req()`](#_CPPv432bk_wifi_send_listen_interval_req7uint8_t "bk_wifi_send_listen_interval_req") \- set the listen interval

Module Specific WiFi APIs:
:   - `bk_wifi_scan_register_cb()` \- register scan callback function
    - [`bk_wifi_scan_start()`](#_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t "bk_wifi_scan_start") \- start the scan
    - [`bk_wifi_scan_stop()`](#_CPPv417bk_wifi_scan_stopv "bk_wifi_scan_stop") \- stop the scan
    - [`bk_wifi_scan_get_result()`](#_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t "bk_wifi_scan_get_result") \- get the scan result
    - [`bk_wifi_scan_dump_result()`](#_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t "bk_wifi_scan_dump_result") \- dump the scan result
    - [`bk_wifi_scan_free_result()`](#_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t "bk_wifi_scan_free_result") \- dump the scan result
    - [`bk_wifi_filter_set_config()`](#_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t "bk_wifi_filter_set_config") \- set filter configuration
    - [`bk_wifi_filter_register_cb()`](#_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t "bk_wifi_filter_register_cb") \- register the filter callback function

<a id="compatibility-and-extension"></a>

## Compatibility and Extension

The WiFi APIs are flexible, easy to be extended and backward compatible. For most of the WiFi configurations, we put some reserved fields in the config struct for future extension. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.

<a id="programing-principle"></a>

## Programing Principle

重要

Here is some general principle for WiFi API users:
:   - Always init the reserved fields of config struct to 0
    - Use BK\_ERR\_CHECK to check the return value of the WiFi API
    - If you are not sure how to use WiFi APIs, study the WiFi example code first
    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields, e.g. use WIFI\_DEFAULT\_INIT\_CONFIG() to init wifi\_config\_t first.
    - Don’t do too much work in WiFi event callback, relay the event to your own application task.

<a id="user-development-model"></a>

## User Development Model

Similar as most popular WiFi driver, the Beken WiFi driver is implemented as event driver. The application call WiFi APIs to operate the WiFi driver and get notified by WiFi event.

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [wifi.h](https://github.com/bekencorp/armino/blob/main/components/wifi.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_wifi_initPK18wifi_init_config_t"></a>

<a id="_CPPv312bk_wifi_initPK18wifi_init_config_t"></a> <a id="_CPPv212bk_wifi_initPK18wifi_init_config_t"></a> <a id="bk_wifi_init__wifi_init_config_tCP"></a> <a id="group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_init(const [wifi\_init\_config\_t](#_CPPv418wifi_init_config_t "wifi_init_config_t") \*init\_config)
:   This API initializes the WiFi driver, e.g. creating task for supplicant, allocating resource for low level WiFi driver etc.

    Usage example:

    ```
     wifi_init_config_t init_config = WIFI_DEFAULT_INIT_CONFIG();
     BK_LOG_ON_ERR(bk_wifi_init(&init_config);
    ```

    **Attention**
    :   1\. This API is the 1st API that should be called before any other WiFi API can be called.

    **Attention**
    :   2\. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414bk_wifi_deinitv"></a>

<a id="_CPPv314bk_wifi_deinitv"></a> <a id="_CPPv214bk_wifi_deinitv"></a> <a id="bk_wifi_deinit__void"></a> <a id="group__bk__api__wifi__v2_1ga7e6332a6b55a560bb276e9637465bb07"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_deinit(void)
:   Deinit the BK WiFi driver.

    This API free all resources related to WiFi.

    **Attention**
    :   1\. This API is not ready yet, will support in future release.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NOT\_SUPPORT: The API is not supported yet.
        - others: other errors.

<a id="_CPPv417bk_wifi_sta_startv"></a>

<a id="_CPPv317bk_wifi_sta_startv"></a> <a id="_CPPv217bk_wifi_sta_startv"></a> <a id="bk_wifi_sta_start__void"></a> <a id="group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_start(void)
:   Start the BK STA.

    This API init the resoure specific to BK STA, e.g. init STA specific globals, init the supplicant and STA specific WiFi driver etc.

    **Attention**
    :   1\. Make sure the [bk\_wifi\_sta\_set\_config()](#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94) are succeedful before calling this API.

    **Attention**
    :   2\. This API connect the BK STA to the configured AP automatically.

    **Attention**
    :   3\. If the BK STA is already started, this API ignores the request and returns BK\_OK. if you want to restart the BK STA, call [bk\_wifi\_sta\_stop()](#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b) first and then call this API.

    **Attention**
    :   4\. TODO description about fast connection

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_STA\_NOT\_CONFIG: the BK STA is not configured.
        - BK\_ERR\_WIFI\_MONITOR\_IP: the BK STA can’t be started because monitor is started.
        - others: other errors.

<a id="_CPPv422bk_wifi_sta_split_initv"></a>

<a id="_CPPv322bk_wifi_sta_split_initv"></a> <a id="_CPPv222bk_wifi_sta_split_initv"></a> <a id="bk_wifi_sta_split_init__void"></a> <a id="group__bk__api__wifi__v2_1gadf61d1522e3aab6fc44cba1e77f70941"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_split\_init(void)
:   Init the BK STA.

    This API init is splited form bk\_wifi\_sta\_start.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_wifi_sta_split_startv"></a>

<a id="_CPPv323bk_wifi_sta_split_startv"></a> <a id="_CPPv223bk_wifi_sta_split_startv"></a> <a id="bk_wifi_sta_split_start__void"></a> <a id="group__bk__api__wifi__v2_1ga27c179288130a5b2e2d7be040fdcb61c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_split\_start(void)
:   Start the BK STA.

    This API start is splited form bk\_wifi\_sta\_start.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_wifi_sta_split_connectv"></a>

<a id="_CPPv325bk_wifi_sta_split_connectv"></a> <a id="_CPPv225bk_wifi_sta_split_connectv"></a> <a id="bk_wifi_sta_split_connect__void"></a> <a id="group__bk__api__wifi__v2_1ga91167ec716581e1b7e9990c601f9874e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_split\_connect(void)
:   Connect the BK STA.

    This API connect is splited form bk\_wifi\_sta\_start.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_wifi_sta_stopv"></a>

<a id="_CPPv316bk_wifi_sta_stopv"></a> <a id="_CPPv216bk_wifi_sta_stopv"></a> <a id="bk_wifi_sta_stop__void"></a> <a id="group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_stop(void)
:   Stop the BK STA.

    **Attention**
    :   This API causes the BK STA disconnect from the AP, it similar as [bk\_wifi\_sta\_disconnect()](#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11), but this API may free resource.

    返回
    :   - BK\_OK: succeed
        - BK\_FAIL: fail

<a id="_CPPv417bk_wifi_scan_stopv"></a>

<a id="_CPPv317bk_wifi_scan_stopv"></a> <a id="_CPPv217bk_wifi_scan_stopv"></a> <a id="bk_wifi_scan_stop__void"></a> <a id="group__bk__api__wifi__v2_1gac82b880ed9021836162aca4aebd4c3e0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_scan\_stop(void)
:   Stop the pure scan operation.

    **Attention**
    :   This API causes the BK STA disconnect from the AP, it similar as [bk\_wifi\_sta\_disconnect()](#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11), but this API may free resource.

    返回
    :   - BK\_OK: succeed
        - BK\_FAIL: fail

<a id="_CPPv422bk_wifi_sta_set_configPK17wifi_sta_config_t"></a>

<a id="_CPPv322bk_wifi_sta_set_configPK17wifi_sta_config_t"></a> <a id="_CPPv222bk_wifi_sta_set_configPK17wifi_sta_config_t"></a> <a id="bk_wifi_sta_set_config__wifi_sta_config_tCP"></a> <a id="group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_set\_config(const [wifi\_sta\_config\_t](#_CPPv417wifi_sta_config_t "wifi_sta_config_t") \*sta\_config)
:   Config the BK STA.

    This API configures the basic configurations of the BK STA, it should be called before we call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) to start the BK STA. It can also be used to update the configuration after the BK STA is started.

    Usage example:

    ```
    wifi_sta_config_t sta_config = WIFI_DEFAULT_STA_CONFIG();

    os_strncpy(sta_config.ssid, "ssid", WIFI_SSID_STR_LEN);
    os_strncpy(sta_config.password, "password", WIFI_PASSWORD_LEN);
    //more initialization here
    BK_LOG_ON_ERR(bk_wifi_sta_set_config(&sta_config));
    ```

    **Attention**
    :   1\. Don’t call this API when the monitor is in-progress

    **Attention**
    :   2\. If STA is already connected to AP, this API cases BK STA reconnects the AP.

    **Attention**
    :   3\. Make sure the reserved fields in sta\_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    **Attention**
    :   4\. Auto reconnect max count and timeout can be set. When user app receives EVENT\_WIFI\_STA\_DISCONNECTED event, it’s user app’s responsibility to reconnect to AP manually. Max count and timeout set to zero to let supplicant automatically handles connection without user app’s interaction.

    参数
    :   **sta\_config** – the STA configuration

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: the STA is not initialized, call [bk\_wifi\_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226) first.
        - BK\_ERR\_NULL\_PARAM: parameter config is NULL.
        - BK\_ERR\_WIFI\_RESERVED\_FIELD: the reserved field of config is not 0\.
        - others: other errors

<a id="_CPPv422bk_wifi_sta_get_configP17wifi_sta_config_t"></a>

<a id="_CPPv322bk_wifi_sta_get_configP17wifi_sta_config_t"></a> <a id="_CPPv222bk_wifi_sta_get_configP17wifi_sta_config_t"></a> <a id="bk_wifi_sta_get_config__wifi_sta_config_tP"></a> <a id="group__bk__api__wifi__v2_1gabd063029cb792bd168970dd1f8dd06b3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_get\_config([wifi\_sta\_config\_t](#_CPPv417wifi_sta_config_t "wifi_sta_config_t") \*sta\_config)
:   Get the configuration of the BK STA.

    参数
    :   **sta\_config** – store the BK STA configuration

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL.
        - BK\_ERR\_WIFI\_STA\_NOT\_CONFIG: STA is not configured yet.
        - others: other errors

<a id="_CPPv437bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t"></a>

<a id="_CPPv337bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t"></a> <a id="_CPPv237bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t"></a> <a id="bk_wifi_sta_get_linkstate_with_reason__wifi_linkstate_reason_tP"></a> <a id="group__bk__api__wifi__v2_1ga80b3efdbbca7a35ac7bdfb38546b8ccb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_get\_linkstate\_with\_reason([wifi\_linkstate\_reason\_t](#_CPPv423wifi_linkstate_reason_t "wifi_linkstate_reason_t") \*info)
:   Get the WiFi station state of the BK STA.

    - If sta is idle or connected, reason code will be WIFI\_REASON\_MAX

    **Attention**
    :   the difference between this API and [bk\_wifi\_sta\_get\_link\_status()](#group__bk__api__wifi__v2_1ga05fa3da4689980df705e03c6416df12e) is

        - This API gets the actual WiFi STA link status and reason code

    参数
    :   **state** – store the WiFi station state of the BK STA

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL.
        - others: other errors

<a id="_CPPv427bk_wifi_sta_get_link_statusP18wifi_link_status_t"></a>

<a id="_CPPv327bk_wifi_sta_get_link_statusP18wifi_link_status_t"></a> <a id="_CPPv227bk_wifi_sta_get_link_statusP18wifi_link_status_t"></a> <a id="bk_wifi_sta_get_link_status__wifi_link_status_tP"></a> <a id="group__bk__api__wifi__v2_1ga05fa3da4689980df705e03c6416df12e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_get\_link\_status([wifi\_link\_status\_t](#_CPPv418wifi_link_status_t "wifi_link_status_t") \*link\_status)
:   Get the WiFi link info of the BK STA.

    Get the actual WiFi link status of the BK STA.

    **Attention**
    :   the difference between this API and [bk\_wifi\_sta\_get\_config()](#group__bk__api__wifi__v2_1gabd063029cb792bd168970dd1f8dd06b3) is

        - This API gets the actual STA link info while the later gets the configured value
        - This API can get more info of the link, such as RSSI, WiFi link status, AID etc.
        - The AID is only valid if @link\_status-\>state is WIFI\_LINK\_CONNECTED.

    参数
    :   **link\_status** – store the WiFi link status of the BK STA

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter link\_info is NULL.
        - BK\_ERR\_WIFI\_DRIVER: WiFi low level driver has failure.
        - BK\_ERR\_WIFI\_NO\_MEM: Not enough memory
        - others: other errors

<a id="_CPPv419bk_wifi_sta_connectv"></a>

<a id="_CPPv319bk_wifi_sta_connectv"></a> <a id="_CPPv219bk_wifi_sta_connectv"></a> <a id="bk_wifi_sta_connect__void"></a> <a id="group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_connect(void)
:   Connect the BK STA to the AP.

    **Attention**
    :   1\. Make sure STA is started by [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) before calling this API.

    **Attention**
    :   2\. Don’t call this API when the monitor is in-progress

    **Attention**
    :   3\. If STA is already connected to AP, this API reconnects the BK STA.

    **Attention**
    :   4\. TODO \- multiple same SSID connect???

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_STA\_NOT\_STARTED: the STA is not started, call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) first.
        - BK\_ERR\_WIFI\_MONITOR\_IP: the API is not allowed because monitor is in-progress.
        - others: other failures.

<a id="_CPPv422bk_wifi_sta_disconnectv"></a>

<a id="_CPPv322bk_wifi_sta_disconnectv"></a> <a id="_CPPv222bk_wifi_sta_disconnectv"></a> <a id="bk_wifi_sta_disconnect__void"></a> <a id="group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_disconnect(void)
:   Disconnect the WiFi connection of the BK STA.

    **Attention**
    :   TODO \- add description about disconnect event!

    返回
    :   - BK\_OK: succeed
        - others: other failures.

<a id="_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t"></a>

<a id="_CPPv318bk_wifi_scan_startPK18wifi_scan_config_t"></a> <a id="_CPPv218bk_wifi_scan_startPK18wifi_scan_config_t"></a> <a id="bk_wifi_scan_start__wifi_scan_config_tCP"></a> <a id="group__bk__api__wifi__v2_1gaf4b85a984fa5c5d633769274a50b5b9c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_scan\_start(const [wifi\_scan\_config\_t](#_CPPv418wifi_scan_config_t "wifi_scan_config_t") \*scan\_config)
:   Start a scan.

    This API notifies the WiFi driver to start a scan, the event EVENT\_WIFI\_SCAN\_DONE will be raised if the scan is completed. General steps to use this API:

    - prepare the scan done event callback, the callback can call [bk\_wifi\_scan\_get\_result()](#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc) to get the scan result and then call [bk\_wifi\_scan\_free\_result()](#group__bk__api__wifi__v2_1ga75df3c75b3bd8844e9e68c8e339859b6) to free the resource.
    - call bk\_event\_register\_cb(EVENT\_MOD\_WIFI, EVENT\_WIFI\_SCAN\_DONE, …) to register scan done event callback.
    - call this API to trigger this the scan.

    Usage example:

    ```
    //Define your scan done handler
    int scan_done_handler(void *arg, event_module_t event_module, int event_id, void *event_data)
    {
        wifi_scan_result_t scan_result = {0};

        BK_LOG_ON_ERR(bk_wifi_scan_get_result(&scan_result));
        bk_wifi_scan_dump_result(&scan_result);
        bk_wifi_scan_free_result(&scan_result);

        return BK_OK;
    }

    //Start the scan
    wifi_scan_config_t config = {0};

    BK_LOG_ON_ERR(bk_event_register_cb(EVENT_MOD_WIFI, EVENT_WIFI_SCAN_DONE, scan_done_handler, NULL));
    BK_LOG_ON_ERR(bk_wifi_scan_start(&scan_config));
    ```

    **Attention**
    :   1\. This API triggers an active scan on all channels (TODO double check)

    **Attention**
    :   2\. Pass NULL scan\_config to scan all APs, otherwise scan the SSID specified in scan\_config.ssid

    **Attention**
    :   3\. Make sure the reserved fields in scan\_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    **Attention**
    :   4\. TODO scan result limits???

    参数
    :   **scan\_config** – the configuration of scan

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: the STA is not initialized, call [bk\_wifi\_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226) first.
        - BK\_ERR\_WIFI\_MONITOR\_IP: the API is not allowed because monitor is in-progress.
        - others: other failures.

<a id="_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t"></a>

<a id="_CPPv323bk_wifi_scan_get_resultP18wifi_scan_result_t"></a> <a id="_CPPv223bk_wifi_scan_get_resultP18wifi_scan_result_t"></a> <a id="bk_wifi_scan_get_result__wifi_scan_result_tP"></a> <a id="group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_scan\_get\_result([wifi\_scan\_result\_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") \*scan\_result)
:   Get the scan result.

    Usage example:

    ```
    wifi_scan_result_t scan_result = {0};

    BK_LOG_ON_ERR(bk_wifi_scan_get_result(&scan_result));
    bk_wifi_scan_free_result(&scan_result);
    ```

    **Attention**
    :   1\. The caller don’t need to allocate memory for scan\_result-\>aps, this API will allocate the memory for scan\_result-\>aps according to the actual found AP number.

    **Attention**
    :   2\. Don’t forget to call bk\_wifi\_scan\_free\_result(\&scan\_result) to free the the resource allocated in this API, otherwise memory leak.

    参数
    :   **scan\_result** – store the scan result

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: NULL scan\_result
        - BK\_ERR\_NO\_MEM: out of memory
        - others: other failures

<a id="_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t"></a>

<a id="_CPPv324bk_wifi_scan_dump_resultPK18wifi_scan_result_t"></a> <a id="_CPPv224bk_wifi_scan_dump_resultPK18wifi_scan_result_t"></a> <a id="bk_wifi_scan_dump_result__wifi_scan_result_tCP"></a> <a id="group__bk__api__wifi__v2_1gaf4eee514ca5fa831a6d403bdb838efa7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_scan\_dump\_result(const [wifi\_scan\_result\_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") \*scan\_result)
:   Dump the scan result.

    参数
    :   **scan\_result** – The scan result to be dumped.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PARAM: invalid scan result

<a id="_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t"></a>

<a id="_CPPv324bk_wifi_scan_free_resultP18wifi_scan_result_t"></a> <a id="_CPPv224bk_wifi_scan_free_resultP18wifi_scan_result_t"></a> <a id="bk_wifi_scan_free_result__wifi_scan_result_tP"></a> <a id="group__bk__api__wifi__v2_1ga75df3c75b3bd8844e9e68c8e339859b6"></a> void bk\_wifi\_scan\_free\_result([wifi\_scan\_result\_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") \*scan\_result)
:   Free the scan result.

    **Attention**
    :   This API free scan\_result-\>aps which allocated in [bk\_wifi\_scan\_get\_result()](#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc), it doesn’t free scan\_result. So if scan\_result is allocated by the caller, the caller need to free it.

    参数
    :   **scan\_result** – The scan result to be freed.

    返回
    :   - BK\_OK: always succeed

<a id="_CPPv429bk_wlan_sta_set_wireless_mode7uint8_t7uint8_t"></a>

<a id="_CPPv329bk_wlan_sta_set_wireless_mode7uint8_t7uint8_t"></a> <a id="_CPPv229bk_wlan_sta_set_wireless_mode7uint8_t7uint8_t"></a> <a id="bk_wlan_sta_set_wireless_mode__uint8_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1gacdec1f1b20022cb7515d491813f3800b"></a> void bk\_wlan\_sta\_set\_wireless\_mode(uint8\_t mode\_24g, uint8\_t mode\_5g)
:   Set the wireless mode for the WLAN station.

    备注

    This API configures both 2.4G and 5G station wireless modes.

    参数
    :   - **mode\_24g** – The desired 2.4G wireless mode, one of WIFI\_STA\_HW\_MODE\_B/B\_G/B\_G\_N/B\_G\_N\_AX
        - **mode\_5g** – The desired 5G wireless mode, one of WIFI\_STA\_HW\_MODE\_A/A\_N/A\_N\_AC/A\_N\_AC\_AX

<a id="_CPPv428bk_wlan_sta_set_retry_config7uint8_t8uint16_t7uint8_t8uint16_t7uint8_t"></a>

<a id="_CPPv328bk_wlan_sta_set_retry_config7uint8_t8uint16_t7uint8_t8uint16_t7uint8_t"></a> <a id="_CPPv228bk_wlan_sta_set_retry_config7uint8_t8uint16_t7uint8_t8uint16_t7uint8_t"></a> <a id="bk_wlan_sta_set_retry_config__uint8_t.uint16_t.uint8_t.uint16_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga2405f2a52ed9e2e2d72dcad7d202164e"></a> void bk\_wlan\_sta\_set\_retry\_config(uint8\_t auth\_retry, uint16\_t auth\_retry\_interval, uint8\_t assoc\_retry, uint16\_t assoc\_retry\_interval, uint8\_t eapol\_2\_retry)
:   Set the retry configuration for the WLAN station.

    Configure authentication/association retry counts and intervals for the STA.

    参数
    :   - **auth\_retry** – Authentication retry count
        - **auth\_retry\_interval** – Authentication retry interval (unit: 100 ms)
        - **assoc\_retry** – Association retry count
        - **assoc\_retry\_interval** – Association retry interval (unit: 100 ms)
        - **eapol\_2\_retry** – EAPOL-2 retry count

<a id="_CPPv430bk_wlan_sta_get_tx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a>

<a id="_CPPv330bk_wlan_sta_get_tx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a> <a id="_CPPv230bk_wlan_sta_get_tx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a> <a id="bk_wlan_sta_get_tx_frame_count__uint32_tP.uint32_tP.uint32_tP"></a> <a id="group__bk__api__wifi__v2_1ga5d2d98ea857650db690b8497f6a7beed"></a> void bk\_wlan\_sta\_get\_tx\_frame\_count(uint32\_t \*tx\_total\_num, uint32\_t \*tx\_dropped\_num, uint32\_t \*tx\_data\_num)
:   Get the TX frame statistics of the WLAN station.

    This API retrieves the total number of transmitted frames, the number of dropped frames, and the number of transmitted data frames for the STA interface.

    备注

    The counters are typically reset on Wi-Fi initialization or STA start.

    参数
    :   - **tx\_total\_num** – **\[out\]** Pointer to store the total number of transmitted frames
        - **tx\_dropped\_num** – **\[out\]** Pointer to store the number of dropped frames
        - **tx\_data\_num** – **\[out\]** Pointer to store the number of transmitted data frames

<a id="_CPPv430bk_wlan_sta_get_rx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a>

<a id="_CPPv330bk_wlan_sta_get_rx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a> <a id="_CPPv230bk_wlan_sta_get_rx_frame_countP8uint32_tP8uint32_tP8uint32_t"></a> <a id="bk_wlan_sta_get_rx_frame_count__uint32_tP.uint32_tP.uint32_tP"></a> <a id="group__bk__api__wifi__v2_1gaf910c9ec065f2ee9852edfb0ef435b30"></a> void bk\_wlan\_sta\_get\_rx\_frame\_count(uint32\_t \*rx\_total\_num, uint32\_t \*rx\_dropped\_num, uint32\_t \*rx\_data\_num)
:   Get the RX frame statistics of the WLAN station.

    This API retrieves the total number of received frames, the number of dropped frames, and the number of received data frames for the STA interface.

    备注

    The counters are typically reset on Wi-Fi initialization or STA start.

    参数
    :   - **rx\_total\_num** – **\[out\]** Pointer to store the total number of received frames
        - **rx\_dropped\_num** – **\[out\]** Pointer to store the number of dropped frames
        - **rx\_data\_num** – **\[out\]** Pointer to store the number of received data frames

<a id="_CPPv425bk_wifi_sta_add_vendor_ie7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv325bk_wifi_sta_add_vendor_ie7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv225bk_wifi_sta_add_vendor_ie7uint8_tP7uint8_t7uint8_t"></a> <a id="bk_wifi_sta_add_vendor_ie__uint8_t.uint8_tP.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga25b95ae1a74d886532f705319f1cc015"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_add\_vendor\_ie(uint8\_t frame, uint8\_t \*vsie, uint8\_t len)
:   Add/Update/Del STA’s Vendor Specific IE **before** connect to AP.

    **Attention**
    :   If you want to add vsie when sta starts, just initialize [wifi\_sta\_config\_t](#structwifi__sta__config__t) when call [bk\_wifi\_sta\_set\_config()](#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94).

    参数
    :   - **buf** – vsie buf
        - **len** – vsie buf len

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv428bk_wifi_sta_update_vendor_ie7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv328bk_wifi_sta_update_vendor_ie7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv228bk_wifi_sta_update_vendor_ie7uint8_tP7uint8_t7uint8_t"></a> <a id="bk_wifi_sta_update_vendor_ie__uint8_t.uint8_tP.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga1f7834c37e0b43e89aaa17f3c1226fa9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_update\_vendor\_ie(uint8\_t frame, uint8\_t \*vsie, uint8\_t len)

<a id="_CPPv425bk_wifi_sta_del_vendor_ie7uint8_t"></a>

<a id="_CPPv325bk_wifi_sta_del_vendor_ie7uint8_t"></a> <a id="_CPPv225bk_wifi_sta_del_vendor_ie7uint8_t"></a> <a id="bk_wifi_sta_del_vendor_ie__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga4cf14b2234ba6e83aedc62ac825da03d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_del\_vendor\_ie(uint8\_t frame)

<a id="_CPPv416bk_wifi_ap_startv"></a>

<a id="_CPPv316bk_wifi_ap_startv"></a> <a id="_CPPv216bk_wifi_ap_startv"></a> <a id="bk_wifi_ap_start__void"></a> <a id="group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_start(void)
:   Start the BK AP.

    This API init the resoure specific to BK AP, e.g. init BK AP specific globals, init the hostapd and AP specific WiFi driver etc.

    If the BK AP is already started, this API ignores the request and returns BK\_OK, we can call [bk\_wifi\_ap\_stop()](#group__bk__api__wifi__v2_1ga1836b0aeeb20668e861bad0baa2ea0d3) to stop BK AP first and then call [bk\_wifi\_ap\_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5) to restart it.

    **Restart** AP Usage example:

    ```
    BK_LOG_ON_ERR(bk_wifi_ap_stop());
    BK_LOG_ON_ERR(bk_wifi_ap_start());
    ```

    **Attention**
    :   1\. Don’t call this API when the monitor is in-progress

    **Attention**
    :   2\. If [bk\_wifi\_ap\_set\_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39) is not called, this API start the AP with default value, normally you should configure the AP first before calling this API.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_AP\_NOT\_CONFIG: the WiFi AP is not configured, call [bk\_wifi\_ap\_set\_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39) first.
        - others: other errors

<a id="_CPPv415bk_wifi_ap_stopv"></a>

<a id="_CPPv315bk_wifi_ap_stopv"></a> <a id="_CPPv215bk_wifi_ap_stopv"></a> <a id="bk_wifi_ap_stop__void"></a> <a id="group__bk__api__wifi__v2_1ga1836b0aeeb20668e861bad0baa2ea0d3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_stop(void)
:   Stop the BK AP.

    返回
    :   - BK\_OK: succeed
        - BK\_WIFI\_NOT\_INIT: the WiFi is not initialized, call [bk\_wifi\_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226) first.
        - others: other errors

<a id="_CPPv421bk_wifi_ap_set_configPK16wifi_ap_config_t"></a>

<a id="_CPPv321bk_wifi_ap_set_configPK16wifi_ap_config_t"></a> <a id="_CPPv221bk_wifi_ap_set_configPK16wifi_ap_config_t"></a> <a id="bk_wifi_ap_set_config__wifi_ap_config_tCP"></a> <a id="group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_set\_config(const [wifi\_ap\_config\_t](#_CPPv416wifi_ap_config_t "wifi_ap_config_t") \*ap\_config)
:   Config the BK AP.

    Usage example:

    ```
    wifi_ap_config_t ap_config = WIFI_DEFAULT_AP_CONFIG();

    os_strncpy(ap_config.ssid, "ssid", WIFI_SSID_STR_LEN);
    os_strncpy(ap_config.password, "password", WIFI_PASSWORD_LEN);
    BK_LOG_ON_ERR(bk_wifi_ap_set_config(&ap_config));
    ```

    **Attention**
    :   1\. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    参数
    :   **ap\_config** – the AP configuration

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the ap\_config is NULL.
        - others: other errors

<a id="_CPPv421bk_wifi_ap_get_configP16wifi_ap_config_t"></a>

<a id="_CPPv321bk_wifi_ap_get_configP16wifi_ap_config_t"></a> <a id="_CPPv221bk_wifi_ap_get_configP16wifi_ap_config_t"></a> <a id="bk_wifi_ap_get_config__wifi_ap_config_tP"></a> <a id="group__bk__api__wifi__v2_1ga932494dcee096896906446086d82649b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_get\_config([wifi\_ap\_config\_t](#_CPPv416wifi_ap_config_t "wifi_ap_config_t") \*ap\_config)
:   Get the configuration of the BK AP.

    参数
    :   **ap\_config** – store the configuration of BK AP

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL.
        - others: other errors

<a id="_CPPv423bk_wifi_ap_get_sta_listP14wlan_ap_stas_t"></a>

<a id="_CPPv323bk_wifi_ap_get_sta_listP14wlan_ap_stas_t"></a> <a id="_CPPv223bk_wifi_ap_get_sta_listP14wlan_ap_stas_t"></a> <a id="bk_wifi_ap_get_sta_list__wlan_ap_stas_tP"></a> <a id="group__bk__api__wifi__v2_1ga3c4500ec7dd69bf6d5b344f0ca22b330"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_get\_sta\_list([wlan\_ap\_stas\_t](#_CPPv414wlan_ap_stas_t "wlan_ap_stas_t") \*stas)
:   Get the STAs connected to BK AP.

    **Attention**
    :   Free stas-\>sta after usage.

    参数
    :   **stas** – store the STA list in BK AP

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv418wlan_ap_sta_deauthP7uint8_ti"></a>

<a id="_CPPv318wlan_ap_sta_deauthP7uint8_ti"></a> <a id="_CPPv218wlan_ap_sta_deauthP7uint8_ti"></a> <a id="wlan_ap_sta_deauth__uint8_tP.i"></a> <a id="group__bk__api__wifi__v2_1gab6a2b6bcd16a308d9389e4952c2b921d"></a> int wlan\_ap\_sta\_deauth(uint8\_t \*mac, int reason\_code)
:   De-authenticate a specific station associated to the BK AP.

    This API sends a de-authentication frame to the specified STA and removes it from the associated STA list of the AP.

    参数
    :   - **mac** – Pointer to the MAC address of the station to be de-authenticated
        - **reason\_code** – Reason code for de-authentication

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv422wlan_ap_deauth_all_stav"></a>

<a id="_CPPv322wlan_ap_deauth_all_stav"></a> <a id="_CPPv222wlan_ap_deauth_all_stav"></a> <a id="wlan_ap_deauth_all_sta__void"></a> <a id="group__bk__api__wifi__v2_1gaa2cf7877f9fed1c2cd2411ffbea36484"></a> int wlan\_ap\_deauth\_all\_sta(void)
:   De-authenticate all stations currently associated to the BK AP.

    This API sends a de-authentication frame to every associated STA and clears the entire associated STA list of the AP.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_sta_get_signal_infoP18wifi_signal_info_t"></a>

<a id="_CPPv327bk_wifi_sta_get_signal_infoP18wifi_signal_info_t"></a> <a id="_CPPv227bk_wifi_sta_get_signal_infoP18wifi_signal_info_t"></a> <a id="bk_wifi_sta_get_signal_info__wifi_signal_info_tP"></a> <a id="group__bk__api__wifi__v2_1ga1ad179d6ff66fe4546d65291e9e44982"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_get\_signal\_info([wifi\_signal\_info\_t](#_CPPv418wifi_signal_info_t "wifi_signal_info_t") \*signal\_info)
:   Get the signal information of the connected AP.

    参数
    :   **signal\_info** – store the signal information of the connected AP

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv421bk_wifi_calculate_pmkPKcPKcPc"></a>

<a id="_CPPv321bk_wifi_calculate_pmkPKcPKcPc"></a> <a id="_CPPv221bk_wifi_calculate_pmkPKcPKcPc"></a> <a id="bk_wifi_calculate_pmk__cCP.cCP.cP"></a> <a id="group__bk__api__wifi__v2_1ga12b1db14c57293e05e32a7ec1047883a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_calculate\_pmk(const char \*ssid, const char \*pwd, char \*pmk)
:   Calculate softap’s Pmk when softap is starts.

    参数
    :   - **ssid** – softap’s ssid
        - **pwd** – softap’s pwd
        - **pmk** – softap’s pmk

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_ap_add_vendor_iePv7uint8_t"></a>

<a id="_CPPv324bk_wifi_ap_add_vendor_iePv7uint8_t"></a> <a id="_CPPv224bk_wifi_ap_add_vendor_iePv7uint8_t"></a> <a id="bk_wifi_ap_add_vendor_ie__voidP.uint8_t"></a> <a id="group__bk__api__wifi__v2_1gabe2ffb072255ac1f6a7bd3e271aa904a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_add\_vendor\_ie(void \*buf, uint8\_t len)
:   Add softap’s Vendor Specific IE when softap is running.

    **Attention**
    :   If you want to add vsie when softap starts, just initialize [wifi\_ap\_config\_t](#structwifi__ap__config__t) when call [bk\_wifi\_ap\_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5).

    参数
    :   - **buf** – vsie buf
        - **len** – vsie buf len

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_ap_del_vendor_iev"></a>

<a id="_CPPv324bk_wifi_ap_del_vendor_iev"></a> <a id="_CPPv224bk_wifi_ap_del_vendor_iev"></a> <a id="bk_wifi_ap_del_vendor_ie__void"></a> <a id="group__bk__api__wifi__v2_1ga8fdeff9c4e3ad6180eb74bafc452ca62"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_del\_vendor\_ie(void)
:   Delete softap’s Vendor Specific IE when softap is running.

    **Attention**
    :   If you want to add vsie when softap starts, just initialize [wifi\_ap\_config\_t](#structwifi__ap__config__t) when call [bk\_wifi\_ap\_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5).

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv428bk_wifi_ap_update_hidden_capb"></a>

<a id="_CPPv328bk_wifi_ap_update_hidden_capb"></a> <a id="_CPPv228bk_wifi_ap_update_hidden_capb"></a> <a id="bk_wifi_ap_update_hidden_cap__b"></a> <a id="group__bk__api__wifi__v2_1ga178bace6234723471c6d00b671a998ca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_update\_hidden\_cap(bool flag)
:   Update softap’s Hidden Ssid Capaility when softap is running.

    - BK\_OK: succeed
    - others: other errors

    **Attention**
    :   If you want to update hidden ssid capability when softap starts, just call [bk\_wifi\_ap\_update\_hidden\_cap()](#group__bk__api__wifi__v2_1ga178bace6234723471c6d00b671a998ca).

    参数
    :   **flag** – set true for hidden ssid

    返回

<a id="_CPPv421bk_wifi_monitor_startv"></a>

<a id="_CPPv321bk_wifi_monitor_startv"></a> <a id="_CPPv221bk_wifi_monitor_startv"></a> <a id="bk_wifi_monitor_start__void"></a> <a id="group__bk__api__wifi__v2_1gafb67a0a2f743a9dbf65904a0a685a26f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_start(void)
:   Start the monitor.

    **Attention**
    :   1\. When monitor mode is enabled, the scan will not work and [bk\_wifi\_scan\_start()](#group__bk__api__wifi__v2_1gaf4b85a984fa5c5d633769274a50b5b9c) returns BK\_ERR\_WIFI\_MONITOR\_IP.

    **Attention**
    :   2\. When monitor mode is enabled, the STA connect will not work and [bk\_wifi\_sta\_connect()](#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06) returns BK\_ERR\_WIFI\_MONITOR\_IP.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv420bk_wifi_monitor_stopv"></a>

<a id="_CPPv320bk_wifi_monitor_stopv"></a> <a id="_CPPv220bk_wifi_monitor_stopv"></a> <a id="bk_wifi_monitor_stop__void"></a> <a id="group__bk__api__wifi__v2_1ga64895e925025cb2b891abbf4f4608ab4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_stop(void)
:   Stop the monitor.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv426bk_wifi_monitor_set_configPK21wifi_monitor_config_t"></a>

<a id="_CPPv326bk_wifi_monitor_set_configPK21wifi_monitor_config_t"></a> <a id="_CPPv226bk_wifi_monitor_set_configPK21wifi_monitor_config_t"></a> <a id="bk_wifi_monitor_set_config__wifi_monitor_config_tCP"></a> <a id="group__bk__api__wifi__v2_1ga5bfbda3bbaa90a4ff3daa19e9acbbb3f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_set\_config(const [wifi\_monitor\_config\_t](#_CPPv421wifi_monitor_config_t "wifi_monitor_config_t") \*monitor\_config)
:   Configure the monitor.

    参数
    :   **monitor\_config** – the configuration of monitor

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv426bk_wifi_monitor_get_configP21wifi_monitor_config_t"></a>

<a id="_CPPv326bk_wifi_monitor_get_configP21wifi_monitor_config_t"></a> <a id="_CPPv226bk_wifi_monitor_get_configP21wifi_monitor_config_t"></a> <a id="bk_wifi_monitor_get_config__wifi_monitor_config_tP"></a> <a id="group__bk__api__wifi__v2_1ga6013fd42f04c9acbee9a60ba1cc00fe5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_get\_config([wifi\_monitor\_config\_t](#_CPPv421wifi_monitor_config_t "wifi_monitor_config_t") \*monitor\_config)
:   Get the configuration of the monitor.

    参数
    :   **monitor\_config** – store the configuration of monitor

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_monitor_register_cbK17wifi_monitor_cb_t"></a>

<a id="_CPPv327bk_wifi_monitor_register_cbK17wifi_monitor_cb_t"></a> <a id="_CPPv227bk_wifi_monitor_register_cbK17wifi_monitor_cb_t"></a> <a id="bk_wifi_monitor_register_cb__wifi_monitor_cb_tC"></a> <a id="group__bk__api__wifi__v2_1ga61920d478aa5884503b20874337d62bb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_register\_cb(const [wifi\_monitor\_cb\_t](#_CPPv417wifi_monitor_cb_t "wifi_monitor_cb_t") monitor\_cb)
:   Register the user callback of monitor.

    参数
    :   **monitor\_cb** – monitor callback

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_monitor_set_channelPK14wifi_channel_t"></a>

<a id="_CPPv327bk_wifi_monitor_set_channelPK14wifi_channel_t"></a> <a id="_CPPv227bk_wifi_monitor_set_channelPK14wifi_channel_t"></a> <a id="bk_wifi_monitor_set_channel__wifi_channel_tCP"></a> <a id="group__bk__api__wifi__v2_1gae2ba858f657a0e9dbb9fe594a83e0e87"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_set\_channel(const [wifi\_channel\_t](#_CPPv414wifi_channel_t "wifi_channel_t") \*chan)
:   Set monitor channel.

    **Attention**
    :   1\. Currently we only support HT20, chan-\>second should always be 0\.

    **Attention**
    :   2\. This API is only used for settting monitor channel, NOT for other purpose.

    **Attention**
    :   3\. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.

    **Attention**
    :   4\. The channel range can be set is from channel 1 to channel 14,

    参数
    :   **chan** – channel of monitor

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv435bk_wifi_monitor_set_channel_bondingPK14wifi_channel_t"></a>

<a id="_CPPv335bk_wifi_monitor_set_channel_bondingPK14wifi_channel_t"></a> <a id="_CPPv235bk_wifi_monitor_set_channel_bondingPK14wifi_channel_t"></a> <a id="bk_wifi_monitor_set_channel_bonding__wifi_channel_tCP"></a> <a id="group__bk__api__wifi__v2_1gae0c81796ca6f4ba0c66565f1185515ab"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_set\_channel\_bonding(const [wifi\_channel\_t](#_CPPv414wifi_channel_t "wifi_channel_t") \*chan)
:   Set monitor channel bonding.

    **Attention**
    :   1\. This API will bond the monitor channel with the given channel.

    **Attention**
    :   2\. This API is only used for settting monitor channel, NOT for other purpose.

    **Attention**
    :   3\. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.

    **Attention**
    :   4\. The channel range can be set is from channel 1 to channel 14,

    参数
    :   **chan** – channel of monitor

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv422bk_wifi_monitor_resumev"></a>

<a id="_CPPv322bk_wifi_monitor_resumev"></a> <a id="_CPPv222bk_wifi_monitor_resumev"></a> <a id="bk_wifi_monitor_resume__void"></a> <a id="group__bk__api__wifi__v2_1gab6679fbb4ae72b047ec3b535a69661c3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_resume(void)
:   resume the monitor to wakeup Wi-Fi from sleep mode

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv423bk_wifi_monitor_suspendv"></a>

<a id="_CPPv323bk_wifi_monitor_suspendv"></a> <a id="_CPPv223bk_wifi_monitor_suspendv"></a> <a id="bk_wifi_monitor_suspend__void"></a> <a id="group__bk__api__wifi__v2_1gac579e95b5dd742c3cb349eff26a666bb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_monitor\_suspend(void)
:   suspend the monitor to allow Wi-Fi can goto sleep mode

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv417bk_wifi_twt_setup7uint8_t8uint16_t7uint8_t"></a>

<a id="_CPPv317bk_wifi_twt_setup7uint8_t8uint16_t7uint8_t"></a> <a id="_CPPv217bk_wifi_twt_setup7uint8_t8uint16_t7uint8_t"></a> <a id="bk_wifi_twt_setup__uint8_t.uint16_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga5def7b7b5e3cdb6a2e0c85b4aabe202d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_twt\_setup(uint8\_t setup\_type, uint16\_t mantissa, uint8\_t min\_twt)
:   twt set up

    参数
    :   - **setup\_type** – suggest/demand
        - **mantissa** – wake\_int\_mantissa
        - **min\_twt** – min\_twt\_wake\_dur

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv420bk_wifi_twt_teardownv"></a>

<a id="_CPPv320bk_wifi_twt_teardownv"></a> <a id="_CPPv220bk_wifi_twt_teardownv"></a> <a id="bk_wifi_twt_teardown__void"></a> <a id="group__bk__api__wifi__v2_1ga1e37ef1e6e1b3082152d2fe87b462916"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_twt\_teardown(void)
:   twt tear down

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t"></a>

<a id="_CPPv325bk_wifi_filter_set_configPK20wifi_filter_config_t"></a> <a id="_CPPv225bk_wifi_filter_set_configPK20wifi_filter_config_t"></a> <a id="bk_wifi_filter_set_config__wifi_filter_config_tCP"></a> <a id="group__bk__api__wifi__v2_1gad89834d0bcf579fe0ac338cb0fcf3d21"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_filter\_set\_config(const [wifi\_filter\_config\_t](#_CPPv420wifi_filter_config_t "wifi_filter_config_t") \*filter\_config)
:   Set the filter configuration.

    The filter is used to configure what kind of management packets can be received by the filter callback registered by [bk\_wifi\_filter\_register\_cb()](#group__bk__api__wifi__v2_1ga0276b4fd054e03c62f79e0b52b1870c0).

    Per the WiFi receiving data path, the management frames are firstly received by WiFi hardware, then the hardware relays them to WiFi software (WiFi driver). Normally the hardware receives all management frames in the air, however it don’t relay all of them to WiFi driver (WiFi software), it only relays management frames necessary to STA or AP or scan or monitor, depends on which interface or function are enabled. In other word, WiFi driver only receives management frames necessary to them from hardware.

    When no filter callback is registered, all management frame processing is ended in WiFi driver unless the filter callback is registered.

    If filter callback is register and if filter\_config.rx\_all\_default\_mgmt is set to 1, then all the management frames received by WiFi driver are relayed to the filter callback. **Notified that the default management frame types can be received depends on whether STA or AP or scan or monitor are enabled or not, e.g. when only STA is enabled, the WiFi driver needs to handle PROBE response, but don’t need to handle PROBE request, so the WiFi driver only receive PROBE response from WiFi hardware**.

    Here is summary about default management frame received by WiFi:

    | Condition | Default management frame |
    | --- | --- |
    | STA connected | Management frames sent by the connected AP, such as beacon etc. |
    | AP started | Management frames sent by connected STA and probe request etc. |
    | Scan starting | Probe response and beacon frames of all APs. |
    | Monitor started | All kind of management frames |

    How about if the filter callback wants to receive more management frame types, e.g. want to receive PROBE request when only STA is enabled. We can set filter\_config-\>rx\_probe\_req to receive PROBE response no matter whether AP is enabled or NOT.

    Usage example:

    ```
    // Only receive management frame default received by WiFi driver
    // Equal to the case when bk_wifi_filter_set_config() is not called
    wifi_filter_config_t filter_config = WIFI_DEFAULT_FILTER_CONFIG();
    BK_LOG_ON_ERR(bk_wifi_filter_set_config(&filter_config);

    // Receive all beacon and management frames default received by WiFi driver
    filter_config.rx_all_beacon = 1;
    BK_LOG_ON_ERR(bk_wifi_filter_set_config(&filter_config);

    // Only receive all beacon
    filter_config.rx_all_beacon = 1;
    filter_config.rx_all_default_mgmt = 0;
    BK_LOG_ON_ERR(bk_wifi_filter_set_config(&filter_config);
    ```

    **Attention**
    :   1\. If this API is not called, the default filter is to relay all mamangement frames received by WiFi driver to the filter callback.

    **Attention**
    :   2\. If STA is enabled, the WiFi driver only receives beacon from the connected AP, if scan is enabled or filter\_config-\>rx\_all\_beacon is set, the WiFi driver receives beacons of all APs.

    参数
    :   **filter\_config** – configuration of filter

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv425bk_wifi_filter_get_configP20wifi_filter_config_t"></a>

<a id="_CPPv325bk_wifi_filter_get_configP20wifi_filter_config_t"></a> <a id="_CPPv225bk_wifi_filter_get_configP20wifi_filter_config_t"></a> <a id="bk_wifi_filter_get_config__wifi_filter_config_tP"></a> <a id="group__bk__api__wifi__v2_1ga5fc10f022beb010273cdece352634daf"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_filter\_get\_config([wifi\_filter\_config\_t](#_CPPv420wifi_filter_config_t "wifi_filter_config_t") \*filter\_config)
:   Get the filter configuration.

    参数
    :   **filter\_config** – store configuration of filter

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t"></a>

<a id="_CPPv326bk_wifi_filter_register_cbK16wifi_filter_cb_t"></a> <a id="_CPPv226bk_wifi_filter_register_cbK16wifi_filter_cb_t"></a> <a id="bk_wifi_filter_register_cb__wifi_filter_cb_tC"></a> <a id="group__bk__api__wifi__v2_1ga0276b4fd054e03c62f79e0b52b1870c0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_filter\_register\_cb(const [wifi\_filter\_cb\_t](#_CPPv416wifi_filter_cb_t "wifi_filter_cb_t") filter\_cb)
:   Register the filter user callback.

    **Attention**
    :   1\. If the monitor is enabled, the management packets received by filter callback can also be received by monitor callback. If this is not what we want, we can disable filter when enabling monitor, or disable monitor when enabling filter.

    **Attention**
    :   2\. During WiFi scan, the filter also works.

    **Attention**
    :   3\. Pass NULL callback or set all fields of filter\_config to 0 to disable the filter.

    **Attention**
    :   4\. The memory used to hold the frame buffer and frame\_info will be freed immediately when the callback is returned, so don’t relay them to other task. Make a copy of them and then relay to other task if necessary.

    **Attention**
    :   5\. Don’t do too much work in the filter callback because it’s called in WiFi driver core thread, otherwise it may impact the WiFi performance.

    参数
    :   **filter\_cb** – the filter user callback

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv419bk_wifi_sta_get_macP7uint8_t"></a>

<a id="_CPPv319bk_wifi_sta_get_macP7uint8_t"></a> <a id="_CPPv219bk_wifi_sta_get_macP7uint8_t"></a> <a id="bk_wifi_sta_get_mac__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga2f4c7d2ddf5b64c341a8afcf67a1c739"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_get\_mac(uint8\_t \*mac)
:   Get the MAC of BK STA.

    **Attention**
    :   1\. The AP’s MAC is derived from the base MAC of the system.

    **Attention**
    :   2\. If you want to change the MAC of AP, call bk\_set\_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK STA

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv418bk_wifi_ap_get_macP7uint8_t"></a>

<a id="_CPPv318bk_wifi_ap_get_macP7uint8_t"></a> <a id="_CPPv218bk_wifi_ap_get_macP7uint8_t"></a> <a id="bk_wifi_ap_get_mac__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga10793928908208140565121eca953d90"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_get\_mac(uint8\_t \*mac)
:   Get the MAC of BK AP.

    **Attention**
    :   1\. The AP’s MAC is derived from the base MAC of the system.

    **Attention**
    :   2\. If you want to change the MAC of AP, call bk\_set\_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK AP

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv416bk_wifi_send_rawP7uint8_ti"></a>

<a id="_CPPv316bk_wifi_send_rawP7uint8_ti"></a> <a id="_CPPv216bk_wifi_send_rawP7uint8_ti"></a> <a id="bk_wifi_send_raw__uint8_tP.i"></a> <a id="group__bk__api__wifi__v2_1ga292217fd7679b25131b8c55826d84907"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_raw(uint8\_t \*buffer, int len)
:   Send raw 802.11 frame.

    **Attention**
    :   1\. This API can be used in WiFi station, softap, or monitor mode.

    **Attention**
    :   2\. Only support to send non-QoS frame.

    **Attention**
    :   3\. The frame sequence will be overwritten by WiFi driver.

    **Attention**
    :   4\. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **buffer** – raw 802.11 frame
        - **len** – the length of the 802.11 frame

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv419bk_wifi_send_raw_exP18wifi_raw_tx_info_tPvPv"></a>

<a id="_CPPv319bk_wifi_send_raw_exP18wifi_raw_tx_info_tPvPv"></a> <a id="_CPPv219bk_wifi_send_raw_exP18wifi_raw_tx_info_tPvPv"></a> <a id="bk_wifi_send_raw_ex__wifi_raw_tx_info_tP.voidP.voidP"></a> <a id="group__bk__api__wifi__v2_1ga2bcf71fcfd0f9b74607340f64b657277"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_raw\_ex([wifi\_raw\_tx\_info\_t](#_CPPv418wifi_raw_tx_info_t "wifi_raw_tx_info_t") \*raw\_tx, void \*cb, void \*param)
:   Send raw 802.11 frame.

    **Attention**
    :   1\. This API can be used in WiFi station, softap, or monitor mode.

    **Attention**
    :   2\. Only support to send non-QoS frame.

    **Attention**
    :   3\. The frame sequence will be overwritten by WiFi driver.

    **Attention**
    :   4\. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw\_tx** – raw tx information, refer to struct [wifi\_raw\_tx\_info\_t](#structwifi__raw__tx__info__t)
        - **cb** – send status call back
        - **param** – send status call back paramter

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv422bk_wifi_send_tx_raw_exP18wifi_raw_tx_info_tPvPv"></a>

<a id="_CPPv322bk_wifi_send_tx_raw_exP18wifi_raw_tx_info_tPvPv"></a> <a id="_CPPv222bk_wifi_send_tx_raw_exP18wifi_raw_tx_info_tPvPv"></a> <a id="bk_wifi_send_tx_raw_ex__wifi_raw_tx_info_tP.voidP.voidP"></a> <a id="group__bk__api__wifi__v2_1ga2e18c3929fb874dd01aa1e850de94bca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_tx\_raw\_ex([wifi\_raw\_tx\_info\_t](#_CPPv418wifi_raw_tx_info_t "wifi_raw_tx_info_t") \*raw\_tx, void \*cb, void \*param)
:   Send raw 802.11 tx frame.

    **Attention**
    :   1\. This API can be used in WiFi station, softap, or monitor mode.

    **Attention**
    :   2\. Only support to send non-QoS frame.

    **Attention**
    :   3\. The frame sequence will be overwritten by WiFi driver.

    **Attention**
    :   4\. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw\_tx** – raw tx information, refer to struct [wifi\_raw\_tx\_info\_t](#structwifi__raw__tx__info__t)
        - **cb** – send status call back
        - **param** – send status call back paramter

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv429bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a>

<a id="_CPPv329bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a> <a id="_CPPv229bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a> <a id="bk_wifi_set_tx_raw_rate_power__uint32_t.uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga2650d71604e350578fc8c18fb5ea3d00"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_rate\_power(uint32\_t rate, uint32\_t power)
:   Update raw 802.11 frame TX rate and power.

    参数
    :   - **rate** – TX rate control
        - **power** – TX power control

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv421bk_wifi_set_tx_raw_ac7uint8_t"></a>

<a id="_CPPv321bk_wifi_set_tx_raw_ac7uint8_t"></a> <a id="_CPPv221bk_wifi_set_tx_raw_ac7uint8_t"></a> <a id="bk_wifi_set_tx_raw_ac__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga51eb1e9e836d29a1a6726d69037d1faa"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_ac(uint8\_t ac)
:   Update raw 802.11 frame TX AC.

    参数
    :   **ac** – TX AC

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv426bk_wifi_set_tx_raw_timeout8uint16_t"></a>

<a id="_CPPv326bk_wifi_set_tx_raw_timeout8uint16_t"></a> <a id="_CPPv226bk_wifi_set_tx_raw_timeout8uint16_t"></a> <a id="bk_wifi_set_tx_raw_timeout__uint16_t"></a> <a id="group__bk__api__wifi__v2_1gac9081dbb8aa6a9d63abaedfd70149b03"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_timeout(uint16\_t timeout\_ms)
:   Update raw 802.11 frame TX timeout.

    参数
    :   **timeout\_ms** – TX timeout in ms

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv427bk_wifi_set_wifi_media_modeb"></a>

<a id="_CPPv327bk_wifi_set_wifi_media_modeb"></a> <a id="_CPPv227bk_wifi_set_wifi_media_modeb"></a> <a id="bk_wifi_set_wifi_media_mode__b"></a> <a id="group__bk__api__wifi__v2_1ga9fc185f0df5a7d412408e8c397c076a8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_wifi\_media\_mode(bool flag)
:   Configure wifi multimedia mode when the multimedia is running.

    This API is used to configure multimedia mode of Wi-Fi. Multimedia mode can enchance video fluency and make a better experience of video.

    **Attention**
    :   1\. If you want to running multimedia mode,please configure this flag when open and close multimedia mode.

    **Attention**
    :   2\. Please set this flag before running multimedia and clear this flag after closing multimedia.

    **Attention**
    :   3\. If the flag is set when multimedia is turned on and it is not cleared after multimedia is turned off,the Wi-Fi will not be able to enter ps mode.

    参数
    :   **flag** – set true if you want to enable multimedia mode.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv434bk_wifi_get_wifi_media_mode_configPb"></a>

<a id="_CPPv334bk_wifi_get_wifi_media_mode_configPb"></a> <a id="_CPPv234bk_wifi_get_wifi_media_mode_configPb"></a> <a id="bk_wifi_get_wifi_media_mode_config__bP"></a> <a id="group__bk__api__wifi__v2_1ga6d0e5d4612540151a95e4fa2feedf33b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_wifi\_media\_mode\_config(bool \*flag)
:   get wifi media mode configuration

    参数
    :   **flag** – store configuration of wifi media mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL
        - others: other errors

<a id="_CPPv425bk_wifi_set_video_quality7uint8_t"></a>

<a id="_CPPv325bk_wifi_set_video_quality7uint8_t"></a> <a id="_CPPv225bk_wifi_set_video_quality7uint8_t"></a> <a id="bk_wifi_set_video_quality__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga6293cddbc6a8c7ad79d708a678c8c22a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_video\_quality(uint8\_t quality)
:   Configure video quality when the video is running.

    This API is used to configure video quality.There are three mode to choose:

    Fluent definition(FD): The video transmission is relatively stable and has strong anti-interference ability,which can ensure the stable video transmission in a complex enviroment;

    Standard definition(SD):The video transmission is stable in a clean environment and is slightly stuck in a complex environment,which transmission bandwidth is improved;

    High definition(HD):The video transmission gives priority to high speed which can transmit high-bandwidth data in a clean environment, but the video transmission is relatively stuck in a complex environment;

    The default value is HD mode when the video is running.

    **Attention**
    :   1\. If you want to running video mode,please configure this parameter when open video mode.

    **Attention**
    :   2\. Please configure this parameter before running video mode.

    **Attention**
    :   3\. Please configure bk\_wifi\_set\_wifi\_media\_mode(flag) before useing this API.

    参数
    :   **quality** – set the video quality when the video is running. Three mode can be choose: 0-FD,1-SD,2-HD,default is HD.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv432bk_wifi_get_video_quality_configP7uint8_t"></a>

<a id="_CPPv332bk_wifi_get_video_quality_configP7uint8_t"></a> <a id="_CPPv232bk_wifi_get_video_quality_configP7uint8_t"></a> <a id="bk_wifi_get_video_quality_config__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1gaac857413097ced726e8071fed659d6c6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_video\_quality\_config(uint8\_t \*quality)
:   get video quality configuration

    参数
    :   **quality** – store configuration of video quality

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL
        - others: other errors

<a id="_CPPv422bk_wifi_set_default_ac8uint32_t"></a>

<a id="_CPPv322bk_wifi_set_default_ac8uint32_t"></a> <a id="_CPPv222bk_wifi_set_default_ac8uint32_t"></a> <a id="bk_wifi_set_default_ac__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga11967a6b5f2781897003fe24955a4f2e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_default\_ac(uint32\_t ac)
:   Configure defalut AC.

    This API is used to configure default AC,rang in \[0 3\]

    参数
    :   **ac** – set default AC rang in \[0 3\]

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv422bk_wifi_get_default_acP8uint32_t"></a>

<a id="_CPPv322bk_wifi_get_default_acP8uint32_t"></a> <a id="_CPPv222bk_wifi_get_default_acP8uint32_t"></a> <a id="bk_wifi_get_default_ac__uint32_tP"></a> <a id="group__bk__api__wifi__v2_1gaf8341bcaf566a9a50e34c855c6f56023"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_default\_ac(uint32\_t \*ac)
:   get default AC

    参数
    :   **ac** – store default AC

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: the parameter config is NULL
        - others: other errors

<a id="_CPPv425bk_wifi_set_scan_5g_firstb"></a>

<a id="_CPPv325bk_wifi_set_scan_5g_firstb"></a> <a id="_CPPv225bk_wifi_set_scan_5g_firstb"></a> <a id="bk_wifi_set_scan_5g_first__b"></a> <a id="group__bk__api__wifi__v2_1gacac547023dfeadff4e612c8e6158d504"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_scan\_5g\_first(bool enable)
:   Enable/disable prioritizing 5G channels during station scan.

    参数
    :   **enable** – true to scan 5G channels first, false to keep normal order.

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv425bk_wifi_get_scan_5g_firstPb"></a>

<a id="_CPPv325bk_wifi_get_scan_5g_firstPb"></a> <a id="_CPPv225bk_wifi_get_scan_5g_firstPb"></a> <a id="bk_wifi_get_scan_5g_first__bP"></a> <a id="group__bk__api__wifi__v2_1ga4f4bdf6a39ee3c00100fb348421b21a6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_scan\_5g\_first(bool \*enable)
:   Get current 5G-first scan configuration.

    参数
    :   **enable** – output flag, true means scan 5G channels first.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: parameter is NULL
        - others: other errors

<a id="_CPPv421bk_wifi_get_tx_raw_acP7uint8_t"></a>

<a id="_CPPv321bk_wifi_get_tx_raw_acP7uint8_t"></a> <a id="_CPPv221bk_wifi_get_tx_raw_acP7uint8_t"></a> <a id="bk_wifi_get_tx_raw_ac__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga4db7515aa0711410116b5acd3b93a4bb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_raw\_ac(uint8\_t \*ac)
:   get tx raw ac info

    参数
    :   **ac** – ac info

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv426bk_wifi_get_tx_raw_timeoutP8uint16_t"></a>

<a id="_CPPv326bk_wifi_get_tx_raw_timeoutP8uint16_t"></a> <a id="_CPPv226bk_wifi_get_tx_raw_timeoutP8uint16_t"></a> <a id="bk_wifi_get_tx_raw_timeout__uint16_tP"></a> <a id="group__bk__api__wifi__v2_1ga39995099b86b7f16604060ef4627cfb2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_raw\_timeout(uint16\_t \*time)
:   get tx raw timeout info

    参数
    :   **time** – timeout info

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv423bk_wifi_set_min_rsv_mem8uint16_t"></a>

<a id="_CPPv323bk_wifi_set_min_rsv_mem8uint16_t"></a> <a id="_CPPv223bk_wifi_set_min_rsv_mem8uint16_t"></a> <a id="bk_wifi_set_min_rsv_mem__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga04358a5590c7c7b3892bbd790ac6f8e1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_min\_rsv\_mem(uint16\_t mem\_bytes)
:   Update the minimux heap memory size that Wi-Fi should reserve.

    **Attention**
    :   1\. An small piece of extra memory will be malloced from heap for each TX packets delivered to Wi-Fi, so if the pending TX packets are too many for some reasons, the heap memory will be occupied too much by TX packets. To ensure the stability of whole system, this interface is provied to limit the memory size for Wi-Fi TX packets.

    **Attention**
    :   2\. The maximum valid value of memory size which could update via this API is 30K bytes

    **Attention**
    :   3\. The default minimux reserved memory size is 10K bytes

    参数
    :   **mem\_bytes** – the expected reserved memory size(bytes)

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv423bk_wifi_get_min_rsv_memP8uint16_t"></a>

<a id="_CPPv323bk_wifi_get_min_rsv_memP8uint16_t"></a> <a id="_CPPv223bk_wifi_get_min_rsv_memP8uint16_t"></a> <a id="bk_wifi_get_min_rsv_mem__uint16_tP"></a> <a id="group__bk__api__wifi__v2_1ga27c6f9387af82c93fdb4d4745567811e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_min\_rsv\_mem(uint16\_t \*mem\_bytes)
:   Get the minimux heap memory size that Wi-Fi currently creserves.

    参数
    :   **mem\_bytes** – return currently reserved memory size(bytes)

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a>

<a id="_CPPv327bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a> <a id="_CPPv227bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a> <a id="bk_wifi_set_tx_max_msdu_cnt__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga1f4d92b573cb998c9b7844d5088097a4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_max\_msdu\_cnt(uint16\_t max\_cnt)
:   Update the maximum MSDU count that Wi-Fi could handle.

    参数
    :   **max\_cnt** – the maxmimum MSDU count

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a>

<a id="_CPPv327bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a> <a id="_CPPv227bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a> <a id="bk_wifi_get_tx_max_msdu_cnt__uint16_tP"></a> <a id="group__bk__api__wifi__v2_1gae2d2f50c4bb2a7976a2f259450e44d2e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_max\_msdu\_cnt(uint16\_t \*max\_cnt)
:   Get the maximum MSDU count configuration that Wi-Fi could handle.

    参数
    :   **max\_cnt** – return the maxmimum MSDU count

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_set_data_rty_num7uint8_t"></a>

<a id="_CPPv324bk_wifi_set_data_rty_num7uint8_t"></a> <a id="_CPPv224bk_wifi_set_data_rty_num7uint8_t"></a> <a id="bk_wifi_set_data_rty_num__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga774f6bf3b9c4c8714a7aba4a4fdc9662"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_data\_rty\_num(uint8\_t rty\_num)
:   Set data frame retry numbers.

    参数
    :   **rty\_num** – data frame retry numbers

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_get_data_rty_numP8uint32_t"></a>

<a id="_CPPv324bk_wifi_get_data_rty_numP8uint32_t"></a> <a id="_CPPv224bk_wifi_get_data_rty_numP8uint32_t"></a> <a id="bk_wifi_get_data_rty_num__uint32_tP"></a> <a id="group__bk__api__wifi__v2_1ga0478c8d841bea3910c511064429c8713"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_data\_rty\_num(uint32\_t \*rty\_num)
:   Get data frame retry numbers.

    参数
    :   **rty\_num** – data frame retry numbers

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_set_mgmt_rty_num7uint8_t"></a>

<a id="_CPPv324bk_wifi_set_mgmt_rty_num7uint8_t"></a> <a id="_CPPv224bk_wifi_set_mgmt_rty_num7uint8_t"></a> <a id="bk_wifi_set_mgmt_rty_num__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaad9a692a885f53de215245cea9e6cd5c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_mgmt\_rty\_num(uint8\_t rty\_num)
:   Set management frame retry numbers.

    参数
    :   **rty\_num** – management frame retry numbers

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_wifi_get_mgmt_rty_numP8uint32_t"></a>

<a id="_CPPv324bk_wifi_get_mgmt_rty_numP8uint32_t"></a> <a id="_CPPv224bk_wifi_get_mgmt_rty_numP8uint32_t"></a> <a id="bk_wifi_get_mgmt_rty_num__uint32_tP"></a> <a id="group__bk__api__wifi__v2_1gabedf576170e387eeb82636241bfd235c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_mgmt\_rty\_num(uint32\_t \*rty\_num)
:   Get management frame retry numbers.

    参数
    :   **rty\_num** – management frame retry numbers

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv419bk_wifi_capa_config17wifi_capability_t8uint32_t"></a>

<a id="_CPPv319bk_wifi_capa_config17wifi_capability_t8uint32_t"></a> <a id="_CPPv219bk_wifi_capa_config17wifi_capability_t8uint32_t"></a> <a id="bk_wifi_capa_config__wifi_capability_t.uint32_t"></a> <a id="group__bk__api__wifi__v2_1gac844dc0c4b7acd23f5ec8f5f1cc6fa90"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_capa\_config([wifi\_capability\_t](#_CPPv417wifi_capability_t "wifi_capability_t") capa\_id, uint32\_t capa\_val)
:   Update Wi-Fi capability configuration.

    This API is used to change some Wi-Fi capability configuration, please refer to wifi\_capability\_t to get the capability that has been supported.

    **Attention**
    :   1\. Please keep in mind that Wi-Fi behavior may change if the capability is changed to different value compared with the default value.

    **Attention**
    :   2\. We strongly suggest not using this API except you are very farmiliar with the Wi-Fi specification.

    **Attention**
    :   3\. If you want Wi-Fi working on 11b only mode, please set 11b only mode by configurate paramter capa\_id with WIFI\_CAPA\_ID\_11B\_ONLY\_EN and capa\_val with TRUE.

    参数
    :   - **capa\_id** – the specific capability you want to change
        - **capa\_val** – new capability value

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv419bk_wifi_set_countryPK14wifi_country_t"></a>

<a id="_CPPv319bk_wifi_set_countryPK14wifi_country_t"></a> <a id="_CPPv219bk_wifi_set_countryPK14wifi_country_t"></a> <a id="bk_wifi_set_country__wifi_country_tCP"></a> <a id="group__bk__api__wifi__v2_1gaa73a4fdaf2ca78ccd0d24c02d94e826f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_country(const [wifi\_country\_t](#_CPPv414wifi_country_t "wifi_country_t") \*country)
:   configure country info

    **Attention**
    :   1\. The default country is {.cc\=”CN”, .schan\=1, .nchan\=13, policy\=WIFI\_COUNTRY\_POLICY\_AUTO}

    **Attention**
    :   2\. When the country policy is WIFI\_COUNTRY\_POLICY\_AUTO, the country info of the AP to which the station is connected is used. E.g. if the configured country info is {.cc\=”USA”, .schan\=1, .nchan\=11} and the country info of the AP to which the station is connected is {.cc\=”JP”, .schan\=1, .nchan\=14} then the country info that will be used is {.cc\=”JP”, .schan\=1, .nchan\=14}. If the station disconnected from the AP the country info is set back back to the country info of the station automatically, {.cc\=”USA”, .schan\=1, .nchan\=11} in the example.

    **Attention**
    :   3\. When the country policy is WIFI\_COUNTRY\_POLICY\_MANUAL, always use the configured country info.

    **Attention**
    :   4\. When the country info is changed because of configuration or because the station connects to a different external AP, the country IE in probe response/beacon of the soft-AP is changed also.

    **Attention**
    :   5\. The country configuration is not stored into flash

    **Attention**
    :   6\. This API doesn’t validate the per-country rules, it’s up to the user to fill in all fields according to local regulations.

    参数
    :   **country** – the configured country info

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: WiFi is not initialized
        - BK\_ERR\_PARAM: invalid argument

<a id="_CPPv424bk_wifi_set_country_codePKc"></a>

<a id="_CPPv324bk_wifi_set_country_codePKc"></a> <a id="_CPPv224bk_wifi_set_country_codePKc"></a> <a id="bk_wifi_set_country_code__cCP"></a> <a id="group__bk__api__wifi__v2_1ga6b2e572f9c1a97aa49baf2892da5063c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_country\_code(const char \*alpha2)
:   configure regulatory domain

    @alpha2 alpha2 ISO/IEC 3166-1 alpha

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: WiFi is not initialized
        - BK\_ERR\_PARAM: invalid argument

<a id="_CPPv419bk_wifi_get_countryP14wifi_country_t"></a>

<a id="_CPPv319bk_wifi_get_countryP14wifi_country_t"></a> <a id="_CPPv219bk_wifi_get_countryP14wifi_country_t"></a> <a id="bk_wifi_get_country__wifi_country_tP"></a> <a id="group__bk__api__wifi__v2_1gac7d81cf7284a781dc89f32a34bdbd19b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_country([wifi\_country\_t](#_CPPv414wifi_country_t "wifi_country_t") \*country)
:   get the current country info

    参数
    :   **country** – country info

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: WiFi is not initialized
        - BK\_ERR\_PARAM: invalid argument

<a id="_CPPv424bk_wifi_get_country_codev"></a>

<a id="_CPPv324bk_wifi_get_country_codev"></a> <a id="_CPPv224bk_wifi_get_country_codev"></a> <a id="bk_wifi_get_country_code__void"></a> <a id="group__bk__api__wifi__v2_1ga9033494dddef83c90015b6005bd1f92b"></a> char \*bk\_wifi\_get\_country\_code(void)
:   get the current country code

    返回
    :   country code string

<a id="_CPPv421bk_wifi_sta_pm_enablev"></a>

<a id="_CPPv321bk_wifi_sta_pm_enablev"></a> <a id="_CPPv221bk_wifi_sta_pm_enablev"></a> <a id="bk_wifi_sta_pm_enable__void"></a> <a id="group__bk__api__wifi__v2_1gad4c99153083a4794817f4d94bb373511"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_pm\_enable(void)
:   enable wifi sta power management

    返回
    :   - BK\_OK: on succeed
        - others: real error, used for future.

<a id="_CPPv422bk_wifi_sta_pm_disablev"></a>

<a id="_CPPv322bk_wifi_sta_pm_disablev"></a> <a id="_CPPv222bk_wifi_sta_pm_disablev"></a> <a id="bk_wifi_sta_pm_disable__void"></a> <a id="group__bk__api__wifi__v2_1gace062a914995e24ed92af5627e10410a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_sta\_pm\_disable(void)
:   disable wifi sta power management

    返回
    :   - BK\_OK: on succeed
        - others: real error, used for future.

<a id="_CPPv419bk_wifi_get_channelv"></a>

<a id="_CPPv319bk_wifi_get_channelv"></a> <a id="_CPPv219bk_wifi_get_channelv"></a> <a id="bk_wifi_get_channel__void"></a> <a id="group__bk__api__wifi__v2_1ga78cd0fd3138dd36fb20c862ea33d4712"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_channel(void)
:   get current channel ID

    参数
    :   **basically** – range from 1\~13

    返回
    :   - BK\_OK: on succeed
        - others: real error, used for future.

<a id="_CPPv423bk_wifi_set_mac_addressPc"></a>

<a id="_CPPv323bk_wifi_set_mac_addressPc"></a> <a id="_CPPv223bk_wifi_set_mac_addressPc"></a> <a id="bk_wifi_set_mac_address__cP"></a> <a id="group__bk__api__wifi__v2_1gac6612c64c6284a344100b43ba4e9997f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_mac\_address(char \*mac)
:   Set Wi-Fi MAC addresses.

    The given MAC address will become the station MAC address.The AP MAC address (i.e BSSID) will be the same MAC address but with the local bit set.

    @usage example: mac c8478cxxyyzz txevm -e 2 //if needed

    备注

    on some platforms the change of MAC address can only take effect after reboot.

    参数
    :   **mac** – system mac

    返回
    :   ```
        - BK_OK: on succeed
         - others: real error, used for future.
        ```

<a id="_CPPv432bk_wifi_manual_cal_rfcali_statusv"></a>

<a id="_CPPv332bk_wifi_manual_cal_rfcali_statusv"></a> <a id="_CPPv232bk_wifi_manual_cal_rfcali_statusv"></a> <a id="bk_wifi_manual_cal_rfcali_status__void"></a> <a id="group__bk__api__wifi__v2_1gad0f9f4f5e6294e7c3e55c95f209d30d8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_manual\_cal\_rfcali\_status(void)
:   Get Wi-Fi Calibration status.

    返回
    :   - BK\_OK: on succeed
        - others: real error, used for future.

<a id="_CPPv442bk_wifi_ap_vif_probe_req_frame_cb_registerPv"></a>

<a id="_CPPv342bk_wifi_ap_vif_probe_req_frame_cb_registerPv"></a> <a id="_CPPv242bk_wifi_ap_vif_probe_req_frame_cb_registerPv"></a> <a id="bk_wifi_ap_vif_probe_req_frame_cb_register__voidP"></a> <a id="group__bk__api__wifi__v2_1ga27ed944101f44ef722ad441bbf793a5c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ap\_vif\_probe\_req\_frame\_cb\_register(void \*cb)
:   Register a cb of probe request for ap.

    参数
    :   **cb** – callback function of probe request to register

<a id="_CPPv425bk_wifi_get_lowpower_modev"></a>

<a id="_CPPv325bk_wifi_get_lowpower_modev"></a> <a id="_CPPv225bk_wifi_get_lowpower_modev"></a> <a id="bk_wifi_get_lowpower_mode__void"></a> <a id="group__bk__api__wifi__v2_1ga0f10e28e84341f96f9d03ace463fa352"></a> bool bk\_wifi\_get\_lowpower\_mode(void)
:   get if ever set dtim10.

    返回
    :   - true: has been set to \>\= dtim10.
        - false: never set \>\= dtim10 before.

<a id="_CPPv432bk_wifi_send_listen_interval_req7uint8_t"></a>

<a id="_CPPv332bk_wifi_send_listen_interval_req7uint8_t"></a> <a id="_CPPv232bk_wifi_send_listen_interval_req7uint8_t"></a> <a id="bk_wifi_send_listen_interval_req__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gab85e92fdd41b151d1e99e3cd784e380f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_listen\_interval\_req(uint8\_t interval)
:   Set listen interval.

    参数
    :   **any** – value is acceptable,but 1, 3, 10 is recommended.

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv427bk_wifi_send_sleep_mode_req7uint8_t"></a>

<a id="_CPPv327bk_wifi_send_sleep_mode_req7uint8_t"></a> <a id="_CPPv227bk_wifi_send_sleep_mode_req7uint8_t"></a> <a id="bk_wifi_send_sleep_mode_req__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga68c63933ab0c23e9ac10b1d30e9398d5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_sleep\_mode\_req(uint8\_t sleep\_mode)
:   Set sleep mode.

    参数
    :   **0, 1, 2** –

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv422bk_wifi_get_sleep_modeP7uint8_t"></a>

<a id="_CPPv322bk_wifi_get_sleep_modeP7uint8_t"></a> <a id="_CPPv222bk_wifi_get_sleep_modeP7uint8_t"></a> <a id="bk_wifi_get_sleep_mode__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga49d50d1cc51f3aa8e88ae813aacc703d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_sleep\_mode(uint8\_t \*sleep\_mode)
:   Get sleep mode.

    参数
    :   **return** – the configure sleep mode

    返回
    :   -0: min modem sleep mode -1: middle modem sleep mode -2: max modem sleep mode

<a id="_CPPv427bk_wifi_get_listen_intervalP7uint8_t"></a>

<a id="_CPPv327bk_wifi_get_listen_intervalP7uint8_t"></a> <a id="_CPPv227bk_wifi_get_listen_intervalP7uint8_t"></a> <a id="bk_wifi_get_listen_interval__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga2f3319ed4dd92eb1220934e30154d193"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_listen\_interval(uint8\_t \*listen\_interval)
:   Get listen interval.

    参数
    :   **return** – the configure listen interval

    返回
    :   -0: not set listen interval -others:return the configure listen interval value.

<a id="_CPPv429bk_wifi_send_arp_set_rate_req8uint16_t"></a>

<a id="_CPPv329bk_wifi_send_arp_set_rate_req8uint16_t"></a> <a id="_CPPv229bk_wifi_send_arp_set_rate_req8uint16_t"></a> <a id="bk_wifi_send_arp_set_rate_req__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga9ea1a5f451da1e093f0ff1e99000b0c6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_arp\_set\_rate\_req(uint16\_t arp\_tx\_rate)
:   Set arp tx rate.

    参数
    :   **any** – value is acceptable,but 1, 6 is recommended.

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv429bk_wifi_send_bcn_loss_int_req7uint8_t7uint8_t"></a>

<a id="_CPPv329bk_wifi_send_bcn_loss_int_req7uint8_t7uint8_t"></a> <a id="_CPPv229bk_wifi_send_bcn_loss_int_req7uint8_t7uint8_t"></a> <a id="bk_wifi_send_bcn_loss_int_req__uint8_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga9914fd1de54614e3f152b1d2415cb435"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_bcn\_loss\_int\_req(uint8\_t interval, uint8\_t repeat\_num)
:   When beacon loss occurs,use beacon loss interval.

    参数
    :   - **interval** – any value is acceptable,it is recommended that this value less than listen interval
        - **repeat\_num** – set beacon loss interval number,the minimum value is 1

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv425bk_wifi_set_bcn_loss_time7uint8_t7uint8_t"></a>

<a id="_CPPv325bk_wifi_set_bcn_loss_time7uint8_t7uint8_t"></a> <a id="_CPPv225bk_wifi_set_bcn_loss_time7uint8_t7uint8_t"></a> <a id="bk_wifi_set_bcn_loss_time__uint8_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga7bab2dc03a6d323612808f461fc3f3de"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_bcn\_loss\_time(uint8\_t wait\_cnt, uint8\_t wake\_cnt)
:   When beacon loss occurs,use bcn loss time.

    @usage example:(10s no beacon frame received(normal reception for the first 5s,ps off for the next 5s),disconnect from the router) DTIM10:wait\_cnt \= 5,wake\_cnt \= 50 DTIM1 :wait\_cnt \= 50,wake\_cnt \= 50

    参数
    :   - **wait\_cnt** – failed to receive beacon for wait\_cnt consecutive cycles, close ps,wait\_cnt corresponds to dtimx(listen\_interval)
        - **wake\_cnt** – after ps is turned off,the beacon fails to receive for wake\_cnt consecutive cycles, disconnect;wake\_cnt corresponds to dtim1

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv425bk_wifi_set_bcn_miss_time7uint8_t"></a>

<a id="_CPPv325bk_wifi_set_bcn_miss_time7uint8_t"></a> <a id="_CPPv225bk_wifi_set_bcn_miss_time7uint8_t"></a> <a id="bk_wifi_set_bcn_miss_time__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga7d593c4da831aa9614dfc014588bf766"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_bcn\_miss\_time(uint8\_t bcnmiss\_time)
:   configure beacon miss time.

    bcnmiss\_time: bcnmiss\_time not receive the beacon,disconnected from the router;unit: second

    @usage example:(30s no beacon frame received,disconnect from the router) bcnmiss\_time:30

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv427bk_wifi_set_conn_delay_time7uint8_t"></a>

<a id="_CPPv327bk_wifi_set_conn_delay_time7uint8_t"></a> <a id="_CPPv227bk_wifi_set_conn_delay_time7uint8_t"></a> <a id="bk_wifi_set_conn_delay_time__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gafd4824dd62dd6bdba386c0b6fc081f5a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_conn\_delay\_time(uint8\_t conn\_delay\_time)
:   set station connection delay time.

    参数
    :   **conn\_delay\_time** – delay time of starting station connection (in ms).

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv431bk_wifi_bcn_cc_rxed_register_cbK21wifi_beacon_cc_rxed_tPv"></a>

<a id="_CPPv331bk_wifi_bcn_cc_rxed_register_cbK21wifi_beacon_cc_rxed_tPv"></a> <a id="_CPPv231bk_wifi_bcn_cc_rxed_register_cbK21wifi_beacon_cc_rxed_tPv"></a> <a id="bk_wifi_bcn_cc_rxed_register_cb__wifi_beacon_cc_rxed_tC.voidP"></a> <a id="group__bk__api__wifi__v2_1ga126e549848120c764fa77ac30ddee050"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_bcn\_cc\_rxed\_register\_cb(const [wifi\_beacon\_cc\_rxed\_t](#_CPPv421wifi_beacon_cc_rxed_t "wifi_beacon_cc_rxed_t") cc\_cb, void \*ctxt)
:   regist bcn cc rxed callback.

    参数
    :   **bcn** – cc the callback function.

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv413cc_scan_startv"></a>

<a id="_CPPv313cc_scan_startv"></a> <a id="_CPPv213cc_scan_startv"></a> <a id="cc_scan_start__void"></a> <a id="group__bk__api__wifi__v2_1gab4713d825f06b4a15840b41754381f71"></a> int cc\_scan\_start(void)
:   start scan procedure to find AP’s country code

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv412cc_scan_stopv"></a>

<a id="_CPPv312cc_scan_stopv"></a> <a id="_CPPv212cc_scan_stopv"></a> <a id="cc_scan_stop__void"></a> <a id="group__bk__api__wifi__v2_1gac48b18ba13d0a795978a8d71100429e0"></a> void cc\_scan\_stop(void)
:   stop scan procedure to find AP’s country code

    返回
    :   success

<a id="_CPPv420bk_scan_country_codeP7uint8_t"></a>

<a id="_CPPv320bk_scan_country_codeP7uint8_t"></a> <a id="_CPPv220bk_scan_country_codeP7uint8_t"></a> <a id="bk_scan_country_code__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1gaa22b1b782ef4c7442a1285c26a7cf954"></a> int bk\_scan\_country\_code(uint8\_t \*country\_code)
:   Get country code by scan.

    **Attention**
    :   Need open CONFIG\_WIFI\_SCAN\_COUNTRY\_CODE\=y in config

    参数
    :   **country\_code** – The point of country code buffer

    返回
    :   - \> 0 : succeed, and the length of country code buffer
        - \= 0 : not found
        - \<\= 0 : failures.

<a id="_CPPv428bk_wifi_bcn_miss_register_cbK17wifi_bcnmiss_cb_t"></a>

<a id="_CPPv328bk_wifi_bcn_miss_register_cbK17wifi_bcnmiss_cb_t"></a> <a id="_CPPv228bk_wifi_bcn_miss_register_cbK17wifi_bcnmiss_cb_t"></a> <a id="bk_wifi_bcn_miss_register_cb__wifi_bcnmiss_cb_tC"></a> <a id="group__bk__api__wifi__v2_1ga212e2957e33bd6c5de13c22fe4b34369"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_bcn\_miss\_register\_cb(const [wifi\_bcnmiss\_cb\_t](#_CPPv417wifi_bcnmiss_cb_t "wifi_bcnmiss_cb_t") bcnmiss\_cb)
:   regist bcn miss callback.

    参数
    :   **bcnmiss\_cb** – the callback function, this function should return bool value indicating whether disconnected from router or not.

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv424bk_wifi_set_bcn_recv_win7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv324bk_wifi_set_bcn_recv_win7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv224bk_wifi_set_bcn_recv_win7uint8_t7uint8_t7uint8_t"></a> <a id="bk_wifi_set_bcn_recv_win__uint8_t.uint8_t.uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga93de8247d9cc2de8d9541360253686e6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_bcn\_recv\_win(uint8\_t default\_win, uint8\_t max\_win, uint8\_t step)
:   set beacon receive window.

    参数
    :   - **default\_win** – default beacon receive window(ms),minimum is 5,less than or equal to max\_win.
        - **max\_win** – max beacon receive window(ms),maximum is 20\.
        - **step** – increase the beacon reception time by a step value(ms)

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv429bk_wifi_get_support_wifi_modeP7uint8_t"></a>

<a id="_CPPv329bk_wifi_get_support_wifi_modeP7uint8_t"></a> <a id="_CPPv229bk_wifi_get_support_wifi_modeP7uint8_t"></a> <a id="bk_wifi_get_support_wifi_mode__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga823977c99fd408ec06fcfd33e3fff41a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_support\_wifi\_mode(uint8\_t \*support\_mode)
:   Get wifi support mode.

    参数
    :   **get** – wifi support info

    返回
    :   -2: support wifi6(HE) -1: support wifi4(HT) -0: support others(11n/g)

<a id="_CPPv426bk_wifi_get_statistic_infoP22wifi_statistics_info_t"></a>

<a id="_CPPv326bk_wifi_get_statistic_infoP22wifi_statistics_info_t"></a> <a id="_CPPv226bk_wifi_get_statistic_infoP22wifi_statistics_info_t"></a> <a id="bk_wifi_get_statistic_info__wifi_statistics_info_tP"></a> <a id="group__bk__api__wifi__v2_1gae7f7f32858ec93b741b6682d60eaddf9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_statistic\_info([wifi\_statistics\_info\_t](#_CPPv422wifi_statistics_info_t "wifi_statistics_info_t") \*wifiinfo)
:   Get wifi statistic info.

    参数
    :   **get** – wifi info from fw

    返回
    :   -BK\_OK: on success -others:real error, used for future.

<a id="_CPPv416bk_wifi_ota_dtimb"></a>

<a id="_CPPv316bk_wifi_ota_dtimb"></a> <a id="_CPPv216bk_wifi_ota_dtimb"></a> <a id="bk_wifi_ota_dtim__b"></a> <a id="group__bk__api__wifi__v2_1ga8c1255c2ce751393f9304c154bc75c40"></a> void bk\_wifi\_ota\_dtim(bool is\_open)
:   set wifi ps dtim info.

    参数
    :   **dtim** – 1 open or not

    返回
    :   -void.

<a id="_CPPv429bk_wifi_set_td_active_percent7uint8_t"></a>

<a id="_CPPv329bk_wifi_set_td_active_percent7uint8_t"></a> <a id="_CPPv229bk_wifi_set_td_active_percent7uint8_t"></a> <a id="bk_wifi_set_td_active_percent__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga10e352311d7fe5aadcc701add20ff41a"></a> void bk\_wifi\_set\_td\_active\_percent(uint8\_t active\_percent)
:   Set active\_percent.

    参数
    :   **{10ms-100ms}** – \*

    返回
    :   -void.

<a id="_CPPv430bk_wifi_mask_td_active_percentv"></a>

<a id="_CPPv330bk_wifi_mask_td_active_percentv"></a> <a id="_CPPv230bk_wifi_mask_td_active_percentv"></a> <a id="bk_wifi_mask_td_active_percent"></a> <a id="group__bk__api__wifi__v2_1ga1bd2739d41e9d1f4ec31276d190bec18"></a> void bk\_wifi\_mask\_td\_active\_percent()
:   mask active\_percent

    参数
    :   **\*** –

<a id="_CPPv428bk_wifi_ap_power_register_cb15FUNC_1PARAM_PTR"></a>

<a id="_CPPv328bk_wifi_ap_power_register_cb15FUNC_1PARAM_PTR"></a> <a id="_CPPv228bk_wifi_ap_power_register_cb15FUNC_1PARAM_PTR"></a> <a id="bk_wifi_ap_power_register_cb__FUNC_1PARAM_PTR"></a> <a id="group__bk__api__wifi__v2_1ga89517c629e44da48ffb89bdb21b73e38"></a> void bk\_wifi\_ap\_power\_register\_cb(FUNC\_1PARAM\_PTR cb)
:   register callback to get wifi ap power

    参数
    :   **callback** – interface \*

    返回
    :   -void.

<a id="_CPPv420bk_wlan_phy_open_ccav"></a>

<a id="_CPPv320bk_wlan_phy_open_ccav"></a> <a id="_CPPv220bk_wlan_phy_open_ccav"></a> <a id="bk_wlan_phy_open_cca__void"></a> <a id="group__bk__api__wifi__v2_1gab6111ca87fea32f862d4024b76e110a1"></a> void bk\_wlan\_phy\_open\_cca(void)

<a id="_CPPv421bk_wlan_phy_close_ccav"></a>

<a id="_CPPv321bk_wlan_phy_close_ccav"></a> <a id="_CPPv221bk_wlan_phy_close_ccav"></a> <a id="bk_wlan_phy_close_cca__void"></a> <a id="group__bk__api__wifi__v2_1ga897c1faa280f7ee71d0694b2a0aa9c73"></a> void bk\_wlan\_phy\_close\_cca(void)

<a id="_CPPv420bk_wlan_phy_show_ccav"></a>

<a id="_CPPv320bk_wlan_phy_show_ccav"></a> <a id="_CPPv220bk_wlan_phy_show_ccav"></a> <a id="bk_wlan_phy_show_cca__void"></a> <a id="group__bk__api__wifi__v2_1ga4d35cbf7a16c2baed5a0221c1da9b2a2"></a> void bk\_wlan\_phy\_show\_cca(void)

<a id="_CPPv417bk_wifi_ftm_startPK17wifi_ftm_config_tP18wifi_ftm_results_t"></a>

<a id="_CPPv317bk_wifi_ftm_startPK17wifi_ftm_config_tP18wifi_ftm_results_t"></a> <a id="_CPPv217bk_wifi_ftm_startPK17wifi_ftm_config_tP18wifi_ftm_results_t"></a> <a id="bk_wifi_ftm_start__wifi_ftm_config_tCP.wifi_ftm_results_tP"></a> <a id="group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ftm\_start(const [wifi\_ftm\_config\_t](#_CPPv417wifi_ftm_config_t "wifi_ftm_config_t") \*config, [wifi\_ftm\_results\_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") \*ftm\_results)
:   Start a fine timing measurement (FTM)

    This API notifies the WiFi driver to start a fine timing measurement, and get the ftm results.

    参数
    :   - **config** – the configuration of ftm
        - **ftm\_results** – the results of ftm

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_NOT\_INIT: WiFi is not initialized
        - BK\_ERR\_WIFI\_STA\_NOT\_STARTED: the STA is not started, call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) first.
        - BK\_ERR\_WIFI\_DRIVER: WiFi low level driver has failure.
        - others: other failures.

<a id="_CPPv423bk_wifi_ftm_dump_resultPK18wifi_ftm_results_t"></a>

<a id="_CPPv323bk_wifi_ftm_dump_resultPK18wifi_ftm_results_t"></a> <a id="_CPPv223bk_wifi_ftm_dump_resultPK18wifi_ftm_results_t"></a> <a id="bk_wifi_ftm_dump_result__wifi_ftm_results_tCP"></a> <a id="group__bk__api__wifi__v2_1gac6f6ae11c304a848c79aba4d207c9702"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_ftm\_dump\_result(const [wifi\_ftm\_results\_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") \*ftm\_results)
:   Dump the ftm results.

    **Attention**
    :   call [bk\_wifi\_ftm\_start()](#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd) first before call bk\_wifi\_ftm\_dump\_result.

    参数
    :   **ftm\_results** – The ftm result to be dumped.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PARAM: invalid scan result

<a id="_CPPv423bk_wifi_ftm_free_resultP18wifi_ftm_results_t"></a>

<a id="_CPPv323bk_wifi_ftm_free_resultP18wifi_ftm_results_t"></a> <a id="_CPPv223bk_wifi_ftm_free_resultP18wifi_ftm_results_t"></a> <a id="bk_wifi_ftm_free_result__wifi_ftm_results_tP"></a> <a id="group__bk__api__wifi__v2_1gaee64f6f8d06b25fde40dbbba64409d03"></a> void bk\_wifi\_ftm\_free\_result([wifi\_ftm\_results\_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") \*ftm\_results)
:   Free the ftm result.

    **Attention**
    :   This API free ftm\_results-\>rsp which allocated in [bk\_wifi\_ftm\_start()](#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd), it doesn’t free ftm\_results. So if ftm\_results is allocated by the caller, the caller need to free it.

    参数
    :   **ftm\_results** – The ftm result to be freed.

    返回
    :   - BK\_OK: always succeed

<a id="_CPPv427bk_wifi_set_pkt_trx_dbg_cfg8uint32_t"></a>

<a id="_CPPv327bk_wifi_set_pkt_trx_dbg_cfg8uint32_t"></a> <a id="_CPPv227bk_wifi_set_pkt_trx_dbg_cfg8uint32_t"></a> <a id="bk_wifi_set_pkt_trx_dbg_cfg__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga07613ff50b3e5a1f06c6cf76d4c3305b"></a> void bk\_wifi\_set\_pkt\_trx\_dbg\_cfg(uint32\_t cfg\_bit)
:   Set Wi-Fi TX/RX debug log configuration.

    This API could enable the TX/RX debug log by setting the corresponding debug bit.

    **Attention**
    :   This API is only used for DEBUG Wi-Fi issues according to frame TX/RX, there will be a lot of logs generated after set debug bit and it will have affect on the performance. To capture the whole logs, you should increase the buadrate of UART.

    参数
    :   **cfg\_bit** – Please refer to enum wifi\_pkt\_dbg\_bit to get more detail.

    返回
    :   - void: always succeed

<a id="_CPPv422bk_wifi_set_ap_channel7uint8_t"></a>

<a id="_CPPv322bk_wifi_set_ap_channel7uint8_t"></a> <a id="_CPPv222bk_wifi_set_ap_channel7uint8_t"></a> <a id="bk_wifi_set_ap_channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gad9d664910c75d3751c1dea690385b7cf"></a> void bk\_wifi\_set\_ap\_channel(uint8\_t channel)
:   Set Wi-Fi Softap Channel.

    This API could be used to change softap operation channel.

    @channel The valid channel ID should range from 1-14.

    **Attention**
    :   This API can only be used when softap is enabled and make sure the internal CSA strategy is disabled by calling API bk\_feature\_close\_coexist\_csa.

    返回
    :   - void: always succeed

<a id="_CPPv425bk_wifi_set_block_bcmc_en7uint8_t"></a>

<a id="_CPPv325bk_wifi_set_block_bcmc_en7uint8_t"></a> <a id="_CPPv225bk_wifi_set_block_bcmc_en7uint8_t"></a> <a id="bk_wifi_set_block_bcmc_en__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gabd0ee4a405311a19356f68b40975316d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_block\_bcmc\_en(uint8\_t config)
:   Enable Wi-Fi rx block broadcast and multicast frame.

    This API could enable Wi-Fi rx block broadcast and multicast frame.

    参数
    :   **config** – block type. 0:WIFI\_BCMC\_CLOSE 1:WIFI\_MC\_ON, 2:WIFI\_BC\_ON, 3:WIFI\_BC\_MC\_ON,

    返回
    :   - void: always succeed

<a id="_CPPv425bk_wifi_get_block_bcmc_env"></a>

<a id="_CPPv325bk_wifi_get_block_bcmc_env"></a> <a id="_CPPv225bk_wifi_get_block_bcmc_env"></a> <a id="bk_wifi_get_block_bcmc_en__void"></a> <a id="group__bk__api__wifi__v2_1ga5235feedd63bb0e0391f5af9d7b9b839"></a> bool bk\_wifi\_get\_block\_bcmc\_en(void)
:   Get Wi-Fi rx block broadcast and multicast frame status.

    参数
    :   **void.** –

    返回
    :   - enable status

<a id="_CPPv418bk_wifi_set_ani_enb"></a>

<a id="_CPPv318bk_wifi_set_ani_enb"></a> <a id="_CPPv218bk_wifi_set_ani_enb"></a> <a id="bk_wifi_set_ani_en__b"></a> <a id="group__bk__api__wifi__v2_1gae1f1484a628bd37ae8f2a5136e68edfc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_ani\_en(bool enable)
:   Enable Wi-Fi microwave anti-interference policy.

    This API could enable Wi-Fi microwave anti-interference policy.

    参数
    :   **enable.** –

    返回
    :   - void: always succeed

<a id="_CPPv418bk_wifi_get_ani_env"></a>

<a id="_CPPv318bk_wifi_get_ani_env"></a> <a id="_CPPv218bk_wifi_get_ani_env"></a> <a id="bk_wifi_get_ani_en__void"></a> <a id="group__bk__api__wifi__v2_1ga81a0150bfb641fece6e8504beca5e30c"></a> bool bk\_wifi\_get\_ani\_en(void)
:   Get Wi-Fi microwave anti-interference policy enable status.

    参数
    :   **void.** –

    返回
    :   - enable status

<a id="_CPPv421bk_wifi_set_pwr_limitP17wifi_tx_pwr_lmt_t"></a>

<a id="_CPPv321bk_wifi_set_pwr_limitP17wifi_tx_pwr_lmt_t"></a> <a id="_CPPv221bk_wifi_set_pwr_limitP17wifi_tx_pwr_lmt_t"></a> <a id="bk_wifi_set_pwr_limit__wifi_tx_pwr_lmt_tP"></a> <a id="group__bk__api__wifi__v2_1gaff17d87c8ede896a47db7b7b4081212a"></a> int bk\_wifi\_set\_pwr\_limit([wifi\_tx\_pwr\_lmt\_t](#_CPPv417wifi_tx_pwr_lmt_t "wifi_tx_pwr_lmt_t") \*tx\_pwr\_lmt)
:   Set Wi-Fi Power Limit.

    This API could be used to change max tx power with regulation,ratesection and channel .

    **Attention**
    :   This API can only be used to modify rf max power limit for specific regulation,rate and channel.

    参数
    :   **tx\_pwr\_lmt** – wifi tx power limit info

    返回
    :   - void: always succeed

<a id="_CPPv418bk_wifi_get_cal_2gv"></a>

<a id="_CPPv318bk_wifi_get_cal_2gv"></a> <a id="_CPPv218bk_wifi_get_cal_2gv"></a> <a id="bk_wifi_get_cal_2g__void"></a> <a id="group__bk__api__wifi__v2_1ga10f18a3b00754d6229d68526c88f1fc1"></a> bool bk\_wifi\_get\_cal\_2g(void)
:   Get rf cal 2g information.

    This API could be used to check rf 2g calibration .

    返回
    :   - true:if rf 2g is calibrated, false: if rf 2g is not calibrated

<a id="_CPPv423bk_wifi_get_noise_floorP7uint8_t"></a>

<a id="_CPPv323bk_wifi_get_noise_floorP7uint8_t"></a> <a id="_CPPv223bk_wifi_get_noise_floorP7uint8_t"></a> <a id="bk_wifi_get_noise_floor__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1gab268706b0f12487acba297e4e77f45d1"></a> void bk\_wifi\_get\_noise\_floor(uint8\_t \*noise\_floor)
:   Get noise floor.

    参数
    :   **noise\_floor** – store noise floor

    返回
    :   - void: always succeed

<a id="_CPPv420bk_wifi_get_tx_stats7uint8_tP10tx_stats_t"></a>

<a id="_CPPv320bk_wifi_get_tx_stats7uint8_tP10tx_stats_t"></a> <a id="_CPPv220bk_wifi_get_tx_stats7uint8_tP10tx_stats_t"></a> <a id="bk_wifi_get_tx_stats__uint8_t.tx_stats_tP"></a> <a id="group__bk__api__wifi__v2_1ga61deab95ef0153858c76c5fe65e383ef"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_stats(uint8\_t mode, struct [tx\_stats\_t](#_CPPv410tx_stats_t "tx_stats_t") \*tx\_stats)
:   Get tx stats.

    ```
        PER calculation formula:  per = (tx_agg_fail + tx_singel_retry)/(tx_agg_total + tx_singel_total*SINGLE_RETRY_CNT)
        - tx_agg_fail/tx_singel_retry/tx_agg_total/tx_singel_total: get from struct tx_stats,
        - SINGLE_RETRY_CNT: get from function bk_wifi_get_data_rty_num();
    ```

    参数
    :   **config** – mode. 0:STATION 1:SOFT AP

    返回
    :   - tx\_stats:tx statistics

<a id="_CPPv420bk_wifi_get_tx_power13wifi_standardPf"></a>

<a id="_CPPv320bk_wifi_get_tx_power13wifi_standardPf"></a> <a id="_CPPv220bk_wifi_get_tx_power13wifi_standardPf"></a> <a id="bk_wifi_get_tx_power__wifi_standard.floatP"></a> <a id="group__bk__api__wifi__v2_1gaf3d87a567db82eb0c071f82969e0e243"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_power([wifi\_standard](#_CPPv413wifi_standard "wifi_standard") standard, float \*powerdBm)
:   Fetch 802.11 TX power by standards.

    参数
    :   - **standard** – IEEE 80211 standard
        - **power** – TX power in dBm

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv420bk_wifi_set_tx_power13wifi_standardf"></a>

<a id="_CPPv320bk_wifi_set_tx_power13wifi_standardf"></a> <a id="_CPPv220bk_wifi_set_tx_power13wifi_standardf"></a> <a id="bk_wifi_set_tx_power__wifi_standard.float"></a> <a id="group__bk__api__wifi__v2_1ga916cce8f8adcc43ea8cbdad5a04b1713"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_power([wifi\_standard](#_CPPv413wifi_standard "wifi_standard") standard, float powerdBm)
:   Update 802.11 TX power by standards.

    参数
    :   - **standard** – IEEE 80211 standard
        - **power** – TX power in dBm

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv415bk_wifi_disablev"></a>

<a id="_CPPv315bk_wifi_disablev"></a> <a id="_CPPv215bk_wifi_disablev"></a> <a id="bk_wifi_disable__void"></a> <a id="group__bk__api__wifi__v2_1ga2755479f996867212efb1ef37543c2d8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_disable(void)
:   Disable wifi mac.

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv414bk_wifi_enablev"></a>

<a id="_CPPv314bk_wifi_enablev"></a> <a id="_CPPv214bk_wifi_enablev"></a> <a id="bk_wifi_enable__void"></a> <a id="group__bk__api__wifi__v2_1ga5fa1e47211b479d419620d160911c859"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_enable(void)
:   enable wifi mac

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [wifi\_types.h](https://github.com/bekencorp/armino/blob/main/components/wifi_types.h)

<a id="id2"></a>

### Functions

<a id="_CPPv433wifi_rlk_scan_get_register_cfm_cbv"></a>

<a id="_CPPv333wifi_rlk_scan_get_register_cfm_cbv"></a> <a id="_CPPv233wifi_rlk_scan_get_register_cfm_cbv"></a> <a id="wifi_rlk_scan_get_register_cfm_cb__void"></a> <a id="group__bk__api__wifi__v2__typedef_1ga758681738923281405e4cef9601dc56f"></a> [wifi\_rlk\_scan\_cfm\_cb\_t](#_CPPv422wifi_rlk_scan_cfm_cb_t "wifi_rlk_scan_cfm_cb_t") wifi\_rlk\_scan\_get\_register\_cfm\_cb(void)

<a id="structures"></a>

### Structures

<a id="_CPPv418wifi_init_config_t"></a>

<a id="_CPPv318wifi_init_config_t"></a> <a id="_CPPv218wifi_init_config_t"></a> <a id="wifi_init_config_t"></a> <a id="structwifi__init__config__t"></a> struct wifi\_init\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_init_config_t8featuresE"></a>

    <a id="_CPPv3N18wifi_init_config_t8featuresE"></a> <a id="_CPPv2N18wifi_init_config_t8featuresE"></a> <a id="wifi_init_config_t::features__uint64_t"></a> <a id="group__bk__api__wifi__v2_1gae9f99f3b03f67d5c39a0e20f901bd08b"></a> uint64\_t features
    :   WiFi feature bitmaps

    <a id="_CPPv4N18wifi_init_config_t8os_funcsE"></a>

    <a id="_CPPv3N18wifi_init_config_t8os_funcsE"></a> <a id="_CPPv2N18wifi_init_config_t8os_funcsE"></a> <a id="wifi_init_config_t::os_funcs__voidP"></a> <a id="group__bk__api__wifi__v2_1ga06ba2b0c66e5abe4f5edd681a0715716"></a> void \*os\_funcs
    :   WiFi OS functions

    <a id="_CPPv4N18wifi_init_config_t6os_valE"></a>

    <a id="_CPPv3N18wifi_init_config_t6os_valE"></a> <a id="_CPPv2N18wifi_init_config_t6os_valE"></a> <a id="wifi_init_config_t::os_val__voidP"></a> <a id="group__bk__api__wifi__v2_1gaa65b53e6647ab9a642a6d982c6da3f11"></a> void \*os\_val
    :   WiFI Values

    <a id="_CPPv4N18wifi_init_config_t8reservedE"></a>

    <a id="_CPPv3N18wifi_init_config_t8reservedE"></a> <a id="_CPPv2N18wifi_init_config_t8reservedE"></a> <a id="wifi_init_config_t::reserved__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga85267c94d0e747b3d001848dadda318b"></a> uint8\_t reserved\[16\]
    :   Reserved

<a id="_CPPv414wifi_channel_t"></a>

<a id="_CPPv314wifi_channel_t"></a> <a id="_CPPv214wifi_channel_t"></a> <a id="wifi_channel_t"></a> <a id="structwifi__channel__t"></a> struct wifi\_channel\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14wifi_channel_t7primaryE"></a>

    <a id="_CPPv3N14wifi_channel_t7primaryE"></a> <a id="_CPPv2N14wifi_channel_t7primaryE"></a> <a id="wifi_channel_t::primary__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga2753b11986e9c2876a93c8c4d8261b77"></a> uint8\_t primary
    :   Primary channel

    <a id="_CPPv4N14wifi_channel_t6secondE"></a>

    <a id="_CPPv3N14wifi_channel_t6secondE"></a> <a id="_CPPv2N14wifi_channel_t6secondE"></a> <a id="wifi_channel_t::second__wifi_second_channel_t"></a> <a id="group__bk__api__wifi__v2_1gaddd0b1028bfc9310ee2152a40c4df386"></a> [wifi\_second\_channel\_t](#_CPPv421wifi_second_channel_t "wifi_second_channel_t") second
    :   Secondary cahnnel

<a id="_CPPv47bk_vise"></a>

<a id="_CPPv37bk_vise"></a> <a id="_CPPv27bk_vise"></a> <a id="bk_vise"></a> <a id="structbk__vise"></a> struct bk\_vise

<a id="_CPPv417wifi_sta_config_t"></a>

<a id="_CPPv317wifi_sta_config_t"></a> <a id="_CPPv217wifi_sta_config_t"></a> <a id="wifi_sta_config_t"></a> <a id="structwifi__sta__config__t"></a> struct wifi\_sta\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_sta_config_t4ssidE"></a>

    <a id="_CPPv3N17wifi_sta_config_t4ssidE"></a> <a id="_CPPv2N17wifi_sta_config_t4ssidE"></a> <a id="wifi_sta_config_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1ga173955fd4b6debbf470dcee831f82fe5"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP to be connected

    <a id="_CPPv4N17wifi_sta_config_t5bssidE"></a>

    <a id="_CPPv3N17wifi_sta_config_t5bssidE"></a> <a id="_CPPv2N17wifi_sta_config_t5bssidE"></a> <a id="wifi_sta_config_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gaf4c854d9f2fe90367777324fea95fc63"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP to be connected, fast connect only

    <a id="_CPPv4N17wifi_sta_config_t7channelE"></a>

    <a id="_CPPv3N17wifi_sta_config_t7channelE"></a> <a id="_CPPv2N17wifi_sta_config_t7channelE"></a> <a id="wifi_sta_config_t::channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga2cc86d1fa7e6aeebdfbc73068c19cbf7"></a> uint8\_t channel
    :   Primary channel of AP to be connected, fast connect only

    <a id="_CPPv4N17wifi_sta_config_t8securityE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8securityE"></a> <a id="_CPPv2N17wifi_sta_config_t8securityE"></a> <a id="wifi_sta_config_t::security__wifi_security_t"></a> <a id="group__bk__api__wifi__v2_1gac23fbfa8a5f39e98bf8d42b9817a0b50"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security of AP to be connected

    <a id="_CPPv4N17wifi_sta_config_t8passwordE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8passwordE"></a> <a id="_CPPv2N17wifi_sta_config_t8passwordE"></a> <a id="wifi_sta_config_t::password__cA"></a> <a id="group__bk__api__wifi__v2_1ga6a0700a6d3655cb0eb38453cadf15660"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Security key or PMK of the wlan.

    <a id="_CPPv4N17wifi_sta_config_t3pskE"></a>

    <a id="_CPPv3N17wifi_sta_config_t3pskE"></a> <a id="_CPPv2N17wifi_sta_config_t3pskE"></a> <a id="wifi_sta_config_t::psk__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga18b5d00cb081bc70f9dcdfb167ae8a26"></a> uint8\_t psk\[WIFI\_PASSWORD\_LEN\]
    :   PSK of AP

    <a id="_CPPv4N17wifi_sta_config_t7ip_addrE"></a>

    <a id="_CPPv3N17wifi_sta_config_t7ip_addrE"></a> <a id="_CPPv2N17wifi_sta_config_t7ip_addrE"></a> <a id="wifi_sta_config_t::ip_addr__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gafbc13d80f3fdb95399228cd9eefa2264"></a> uint8\_t ip\_addr\[4\]
    :   IP address

    <a id="_CPPv4N17wifi_sta_config_t7netmaskE"></a>

    <a id="_CPPv3N17wifi_sta_config_t7netmaskE"></a> <a id="_CPPv2N17wifi_sta_config_t7netmaskE"></a> <a id="wifi_sta_config_t::netmask__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga04415fbf53ad2856e2e67c6028d85d63"></a> uint8\_t netmask\[4\]
    :   NET address

    <a id="_CPPv4N17wifi_sta_config_t2gwE"></a>

    <a id="_CPPv3N17wifi_sta_config_t2gwE"></a> <a id="_CPPv2N17wifi_sta_config_t2gwE"></a> <a id="wifi_sta_config_t::gw__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gac4f04c29a35bf6daba23e83b762b74e3"></a> uint8\_t gw\[4\]
    :   GW address

    <a id="_CPPv4N17wifi_sta_config_t4dns1E"></a>

    <a id="_CPPv3N17wifi_sta_config_t4dns1E"></a> <a id="_CPPv2N17wifi_sta_config_t4dns1E"></a> <a id="wifi_sta_config_t::dns1__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga713bc11340fc5d6316e2c35e1b1c4cb8"></a> uint8\_t dns1\[4\]
    :   DNS address

    <a id="_CPPv4N17wifi_sta_config_t23is_not_support_auto_fciE"></a>

    <a id="_CPPv3N17wifi_sta_config_t23is_not_support_auto_fciE"></a> <a id="_CPPv2N17wifi_sta_config_t23is_not_support_auto_fciE"></a> <a id="wifi_sta_config_t::is_not_support_auto_fci__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga55f295affe3bf20a237d624ca251858e"></a> uint8\_t is\_not\_support\_auto\_fci
    :   is not support auto fast connect

    <a id="_CPPv4N17wifi_sta_config_t20is_user_fast_connectE"></a>

    <a id="_CPPv3N17wifi_sta_config_t20is_user_fast_connectE"></a> <a id="_CPPv2N17wifi_sta_config_t20is_user_fast_connectE"></a> <a id="wifi_sta_config_t::is_user_fast_connect__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gacd6b220c8e41f8c57196cf3275782d1a"></a> uint8\_t is\_user\_fast\_connect
    :   is use user fast connect

    <a id="_CPPv4N17wifi_sta_config_t3pmfE"></a>

    <a id="_CPPv3N17wifi_sta_config_t3pmfE"></a> <a id="_CPPv2N17wifi_sta_config_t3pmfE"></a> <a id="wifi_sta_config_t::pmf__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaff5c71052eeb8d2423993fa916a0446c"></a> uint8\_t pmf
    :   is support pmf

    <a id="_CPPv4N17wifi_sta_config_t2tkE"></a>

    <a id="_CPPv3N17wifi_sta_config_t2tkE"></a> <a id="_CPPv2N17wifi_sta_config_t2tkE"></a> <a id="wifi_sta_config_t::tk__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga79b2248b38ac81032f908df700a6d5d4"></a> uint8\_t tk\[16\]
    :   WPA3 tk key

    <a id="_CPPv4N17wifi_sta_config_t20auto_reconnect_countE"></a>

    <a id="_CPPv3N17wifi_sta_config_t20auto_reconnect_countE"></a> <a id="_CPPv2N17wifi_sta_config_t20auto_reconnect_countE"></a> <a id="wifi_sta_config_t::auto_reconnect_count__i"></a> <a id="group__bk__api__wifi__v2_1ga7a9d2fe502ba1e58ca5d7595dbc2a502"></a> int auto\_reconnect\_count
    :   auto reconnect max count, 0 for always reconnect

    <a id="_CPPv4N17wifi_sta_config_t22auto_reconnect_timeoutE"></a>

    <a id="_CPPv3N17wifi_sta_config_t22auto_reconnect_timeoutE"></a> <a id="_CPPv2N17wifi_sta_config_t22auto_reconnect_timeoutE"></a> <a id="wifi_sta_config_t::auto_reconnect_timeout__i"></a> <a id="group__bk__api__wifi__v2_1gae5f74786c5667ad5f0bb1ad862688e49"></a> int auto\_reconnect\_timeout
    :   auto reconnect timeout in secs, 0 for no timeout

    <a id="_CPPv4N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a>

    <a id="_CPPv3N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a> <a id="_CPPv2N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a> <a id="wifi_sta_config_t::disable_auto_reconnect_after_disconnect__b"></a> <a id="group__bk__api__wifi__v2_1gacd8a95fa035752187cbcfc388d0df9f6"></a> bool disable\_auto\_reconnect\_after\_disconnect
    :   disable auto reconnect if deauth/disassoc by AP when in connected state

    <a id="_CPPv4N17wifi_sta_config_t9freq_listE"></a>

    <a id="_CPPv3N17wifi_sta_config_t9freq_listE"></a> <a id="_CPPv2N17wifi_sta_config_t9freq_listE"></a> <a id="wifi_sta_config_t::freq_list__iA"></a> <a id="group__bk__api__wifi__v2_1gae880baf306344af8c5dde7141ed3c30b"></a> int freq\_list\[WIFI\_2BAND\_MAX\_CHAN\_NUM \+ 1\]
    :   optional zero-terminated array of frequencies in megahertz (MHz) to allow for selecting the BSS

    <a id="_CPPv4N17wifi_sta_config_t8reservedE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8reservedE"></a> <a id="_CPPv2N17wifi_sta_config_t8reservedE"></a> <a id="wifi_sta_config_t::reserved__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga2d40ae19dd768487ecdf0fa5b09c2f7c"></a> uint8\_t reserved\[32\]
    :   reserved, **must set to 0**

<a id="_CPPv423wifi_linkstate_reason_t"></a>

<a id="_CPPv323wifi_linkstate_reason_t"></a> <a id="_CPPv223wifi_linkstate_reason_t"></a> <a id="wifi_linkstate_reason_t"></a> <a id="structwifi__linkstate__reason__t"></a> struct wifi\_linkstate\_reason\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23wifi_linkstate_reason_t5stateE"></a>

    <a id="_CPPv3N23wifi_linkstate_reason_t5stateE"></a> <a id="_CPPv2N23wifi_linkstate_reason_t5stateE"></a> <a id="wifi_linkstate_reason_t::state__wifi_link_state_t"></a> <a id="group__bk__api__wifi__v2_1ga29e61eb4dd05859b9598bf6d36edca39"></a> [wifi\_link\_state\_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state
    :   Wifi linkstate

    <a id="_CPPv4N23wifi_linkstate_reason_t11reason_codeE"></a>

    <a id="_CPPv3N23wifi_linkstate_reason_t11reason_codeE"></a> <a id="_CPPv2N23wifi_linkstate_reason_t11reason_codeE"></a> <a id="wifi_linkstate_reason_t::reason_code__wifi_err_reason_t"></a> <a id="group__bk__api__wifi__v2_1ga626b24ac39702a34da66ab39b941a62c"></a> [wifi\_err\_reason\_t](#_CPPv417wifi_err_reason_t "wifi_err_reason_t") reason\_code
    :   Wifi disconnect reason code, success will be WIFI\_REASON\_MAX

<a id="_CPPv418wifi_link_status_t"></a>

<a id="_CPPv318wifi_link_status_t"></a> <a id="_CPPv218wifi_link_status_t"></a> <a id="wifi_link_status_t"></a> <a id="structwifi__link__status__t"></a> struct wifi\_link\_status\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_link_status_t5stateE"></a>

    <a id="_CPPv3N18wifi_link_status_t5stateE"></a> <a id="_CPPv2N18wifi_link_status_t5stateE"></a> <a id="wifi_link_status_t::state__wifi_link_state_t"></a> <a id="group__bk__api__wifi__v2_1gae2217f198571149fd1ea194e2987fa9a"></a> [wifi\_link\_state\_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state
    :   The WiFi connection status

    <a id="_CPPv4N18wifi_link_status_t3aidE"></a>

    <a id="_CPPv3N18wifi_link_status_t3aidE"></a> <a id="_CPPv2N18wifi_link_status_t3aidE"></a> <a id="wifi_link_status_t::aid__i"></a> <a id="group__bk__api__wifi__v2_1gaf7f1f46b82ff710670cab9ff4fb6d89b"></a> int aid
    :   STA AID

    <a id="_CPPv4N18wifi_link_status_t4rssiE"></a>

    <a id="_CPPv3N18wifi_link_status_t4rssiE"></a> <a id="_CPPv2N18wifi_link_status_t4rssiE"></a> <a id="wifi_link_status_t::rssi__i"></a> <a id="group__bk__api__wifi__v2_1ga726485b304bcbeacf81e8c199e4d9650"></a> int rssi
    :   The RSSI of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t4ssidE"></a>

    <a id="_CPPv3N18wifi_link_status_t4ssidE"></a> <a id="_CPPv2N18wifi_link_status_t4ssidE"></a> <a id="wifi_link_status_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1ga931982c6fb3f4b31f23bcb0f301fff23"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t5bssidE"></a>

    <a id="_CPPv3N18wifi_link_status_t5bssidE"></a> <a id="_CPPv2N18wifi_link_status_t5bssidE"></a> <a id="wifi_link_status_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga931ec371d60d095e55035f9601a032aa"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t7channelE"></a>

    <a id="_CPPv3N18wifi_link_status_t7channelE"></a> <a id="_CPPv2N18wifi_link_status_t7channelE"></a> <a id="wifi_link_status_t::channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga2e6648f0d5426138954d395d3c181c83"></a> uint8\_t channel
    :   Primary channel of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t8securityE"></a>

    <a id="_CPPv3N18wifi_link_status_t8securityE"></a> <a id="_CPPv2N18wifi_link_status_t8securityE"></a> <a id="wifi_link_status_t::security__wifi_security_t"></a> <a id="group__bk__api__wifi__v2_1ga1932604f49a07b22ba838dd0dd1da52c"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t8passwordE"></a>

    <a id="_CPPv3N18wifi_link_status_t8passwordE"></a> <a id="_CPPv2N18wifi_link_status_t8passwordE"></a> <a id="wifi_link_status_t::password__cA"></a> <a id="group__bk__api__wifi__v2_1ga412b62929f6c157e3ae980111bd41317"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Passord of AP the BK STA is connected

<a id="_CPPv418wifi_scan_config_t"></a>

<a id="_CPPv318wifi_scan_config_t"></a> <a id="_CPPv218wifi_scan_config_t"></a> <a id="wifi_scan_config_t"></a> <a id="structwifi__scan__config__t"></a> struct wifi\_scan\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_scan_config_t4ssidE"></a>

    <a id="_CPPv3N18wifi_scan_config_t4ssidE"></a> <a id="_CPPv2N18wifi_scan_config_t4ssidE"></a> <a id="wifi_scan_config_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1gace0f6592172fb7045603763e5691ac8a"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID to be scaned

    <a id="_CPPv4N18wifi_scan_config_t5bssidE"></a>

    <a id="_CPPv3N18wifi_scan_config_t5bssidE"></a> <a id="_CPPv2N18wifi_scan_config_t5bssidE"></a> <a id="wifi_scan_config_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga50a490eb3a74ac19605f446310ae2f88"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID to be scaned

    <a id="_CPPv4N18wifi_scan_config_t9scan_typeE"></a>

    <a id="_CPPv3N18wifi_scan_config_t9scan_typeE"></a> <a id="_CPPv2N18wifi_scan_config_t9scan_typeE"></a> <a id="wifi_scan_config_t::scan_type__u8"></a> <a id="group__bk__api__wifi__v2_1gaec9deac988493bc07f155f9605abef38"></a> u8 scan\_type
    :   0: active scan; 1: passive scan

    <a id="_CPPv4N18wifi_scan_config_t8chan_cntE"></a>

    <a id="_CPPv3N18wifi_scan_config_t8chan_cntE"></a> <a id="_CPPv2N18wifi_scan_config_t8chan_cntE"></a> <a id="wifi_scan_config_t::chan_cnt__u8"></a> <a id="group__bk__api__wifi__v2_1gaed43400cea3a9a05f3871514068869fa"></a> u8 chan\_cnt
    :   scan channel cnt

    <a id="_CPPv4N18wifi_scan_config_t7chan_nbE"></a>

    <a id="_CPPv3N18wifi_scan_config_t7chan_nbE"></a> <a id="_CPPv2N18wifi_scan_config_t7chan_nbE"></a> <a id="wifi_scan_config_t::chan_nb__u8A"></a> <a id="group__bk__api__wifi__v2_1ga24778fba9ded56ca8eaad50d30d04706"></a> u8 chan\_nb\[WIFI\_2BAND\_MAX\_CHAN\_NUM\]
    :   scan channel number 2.4g\+5g

    <a id="_CPPv4N18wifi_scan_config_t8durationE"></a>

    <a id="_CPPv3N18wifi_scan_config_t8durationE"></a> <a id="_CPPv2N18wifi_scan_config_t8durationE"></a> <a id="wifi_scan_config_t::duration__u32"></a> <a id="group__bk__api__wifi__v2_1ga213bbb8221eb054e2cdee0f88eeadecf"></a> u32 duration
    :   scan duration,ms

<a id="_CPPv419wifi_scan_ap_info_t"></a>

<a id="_CPPv319wifi_scan_ap_info_t"></a> <a id="_CPPv219wifi_scan_ap_info_t"></a> <a id="wifi_scan_ap_info_t"></a> <a id="structwifi__scan__ap__info__t"></a> struct wifi\_scan\_ap\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19wifi_scan_ap_info_t4ssidE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t4ssidE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t4ssidE"></a> <a id="wifi_scan_ap_info_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1gaa4c204effe106eddb1aeb5ef9c8b25d2"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t5bssidE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t5bssidE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t5bssidE"></a> <a id="wifi_scan_ap_info_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gae3869d94dd1302a1c6f190f5f7f8995a"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t4rssiE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t4rssiE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t4rssiE"></a> <a id="wifi_scan_ap_info_t::rssi__i"></a> <a id="group__bk__api__wifi__v2_1ga355b6900c5c6e658a5fdcb17d96f67ad"></a> int rssi
    :   RSSI of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t7channelE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t7channelE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t7channelE"></a> <a id="wifi_scan_ap_info_t::channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gae4819d917122c72c505dc3240199d28e"></a> uint8\_t channel
    :   The channel of the AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t8securityE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t8securityE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t8securityE"></a> <a id="wifi_scan_ap_info_t::security__wifi_security_t"></a> <a id="group__bk__api__wifi__v2_1gad11455feb4df0ac53c237f659d8b9e4d"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   The security type of the AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t9is_bridgeE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t9is_bridgeE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t9is_bridgeE"></a> <a id="wifi_scan_ap_info_t::is_bridge__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaa1a3fa995517b253e769ef90ac4f2008"></a> uint8\_t is\_bridge
    :   is AP support bridge

    <a id="_CPPv4N19wifi_scan_ap_info_t8reservedE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t8reservedE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t8reservedE"></a> <a id="wifi_scan_ap_info_t::reserved__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga03022794ede1f6e1b2b472fd4f7d8c9e"></a> uint8\_t reserved\[16\]
    :   Reserved, **must be zero**

<a id="_CPPv418wifi_scan_result_t"></a>

<a id="_CPPv318wifi_scan_result_t"></a> <a id="_CPPv218wifi_scan_result_t"></a> <a id="wifi_scan_result_t"></a> <a id="structwifi__scan__result__t"></a> struct wifi\_scan\_result\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_scan_result_t6ap_numE"></a>

    <a id="_CPPv3N18wifi_scan_result_t6ap_numE"></a> <a id="_CPPv2N18wifi_scan_result_t6ap_numE"></a> <a id="wifi_scan_result_t::ap_num__i"></a> <a id="group__bk__api__wifi__v2_1gababf0f253ac248d67f7dd25db0452287"></a> int ap\_num
    :   The number of AP found by scan

    <a id="_CPPv4N18wifi_scan_result_t3apsE"></a>

    <a id="_CPPv3N18wifi_scan_result_t3apsE"></a> <a id="_CPPv2N18wifi_scan_result_t3apsE"></a> <a id="wifi_scan_result_t::aps__wifi_scan_ap_info_tP"></a> <a id="group__bk__api__wifi__v2_1gafc7ec251f26525956b4d710092012c04"></a> [wifi\_scan\_ap\_info\_t](#_CPPv419wifi_scan_ap_info_t "wifi_scan_ap_info_t") \*aps
    :   The APs found by scan

<a id="_CPPv416wifi_ap_config_t"></a>

<a id="_CPPv316wifi_ap_config_t"></a> <a id="_CPPv216wifi_ap_config_t"></a> <a id="wifi_ap_config_t"></a> <a id="structwifi__ap__config__t"></a> struct wifi\_ap\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16wifi_ap_config_t4ssidE"></a>

    <a id="_CPPv3N16wifi_ap_config_t4ssidE"></a> <a id="_CPPv2N16wifi_ap_config_t4ssidE"></a> <a id="wifi_ap_config_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1gaa931247a4b99b7bd4f9e364c697533f3"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   The SSID of BK AP

    <a id="_CPPv4N16wifi_ap_config_t8passwordE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8passwordE"></a> <a id="_CPPv2N16wifi_ap_config_t8passwordE"></a> <a id="wifi_ap_config_t::password__cA"></a> <a id="group__bk__api__wifi__v2_1ga711f1a365b4b3809fa13adcbeae8608d"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Password of BK AP, ignored in an open system.

    <a id="_CPPv4N16wifi_ap_config_t7channelE"></a>

    <a id="_CPPv3N16wifi_ap_config_t7channelE"></a> <a id="_CPPv2N16wifi_ap_config_t7channelE"></a> <a id="wifi_ap_config_t::channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gab4005256cbe734b1a0b54c6c50609db3"></a> uint8\_t channel
    :   The channel of BK AP, 0 indicates default TODO

    <a id="_CPPv4N16wifi_ap_config_t8securityE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8securityE"></a> <a id="_CPPv2N16wifi_ap_config_t8securityE"></a> <a id="wifi_ap_config_t::security__wifi_security_t"></a> <a id="group__bk__api__wifi__v2_1gaed1f22f0ba8a8d943ed574545a103556"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security type of BK AP, default value TODO

    <a id="_CPPv4N16wifi_ap_config_t6hiddenE"></a>

    <a id="_CPPv3N16wifi_ap_config_t6hiddenE"></a> <a id="_CPPv2N16wifi_ap_config_t6hiddenE"></a> <a id="wifi_ap_config_t::hidden__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga4e43520cd26178b2eb1b537fe04593be"></a> uint8\_t hidden
    :   Whether the BK AP is hidden

    <a id="_CPPv4N16wifi_ap_config_t3acsE"></a>

    <a id="_CPPv3N16wifi_ap_config_t3acsE"></a> <a id="_CPPv2N16wifi_ap_config_t3acsE"></a> <a id="wifi_ap_config_t::acs__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga365e2514f23c988ac1fe5e41a2326e3b"></a> uint8\_t acs
    :   Whether Auto Channel Selection is enabled

    <a id="_CPPv4N16wifi_ap_config_t6bridgeE"></a>

    <a id="_CPPv3N16wifi_ap_config_t6bridgeE"></a> <a id="_CPPv2N16wifi_ap_config_t6bridgeE"></a> <a id="wifi_ap_config_t::bridge__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga2d06f1c87dfeff7022091c584a211ba7"></a> uint8\_t bridge
    :   BK AP support bridge

    <a id="_CPPv4N16wifi_ap_config_t8vsie_lenE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8vsie_lenE"></a> <a id="_CPPv2N16wifi_ap_config_t8vsie_lenE"></a> <a id="wifi_ap_config_t::vsie_len__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga70a682fa907176b7a2c044e69204cd67"></a> uint8\_t vsie\_len
    :   Beacon/ProbeResp Vendor Specific IE len

    <a id="_CPPv4N16wifi_ap_config_t4vsieE"></a>

    <a id="_CPPv3N16wifi_ap_config_t4vsieE"></a> <a id="_CPPv2N16wifi_ap_config_t4vsieE"></a> <a id="wifi_ap_config_t::vsie__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gaaccfac4bdaecd48892a9b40dd0d9376d"></a> uint8\_t vsie\[255\]
    :   Beacon/ProbeResp Vendor Specific IE

    <a id="_CPPv4N16wifi_ap_config_t7max_conE"></a>

    <a id="_CPPv3N16wifi_ap_config_t7max_conE"></a> <a id="_CPPv2N16wifi_ap_config_t7max_conE"></a> <a id="wifi_ap_config_t::max_con__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga116921d43539d5acde0b878b8b0b61bb"></a> uint8\_t max\_con
    :   Max number of stations allowed to connect to BK AP, TODO default value?

    <a id="_CPPv4N16wifi_ap_config_t8reservedE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8reservedE"></a> <a id="_CPPv2N16wifi_ap_config_t8reservedE"></a> <a id="wifi_ap_config_t::reserved__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gad67b68cd2431f45036aec30c7d48c4ea"></a> uint8\_t reserved\[32\]
    :   Reserved, **must be zero**

<a id="_CPPv411wlan_ap_sta"></a>

<a id="_CPPv311wlan_ap_sta"></a> <a id="_CPPv211wlan_ap_sta"></a> <a id="wlan_ap_sta"></a> <a id="structwlan__ap__sta"></a> struct wlan\_ap\_sta
:   Wlan station information definition.

<a id="_CPPv412wlan_ap_stas"></a>

<a id="_CPPv312wlan_ap_stas"></a> <a id="_CPPv212wlan_ap_stas"></a> <a id="wlan_ap_stas"></a> <a id="structwlan__ap__stas"></a> struct wlan\_ap\_stas
:   Wlan connected stations information definition.

<a id="_CPPv412wlan_ap_vsie"></a>

<a id="_CPPv312wlan_ap_vsie"></a> <a id="_CPPv212wlan_ap_vsie"></a> <a id="wlan_ap_vsie"></a> <a id="structwlan__ap__vsie"></a> struct wlan\_ap\_vsie
:   softap beacon/probe response’s vendor IEs Dynamic change softap’s vendor specific IEs.

<a id="_CPPv413wlan_sta_vsie"></a>

<a id="_CPPv313wlan_sta_vsie"></a> <a id="_CPPv213wlan_sta_vsie"></a> <a id="wlan_sta_vsie"></a> <a id="structwlan__sta__vsie"></a> struct wlan\_sta\_vsie
:   STA vendor IEs for (re)assoc, scan, p2p, p2p go, etc. Dynamic change STA’s vendor specific IEs.

<a id="_CPPv421wifi_monitor_config_t"></a>

<a id="_CPPv321wifi_monitor_config_t"></a> <a id="_CPPv221wifi_monitor_config_t"></a> <a id="wifi_monitor_config_t"></a> <a id="structwifi__monitor__config__t"></a> struct wifi\_monitor\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21wifi_monitor_config_t14rx_mcast_frameE"></a>

    <a id="_CPPv3N21wifi_monitor_config_t14rx_mcast_frameE"></a> <a id="_CPPv2N21wifi_monitor_config_t14rx_mcast_frameE"></a> <a id="wifi_monitor_config_t::rx_mcast_frame__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga11e18caf7431f8dffb6fd9d3f7f8a2d8"></a> uint32\_t rx\_mcast\_frame
    :   Set this bit to enable callback to receive multicast/broadcast

    <a id="_CPPv4N21wifi_monitor_config_t12rx_dup_frameE"></a>

    <a id="_CPPv3N21wifi_monitor_config_t12rx_dup_frameE"></a> <a id="_CPPv2N21wifi_monitor_config_t12rx_dup_frameE"></a> <a id="wifi_monitor_config_t::rx_dup_frame__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga2e2175ad44c90e1604dc2d15282cf3d9"></a> uint32\_t rx\_dup\_frame
    :   Set this bit to enable callback to receive the duplicated

    <a id="_CPPv4N21wifi_monitor_config_t8reservedE"></a>

    <a id="_CPPv3N21wifi_monitor_config_t8reservedE"></a> <a id="_CPPv2N21wifi_monitor_config_t8reservedE"></a> <a id="wifi_monitor_config_t::reserved__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga55182a160c0a3e24d43e8ed4af1e6b97"></a> uint32\_t reserved
    :   Reserved bits, **must set to 0**

<a id="_CPPv417wifi_frame_info_t"></a>

<a id="_CPPv317wifi_frame_info_t"></a> <a id="_CPPv217wifi_frame_info_t"></a> <a id="wifi_frame_info_t"></a> <a id="structwifi__frame__info__t"></a> struct wifi\_frame\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_frame_info_t4rssiE"></a>

    <a id="_CPPv3N17wifi_frame_info_t4rssiE"></a> <a id="_CPPv2N17wifi_frame_info_t4rssiE"></a> <a id="wifi_frame_info_t::rssi__i"></a> <a id="group__bk__api__wifi__v2_1ga6aff7f1e26a5ff819a3409d77e0b5521"></a> int rssi
    :   RSSI of the received frame in monitor mode

    <a id="_CPPv4N17wifi_frame_info_t6tsf_loE"></a>

    <a id="_CPPv3N17wifi_frame_info_t6tsf_loE"></a> <a id="_CPPv2N17wifi_frame_info_t6tsf_loE"></a> <a id="wifi_frame_info_t::tsf_lo__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gada0014a44f4f83a4ebf0a7a5a02942ee"></a> uint32\_t tsf\_lo
    :   Total length for the MPDU transfer

    <a id="_CPPv4N17wifi_frame_info_t6tsf_hiE"></a>

    <a id="_CPPv3N17wifi_frame_info_t6tsf_hiE"></a> <a id="_CPPv2N17wifi_frame_info_t6tsf_hiE"></a> <a id="wifi_frame_info_t::tsf_hi__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga3ea264c6284bdf8f027f77c28e94c986"></a> uint32\_t tsf\_hi
    :   TSF Low

    <a id="_CPPv4N17wifi_frame_info_t8recvec1aE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec1aE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec1aE"></a> <a id="wifi_frame_info_t::recvec1a__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gae0d333eb5879ed9daac99b9179407543"></a> uint32\_t recvec1a
    :   TSF High

    <a id="_CPPv4N17wifi_frame_info_t8recvec1bE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec1bE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec1bE"></a> <a id="wifi_frame_info_t::recvec1b__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga6987bcb47b35710458ce14d361276693"></a> uint32\_t recvec1b
    :   Receive Vector 1

    <a id="_CPPv4N17wifi_frame_info_t8recvec1cE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec1cE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec1cE"></a> <a id="wifi_frame_info_t::recvec1c__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gab9665aa96da68312cbb460de28151bd4"></a> uint32\_t recvec1c
    :   Receive Vector 1

    <a id="_CPPv4N17wifi_frame_info_t8recvec1dE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec1dE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec1dE"></a> <a id="wifi_frame_info_t::recvec1d__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga47e2615924af549eb291336b8fc3d8c7"></a> uint32\_t recvec1d
    :   Receive Vector 1

    <a id="_CPPv4N17wifi_frame_info_t8recvec2aE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec2aE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec2aE"></a> <a id="wifi_frame_info_t::recvec2a__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga60215dd424e32f2a7ceadfa5b649023c"></a> uint32\_t recvec2a
    :   Receive Vector 1

    <a id="_CPPv4N17wifi_frame_info_t8recvec2bE"></a>

    <a id="_CPPv3N17wifi_frame_info_t8recvec2bE"></a> <a id="_CPPv2N17wifi_frame_info_t8recvec2bE"></a> <a id="wifi_frame_info_t::recvec2b__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga7ab1c5ff3511be53769795a05b238268"></a> uint32\_t recvec2b
    :   Receive Vector 2

<a id="_CPPv418wifi_rlk_chan_info"></a>

<a id="_CPPv318wifi_rlk_chan_info"></a> <a id="_CPPv218wifi_rlk_chan_info"></a> <a id="wifi_rlk_chan_info"></a> <a id="structwifi__rlk__chan__info"></a> struct wifi\_rlk\_chan\_info
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_rlk_chan_info4freqE"></a>

    <a id="_CPPv3N18wifi_rlk_chan_info4freqE"></a> <a id="_CPPv2N18wifi_rlk_chan_info4freqE"></a> <a id="wifi_rlk_chan_info::freq__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga7c1462fe97e388cb8d4e3f9e37be6646"></a> uint16\_t freq
    :   Frequency of the channel.

    <a id="_CPPv4N18wifi_rlk_chan_info9noise_dbmE"></a>

    <a id="_CPPv3N18wifi_rlk_chan_info9noise_dbmE"></a> <a id="_CPPv2N18wifi_rlk_chan_info9noise_dbmE"></a> <a id="wifi_rlk_chan_info::noise_dbm__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga71838c4db2e6c7cc1291950e256a2999"></a> uint8\_t noise\_dbm
    :   Noise in dbm.

    <a id="_CPPv4N18wifi_rlk_chan_info12chan_time_msE"></a>

    <a id="_CPPv3N18wifi_rlk_chan_info12chan_time_msE"></a> <a id="_CPPv2N18wifi_rlk_chan_info12chan_time_msE"></a> <a id="wifi_rlk_chan_info::chan_time_ms__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga1bed807c7db19d660083dc3b34a68f77"></a> uint32\_t chan\_time\_ms
    :   Amount of time spent of the channel (in ms)

    <a id="_CPPv4N18wifi_rlk_chan_info17chan_time_busy_msE"></a>

    <a id="_CPPv3N18wifi_rlk_chan_info17chan_time_busy_msE"></a> <a id="_CPPv2N18wifi_rlk_chan_info17chan_time_busy_msE"></a> <a id="wifi_rlk_chan_info::chan_time_busy_ms__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gacb6f1d2e071991c57883e997c8f4aa7b"></a> uint32\_t chan\_time\_busy\_ms
    :   Amount of time the primary channel was sensed busy.

<a id="_CPPv418wifi_rlk_base_info"></a>

<a id="_CPPv318wifi_rlk_base_info"></a> <a id="_CPPv218wifi_rlk_base_info"></a> <a id="wifi_rlk_base_info"></a> <a id="structwifi__rlk__base__info"></a> struct wifi\_rlk\_base\_info

<a id="_CPPv420wifi_filter_config_t"></a>

<a id="_CPPv320wifi_filter_config_t"></a> <a id="_CPPv220wifi_filter_config_t"></a> <a id="wifi_filter_config_t"></a> <a id="structwifi__filter__config__t"></a> struct wifi\_filter\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20wifi_filter_config_t19rx_all_default_mgmtE"></a>

    <a id="_CPPv3N20wifi_filter_config_t19rx_all_default_mgmtE"></a> <a id="_CPPv2N20wifi_filter_config_t19rx_all_default_mgmtE"></a> <a id="wifi_filter_config_t::rx_all_default_mgmt__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga687c38bc58f5cdc6077eb33cf3062345"></a> uint32\_t rx\_all\_default\_mgmt
    :   Set the bit to enable the callback to receive all management frame recived by WiFi driver

    <a id="_CPPv4N20wifi_filter_config_t12rx_probe_reqE"></a>

    <a id="_CPPv3N20wifi_filter_config_t12rx_probe_reqE"></a> <a id="_CPPv2N20wifi_filter_config_t12rx_probe_reqE"></a> <a id="wifi_filter_config_t::rx_probe_req__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga4a90c000675f2cf4809dfbbfdc97b1e9"></a> uint32\_t rx\_probe\_req
    :   Set the bit to enable the callback to receive probe request

    <a id="_CPPv4N20wifi_filter_config_t12rx_probe_rspE"></a>

    <a id="_CPPv3N20wifi_filter_config_t12rx_probe_rspE"></a> <a id="_CPPv2N20wifi_filter_config_t12rx_probe_rspE"></a> <a id="wifi_filter_config_t::rx_probe_rsp__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gafe83e7acbd6d9fc4e1f9143440bbcff7"></a> uint32\_t rx\_probe\_rsp
    :   Set the bit to enable the callback to receive probe response

    <a id="_CPPv4N20wifi_filter_config_t13rx_all_beaconE"></a>

    <a id="_CPPv3N20wifi_filter_config_t13rx_all_beaconE"></a> <a id="_CPPv2N20wifi_filter_config_t13rx_all_beaconE"></a> <a id="wifi_filter_config_t::rx_all_beacon__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gafd9a6181c3ccc3c6a5d94d7bf4efe985"></a> uint32\_t rx\_all\_beacon
    :   Set the bit to enable the callback to receive all beacon

    <a id="_CPPv4N20wifi_filter_config_t9rx_actionE"></a>

    <a id="_CPPv3N20wifi_filter_config_t9rx_actionE"></a> <a id="_CPPv2N20wifi_filter_config_t9rx_actionE"></a> <a id="wifi_filter_config_t::rx_action__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaff61cbdfa1cb9c7735ff255ce9fd9b48"></a> uint32\_t rx\_action
    :   Set the bit to enable the callback to receive action frame

    <a id="_CPPv4N20wifi_filter_config_t8reservedE"></a>

    <a id="_CPPv3N20wifi_filter_config_t8reservedE"></a> <a id="_CPPv2N20wifi_filter_config_t8reservedE"></a> <a id="wifi_filter_config_t::reserved__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga973df8eff99eb428b0c3e929946c3543"></a> uint32\_t reserved
    :   Reserved bits, **must set to 0**

<a id="_CPPv414wifi_country_t"></a>

<a id="_CPPv314wifi_country_t"></a> <a id="_CPPv214wifi_country_t"></a> <a id="wifi_country_t"></a> <a id="structwifi__country__t"></a> struct wifi\_country\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14wifi_country_t2ccE"></a>

    <a id="_CPPv3N14wifi_country_t2ccE"></a> <a id="_CPPv2N14wifi_country_t2ccE"></a> <a id="wifi_country_t::cc__cA"></a> <a id="group__bk__api__wifi__v2_1ga1fd01869f4230eddd580637171e2e5cf"></a> char cc\[3\]
    :   country code string

    <a id="_CPPv4N14wifi_country_t5schanE"></a>

    <a id="_CPPv3N14wifi_country_t5schanE"></a> <a id="_CPPv2N14wifi_country_t5schanE"></a> <a id="wifi_country_t::schan__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaf260339dd254a65b93a4e1d65576b117"></a> uint8\_t schan
    :   start channel

    <a id="_CPPv4N14wifi_country_t5nchanE"></a>

    <a id="_CPPv3N14wifi_country_t5nchanE"></a> <a id="_CPPv2N14wifi_country_t5nchanE"></a> <a id="wifi_country_t::nchan__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga1c129465b6bf5c803636dc05c21828dd"></a> uint8\_t nchan
    :   total channel number

    <a id="_CPPv4N14wifi_country_t12max_tx_powerE"></a>

    <a id="_CPPv3N14wifi_country_t12max_tx_powerE"></a> <a id="_CPPv2N14wifi_country_t12max_tx_powerE"></a> <a id="wifi_country_t::max_tx_power__int8_t"></a> <a id="group__bk__api__wifi__v2_1ga47a74c0fedee026097b4707efb792632"></a> int8\_t max\_tx\_power
    :   maximum tx power

    <a id="_CPPv4N14wifi_country_t6policyE"></a>

    <a id="_CPPv3N14wifi_country_t6policyE"></a> <a id="_CPPv2N14wifi_country_t6policyE"></a> <a id="wifi_country_t::policy__wifi_country_policy_t"></a> <a id="group__bk__api__wifi__v2_1ga80f2e1485534d43ae527f413d9c3095d"></a> [wifi\_country\_policy\_t](#_CPPv421wifi_country_policy_t "wifi_country_policy_t") policy
    :   country policy

<a id="_CPPv422wifi_event_scan_done_t"></a>

<a id="_CPPv322wifi_event_scan_done_t"></a> <a id="_CPPv222wifi_event_scan_done_t"></a> <a id="wifi_event_scan_done_t"></a> <a id="structwifi__event__scan__done__t"></a> struct wifi\_event\_scan\_done\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22wifi_event_scan_done_t7scan_idE"></a>

    <a id="_CPPv3N22wifi_event_scan_done_t7scan_idE"></a> <a id="_CPPv2N22wifi_event_scan_done_t7scan_idE"></a> <a id="wifi_event_scan_done_t::scan_id__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga20b753514128873656807dde26c25806"></a> uint32\_t scan\_id
    :   Scan ID

    <a id="_CPPv4N22wifi_event_scan_done_t13scan_use_timeE"></a>

    <a id="_CPPv3N22wifi_event_scan_done_t13scan_use_timeE"></a> <a id="_CPPv2N22wifi_event_scan_done_t13scan_use_timeE"></a> <a id="wifi_event_scan_done_t::scan_use_time__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga1f5fce0cd516e7bcda758e6ee8bf12a7"></a> uint32\_t scan\_use\_time
    :   scan time. us

    <a id="_CPPv4N22wifi_event_scan_done_t13last_scan_reqE"></a>

    <a id="_CPPv3N22wifi_event_scan_done_t13last_scan_reqE"></a> <a id="_CPPv2N22wifi_event_scan_done_t13last_scan_reqE"></a> <a id="wifi_event_scan_done_t::last_scan_req__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga069e1f3e939a45bf8843c9e400d3ddc5"></a> uint32\_t last\_scan\_req
    :   last scan request

<a id="_CPPv426wifi_event_network_found_t"></a>

<a id="_CPPv326wifi_event_network_found_t"></a> <a id="_CPPv226wifi_event_network_found_t"></a> <a id="wifi_event_network_found_t"></a> <a id="structwifi__event__network__found__t"></a> struct wifi\_event\_network\_found\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26wifi_event_network_found_t4ssidE"></a>

    <a id="_CPPv3N26wifi_event_network_found_t4ssidE"></a> <a id="_CPPv2N26wifi_event_network_found_t4ssidE"></a> <a id="wifi_event_network_found_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1gad59ad54d291e08b2cc012bb52b9c0f5b"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID found to be connected

    <a id="_CPPv4N26wifi_event_network_found_t5bssidE"></a>

    <a id="_CPPv3N26wifi_event_network_found_t5bssidE"></a> <a id="_CPPv2N26wifi_event_network_found_t5bssidE"></a> <a id="wifi_event_network_found_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga4af63f621b2cfa3dff458547c67d9529"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID found to be connected

<a id="_CPPv426wifi_event_sta_connected_t"></a>

<a id="_CPPv326wifi_event_sta_connected_t"></a> <a id="_CPPv226wifi_event_sta_connected_t"></a> <a id="wifi_event_sta_connected_t"></a> <a id="structwifi__event__sta__connected__t"></a> struct wifi\_event\_sta\_connected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26wifi_event_sta_connected_t4ssidE"></a>

    <a id="_CPPv3N26wifi_event_sta_connected_t4ssidE"></a> <a id="_CPPv2N26wifi_event_sta_connected_t4ssidE"></a> <a id="wifi_event_sta_connected_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1gae44a1f398d1e05aa00444cc1aa4aee5a"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of connected AP

    <a id="_CPPv4N26wifi_event_sta_connected_t5bssidE"></a>

    <a id="_CPPv3N26wifi_event_sta_connected_t5bssidE"></a> <a id="_CPPv2N26wifi_event_sta_connected_t5bssidE"></a> <a id="wifi_event_sta_connected_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga604d35bc824aa92b370f478c4066ed53"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of connected AP

    <a id="_CPPv4N26wifi_event_sta_connected_t4freqE"></a>

    <a id="_CPPv3N26wifi_event_sta_connected_t4freqE"></a> <a id="_CPPv2N26wifi_event_sta_connected_t4freqE"></a> <a id="wifi_event_sta_connected_t::freq__i"></a> <a id="group__bk__api__wifi__v2_1gaf530558e8d4a90c7db03e19fdba16648"></a> int freq
    :   frequency of connected AP

<a id="_CPPv429wifi_event_sta_disconnected_t"></a>

<a id="_CPPv329wifi_event_sta_disconnected_t"></a> <a id="_CPPv229wifi_event_sta_disconnected_t"></a> <a id="wifi_event_sta_disconnected_t"></a> <a id="structwifi__event__sta__disconnected__t"></a> struct wifi\_event\_sta\_disconnected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a> <a id="wifi_event_sta_disconnected_t::disconnect_reason__i"></a> <a id="group__bk__api__wifi__v2_1ga9b210ef1d662b2a29629754f7d507774"></a> int disconnect\_reason
    :   Disconnect reason of BK STA

    <a id="_CPPv4N29wifi_event_sta_disconnected_t15local_generatedE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t15local_generatedE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t15local_generatedE"></a> <a id="wifi_event_sta_disconnected_t::local_generated__b"></a> <a id="group__bk__api__wifi__v2_1ga8bb56bc2b970c2c802ffe11f91899948"></a> bool local\_generated
    :   if disconnect is request by local

    <a id="_CPPv4N29wifi_event_sta_disconnected_t4ssidE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t4ssidE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t4ssidE"></a> <a id="wifi_event_sta_disconnected_t::ssid__cA"></a> <a id="group__bk__api__wifi__v2_1ga9cf15e82cf6c5907b0a0815d8bcda478"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of disconnected AP

    <a id="_CPPv4N29wifi_event_sta_disconnected_t5bssidE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t5bssidE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t5bssidE"></a> <a id="wifi_event_sta_disconnected_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga1dfa51bd1519f08139986e9910a65469"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of disconnected AP

<a id="_CPPv425wifi_event_ap_connected_t"></a>

<a id="_CPPv325wifi_event_ap_connected_t"></a> <a id="_CPPv225wifi_event_ap_connected_t"></a> <a id="wifi_event_ap_connected_t"></a> <a id="structwifi__event__ap__connected__t"></a> struct wifi\_event\_ap\_connected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N25wifi_event_ap_connected_t3macE"></a>

    <a id="_CPPv3N25wifi_event_ap_connected_t3macE"></a> <a id="_CPPv2N25wifi_event_ap_connected_t3macE"></a> <a id="wifi_event_ap_connected_t::mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gaaa082b5a590c648d34a3481b22604d26"></a> uint8\_t mac\[WIFI\_MAC\_LEN\]
    :   MAC of the STA connected to the BK AP

    <a id="_CPPv4N25wifi_event_ap_connected_t6ipaddrE"></a>

    <a id="_CPPv3N25wifi_event_ap_connected_t6ipaddrE"></a> <a id="_CPPv2N25wifi_event_ap_connected_t6ipaddrE"></a> <a id="wifi_event_ap_connected_t::ipaddr__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gac8947201e4bc11c9139068ca0ea034a8"></a> uint32\_t ipaddr
    :   IP address of the STA connected to the BK AP

<a id="_CPPv429wifi_event_ap_staipassigned_t"></a>

<a id="_CPPv329wifi_event_ap_staipassigned_t"></a> <a id="_CPPv229wifi_event_ap_staipassigned_t"></a> <a id="wifi_event_ap_staipassigned_t"></a> <a id="structwifi__event__ap__staipassigned__t"></a> struct wifi\_event\_ap\_staipassigned\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N29wifi_event_ap_staipassigned_t3macE"></a>

    <a id="_CPPv3N29wifi_event_ap_staipassigned_t3macE"></a> <a id="_CPPv2N29wifi_event_ap_staipassigned_t3macE"></a> <a id="wifi_event_ap_staipassigned_t::mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gaf511253d1e78d217a34057250e363dbc"></a> uint8\_t mac\[WIFI\_MAC\_LEN\]
    :   MAC of the STA connected to the BK AP

    <a id="_CPPv4N29wifi_event_ap_staipassigned_t6ipaddrE"></a>

    <a id="_CPPv3N29wifi_event_ap_staipassigned_t6ipaddrE"></a> <a id="_CPPv2N29wifi_event_ap_staipassigned_t6ipaddrE"></a> <a id="wifi_event_ap_staipassigned_t::ipaddr__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga3006bccc9fd52e708244266b3efb953c"></a> uint32\_t ipaddr
    :   IP address assigned to the STA (network order)

<a id="_CPPv428wifi_event_ap_disconnected_t"></a>

<a id="_CPPv328wifi_event_ap_disconnected_t"></a> <a id="_CPPv228wifi_event_ap_disconnected_t"></a> <a id="wifi_event_ap_disconnected_t"></a> <a id="structwifi__event__ap__disconnected__t"></a> struct wifi\_event\_ap\_disconnected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N28wifi_event_ap_disconnected_t3macE"></a>

    <a id="_CPPv3N28wifi_event_ap_disconnected_t3macE"></a> <a id="_CPPv2N28wifi_event_ap_disconnected_t3macE"></a> <a id="wifi_event_ap_disconnected_t::mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1gadb4e6dc30c213cc53f1e0ab4fb799ea3"></a> uint8\_t mac\[WIFI\_MAC\_LEN\]
    :   MAC of the STA disconnected from the BK AP

<a id="_CPPv426wifi_event_dtim_received_t"></a>

<a id="_CPPv326wifi_event_dtim_received_t"></a> <a id="_CPPv226wifi_event_dtim_received_t"></a> <a id="wifi_event_dtim_received_t"></a> <a id="structwifi__event__dtim__received__t"></a> struct wifi\_event\_dtim\_received\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26wifi_event_dtim_received_t15beacon_intervalE"></a>

    <a id="_CPPv3N26wifi_event_dtim_received_t15beacon_intervalE"></a> <a id="_CPPv2N26wifi_event_dtim_received_t15beacon_intervalE"></a> <a id="wifi_event_dtim_received_t::beacon_interval__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga351dd20afa3cbca378ca2cbb82731284"></a> uint32\_t beacon\_interval
    :   beacon interval

    <a id="_CPPv4N26wifi_event_dtim_received_t11dtim_periodE"></a>

    <a id="_CPPv3N26wifi_event_dtim_received_t11dtim_periodE"></a> <a id="_CPPv2N26wifi_event_dtim_received_t11dtim_periodE"></a> <a id="wifi_event_dtim_received_t::dtim_period__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga7a30fc03a07f0b5d79d5976647d6b218"></a> uint8\_t dtim\_period
    :   dtim period

<a id="_CPPv423wifi_event_reg_change_t"></a>

<a id="_CPPv323wifi_event_reg_change_t"></a> <a id="_CPPv223wifi_event_reg_change_t"></a> <a id="wifi_event_reg_change_t"></a> <a id="structwifi__event__reg__change__t"></a> struct wifi\_event\_reg\_change\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23wifi_event_reg_change_t9initiatorE"></a>

    <a id="_CPPv3N23wifi_event_reg_change_t9initiatorE"></a> <a id="_CPPv2N23wifi_event_reg_change_t9initiatorE"></a> <a id="wifi_event_reg_change_t::initiator__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaa5d42ff852b6d05146cf1cb4b5165077"></a> uint8\_t initiator
    :   0: core, 1: user, 2: driver, 3: dot11d

    <a id="_CPPv4N23wifi_event_reg_change_t4typeE"></a>

    <a id="_CPPv3N23wifi_event_reg_change_t4typeE"></a> <a id="_CPPv2N23wifi_event_reg_change_t4typeE"></a> <a id="wifi_event_reg_change_t::type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga634ed1763f01d49c04cd1e0163d560e0"></a> uint8\_t type
    :   0: country, 1: world, 2: custom, 3: intersection

    <a id="_CPPv4N23wifi_event_reg_change_t6alpha2E"></a>

    <a id="_CPPv3N23wifi_event_reg_change_t6alpha2E"></a> <a id="_CPPv2N23wifi_event_reg_change_t6alpha2E"></a> <a id="wifi_event_reg_change_t::alpha2__cA"></a> <a id="group__bk__api__wifi__v2_1gad4922fada44e8dcd13dadabfffb2c715"></a> char alpha2\[2\]
    :   country code

<a id="_CPPv422wifi_statistics_info_t"></a>

<a id="_CPPv322wifi_statistics_info_t"></a> <a id="_CPPv222wifi_statistics_info_t"></a> <a id="wifi_statistics_info_t"></a> <a id="structwifi__statistics__info__t"></a> struct wifi\_statistics\_info\_t
:   Wi-Fi Statistic info.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22wifi_statistics_info_t16tx_success_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t16tx_success_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t16tx_success_countE"></a> <a id="wifi_statistics_info_t::tx_success_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga75fa5f69654b9bd14f88559f2955ad46"></a> uint32\_t tx\_success\_count
    :   Number of TX successes, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t14tx_retry_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t14tx_retry_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t14tx_retry_countE"></a> <a id="wifi_statistics_info_t::tx_retry_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga2b9d80c7f66c11b6def89cb1153ca7b5"></a> uint32\_t tx\_retry\_count
    :   Number of TX retries, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t13tx_fail_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t13tx_fail_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t13tx_fail_countE"></a> <a id="wifi_statistics_info_t::tx_fail_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga6024723cccfc6a999a0e4451fe291af5"></a> uint32\_t tx\_fail\_count
    :   Number of TX failures, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t16rx_success_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t16rx_success_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t16rx_success_countE"></a> <a id="wifi_statistics_info_t::rx_success_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaefa4726286a6840096833fe24f03a916"></a> uint32\_t rx\_success\_count
    :   Number of RX successes, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t17rx_crcerror_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t17rx_crcerror_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t17rx_crcerror_countE"></a> <a id="wifi_statistics_info_t::rx_crcerror_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga362dd76a480dfb489e5b87dc3a1e3c13"></a> uint32\_t rx\_crcerror\_count
    :   Number of RX FCS errors, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t15mic_error_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t15mic_error_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t15mic_error_countE"></a> <a id="wifi_statistics_info_t::mic_error_count__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga6af2889ba06a3db9487c6e3d48eaa903"></a> uint32\_t mic\_error\_count
    :   Number of MIC errors, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t5noiseE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t5noiseE"></a> <a id="_CPPv2N22wifi_statistics_info_t5noiseE"></a> <a id="wifi_statistics_info_t::noise__int8_t"></a> <a id="group__bk__api__wifi__v2_1gacdedfd5d6f6d16043b919b6ac48197d2"></a> int8\_t noise
    :   Average noise level in dBm, -128 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t7phyrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t7phyrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t7phyrateE"></a> <a id="wifi_statistics_info_t::phyrate__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga8ff500d5044f9a7392a481852dba1c55"></a> uint16\_t phyrate
    :   Maximum used PHY rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t6txrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t6txrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t6txrateE"></a> <a id="wifi_statistics_info_t::txrate__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga9df8dbc49bc25de7a40ae3596ddb8a83"></a> uint16\_t txrate
    :   Average used TX rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t6rxrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t6rxrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t6rxrateE"></a> <a id="wifi_statistics_info_t::rxrate__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga1718a529576569b810b026c300435acc"></a> uint16\_t rxrate
    :   Average used RX rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t4rssiE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t4rssiE"></a> <a id="_CPPv2N22wifi_statistics_info_t4rssiE"></a> <a id="wifi_statistics_info_t::rssi__int8_t"></a> <a id="group__bk__api__wifi__v2_1gac0747e25cd3c89c3f3cd4f598be4385a"></a> int8\_t rssi
    :   Average beacon RSSI in dBm, -128 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t9bandwidthE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t9bandwidthE"></a> <a id="_CPPv2N22wifi_statistics_info_t9bandwidthE"></a> <a id="wifi_statistics_info_t::bandwidth__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gad797fb8d4586f94afbfbe91a56682f0a"></a> uint8\_t bandwidth
    :   Average used bandwidth, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t13idle_time_perE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t13idle_time_perE"></a> <a id="_CPPv2N22wifi_statistics_info_t13idle_time_perE"></a> <a id="wifi_statistics_info_t::idle_time_per__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga481102f7a5ddf09b8daa5d729a30771d"></a> uint8\_t idle\_time\_per
    :   Percent of idle time, 0 if unavailable

<a id="_CPPv414raw_tx_cntrl_t"></a>

<a id="_CPPv314raw_tx_cntrl_t"></a> <a id="_CPPv214raw_tx_cntrl_t"></a> <a id="raw_tx_cntrl_t"></a> <a id="structraw__tx__cntrl__t"></a> struct raw\_tx\_cntrl\_t
:   Wi-Fi RAW TX control.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14raw_tx_cntrl_t5tx_acE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t5tx_acE"></a> <a id="_CPPv2N14raw_tx_cntrl_t5tx_acE"></a> <a id="raw_tx_cntrl_t::tx_ac__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga5365c1f3852c81c2c2b12f8387ffe35f"></a> uint32\_t tx\_ac
    :   RAW Data TX AC information

    <a id="_CPPv4N14raw_tx_cntrl_t7tx_rateE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t7tx_rateE"></a> <a id="_CPPv2N14raw_tx_cntrl_t7tx_rateE"></a> <a id="raw_tx_cntrl_t::tx_rate__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga105fb7de46f6eb363b6a3840dc374a6d"></a> uint32\_t tx\_rate
    :   RAW Data TX rate information

    <a id="_CPPv4N14raw_tx_cntrl_t8tx_powerE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t8tx_powerE"></a> <a id="_CPPv2N14raw_tx_cntrl_t8tx_powerE"></a> <a id="raw_tx_cntrl_t::tx_power__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga7a01d26ccad63affbd38d0ef29f8f264"></a> uint32\_t tx\_power
    :   RAW Data TX power information

    <a id="_CPPv4N14raw_tx_cntrl_t12tx_retry_cntE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t12tx_retry_cntE"></a> <a id="_CPPv2N14raw_tx_cntrl_t12tx_retry_cntE"></a> <a id="raw_tx_cntrl_t::tx_retry_cnt__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaa43c32fc5138afb8caccb660ad877cad"></a> uint32\_t tx\_retry\_cnt
    :   RAW Data TX retry count

    <a id="_CPPv4N14raw_tx_cntrl_t13tx_timeout_msE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t13tx_timeout_msE"></a> <a id="_CPPv2N14raw_tx_cntrl_t13tx_timeout_msE"></a> <a id="raw_tx_cntrl_t::tx_timeout_ms__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga0cb3ab2f8b327cf70c0d2719579367bf"></a> uint32\_t tx\_timeout\_ms
    :   RAW Data TX timeout information

    <a id="_CPPv4N14raw_tx_cntrl_t6formatE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t6formatE"></a> <a id="_CPPv2N14raw_tx_cntrl_t6formatE"></a> <a id="raw_tx_cntrl_t::format__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga51cf0d8b9909a72b0b8b4d612792c97e"></a> uint8\_t format
    :   RAW Data TX format information

    <a id="_CPPv4N14raw_tx_cntrl_t10band_widthE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t10band_widthE"></a> <a id="_CPPv2N14raw_tx_cntrl_t10band_widthE"></a> <a id="raw_tx_cntrl_t::band_width__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga3ac14746c956cf861e57fbcbddc4db5b"></a> uint8\_t band\_width
    :   RAW Data TX band width information

    <a id="_CPPv4N14raw_tx_cntrl_t7gi_typeE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t7gi_typeE"></a> <a id="_CPPv2N14raw_tx_cntrl_t7gi_typeE"></a> <a id="raw_tx_cntrl_t::gi_type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaa85ee7ee694a9db492d06fea9a9b42d5"></a> uint8\_t gi\_type
    :   RAW Data TX guard interval type information

    <a id="_CPPv4N14raw_tx_cntrl_t6ht_mcsE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t6ht_mcsE"></a> <a id="_CPPv2N14raw_tx_cntrl_t6ht_mcsE"></a> <a id="raw_tx_cntrl_t::ht_mcs__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga9ee6e576297ddb489a5dec5c24ad3b16"></a> uint8\_t ht\_mcs
    :   RAW Data TX HT MCS index information

<a id="_CPPv418wifi_raw_tx_info_t"></a>

<a id="_CPPv318wifi_raw_tx_info_t"></a> <a id="_CPPv218wifi_raw_tx_info_t"></a> <a id="wifi_raw_tx_info_t"></a> <a id="structwifi__raw__tx__info__t"></a> struct wifi\_raw\_tx\_info\_t
:   Wi-Fi RAW TX control.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_raw_tx_info_t3pktE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t3pktE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t3pktE"></a> <a id="wifi_raw_tx_info_t::pkt__uint8_tP"></a> <a id="group__bk__api__wifi__v2_1ga357f8cb52865dacbff1bc7b9f64b3461"></a> uint8\_t \*pkt
    :   RAW data tx packet address

    <a id="_CPPv4N18wifi_raw_tx_info_t3lenE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t3lenE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t3lenE"></a> <a id="wifi_raw_tx_info_t::len__i"></a> <a id="group__bk__api__wifi__v2_1gaaafc45d0951efd5b56d03757f8b5a7a4"></a> int len
    :   RAW data tx packet length

    <a id="_CPPv4N18wifi_raw_tx_info_t4typeE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t4typeE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t4typeE"></a> <a id="wifi_raw_tx_info_t::type__i"></a> <a id="group__bk__api__wifi__v2_1gaf043b27624ad1f2859731ae381bd0314"></a> int type
    :   Raw data tx packet type length

    <a id="_CPPv4N18wifi_raw_tx_info_t8tx_cntrlE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t8tx_cntrlE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t8tx_cntrlE"></a> <a id="wifi_raw_tx_info_t::tx_cntrl__raw_tx_cntrl_t"></a> <a id="group__bk__api__wifi__v2_1gae23c160b93223bd0d3d54810c1b3d1cf"></a> [raw\_tx\_cntrl\_t](#_CPPv414raw_tx_cntrl_t "raw_tx_cntrl_t") tx\_cntrl
    :   RAW data tx control information

<a id="_CPPv417wifi_ftm_config_t"></a>

<a id="_CPPv317wifi_ftm_config_t"></a> <a id="_CPPv217wifi_ftm_config_t"></a> <a id="wifi_ftm_config_t"></a> <a id="structwifi__ftm__config__t"></a> struct wifi\_ftm\_config\_t
:   FTM configuration and results.

    Wi-Fi fine timing measurement configuration.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_ftm_config_t13ftm_per_burstE"></a>

    <a id="_CPPv3N17wifi_ftm_config_t13ftm_per_burstE"></a> <a id="_CPPv2N17wifi_ftm_config_t13ftm_per_burstE"></a> <a id="wifi_ftm_config_t::ftm_per_burst__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga091f38d5a8f83cb91adff13652f26f28"></a> uint8\_t ftm\_per\_burst
    :   Number of FTMs per Burst

    <a id="_CPPv4N17wifi_ftm_config_t10nb_ftm_rspE"></a>

    <a id="_CPPv3N17wifi_ftm_config_t10nb_ftm_rspE"></a> <a id="_CPPv2N17wifi_ftm_config_t10nb_ftm_rspE"></a> <a id="wifi_ftm_config_t::nb_ftm_rsp__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga4a0d8523f58fabbce82a52cf912cc1d8"></a> uint8\_t nb\_ftm\_rsp
    :   Number of FTM responders on which we do the measurements

<a id="_CPPv419wifi_ftm_rsp_info_t"></a>

<a id="_CPPv319wifi_ftm_rsp_info_t"></a> <a id="_CPPv219wifi_ftm_rsp_info_t"></a> <a id="wifi_ftm_rsp_info_t"></a> <a id="structwifi__ftm__rsp__info__t"></a> struct wifi\_ftm\_rsp\_info\_t
:   Wi-Fi fine timing measurement results.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19wifi_ftm_rsp_info_t5bssidE"></a>

    <a id="_CPPv3N19wifi_ftm_rsp_info_t5bssidE"></a> <a id="_CPPv2N19wifi_ftm_rsp_info_t5bssidE"></a> <a id="wifi_ftm_rsp_info_t::bssid__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga35de386dafa284745c14d843ab5faad6"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   MAC Address of the FTM responder

    <a id="_CPPv4N19wifi_ftm_rsp_info_t3rttE"></a>

    <a id="_CPPv3N19wifi_ftm_rsp_info_t3rttE"></a> <a id="_CPPv2N19wifi_ftm_rsp_info_t3rttE"></a> <a id="wifi_ftm_rsp_info_t::rtt__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga4a1fda122183915c9c180d87ed73aefa"></a> uint32\_t rtt
    :   Round Trip Time (in ns)

    <a id="_CPPv4N19wifi_ftm_rsp_info_t8distanceE"></a>

    <a id="_CPPv3N19wifi_ftm_rsp_info_t8distanceE"></a> <a id="_CPPv2N19wifi_ftm_rsp_info_t8distanceE"></a> <a id="wifi_ftm_rsp_info_t::distance__float"></a> <a id="group__bk__api__wifi__v2_1gab6f472fb284e9d1dce0c478fe70cf7e6"></a> float distance
    :   Distance (in m)

<a id="_CPPv418wifi_ftm_results_t"></a>

<a id="_CPPv318wifi_ftm_results_t"></a> <a id="_CPPv218wifi_ftm_results_t"></a> <a id="wifi_ftm_results_t"></a> <a id="structwifi__ftm__results__t"></a> struct wifi\_ftm\_results\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_ftm_results_t10nb_ftm_rspE"></a>

    <a id="_CPPv3N18wifi_ftm_results_t10nb_ftm_rspE"></a> <a id="_CPPv2N18wifi_ftm_results_t10nb_ftm_rspE"></a> <a id="wifi_ftm_results_t::nb_ftm_rsp__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaa1a90e2fe5225c7ef2ad30163f3428e5"></a> uint8\_t nb\_ftm\_rsp
    :   Number of FTM responders for which we have a measurement

    <a id="_CPPv4N18wifi_ftm_results_t3rspE"></a>

    <a id="_CPPv3N18wifi_ftm_results_t3rspE"></a> <a id="_CPPv2N18wifi_ftm_results_t3rspE"></a> <a id="wifi_ftm_results_t::rsp__wifi_ftm_rsp_info_tP"></a> <a id="group__bk__api__wifi__v2_1gad528a891cb9d56c0794b73984f55d00e"></a> [wifi\_ftm\_rsp\_info\_t](#_CPPv419wifi_ftm_rsp_info_t "wifi_ftm_rsp_info_t") \*rsp
    :   Per-responder measurements

<a id="_CPPv429wifi_csi_active_mode_config_t"></a>

<a id="_CPPv329wifi_csi_active_mode_config_t"></a> <a id="_CPPv229wifi_csi_active_mode_config_t"></a> <a id="wifi_csi_active_mode_config_t"></a> <a id="structwifi__csi__active__mode__config__t"></a> struct wifi\_csi\_active\_mode\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N29wifi_csi_active_mode_config_t6enableE"></a>

    <a id="_CPPv3N29wifi_csi_active_mode_config_t6enableE"></a> <a id="_CPPv2N29wifi_csi_active_mode_config_t6enableE"></a> <a id="wifi_csi_active_mode_config_t::enable__b"></a> <a id="group__bk__api__wifi__v2_1gad2eb9ae163cde004e5a750d22ca84dce"></a> bool enable
    :   enable or disable csi active, true: enable, false: disable

    <a id="_CPPv4N29wifi_csi_active_mode_config_t8intervalE"></a>

    <a id="_CPPv3N29wifi_csi_active_mode_config_t8intervalE"></a> <a id="_CPPv2N29wifi_csi_active_mode_config_t8intervalE"></a> <a id="wifi_csi_active_mode_config_t::interval__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaea8e51a8330620bcbae99e337e25d900"></a> uint32\_t interval
    :   interval of csi active, unit: ms

<a id="_CPPv424wifi_csi_filter_config_t"></a>

<a id="_CPPv324wifi_csi_filter_config_t"></a> <a id="_CPPv224wifi_csi_filter_config_t"></a> <a id="wifi_csi_filter_config_t"></a> <a id="structwifi__csi__filter__config__t"></a> struct wifi\_csi\_filter\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24wifi_csi_filter_config_t14proto_type_bmpE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t14proto_type_bmpE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t14proto_type_bmpE"></a> <a id="wifi_csi_filter_config_t::proto_type_bmp__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga1c9f12e016415538409eb526e4bfc533"></a> uint8\_t proto\_type\_bmp
    :   b`0001:NON_HT,b`0010:HT, b`0100:VHT, b`1000:HE

    <a id="_CPPv4N24wifi_csi_filter_config_t7cbw_bmpE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t7cbw_bmpE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t7cbw_bmpE"></a> <a id="wifi_csi_filter_config_t::cbw_bmp__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga4922eaeef4bece6ad6ac95059d88c5f4"></a> uint8\_t cbw\_bmp
    :   b`0001:20MHz, b`0010:40MHz, b\`0011: 20Mhz \|\| 40Mhz

    <a id="_CPPv4N24wifi_csi_filter_config_t20filter_mac_addr_typeE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t20filter_mac_addr_typeE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t20filter_mac_addr_typeE"></a> <a id="wifi_csi_filter_config_t::filter_mac_addr_type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga377585f866e696c33f6eb8f9508cb8e6"></a> uint8\_t filter\_mac\_addr\_type
    :   0:all mac;1:src \&\& dst;2: dst only; 3:src only; 4:src \|\| dst

    <a id="_CPPv4N24wifi_csi_filter_config_t18filter_src_mac_numE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t18filter_src_mac_numE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t18filter_src_mac_numE"></a> <a id="wifi_csi_filter_config_t::filter_src_mac_num__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga25f2a4820d3113f8b75bcf55012780b0"></a> uint8\_t filter\_src\_mac\_num
    :   Number of source MAC addresses to filter

    <a id="_CPPv4N24wifi_csi_filter_config_t14filter_src_macE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t14filter_src_macE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t14filter_src_macE"></a> <a id="wifi_csi_filter_config_t::filter_src_mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga081590e377a82a14c652c8a25eb01b99"></a> uint8\_t filter\_src\_mac\[WIFI\_MAC\_LEN \* FILTER\_SRC\_MAC\_MAX\]
    :   Source MAC filter list (max 16 entries)

    <a id="_CPPv4N24wifi_csi_filter_config_t18filter_dst_mac_numE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t18filter_dst_mac_numE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t18filter_dst_mac_numE"></a> <a id="wifi_csi_filter_config_t::filter_dst_mac_num__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gab19615a2e36619425a546441db795ab9"></a> uint8\_t filter\_dst\_mac\_num
    :   Number of destination MAC addresses to filter

    <a id="_CPPv4N24wifi_csi_filter_config_t14filter_dst_macE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t14filter_dst_macE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t14filter_dst_macE"></a> <a id="wifi_csi_filter_config_t::filter_dst_mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga41ef24d6a5bf0128c9e2162e1619dd34"></a> uint8\_t filter\_dst\_mac\[WIFI\_MAC\_LEN \* FILTER\_DST\_MAC\_MAX\]
    :   Destination MAC filter list (max 8 entries)

    <a id="_CPPv4N24wifi_csi_filter_config_t21filter_mgmt_frame_bmpE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t21filter_mgmt_frame_bmpE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t21filter_mgmt_frame_bmpE"></a> <a id="wifi_csi_filter_config_t::filter_mgmt_frame_bmp__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga97b8cf1ed0e067091e493dd83e1d49ab"></a> uint32\_t filter\_mgmt\_frame\_bmp
    :   Bitmap for management frames to capture ,enable:0x80000000

    <a id="_CPPv4N24wifi_csi_filter_config_t21filter_ctrl_frame_bmpE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t21filter_ctrl_frame_bmpE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t21filter_ctrl_frame_bmpE"></a> <a id="wifi_csi_filter_config_t::filter_ctrl_frame_bmp__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga574696627ffdc8492667d443f868ebc1"></a> uint32\_t filter\_ctrl\_frame\_bmp
    :   Bitmap for control frames to capture ,enable:0x80000000

    <a id="_CPPv4N24wifi_csi_filter_config_t21filter_data_frame_bmpE"></a>

    <a id="_CPPv3N24wifi_csi_filter_config_t21filter_data_frame_bmpE"></a> <a id="_CPPv2N24wifi_csi_filter_config_t21filter_data_frame_bmpE"></a> <a id="wifi_csi_filter_config_t::filter_data_frame_bmp__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga5dc5135eff4ffeb16d29eb9f5ec5d8af"></a> uint32\_t filter\_data\_frame\_bmp
    :   Bitmap for data frames to capture ,enable:0x80000000

<a id="_CPPv430wifi_csi_receive_mode_config_t"></a>

<a id="_CPPv330wifi_csi_receive_mode_config_t"></a> <a id="_CPPv230wifi_csi_receive_mode_config_t"></a> <a id="wifi_csi_receive_mode_config_t"></a> <a id="structwifi__csi__receive__mode__config__t"></a> struct wifi\_csi\_receive\_mode\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N30wifi_csi_receive_mode_config_t6enableE"></a>

    <a id="_CPPv3N30wifi_csi_receive_mode_config_t6enableE"></a> <a id="_CPPv2N30wifi_csi_receive_mode_config_t6enableE"></a> <a id="wifi_csi_receive_mode_config_t::enable__b"></a> <a id="group__bk__api__wifi__v2_1gae99c74dee66591b0a745bf4c80b30482"></a> bool enable
    :   enable or disable csi pure receiving, true: enable, false: disable

    <a id="_CPPv4N30wifi_csi_receive_mode_config_t13filter_configE"></a>

    <a id="_CPPv3N30wifi_csi_receive_mode_config_t13filter_configE"></a> <a id="_CPPv2N30wifi_csi_receive_mode_config_t13filter_configE"></a> <a id="wifi_csi_receive_mode_config_t::filter_config__wifi_csi_filter_config_t"></a> <a id="group__bk__api__wifi__v2_1ga9348be0cfc0a6e85be12c8e2692a26a5"></a> [wifi\_csi\_filter\_config\_t](#_CPPv424wifi_csi_filter_config_t "wifi_csi_filter_config_t") filter\_config
    :   filter config

<a id="_CPPv413wifi_rx_pkt_t"></a>

<a id="_CPPv313wifi_rx_pkt_t"></a> <a id="_CPPv213wifi_rx_pkt_t"></a> <a id="wifi_rx_pkt_t"></a> <a id="structwifi__rx__pkt__t"></a> struct wifi\_rx\_pkt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13wifi_rx_pkt_t10proto_typeE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t10proto_typeE"></a> <a id="_CPPv2N13wifi_rx_pkt_t10proto_typeE"></a> <a id="wifi_rx_pkt_t::proto_type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gaeb45d1a2c16aba5ca6fd86ccdeb524f6"></a> uint8\_t proto\_type
    :   0x0:non HT packet; 0x2:HT packet;0x4:VHT packet;0x5:HE packet

    <a id="_CPPv4N13wifi_rx_pkt_t4bandE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t4bandE"></a> <a id="_CPPv2N13wifi_rx_pkt_t4bandE"></a> <a id="wifi_rx_pkt_t::band__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga68b2d9d9608c8aeb6c65731c48b393d0"></a> uint8\_t band
    :   0x0:2.4G; 0x1:5G

    <a id="_CPPv4N13wifi_rx_pkt_t8pri_chanE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t8pri_chanE"></a> <a id="_CPPv2N13wifi_rx_pkt_t8pri_chanE"></a> <a id="wifi_rx_pkt_t::pri_chan__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga75ad3b428dd8f030cc97e1010c1dd3c7"></a> uint8\_t pri\_chan
    :   primary channel on which this packet is received

    <a id="_CPPv4N13wifi_rx_pkt_t4rateE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t4rateE"></a> <a id="_CPPv2N13wifi_rx_pkt_t4rateE"></a> <a id="wifi_rx_pkt_t::rate__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gadc17290944206869d9c15df6a50883df"></a> uint8\_t rate
    :   PHY rate encoding of the packet. Only valid for non-HT packet

    <a id="_CPPv4N13wifi_rx_pkt_t3mcsE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t3mcsE"></a> <a id="_CPPv2N13wifi_rx_pkt_t3mcsE"></a> <a id="wifi_rx_pkt_t::mcs__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gab2f79e4de13424c4a409e9a8729ac614"></a> uint8\_t mcs
    :   Modulation Coding Scheme. Only valid for HT,VHT,HE packet

    <a id="_CPPv4N13wifi_rx_pkt_t3cbwE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t3cbwE"></a> <a id="_CPPv2N13wifi_rx_pkt_t3cbwE"></a> <a id="wifi_rx_pkt_t::cbw__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gac4e3050b2d572b543073cb675ac9934c"></a> uint8\_t cbw
    :   Channel Bandwidth of the packet. 0: 20MHz; 1: 40MHz

    <a id="_CPPv4N13wifi_rx_pkt_t4rssiE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t4rssiE"></a> <a id="_CPPv2N13wifi_rx_pkt_t4rssiE"></a> <a id="wifi_rx_pkt_t::rssi__int8_t"></a> <a id="group__bk__api__wifi__v2_1ga234c13b1be149aa92886ce458bbf01bc"></a> int8\_t rssi
    :   Received Signal Strength Indicator(RSSI) of packet. unit: dBm

    <a id="_CPPv4N13wifi_rx_pkt_t3snrE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t3snrE"></a> <a id="_CPPv2N13wifi_rx_pkt_t3snrE"></a> <a id="wifi_rx_pkt_t::snr__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga9025a42f0fd993057b4cc31bfb76b32f"></a> uint8\_t snr
    :   SNR of AGC stage

    <a id="_CPPv4N13wifi_rx_pkt_t8agc_gainE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t8agc_gainE"></a> <a id="_CPPv2N13wifi_rx_pkt_t8agc_gainE"></a> <a id="wifi_rx_pkt_t::agc_gain__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga758ea4ccf694430ef75881632d8fe784"></a> uint8\_t agc\_gain
    :   Post-AGC link gain

    <a id="_CPPv4N13wifi_rx_pkt_t7gi_typeE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t7gi_typeE"></a> <a id="_CPPv2N13wifi_rx_pkt_t7gi_typeE"></a> <a id="wifi_rx_pkt_t::gi_type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga4ff3d750d69c7c297b3ec2523e686fd1"></a> uint8\_t gi\_type
    :   Guide Interval(GI).

    <a id="_CPPv4N13wifi_rx_pkt_t4stbcE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t4stbcE"></a> <a id="_CPPv2N13wifi_rx_pkt_t4stbcE"></a> <a id="wifi_rx_pkt_t::stbc__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga67307eea8a7886fdf8761e09fb2292d3"></a> uint8\_t stbc
    :   Space Time Block Code(STBC). 0: non STBC packet; 1: STBC packet

    <a id="_CPPv4N13wifi_rx_pkt_t7pkt_lenE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t7pkt_lenE"></a> <a id="_CPPv2N13wifi_rx_pkt_t7pkt_lenE"></a> <a id="wifi_rx_pkt_t::pkt_len__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga0053c1523fe9f27545fcebd5b256b87b"></a> uint8\_t pkt\_len
    :   length of packet including Frame Check Sequence(FCS)

    <a id="_CPPv4N13wifi_rx_pkt_t7src_macE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t7src_macE"></a> <a id="_CPPv2N13wifi_rx_pkt_t7src_macE"></a> <a id="wifi_rx_pkt_t::src_mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga90da1dd94712130af195e611122bad0d"></a> uint8\_t src\_mac\[WIFI\_MAC\_LEN\]
    :   Source MAC Address of the CSI info receive

    <a id="_CPPv4N13wifi_rx_pkt_t7dst_macE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t7dst_macE"></a> <a id="_CPPv2N13wifi_rx_pkt_t7dst_macE"></a> <a id="wifi_rx_pkt_t::dst_mac__uint8_tA"></a> <a id="group__bk__api__wifi__v2_1ga1ecfac5a611265023bbecd94a4f6e4fa"></a> uint8\_t dst\_mac\[WIFI\_MAC\_LEN\]
    :   Destination MAC Address of the CSI info receive

    <a id="_CPPv4N13wifi_rx_pkt_t9timestampE"></a>

    <a id="_CPPv3N13wifi_rx_pkt_t9timestampE"></a> <a id="_CPPv2N13wifi_rx_pkt_t9timestampE"></a> <a id="wifi_rx_pkt_t::timestamp__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaca9068ee6a593eca73a0e3110753d1f7"></a> uint32\_t timestamp
    :   timestamp. The local time when this packet is received. unit: microsecond

<a id="_CPPv49csi_cfr_t"></a>

<a id="_CPPv39csi_cfr_t"></a> <a id="_CPPv29csi_cfr_t"></a> <a id="csi_cfr_t"></a> <a id="structcsi__cfr__t"></a> struct csi\_cfr\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N9csi_cfr_t4realE"></a>

    <a id="_CPPv3N9csi_cfr_t4realE"></a> <a id="_CPPv2N9csi_cfr_t4realE"></a> <a id="csi_cfr_t::real__float"></a> <a id="group__bk__api__wifi__v2_1ga150ef63a7485a1ca51788f9f8d99c020"></a> float real
    :   csi real part

    <a id="_CPPv4N9csi_cfr_t4imagE"></a>

    <a id="_CPPv3N9csi_cfr_t4imagE"></a> <a id="_CPPv2N9csi_cfr_t4imagE"></a> <a id="csi_cfr_t::imag__float"></a> <a id="group__bk__api__wifi__v2_1gacbbf4fa0844ff71a00eb720a6269273e"></a> float imag
    :   csi imaginary part

<a id="_CPPv410csi_info_t"></a>

<a id="_CPPv310csi_info_t"></a> <a id="_CPPv210csi_info_t"></a> <a id="csi_info_t"></a> <a id="structcsi__info__t"></a> struct csi\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10csi_info_t8ltf_typeE"></a>

    <a id="_CPPv3N10csi_info_t8ltf_typeE"></a> <a id="_CPPv2N10csi_info_t8ltf_typeE"></a> <a id="csi_info_t::ltf_type__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga751caa7be9c63e2df50df0b5c6c87805"></a> uint8\_t ltf\_type
    :   0:invalid; 1:L-LTF; 2:HT\_LTF; 3: VHT\_LTF; 4: HE; 5: STBC\_HT\_LTF; 6: STBC\_VHT\_LTF; 7: STBC\_HE\_LTF

    <a id="_CPPv4N10csi_info_t6sc_numE"></a>

    <a id="_CPPv3N10csi_info_t6sc_numE"></a> <a id="_CPPv2N10csi_info_t6sc_numE"></a> <a id="csi_info_t::sc_num__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga37761b2f469a07575f01d29e446dc0e7"></a> uint8\_t sc\_num
    :   The number of CSI subcarrier

    <a id="_CPPv4N10csi_info_t8csi_dataE"></a>

    <a id="_CPPv3N10csi_info_t8csi_dataE"></a> <a id="_CPPv2N10csi_info_t8csi_dataE"></a> <a id="csi_info_t::csi_data__csi_cfr_tP"></a> <a id="group__bk__api__wifi__v2_1gad6b7a290662e5631f7a82eeb5c0fe6e7"></a> struct [csi\_cfr\_t](#_CPPv49csi_cfr_t "csi_cfr_t") \*csi\_data
    :   pointer to csi\_data, data\_len is sc\_num

<a id="_CPPv415wifi_csi_info_t"></a>

<a id="_CPPv315wifi_csi_info_t"></a> <a id="_CPPv215wifi_csi_info_t"></a> <a id="wifi_csi_info_t"></a> <a id="structwifi__csi__info__t"></a> struct wifi\_csi\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15wifi_csi_info_t7rx_ctrlE"></a>

    <a id="_CPPv3N15wifi_csi_info_t7rx_ctrlE"></a> <a id="_CPPv2N15wifi_csi_info_t7rx_ctrlE"></a> <a id="wifi_csi_info_t::rx_ctrl__wifi_rx_pkt_t"></a> <a id="group__bk__api__wifi__v2_1ga5e4ee945449747c6695b659435edadb2"></a> struct [wifi\_rx\_pkt\_t](#_CPPv413wifi_rx_pkt_t "wifi_rx_pkt_t") rx\_ctrl
    :   rx packet ctrl info

    <a id="_CPPv4N15wifi_csi_info_t8csi_infoE"></a>

    <a id="_CPPv3N15wifi_csi_info_t8csi_infoE"></a> <a id="_CPPv2N15wifi_csi_info_t8csi_infoE"></a> <a id="wifi_csi_info_t::csi_info__csi_info_tA"></a> <a id="group__bk__api__wifi__v2_1gae3b3f5eace785f9c5424241dc110b372"></a> struct [csi\_info\_t](#_CPPv410csi_info_t "csi_info_t") csi\_info\[MAX\_NUM\]
    :   csi data info, max is 3

<a id="_CPPv418wifi_signal_info_t"></a>

<a id="_CPPv318wifi_signal_info_t"></a> <a id="_CPPv218wifi_signal_info_t"></a> <a id="wifi_signal_info_t"></a> <a id="structwifi__signal__info__t"></a> struct wifi\_signal\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_signal_info_t9frequencyE"></a>

    <a id="_CPPv3N18wifi_signal_info_t9frequencyE"></a> <a id="_CPPv2N18wifi_signal_info_t9frequencyE"></a> <a id="wifi_signal_info_t::frequency__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaf24c99d54a40eb9bf0455ab49186104a"></a> uint32\_t frequency
    :   frequency of the signal

    <a id="_CPPv4N18wifi_signal_info_t14current_signalE"></a>

    <a id="_CPPv3N18wifi_signal_info_t14current_signalE"></a> <a id="_CPPv2N18wifi_signal_info_t14current_signalE"></a> <a id="wifi_signal_info_t::current_signal__i"></a> <a id="group__bk__api__wifi__v2_1ga276cab9159d1a2a0d10a7742002f27df"></a> int current\_signal
    :   current signal

    <a id="_CPPv4N18wifi_signal_info_t10avg_signalE"></a>

    <a id="_CPPv3N18wifi_signal_info_t10avg_signalE"></a> <a id="_CPPv2N18wifi_signal_info_t10avg_signalE"></a> <a id="wifi_signal_info_t::avg_signal__i"></a> <a id="group__bk__api__wifi__v2_1gaab151130519c64d06c148428f2d79337"></a> int avg\_signal
    :   average signal

    <a id="_CPPv4N18wifi_signal_info_t13current_noiseE"></a>

    <a id="_CPPv3N18wifi_signal_info_t13current_noiseE"></a> <a id="_CPPv2N18wifi_signal_info_t13current_noiseE"></a> <a id="wifi_signal_info_t::current_noise__i"></a> <a id="group__bk__api__wifi__v2_1ga823fc0627d6c28f5689dc6a7ce7fc498"></a> int current\_noise
    :   current noise

<a id="_CPPv410tx_stats_t"></a>

<a id="_CPPv310tx_stats_t"></a> <a id="_CPPv210tx_stats_t"></a> <a id="tx_stats_t"></a> <a id="structtx__stats__t"></a> struct tx\_stats\_t
:   Wi-Fi tx statistics.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10tx_stats_t15tx_singel_totalE"></a>

    <a id="_CPPv3N10tx_stats_t15tx_singel_totalE"></a> <a id="_CPPv2N10tx_stats_t15tx_singel_totalE"></a> <a id="tx_stats_t::tx_singel_total__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaa0b78b346e2dcaf8f15653ef209b0d05"></a> uint32\_t tx\_singel\_total
    :   tx single mpdu total count

    <a id="_CPPv4N10tx_stats_t15tx_singel_retryE"></a>

    <a id="_CPPv3N10tx_stats_t15tx_singel_retryE"></a> <a id="_CPPv2N10tx_stats_t15tx_singel_retryE"></a> <a id="tx_stats_t::tx_singel_retry__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gadaae08ae82d4f1f67d67d546bafae675"></a> uint32\_t tx\_singel\_retry
    :   tx single mpdu retry count

    <a id="_CPPv4N10tx_stats_t12tx_agg_totalE"></a>

    <a id="_CPPv3N10tx_stats_t12tx_agg_totalE"></a> <a id="_CPPv2N10tx_stats_t12tx_agg_totalE"></a> <a id="tx_stats_t::tx_agg_total__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaedba761cc950cc444afb80ea55acd4e3"></a> uint32\_t tx\_agg\_total
    :   tx mpdu of ampdu total count

    <a id="_CPPv4N10tx_stats_t11tx_agg_failE"></a>

    <a id="_CPPv3N10tx_stats_t11tx_agg_failE"></a> <a id="_CPPv2N10tx_stats_t11tx_agg_failE"></a> <a id="tx_stats_t::tx_agg_fail__uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga623468861344cb8c57c46ad6b7d2cf26"></a> uint32\_t tx\_agg\_fail
    :   tx mpdu of ampdu fail count

<a id="_CPPv417wifi_tx_pwr_lmt_t"></a>

<a id="_CPPv317wifi_tx_pwr_lmt_t"></a> <a id="_CPPv217wifi_tx_pwr_lmt_t"></a> <a id="wifi_tx_pwr_lmt_t"></a> <a id="structwifi__tx__pwr__lmt__t"></a> struct wifi\_tx\_pwr\_lmt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_tx_pwr_lmt_t10regulationE"></a>

    <a id="_CPPv3N17wifi_tx_pwr_lmt_t10regulationE"></a> <a id="_CPPv2N17wifi_tx_pwr_lmt_t10regulationE"></a> <a id="wifi_tx_pwr_lmt_t::regulation__wifi_regulation_t"></a> <a id="group__bk__api__wifi__v2_1ga7e58401eb3caa3380a02506c3bbdafd9"></a> [wifi\_regulation\_t](#_CPPv417wifi_regulation_t "wifi_regulation_t") regulation
    :   region regulation 0 REGUALTION\_NULL 1 REGUALTION\_FCC 2 REGUALTION\_ETSI 3 REGUALTION\_JP 4 REGUALTION\_EXT

    <a id="_CPPv4N17wifi_tx_pwr_lmt_t11ratesectionE"></a>

    <a id="_CPPv3N17wifi_tx_pwr_lmt_t11ratesectionE"></a> <a id="_CPPv2N17wifi_tx_pwr_lmt_t11ratesectionE"></a> <a id="wifi_tx_pwr_lmt_t::ratesection__wifi_ratesection_t"></a> <a id="group__bk__api__wifi__v2_1ga18a9bfc78bd5777ae5aa55c89a642bed"></a> [wifi\_ratesection\_t](#_CPPv418wifi_ratesection_t "wifi_ratesection_t") ratesection
    :   ratesection 0 RATE\_NULL 1 RATE\_CCK 2 RATE\_OFDM 3 RATE\_HT 4 RATE\_VHT 5 RATE\_HE

    <a id="_CPPv4N17wifi_tx_pwr_lmt_t7channelE"></a>

    <a id="_CPPv3N17wifi_tx_pwr_lmt_t7channelE"></a> <a id="_CPPv2N17wifi_tx_pwr_lmt_t7channelE"></a> <a id="wifi_tx_pwr_lmt_t::channel__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gad31f7724b31bef16b0de9f29867c18f9"></a> uint8\_t channel
    :   channel range from 1-14

    <a id="_CPPv4N17wifi_tx_pwr_lmt_t5valueE"></a>

    <a id="_CPPv3N17wifi_tx_pwr_lmt_t5valueE"></a> <a id="_CPPv2N17wifi_tx_pwr_lmt_t5valueE"></a> <a id="wifi_tx_pwr_lmt_t::value__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga6a4e26292440960e3464f67f1c2aa689"></a> uint8\_t value
    :   value max tx power

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_WIFI_NOT_INIT"></a>

<a id="group__bk__api__wifi__v2__enum_1ga3e53cec7119809b7717506ad5f36085f"></a> BK\_ERR\_WIFI\_NOT\_INIT
:   WiFi is not initialized, call [bk\_wifi\_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226) to init the WiFi

<a id="c.BK_ERR_WIFI_STA_NOT_STARTED"></a>

<a id="group__bk__api__wifi__v2__enum_1ga17397126f67479e898c44c2e1578a984"></a> BK\_ERR\_WIFI\_STA\_NOT\_STARTED
:   STA is not started, call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) to start the STA

<a id="c.BK_ERR_WIFI_AP_NOT_STARTED"></a>

<a id="group__bk__api__wifi__v2__enum_1ga34aaecea3c4f55fe70c11300da07baa9"></a> BK\_ERR\_WIFI\_AP\_NOT\_STARTED
:   AP is not initialized, call [bk\_wifi\_ap\_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5) to start the AP

<a id="c.BK_ERR_WIFI_CHAN_RANGE"></a>

<a id="group__bk__api__wifi__v2__enum_1ga8bf3b9834855ed40271d83a1332e1d06"></a> BK\_ERR\_WIFI\_CHAN\_RANGE
:   Invalid channel range

<a id="c.BK_ERR_WIFI_COUNTRY_POLICY"></a>

<a id="group__bk__api__wifi__v2__enum_1gab54a20c4c8c8ae4d3adea384a3749fdf"></a> BK\_ERR\_WIFI\_COUNTRY\_POLICY
:   Invalid country policy

<a id="c.BK_ERR_WIFI_RESERVED_FIELD"></a>

<a id="group__bk__api__wifi__v2__enum_1gaf7265e0814c2c72e238c2941338e0d9a"></a> BK\_ERR\_WIFI\_RESERVED\_FIELD
:   Reserved fields not 0

<a id="c.BK_ERR_WIFI_MONITOR_IP"></a>

<a id="group__bk__api__wifi__v2__enum_1ga6757a1fb11154019aea1acbc9a3a0bb9"></a> BK\_ERR\_WIFI\_MONITOR\_IP
:   Monitor is in progress

<a id="c.BK_ERR_WIFI_STA_NOT_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga1e66a2588e18bec7a53a5429450ed1e7"></a> BK\_ERR\_WIFI\_STA\_NOT\_CONFIG
:   STA is not configured, call bk\_wifi\_sta\_config() to configure it

<a id="c.BK_ERR_WIFI_AP_NOT_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga2baae2e392326f80340c427904258c95"></a> BK\_ERR\_WIFI\_AP\_NOT\_CONFIG
:   AP is not configured, call bk\_wifi\_ap\_config() to configure it

<a id="c.BK_ERR_WIFI_DRIVER"></a>

<a id="group__bk__api__wifi__v2__enum_1ga47bd90f7ae0e9c24e9082c20c957297e"></a> BK\_ERR\_WIFI\_DRIVER
:   Internal WiFi driver error

<a id="c.BK_ERR_WIFI_MONITOR_ENTER"></a>

<a id="group__bk__api__wifi__v2__enum_1gae81db1f58e616d8d52e9937906d1b778"></a> BK\_ERR\_WIFI\_MONITOR\_ENTER
:   WiFi failed to enter monitor mode

<a id="c.BK_ERR_WIFI_DRIVER_DEL_VIF"></a>

<a id="group__bk__api__wifi__v2__enum_1ga1f5df9c7ae88414099ca70ee560a7dc2"></a> BK\_ERR\_WIFI\_DRIVER\_DEL\_VIF
:   WiFi driver failed to delete WiFi virtual interface

<a id="c.BK_ERR_WIFI_DRIVER_AP_START"></a>

<a id="group__bk__api__wifi__v2__enum_1ga0d255c15f94c4e773dc746906479b7c7"></a> BK\_ERR\_WIFI\_DRIVER\_AP\_START
:   WiFi driver failed to start BK AP

<a id="c.BK_ERR_WIFI_CHAN_NUMBER"></a>

<a id="group__bk__api__wifi__v2__enum_1gaf0e6f1d89444885164d19206c49ed42a"></a> BK\_ERR\_WIFI\_CHAN\_NUMBER
:   Invalid channel number

<a id="c.WIFI_MIN_CHAN_NUM"></a>

<a id="group__bk__api__wifi__v2__enum_1gaa4fdfa3785cfcfe8e88072acb4b94913"></a> WIFI\_MIN\_CHAN\_NUM
:   Minimum supported channel number

<a id="c.WIFI_MAX_CHAN_NUM"></a>

<a id="group__bk__api__wifi__v2__enum_1ga736217f5963b4ae49dc331aa143c70bb"></a> WIFI\_MAX\_CHAN\_NUM
:   Maximum supported channel number

<a id="c.WIFI_MAX_SCAN_CHAN_DUR"></a>

<a id="group__bk__api__wifi__v2__enum_1ga518251a605e88070abffd60373679ec8"></a> WIFI\_MAX\_SCAN\_CHAN\_DUR
:   scan duration param, need less than 200ms

<a id="c.WIFI_CHANNEL_NUM_2G4"></a>

<a id="group__bk__api__wifi__v2__enum_1gacd06456321ebd80b9001f069135c17ba"></a> WIFI\_CHANNEL\_NUM\_2G4
:   Maximum supported 2.4G channel number

<a id="c.WIFI_CHANNEL_NUM_5G"></a>

<a id="group__bk__api__wifi__v2__enum_1gac2564f06820fef7feb201c608694e866"></a> WIFI\_CHANNEL\_NUM\_5G
:   Maximum supported 5G channel numbe

<a id="c.WIFI_2BAND_MAX_CHAN_NUM"></a>

<a id="group__bk__api__wifi__v2__enum_1ga0a3b488fd022c9562533ae2ad22eadaa"></a> WIFI\_2BAND\_MAX\_CHAN\_NUM

<a id="c.WIFI_SSID_STR_LEN"></a>

<a id="group__bk__api__wifi__v2__enum_1ga0494f16536e40b559f4f4965b4f6d218"></a> WIFI\_SSID\_STR\_LEN
:   Maximum **NULL-terminated** WiFi SSID length

<a id="c.WIFI_BSSID_LEN"></a>

<a id="group__bk__api__wifi__v2__enum_1ga3f6e17172d889ba61f6fb28820b3cd12"></a> WIFI\_BSSID\_LEN
:   Length of BSSID

<a id="c.WIFI_MAC_LEN"></a>

<a id="group__bk__api__wifi__v2__enum_1gabc871a0934ad71ec71b29de3f9bc4815"></a> WIFI\_MAC\_LEN
:   Length of MAC

<a id="c.WIFI_PASSWORD_LEN"></a>

<a id="group__bk__api__wifi__v2__enum_1gaf4b865a3a45e5f7a5ca3f561a649e804"></a> WIFI\_PASSWORD\_LEN
:   Maximum **NULL-terminated** WiFi password length

<a id="c.WIFI_DEFAULT_INIT_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga412e5b8a95fbe4baf89a44c949b30a44"></a> WIFI\_DEFAULT\_INIT\_CONFIG()
:   default init configuration

<a id="c.WIFI_DEFAULT_STA_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga04611cd1fea13178e3c1654cfafd4253"></a> WIFI\_DEFAULT\_STA\_CONFIG()
:   default STA configuration

<a id="c.WIFI_DEFAULT_AP_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga0710d007a12faf0163e20b04f4e73aba"></a> WIFI\_DEFAULT\_AP\_CONFIG()
:   default AP configuration

<a id="c.WIFI_DEFAULT_SCAN_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga15d1f6c3ddee8b3a7068aa7711c885f5"></a> WIFI\_DEFAULT\_SCAN\_CONFIG()
:   default Scan configuration

<a id="c.WIFI_DEFAULT_FILTER_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga92389c2b9bbad59c8194debb8c51efa5"></a> WIFI\_DEFAULT\_FILTER\_CONFIG()
:   default Filter configuration

<a id="c.WIFI_DEFAULT_FTM_CONFIG"></a>

<a id="group__bk__api__wifi__v2__enum_1ga8a528409f2d46eeab15affaacf634263"></a> WIFI\_DEFAULT\_FTM\_CONFIG()
:   default FTM configuration

<a id="c.BK_MAX_STA_TYPE"></a>

<a id="group__bk__api__wifi__v2__typedef_1gafd21e4dbe54802b84c9014913faef2d4"></a> BK\_MAX\_STA\_TYPE

<a id="c.OUI_BEKEN"></a>

<a id="group__bk__api__wifi__v2__typedef_1ga8c05f9c6420142a4b7fa4cfe8dfb8aca"></a> OUI\_BEKEN

<a id="c.WLAN_EID_VENDOR_SPECIFIC"></a>

<a id="group__bk__api__wifi__v2__typedef_1ga35f179d40f064114d74f686c2eb3b159"></a> WLAN\_EID\_VENDOR\_SPECIFIC

<a id="c.FILTER_SRC_MAC_MAX"></a>

<a id="group__bk__api__wifi__v2__typedef_1gabeb532f5d6c3c717a1e9ef871373c584"></a> FILTER\_SRC\_MAC\_MAX
:   CSI configuration and results.

    Wi-Fi Channel State Information configuration and results.

<a id="c.FILTER_DST_MAC_MAX"></a>

<a id="group__bk__api__wifi__v2__typedef_1gaed9a782068e569772d7f37213a269074"></a> FILTER\_DST\_MAC\_MAX

<a id="c.MAX_NUM"></a>

<a id="group__bk__api__wifi__v2__typedef_1ga55bfdcfe7613d75fb48ec99c7bf4dd5e"></a> MAX\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411BK_STA_TYPE"></a>

<a id="_CPPv311BK_STA_TYPE"></a> <a id="_CPPv211BK_STA_TYPE"></a> <a id="BK_STA_TYPE"></a> <a id="group__bk__api__wifi__v2__typedef_1ga338c42a75d2f50a9ef55c2238fc33adf"></a> typedef enum [sta\_type](#_CPPv48sta_type "sta_type") BK\_STA\_TYPE

<a id="_CPPv413wlan_ap_sta_t"></a>

<a id="_CPPv313wlan_ap_sta_t"></a> <a id="_CPPv213wlan_ap_sta_t"></a> <a id="wlan_ap_sta_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaef5913aef30a4dee0001e45a0450473d"></a> typedef struct [wlan\_ap\_sta](#_CPPv411wlan_ap_sta "wlan_ap_sta") wlan\_ap\_sta\_t
:   Wlan station information definition.

<a id="_CPPv414wlan_ap_stas_t"></a>

<a id="_CPPv314wlan_ap_stas_t"></a> <a id="_CPPv214wlan_ap_stas_t"></a> <a id="wlan_ap_stas_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga6c2683431c3956e933cd3340c1329f41"></a> typedef struct [wlan\_ap\_stas](#_CPPv412wlan_ap_stas "wlan_ap_stas") wlan\_ap\_stas\_t
:   Wlan connected stations information definition.

<a id="_CPPv414wlan_ap_vsie_t"></a>

<a id="_CPPv314wlan_ap_vsie_t"></a> <a id="_CPPv214wlan_ap_vsie_t"></a> <a id="wlan_ap_vsie_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaaecb4a474ea19a8599453f36b74ae4aa"></a> typedef struct [wlan\_ap\_vsie](#_CPPv412wlan_ap_vsie "wlan_ap_vsie") wlan\_ap\_vsie\_t
:   softap beacon/probe response’s vendor IEs Dynamic change softap’s vendor specific IEs.

<a id="_CPPv415wlan_sta_vsie_t"></a>

<a id="_CPPv315wlan_sta_vsie_t"></a> <a id="_CPPv215wlan_sta_vsie_t"></a> <a id="wlan_sta_vsie_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gae8c7d3c160a32f4f0b618913dafe3faa"></a> typedef struct [wlan\_sta\_vsie](#_CPPv413wlan_sta_vsie "wlan_sta_vsie") wlan\_sta\_vsie\_t
:   STA vendor IEs for (re)assoc, scan, p2p, p2p go, etc. Dynamic change STA’s vendor specific IEs.

<a id="_CPPv417wifi_monitor_cb_t"></a>

<a id="_CPPv317wifi_monitor_cb_t"></a> <a id="_CPPv217wifi_monitor_cb_t"></a> <a id="wifi_monitor_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga7a1cb892e0cb787179b189d79faa421e"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_monitor\_cb\_t)(const uint8\_t \*frame, uint32\_t len, const [wifi\_frame\_info\_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") \*frame\_info)
:   Monitor callback to receive frames relayed by WiFi driver.

    **Attention**
    :   1\. The memory of frame and frame\_info will be freed immediately when the callback is returned. If we want to use the frame or frame\_info in other task, make a copy of them and handle them accordingly.

    **Attention**
    :   2\. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

<a id="_CPPv420wifi_rlk_chan_info_t"></a>

<a id="_CPPv320wifi_rlk_chan_info_t"></a> <a id="_CPPv220wifi_rlk_chan_info_t"></a> <a id="wifi_rlk_chan_info_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga9d50876726075b1f3fa57cc1e36f124f"></a> typedef struct [wifi\_rlk\_chan\_info](#_CPPv418wifi_rlk_chan_info "wifi_rlk_chan_info") wifi\_rlk\_chan\_info\_t

<a id="_CPPv420wifi_rlk_base_info_t"></a>

<a id="_CPPv320wifi_rlk_base_info_t"></a> <a id="_CPPv220wifi_rlk_base_info_t"></a> <a id="wifi_rlk_base_info_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga8a41983d1759b1542cb4741a9f19a80d"></a> typedef struct [wifi\_rlk\_base\_info](#_CPPv418wifi_rlk_base_info "wifi_rlk_base_info") wifi\_rlk\_base\_info\_t

<a id="_CPPv422wifi_rlk_scan_cfm_cb_t"></a>

<a id="_CPPv322wifi_rlk_scan_cfm_cb_t"></a> <a id="_CPPv222wifi_rlk_scan_cfm_cb_t"></a> <a id="wifi_rlk_scan_cfm_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga7b2ceefa837dfa63a8659ae2c527b24b"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_rlk\_scan\_cfm\_cb\_t)(void)

<a id="_CPPv416wifi_filter_cb_t"></a>

<a id="_CPPv316wifi_filter_cb_t"></a> <a id="_CPPv216wifi_filter_cb_t"></a> <a id="wifi_filter_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga4f78a94640b8b4e51f59fa17fea4b923"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_filter\_cb\_t)(const uint8\_t \*frame, uint32\_t len, const [wifi\_frame\_info\_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") \*frame\_info)
:   Filter callback to receive frames relayed by WiFi driver.

    **Attention**
    :   1\. The memory of frame and frame\_info will be freed immediately when the callback is returned. If we want to use the frame or frame\_info in other task, make a copy of them and handle them accordingly.

    **Attention**
    :   2\. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

<a id="_CPPv413wifi_csi_cb_t"></a>

<a id="_CPPv313wifi_csi_cb_t"></a> <a id="_CPPv213wifi_csi_cb_t"></a> <a id="wifi_csi_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga1049b9985d49124ef64821770ebd313b"></a> typedef void (\*wifi\_csi\_cb\_t)(struct [wifi\_csi\_info\_t](#_CPPv415wifi_csi_info_t "wifi_csi_info_t") \*info)

<a id="_CPPv421wifi_beacon_cc_rxed_t"></a>

<a id="_CPPv321wifi_beacon_cc_rxed_t"></a> <a id="_CPPv221wifi_beacon_cc_rxed_t"></a> <a id="wifi_beacon_cc_rxed_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga164b8762b3b18d74c6e4cb834a33edd1"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_beacon\_cc\_rxed\_t)(void \*ctxt, uint8\_t \*cc, uint8\_t cc\_len)

<a id="_CPPv418wifi_get_vsie_cb_t"></a>

<a id="_CPPv318wifi_get_vsie_cb_t"></a> <a id="_CPPv218wifi_get_vsie_cb_t"></a> <a id="wifi_get_vsie_cb_t"></a> <a id="group__bk__api__wifi__v2_1gabce969b7ac1ba6eb13f177a11f29745f"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_get\_vsie\_cb\_t)(void \*vendor\_ie, uint8\_t frame\_type)
:   wifi get vsie cb interface

    Param void\*
    :   vendor\_ie

    Param frame
    :   type 1: probe response(or beacon) 2: assoc response

<a id="_CPPv417wifi_bcnmiss_cb_t"></a>

<a id="_CPPv317wifi_bcnmiss_cb_t"></a> <a id="_CPPv217wifi_bcnmiss_cb_t"></a> <a id="wifi_bcnmiss_cb_t"></a> <a id="group__bk__api__wifi__v2_1ga0a85aeafe2690d71945230d0d4707370"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_bcnmiss\_cb\_t)(void)
:   wifi beacon miss cb interface

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411wifi_band_t"></a>

<a id="_CPPv311wifi_band_t"></a> <a id="_CPPv211wifi_band_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga88bf982f778c6644a16c5dd47a3eebda"></a> enum wifi\_band\_t
:   enum ieee80211\_band \- supported frequency bands

    The bands are assigned this way because the supported bitrates differ in these bands.

    @IEEE80211\_BAND\_2GHZ: 2.4GHz ISM band @IEEE80211\_BAND\_5GHZ: around 5GHz band (4.9-5.7) @IEEE80211\_BAND\_6GHZ: around 6GHz band (5.925-7.125) @IEEE80211\_BAND\_60GHZ: around 60 GHz band (58.32 \- 64.80 GHz) @IEEE80211\_NUM\_BANDS: number of defined bands

    *Values:*

    <a id="_CPPv4N11wifi_band_t19IEEE80211_BAND_2GHZE"></a>

    <a id="_CPPv3N11wifi_band_t19IEEE80211_BAND_2GHZE"></a> <a id="_CPPv2N11wifi_band_t19IEEE80211_BAND_2GHZE"></a> <a id="group__bk__api__wifi__v2__enum_1gga88bf982f778c6644a16c5dd47a3eebdaaf339f82c036557f42f668a358aa96da3"></a> enumerator IEEE80211\_BAND\_2GHZ

    <a id="_CPPv4N11wifi_band_t19IEEE80211_BAND_5GHZE"></a>

    <a id="_CPPv3N11wifi_band_t19IEEE80211_BAND_5GHZE"></a> <a id="_CPPv2N11wifi_band_t19IEEE80211_BAND_5GHZE"></a> <a id="group__bk__api__wifi__v2__enum_1gga88bf982f778c6644a16c5dd47a3eebdaa0871c8866251ec4e668e956bb0427cfa"></a> enumerator IEEE80211\_BAND\_5GHZ

    <a id="_CPPv4N11wifi_band_t19IEEE80211_BAND_6GHZE"></a>

    <a id="_CPPv3N11wifi_band_t19IEEE80211_BAND_6GHZE"></a> <a id="_CPPv2N11wifi_band_t19IEEE80211_BAND_6GHZE"></a> <a id="group__bk__api__wifi__v2__enum_1gga88bf982f778c6644a16c5dd47a3eebdaa309372a5d128e7a1ee9a5cd55f27f622"></a> enumerator IEEE80211\_BAND\_6GHZ

    <a id="_CPPv4N11wifi_band_t20IEEE80211_BAND_60GHZE"></a>

    <a id="_CPPv3N11wifi_band_t20IEEE80211_BAND_60GHZE"></a> <a id="_CPPv2N11wifi_band_t20IEEE80211_BAND_60GHZE"></a> <a id="group__bk__api__wifi__v2__enum_1gga88bf982f778c6644a16c5dd47a3eebdaa8e43a12ab8250a1d24e84496b6b9d8fb"></a> enumerator IEEE80211\_BAND\_60GHZ

    <a id="_CPPv4N11wifi_band_t19IEEE80211_NUM_BANDSE"></a>

    <a id="_CPPv3N11wifi_band_t19IEEE80211_NUM_BANDSE"></a> <a id="_CPPv2N11wifi_band_t19IEEE80211_NUM_BANDSE"></a> <a id="group__bk__api__wifi__v2__enum_1gga88bf982f778c6644a16c5dd47a3eebdaa703cf67d516a80d6dae1b1995017b9a4"></a> enumerator IEEE80211\_NUM\_BANDS

<a id="_CPPv412wifi_event_t"></a>

<a id="_CPPv312wifi_event_t"></a> <a id="_CPPv212wifi_event_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga4d4930414997036f72c92e8a02a6de33"></a> enum wifi\_event\_t
:   WiFi public event type.

    *Values:*

    <a id="_CPPv4N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a>

    <a id="_CPPv3N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a> <a id="_CPPv2N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a70b73fdd0fe544808f91625b672c8381"></a> enumerator EVENT\_WIFI\_SCAN\_DONE
    :   WiFi scan done event

    <a id="_CPPv4N12wifi_event_t23EVENT_WIFI_CSI_DATA_INDE"></a>

    <a id="_CPPv3N12wifi_event_t23EVENT_WIFI_CSI_DATA_INDE"></a> <a id="_CPPv2N12wifi_event_t23EVENT_WIFI_CSI_DATA_INDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a068431fc3abb7545fc797cdac0032508"></a> enumerator EVENT\_WIFI\_CSI\_DATA\_IND

    <a id="_CPPv4N12wifi_event_t22EVENT_WIFI_CSI_ALG_INDE"></a>

    <a id="_CPPv3N12wifi_event_t22EVENT_WIFI_CSI_ALG_INDE"></a> <a id="_CPPv2N12wifi_event_t22EVENT_WIFI_CSI_ALG_INDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a89342e81d690ae634169cc1b35fbfc11"></a> enumerator EVENT\_WIFI\_CSI\_ALG\_IND

    <a id="_CPPv4N12wifi_event_t16EVENT_WIFI_STARTE"></a>

    <a id="_CPPv3N12wifi_event_t16EVENT_WIFI_STARTE"></a> <a id="_CPPv2N12wifi_event_t16EVENT_WIFI_STARTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a53d51487ca8531e093b0ce94d443178a"></a> enumerator EVENT\_WIFI\_START
    :   WiFi start event

    <a id="_CPPv4N12wifi_event_t15EVENT_WIFI_STOPE"></a>

    <a id="_CPPv3N12wifi_event_t15EVENT_WIFI_STOPE"></a> <a id="_CPPv2N12wifi_event_t15EVENT_WIFI_STOPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a60c59854320c3ba92707ce81b73d54e0"></a> enumerator EVENT\_WIFI\_STOP
    :   WiFi stop event

    <a id="_CPPv4N12wifi_event_t19EVENT_WIFI_AP_STARTE"></a>

    <a id="_CPPv3N12wifi_event_t19EVENT_WIFI_AP_STARTE"></a> <a id="_CPPv2N12wifi_event_t19EVENT_WIFI_AP_STARTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33ad59037ab61b5ea521b5eb3d13386a497"></a> enumerator EVENT\_WIFI\_AP\_START
    :   WiFi AP start event

    <a id="_CPPv4N12wifi_event_t18EVENT_WIFI_AP_STOPE"></a>

    <a id="_CPPv3N12wifi_event_t18EVENT_WIFI_AP_STOPE"></a> <a id="_CPPv2N12wifi_event_t18EVENT_WIFI_AP_STOPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a6cbed68d12b7fb6da6d4c6837caba25d"></a> enumerator EVENT\_WIFI\_AP\_STOP
    :   WiFi AP stop event

    <a id="_CPPv4N12wifi_event_t16EVENT_WIFI_READYE"></a>

    <a id="_CPPv3N12wifi_event_t16EVENT_WIFI_READYE"></a> <a id="_CPPv2N12wifi_event_t16EVENT_WIFI_READYE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a811edc8b65e5d1bafc1da2d3ad8e66d9"></a> enumerator EVENT\_WIFI\_READY
    :   WiFi ready event

    <a id="_CPPv4N12wifi_event_t24EVENT_WIFI_STA_CONNECTEDE"></a>

    <a id="_CPPv3N12wifi_event_t24EVENT_WIFI_STA_CONNECTEDE"></a> <a id="_CPPv2N12wifi_event_t24EVENT_WIFI_STA_CONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a18bf31613ee317b91cac1d081439db1f"></a> enumerator EVENT\_WIFI\_STA\_CONNECTED
    :   The BK STA is connected

    <a id="_CPPv4N12wifi_event_t27EVENT_WIFI_STA_DISCONNECTEDE"></a>

    <a id="_CPPv3N12wifi_event_t27EVENT_WIFI_STA_DISCONNECTEDE"></a> <a id="_CPPv2N12wifi_event_t27EVENT_WIFI_STA_DISCONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a7dfa9bfd390236e0dd4b9565cba07daa"></a> enumerator EVENT\_WIFI\_STA\_DISCONNECTED
    :   The BK STA is disconnected

    <a id="_CPPv4N12wifi_event_t23EVENT_WIFI_AP_CONNECTEDE"></a>

    <a id="_CPPv3N12wifi_event_t23EVENT_WIFI_AP_CONNECTEDE"></a> <a id="_CPPv2N12wifi_event_t23EVENT_WIFI_AP_CONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33abc51ea6bc465bbbbe83e62b5b085006b"></a> enumerator EVENT\_WIFI\_AP\_CONNECTED
    :   A STA is connected to the BK AP

    <a id="_CPPv4N12wifi_event_t26EVENT_WIFI_AP_DISCONNECTEDE"></a>

    <a id="_CPPv3N12wifi_event_t26EVENT_WIFI_AP_DISCONNECTEDE"></a> <a id="_CPPv2N12wifi_event_t26EVENT_WIFI_AP_DISCONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33ac8f0ceb3b967f3422335c7358f627f99"></a> enumerator EVENT\_WIFI\_AP\_DISCONNECTED
    :   A STA is disconnected from the BK AP

    <a id="_CPPv4N12wifi_event_t27EVENT_WIFI_AP_STAIPASSIGNEDE"></a>

    <a id="_CPPv3N12wifi_event_t27EVENT_WIFI_AP_STAIPASSIGNEDE"></a> <a id="_CPPv2N12wifi_event_t27EVENT_WIFI_AP_STAIPASSIGNEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33abcd9197086217ae89237fbce1ede9464"></a> enumerator EVENT\_WIFI\_AP\_STAIPASSIGNED
    :   The BK AP STA IP assigned

    <a id="_CPPv4N12wifi_event_t24EVENT_WIFI_NETWORK_FOUNDE"></a>

    <a id="_CPPv3N12wifi_event_t24EVENT_WIFI_NETWORK_FOUNDE"></a> <a id="_CPPv2N12wifi_event_t24EVENT_WIFI_NETWORK_FOUNDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33ad2130915964e9a9a66bddbc2e0fa0907"></a> enumerator EVENT\_WIFI\_NETWORK\_FOUND
    :   The BK STA find target AP

    <a id="_CPPv4N12wifi_event_t22EVENT_WIFI_BEACON_HINTE"></a>

    <a id="_CPPv3N12wifi_event_t22EVENT_WIFI_BEACON_HINTE"></a> <a id="_CPPv2N12wifi_event_t22EVENT_WIFI_BEACON_HINTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a54417b6e5fa2de1b753bc4bf98ea8381"></a> enumerator EVENT\_WIFI\_BEACON\_HINT
    :   Beacon found on NO\_IR channel

    <a id="_CPPv4N12wifi_event_t28EVENT_WIFI_REGDOMAIN_CHANGEDE"></a>

    <a id="_CPPv3N12wifi_event_t28EVENT_WIFI_REGDOMAIN_CHANGEDE"></a> <a id="_CPPv2N12wifi_event_t28EVENT_WIFI_REGDOMAIN_CHANGEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a0b26bedb5b332d7374f5e34b8818f1e3"></a> enumerator EVENT\_WIFI\_REGDOMAIN\_CHANGED
    :   Regulatory domain changed

    <a id="_CPPv4N12wifi_event_t24EVENT_WIFI_DTIM_RECEIVEDE"></a>

    <a id="_CPPv3N12wifi_event_t24EVENT_WIFI_DTIM_RECEIVEDE"></a> <a id="_CPPv2N12wifi_event_t24EVENT_WIFI_DTIM_RECEIVEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a4ef8d3ab67d1bea0c72e95b4ce5c39fa"></a> enumerator EVENT\_WIFI\_DTIM\_RECEIVED
    :   The BK STA receives DTIM from AP

    <a id="_CPPv4N12wifi_event_t36EVENT_WIFI_AWARE_WAKE_INTERVAL_STARTE"></a>

    <a id="_CPPv3N12wifi_event_t36EVENT_WIFI_AWARE_WAKE_INTERVAL_STARTE"></a> <a id="_CPPv2N12wifi_event_t36EVENT_WIFI_AWARE_WAKE_INTERVAL_STARTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a88ce5f1530249458265f87fe85f9debf"></a> enumerator EVENT\_WIFI\_AWARE\_WAKE\_INTERVAL\_START
    :   The BK Aware wake interval start

    <a id="_CPPv4N12wifi_event_t16EVENT_WIFI_COUNTE"></a>

    <a id="_CPPv3N12wifi_event_t16EVENT_WIFI_COUNTE"></a> <a id="_CPPv2N12wifi_event_t16EVENT_WIFI_COUNTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a45f8fd32bccb88538c4e36c1bf884c8c"></a> enumerator EVENT\_WIFI\_COUNT
    :   WiFi event count

<a id="_CPPv417wifi_err_reason_t"></a>

<a id="_CPPv317wifi_err_reason_t"></a> <a id="_CPPv217wifi_err_reason_t"></a> <a id="group__bk__api__wifi__v2__enum_1gaf2f44e69763071bbe8c3903158c5a357"></a> enum wifi\_err\_reason\_t
:   *Values:*

    <a id="_CPPv4N17wifi_err_reason_t20WIFI_REASON_RESERVEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t20WIFI_REASON_RESERVEDE"></a> <a id="_CPPv2N17wifi_err_reason_t20WIFI_REASON_RESERVEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357aeb810b53563e59d566d1c1dffce9b3a3"></a> enumerator WIFI\_REASON\_RESERVED

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_UNSPECIFIEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_UNSPECIFIEDE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_UNSPECIFIEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a976f9cb06ee9e62bf5141d11a80d8199"></a> enumerator WIFI\_REASON\_UNSPECIFIED

    <a id="_CPPv4N17wifi_err_reason_t31WIFI_REASON_PREV_AUTH_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t31WIFI_REASON_PREV_AUTH_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t31WIFI_REASON_PREV_AUTH_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a33bba2a2a3b682f80eac4350957ac64f"></a> enumerator WIFI\_REASON\_PREV\_AUTH\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t26WIFI_REASON_DEAUTH_LEAVINGE"></a>

    <a id="_CPPv3N17wifi_err_reason_t26WIFI_REASON_DEAUTH_LEAVINGE"></a> <a id="_CPPv2N17wifi_err_reason_t26WIFI_REASON_DEAUTH_LEAVINGE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ae41fb8600a5cf9d95b218c6fe903f588"></a> enumerator WIFI\_REASON\_DEAUTH\_LEAVING

    <a id="_CPPv4N17wifi_err_reason_t38WIFI_REASON_DISASSOC_DUE_TO_INACTIVITYE"></a>

    <a id="_CPPv3N17wifi_err_reason_t38WIFI_REASON_DISASSOC_DUE_TO_INACTIVITYE"></a> <a id="_CPPv2N17wifi_err_reason_t38WIFI_REASON_DISASSOC_DUE_TO_INACTIVITYE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a959f13c5cd53fe5b57ef28f7412d124d"></a> enumerator WIFI\_REASON\_DISASSOC\_DUE\_TO\_INACTIVITY

    <a id="_CPPv4N17wifi_err_reason_t28WIFI_REASON_DISASSOC_AP_BUSYE"></a>

    <a id="_CPPv3N17wifi_err_reason_t28WIFI_REASON_DISASSOC_AP_BUSYE"></a> <a id="_CPPv2N17wifi_err_reason_t28WIFI_REASON_DISASSOC_AP_BUSYE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357adf76631da677a459991221c5d3f3c151"></a> enumerator WIFI\_REASON\_DISASSOC\_AP\_BUSY

    <a id="_CPPv4N17wifi_err_reason_t41WIFI_REASON_CLASS2_FRAME_FROM_NONAUTH_STAE"></a>

    <a id="_CPPv3N17wifi_err_reason_t41WIFI_REASON_CLASS2_FRAME_FROM_NONAUTH_STAE"></a> <a id="_CPPv2N17wifi_err_reason_t41WIFI_REASON_CLASS2_FRAME_FROM_NONAUTH_STAE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a33038f81427b85bb06ebc96a5e4333b1"></a> enumerator WIFI\_REASON\_CLASS2\_FRAME\_FROM\_NONAUTH\_STA

    <a id="_CPPv4N17wifi_err_reason_t42WIFI_REASON_CLASS3_FRAME_FROM_NONASSOC_STAE"></a>

    <a id="_CPPv3N17wifi_err_reason_t42WIFI_REASON_CLASS3_FRAME_FROM_NONASSOC_STAE"></a> <a id="_CPPv2N17wifi_err_reason_t42WIFI_REASON_CLASS3_FRAME_FROM_NONASSOC_STAE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a82e17676f57006229f6560106fd0b778"></a> enumerator WIFI\_REASON\_CLASS3\_FRAME\_FROM\_NONASSOC\_STA

    <a id="_CPPv4N17wifi_err_reason_t33WIFI_REASON_DISASSOC_STA_HAS_LEFTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t33WIFI_REASON_DISASSOC_STA_HAS_LEFTE"></a> <a id="_CPPv2N17wifi_err_reason_t33WIFI_REASON_DISASSOC_STA_HAS_LEFTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ab987db2bf12af11504c38aa158f82f6b"></a> enumerator WIFI\_REASON\_DISASSOC\_STA\_HAS\_LEFT

    <a id="_CPPv4N17wifi_err_reason_t38WIFI_REASON_STA_REQ_ASSOC_WITHOUT_AUTHE"></a>

    <a id="_CPPv3N17wifi_err_reason_t38WIFI_REASON_STA_REQ_ASSOC_WITHOUT_AUTHE"></a> <a id="_CPPv2N17wifi_err_reason_t38WIFI_REASON_STA_REQ_ASSOC_WITHOUT_AUTHE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a08e67aa577437487eee2f070c029e824"></a> enumerator WIFI\_REASON\_STA\_REQ\_ASSOC\_WITHOUT\_AUTH

    <a id="_CPPv4N17wifi_err_reason_t36WIFI_REASON_PWR_CAPABILITY_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t36WIFI_REASON_PWR_CAPABILITY_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t36WIFI_REASON_PWR_CAPABILITY_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ab8cb5d125a4528950b1f8afb47114bbc"></a> enumerator WIFI\_REASON\_PWR\_CAPABILITY\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t39WIFI_REASON_SUPPORTED_CHANNEL_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t39WIFI_REASON_SUPPORTED_CHANNEL_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t39WIFI_REASON_SUPPORTED_CHANNEL_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a131dc746f66ae4ce7110bbba1627ee30"></a> enumerator WIFI\_REASON\_SUPPORTED\_CHANNEL\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t35WIFI_REASON_BSS_TRANSITION_DISASSOCE"></a>

    <a id="_CPPv3N17wifi_err_reason_t35WIFI_REASON_BSS_TRANSITION_DISASSOCE"></a> <a id="_CPPv2N17wifi_err_reason_t35WIFI_REASON_BSS_TRANSITION_DISASSOCE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ae016c532830e08f69dbf730af6869bc7"></a> enumerator WIFI\_REASON\_BSS\_TRANSITION\_DISASSOC

    <a id="_CPPv4N17wifi_err_reason_t22WIFI_REASON_INVALID_IEE"></a>

    <a id="_CPPv3N17wifi_err_reason_t22WIFI_REASON_INVALID_IEE"></a> <a id="_CPPv2N17wifi_err_reason_t22WIFI_REASON_INVALID_IEE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a89b89284499f00a44ffb448c41f6d7c1"></a> enumerator WIFI\_REASON\_INVALID\_IE

    <a id="_CPPv4N17wifi_err_reason_t31WIFI_REASON_MICHAEL_MIC_FAILUREE"></a>

    <a id="_CPPv3N17wifi_err_reason_t31WIFI_REASON_MICHAEL_MIC_FAILUREE"></a> <a id="_CPPv2N17wifi_err_reason_t31WIFI_REASON_MICHAEL_MIC_FAILUREE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a8665f4acc6ef6f1ec2a5273dc257638b"></a> enumerator WIFI\_REASON\_MICHAEL\_MIC\_FAILURE

    <a id="_CPPv4N17wifi_err_reason_t34WIFI_REASON_4WAY_HANDSHAKE_TIMEOUTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t34WIFI_REASON_4WAY_HANDSHAKE_TIMEOUTE"></a> <a id="_CPPv2N17wifi_err_reason_t34WIFI_REASON_4WAY_HANDSHAKE_TIMEOUTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ac9fc8823a1c371dfb1c39daeb8090b44"></a> enumerator WIFI\_REASON\_4WAY\_HANDSHAKE\_TIMEOUT

    <a id="_CPPv4N17wifi_err_reason_t36WIFI_REASON_GROUP_KEY_UPDATE_TIMEOUTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t36WIFI_REASON_GROUP_KEY_UPDATE_TIMEOUTE"></a> <a id="_CPPv2N17wifi_err_reason_t36WIFI_REASON_GROUP_KEY_UPDATE_TIMEOUTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a1271a3cb9f8c81b796054ce88ca3f51d"></a> enumerator WIFI\_REASON\_GROUP\_KEY\_UPDATE\_TIMEOUT

    <a id="_CPPv4N17wifi_err_reason_t30WIFI_REASON_IE_IN_4WAY_DIFFERSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t30WIFI_REASON_IE_IN_4WAY_DIFFERSE"></a> <a id="_CPPv2N17wifi_err_reason_t30WIFI_REASON_IE_IN_4WAY_DIFFERSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ac44df5ca9975e4d70d6afe2357f00390"></a> enumerator WIFI\_REASON\_IE\_IN\_4WAY\_DIFFERS

    <a id="_CPPv4N17wifi_err_reason_t34WIFI_REASON_GROUP_CIPHER_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t34WIFI_REASON_GROUP_CIPHER_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t34WIFI_REASON_GROUP_CIPHER_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357add540d0cbd39c63068e62d784a3017da"></a> enumerator WIFI\_REASON\_GROUP\_CIPHER\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t37WIFI_REASON_PAIRWISE_CIPHER_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t37WIFI_REASON_PAIRWISE_CIPHER_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t37WIFI_REASON_PAIRWISE_CIPHER_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a39ae347e702c2262cb41da348f14550e"></a> enumerator WIFI\_REASON\_PAIRWISE\_CIPHER\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t26WIFI_REASON_AKMP_NOT_VALIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t26WIFI_REASON_AKMP_NOT_VALIDE"></a> <a id="_CPPv2N17wifi_err_reason_t26WIFI_REASON_AKMP_NOT_VALIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a9d3f3cb0bf8d2e5b15ed7966e60fe112"></a> enumerator WIFI\_REASON\_AKMP\_NOT\_VALID

    <a id="_CPPv4N17wifi_err_reason_t38WIFI_REASON_UNSUPPORTED_RSN_IE_VERSIONE"></a>

    <a id="_CPPv3N17wifi_err_reason_t38WIFI_REASON_UNSUPPORTED_RSN_IE_VERSIONE"></a> <a id="_CPPv2N17wifi_err_reason_t38WIFI_REASON_UNSUPPORTED_RSN_IE_VERSIONE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a417f54751618433d59f85150866c03ef"></a> enumerator WIFI\_REASON\_UNSUPPORTED\_RSN\_IE\_VERSION

    <a id="_CPPv4N17wifi_err_reason_t32WIFI_REASON_INVALID_RSN_IE_CAPABE"></a>

    <a id="_CPPv3N17wifi_err_reason_t32WIFI_REASON_INVALID_RSN_IE_CAPABE"></a> <a id="_CPPv2N17wifi_err_reason_t32WIFI_REASON_INVALID_RSN_IE_CAPABE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a0b810d356a6df8102ec0450e1c9a0618"></a> enumerator WIFI\_REASON\_INVALID\_RSN\_IE\_CAPAB

    <a id="_CPPv4N17wifi_err_reason_t35WIFI_REASON_IEEE_802_1X_AUTH_FAILEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t35WIFI_REASON_IEEE_802_1X_AUTH_FAILEDE"></a> <a id="_CPPv2N17wifi_err_reason_t35WIFI_REASON_IEEE_802_1X_AUTH_FAILEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a9993167a1a1889c923fcb27ff63b2c25"></a> enumerator WIFI\_REASON\_IEEE\_802\_1X\_AUTH\_FAILED

    <a id="_CPPv4N17wifi_err_reason_t33WIFI_REASON_CIPHER_SUITE_REJECTEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t33WIFI_REASON_CIPHER_SUITE_REJECTEDE"></a> <a id="_CPPv2N17wifi_err_reason_t33WIFI_REASON_CIPHER_SUITE_REJECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357aca4ebf78c471b5da5e057175a612e911"></a> enumerator WIFI\_REASON\_CIPHER\_SUITE\_REJECTED

    <a id="_CPPv4N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNREACHABLEE"></a>

    <a id="_CPPv3N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNREACHABLEE"></a> <a id="_CPPv2N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNREACHABLEE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a215e65911c8c23926fded83fa39c822b"></a> enumerator WIFI\_REASON\_TDLS\_TEARDOWN\_UNREACHABLE

    <a id="_CPPv4N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNSPECIFIEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNSPECIFIEDE"></a> <a id="_CPPv2N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNSPECIFIEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a7fd7c75f431d097e921d822bc92cf96b"></a> enumerator WIFI\_REASON\_TDLS\_TEARDOWN\_UNSPECIFIED

    <a id="_CPPv4N17wifi_err_reason_t34WIFI_REASON_SSP_REQUESTED_DISASSOCE"></a>

    <a id="_CPPv3N17wifi_err_reason_t34WIFI_REASON_SSP_REQUESTED_DISASSOCE"></a> <a id="_CPPv2N17wifi_err_reason_t34WIFI_REASON_SSP_REQUESTED_DISASSOCE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357adae236d4d38412f34602e992a20de7a7"></a> enumerator WIFI\_REASON\_SSP\_REQUESTED\_DISASSOC

    <a id="_CPPv4N17wifi_err_reason_t36WIFI_REASON_NO_SSP_ROAMING_AGREEMENTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t36WIFI_REASON_NO_SSP_ROAMING_AGREEMENTE"></a> <a id="_CPPv2N17wifi_err_reason_t36WIFI_REASON_NO_SSP_ROAMING_AGREEMENTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ae7ea7d61d8ae4c2429e6f71af84d50b1"></a> enumerator WIFI\_REASON\_NO\_SSP\_ROAMING\_AGREEMENT

    <a id="_CPPv4N17wifi_err_reason_t29WIFI_REASON_BAD_CIPHER_OR_AKME"></a>

    <a id="_CPPv3N17wifi_err_reason_t29WIFI_REASON_BAD_CIPHER_OR_AKME"></a> <a id="_CPPv2N17wifi_err_reason_t29WIFI_REASON_BAD_CIPHER_OR_AKME"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a63149e9c5e84c991688377aead698e9a"></a> enumerator WIFI\_REASON\_BAD\_CIPHER\_OR\_AKM

    <a id="_CPPv4N17wifi_err_reason_t40WIFI_REASON_NOT_AUTHORIZED_THIS_LOCATIONE"></a>

    <a id="_CPPv3N17wifi_err_reason_t40WIFI_REASON_NOT_AUTHORIZED_THIS_LOCATIONE"></a> <a id="_CPPv2N17wifi_err_reason_t40WIFI_REASON_NOT_AUTHORIZED_THIS_LOCATIONE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a65e5541e83035e905a7234ea4234c46a"></a> enumerator WIFI\_REASON\_NOT\_AUTHORIZED\_THIS\_LOCATION

    <a id="_CPPv4N17wifi_err_reason_t39WIFI_REASON_SERVICE_CHANGE_PRECLUDES_TSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t39WIFI_REASON_SERVICE_CHANGE_PRECLUDES_TSE"></a> <a id="_CPPv2N17wifi_err_reason_t39WIFI_REASON_SERVICE_CHANGE_PRECLUDES_TSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a82330c591a483eeeae2acbc1a1d11bda"></a> enumerator WIFI\_REASON\_SERVICE\_CHANGE\_PRECLUDES\_TS

    <a id="_CPPv4N17wifi_err_reason_t34WIFI_REASON_UNSPECIFIED_QOS_REASONE"></a>

    <a id="_CPPv3N17wifi_err_reason_t34WIFI_REASON_UNSPECIFIED_QOS_REASONE"></a> <a id="_CPPv2N17wifi_err_reason_t34WIFI_REASON_UNSPECIFIED_QOS_REASONE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a05abcccc4f4ba52fd60761f253b82087"></a> enumerator WIFI\_REASON\_UNSPECIFIED\_QOS\_REASON

    <a id="_CPPv4N17wifi_err_reason_t32WIFI_REASON_NOT_ENOUGH_BANDWIDTHE"></a>

    <a id="_CPPv3N17wifi_err_reason_t32WIFI_REASON_NOT_ENOUGH_BANDWIDTHE"></a> <a id="_CPPv2N17wifi_err_reason_t32WIFI_REASON_NOT_ENOUGH_BANDWIDTHE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a88328baecd33bd4912f35826ffef4ba5"></a> enumerator WIFI\_REASON\_NOT\_ENOUGH\_BANDWIDTH

    <a id="_CPPv4N17wifi_err_reason_t28WIFI_REASON_DISASSOC_LOW_ACKE"></a>

    <a id="_CPPv3N17wifi_err_reason_t28WIFI_REASON_DISASSOC_LOW_ACKE"></a> <a id="_CPPv2N17wifi_err_reason_t28WIFI_REASON_DISASSOC_LOW_ACKE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a999c07b2c62f5971083506245ca231d6"></a> enumerator WIFI\_REASON\_DISASSOC\_LOW\_ACK

    <a id="_CPPv4N17wifi_err_reason_t25WIFI_REASON_EXCEEDED_TXOPE"></a>

    <a id="_CPPv3N17wifi_err_reason_t25WIFI_REASON_EXCEEDED_TXOPE"></a> <a id="_CPPv2N17wifi_err_reason_t25WIFI_REASON_EXCEEDED_TXOPE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a7668084413d351d497c250eee7387d6d"></a> enumerator WIFI\_REASON\_EXCEEDED\_TXOP

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_STA_LEAVINGE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_STA_LEAVINGE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_STA_LEAVINGE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357add591c1bedadd550edaffe45ab879e6b"></a> enumerator WIFI\_REASON\_STA\_LEAVING

    <a id="_CPPv4N17wifi_err_reason_t25WIFI_REASON_END_TS_BA_DLSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t25WIFI_REASON_END_TS_BA_DLSE"></a> <a id="_CPPv2N17wifi_err_reason_t25WIFI_REASON_END_TS_BA_DLSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a040cd385166c966f9e5ab2b11794025b"></a> enumerator WIFI\_REASON\_END\_TS\_BA\_DLS

    <a id="_CPPv4N17wifi_err_reason_t25WIFI_REASON_UNKNOWN_TS_BAE"></a>

    <a id="_CPPv3N17wifi_err_reason_t25WIFI_REASON_UNKNOWN_TS_BAE"></a> <a id="_CPPv2N17wifi_err_reason_t25WIFI_REASON_UNKNOWN_TS_BAE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ad2f05a777c06f8b54e053a56754fb4c8"></a> enumerator WIFI\_REASON\_UNKNOWN\_TS\_BA

    <a id="_CPPv4N17wifi_err_reason_t19WIFI_REASON_TIMEOUTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t19WIFI_REASON_TIMEOUTE"></a> <a id="_CPPv2N17wifi_err_reason_t19WIFI_REASON_TIMEOUTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357abf48fd373a4f12e000d90e713ee3a5f1"></a> enumerator WIFI\_REASON\_TIMEOUT

    <a id="_CPPv4N17wifi_err_reason_t28WIFI_REASON_PEERKEY_MISMATCHE"></a>

    <a id="_CPPv3N17wifi_err_reason_t28WIFI_REASON_PEERKEY_MISMATCHE"></a> <a id="_CPPv2N17wifi_err_reason_t28WIFI_REASON_PEERKEY_MISMATCHE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357aa2e5d3fa9760b684462d18061d09b071"></a> enumerator WIFI\_REASON\_PEERKEY\_MISMATCH

    <a id="_CPPv4N17wifi_err_reason_t43WIFI_REASON_AUTHORIZED_ACCESS_LIMIT_REACHEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t43WIFI_REASON_AUTHORIZED_ACCESS_LIMIT_REACHEDE"></a> <a id="_CPPv2N17wifi_err_reason_t43WIFI_REASON_AUTHORIZED_ACCESS_LIMIT_REACHEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a566f9c1c3a8408ed5249e2ba1771aa70"></a> enumerator WIFI\_REASON\_AUTHORIZED\_ACCESS\_LIMIT\_REACHED

    <a id="_CPPv4N17wifi_err_reason_t41WIFI_REASON_EXTERNAL_SERVICE_REQUIREMENTSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t41WIFI_REASON_EXTERNAL_SERVICE_REQUIREMENTSE"></a> <a id="_CPPv2N17wifi_err_reason_t41WIFI_REASON_EXTERNAL_SERVICE_REQUIREMENTSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a443f64781f1e5d1d8d296504a2f6dc68"></a> enumerator WIFI\_REASON\_EXTERNAL\_SERVICE\_REQUIREMENTS

    <a id="_CPPv4N17wifi_err_reason_t41WIFI_REASON_INVALID_FT_ACTION_FRAME_COUNTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t41WIFI_REASON_INVALID_FT_ACTION_FRAME_COUNTE"></a> <a id="_CPPv2N17wifi_err_reason_t41WIFI_REASON_INVALID_FT_ACTION_FRAME_COUNTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a8c766be339cb1667638adf86576f517b"></a> enumerator WIFI\_REASON\_INVALID\_FT\_ACTION\_FRAME\_COUNT

    <a id="_CPPv4N17wifi_err_reason_t25WIFI_REASON_INVALID_PMKIDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t25WIFI_REASON_INVALID_PMKIDE"></a> <a id="_CPPv2N17wifi_err_reason_t25WIFI_REASON_INVALID_PMKIDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a80c5e73cdd5cb3b2e1fef1e3509d7ab7"></a> enumerator WIFI\_REASON\_INVALID\_PMKID

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_INVALID_MDEE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_INVALID_MDEE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_INVALID_MDEE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357aa411dacf36d46f92cb90afae19cf48ab"></a> enumerator WIFI\_REASON\_INVALID\_MDE

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_INVALID_FTEE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_INVALID_FTEE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_INVALID_FTEE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a5ae6446bf31d57f4ccc66eb457b33f61"></a> enumerator WIFI\_REASON\_INVALID\_FTE

    <a id="_CPPv4N17wifi_err_reason_t34WIFI_REASON_MESH_PEERING_CANCELLEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t34WIFI_REASON_MESH_PEERING_CANCELLEDE"></a> <a id="_CPPv2N17wifi_err_reason_t34WIFI_REASON_MESH_PEERING_CANCELLEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a6b1eda6f35920b3bf55109e9c39241e2"></a> enumerator WIFI\_REASON\_MESH\_PEERING\_CANCELLED

    <a id="_CPPv4N17wifi_err_reason_t26WIFI_REASON_MESH_MAX_PEERSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t26WIFI_REASON_MESH_MAX_PEERSE"></a> <a id="_CPPv2N17wifi_err_reason_t26WIFI_REASON_MESH_MAX_PEERSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357abf3a452a2c8cb3d6a6ae096815687de9"></a> enumerator WIFI\_REASON\_MESH\_MAX\_PEERS

    <a id="_CPPv4N17wifi_err_reason_t40WIFI_REASON_MESH_CONFIG_POLICY_VIOLATIONE"></a>

    <a id="_CPPv3N17wifi_err_reason_t40WIFI_REASON_MESH_CONFIG_POLICY_VIOLATIONE"></a> <a id="_CPPv2N17wifi_err_reason_t40WIFI_REASON_MESH_CONFIG_POLICY_VIOLATIONE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a7a7754fb7300c0e91cebbebb42775f95"></a> enumerator WIFI\_REASON\_MESH\_CONFIG\_POLICY\_VIOLATION

    <a id="_CPPv4N17wifi_err_reason_t27WIFI_REASON_MESH_CLOSE_RCVDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t27WIFI_REASON_MESH_CLOSE_RCVDE"></a> <a id="_CPPv2N17wifi_err_reason_t27WIFI_REASON_MESH_CLOSE_RCVDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357af5e0a3e9e5d506b7edb166ba248bba44"></a> enumerator WIFI\_REASON\_MESH\_CLOSE\_RCVD

    <a id="_CPPv4N17wifi_err_reason_t28WIFI_REASON_MESH_MAX_RETRIESE"></a>

    <a id="_CPPv3N17wifi_err_reason_t28WIFI_REASON_MESH_MAX_RETRIESE"></a> <a id="_CPPv2N17wifi_err_reason_t28WIFI_REASON_MESH_MAX_RETRIESE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ae74a633ca82e9b09edf2cbaecb67b8df"></a> enumerator WIFI\_REASON\_MESH\_MAX\_RETRIES

    <a id="_CPPv4N17wifi_err_reason_t32WIFI_REASON_MESH_CONFIRM_TIMEOUTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t32WIFI_REASON_MESH_CONFIRM_TIMEOUTE"></a> <a id="_CPPv2N17wifi_err_reason_t32WIFI_REASON_MESH_CONFIRM_TIMEOUTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a13e4c1892196f91b050a1d12d3b2136a"></a> enumerator WIFI\_REASON\_MESH\_CONFIRM\_TIMEOUT

    <a id="_CPPv4N17wifi_err_reason_t28WIFI_REASON_MESH_INVALID_GTKE"></a>

    <a id="_CPPv3N17wifi_err_reason_t28WIFI_REASON_MESH_INVALID_GTKE"></a> <a id="_CPPv2N17wifi_err_reason_t28WIFI_REASON_MESH_INVALID_GTKE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357aeda8587c6defef19a15d827687c99723"></a> enumerator WIFI\_REASON\_MESH\_INVALID\_GTK

    <a id="_CPPv4N17wifi_err_reason_t36WIFI_REASON_MESH_INCONSISTENT_PARAMSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t36WIFI_REASON_MESH_INCONSISTENT_PARAMSE"></a> <a id="_CPPv2N17wifi_err_reason_t36WIFI_REASON_MESH_INCONSISTENT_PARAMSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ac92b7ce586eaacfee48fd6ca60ab32fd"></a> enumerator WIFI\_REASON\_MESH\_INCONSISTENT\_PARAMS

    <a id="_CPPv4N17wifi_err_reason_t37WIFI_REASON_MESH_INVALID_SECURITY_CAPE"></a>

    <a id="_CPPv3N17wifi_err_reason_t37WIFI_REASON_MESH_INVALID_SECURITY_CAPE"></a> <a id="_CPPv2N17wifi_err_reason_t37WIFI_REASON_MESH_INVALID_SECURITY_CAPE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357acff0977b60ba0201cc000afeeac159db"></a> enumerator WIFI\_REASON\_MESH\_INVALID\_SECURITY\_CAP

    <a id="_CPPv4N17wifi_err_reason_t41WIFI_REASON_MESH_PATH_ERROR_NO_PROXY_INFOE"></a>

    <a id="_CPPv3N17wifi_err_reason_t41WIFI_REASON_MESH_PATH_ERROR_NO_PROXY_INFOE"></a> <a id="_CPPv2N17wifi_err_reason_t41WIFI_REASON_MESH_PATH_ERROR_NO_PROXY_INFOE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a5403edf3f9c99372fb24d3d0c6e362ec"></a> enumerator WIFI\_REASON\_MESH\_PATH\_ERROR\_NO\_PROXY\_INFO

    <a id="_CPPv4N17wifi_err_reason_t46WIFI_REASON_MESH_PATH_ERROR_NO_FORWARDING_INFOE"></a>

    <a id="_CPPv3N17wifi_err_reason_t46WIFI_REASON_MESH_PATH_ERROR_NO_FORWARDING_INFOE"></a> <a id="_CPPv2N17wifi_err_reason_t46WIFI_REASON_MESH_PATH_ERROR_NO_FORWARDING_INFOE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357af4c91cecda66e66285fad2c02270df3d"></a> enumerator WIFI\_REASON\_MESH\_PATH\_ERROR\_NO\_FORWARDING\_INFO

    <a id="_CPPv4N17wifi_err_reason_t44WIFI_REASON_MESH_PATH_ERROR_DEST_UNREACHABLEE"></a>

    <a id="_CPPv3N17wifi_err_reason_t44WIFI_REASON_MESH_PATH_ERROR_DEST_UNREACHABLEE"></a> <a id="_CPPv2N17wifi_err_reason_t44WIFI_REASON_MESH_PATH_ERROR_DEST_UNREACHABLEE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357ac0c9474e2c67608652462ae95d76f496"></a> enumerator WIFI\_REASON\_MESH\_PATH\_ERROR\_DEST\_UNREACHABLE

    <a id="_CPPv4N17wifi_err_reason_t46WIFI_REASON_MAC_ADDRESS_ALREADY_EXISTS_IN_MBSSE"></a>

    <a id="_CPPv3N17wifi_err_reason_t46WIFI_REASON_MAC_ADDRESS_ALREADY_EXISTS_IN_MBSSE"></a> <a id="_CPPv2N17wifi_err_reason_t46WIFI_REASON_MAC_ADDRESS_ALREADY_EXISTS_IN_MBSSE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a5aca4931966b6b7f27006731e3292202"></a> enumerator WIFI\_REASON\_MAC\_ADDRESS\_ALREADY\_EXISTS\_IN\_MBSS

    <a id="_CPPv4N17wifi_err_reason_t46WIFI_REASON_MESH_CHANNEL_SWITCH_REGULATORY_REQE"></a>

    <a id="_CPPv3N17wifi_err_reason_t46WIFI_REASON_MESH_CHANNEL_SWITCH_REGULATORY_REQE"></a> <a id="_CPPv2N17wifi_err_reason_t46WIFI_REASON_MESH_CHANNEL_SWITCH_REGULATORY_REQE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a5a57cf5fe5ee4546505536064f8d216b"></a> enumerator WIFI\_REASON\_MESH\_CHANNEL\_SWITCH\_REGULATORY\_REQ

    <a id="_CPPv4N17wifi_err_reason_t43WIFI_REASON_MESH_CHANNEL_SWITCH_UNSPECIFIEDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t43WIFI_REASON_MESH_CHANNEL_SWITCH_UNSPECIFIEDE"></a> <a id="_CPPv2N17wifi_err_reason_t43WIFI_REASON_MESH_CHANNEL_SWITCH_UNSPECIFIEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a7169d1770e021ac4d9caf58ef930b7b8"></a> enumerator WIFI\_REASON\_MESH\_CHANNEL\_SWITCH\_UNSPECIFIED

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_BEACON_LOSTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_BEACON_LOSTE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_BEACON_LOSTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a062cefbcbce2d1ab72e5c125fc644ab1"></a> enumerator WIFI\_REASON\_BEACON\_LOST
    :   The BK STA can’t detect the beacon of the connected AP

    <a id="_CPPv4N17wifi_err_reason_t23WIFI_REASON_NO_AP_FOUNDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t23WIFI_REASON_NO_AP_FOUNDE"></a> <a id="_CPPv2N17wifi_err_reason_t23WIFI_REASON_NO_AP_FOUNDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357af82af1859d31e0937c7270d9cc9d9206"></a> enumerator WIFI\_REASON\_NO\_AP\_FOUND
    :   Can’t find the target AP

    <a id="_CPPv4N17wifi_err_reason_t26WIFI_REASON_WRONG_PASSWORDE"></a>

    <a id="_CPPv3N17wifi_err_reason_t26WIFI_REASON_WRONG_PASSWORDE"></a> <a id="_CPPv2N17wifi_err_reason_t26WIFI_REASON_WRONG_PASSWORDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a05668c52edd86c86cb54a1e60b635cb5"></a> enumerator WIFI\_REASON\_WRONG\_PASSWORD
    :   The password is wrong

    <a id="_CPPv4N17wifi_err_reason_t29WIFI_REASON_DISCONNECT_BY_APPE"></a>

    <a id="_CPPv3N17wifi_err_reason_t29WIFI_REASON_DISCONNECT_BY_APPE"></a> <a id="_CPPv2N17wifi_err_reason_t29WIFI_REASON_DISCONNECT_BY_APPE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a8020cf41e19caed91a3ac9eb40de87de"></a> enumerator WIFI\_REASON\_DISCONNECT\_BY\_APP
    :   The BK STA disconnected by application

    <a id="_CPPv4N17wifi_err_reason_t24WIFI_REASON_DHCP_TIMEOUTE"></a>

    <a id="_CPPv3N17wifi_err_reason_t24WIFI_REASON_DHCP_TIMEOUTE"></a> <a id="_CPPv2N17wifi_err_reason_t24WIFI_REASON_DHCP_TIMEOUTE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a442ca60ac9b344d4338487f8dd1f4fd3"></a> enumerator WIFI\_REASON\_DHCP\_TIMEOUT
    :   The BK STA dhcp timeout, 20s

    <a id="_CPPv4N17wifi_err_reason_t36WIFI_REASON_SECURITY_LEVEL_NOT_MATCHE"></a>

    <a id="_CPPv3N17wifi_err_reason_t36WIFI_REASON_SECURITY_LEVEL_NOT_MATCHE"></a> <a id="_CPPv2N17wifi_err_reason_t36WIFI_REASON_SECURITY_LEVEL_NOT_MATCHE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357a48414853cf8ac50892a41d056007b8e0"></a> enumerator WIFI\_REASON\_SECURITY\_LEVEL\_NOT\_MATCH
    :   The AP’s security level is too low

    <a id="_CPPv4N17wifi_err_reason_t15WIFI_REASON_MAXE"></a>

    <a id="_CPPv3N17wifi_err_reason_t15WIFI_REASON_MAXE"></a> <a id="_CPPv2N17wifi_err_reason_t15WIFI_REASON_MAXE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaf2f44e69763071bbe8c3903158c5a357abb99e24bbd9427f0708c926b0de86b2d"></a> enumerator WIFI\_REASON\_MAX
    :   The BK STA connect success

<a id="_CPPv415wifi_security_t"></a>

<a id="_CPPv315wifi_security_t"></a> <a id="_CPPv215wifi_security_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga010e38e08f1370cc671b2f65a26042ad"></a> enum wifi\_security\_t
:   *Values:*

    <a id="_CPPv4N15wifi_security_t18WIFI_SECURITY_NONEE"></a>

    <a id="_CPPv3N15wifi_security_t18WIFI_SECURITY_NONEE"></a> <a id="_CPPv2N15wifi_security_t18WIFI_SECURITY_NONEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada33a293ccf3a4ffe3ad24bda9145190a9"></a> enumerator WIFI\_SECURITY\_NONE
    :   Open system.

    <a id="_CPPv4N15wifi_security_t17WIFI_SECURITY_WEPE"></a>

    <a id="_CPPv3N15wifi_security_t17WIFI_SECURITY_WEPE"></a> <a id="_CPPv2N15wifi_security_t17WIFI_SECURITY_WEPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada2051e50876375942df94bdd2e1f5dae6"></a> enumerator WIFI\_SECURITY\_WEP
    :   WEP security, **it’s unsafe security, please don’t use it**

    <a id="_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA_TKIPE"></a>

    <a id="_CPPv3N15wifi_security_t22WIFI_SECURITY_WPA_TKIPE"></a> <a id="_CPPv2N15wifi_security_t22WIFI_SECURITY_WPA_TKIPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada40fb9b4f6c3427830eb50439b9009ea4"></a> enumerator WIFI\_SECURITY\_WPA\_TKIP
    :   WPA TKIP

    <a id="_CPPv4N15wifi_security_t21WIFI_SECURITY_WPA_AESE"></a>

    <a id="_CPPv3N15wifi_security_t21WIFI_SECURITY_WPA_AESE"></a> <a id="_CPPv2N15wifi_security_t21WIFI_SECURITY_WPA_AESE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042adaa13f938cb24eea07b70eabd66ade152b"></a> enumerator WIFI\_SECURITY\_WPA\_AES
    :   WPA AES

    <a id="_CPPv4N15wifi_security_t23WIFI_SECURITY_WPA_MIXEDE"></a>

    <a id="_CPPv3N15wifi_security_t23WIFI_SECURITY_WPA_MIXEDE"></a> <a id="_CPPv2N15wifi_security_t23WIFI_SECURITY_WPA_MIXEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada6e920955c329f296285d0833c41f5424"></a> enumerator WIFI\_SECURITY\_WPA\_MIXED
    :   WPA AES or TKIP

    <a id="_CPPv4N15wifi_security_t23WIFI_SECURITY_WPA2_TKIPE"></a>

    <a id="_CPPv3N15wifi_security_t23WIFI_SECURITY_WPA2_TKIPE"></a> <a id="_CPPv2N15wifi_security_t23WIFI_SECURITY_WPA2_TKIPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada09ae5057124a07bd0a01951e4ae6a7c2"></a> enumerator WIFI\_SECURITY\_WPA2\_TKIP
    :   WPA2 TKIP

    <a id="_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA2_AESE"></a>

    <a id="_CPPv3N15wifi_security_t22WIFI_SECURITY_WPA2_AESE"></a> <a id="_CPPv2N15wifi_security_t22WIFI_SECURITY_WPA2_AESE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada573efbfc2c9182f319b301ba2584fc46"></a> enumerator WIFI\_SECURITY\_WPA2\_AES
    :   WPA2 AES

    <a id="_CPPv4N15wifi_security_t24WIFI_SECURITY_WPA2_MIXEDE"></a>

    <a id="_CPPv3N15wifi_security_t24WIFI_SECURITY_WPA2_MIXEDE"></a> <a id="_CPPv2N15wifi_security_t24WIFI_SECURITY_WPA2_MIXEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042adaf66ff147f179d4808272771237b60533"></a> enumerator WIFI\_SECURITY\_WPA2\_MIXED
    :   WPA2 AES or TKIP

    <a id="_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA3_SAEE"></a>

    <a id="_CPPv3N15wifi_security_t22WIFI_SECURITY_WPA3_SAEE"></a> <a id="_CPPv2N15wifi_security_t22WIFI_SECURITY_WPA3_SAEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada111c17fe9ff0e63765051aa41406ce0e"></a> enumerator WIFI\_SECURITY\_WPA3\_SAE
    :   WPA3 SAE

    <a id="_CPPv4N15wifi_security_t29WIFI_SECURITY_WPA3_WPA2_MIXEDE"></a>

    <a id="_CPPv3N15wifi_security_t29WIFI_SECURITY_WPA3_WPA2_MIXEDE"></a> <a id="_CPPv2N15wifi_security_t29WIFI_SECURITY_WPA3_WPA2_MIXEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042adab90b89fbe6f6820a5e9fa243f85aceea"></a> enumerator WIFI\_SECURITY\_WPA3\_WPA2\_MIXED
    :   WPA3 SAE or WPA2 AES

    <a id="_CPPv4N15wifi_security_t17WIFI_SECURITY_EAPE"></a>

    <a id="_CPPv3N15wifi_security_t17WIFI_SECURITY_EAPE"></a> <a id="_CPPv2N15wifi_security_t17WIFI_SECURITY_EAPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada0a1de0eb5a7a0dba682a19ffb7cf8103"></a> enumerator WIFI\_SECURITY\_EAP
    :   EAP

    <a id="_CPPv4N15wifi_security_t17WIFI_SECURITY_OWEE"></a>

    <a id="_CPPv3N15wifi_security_t17WIFI_SECURITY_OWEE"></a> <a id="_CPPv2N15wifi_security_t17WIFI_SECURITY_OWEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada48e16f954c45a290cff801ca20586f0f"></a> enumerator WIFI\_SECURITY\_OWE
    :   OWE

    <a id="_CPPv4N15wifi_security_t18WIFI_SECURITY_AUTOE"></a>

    <a id="_CPPv3N15wifi_security_t18WIFI_SECURITY_AUTOE"></a> <a id="_CPPv2N15wifi_security_t18WIFI_SECURITY_AUTOE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada67b77452432c7a01ffa6a3008941ad6c"></a> enumerator WIFI\_SECURITY\_AUTO
    :   WiFi automatically detect the security type

    <a id="_CPPv4N15wifi_security_t27WIFI_SECURITY_TYPE_WAPI_PSKE"></a>

    <a id="_CPPv3N15wifi_security_t27WIFI_SECURITY_TYPE_WAPI_PSKE"></a> <a id="_CPPv2N15wifi_security_t27WIFI_SECURITY_TYPE_WAPI_PSKE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada1358abe54efe484d0c67033fb2edd518"></a> enumerator WIFI\_SECURITY\_TYPE\_WAPI\_PSK

    <a id="_CPPv4N15wifi_security_t28WIFI_SECURITY_TYPE_WAPI_CERTE"></a>

    <a id="_CPPv3N15wifi_security_t28WIFI_SECURITY_TYPE_WAPI_CERTE"></a> <a id="_CPPv2N15wifi_security_t28WIFI_SECURITY_TYPE_WAPI_CERTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada6ed77c40d27fd70bc1a78a5581b242d5"></a> enumerator WIFI\_SECURITY\_TYPE\_WAPI\_CERT

    <a id="_CPPv4N15wifi_security_t31WIFI_SECURITY_TYPE_WAPI_UNKNOWNE"></a>

    <a id="_CPPv3N15wifi_security_t31WIFI_SECURITY_TYPE_WAPI_UNKNOWNE"></a> <a id="_CPPv2N15wifi_security_t31WIFI_SECURITY_TYPE_WAPI_UNKNOWNE"></a> <a id="group__bk__api__wifi__v2__enum_1gga010e38e08f1370cc671b2f65a26042ada1f6c634e21bf5622d4227ccaefef151f"></a> enumerator WIFI\_SECURITY\_TYPE\_WAPI\_UNKNOWN

<a id="_CPPv417wifi_link_state_t"></a>

<a id="_CPPv317wifi_link_state_t"></a> <a id="_CPPv217wifi_link_state_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga4173eff95b62808051ec8f9af3435b10"></a> enum wifi\_link\_state\_t
:   *Values:*

    <a id="_CPPv4N17wifi_link_state_t23WIFI_LINKSTATE_STA_IDLEE"></a>

    <a id="_CPPv3N17wifi_link_state_t23WIFI_LINKSTATE_STA_IDLEE"></a> <a id="_CPPv2N17wifi_link_state_t23WIFI_LINKSTATE_STA_IDLEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a09a516d7abd3c5681de1aadf097f4310"></a> enumerator WIFI\_LINKSTATE\_STA\_IDLE
    :   sta mode is idle

    <a id="_CPPv4N17wifi_link_state_t29WIFI_LINKSTATE_STA_CONNECTINGE"></a>

    <a id="_CPPv3N17wifi_link_state_t29WIFI_LINKSTATE_STA_CONNECTINGE"></a> <a id="_CPPv2N17wifi_link_state_t29WIFI_LINKSTATE_STA_CONNECTINGE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a6cdfde664c6840fb4d0736ca725e9df4"></a> enumerator WIFI\_LINKSTATE\_STA\_CONNECTING
    :   sta mode is connecting

    <a id="_CPPv4N17wifi_link_state_t31WIFI_LINKSTATE_STA_DISCONNECTEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t31WIFI_LINKSTATE_STA_DISCONNECTEDE"></a> <a id="_CPPv2N17wifi_link_state_t31WIFI_LINKSTATE_STA_DISCONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a284f9d36abc54bc38982213f63bf6e8b"></a> enumerator WIFI\_LINKSTATE\_STA\_DISCONNECTED
    :   sta mode is disconnected

    <a id="_CPPv4N17wifi_link_state_t28WIFI_LINKSTATE_STA_CONNECTEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t28WIFI_LINKSTATE_STA_CONNECTEDE"></a> <a id="_CPPv2N17wifi_link_state_t28WIFI_LINKSTATE_STA_CONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a26df5f7619ee219bd4aab733a8a63e62"></a> enumerator WIFI\_LINKSTATE\_STA\_CONNECTED
    :   sta mode is connected

    <a id="_CPPv4N17wifi_link_state_t33WIFI_LINKSTATE_STA_CONNECT_FAILEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t33WIFI_LINKSTATE_STA_CONNECT_FAILEDE"></a> <a id="_CPPv2N17wifi_link_state_t33WIFI_LINKSTATE_STA_CONNECT_FAILEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10aca4a8a6f8b98b6b23ae47b0d2be0965e"></a> enumerator WIFI\_LINKSTATE\_STA\_CONNECT\_FAILED
    :   sta mode is connec fail

    <a id="_CPPv4N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a>

    <a id="_CPPv3N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a> <a id="_CPPv2N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10ae63b6c62932542faeff9cdc3b1bccfad"></a> enumerator WIFI\_LINKSTATE\_STA\_GOT\_IP
    :   sta mode got ip

    <a id="_CPPv4N17wifi_link_state_t28WIFI_LINKSTATE_STA_SCAN_DONEE"></a>

    <a id="_CPPv3N17wifi_link_state_t28WIFI_LINKSTATE_STA_SCAN_DONEE"></a> <a id="_CPPv2N17wifi_link_state_t28WIFI_LINKSTATE_STA_SCAN_DONEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10ac9704f2e626449f014f21b2040f198e5"></a> enumerator WIFI\_LINKSTATE\_STA\_SCAN\_DONE

    <a id="_CPPv4N17wifi_link_state_t27WIFI_LINKSTATE_AP_CONNECTEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t27WIFI_LINKSTATE_AP_CONNECTEDE"></a> <a id="_CPPv2N17wifi_link_state_t27WIFI_LINKSTATE_AP_CONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a8c3041ca9da36552c1c879bf9f40bf53"></a> enumerator WIFI\_LINKSTATE\_AP\_CONNECTED
    :   softap mode, a client association success

    <a id="_CPPv4N17wifi_link_state_t30WIFI_LINKSTATE_AP_DISCONNECTEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t30WIFI_LINKSTATE_AP_DISCONNECTEDE"></a> <a id="_CPPv2N17wifi_link_state_t30WIFI_LINKSTATE_AP_DISCONNECTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10adb4180194c47e43de9b85af3d2913c56"></a> enumerator WIFI\_LINKSTATE\_AP\_DISCONNECTED
    :   softap mode, a client disconnect

    <a id="_CPPv4N17wifi_link_state_t32WIFI_LINKSTATE_AP_CONNECT_FAILEDE"></a>

    <a id="_CPPv3N17wifi_link_state_t32WIFI_LINKSTATE_AP_CONNECT_FAILEDE"></a> <a id="_CPPv2N17wifi_link_state_t32WIFI_LINKSTATE_AP_CONNECT_FAILEDE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10af5a9e0f229b6341f43ebd3c57e6e0e5b"></a> enumerator WIFI\_LINKSTATE\_AP\_CONNECT\_FAILED
    :   softap mode, a client association failed

    <a id="_CPPv4N17wifi_link_state_t18WIFI_LINKSTATE_MAXE"></a>

    <a id="_CPPv3N17wifi_link_state_t18WIFI_LINKSTATE_MAXE"></a> <a id="_CPPv2N17wifi_link_state_t18WIFI_LINKSTATE_MAXE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10a5ba0b8dc6fb0d9484d7ea70ae1b4dd9a"></a> enumerator WIFI\_LINKSTATE\_MAX
    :   reserved

<a id="_CPPv421wifi_country_policy_t"></a>

<a id="_CPPv321wifi_country_policy_t"></a> <a id="_CPPv221wifi_country_policy_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga5bc9a18309dadba51c6b33742b22caab"></a> enum wifi\_country\_policy\_t
:   *Values:*

    <a id="_CPPv4N21wifi_country_policy_t24WIFI_COUNTRY_POLICY_AUTOE"></a>

    <a id="_CPPv3N21wifi_country_policy_t24WIFI_COUNTRY_POLICY_AUTOE"></a> <a id="_CPPv2N21wifi_country_policy_t24WIFI_COUNTRY_POLICY_AUTOE"></a> <a id="group__bk__api__wifi__v2__enum_1gga5bc9a18309dadba51c6b33742b22caaba5e8710ac8a30e8f1bc27b0c4f6945301"></a> enumerator WIFI\_COUNTRY\_POLICY\_AUTO
    :   Country policy is auto, use the country info of AP to which the station is connected

    <a id="_CPPv4N21wifi_country_policy_t26WIFI_COUNTRY_POLICY_MANUALE"></a>

    <a id="_CPPv3N21wifi_country_policy_t26WIFI_COUNTRY_POLICY_MANUALE"></a> <a id="_CPPv2N21wifi_country_policy_t26WIFI_COUNTRY_POLICY_MANUALE"></a> <a id="group__bk__api__wifi__v2__enum_1gga5bc9a18309dadba51c6b33742b22caabad7e0750058f60a010b71d2445e44dde1"></a> enumerator WIFI\_COUNTRY\_POLICY\_MANUAL
    :   Country policy is manual, always use the configured country info

<a id="_CPPv421wifi_second_channel_t"></a>

<a id="_CPPv321wifi_second_channel_t"></a> <a id="_CPPv221wifi_second_channel_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga3306794e1a9adad8e00f7d68e7930805"></a> enum wifi\_second\_channel\_t
:   *Values:*

    <a id="_CPPv4N21wifi_second_channel_t24WIFI_SECOND_CHANNEL_NONEE"></a>

    <a id="_CPPv3N21wifi_second_channel_t24WIFI_SECOND_CHANNEL_NONEE"></a> <a id="_CPPv2N21wifi_second_channel_t24WIFI_SECOND_CHANNEL_NONEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga3306794e1a9adad8e00f7d68e7930805a58b87547af406c2cd74bc85612d148f2"></a> enumerator WIFI\_SECOND\_CHANNEL\_NONE
    :   HT20 mode, no secondary channel

    <a id="_CPPv4N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_ABOVEE"></a>

    <a id="_CPPv3N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_ABOVEE"></a> <a id="_CPPv2N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_ABOVEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga3306794e1a9adad8e00f7d68e7930805a891095a7e17644b9912d5470979954b1"></a> enumerator WIFI\_SECOND\_CHANNEL\_ABOVE
    :   Second channel is above the primary channel

    <a id="_CPPv4N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_BELOWE"></a>

    <a id="_CPPv3N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_BELOWE"></a> <a id="_CPPv2N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_BELOWE"></a> <a id="group__bk__api__wifi__v2__enum_1gga3306794e1a9adad8e00f7d68e7930805a904ab4a518e0a1b4e3b2bbb48cb6b358"></a> enumerator WIFI\_SECOND\_CHANNEL\_BELOW
    :   Second channel is below the primary channel

<a id="_CPPv417wifi_regulation_t"></a>

<a id="_CPPv317wifi_regulation_t"></a> <a id="_CPPv217wifi_regulation_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga37e2eea436f04320ed304089acce47e5"></a> enum wifi\_regulation\_t
:   *Values:*

    <a id="_CPPv4N17wifi_regulation_t14WIFI_REGU_NULLE"></a>

    <a id="_CPPv3N17wifi_regulation_t14WIFI_REGU_NULLE"></a> <a id="_CPPv2N17wifi_regulation_t14WIFI_REGU_NULLE"></a> <a id="group__bk__api__wifi__v2__enum_1gga37e2eea436f04320ed304089acce47e5a2b9d49ee82a9ae3de8c9b7caea8b276b"></a> enumerator WIFI\_REGU\_NULL

    <a id="_CPPv4N17wifi_regulation_t13WIFI_REGU_FCCE"></a>

    <a id="_CPPv3N17wifi_regulation_t13WIFI_REGU_FCCE"></a> <a id="_CPPv2N17wifi_regulation_t13WIFI_REGU_FCCE"></a> <a id="group__bk__api__wifi__v2__enum_1gga37e2eea436f04320ed304089acce47e5ad5c49dee3f40770637b7996c241e5d13"></a> enumerator WIFI\_REGU\_FCC

    <a id="_CPPv4N17wifi_regulation_t14WIFI_REGU_ETSIE"></a>

    <a id="_CPPv3N17wifi_regulation_t14WIFI_REGU_ETSIE"></a> <a id="_CPPv2N17wifi_regulation_t14WIFI_REGU_ETSIE"></a> <a id="group__bk__api__wifi__v2__enum_1gga37e2eea436f04320ed304089acce47e5a2da946c884d2b5a9ad6e29f794a97072"></a> enumerator WIFI\_REGU\_ETSI

    <a id="_CPPv4N17wifi_regulation_t13WIFI_REGU_MKKE"></a>

    <a id="_CPPv3N17wifi_regulation_t13WIFI_REGU_MKKE"></a> <a id="_CPPv2N17wifi_regulation_t13WIFI_REGU_MKKE"></a> <a id="group__bk__api__wifi__v2__enum_1gga37e2eea436f04320ed304089acce47e5aebc91b4082419bf07ec37d75db2901ab"></a> enumerator WIFI\_REGU\_MKK

    <a id="_CPPv4N17wifi_regulation_t13WIFI_REGU_EXTE"></a>

    <a id="_CPPv3N17wifi_regulation_t13WIFI_REGU_EXTE"></a> <a id="_CPPv2N17wifi_regulation_t13WIFI_REGU_EXTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga37e2eea436f04320ed304089acce47e5ad6bfafda7a5621fb772971568131cb60"></a> enumerator WIFI\_REGU\_EXT

<a id="_CPPv418wifi_ratesection_t"></a>

<a id="_CPPv318wifi_ratesection_t"></a> <a id="_CPPv218wifi_ratesection_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga4f8d473202c3e99fd3ea319e6d43531d"></a> enum wifi\_ratesection\_t
:   *Values:*

    <a id="_CPPv4N18wifi_ratesection_t12WIFI_RS_NULLE"></a>

    <a id="_CPPv3N18wifi_ratesection_t12WIFI_RS_NULLE"></a> <a id="_CPPv2N18wifi_ratesection_t12WIFI_RS_NULLE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531dae7c4a462fcd5464bd5be74bd1bec937d"></a> enumerator WIFI\_RS\_NULL

    <a id="_CPPv4N18wifi_ratesection_t11WIFI_RS_CCKE"></a>

    <a id="_CPPv3N18wifi_ratesection_t11WIFI_RS_CCKE"></a> <a id="_CPPv2N18wifi_ratesection_t11WIFI_RS_CCKE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531daa816a3830d8b26a8fdc2c08d213064b9"></a> enumerator WIFI\_RS\_CCK

    <a id="_CPPv4N18wifi_ratesection_t12WIFI_RS_OFDME"></a>

    <a id="_CPPv3N18wifi_ratesection_t12WIFI_RS_OFDME"></a> <a id="_CPPv2N18wifi_ratesection_t12WIFI_RS_OFDME"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531da654114e9a4a3d4f4273dc679a9be1ec9"></a> enumerator WIFI\_RS\_OFDM

    <a id="_CPPv4N18wifi_ratesection_t10WIFI_RS_HTE"></a>

    <a id="_CPPv3N18wifi_ratesection_t10WIFI_RS_HTE"></a> <a id="_CPPv2N18wifi_ratesection_t10WIFI_RS_HTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531da307e25d4b9f6cf12022de6f80aa9ee1a"></a> enumerator WIFI\_RS\_HT

    <a id="_CPPv4N18wifi_ratesection_t11WIFI_RS_VHTE"></a>

    <a id="_CPPv3N18wifi_ratesection_t11WIFI_RS_VHTE"></a> <a id="_CPPv2N18wifi_ratesection_t11WIFI_RS_VHTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531daf848d2dc01992814ea9d1839cd82b0d2"></a> enumerator WIFI\_RS\_VHT

    <a id="_CPPv4N18wifi_ratesection_t10WIFI_RS_HEE"></a>

    <a id="_CPPv3N18wifi_ratesection_t10WIFI_RS_HEE"></a> <a id="_CPPv2N18wifi_ratesection_t10WIFI_RS_HEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4f8d473202c3e99fd3ea319e6d43531da9d66c91f5b53cf8b04a5fcd390959f52"></a> enumerator WIFI\_RS\_HE

<a id="_CPPv417wifi_tx_raw_pkt_t"></a>

<a id="_CPPv317wifi_tx_raw_pkt_t"></a> <a id="_CPPv217wifi_tx_raw_pkt_t"></a> <a id="group__bk__api__wifi__v2__enum_1gaba2da6a456633bee003189c8076e40dd"></a> enum wifi\_tx\_raw\_pkt\_t
:   *Values:*

    <a id="_CPPv4N17wifi_tx_raw_pkt_t16WIFI_TX_RAW_DATAE"></a>

    <a id="_CPPv3N17wifi_tx_raw_pkt_t16WIFI_TX_RAW_DATAE"></a> <a id="_CPPv2N17wifi_tx_raw_pkt_t16WIFI_TX_RAW_DATAE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaba2da6a456633bee003189c8076e40dda38e77f10b07e6b822c02d23acf6af7f8"></a> enumerator WIFI\_TX\_RAW\_DATA
    :   Wi-Fi tx raw data

    <a id="_CPPv4N17wifi_tx_raw_pkt_t25WIFI_TX_RAW_SPECIAL_DATTAE"></a>

    <a id="_CPPv3N17wifi_tx_raw_pkt_t25WIFI_TX_RAW_SPECIAL_DATTAE"></a> <a id="_CPPv2N17wifi_tx_raw_pkt_t25WIFI_TX_RAW_SPECIAL_DATTAE"></a> <a id="group__bk__api__wifi__v2__enum_1ggaba2da6a456633bee003189c8076e40dda20a231bdbdd94b8eec47e512d01fbb91"></a> enumerator WIFI\_TX\_RAW\_SPECIAL\_DATTA
    :   Wi-Fi tx raw speacial data

<a id="_CPPv417wifi_capability_t"></a>

<a id="_CPPv317wifi_capability_t"></a> <a id="_CPPv217wifi_capability_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga1bc14fb46de73ab0c10a7aa6f93469b1"></a> enum wifi\_capability\_t
:   WiFi capability interface ID.

    *Values:*

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1ab3e86139f96fa7bf44bfca2e48e99288"></a> enumerator WIFI\_CAPA\_ID\_ERP\_EN
    :   Update Wi-Fi 11g support capability

    <a id="_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a> <a id="_CPPv2N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a509db8830dd020d46467f5f901c61750"></a> enumerator WIFI\_CAPA\_ID\_HT\_EN
    :   Update Wi-Fi 11n support capability

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a20a580b04bf57e6643dd7f6caced3b0e"></a> enumerator WIFI\_CAPA\_ID\_VHT\_EN
    :   Update Wi-Fi 11ac support capability

    <a id="_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a> <a id="_CPPv2N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a539c9e9af6fc31f9a0e6ff59ed692e60"></a> enumerator WIFI\_CAPA\_ID\_HE\_EN
    :   Update Wi-Fi 11ax support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a90c2ebb0b0317f1f0e63ac6682234ac7"></a> enumerator WIFI\_CAPA\_ID\_TX\_AMPDU\_EN
    :   Update Wi-Fi TX AMPDU support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a3700a20c2b98c1057cf037609259a165"></a> enumerator WIFI\_CAPA\_ID\_RX\_AMPDU\_EN
    :   Update Wi-Fi RX AMPDU support capability

    <a id="_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a>

    <a id="_CPPv3N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a> <a id="_CPPv2N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1af49634dbabbc838822f79ac41c2736ed"></a> enumerator WIFI\_CAPA\_ID\_TX\_AMPDU\_NUM
    :   Update Wi-Fi TX AMPDU maximum number

    <a id="_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a>

    <a id="_CPPv3N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a> <a id="_CPPv2N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a94706d23864a16daa9da8fdcab9cb078"></a> enumerator WIFI\_CAPA\_ID\_RX\_AMPDU\_NUM
    :   Update Wi-Fi RX AMPDU maximum number

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a540fa8c0fd197d5fab3e5cda5d459bea"></a> enumerator WIFI\_CAPA\_ID\_VHT\_MCS
    :   Update Wi-Fi VHT MCS

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1aecfd132e3d6befab007b9e494fb023cf"></a> enumerator WIFI\_CAPA\_ID\_HE\_MCS
    :   Update Wi-Fi HE MCS

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a2d33c8884f8ec6ef08917bfecb58590e"></a> enumerator WIFI\_CAPA\_ID\_B40\_EN
    :   Update Wi-Fi 40M bandwidth support capability

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1ac5c351263a116445f5e06cf768049e89"></a> enumerator WIFI\_CAPA\_ID\_STBC\_EN
    :   Update Wi-Fi STBC support capability

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1afdfb433a65abbcabaadbc3bb6c57b6df"></a> enumerator WIFI\_CAPA\_ID\_SGI\_EN
    :   Update Wi-Fi Short GI support capability

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1a9d7b5c52661ed0f3fd96e71d4751a531"></a> enumerator WIFI\_CAPA\_ID\_LDPC\_EN
    :   Update Wi-Fi LDPC support capability

    <a id="_CPPv4N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a> <a id="_CPPv2N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1aa976ce961e99b6667ff5d87ac8be793b"></a> enumerator WIFI\_CAPA\_ID\_BEAMFORMEE\_EN
    :   Update Wi-Fi Beamforming support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1ab905eabd71d5435d08f5e869e8727969"></a> enumerator WIFI\_CAPA\_ID\_11B\_ONLY\_EN
    :   Update Wi-Fi 11b support capability

    <a id="_CPPv4N17wifi_capability_t26WIFI_CAPA_ID_TX_USE_MAX_BWE"></a>

    <a id="_CPPv3N17wifi_capability_t26WIFI_CAPA_ID_TX_USE_MAX_BWE"></a> <a id="_CPPv2N17wifi_capability_t26WIFI_CAPA_ID_TX_USE_MAX_BWE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1ad66a10d80c917182ad6d25c5c3a0012d"></a> enumerator WIFI\_CAPA\_ID\_TX\_USE\_MAX\_BW
    :   Update Wi-Fi TX Use max bandwidth capability

    <a id="_CPPv4N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a>

    <a id="_CPPv3N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a> <a id="_CPPv2N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga1bc14fb46de73ab0c10a7aa6f93469b1aa67a283f3bf515e1bd9f664d47469876"></a> enumerator WIFI\_CAPA\_ID\_MAX

<a id="_CPPv426wifi_legacy_rate_support_t"></a>

<a id="_CPPv326wifi_legacy_rate_support_t"></a> <a id="_CPPv226wifi_legacy_rate_support_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga4dce7ced783b5d63174cae8167d1c22d"></a> enum wifi\_legacy\_rate\_support\_t
:   enum wifi legacy rate support \- Legacy rate support definitions

    *Values:*

    <a id="_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_1MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_1MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_1MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da8b40c42452b919a8c86d1932aa468d8a"></a> enumerator WIFI\_LEGACY\_RATE\_1MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_2MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_2MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_2MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22dabcc8bce282a55feb0744d2a64d1e8d6c"></a> enumerator WIFI\_LEGACY\_RATE\_2MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t24WIFI_LEGACY_RATE_5_5MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t24WIFI_LEGACY_RATE_5_5MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t24WIFI_LEGACY_RATE_5_5MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da4a33e42352b0799f030c65463df696c4"></a> enumerator WIFI\_LEGACY\_RATE\_5\_5MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_11MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_11MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_11MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22dac9dde0e36fcd183a1ce677ce19ea011f"></a> enumerator WIFI\_LEGACY\_RATE\_11MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_6MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_6MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_6MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da484d7c60e0c1ffb4e0b692bbb87da3af"></a> enumerator WIFI\_LEGACY\_RATE\_6MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_9MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_9MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_9MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da4c2bbe6850627f983b92966cd6412012"></a> enumerator WIFI\_LEGACY\_RATE\_9MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_12MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_12MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_12MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22dafd71942f993c8abacd451dcbca9e54be"></a> enumerator WIFI\_LEGACY\_RATE\_12MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_18MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_18MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_18MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22dabb8bfca0b2d31d261d171512215c64c7"></a> enumerator WIFI\_LEGACY\_RATE\_18MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_24MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_24MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_24MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da79b93dfedfe4475a66e1da5182d5fdb0"></a> enumerator WIFI\_LEGACY\_RATE\_24MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_36MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_36MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_36MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da771388c79b2edce60f679d179ec21576"></a> enumerator WIFI\_LEGACY\_RATE\_36MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_48MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_48MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_48MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da279a630df6d6cff8312ffff3ac22bd91"></a> enumerator WIFI\_LEGACY\_RATE\_48MBPS

    <a id="_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_54MBPSE"></a>

    <a id="_CPPv3N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_54MBPSE"></a> <a id="_CPPv2N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_54MBPSE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga4dce7ced783b5d63174cae8167d1c22da86ea55d0a6f71d120f5b9997d5ae88f3"></a> enumerator WIFI\_LEGACY\_RATE\_54MBPS

<a id="_CPPv422wifi_vht_mcs_support_t"></a>

<a id="_CPPv322wifi_vht_mcs_support_t"></a> <a id="_CPPv222wifi_vht_mcs_support_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gadb26f2daae2c9087a555c24eddbecb0a"></a> enum wifi\_vht\_mcs\_support\_t
:   enum wifi\_vht\_mcs\_support\_t \- VHT MCS support definitions @WIFI\_VHT\_MCS\_SUPPORT\_0\_7: MCSes 0-7 are supported for the number of streams @WIFI\_VHT\_MCS\_SUPPORT\_0\_8: MCSes 0-8 are supported @WIFI\_VHT\_MCS\_SUPPORT\_0\_9: MCSes 0-9 are supported @WIFI\_VHT\_MCS\_NOT\_SUPPORTED: This number of streams isn’t supported

    *Values:*

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggadb26f2daae2c9087a555c24eddbecb0aa062b704f0871c4a2d56681c14f804929"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_7

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggadb26f2daae2c9087a555c24eddbecb0aa209c326411d901faed481cff5cd43f6a"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_8

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggadb26f2daae2c9087a555c24eddbecb0aaabebf87c28a705d8cb1de13b2a4976cb"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_9

    <a id="_CPPv4N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggadb26f2daae2c9087a555c24eddbecb0aa112ae860aeec764efa0f0f4ce1545c5c"></a> enumerator WIFI\_VHT\_MCS\_NOT\_SUPPORTED

<a id="_CPPv421wifi_he_mcs_support_t"></a>

<a id="_CPPv321wifi_he_mcs_support_t"></a> <a id="_CPPv221wifi_he_mcs_support_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gae7464a9b074f1be5423f165133c9ad3a"></a> enum wifi\_he\_mcs\_support\_t
:   enum wifi\_he\_mcs\_support\_t \- HE MCS support definitions @WIFI\_HE\_MCS\_SUPPORT\_0\_7: MCSes 0-7 are supported for the number of streams @WIFI\_HE\_MCS\_SUPPORT\_0\_9: MCSes 0-9 are supported @WIFI\_HE\_MCS\_SUPPORT\_0\_11: MCSes 0-11 are supported @WIFI\_HE\_MCS\_NOT\_SUPPORTED: This number of streams isn’t supported

    *Values:*

    <a id="_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggae7464a9b074f1be5423f165133c9ad3aa4e0382b30014b923c2a8837784f5c424"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_7

    <a id="_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggae7464a9b074f1be5423f165133c9ad3aae4ebc49186f71531199b487be61b467b"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_9

    <a id="_CPPv4N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggae7464a9b074f1be5423f165133c9ad3aa2714520af3f93b9d74fd13b37cb043d1"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_11

    <a id="_CPPv4N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a> <a id="_CPPv2N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggae7464a9b074f1be5423f165133c9ad3aa7c2eb8768bd4374f50fb00861ae4d953"></a> enumerator WIFI\_HE\_MCS\_NOT\_SUPPORTED

<a id="_CPPv420wifi_video_quality_t"></a>

<a id="_CPPv320wifi_video_quality_t"></a> <a id="_CPPv220wifi_video_quality_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaccc1dda3078a15f1e1acb8df8b8a4ca5"></a> enum wifi\_video\_quality\_t
:   enum wifi\_video\_quality\_t \- video quality definitions @WIFI\_VIDEO\_QUALITY\_FD: video quality choose Fluent definition(FD) @WIFI\_VIDEO\_QUALITY\_SD: video quality choose Standard definition(SD) @WIFI\_VIDEO\_QUALITY\_HD: video quality choose High definition(HD)

    *Values:*

    <a id="_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_FDE"></a>

    <a id="_CPPv3N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_FDE"></a> <a id="_CPPv2N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_FDE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaccc1dda3078a15f1e1acb8df8b8a4ca5a95fbd41afb553a19d285604033ca540a"></a> enumerator WIFI\_VIDEO\_QUALITY\_FD

    <a id="_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_SDE"></a>

    <a id="_CPPv3N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_SDE"></a> <a id="_CPPv2N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_SDE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaccc1dda3078a15f1e1acb8df8b8a4ca5a7556ce1d9e6acf402fea1b133a2b254b"></a> enumerator WIFI\_VIDEO\_QUALITY\_SD

    <a id="_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_HDE"></a>

    <a id="_CPPv3N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_HDE"></a> <a id="_CPPv2N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_HDE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaccc1dda3078a15f1e1acb8df8b8a4ca5a4d6e17d52b320707ed2054d4ab172eab"></a> enumerator WIFI\_VIDEO\_QUALITY\_HD

<a id="_CPPv413wifi_sta_vsie"></a>

<a id="_CPPv313wifi_sta_vsie"></a> <a id="_CPPv213wifi_sta_vsie"></a> <a id="group__bk__api__wifi__v2__typedef_1gaa1d5b5ba230d1c589aef12cc2f37b74a"></a> enum wifi\_sta\_vsie
:   *Values:*

    <a id="_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a>

    <a id="_CPPv3N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a> <a id="_CPPv2N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aa26a026a55299e3c1d38a55d19ccb4012"></a> enumerator WIFI\_VENDOR\_ELEM\_ASSOC\_REQ

    <a id="_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a>

    <a id="_CPPv3N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a> <a id="_CPPv2N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aa49490b43ee20cbe063ea6684ff56ec92"></a> enumerator WIFI\_VENDOR\_ELEM\_PROBE\_REQ

    <a id="_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a>

    <a id="_CPPv3N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a> <a id="_CPPv2N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aab5c7caa3432bfa14169d5e3d3e87a67a"></a> enumerator NUM\_WIFI\_VENDOR\_ELEM\_FRAMES

<a id="_CPPv416wifi_pkt_dbg_bit"></a>

<a id="_CPPv316wifi_pkt_dbg_bit"></a> <a id="_CPPv216wifi_pkt_dbg_bit"></a> <a id="group__bk__api__wifi__v2__typedef_1ga65ff512611910fcd645e8efab7316bb6"></a> enum wifi\_pkt\_dbg\_bit
:   *Values:*

    <a id="_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_DATA_PKTE"></a>

    <a id="_CPPv3N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_DATA_PKTE"></a> <a id="_CPPv2N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_DATA_PKTE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga65ff512611910fcd645e8efab7316bb6ae53b72fc7c8fce307fb61ef74f305bc5"></a> enumerator WIFI\_TX\_DBG\_LOG\_DATA\_PKT

    <a id="_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_MGMT_PKTE"></a>

    <a id="_CPPv3N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_MGMT_PKTE"></a> <a id="_CPPv2N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_MGMT_PKTE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga65ff512611910fcd645e8efab7316bb6a53d30b9ddc27679a2572b5dab7157b8a"></a> enumerator WIFI\_TX\_DBG\_LOG\_MGMT\_PKT

    <a id="_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_PUSH_PKTE"></a>

    <a id="_CPPv3N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_PUSH_PKTE"></a> <a id="_CPPv2N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_PUSH_PKTE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga65ff512611910fcd645e8efab7316bb6a0f8ecd6dbe5f9a6c6da8963fc379b5a7"></a> enumerator WIFI\_TX\_DBG\_LOG\_PUSH\_PKT

    <a id="_CPPv4N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_DATA_PKTE"></a>

    <a id="_CPPv3N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_DATA_PKTE"></a> <a id="_CPPv2N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_DATA_PKTE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga65ff512611910fcd645e8efab7316bb6ad3bb4a4b56b20dcee42ba29c751f1758"></a> enumerator WIFI\_RX\_DBG\_LOG\_DATA\_PKT

    <a id="_CPPv4N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_MGMT_PKTE"></a>

    <a id="_CPPv3N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_MGMT_PKTE"></a> <a id="_CPPv2N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_MGMT_PKTE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga65ff512611910fcd645e8efab7316bb6a61a4e02404d495fc72798c370d843e81"></a> enumerator WIFI\_RX\_DBG\_LOG\_MGMT\_PKT

<a id="_CPPv48sta_type"></a>

<a id="_CPPv38sta_type"></a> <a id="_CPPv28sta_type"></a> <a id="group__bk__api__wifi__v2__typedef_1gac7141fcda810097a30599e5b9f949197"></a> enum sta\_type
:   *Values:*

    <a id="_CPPv4N8sta_type9STA_TYPE1E"></a>

    <a id="_CPPv3N8sta_type9STA_TYPE1E"></a> <a id="_CPPv2N8sta_type9STA_TYPE1E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggac7141fcda810097a30599e5b9f949197a25eefb955c6774fd37d27c799f84df3e"></a> enumerator STA\_TYPE1

    <a id="_CPPv4N8sta_type9STA_TYPE2E"></a>

    <a id="_CPPv3N8sta_type9STA_TYPE2E"></a> <a id="_CPPv2N8sta_type9STA_TYPE2E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggac7141fcda810097a30599e5b9f949197a87b078c4dbc4077c7cdfb1753b24adf7"></a> enumerator STA\_TYPE2

    <a id="_CPPv4N8sta_type9STA_TYPE3E"></a>

    <a id="_CPPv3N8sta_type9STA_TYPE3E"></a> <a id="_CPPv2N8sta_type9STA_TYPE3E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggac7141fcda810097a30599e5b9f949197ac025e413837f3f2509c9cad6949254c7"></a> enumerator STA\_TYPE3

    <a id="_CPPv4N8sta_type9STA_TYPE4E"></a>

    <a id="_CPPv3N8sta_type9STA_TYPE4E"></a> <a id="_CPPv2N8sta_type9STA_TYPE4E"></a> <a id="group__bk__api__wifi__v2__typedef_1ggac7141fcda810097a30599e5b9f949197a4befbd118160defd3264f8d3c8c72026"></a> enumerator STA\_TYPE4

    <a id="_CPPv4N8sta_type12MAX_STA_TYPEE"></a>

    <a id="_CPPv3N8sta_type12MAX_STA_TYPEE"></a> <a id="_CPPv2N8sta_type12MAX_STA_TYPEE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggac7141fcda810097a30599e5b9f949197a410c3e48fc755dae2a47f6b0cac9e692"></a> enumerator MAX\_STA\_TYPE

<a id="_CPPv4Ut2_20"></a>

<a id="_CPPv3Ut2_20"></a> <a id="group__bk__api__wifi__v2__typedef_1gadb49720dc49f7d4e4cf9adbf2948e409"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt2_2012SCAN_TYPE_CCE"></a>

    <a id="_CPPv3NUt2_2012SCAN_TYPE_CCE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggadb49720dc49f7d4e4cf9adbf2948e409a15a318100b5dcc8f636a3ea429a6b02a"></a> enumerator SCAN\_TYPE\_CC

<a id="_CPPv4Ut2_21"></a>

<a id="_CPPv3Ut2_21"></a> <a id="group__bk__api__wifi__v2__typedef_1gaae05225933a42f81e7c4a9fb286596f9"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt2_2111CSI_RATE_6ME"></a>

    <a id="_CPPv3NUt2_2111CSI_RATE_6ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9a1fa70fc9d62ffb94aee0afad2ff9c9ac"></a> enumerator CSI\_RATE\_6M

    <a id="_CPPv4NUt2_2111CSI_RATE_9ME"></a>

    <a id="_CPPv3NUt2_2111CSI_RATE_9ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9ad79435b67f0fabaded0cd90d7b26463e"></a> enumerator CSI\_RATE\_9M

    <a id="_CPPv4NUt2_2112CSI_RATE_12ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_12ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9ae4dcf985ae94f5df1a5325ced638dc06"></a> enumerator CSI\_RATE\_12M

    <a id="_CPPv4NUt2_2112CSI_RATE_18ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_18ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9a5c25525cccf572f18b62f9ae3ce3eefc"></a> enumerator CSI\_RATE\_18M

    <a id="_CPPv4NUt2_2112CSI_RATE_24ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_24ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9ae0d9672d7c4a8963956faf6f6a410ab9"></a> enumerator CSI\_RATE\_24M

    <a id="_CPPv4NUt2_2112CSI_RATE_36ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_36ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9aa5817c4a01dd61c7cc3ba9203c83a85c"></a> enumerator CSI\_RATE\_36M

    <a id="_CPPv4NUt2_2112CSI_RATE_48ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_48ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9a08a14e5a5fcd7b892e9776004fdafc2d"></a> enumerator CSI\_RATE\_48M

    <a id="_CPPv4NUt2_2112CSI_RATE_54ME"></a>

    <a id="_CPPv3NUt2_2112CSI_RATE_54ME"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaae05225933a42f81e7c4a9fb286596f9a6e40e18c4db6b2073fdb5b8250031ce8"></a> enumerator CSI\_RATE\_54M

<a id="_CPPv4Ut2_22"></a>

<a id="_CPPv3Ut2_22"></a> <a id="group__bk__api__wifi__v2__typedef_1ga39fca1837c5ce7715cbf571669660c13"></a> enum \[anonymous\]
:   BC/MC Filter.

    *Values:*

    <a id="_CPPv4NUt2_2215WIFI_BCMC_CLOSEE"></a>

    <a id="_CPPv3NUt2_2215WIFI_BCMC_CLOSEE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga39fca1837c5ce7715cbf571669660c13ac4d8aa4a655058d6dec1720e7e422af1"></a> enumerator WIFI\_BCMC\_CLOSE

    <a id="_CPPv4NUt2_2210WIFI_MC_ONE"></a>

    <a id="_CPPv3NUt2_2210WIFI_MC_ONE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga39fca1837c5ce7715cbf571669660c13a22623105bf43ab4a45b671a7a3dd2f86"></a> enumerator WIFI\_MC\_ON

    <a id="_CPPv4NUt2_2210WIFI_BC_ONE"></a>

    <a id="_CPPv3NUt2_2210WIFI_BC_ONE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga39fca1837c5ce7715cbf571669660c13a0be6be5152922defb58ee1809a8bb6ea"></a> enumerator WIFI\_BC\_ON

    <a id="_CPPv4NUt2_2213WIFI_BC_MC_ONE"></a>

    <a id="_CPPv3NUt2_2213WIFI_BC_MC_ONE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga39fca1837c5ce7715cbf571669660c13ababf41aca67fe457ce1014f472eb3bd3"></a> enumerator WIFI\_BC\_MC\_ON

<a id="_CPPv413wifi_standard"></a>

<a id="_CPPv313wifi_standard"></a> <a id="_CPPv213wifi_standard"></a> <a id="group__bk__api__wifi__v2__typedef_1ga3dc00bec8f6993cbc09e35742ec7c266"></a> enum wifi\_standard
:   IEEE 802.11 Standards.

    *Values:*

    <a id="_CPPv4N13wifi_standard18WIFI_STANDARD_NONEE"></a>

    <a id="_CPPv3N13wifi_standard18WIFI_STANDARD_NONEE"></a> <a id="_CPPv2N13wifi_standard18WIFI_STANDARD_NONEE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a2bbed9de7eb1f9a7a009f7181bd4fa49"></a> enumerator WIFI\_STANDARD\_NONE

    <a id="_CPPv4N13wifi_standard17WIFI_STANDARD_11AE"></a>

    <a id="_CPPv3N13wifi_standard17WIFI_STANDARD_11AE"></a> <a id="_CPPv2N13wifi_standard17WIFI_STANDARD_11AE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266abf1ce4e3f6248bd1456706e1bd893956"></a> enumerator WIFI\_STANDARD\_11A

    <a id="_CPPv4N13wifi_standard17WIFI_STANDARD_11BE"></a>

    <a id="_CPPv3N13wifi_standard17WIFI_STANDARD_11BE"></a> <a id="_CPPv2N13wifi_standard17WIFI_STANDARD_11BE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a751c2b61a411525c732b7572a16c3a4f"></a> enumerator WIFI\_STANDARD\_11B

    <a id="_CPPv4N13wifi_standard17WIFI_STANDARD_11GE"></a>

    <a id="_CPPv3N13wifi_standard17WIFI_STANDARD_11GE"></a> <a id="_CPPv2N13wifi_standard17WIFI_STANDARD_11GE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a2c1da2e83752f9e1d6cc2cff995781a4"></a> enumerator WIFI\_STANDARD\_11G

    <a id="_CPPv4N13wifi_standard17WIFI_STANDARD_11NE"></a>

    <a id="_CPPv3N13wifi_standard17WIFI_STANDARD_11NE"></a> <a id="_CPPv2N13wifi_standard17WIFI_STANDARD_11NE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266ac831a54d496253ded3ca6aec88883551"></a> enumerator WIFI\_STANDARD\_11N

    <a id="_CPPv4N13wifi_standard18WIFI_STANDARD_11ACE"></a>

    <a id="_CPPv3N13wifi_standard18WIFI_STANDARD_11ACE"></a> <a id="_CPPv2N13wifi_standard18WIFI_STANDARD_11ACE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a462cfe2b1157b814a281a31405b6d82e"></a> enumerator WIFI\_STANDARD\_11AC

    <a id="_CPPv4N13wifi_standard18WIFI_STANDARD_11AXE"></a>

    <a id="_CPPv3N13wifi_standard18WIFI_STANDARD_11AXE"></a> <a id="_CPPv2N13wifi_standard18WIFI_STANDARD_11AXE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266ad1afd541d645bc898024720f1fdcd17a"></a> enumerator WIFI\_STANDARD\_11AX

    <a id="_CPPv4N13wifi_standard24WIFI_STANDARD_NONE_POLARE"></a>

    <a id="_CPPv3N13wifi_standard24WIFI_STANDARD_NONE_POLARE"></a> <a id="_CPPv2N13wifi_standard24WIFI_STANDARD_NONE_POLARE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a47e31102919333f585c9ab33b92e1cc2"></a> enumerator WIFI\_STANDARD\_NONE\_POLAR

    <a id="_CPPv4N13wifi_standard17WIFI_STANDARD_MAXE"></a>

    <a id="_CPPv3N13wifi_standard17WIFI_STANDARD_MAXE"></a> <a id="_CPPv2N13wifi_standard17WIFI_STANDARD_MAXE"></a> <a id="group__bk__api__wifi__v2__typedef_1gga3dc00bec8f6993cbc09e35742ec7c266a82f02bc94488309e7a4fa588662d2b63"></a> enumerator WIFI\_STANDARD\_MAX
