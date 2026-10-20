---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/api-reference/wifi/bk_wifi.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
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

Module Specific WiFi APIs:
:   - `bk_wifi_scan_register_cb()` \- register scan callback function
    - [`bk_wifi_scan_start()`](#_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t "bk_wifi_scan_start") \- start the scan
    - [`bk_wifi_scan_stop()`](#_CPPv417bk_wifi_scan_stopv "bk_wifi_scan_stop") \- stop the scan
    - [`bk_wifi_scan_get_result()`](#_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t "bk_wifi_scan_get_result") \- get the scan result
    - [`bk_wifi_scan_dump_result()`](#_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t "bk_wifi_scan_dump_result") \- dump the scan result
    - [`bk_wifi_scan_free_result()`](#_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t "bk_wifi_scan_free_result") \- dump the scan result
    - [`bk_wifi_filter_set_config()`](#_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t "bk_wifi_filter_set_config") \- set filter configuration
    - [`bk_wifi_filter_register_cb()`](#_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t "bk_wifi_filter_register_cb") \- register the filter callback function

<a id="compitability-and-extension"></a>

## Compitability and Extension

The WiFi APIs are flexible, easy to be extended and backward compatible. For most of the WiFi configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.

<a id="programing-principle"></a>

## Programing Principle

重要

Here is some general principle for WiFi API users:
:   - Always init the reserved fields of config stuct to 0
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

- [wifi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_wifi_initPK18wifi_init_config_t"></a>

<a id="_CPPv312bk_wifi_initPK18wifi_init_config_t"></a> <a id="_CPPv212bk_wifi_initPK18wifi_init_config_t"></a> <a id="bk_wifi_init__wifi_init_config_tCP"></a> <a id="group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_init(const [wifi\_init\_config\_t](#_CPPv418wifi_init_config_t "wifi_init_config_t") \*init\_config)
:   This API initializes the WiFi driver, e.g. creating task for supplicant, allocating resource for low level WiFi driver etc.

    Usage example:

    ```
     wifi_init_config_t init_config = WIFI_DEFAULT_INIT_CONFIG;
     BK_LOG_ON_ERR(bk_wifi_init(&init_config);
    ```

    **Attention**
    :   1\. This API is the 1st API that should be called before any other WiFi API can be called.

        2\. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

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

        2\. This API connect the BK STA to the configured AP automatically.

        3\. If the BK STA is already started, this API ignores the request and returns BK\_OK. if you want to restart the BK STA, call [bk\_wifi\_sta\_stop()](#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b) first and then call this API.

        4\. TODO description about fast connection

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_STA\_NOT\_CONFIG: the BK STA is not configured.
        - BK\_ERR\_WIFI\_MONITOR\_IP: the BK STA can’t be started because monitor is started.
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
    os_strncpy(sta_config.password, "password");
    //more initialization here
    BK_LOG_ON_ERR(bk_wifi_sta_set_config(&sta_config));
    ```

    **Attention**
    :   1\. Don’t call this API when the monitor is in-progress

        2\. If STA is already connected to AP, this API cases BK STA reconnects the AP.

        3\. Make sure the reserved fields in sta\_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

        4\. Auto reconnect max count and timeout can be set. When user app receives EVENT\_WIFI\_STA\_DISCONNECTED event, it’s user app’s responsibility to reconnect to AP manually. Max count and timeout set to zero to let supplicant automatically handles connection without user app’s interaction.

    参数
    :   **sta\_config** – the STA configuration

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_STA\_NOT\_STARTED: the STA is not started, call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) first.
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
        - The AID is only valid if -\>state is WIFI\_LINK\_CONNECTED.

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

        2\. Don’t call this API when the monitor is in-progress

        3\. If STA is already connected to AP, this API reconnects the BK STA.

        4\. TODO \- multiple same SSID connect???

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

        2\. Pass NULL scan\_config to scan all APs, otherwise scan the SSID specified in scan\_config.ssid

        3\. Make sure the reserved fields in scan\_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

        4\. TODO scan result limits???

    参数
    :   **scan\_config** – the configuration of scan

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_STA\_NOT\_STARTED: the STA is not started, call [bk\_wifi\_sta\_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf) first.
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

        2\. Don’t forget to call bk\_wifi\_scan\_free\_result(\&scan\_result) to free the the resource allocated in this API, otherwise memory leak.

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

        2\. If [bk\_wifi\_ap\_set\_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39) is not called, this API start the AP with default value, normally you should configure the AP first before calling this API.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_WIFI\_AP\_NOT\_CONFIGURED: the WiFi AP is not configured, call [bk\_wifi\_ap\_set\_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39) first.
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

        2\. When monitor mode is enabled, the STA connect will not work and [bk\_wifi\_sta\_connect()](#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06) returns BK\_ERR\_WIFI\_MONITOR\_IP.

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

        2\. This API is only used for settting monitor channel, NOT for other purpose.

        3\. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.

        4\. The channel range can be set is from channel 1 to channel 14,

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

        2\. If STA is enabled, the WiFi driver only receives beacon from the connected AP, if scan is enabled or filter\_config-\>rx\_all\_beacon is set, the WiFi driver receives beacons of all APs.

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

        2\. During WiFi scan, the filter also works.

        3\. Pass NULL callback or set all fields of filter\_config to 0 to disable the filter.

        4\. The memory used to hold the frame buffer and frame\_info will be freed immediately when the callback is returned, so don’t relay them to other task. Make a copy of them and then relay to other task if necessary.

        5\. Don’t do too much work in the filter callback because it’s called in WiFi driver core thread, otherwise it may impact the WiFi performance.

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

        2\. If you want to change the MAC of AP, call bk\_set\_mac() to set the base MAC of the system.

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

        2\. If you want to change the MAC of AP, call bk\_set\_mac() to set the base MAC of the system.

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

        2\. Only support to send non-QoS frame.

        3\. The frame sequence will be overwritten by WiFi driver.

        4\. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

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

        2\. Only support to send non-QoS frame.

        3\. The frame sequence will be overwritten by WiFi driver.

        4\. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw\_tx** – : raw tx information, refer to struct [wifi\_raw\_tx\_info\_t](#structwifi__raw__tx__info__t)
        - **cb** – : send status call back
        - **param** – : send status call back paramter

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv429bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a>

<a id="_CPPv329bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a> <a id="_CPPv229bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t"></a> <a id="bk_wifi_set_tx_raw_rate_power__uint32_t.uint32_t"></a> <a id="group__bk__api__wifi__v2_1ga2650d71604e350578fc8c18fb5ea3d00"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_rate\_power(uint32\_t rate, uint32\_t power)
:   Update raw 802.11 frame TX rate and power.

    参数
    :   - **rate** – : TX rate control
        - **power** – : TX power control

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv421bk_wifi_set_tx_raw_ac7uint8_t"></a>

<a id="_CPPv321bk_wifi_set_tx_raw_ac7uint8_t"></a> <a id="_CPPv221bk_wifi_set_tx_raw_ac7uint8_t"></a> <a id="bk_wifi_set_tx_raw_ac__uint8_t"></a> <a id="group__bk__api__wifi__v2_1ga51eb1e9e836d29a1a6726d69037d1faa"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_ac(uint8\_t ac)
:   Update raw 802.11 frame TX AC.

    参数
    :   **rate** – : TX AC

    返回
    :   - kNoErr: succeed
        - otherwise: fail

<a id="_CPPv426bk_wifi_set_tx_raw_timeout8uint16_t"></a>

<a id="_CPPv326bk_wifi_set_tx_raw_timeout8uint16_t"></a> <a id="_CPPv226bk_wifi_set_tx_raw_timeout8uint16_t"></a> <a id="bk_wifi_set_tx_raw_timeout__uint16_t"></a> <a id="group__bk__api__wifi__v2_1gac9081dbb8aa6a9d63abaedfd70149b03"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_raw\_timeout(uint16\_t timeout\_ms)
:   Update raw 802.11 frame TX timeout.

    参数
    :   **rate** – : TX timeout

    返回
    :   - kNoErr: succeed
        - otherwise: fail

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

<a id="_CPPv423bk_wifi_set_min_rsv_mem8uint32_t"></a>

<a id="_CPPv323bk_wifi_set_min_rsv_mem8uint32_t"></a> <a id="_CPPv223bk_wifi_set_min_rsv_mem8uint32_t"></a> <a id="bk_wifi_set_min_rsv_mem__uint32_t"></a> <a id="group__bk__api__wifi__v2_1gaf2dde20ee4d9d86af217bbc0131a32c0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_min\_rsv\_mem(uint32\_t mem\_bytes)
:   Update the minimux heap memory size that Wi-Fi should reserve.

    **Attention**
    :   1\. An small piece of extra memory will be malloced from heap for each TX packets delivered to Wi-Fi, so if the pending TX packets are too many for some reasons, the heap memory will be occupied too much by TX packets. To ensure the stability of whole system, this interface is provied to limit the memory size for Wi-Fi TX packets.

        2\. The default minimux reserved memory size is 10K bytes

    参数
    :   **mem\_bytes, :** – the expected reserved memory size(bytes)

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv423bk_wifi_get_min_rsv_memP8uint32_t"></a>

<a id="_CPPv323bk_wifi_get_min_rsv_memP8uint32_t"></a> <a id="_CPPv223bk_wifi_get_min_rsv_memP8uint32_t"></a> <a id="bk_wifi_get_min_rsv_mem__uint32_tP"></a> <a id="group__bk__api__wifi__v2_1ga56a0a4e2cfe621845af0c213e6408ecf"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_min\_rsv\_mem(uint32\_t \*mem\_bytes)
:   Get the minimux heap memory size that Wi-Fi currently creserves.

    参数
    :   **mem\_bytes, :** – return currently reserved memory size(bytes)

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a>

<a id="_CPPv327bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a> <a id="_CPPv227bk_wifi_set_tx_max_msdu_cnt8uint16_t"></a> <a id="bk_wifi_set_tx_max_msdu_cnt__uint16_t"></a> <a id="group__bk__api__wifi__v2_1ga1f4d92b573cb998c9b7844d5088097a4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_tx\_max\_msdu\_cnt(uint16\_t max\_cnt)
:   Update the maximum MSDU count that Wi-Fi could handle.

    参数
    :   **max\_cnt, :** – the maxmimum MSDU count

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv427bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a>

<a id="_CPPv327bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a> <a id="_CPPv227bk_wifi_get_tx_max_msdu_cntP8uint16_t"></a> <a id="bk_wifi_get_tx_max_msdu_cnt__uint16_tP"></a> <a id="group__bk__api__wifi__v2_1gae2d2f50c4bb2a7976a2f259450e44d2e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_get\_tx\_max\_msdu\_cnt(uint16\_t \*max\_cnt)
:   Get the maximum MSDU count configuration that Wi-Fi could handle.

    参数
    :   **max\_cnt, :** – return the maxmimum MSDU count

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv419bk_wifi_capa_config17wifi_capability_t8uint32_t"></a>

<a id="_CPPv319bk_wifi_capa_config17wifi_capability_t8uint32_t"></a> <a id="_CPPv219bk_wifi_capa_config17wifi_capability_t8uint32_t"></a> <a id="bk_wifi_capa_config__wifi_capability_t.uint32_t"></a> <a id="group__bk__api__wifi__v2_1gac844dc0c4b7acd23f5ec8f5f1cc6fa90"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_capa\_config([wifi\_capability\_t](#_CPPv417wifi_capability_t "wifi_capability_t") capa\_id, uint32\_t capa\_val)
:   Update Wi-Fi capability configuration.

    This API is used to change some Wi-Fi capability configuration, please refer to wifi\_capability\_t to get the capability that has been supported.

    **Attention**
    :   1\. Please keep in mind that Wi-Fi behavior may change if the capability is changed to different value compared with the default value.

        2\. We strongly suggest not using this API except you are very farmiliar with the Wi-Fi specification.

        3\. If you want Wi-Fi working on 11b only mode, please set 11b only mode by configurate paramter capa\_id with WIFI\_CAPA\_ID\_11B\_ONLY\_EN and capa\_val with true BEFORE connecting AP or opening SoftAP.

    参数
    :   - **capa\_id, :** – the specific capability you want to change
        - **capa\_val, :** – new capability value

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv419bk_wifi_set_countryPK14wifi_country_t"></a>

<a id="_CPPv319bk_wifi_set_countryPK14wifi_country_t"></a> <a id="_CPPv219bk_wifi_set_countryPK14wifi_country_t"></a> <a id="bk_wifi_set_country__wifi_country_tCP"></a> <a id="group__bk__api__wifi__v2_1gaa73a4fdaf2ca78ccd0d24c02d94e826f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_set\_country(const [wifi\_country\_t](#_CPPv414wifi_country_t "wifi_country_t") \*country)
:   configure country info

    **Attention**
    :   1\. The default country is {.cc\=”CN”, .schan\=1, .nchan\=13, policy\=WIFI\_COUNTRY\_POLICY\_AUTO}

        2\. When the country policy is WIFI\_COUNTRY\_POLICY\_AUTO, the country info of the AP to which the station is connected is used. E.g. if the configured country info is {.cc\=”USA”, .schan\=1, .nchan\=11} and the country info of the AP to which the station is connected is {.cc\=”JP”, .schan\=1, .nchan\=14} then the country info that will be used is {.cc\=”JP”, .schan\=1, .nchan\=14}. If the station disconnected from the AP the country info is set back back to the country info of the station automatically, {.cc\=”USA”, .schan\=1, .nchan\=11} in the example.

        3\. When the country policy is WIFI\_COUNTRY\_POLICY\_MANUAL, always use the configured country info.

        4\. When the country info is changed because of configuration or because the station connects to a different external AP, the country IE in probe response/beacon of the soft-AP is changed also.

        5\. The country configuration is not stored into flash

        6\. This API doesn’t validate the per-country rules, it’s up to the user to fill in all fields according to local regulations.

    参数
    :   **country** – the configured country info

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

    example: mac c8478cxxyyzz txevm -e 2 //if needed

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

<a id="_CPPv432bk_wifi_send_listen_interval_req7uint8_t"></a>

<a id="_CPPv332bk_wifi_send_listen_interval_req7uint8_t"></a> <a id="_CPPv232bk_wifi_send_listen_interval_req7uint8_t"></a> <a id="bk_wifi_send_listen_interval_req__uint8_t"></a> <a id="group__bk__api__wifi__v2_1gab85e92fdd41b151d1e99e3cd784e380f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_wifi\_send\_listen\_interval\_req(uint8\_t interval)
:   Set listen interval.

    参数
    :   **any** – value is acceptable,but 1, 3, 10 is recommended.

    返回
    :   -BK\_OK: on success -others:real error, used for future.

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

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [wifi\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv418wifi_init_config_t"></a>

<a id="_CPPv318wifi_init_config_t"></a> <a id="_CPPv218wifi_init_config_t"></a> <a id="wifi_init_config_t"></a> <a id="structwifi__init__config__t"></a> struct wifi\_init\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_init_config_t8featuresE"></a>

    <a id="_CPPv3N18wifi_init_config_t8featuresE"></a> <a id="_CPPv2N18wifi_init_config_t8featuresE"></a> <a id="wifi_init_config_t::features__uint64_t"></a> <a id="structwifi__init__config__t_1ae9f99f3b03f67d5c39a0e20f901bd08b"></a> uint64\_t features
    :   WiFi feature bitmaps

    <a id="_CPPv4N18wifi_init_config_t8reservedE"></a>

    <a id="_CPPv3N18wifi_init_config_t8reservedE"></a> <a id="_CPPv2N18wifi_init_config_t8reservedE"></a> <a id="wifi_init_config_t::reserved__uint8_tA"></a> <a id="structwifi__init__config__t_1a85267c94d0e747b3d001848dadda318b"></a> uint8\_t reserved\[16\]
    :   Reserved

<a id="_CPPv414wifi_channel_t"></a>

<a id="_CPPv314wifi_channel_t"></a> <a id="_CPPv214wifi_channel_t"></a> <a id="wifi_channel_t"></a> <a id="structwifi__channel__t"></a> struct wifi\_channel\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14wifi_channel_t7primaryE"></a>

    <a id="_CPPv3N14wifi_channel_t7primaryE"></a> <a id="_CPPv2N14wifi_channel_t7primaryE"></a> <a id="wifi_channel_t::primary__uint8_t"></a> <a id="structwifi__channel__t_1a2753b11986e9c2876a93c8c4d8261b77"></a> uint8\_t primary
    :   Primary channel

    <a id="_CPPv4N14wifi_channel_t6secondE"></a>

    <a id="_CPPv3N14wifi_channel_t6secondE"></a> <a id="_CPPv2N14wifi_channel_t6secondE"></a> <a id="wifi_channel_t::second__wifi_second_channel_t"></a> <a id="structwifi__channel__t_1addd0b1028bfc9310ee2152a40c4df386"></a> [wifi\_second\_channel\_t](#_CPPv421wifi_second_channel_t "wifi_second_channel_t") second
    :   Secondary cahnnel

<a id="_CPPv47bk_vise"></a>

<a id="_CPPv37bk_vise"></a> <a id="_CPPv27bk_vise"></a> <a id="bk_vise"></a> <a id="structbk__vise"></a> struct bk\_vise

<a id="_CPPv417wifi_sta_config_t"></a>

<a id="_CPPv317wifi_sta_config_t"></a> <a id="_CPPv217wifi_sta_config_t"></a> <a id="wifi_sta_config_t"></a> <a id="structwifi__sta__config__t"></a> struct wifi\_sta\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_sta_config_t4ssidE"></a>

    <a id="_CPPv3N17wifi_sta_config_t4ssidE"></a> <a id="_CPPv2N17wifi_sta_config_t4ssidE"></a> <a id="wifi_sta_config_t::ssid__cA"></a> <a id="structwifi__sta__config__t_1a173955fd4b6debbf470dcee831f82fe5"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP to be connected

    <a id="_CPPv4N17wifi_sta_config_t5bssidE"></a>

    <a id="_CPPv3N17wifi_sta_config_t5bssidE"></a> <a id="_CPPv2N17wifi_sta_config_t5bssidE"></a> <a id="wifi_sta_config_t::bssid__uint8_tA"></a> <a id="structwifi__sta__config__t_1af4c854d9f2fe90367777324fea95fc63"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP to be connected, fast connect only

    <a id="_CPPv4N17wifi_sta_config_t7channelE"></a>

    <a id="_CPPv3N17wifi_sta_config_t7channelE"></a> <a id="_CPPv2N17wifi_sta_config_t7channelE"></a> <a id="wifi_sta_config_t::channel__uint8_t"></a> <a id="structwifi__sta__config__t_1a2cc86d1fa7e6aeebdfbc73068c19cbf7"></a> uint8\_t channel
    :   Primary channel of AP to be connected, fast connect only

    <a id="_CPPv4N17wifi_sta_config_t8securityE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8securityE"></a> <a id="_CPPv2N17wifi_sta_config_t8securityE"></a> <a id="wifi_sta_config_t::security__wifi_security_t"></a> <a id="structwifi__sta__config__t_1ac23fbfa8a5f39e98bf8d42b9817a0b50"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security of AP to be connected

    <a id="_CPPv4N17wifi_sta_config_t8passwordE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8passwordE"></a> <a id="_CPPv2N17wifi_sta_config_t8passwordE"></a> <a id="wifi_sta_config_t::password__cA"></a> <a id="structwifi__sta__config__t_1a6a0700a6d3655cb0eb38453cadf15660"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Security key or PMK of the wlan.

    <a id="_CPPv4N17wifi_sta_config_t5vsiesE"></a>

    <a id="_CPPv3N17wifi_sta_config_t5vsiesE"></a> <a id="_CPPv2N17wifi_sta_config_t5vsiesE"></a> <a id="wifi_sta_config_t::vsies__bk_visePA"></a> <a id="structwifi__sta__config__t_1a0cb7930e45f9ba19cce91a3f0b1b5470"></a> struct [bk\_vise](#_CPPv47bk_vise "bk_vise") \*vsies\[[NUM\_WIFI\_VENDOR\_ELEM\_FRAMES](#_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE "NUM_WIFI_VENDOR_ELEM_FRAMES")\]
    :   Vnedor Specific IEs

    <a id="_CPPv4N17wifi_sta_config_t8reservedE"></a>

    <a id="_CPPv3N17wifi_sta_config_t8reservedE"></a> <a id="_CPPv2N17wifi_sta_config_t8reservedE"></a> <a id="wifi_sta_config_t::reserved__uint8_tA"></a> <a id="structwifi__sta__config__t_1a2d40ae19dd768487ecdf0fa5b09c2f7c"></a> uint8\_t reserved\[32\]
    :   reserved, **must set to 0**

    <a id="_CPPv4N17wifi_sta_config_t20auto_reconnect_countE"></a>

    <a id="_CPPv3N17wifi_sta_config_t20auto_reconnect_countE"></a> <a id="_CPPv2N17wifi_sta_config_t20auto_reconnect_countE"></a> <a id="wifi_sta_config_t::auto_reconnect_count__i"></a> <a id="structwifi__sta__config__t_1a7a9d2fe502ba1e58ca5d7595dbc2a502"></a> int auto\_reconnect\_count
    :   auto reconnect max count, 0 for always reconnect

    <a id="_CPPv4N17wifi_sta_config_t22auto_reconnect_timeoutE"></a>

    <a id="_CPPv3N17wifi_sta_config_t22auto_reconnect_timeoutE"></a> <a id="_CPPv2N17wifi_sta_config_t22auto_reconnect_timeoutE"></a> <a id="wifi_sta_config_t::auto_reconnect_timeout__i"></a> <a id="structwifi__sta__config__t_1ae5f74786c5667ad5f0bb1ad862688e49"></a> int auto\_reconnect\_timeout
    :   auto reconnect timeout in secs, 0 for no timeout

    <a id="_CPPv4N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a>

    <a id="_CPPv3N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a> <a id="_CPPv2N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE"></a> <a id="wifi_sta_config_t::disable_auto_reconnect_after_disconnect__b"></a> <a id="structwifi__sta__config__t_1acd8a95fa035752187cbcfc388d0df9f6"></a> bool disable\_auto\_reconnect\_after\_disconnect
    :   disable auto reconnect if deauth/disassoc by AP when in connected state

<a id="_CPPv423wifi_linkstate_reason_t"></a>

<a id="_CPPv323wifi_linkstate_reason_t"></a> <a id="_CPPv223wifi_linkstate_reason_t"></a> <a id="wifi_linkstate_reason_t"></a> <a id="structwifi__linkstate__reason__t"></a> struct wifi\_linkstate\_reason\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23wifi_linkstate_reason_t5stateE"></a>

    <a id="_CPPv3N23wifi_linkstate_reason_t5stateE"></a> <a id="_CPPv2N23wifi_linkstate_reason_t5stateE"></a> <a id="wifi_linkstate_reason_t::state__wifi_link_state_t"></a> <a id="structwifi__linkstate__reason__t_1a29e61eb4dd05859b9598bf6d36edca39"></a> [wifi\_link\_state\_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state
    :   Wifi linkstate

    <a id="_CPPv4N23wifi_linkstate_reason_t11reason_codeE"></a>

    <a id="_CPPv3N23wifi_linkstate_reason_t11reason_codeE"></a> <a id="_CPPv2N23wifi_linkstate_reason_t11reason_codeE"></a> <a id="wifi_linkstate_reason_t::reason_code__wifi_err_reason_t"></a> <a id="structwifi__linkstate__reason__t_1a626b24ac39702a34da66ab39b941a62c"></a> [wifi\_err\_reason\_t](#_CPPv417wifi_err_reason_t "wifi_err_reason_t") reason\_code
    :   Wifi disconnect reason code, success will be WIFI\_REASON\_MAX

<a id="_CPPv418wifi_link_status_t"></a>

<a id="_CPPv318wifi_link_status_t"></a> <a id="_CPPv218wifi_link_status_t"></a> <a id="wifi_link_status_t"></a> <a id="structwifi__link__status__t"></a> struct wifi\_link\_status\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_link_status_t5stateE"></a>

    <a id="_CPPv3N18wifi_link_status_t5stateE"></a> <a id="_CPPv2N18wifi_link_status_t5stateE"></a> <a id="wifi_link_status_t::state__wifi_link_state_t"></a> <a id="structwifi__link__status__t_1ae2217f198571149fd1ea194e2987fa9a"></a> [wifi\_link\_state\_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state
    :   The WiFi connection status

    <a id="_CPPv4N18wifi_link_status_t3aidE"></a>

    <a id="_CPPv3N18wifi_link_status_t3aidE"></a> <a id="_CPPv2N18wifi_link_status_t3aidE"></a> <a id="wifi_link_status_t::aid__i"></a> <a id="structwifi__link__status__t_1af7f1f46b82ff710670cab9ff4fb6d89b"></a> int aid
    :   STA AID

    <a id="_CPPv4N18wifi_link_status_t4rssiE"></a>

    <a id="_CPPv3N18wifi_link_status_t4rssiE"></a> <a id="_CPPv2N18wifi_link_status_t4rssiE"></a> <a id="wifi_link_status_t::rssi__i"></a> <a id="structwifi__link__status__t_1a726485b304bcbeacf81e8c199e4d9650"></a> int rssi
    :   The RSSI of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t4ssidE"></a>

    <a id="_CPPv3N18wifi_link_status_t4ssidE"></a> <a id="_CPPv2N18wifi_link_status_t4ssidE"></a> <a id="wifi_link_status_t::ssid__cA"></a> <a id="structwifi__link__status__t_1a931982c6fb3f4b31f23bcb0f301fff23"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t5bssidE"></a>

    <a id="_CPPv3N18wifi_link_status_t5bssidE"></a> <a id="_CPPv2N18wifi_link_status_t5bssidE"></a> <a id="wifi_link_status_t::bssid__uint8_tA"></a> <a id="structwifi__link__status__t_1a931ec371d60d095e55035f9601a032aa"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t7channelE"></a>

    <a id="_CPPv3N18wifi_link_status_t7channelE"></a> <a id="_CPPv2N18wifi_link_status_t7channelE"></a> <a id="wifi_link_status_t::channel__uint8_t"></a> <a id="structwifi__link__status__t_1a2e6648f0d5426138954d395d3c181c83"></a> uint8\_t channel
    :   Primary channel of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t8securityE"></a>

    <a id="_CPPv3N18wifi_link_status_t8securityE"></a> <a id="_CPPv2N18wifi_link_status_t8securityE"></a> <a id="wifi_link_status_t::security__wifi_security_t"></a> <a id="structwifi__link__status__t_1a1932604f49a07b22ba838dd0dd1da52c"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security of AP the BK STA is connected

    <a id="_CPPv4N18wifi_link_status_t8passwordE"></a>

    <a id="_CPPv3N18wifi_link_status_t8passwordE"></a> <a id="_CPPv2N18wifi_link_status_t8passwordE"></a> <a id="wifi_link_status_t::password__cA"></a> <a id="structwifi__link__status__t_1a412b62929f6c157e3ae980111bd41317"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Passord of AP the BK STA is connected

<a id="_CPPv418wifi_scan_config_t"></a>

<a id="_CPPv318wifi_scan_config_t"></a> <a id="_CPPv218wifi_scan_config_t"></a> <a id="wifi_scan_config_t"></a> <a id="structwifi__scan__config__t"></a> struct wifi\_scan\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_scan_config_t4ssidE"></a>

    <a id="_CPPv3N18wifi_scan_config_t4ssidE"></a> <a id="_CPPv2N18wifi_scan_config_t4ssidE"></a> <a id="wifi_scan_config_t::ssid__cA"></a> <a id="structwifi__scan__config__t_1ace0f6592172fb7045603763e5691ac8a"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID to be scaned

    <a id="_CPPv4N18wifi_scan_config_t8reservedE"></a>

    <a id="_CPPv3N18wifi_scan_config_t8reservedE"></a> <a id="_CPPv2N18wifi_scan_config_t8reservedE"></a> <a id="wifi_scan_config_t::reserved__uint8_tA"></a> <a id="structwifi__scan__config__t_1ae55dce718837e147e3301dfcf2ab730d"></a> uint8\_t reserved\[16\]
    :   Reserved fields, **must be zero**

<a id="_CPPv419wifi_scan_ap_info_t"></a>

<a id="_CPPv319wifi_scan_ap_info_t"></a> <a id="_CPPv219wifi_scan_ap_info_t"></a> <a id="wifi_scan_ap_info_t"></a> <a id="structwifi__scan__ap__info__t"></a> struct wifi\_scan\_ap\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19wifi_scan_ap_info_t4ssidE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t4ssidE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t4ssidE"></a> <a id="wifi_scan_ap_info_t::ssid__cA"></a> <a id="structwifi__scan__ap__info__t_1aa4c204effe106eddb1aeb5ef9c8b25d2"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t5bssidE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t5bssidE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t5bssidE"></a> <a id="wifi_scan_ap_info_t::bssid__uint8_tA"></a> <a id="structwifi__scan__ap__info__t_1ae3869d94dd1302a1c6f190f5f7f8995a"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t4rssiE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t4rssiE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t4rssiE"></a> <a id="wifi_scan_ap_info_t::rssi__i"></a> <a id="structwifi__scan__ap__info__t_1a355b6900c5c6e658a5fdcb17d96f67ad"></a> int rssi
    :   RSSI of AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t7channelE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t7channelE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t7channelE"></a> <a id="wifi_scan_ap_info_t::channel__uint8_t"></a> <a id="structwifi__scan__ap__info__t_1ae4819d917122c72c505dc3240199d28e"></a> uint8\_t channel
    :   The channel of the AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t8securityE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t8securityE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t8securityE"></a> <a id="wifi_scan_ap_info_t::security__wifi_security_t"></a> <a id="structwifi__scan__ap__info__t_1ad11455feb4df0ac53c237f659d8b9e4d"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   The security type of the AP found by scan

    <a id="_CPPv4N19wifi_scan_ap_info_t8reservedE"></a>

    <a id="_CPPv3N19wifi_scan_ap_info_t8reservedE"></a> <a id="_CPPv2N19wifi_scan_ap_info_t8reservedE"></a> <a id="wifi_scan_ap_info_t::reserved__uint8_tA"></a> <a id="structwifi__scan__ap__info__t_1a03022794ede1f6e1b2b472fd4f7d8c9e"></a> uint8\_t reserved\[16\]
    :   Reserved, **must be zero**

<a id="_CPPv418wifi_scan_result_t"></a>

<a id="_CPPv318wifi_scan_result_t"></a> <a id="_CPPv218wifi_scan_result_t"></a> <a id="wifi_scan_result_t"></a> <a id="structwifi__scan__result__t"></a> struct wifi\_scan\_result\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_scan_result_t6ap_numE"></a>

    <a id="_CPPv3N18wifi_scan_result_t6ap_numE"></a> <a id="_CPPv2N18wifi_scan_result_t6ap_numE"></a> <a id="wifi_scan_result_t::ap_num__i"></a> <a id="structwifi__scan__result__t_1ababf0f253ac248d67f7dd25db0452287"></a> int ap\_num
    :   The number of AP found by scan

    <a id="_CPPv4N18wifi_scan_result_t3apsE"></a>

    <a id="_CPPv3N18wifi_scan_result_t3apsE"></a> <a id="_CPPv2N18wifi_scan_result_t3apsE"></a> <a id="wifi_scan_result_t::aps__wifi_scan_ap_info_tP"></a> <a id="structwifi__scan__result__t_1afc7ec251f26525956b4d710092012c04"></a> [wifi\_scan\_ap\_info\_t](#_CPPv419wifi_scan_ap_info_t "wifi_scan_ap_info_t") \*aps
    :   The APs found by scan

<a id="_CPPv416wifi_ap_config_t"></a>

<a id="_CPPv316wifi_ap_config_t"></a> <a id="_CPPv216wifi_ap_config_t"></a> <a id="wifi_ap_config_t"></a> <a id="structwifi__ap__config__t"></a> struct wifi\_ap\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16wifi_ap_config_t4ssidE"></a>

    <a id="_CPPv3N16wifi_ap_config_t4ssidE"></a> <a id="_CPPv2N16wifi_ap_config_t4ssidE"></a> <a id="wifi_ap_config_t::ssid__cA"></a> <a id="structwifi__ap__config__t_1aa931247a4b99b7bd4f9e364c697533f3"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   The SSID of BK AP

    <a id="_CPPv4N16wifi_ap_config_t8passwordE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8passwordE"></a> <a id="_CPPv2N16wifi_ap_config_t8passwordE"></a> <a id="wifi_ap_config_t::password__cA"></a> <a id="structwifi__ap__config__t_1a711f1a365b4b3809fa13adcbeae8608d"></a> char password\[WIFI\_PASSWORD\_LEN\]
    :   Password of BK AP, ignored in an open system.

    <a id="_CPPv4N16wifi_ap_config_t7channelE"></a>

    <a id="_CPPv3N16wifi_ap_config_t7channelE"></a> <a id="_CPPv2N16wifi_ap_config_t7channelE"></a> <a id="wifi_ap_config_t::channel__uint8_t"></a> <a id="structwifi__ap__config__t_1ab4005256cbe734b1a0b54c6c50609db3"></a> uint8\_t channel
    :   The channel of BK AP, 0 indicates default TODO

    <a id="_CPPv4N16wifi_ap_config_t8securityE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8securityE"></a> <a id="_CPPv2N16wifi_ap_config_t8securityE"></a> <a id="wifi_ap_config_t::security__wifi_security_t"></a> <a id="structwifi__ap__config__t_1aed1f22f0ba8a8d943ed574545a103556"></a> [wifi\_security\_t](#_CPPv415wifi_security_t "wifi_security_t") security
    :   Security type of BK AP, default value TODO

    <a id="_CPPv4N16wifi_ap_config_t6hiddenE"></a>

    <a id="_CPPv3N16wifi_ap_config_t6hiddenE"></a> <a id="_CPPv2N16wifi_ap_config_t6hiddenE"></a> <a id="wifi_ap_config_t::hidden__uint8_t"></a> <a id="structwifi__ap__config__t_1a4e43520cd26178b2eb1b537fe04593be"></a> uint8\_t hidden
    :   Whether the BK AP is hidden

    <a id="_CPPv4N16wifi_ap_config_t3acsE"></a>

    <a id="_CPPv3N16wifi_ap_config_t3acsE"></a> <a id="_CPPv2N16wifi_ap_config_t3acsE"></a> <a id="wifi_ap_config_t::acs__uint8_t"></a> <a id="structwifi__ap__config__t_1a365e2514f23c988ac1fe5e41a2326e3b"></a> uint8\_t acs
    :   Whether Auto Channel Selection is enabled

    <a id="_CPPv4N16wifi_ap_config_t8vsie_lenE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8vsie_lenE"></a> <a id="_CPPv2N16wifi_ap_config_t8vsie_lenE"></a> <a id="wifi_ap_config_t::vsie_len__uint8_t"></a> <a id="structwifi__ap__config__t_1a70a682fa907176b7a2c044e69204cd67"></a> uint8\_t vsie\_len
    :   Beacon/ProbeResp Vendor Specific IE len

    <a id="_CPPv4N16wifi_ap_config_t4vsieE"></a>

    <a id="_CPPv3N16wifi_ap_config_t4vsieE"></a> <a id="_CPPv2N16wifi_ap_config_t4vsieE"></a> <a id="wifi_ap_config_t::vsie__uint8_tA"></a> <a id="structwifi__ap__config__t_1aaccfac4bdaecd48892a9b40dd0d9376d"></a> uint8\_t vsie\[255\]
    :   Beacon/ProbeResp Vendor Specific IE

    <a id="_CPPv4N16wifi_ap_config_t7max_conE"></a>

    <a id="_CPPv3N16wifi_ap_config_t7max_conE"></a> <a id="_CPPv2N16wifi_ap_config_t7max_conE"></a> <a id="wifi_ap_config_t::max_con__uint8_t"></a> <a id="structwifi__ap__config__t_1a116921d43539d5acde0b878b8b0b61bb"></a> uint8\_t max\_con
    :   Max number of stations allowed to connect to BK AP, TODO default value?

    <a id="_CPPv4N16wifi_ap_config_t15max_statype_numE"></a>

    <a id="_CPPv3N16wifi_ap_config_t15max_statype_numE"></a> <a id="_CPPv2N16wifi_ap_config_t15max_statype_numE"></a> <a id="wifi_ap_config_t::max_statype_num__uint8_tA"></a> <a id="structwifi__ap__config__t_1aac1e7e17fe9d7afd2a98a772a76fd828"></a> uint8\_t max\_statype\_num\[4\]
    :   Max number of different station types allowed to connect to BK AP

    <a id="_CPPv4N16wifi_ap_config_t8reservedE"></a>

    <a id="_CPPv3N16wifi_ap_config_t8reservedE"></a> <a id="_CPPv2N16wifi_ap_config_t8reservedE"></a> <a id="wifi_ap_config_t::reserved__uint8_tA"></a> <a id="structwifi__ap__config__t_1ad67b68cd2431f45036aec30c7d48c4ea"></a> uint8\_t reserved\[32\]
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

    <a id="_CPPv3N21wifi_monitor_config_t14rx_mcast_frameE"></a> <a id="_CPPv2N21wifi_monitor_config_t14rx_mcast_frameE"></a> <a id="wifi_monitor_config_t::rx_mcast_frame__uint32_t"></a> <a id="structwifi__monitor__config__t_1a11e18caf7431f8dffb6fd9d3f7f8a2d8"></a> uint32\_t rx\_mcast\_frame
    :   Set this bit to enable callback to receive multicast/broadcast

    <a id="_CPPv4N21wifi_monitor_config_t12rx_dup_frameE"></a>

    <a id="_CPPv3N21wifi_monitor_config_t12rx_dup_frameE"></a> <a id="_CPPv2N21wifi_monitor_config_t12rx_dup_frameE"></a> <a id="wifi_monitor_config_t::rx_dup_frame__uint32_t"></a> <a id="structwifi__monitor__config__t_1a2e2175ad44c90e1604dc2d15282cf3d9"></a> uint32\_t rx\_dup\_frame
    :   Set this bit to enable callback to receive the duplicated

    <a id="_CPPv4N21wifi_monitor_config_t8reservedE"></a>

    <a id="_CPPv3N21wifi_monitor_config_t8reservedE"></a> <a id="_CPPv2N21wifi_monitor_config_t8reservedE"></a> <a id="wifi_monitor_config_t::reserved__uint32_t"></a> <a id="structwifi__monitor__config__t_1a55182a160c0a3e24d43e8ed4af1e6b97"></a> uint32\_t reserved
    :   Reserved bits, **must set to 0**

<a id="_CPPv417wifi_frame_info_t"></a>

<a id="_CPPv317wifi_frame_info_t"></a> <a id="_CPPv217wifi_frame_info_t"></a> <a id="wifi_frame_info_t"></a> <a id="structwifi__frame__info__t"></a> struct wifi\_frame\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17wifi_frame_info_t4rssiE"></a>

    <a id="_CPPv3N17wifi_frame_info_t4rssiE"></a> <a id="_CPPv2N17wifi_frame_info_t4rssiE"></a> <a id="wifi_frame_info_t::rssi__i"></a> <a id="structwifi__frame__info__t_1a6aff7f1e26a5ff819a3409d77e0b5521"></a> int rssi
    :   RSSI of the received frame in monitor mode

<a id="_CPPv420wifi_filter_config_t"></a>

<a id="_CPPv320wifi_filter_config_t"></a> <a id="_CPPv220wifi_filter_config_t"></a> <a id="wifi_filter_config_t"></a> <a id="structwifi__filter__config__t"></a> struct wifi\_filter\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20wifi_filter_config_t19rx_all_default_mgmtE"></a>

    <a id="_CPPv3N20wifi_filter_config_t19rx_all_default_mgmtE"></a> <a id="_CPPv2N20wifi_filter_config_t19rx_all_default_mgmtE"></a> <a id="wifi_filter_config_t::rx_all_default_mgmt__uint32_t"></a> <a id="structwifi__filter__config__t_1a687c38bc58f5cdc6077eb33cf3062345"></a> uint32\_t rx\_all\_default\_mgmt
    :   Set the bit to enable the callback to receive all management frame recived by WiFi driver

    <a id="_CPPv4N20wifi_filter_config_t12rx_probe_reqE"></a>

    <a id="_CPPv3N20wifi_filter_config_t12rx_probe_reqE"></a> <a id="_CPPv2N20wifi_filter_config_t12rx_probe_reqE"></a> <a id="wifi_filter_config_t::rx_probe_req__uint32_t"></a> <a id="structwifi__filter__config__t_1a4a90c000675f2cf4809dfbbfdc97b1e9"></a> uint32\_t rx\_probe\_req
    :   Set the bit to enable the callback to receive probe request

    <a id="_CPPv4N20wifi_filter_config_t12rx_probe_rspE"></a>

    <a id="_CPPv3N20wifi_filter_config_t12rx_probe_rspE"></a> <a id="_CPPv2N20wifi_filter_config_t12rx_probe_rspE"></a> <a id="wifi_filter_config_t::rx_probe_rsp__uint32_t"></a> <a id="structwifi__filter__config__t_1afe83e7acbd6d9fc4e1f9143440bbcff7"></a> uint32\_t rx\_probe\_rsp
    :   Set the bit to enable the callback to receive probe response

    <a id="_CPPv4N20wifi_filter_config_t13rx_all_beaconE"></a>

    <a id="_CPPv3N20wifi_filter_config_t13rx_all_beaconE"></a> <a id="_CPPv2N20wifi_filter_config_t13rx_all_beaconE"></a> <a id="wifi_filter_config_t::rx_all_beacon__uint32_t"></a> <a id="structwifi__filter__config__t_1afd9a6181c3ccc3c6a5d94d7bf4efe985"></a> uint32\_t rx\_all\_beacon
    :   Set the bit to enable the callback to receive all beacon

    <a id="_CPPv4N20wifi_filter_config_t9rx_actionE"></a>

    <a id="_CPPv3N20wifi_filter_config_t9rx_actionE"></a> <a id="_CPPv2N20wifi_filter_config_t9rx_actionE"></a> <a id="wifi_filter_config_t::rx_action__uint32_t"></a> <a id="structwifi__filter__config__t_1aff61cbdfa1cb9c7735ff255ce9fd9b48"></a> uint32\_t rx\_action
    :   Set the bit to enable the callback to receive action frame

    <a id="_CPPv4N20wifi_filter_config_t8reservedE"></a>

    <a id="_CPPv3N20wifi_filter_config_t8reservedE"></a> <a id="_CPPv2N20wifi_filter_config_t8reservedE"></a> <a id="wifi_filter_config_t::reserved__uint32_t"></a> <a id="structwifi__filter__config__t_1a973df8eff99eb428b0c3e929946c3543"></a> uint32\_t reserved
    :   Reserved bits, **must set to 0**

<a id="_CPPv414wifi_country_t"></a>

<a id="_CPPv314wifi_country_t"></a> <a id="_CPPv214wifi_country_t"></a> <a id="wifi_country_t"></a> <a id="structwifi__country__t"></a> struct wifi\_country\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14wifi_country_t2ccE"></a>

    <a id="_CPPv3N14wifi_country_t2ccE"></a> <a id="_CPPv2N14wifi_country_t2ccE"></a> <a id="wifi_country_t::cc__cA"></a> <a id="structwifi__country__t_1a1fd01869f4230eddd580637171e2e5cf"></a> char cc\[3\]
    :   country code string

    <a id="_CPPv4N14wifi_country_t5schanE"></a>

    <a id="_CPPv3N14wifi_country_t5schanE"></a> <a id="_CPPv2N14wifi_country_t5schanE"></a> <a id="wifi_country_t::schan__uint8_t"></a> <a id="structwifi__country__t_1af260339dd254a65b93a4e1d65576b117"></a> uint8\_t schan
    :   start channel

    <a id="_CPPv4N14wifi_country_t5nchanE"></a>

    <a id="_CPPv3N14wifi_country_t5nchanE"></a> <a id="_CPPv2N14wifi_country_t5nchanE"></a> <a id="wifi_country_t::nchan__uint8_t"></a> <a id="structwifi__country__t_1a1c129465b6bf5c803636dc05c21828dd"></a> uint8\_t nchan
    :   total channel number

    <a id="_CPPv4N14wifi_country_t12max_tx_powerE"></a>

    <a id="_CPPv3N14wifi_country_t12max_tx_powerE"></a> <a id="_CPPv2N14wifi_country_t12max_tx_powerE"></a> <a id="wifi_country_t::max_tx_power__int8_t"></a> <a id="structwifi__country__t_1a47a74c0fedee026097b4707efb792632"></a> int8\_t max\_tx\_power
    :   maximum tx power

    <a id="_CPPv4N14wifi_country_t6policyE"></a>

    <a id="_CPPv3N14wifi_country_t6policyE"></a> <a id="_CPPv2N14wifi_country_t6policyE"></a> <a id="wifi_country_t::policy__wifi_country_policy_t"></a> <a id="structwifi__country__t_1a80f2e1485534d43ae527f413d9c3095d"></a> [wifi\_country\_policy\_t](#_CPPv421wifi_country_policy_t "wifi_country_policy_t") policy
    :   country policy

<a id="_CPPv422wifi_event_scan_done_t"></a>

<a id="_CPPv322wifi_event_scan_done_t"></a> <a id="_CPPv222wifi_event_scan_done_t"></a> <a id="wifi_event_scan_done_t"></a> <a id="structwifi__event__scan__done__t"></a> struct wifi\_event\_scan\_done\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22wifi_event_scan_done_t7scan_idE"></a>

    <a id="_CPPv3N22wifi_event_scan_done_t7scan_idE"></a> <a id="_CPPv2N22wifi_event_scan_done_t7scan_idE"></a> <a id="wifi_event_scan_done_t::scan_id__uint32_t"></a> <a id="structwifi__event__scan__done__t_1a20b753514128873656807dde26c25806"></a> uint32\_t scan\_id
    :   Scan ID

<a id="_CPPv426wifi_event_sta_connected_t"></a>

<a id="_CPPv326wifi_event_sta_connected_t"></a> <a id="_CPPv226wifi_event_sta_connected_t"></a> <a id="wifi_event_sta_connected_t"></a> <a id="structwifi__event__sta__connected__t"></a> struct wifi\_event\_sta\_connected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26wifi_event_sta_connected_t4ssidE"></a>

    <a id="_CPPv3N26wifi_event_sta_connected_t4ssidE"></a> <a id="_CPPv2N26wifi_event_sta_connected_t4ssidE"></a> <a id="wifi_event_sta_connected_t::ssid__cA"></a> <a id="structwifi__event__sta__connected__t_1ae44a1f398d1e05aa00444cc1aa4aee5a"></a> char ssid\[WIFI\_SSID\_STR\_LEN\]
    :   SSID of connected AP

    <a id="_CPPv4N26wifi_event_sta_connected_t5bssidE"></a>

    <a id="_CPPv3N26wifi_event_sta_connected_t5bssidE"></a> <a id="_CPPv2N26wifi_event_sta_connected_t5bssidE"></a> <a id="wifi_event_sta_connected_t::bssid__uint8_tA"></a> <a id="structwifi__event__sta__connected__t_1a604d35bc824aa92b370f478c4066ed53"></a> uint8\_t bssid\[WIFI\_BSSID\_LEN\]
    :   BSSID of connected AP

<a id="_CPPv429wifi_event_sta_disconnected_t"></a>

<a id="_CPPv329wifi_event_sta_disconnected_t"></a> <a id="_CPPv229wifi_event_sta_disconnected_t"></a> <a id="wifi_event_sta_disconnected_t"></a> <a id="structwifi__event__sta__disconnected__t"></a> struct wifi\_event\_sta\_disconnected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t17disconnect_reasonE"></a> <a id="wifi_event_sta_disconnected_t::disconnect_reason__i"></a> <a id="structwifi__event__sta__disconnected__t_1a9b210ef1d662b2a29629754f7d507774"></a> int disconnect\_reason
    :   Disconnect reason of BK STA

    <a id="_CPPv4N29wifi_event_sta_disconnected_t15local_generatedE"></a>

    <a id="_CPPv3N29wifi_event_sta_disconnected_t15local_generatedE"></a> <a id="_CPPv2N29wifi_event_sta_disconnected_t15local_generatedE"></a> <a id="wifi_event_sta_disconnected_t::local_generated__b"></a> <a id="structwifi__event__sta__disconnected__t_1a8bb56bc2b970c2c802ffe11f91899948"></a> bool local\_generated
    :   if disconnect is request by local

<a id="_CPPv425wifi_event_ap_connected_t"></a>

<a id="_CPPv325wifi_event_ap_connected_t"></a> <a id="_CPPv225wifi_event_ap_connected_t"></a> <a id="wifi_event_ap_connected_t"></a> <a id="structwifi__event__ap__connected__t"></a> struct wifi\_event\_ap\_connected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N25wifi_event_ap_connected_t3macE"></a>

    <a id="_CPPv3N25wifi_event_ap_connected_t3macE"></a> <a id="_CPPv2N25wifi_event_ap_connected_t3macE"></a> <a id="wifi_event_ap_connected_t::mac__uint8_tA"></a> <a id="structwifi__event__ap__connected__t_1aaa082b5a590c648d34a3481b22604d26"></a> uint8\_t mac\[WIFI\_MAC\_LEN\]
    :   MAC of the STA connected to the BK AP

<a id="_CPPv428wifi_event_ap_disconnected_t"></a>

<a id="_CPPv328wifi_event_ap_disconnected_t"></a> <a id="_CPPv228wifi_event_ap_disconnected_t"></a> <a id="wifi_event_ap_disconnected_t"></a> <a id="structwifi__event__ap__disconnected__t"></a> struct wifi\_event\_ap\_disconnected\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N28wifi_event_ap_disconnected_t3macE"></a>

    <a id="_CPPv3N28wifi_event_ap_disconnected_t3macE"></a> <a id="_CPPv2N28wifi_event_ap_disconnected_t3macE"></a> <a id="wifi_event_ap_disconnected_t::mac__uint8_tA"></a> <a id="structwifi__event__ap__disconnected__t_1adb4e6dc30c213cc53f1e0ab4fb799ea3"></a> uint8\_t mac\[WIFI\_MAC\_LEN\]
    :   MAC of the STA disconnected from the BK AP

<a id="_CPPv422wifi_statistics_info_t"></a>

<a id="_CPPv322wifi_statistics_info_t"></a> <a id="_CPPv222wifi_statistics_info_t"></a> <a id="wifi_statistics_info_t"></a> <a id="structwifi__statistics__info__t"></a> struct wifi\_statistics\_info\_t
:   Wi-Fi Statistic info.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22wifi_statistics_info_t16tx_success_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t16tx_success_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t16tx_success_countE"></a> <a id="wifi_statistics_info_t::tx_success_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1a75fa5f69654b9bd14f88559f2955ad46"></a> uint32\_t tx\_success\_count
    :   Number of TX successes, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t14tx_retry_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t14tx_retry_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t14tx_retry_countE"></a> <a id="wifi_statistics_info_t::tx_retry_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1a2b9d80c7f66c11b6def89cb1153ca7b5"></a> uint32\_t tx\_retry\_count
    :   Number of TX retries, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t13tx_fail_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t13tx_fail_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t13tx_fail_countE"></a> <a id="wifi_statistics_info_t::tx_fail_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1a6024723cccfc6a999a0e4451fe291af5"></a> uint32\_t tx\_fail\_count
    :   Number of TX failures, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t16rx_success_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t16rx_success_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t16rx_success_countE"></a> <a id="wifi_statistics_info_t::rx_success_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1aefa4726286a6840096833fe24f03a916"></a> uint32\_t rx\_success\_count
    :   Number of RX successes, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t17rx_crcerror_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t17rx_crcerror_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t17rx_crcerror_countE"></a> <a id="wifi_statistics_info_t::rx_crcerror_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1a362dd76a480dfb489e5b87dc3a1e3c13"></a> uint32\_t rx\_crcerror\_count
    :   Number of RX FCS errors, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t15mic_error_countE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t15mic_error_countE"></a> <a id="_CPPv2N22wifi_statistics_info_t15mic_error_countE"></a> <a id="wifi_statistics_info_t::mic_error_count__uint32_t"></a> <a id="structwifi__statistics__info__t_1a6af2889ba06a3db9487c6e3d48eaa903"></a> uint32\_t mic\_error\_count
    :   Number of MIC errors, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t5noiseE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t5noiseE"></a> <a id="_CPPv2N22wifi_statistics_info_t5noiseE"></a> <a id="wifi_statistics_info_t::noise__int8_t"></a> <a id="structwifi__statistics__info__t_1acdedfd5d6f6d16043b919b6ac48197d2"></a> int8\_t noise
    :   Average noise level in dBm, -128 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t7phyrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t7phyrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t7phyrateE"></a> <a id="wifi_statistics_info_t::phyrate__uint16_t"></a> <a id="structwifi__statistics__info__t_1a8ff500d5044f9a7392a481852dba1c55"></a> uint16\_t phyrate
    :   Maximum used PHY rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t6txrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t6txrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t6txrateE"></a> <a id="wifi_statistics_info_t::txrate__uint16_t"></a> <a id="structwifi__statistics__info__t_1a9df8dbc49bc25de7a40ae3596ddb8a83"></a> uint16\_t txrate
    :   Average used TX rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t6rxrateE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t6rxrateE"></a> <a id="_CPPv2N22wifi_statistics_info_t6rxrateE"></a> <a id="wifi_statistics_info_t::rxrate__uint16_t"></a> <a id="structwifi__statistics__info__t_1a1718a529576569b810b026c300435acc"></a> uint16\_t rxrate
    :   Average used RX rate, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t4rssiE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t4rssiE"></a> <a id="_CPPv2N22wifi_statistics_info_t4rssiE"></a> <a id="wifi_statistics_info_t::rssi__int8_t"></a> <a id="structwifi__statistics__info__t_1ac0747e25cd3c89c3f3cd4f598be4385a"></a> int8\_t rssi
    :   Average beacon RSSI in dBm, -128 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t9bandwidthE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t9bandwidthE"></a> <a id="_CPPv2N22wifi_statistics_info_t9bandwidthE"></a> <a id="wifi_statistics_info_t::bandwidth__uint8_t"></a> <a id="structwifi__statistics__info__t_1ad797fb8d4586f94afbfbe91a56682f0a"></a> uint8\_t bandwidth
    :   Average used bandwidth, 0 if unavailable

    <a id="_CPPv4N22wifi_statistics_info_t13idle_time_perE"></a>

    <a id="_CPPv3N22wifi_statistics_info_t13idle_time_perE"></a> <a id="_CPPv2N22wifi_statistics_info_t13idle_time_perE"></a> <a id="wifi_statistics_info_t::idle_time_per__uint8_t"></a> <a id="structwifi__statistics__info__t_1a481102f7a5ddf09b8daa5d729a30771d"></a> uint8\_t idle\_time\_per
    :   Percent of idle time, 0 if unavailable

<a id="_CPPv414raw_tx_cntrl_t"></a>

<a id="_CPPv314raw_tx_cntrl_t"></a> <a id="_CPPv214raw_tx_cntrl_t"></a> <a id="raw_tx_cntrl_t"></a> <a id="structraw__tx__cntrl__t"></a> struct raw\_tx\_cntrl\_t
:   Wi-Fi RAW TX control.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14raw_tx_cntrl_t7tx_rateE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t7tx_rateE"></a> <a id="_CPPv2N14raw_tx_cntrl_t7tx_rateE"></a> <a id="raw_tx_cntrl_t::tx_rate__uint32_t"></a> <a id="structraw__tx__cntrl__t_1a105fb7de46f6eb363b6a3840dc374a6d"></a> uint32\_t tx\_rate
    :   RAW Data TX rate information

    <a id="_CPPv4N14raw_tx_cntrl_t8tx_powerE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t8tx_powerE"></a> <a id="_CPPv2N14raw_tx_cntrl_t8tx_powerE"></a> <a id="raw_tx_cntrl_t::tx_power__uint32_t"></a> <a id="structraw__tx__cntrl__t_1a7a01d26ccad63affbd38d0ef29f8f264"></a> uint32\_t tx\_power
    :   RAW Data TX power information

    <a id="_CPPv4N14raw_tx_cntrl_t12tx_retry_cntE"></a>

    <a id="_CPPv3N14raw_tx_cntrl_t12tx_retry_cntE"></a> <a id="_CPPv2N14raw_tx_cntrl_t12tx_retry_cntE"></a> <a id="raw_tx_cntrl_t::tx_retry_cnt__uint32_t"></a> <a id="structraw__tx__cntrl__t_1aa43c32fc5138afb8caccb660ad877cad"></a> uint32\_t tx\_retry\_cnt
    :   RAW Data TX retry count

<a id="_CPPv418wifi_raw_tx_info_t"></a>

<a id="_CPPv318wifi_raw_tx_info_t"></a> <a id="_CPPv218wifi_raw_tx_info_t"></a> <a id="wifi_raw_tx_info_t"></a> <a id="structwifi__raw__tx__info__t"></a> struct wifi\_raw\_tx\_info\_t
:   Wi-Fi RAW TX control.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18wifi_raw_tx_info_t3pktE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t3pktE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t3pktE"></a> <a id="wifi_raw_tx_info_t::pkt__uint8_tP"></a> <a id="structwifi__raw__tx__info__t_1a357f8cb52865dacbff1bc7b9f64b3461"></a> uint8\_t \*pkt
    :   RAW data tx packet address

    <a id="_CPPv4N18wifi_raw_tx_info_t3lenE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t3lenE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t3lenE"></a> <a id="wifi_raw_tx_info_t::len__i"></a> <a id="structwifi__raw__tx__info__t_1aaafc45d0951efd5b56d03757f8b5a7a4"></a> int len
    :   RAW data tx packet length

    <a id="_CPPv4N18wifi_raw_tx_info_t8tx_cntrlE"></a>

    <a id="_CPPv3N18wifi_raw_tx_info_t8tx_cntrlE"></a> <a id="_CPPv2N18wifi_raw_tx_info_t8tx_cntrlE"></a> <a id="wifi_raw_tx_info_t::tx_cntrl__raw_tx_cntrl_t"></a> <a id="structwifi__raw__tx__info__t_1ae23c160b93223bd0d3d54810c1b3d1cf"></a> [raw\_tx\_cntrl\_t](#_CPPv414raw_tx_cntrl_t "raw_tx_cntrl_t") tx\_cntrl
    :   RAW data tx control information

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

<a id="c.BK_MAX_STA_TYPE"></a>

<a id="group__bk__api__wifi__v2__typedef_1gafd21e4dbe54802b84c9014913faef2d4"></a> BK\_MAX\_STA\_TYPE

<a id="c.OUI_BEKEN"></a>

<a id="group__bk__api__wifi__v2__typedef_1ga8c05f9c6420142a4b7fa4cfe8dfb8aca"></a> OUI\_BEKEN

<a id="c.WLAN_EID_VENDOR_SPECIFIC"></a>

<a id="group__bk__api__wifi__v2__typedef_1ga35f179d40f064114d74f686c2eb3b159"></a> WLAN\_EID\_VENDOR\_SPECIFIC

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411BK_STA_TYPE"></a>

<a id="_CPPv311BK_STA_TYPE"></a> <a id="_CPPv211BK_STA_TYPE"></a> <a id="BK_STA_TYPE"></a> <a id="group__bk__api__wifi__v2__typedef_1ga338c42a75d2f50a9ef55c2238fc33adf"></a> typedef enum [sta\_type](#_CPPv48sta_type "sta_type") BK\_STA\_TYPE

<a id="_CPPv413wlan_ap_sta_t"></a>

<a id="_CPPv313wlan_ap_sta_t"></a> <a id="_CPPv213wlan_ap_sta_t"></a> <a id="wlan_ap_sta_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaee1806e2cb2fced0b508e89b826c781f"></a> typedef struct [wlan\_ap\_sta](#_CPPv411wlan_ap_sta "wlan_ap_sta") wlan\_ap\_sta\_t
:   Wlan station information definition.

<a id="_CPPv414wlan_ap_stas_t"></a>

<a id="_CPPv314wlan_ap_stas_t"></a> <a id="_CPPv214wlan_ap_stas_t"></a> <a id="wlan_ap_stas_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga87e20513af9f4d785dce84c467bceeef"></a> typedef struct [wlan\_ap\_stas](#_CPPv412wlan_ap_stas "wlan_ap_stas") wlan\_ap\_stas\_t
:   Wlan connected stations information definition.

<a id="_CPPv414wlan_ap_vsie_t"></a>

<a id="_CPPv314wlan_ap_vsie_t"></a> <a id="_CPPv214wlan_ap_vsie_t"></a> <a id="wlan_ap_vsie_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaf7e8bd776f7f7c2f724be49b4d64c8cb"></a> typedef struct [wlan\_ap\_vsie](#_CPPv412wlan_ap_vsie "wlan_ap_vsie") wlan\_ap\_vsie\_t
:   softap beacon/probe response’s vendor IEs Dynamic change softap’s vendor specific IEs.

<a id="_CPPv415wlan_sta_vsie_t"></a>

<a id="_CPPv315wlan_sta_vsie_t"></a> <a id="_CPPv215wlan_sta_vsie_t"></a> <a id="wlan_sta_vsie_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaadbe112db53caba97b2e6da18d89c3a6"></a> typedef struct [wlan\_sta\_vsie](#_CPPv413wlan_sta_vsie "wlan_sta_vsie") wlan\_sta\_vsie\_t
:   STA vendor IEs for (re)assoc, scan, p2p, p2p go, etc. Dynamic change STA’s vendor specific IEs.

<a id="_CPPv417wifi_monitor_cb_t"></a>

<a id="_CPPv317wifi_monitor_cb_t"></a> <a id="_CPPv217wifi_monitor_cb_t"></a> <a id="wifi_monitor_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1ga03e254e2c4a02c2c7721086c8b42d632"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_monitor\_cb\_t)(const uint8\_t \*frame, uint32\_t len, const [wifi\_frame\_info\_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") \*frame\_info)
:   Monitor callback to receive frames relayed by WiFi driver.

    **Attention**
    :   1\. The memory of frame and frame\_info will be freed immediately when the callback is returned. If we want to use the frame or frame\_info in other task, make a copy of them and handle them accordingly.

        2\. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

<a id="_CPPv416wifi_filter_cb_t"></a>

<a id="_CPPv316wifi_filter_cb_t"></a> <a id="_CPPv216wifi_filter_cb_t"></a> <a id="wifi_filter_cb_t"></a> <a id="group__bk__api__wifi__v2__typedef_1gaefba9da35fd949d32c2379679128c1ad"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*wifi\_filter\_cb\_t)(const uint8\_t \*frame, uint32\_t len, const [wifi\_frame\_info\_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") \*frame\_info)
:   Filter callback to receive frames relayed by WiFi driver.

    **Attention**
    :   1\. The memory of frame and frame\_info will be freed immediately when the callback is returned. If we want to use the frame or frame\_info in other task, make a copy of them and handle them accordingly.

        2\. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412wifi_event_t"></a>

<a id="_CPPv312wifi_event_t"></a> <a id="_CPPv212wifi_event_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga4d4930414997036f72c92e8a02a6de33"></a> enum wifi\_event\_t
:   WiFi public event type.

    *Values:*

    <a id="_CPPv4N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a>

    <a id="_CPPv3N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a> <a id="_CPPv2N12wifi_event_t20EVENT_WIFI_SCAN_DONEE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a70b73fdd0fe544808f91625b672c8381"></a> enumerator EVENT\_WIFI\_SCAN\_DONE
    :   WiFi scan done event

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

    <a id="_CPPv4N12wifi_event_t16EVENT_WIFI_COUNTE"></a>

    <a id="_CPPv3N12wifi_event_t16EVENT_WIFI_COUNTE"></a> <a id="_CPPv2N12wifi_event_t16EVENT_WIFI_COUNTE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4d4930414997036f72c92e8a02a6de33a45f8fd32bccb88538c4e36c1bf884c8c"></a> enumerator EVENT\_WIFI\_COUNT
    :   WiFi event count

<a id="_CPPv417wifi_err_reason_t"></a>

<a id="_CPPv317wifi_err_reason_t"></a> <a id="_CPPv217wifi_err_reason_t"></a> <a id="group__bk__api__wifi__v2__enum_1gaf2f44e69763071bbe8c3903158c5a357"></a> enum wifi\_err\_reason\_t
:   *Values:*

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

    <a id="_CPPv4N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a>

    <a id="_CPPv3N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a> <a id="_CPPv2N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE"></a> <a id="group__bk__api__wifi__v2__enum_1gga4173eff95b62808051ec8f9af3435b10ae63b6c62932542faeff9cdc3b1bccfad"></a> enumerator WIFI\_LINKSTATE\_STA\_GOT\_IP
    :   sta mode got ip

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

<a id="_CPPv417wifi_capability_t"></a>

<a id="_CPPv317wifi_capability_t"></a> <a id="_CPPv217wifi_capability_t"></a> <a id="group__bk__api__wifi__v2__enum_1ga1bc14fb46de73ab0c10a7aa6f93469b1"></a> enum wifi\_capability\_t
:   WiFi capability interface ID.

    *Values:*

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1ab3e86139f96fa7bf44bfca2e48e99288"></a> enumerator WIFI\_CAPA\_ID\_ERP\_EN
    :   Update Wi-Fi 11g support capability

    <a id="_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a> <a id="_CPPv2N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a509db8830dd020d46467f5f901c61750"></a> enumerator WIFI\_CAPA\_ID\_HT\_EN
    :   Update Wi-Fi 11n support capability

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a20a580b04bf57e6643dd7f6caced3b0e"></a> enumerator WIFI\_CAPA\_ID\_VHT\_EN
    :   Update Wi-Fi 11ac support capability

    <a id="_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a> <a id="_CPPv2N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a539c9e9af6fc31f9a0e6ff59ed692e60"></a> enumerator WIFI\_CAPA\_ID\_HE\_EN
    :   Update Wi-Fi 11ax support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a90c2ebb0b0317f1f0e63ac6682234ac7"></a> enumerator WIFI\_CAPA\_ID\_TX\_AMPDU\_EN
    :   Update Wi-Fi TX AMPDU support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a3700a20c2b98c1057cf037609259a165"></a> enumerator WIFI\_CAPA\_ID\_RX\_AMPDU\_EN
    :   Update Wi-Fi RX AMPDU support capability

    <a id="_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a>

    <a id="_CPPv3N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a> <a id="_CPPv2N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1af49634dbabbc838822f79ac41c2736ed"></a> enumerator WIFI\_CAPA\_ID\_TX\_AMPDU\_NUM
    :   Update Wi-Fi TX AMPDU maximum number

    <a id="_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a>

    <a id="_CPPv3N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a> <a id="_CPPv2N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a94706d23864a16daa9da8fdcab9cb078"></a> enumerator WIFI\_CAPA\_ID\_RX\_AMPDU\_NUM
    :   Update Wi-Fi RX AMPDU maximum number

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a540fa8c0fd197d5fab3e5cda5d459bea"></a> enumerator WIFI\_CAPA\_ID\_VHT\_MCS
    :   Update Wi-Fi VHT MCS

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1aecfd132e3d6befab007b9e494fb023cf"></a> enumerator WIFI\_CAPA\_ID\_HE\_MCS
    :   Update Wi-Fi HE MCS

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a2d33c8884f8ec6ef08917bfecb58590e"></a> enumerator WIFI\_CAPA\_ID\_B40\_EN
    :   Update Wi-Fi 40M bandwidth support capability

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1ac5c351263a116445f5e06cf768049e89"></a> enumerator WIFI\_CAPA\_ID\_STBC\_EN
    :   Update Wi-Fi STBC support capability

    <a id="_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a> <a id="_CPPv2N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1afdfb433a65abbcabaadbc3bb6c57b6df"></a> enumerator WIFI\_CAPA\_ID\_SGI\_EN
    :   Update Wi-Fi Short GI support capability

    <a id="_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a> <a id="_CPPv2N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1a9d7b5c52661ed0f3fd96e71d4751a531"></a> enumerator WIFI\_CAPA\_ID\_LDPC\_EN
    :   Update Wi-Fi LDPC support capability

    <a id="_CPPv4N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a> <a id="_CPPv2N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1aa976ce961e99b6667ff5d87ac8be793b"></a> enumerator WIFI\_CAPA\_ID\_BEAMFORMEE\_EN
    :   Update Wi-Fi Beamforming support capability

    <a id="_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a>

    <a id="_CPPv3N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a> <a id="_CPPv2N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1ab905eabd71d5435d08f5e869e8727969"></a> enumerator WIFI\_CAPA\_ID\_11B\_ONLY\_EN
    :   Update Wi-Fi 11b support capability

    <a id="_CPPv4N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a>

    <a id="_CPPv3N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a> <a id="_CPPv2N17wifi_capability_t16WIFI_CAPA_ID_MAXE"></a> <a id="group__bk__api__wifi__v2__enum_1gga1bc14fb46de73ab0c10a7aa6f93469b1aa67a283f3bf515e1bd9f664d47469876"></a> enumerator WIFI\_CAPA\_ID\_MAX

<a id="_CPPv422wifi_vht_mcs_support_t"></a>

<a id="_CPPv322wifi_vht_mcs_support_t"></a> <a id="_CPPv222wifi_vht_mcs_support_t"></a> <a id="group__bk__api__wifi__v2__enum_1gadb26f2daae2c9087a555c24eddbecb0a"></a> enum wifi\_vht\_mcs\_support\_t
:   enum wifi\_vht\_mcs\_support\_t \- VHT MCS support definitions : MCSes 0-7 are supported for the number of streams : MCSes 0-8 are supported : MCSes 0-9 are supported : This number of streams isn’t supported

    *Values:*

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E"></a> <a id="group__bk__api__wifi__v2__enum_1ggadb26f2daae2c9087a555c24eddbecb0aa062b704f0871c4a2d56681c14f804929"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_7

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E"></a> <a id="group__bk__api__wifi__v2__enum_1ggadb26f2daae2c9087a555c24eddbecb0aa209c326411d901faed481cff5cd43f6a"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_8

    <a id="_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E"></a> <a id="group__bk__api__wifi__v2__enum_1ggadb26f2daae2c9087a555c24eddbecb0aaabebf87c28a705d8cb1de13b2a4976cb"></a> enumerator WIFI\_VHT\_MCS\_SUPPORT\_0\_9

    <a id="_CPPv4N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a>

    <a id="_CPPv3N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a> <a id="_CPPv2N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggadb26f2daae2c9087a555c24eddbecb0aa112ae860aeec764efa0f0f4ce1545c5c"></a> enumerator WIFI\_VHT\_MCS\_NOT\_SUPPORTED

<a id="_CPPv421wifi_he_mcs_support_t"></a>

<a id="_CPPv321wifi_he_mcs_support_t"></a> <a id="_CPPv221wifi_he_mcs_support_t"></a> <a id="group__bk__api__wifi__v2__enum_1gae7464a9b074f1be5423f165133c9ad3a"></a> enum wifi\_he\_mcs\_support\_t
:   enum wifi\_he\_mcs\_support\_t \- HE MCS support definitions : MCSes 0-7 are supported for the number of streams : MCSes 0-9 are supported : MCSes 0-11 are supported : This number of streams isn’t supported

    *Values:*

    <a id="_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E"></a> <a id="group__bk__api__wifi__v2__enum_1ggae7464a9b074f1be5423f165133c9ad3aa4e0382b30014b923c2a8837784f5c424"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_7

    <a id="_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E"></a> <a id="group__bk__api__wifi__v2__enum_1ggae7464a9b074f1be5423f165133c9ad3aae4ebc49186f71531199b487be61b467b"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_9

    <a id="_CPPv4N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a> <a id="_CPPv2N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E"></a> <a id="group__bk__api__wifi__v2__enum_1ggae7464a9b074f1be5423f165133c9ad3aa2714520af3f93b9d74fd13b37cb043d1"></a> enumerator WIFI\_HE\_MCS\_SUPPORT\_0\_11

    <a id="_CPPv4N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a>

    <a id="_CPPv3N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a> <a id="_CPPv2N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE"></a> <a id="group__bk__api__wifi__v2__enum_1ggae7464a9b074f1be5423f165133c9ad3aa7c2eb8768bd4374f50fb00861ae4d953"></a> enumerator WIFI\_HE\_MCS\_NOT\_SUPPORTED

<a id="_CPPv413wifi_sta_vsie"></a>

<a id="_CPPv313wifi_sta_vsie"></a> <a id="_CPPv213wifi_sta_vsie"></a> <a id="group__bk__api__wifi__v2__typedef_1gaa1d5b5ba230d1c589aef12cc2f37b74a"></a> enum wifi\_sta\_vsie
:   *Values:*

    <a id="_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a>

    <a id="_CPPv3N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a> <a id="_CPPv2N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aa26a026a55299e3c1d38a55d19ccb4012"></a> enumerator WIFI\_VENDOR\_ELEM\_ASSOC\_REQ

    <a id="_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a>

    <a id="_CPPv3N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a> <a id="_CPPv2N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aa49490b43ee20cbe063ea6684ff56ec92"></a> enumerator WIFI\_VENDOR\_ELEM\_PROBE\_REQ

    <a id="_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a>

    <a id="_CPPv3N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a> <a id="_CPPv2N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE"></a> <a id="group__bk__api__wifi__v2__typedef_1ggaa1d5b5ba230d1c589aef12cc2f37b74aab5c7caa3432bfa14169d5e3d3e87a67a"></a> enumerator NUM\_WIFI\_VENDOR\_ELEM\_FRAMES

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
