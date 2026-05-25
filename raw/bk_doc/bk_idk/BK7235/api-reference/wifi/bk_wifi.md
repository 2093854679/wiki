# Wi-Fi APIs[](#wi-fi-apis "永久链接至标题")


重要

The WiFi API v2.0 is the lastest stable WiFi APIs, it’s used to deprecate the WiFi API v1.0. All new applications should use WiFi API v2.0.


## Wi-Fi Interface[](#wi-fi-interface "永久链接至标题")

The BK WiFi Driver supports following logical WiFi interfaces:

> - BK STA interface
> - BK AP interface
> - BK Monitor interface

Each interface can be operated independently, so theretically all interfaces can be started independently. However because of performance and interference consideration, we limit the coexisting of some interfaces.

E.g. if the monitor interface is started, the starting of STA interface will fail, refer to API for detailed limitation of interface coexisting.


## Wi-Fi API Categories[](#wi-fi-api-categories "永久链接至标题")

Most of WiFi APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk_wifi, the APIs may be common for all interfaces or some interfaces, e.g. bk_wifi_init() etc.
> - Interface specific APIs.
>
>   The API name are prefixed with bk_wifi_interface, the interface can be sta, ap or monitor. e.g. bk_wifi_sta_start() etc.
> - Module specific APIs
>
>   The API name are prefixed with bk_wifi_module, the module can be scan or filter etc, e.g. bk_wifi_scan_start() etc. The API has no direct relationship with the interface, or the API caller don’t nedto care about on which interface the API is operated. E.g. the scan API can be based on STA interface, it can also based on AP interface, but the caller don’t care about it.

Common WiFi APIs:
:   - [`bk_wifi_init()`](#_CPPv412bk_wifi_initPK18wifi_init_config_t "bk_wifi_init") - init WiFi

    - [`bk_wifi_deinit()`](#_CPPv414bk_wifi_deinitv "bk_wifi_deinit") - deinit WiFi

    - [`bk_wifi_set_country()`](#_CPPv419bk_wifi_set_countryPK14wifi_country_t "bk_wifi_set_country") - set country code

    - [`bk_wifi_get_country()`](#_CPPv419bk_wifi_get_countryP14wifi_country_t "bk_wifi_get_country") - get country code

    - [`bk_wifi_send_raw()`](#_CPPv416bk_wifi_send_rawP7uint8_ti "bk_wifi_send_raw") - send raw 802.11 frame

Interface specific WiFi APIs:
:   - [`bk_wifi_sta_start()`](#_CPPv417bk_wifi_sta_startv "bk_wifi_sta_start") - start BK STA

    - [`bk_wifi_sta_stop()`](#_CPPv416bk_wifi_sta_stopv "bk_wifi_sta_stop") - stop BK STA

    - [`bk_wifi_sta_set_config()`](#_CPPv422bk_wifi_sta_set_configPK17wifi_sta_config_t "bk_wifi_sta_set_config") - set **basic** configurations BK STA, such as SSID etc

    - [`bk_wifi_sta_get_config()`](#_CPPv422bk_wifi_sta_get_configP17wifi_sta_config_t "bk_wifi_sta_get_config") - get basic configuration of BK STA

    - [`bk_wifi_sta_get_linkstate_with_reason()`](#_CPPv437bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t "bk_wifi_sta_get_linkstate_with_reason") - get actual link status of BK STA and reason code

    - [`bk_wifi_sta_get_link_status()`](#_CPPv427bk_wifi_sta_get_link_statusP18wifi_link_status_t "bk_wifi_sta_get_link_status") - get link status of BK STA

    - [`bk_wifi_sta_connect()`](#_CPPv419bk_wifi_sta_connectv "bk_wifi_sta_connect") - connect the BK STA to AP

    - [`bk_wifi_sta_disconnect()`](#_CPPv422bk_wifi_sta_disconnectv "bk_wifi_sta_disconnect") - disconnect the Wi-Fi connection

    - [`bk_wifi_sta_pm_enable()`](#_CPPv421bk_wifi_sta_pm_enablev "bk_wifi_sta_pm_enable") - enable STA power management

    - [`bk_wifi_sta_pm_disable()`](#_CPPv422bk_wifi_sta_pm_disablev "bk_wifi_sta_pm_disable") - disable STA power management

    - [`bk_wifi_get_channel()`](#_CPPv419bk_wifi_get_channelv "bk_wifi_get_channel") - get current channel ID

    - [`bk_wifi_set_mac_address()`](#_CPPv423bk_wifi_set_mac_addressPc "bk_wifi_set_mac_address") - set Wi-Fi MAC address

    - [`bk_wifi_manual_cal_rfcali_status()`](#_CPPv432bk_wifi_manual_cal_rfcali_statusv "bk_wifi_manual_cal_rfcali_status") - get Wi-Fi Calibration status

    - [`bk_wifi_ap_start()`](#_CPPv416bk_wifi_ap_startv "bk_wifi_ap_start") - start BK AP

    - [`bk_wifi_ap_stop()`](#_CPPv415bk_wifi_ap_stopv "bk_wifi_ap_stop") - stop BK AP

    - [`bk_wifi_ap_set_config()`](#_CPPv421bk_wifi_ap_set_configPK16wifi_ap_config_t "bk_wifi_ap_set_config") - set the **basic** configuration of BK AP, such as SSID etc

    - [`bk_wifi_ap_get_config()`](#_CPPv421bk_wifi_ap_get_configP16wifi_ap_config_t "bk_wifi_ap_get_config") - get the basic configuration of BK AP

    - [`bk_wifi_ap_get_sta_list()`](#_CPPv423bk_wifi_ap_get_sta_listP14wlan_ap_stas_t "bk_wifi_ap_get_sta_list") - get the STAs connected to BK AP

    - [`bk_wifi_sta_get_mac()`](#_CPPv419bk_wifi_sta_get_macP7uint8_t "bk_wifi_sta_get_mac") - get STA MAC address

    - [`bk_wifi_ap_get_mac()`](#_CPPv418bk_wifi_ap_get_macP7uint8_t "bk_wifi_ap_get_mac") - get AP MAC address

    - [`bk_wifi_monitor_start()`](#_CPPv421bk_wifi_monitor_startv "bk_wifi_monitor_start") - start the monitor

    - [`bk_wifi_monitor_stop()`](#_CPPv420bk_wifi_monitor_stopv "bk_wifi_monitor_stop") - stop the monitor

    - [`bk_wifi_monitor_set_config()`](#_CPPv426bk_wifi_monitor_set_configPK21wifi_monitor_config_t "bk_wifi_monitor_set_config") - set **basic** configuration of the monitor

    - [`bk_wifi_monitor_get_config()`](#_CPPv426bk_wifi_monitor_get_configP21wifi_monitor_config_t "bk_wifi_monitor_get_config") - get basic configuration of the monitor

    - [`bk_wifi_monitor_register_cb()`](#_CPPv427bk_wifi_monitor_register_cbK17wifi_monitor_cb_t "bk_wifi_monitor_register_cb") - register monitor callback function

    - [`bk_wifi_monitor_set_channel()`](#_CPPv427bk_wifi_monitor_set_channelPK14wifi_channel_t "bk_wifi_monitor_set_channel") - set the channel of monitor

Module Specific WiFi APIs:
:   - `bk_wifi_scan_register_cb()` - register scan callback function

    - [`bk_wifi_scan_start()`](#_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t "bk_wifi_scan_start") - start the scan

    - [`bk_wifi_scan_stop()`](#_CPPv417bk_wifi_scan_stopv "bk_wifi_scan_stop") - stop the scan

    - [`bk_wifi_scan_get_result()`](#_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t "bk_wifi_scan_get_result") - get the scan result

    - [`bk_wifi_scan_dump_result()`](#_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t "bk_wifi_scan_dump_result") - dump the scan result

    - [`bk_wifi_scan_free_result()`](#_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t "bk_wifi_scan_free_result") - dump the scan result

    - [`bk_wifi_filter_set_config()`](#_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t "bk_wifi_filter_set_config") - set filter configuration

    - [`bk_wifi_filter_register_cb()`](#_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t "bk_wifi_filter_register_cb") - register the filter callback function


## Compitability and Extension[](#compitability-and-extension "永久链接至标题")

The WiFi APIs are flexible, easy to be extended and backward compatible. For most of the WiFi configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for WiFi API users:
:   - Always init the reserved fields of config stuct to 0

    - Use BK_ERR_CHECK to check the return value of the WiFi API

    - If you are not sure how to use WiFi APIs, study the WiFi example code first

    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields, e.g. use WIFI_DEFAULT_INIT_CONFIG() to init wifi_config_t first.

    - Don’t do too much work in WiFi event callback, relay the event to your own application task.


## User Development Model[](#user-development-model "永久链接至标题")

Similar as most popular WiFi driver, the Beken WiFi driver is implemented as event driver. The application call WiFi APIs to operate the WiFi driver and get notified by WiFi event.


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [wifi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_init(const [wifi_init_config_t](#_CPPv418wifi_init_config_t "wifi_init_config_t") *init_config)[](#_CPPv412bk_wifi_initPK18wifi_init_config_t "永久链接至目标")
:   This API initializes the WiFi driver, e.g. creating task for supplicant, allocating resource for low level WiFi driver etc.

    Usage example:

    ```
     wifi_init_config_t init_config = WIFI_DEFAULT_INIT_CONFIG;
     BK_LOG_ON_ERR(bk_wifi_init(&init_config);
    ```


    **Attention**
    :   1. This API is the 1st API that should be called before any other WiFi API can be called.

        2. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_deinit(void)[](#_CPPv414bk_wifi_deinitv "永久链接至目标")
:   Deinit the BK WiFi driver.

    This API free all resources related to WiFi.


    **Attention**
    :   1. This API is not ready yet, will support in future release.

    返回
    :   - BK_OK: succeed

        - BK_ERR_NOT_SUPPORT: The API is not supported yet.

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_start(void)[](#_CPPv417bk_wifi_sta_startv "永久链接至目标")
:   Start the BK STA.

    This API init the resoure specific to BK STA, e.g. init STA specific globals, init the supplicant and STA specific WiFi driver etc.


    **Attention**
    :   1. Make sure the [bk_wifi_sta_set_config()](#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94 "#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94") are succeedful before calling this API.

        2. This API connect the BK STA to the configured AP automatically.

        3. If the BK STA is already started, this API ignores the request and returns BK_OK. if you want to restart the BK STA, call [bk_wifi_sta_stop()](#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b "#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b") first and then call this API.

        4. TODO description about fast connection

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_STA_NOT_CONFIG: the BK STA is not configured.

        - BK_ERR_WIFI_MONITOR_IP: the BK STA can’t be started because monitor is started.

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_stop(void)[](#_CPPv416bk_wifi_sta_stopv "永久链接至目标")
:   Stop the BK STA.


    **Attention**
    :   This API causes the BK STA disconnect from the AP, it similar as [bk_wifi_sta_disconnect()](#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11 "#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11"), but this API may free resource.

    返回
    :   - BK_OK: succeed

        - BK_FAIL: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_scan_stop(void)[](#_CPPv417bk_wifi_scan_stopv "永久链接至目标")
:   Stop the pure scan operation.


    **Attention**
    :   This API causes the BK STA disconnect from the AP, it similar as [bk_wifi_sta_disconnect()](#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11 "#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11"), but this API may free resource.

    返回
    :   - BK_OK: succeed

        - BK_FAIL: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_set_config(const [wifi_sta_config_t](#_CPPv417wifi_sta_config_t "wifi_sta_config_t") *sta_config)[](#_CPPv422bk_wifi_sta_set_configPK17wifi_sta_config_t "永久链接至目标")
:   Config the BK STA.

    This API configures the basic configurations of the BK STA, it should be called before we call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") to start the BK STA. It can also be used to update the configuration after the BK STA is started.

    Usage example:

    ```
    wifi_sta_config_t sta_config = WIFI_DEFAULT_STA_CONFIG();

    os_strncpy(sta_config.ssid, "ssid", WIFI_SSID_STR_LEN);
    os_strncpy(sta_config.password, "password");
    //more initialization here
    BK_LOG_ON_ERR(bk_wifi_sta_set_config(&sta_config));
    ```


    **Attention**
    :   1. Don’t call this API when the monitor is in-progress

        2. If STA is already connected to AP, this API cases BK STA reconnects the AP.

        3. Make sure the reserved fields in sta_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

        4. Auto reconnect max count and timeout can be set. When user app receives EVENT_WIFI_STA_DISCONNECTED event, it’s user app’s responsibility to reconnect to AP manually. Max count and timeout set to zero to let supplicant automatically handles connection without user app’s interaction.

    参数
    :   **sta_config** – the STA configuration

    返回
    :   - BK_OK: succeed

        - BK_ERR_STA_NOT_STARTED: the STA is not started, call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") first.

        - BK_ERR_NULL_PARAM: parameter config is NULL.

        - BK_ERR_WIFI_RESERVED_FIELD: the reserved field of config is not 0.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_config([wifi_sta_config_t](#_CPPv417wifi_sta_config_t "wifi_sta_config_t") *sta_config)[](#_CPPv422bk_wifi_sta_get_configP17wifi_sta_config_t "永久链接至目标")
:   Get the configuration of the BK STA.

    参数
    :   **sta_config** – store the BK STA configuration

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL.

        - BK_ERR_WIFI_STA_NOT_CONFIG: STA is not configured yet.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_linkstate_with_reason([wifi_linkstate_reason_t](#_CPPv423wifi_linkstate_reason_t "wifi_linkstate_reason_t") *info)[](#_CPPv437bk_wifi_sta_get_linkstate_with_reasonP23wifi_linkstate_reason_t "永久链接至目标")
:   Get the WiFi station state of the BK STA.


    - If sta is idle or connected, reason code will be WIFI_REASON_MAX


    **Attention**
    :   the difference between this API and [bk_wifi_sta_get_link_status()](#group__bk__api__wifi__v2_1ga05fa3da4689980df705e03c6416df12e "#group__bk__api__wifi__v2_1ga05fa3da4689980df705e03c6416df12e") is


        - This API gets the actual WiFi STA link status and reason code

    参数
    :   **state** – store the WiFi station state of the BK STA

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_link_status([wifi_link_status_t](#_CPPv418wifi_link_status_t "wifi_link_status_t") *link_status)[](#_CPPv427bk_wifi_sta_get_link_statusP18wifi_link_status_t "永久链接至目标")
:   Get the WiFi link info of the BK STA.

    Get the actual WiFi link status of the BK STA.


    **Attention**
    :   the difference between this API and [bk_wifi_sta_get_config()](#group__bk__api__wifi__v2_1gabd063029cb792bd168970dd1f8dd06b3 "#group__bk__api__wifi__v2_1gabd063029cb792bd168970dd1f8dd06b3") is


        - This API gets the actual STA link info while the later gets the configured value

        - This API can get more info of the link, such as RSSI, WiFi link status, AID etc.

        - The AID is only valid if ->state is WIFI_LINK_CONNECTED.

    参数
    :   **link_status** – store the WiFi link status of the BK STA

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter link_info is NULL.

        - BK_ERR_WIFI_DRIVER: WiFi low level driver has failure.

        - BK_ERR_WIFI_NO_MEM: Not enough memory

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_connect(void)[](#_CPPv419bk_wifi_sta_connectv "永久链接至目标")
:   Connect the BK STA to the AP.


    **Attention**
    :   1. Make sure STA is started by [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") before calling this API.

        2. Don’t call this API when the monitor is in-progress

        3. If STA is already connected to AP, this API reconnects the BK STA.

        4. TODO - multiple same SSID connect???

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_STA_NOT_STARTED: the STA is not started, call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") first.

        - BK_ERR_WIFI_MONITOR_IP: the API is not allowed because monitor is in-progress.

        - others: other failures.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_disconnect(void)[](#_CPPv422bk_wifi_sta_disconnectv "永久链接至目标")
:   Disconnect the WiFi connection of the BK STA.


    **Attention**
    :   TODO - add description about disconnect event!

    返回
    :   - BK_OK: succeed

        - others: other failures.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_scan_start(const [wifi_scan_config_t](#_CPPv418wifi_scan_config_t "wifi_scan_config_t") *scan_config)[](#_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t "永久链接至目标")
:   Start a scan.

    This API notifies the WiFi driver to start a scan, the event EVENT_WIFI_SCAN_DONE will be raised if the scan is completed. General steps to use this API:


    - prepare the scan done event callback, the callback can call [bk_wifi_scan_get_result()](#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc "#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc") to get the scan result and then call [bk_wifi_scan_free_result()](#group__bk__api__wifi__v2_1ga75df3c75b3bd8844e9e68c8e339859b6 "#group__bk__api__wifi__v2_1ga75df3c75b3bd8844e9e68c8e339859b6") to free the resource.

    - call bk_event_register_cb(EVENT_MOD_WIFI, EVENT_WIFI_SCAN_DONE, …) to register scan done event callback.

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
    :   1. This API triggers an active scan on all channels (TODO double check)

        2. Pass NULL scan_config to scan all APs, otherwise scan the SSID specified in scan_config.ssid

        3. Make sure the reserved fields in scan_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

        4. TODO scan result limits???

    参数
    :   **scan_config** – the configuration of scan

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_STA_NOT_STARTED: the STA is not started, call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") first.

        - BK_ERR_WIFI_MONITOR_IP: the API is not allowed because monitor is in-progress.

        - others: other failures.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_scan_get_result([wifi_scan_result_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") *scan_result)[](#_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t "永久链接至目标")
:   Get the scan result.

    Usage example:

    ```
    wifi_scan_result_t scan_result = {0};

    BK_LOG_ON_ERR(bk_wifi_scan_get_result(&scan_result));
    bk_wifi_scan_free_result(&scan_result);
    ```


    **Attention**
    :   1. The caller don’t need to allocate memory for scan_result->aps, this API will allocate the memory for scan_result->aps according to the actual found AP number.

        2. Don’t forget to call bk_wifi_scan_free_result(&scan_result) to free the the resource allocated in this API, otherwise memory leak.

    参数
    :   **scan_result** – store the scan result

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: NULL scan_result

        - BK_ERR_NO_MEM: out of memory

        - others: other failures

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_scan_dump_result(const [wifi_scan_result_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") *scan_result)[](#_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t "永久链接至目标")
:   Dump the scan result.

    参数
    :   **scan_result** – The scan result to be dumped.

    返回
    :   - BK_OK: succeed

        - BK_ERR_PARAM: invalid scan result

void bk_wifi_scan_free_result([wifi_scan_result_t](#_CPPv418wifi_scan_result_t "wifi_scan_result_t") *scan_result)[](#_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t "永久链接至目标")
:   Free the scan result.


    **Attention**
    :   This API free scan_result->aps which allocated in [bk_wifi_scan_get_result()](#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc "#group__bk__api__wifi__v2_1ga381d59740e2a90c6dbeef0c9eec345dc"), it doesn’t free scan_result. So if scan_result is allocated by the caller, the caller need to free it.

    参数
    :   **scan_result** – The scan result to be freed.

    返回
    :   - BK_OK: always succeed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_add_vendor_ie(uint8_t frame, uint8_t *vsie, uint8_t len)[](#_CPPv425bk_wifi_sta_add_vendor_ie7uint8_tP7uint8_t7uint8_t "永久链接至目标")
:   Add/Update/Del STA’s Vendor Specific IE **before** connect to AP.


    **Attention**
    :   If you want to add vsie when sta starts, just initialize [wifi_sta_config_t](#structwifi__sta__config__t "#structwifi__sta__config__t") when call [bk_wifi_sta_set_config()](#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94 "#group__bk__api__wifi__v2_1ga0096c53cd18fce4b06d5229a7d63cb94").

    参数
    :   - **buf** – vsie buf

        - **len** – vsie buf len

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_update_vendor_ie(uint8_t frame, uint8_t *vsie, uint8_t len)[](#_CPPv428bk_wifi_sta_update_vendor_ie7uint8_tP7uint8_t7uint8_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_del_vendor_ie(uint8_t frame)[](#_CPPv425bk_wifi_sta_del_vendor_ie7uint8_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_start(void)[](#_CPPv416bk_wifi_ap_startv "永久链接至目标")
:   Start the BK AP.

    This API init the resoure specific to BK AP, e.g. init BK AP specific globals, init the hostapd and AP specific WiFi driver etc.

    If the BK AP is already started, this API ignores the request and returns BK_OK, we can call [bk_wifi_ap_stop()](#group__bk__api__wifi__v2_1ga1836b0aeeb20668e861bad0baa2ea0d3 "#group__bk__api__wifi__v2_1ga1836b0aeeb20668e861bad0baa2ea0d3") to stop BK AP first and then call [bk_wifi_ap_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5 "#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5") to restart it.


    **Restart** AP Usage example:

    ```
    BK_LOG_ON_ERR(bk_wifi_ap_stop());
    BK_LOG_ON_ERR(bk_wifi_ap_start());
    ```


    **Attention**
    :   1. Don’t call this API when the monitor is in-progress

        2. If [bk_wifi_ap_set_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39 "#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39") is not called, this API start the AP with default value, normally you should configure the AP first before calling this API.

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_AP_NOT_CONFIGURED: the WiFi AP is not configured, call [bk_wifi_ap_set_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39 "#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39") first.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_stop(void)[](#_CPPv415bk_wifi_ap_stopv "永久链接至目标")
:   Stop the BK AP.

    返回
    :   - BK_OK: succeed

        - BK_WIFI_NOT_INIT: the WiFi is not initialized, call [bk_wifi_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226 "#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226") first.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_set_config(const [wifi_ap_config_t](#_CPPv416wifi_ap_config_t "wifi_ap_config_t") *ap_config)[](#_CPPv421bk_wifi_ap_set_configPK16wifi_ap_config_t "永久链接至目标")
:   Config the BK AP.

    Usage example:

    ```
    wifi_ap_config_t ap_config = WIFI_DEFAULT_AP_CONFIG();

    os_strncpy(ap_config.ssid, "ssid", WIFI_SSID_STR_LEN);
    os_strncpy(ap_config.password, "password", WIFI_PASSWORD_LEN);
    BK_LOG_ON_ERR(bk_wifi_ap_set_config(&ap_config));
    ```


    **Attention**
    :   1. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

    参数
    :   **ap_config** – the AP configuration

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the ap_config is NULL.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_get_config([wifi_ap_config_t](#_CPPv416wifi_ap_config_t "wifi_ap_config_t") *ap_config)[](#_CPPv421bk_wifi_ap_get_configP16wifi_ap_config_t "永久链接至目标")
:   Get the configuration of the BK AP.

    参数
    :   **ap_config** – store the configuration of BK AP

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL.

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_get_sta_list([wlan_ap_stas_t](#_CPPv414wlan_ap_stas_t "wlan_ap_stas_t") *stas)[](#_CPPv423bk_wifi_ap_get_sta_listP14wlan_ap_stas_t "永久链接至目标")
:   Get the STAs connected to BK AP.


    **Attention**
    :   Free stas->sta after usage.

    参数
    :   **stas** – store the STA list in BK AP

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_calculate_pmk(const char *ssid, const char *pwd, char *pmk)[](#_CPPv421bk_wifi_calculate_pmkPKcPKcPc "永久链接至目标")
:   Calculate softap’s Pmk when softap is starts.

    参数
    :   - **ssid** – softap’s ssid

        - **pwd** – softap’s pwd

        - **pmk** – softap’s pmk

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_add_vendor_ie(void *buf, uint8_t len)[](#_CPPv424bk_wifi_ap_add_vendor_iePv7uint8_t "永久链接至目标")
:   Add softap’s Vendor Specific IE when softap is running.


    **Attention**
    :   If you want to add vsie when softap starts, just initialize [wifi_ap_config_t](#structwifi__ap__config__t "#structwifi__ap__config__t") when call [bk_wifi_ap_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5 "#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5").

    参数
    :   - **buf** – vsie buf

        - **len** – vsie buf len

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_del_vendor_ie(void)[](#_CPPv424bk_wifi_ap_del_vendor_iev "永久链接至目标")
:   Delete softap’s Vendor Specific IE when softap is running.


    **Attention**
    :   If you want to add vsie when softap starts, just initialize [wifi_ap_config_t](#structwifi__ap__config__t "#structwifi__ap__config__t") when call [bk_wifi_ap_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5 "#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5").

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_update_hidden_cap(bool flag)[](#_CPPv428bk_wifi_ap_update_hidden_capb "永久链接至目标")
:   Update softap’s Hidden Ssid Capaility when softap is running.


    - BK_OK: succeed

    - others: other errors


    **Attention**
    :   If you want to update hidden ssid capability when softap starts, just call [bk_wifi_ap_update_hidden_cap()](#group__bk__api__wifi__v2_1ga178bace6234723471c6d00b671a998ca "#group__bk__api__wifi__v2_1ga178bace6234723471c6d00b671a998ca").

    参数
    :   **flag** – set true for hidden ssid

    返回

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_start(void)[](#_CPPv421bk_wifi_monitor_startv "永久链接至目标")
:   Start the monitor.


    **Attention**
    :   1. When monitor mode is enabled, the scan will not work and [bk_wifi_scan_start()](#group__bk__api__wifi__v2_1gaf4b85a984fa5c5d633769274a50b5b9c "#group__bk__api__wifi__v2_1gaf4b85a984fa5c5d633769274a50b5b9c") returns BK_ERR_WIFI_MONITOR_IP.

        2. When monitor mode is enabled, the STA connect will not work and [bk_wifi_sta_connect()](#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06 "#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06") returns BK_ERR_WIFI_MONITOR_IP.

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_stop(void)[](#_CPPv420bk_wifi_monitor_stopv "永久链接至目标")
:   Stop the monitor.

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_set_config(const [wifi_monitor_config_t](#_CPPv421wifi_monitor_config_t "wifi_monitor_config_t") *monitor_config)[](#_CPPv426bk_wifi_monitor_set_configPK21wifi_monitor_config_t "永久链接至目标")
:   Configure the monitor.

    参数
    :   **monitor_config** – the configuration of monitor

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_get_config([wifi_monitor_config_t](#_CPPv421wifi_monitor_config_t "wifi_monitor_config_t") *monitor_config)[](#_CPPv426bk_wifi_monitor_get_configP21wifi_monitor_config_t "永久链接至目标")
:   Get the configuration of the monitor.

    参数
    :   **monitor_config** – store the configuration of monitor

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_register_cb(const [wifi_monitor_cb_t](#_CPPv417wifi_monitor_cb_t "wifi_monitor_cb_t") monitor_cb)[](#_CPPv427bk_wifi_monitor_register_cbK17wifi_monitor_cb_t "永久链接至目标")
:   Register the user callback of monitor.

    参数
    :   **monitor_cb** – monitor callback

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_set_channel(const [wifi_channel_t](#_CPPv414wifi_channel_t "wifi_channel_t") *chan)[](#_CPPv427bk_wifi_monitor_set_channelPK14wifi_channel_t "永久链接至目标")
:   Set monitor channel.


    **Attention**
    :   1. Currently we only support HT20, chan->second should always be 0.

        2. This API is only used for settting monitor channel, NOT for other purpose.

        3. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.

        4. The channel range can be set is from channel 1 to channel 14,

    参数
    :   **chan** – channel of monitor

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_resume(void)[](#_CPPv422bk_wifi_monitor_resumev "永久链接至目标")
:   resume the monitor to wakeup Wi-Fi from sleep mode

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_suspend(void)[](#_CPPv423bk_wifi_monitor_suspendv "永久链接至目标")
:   suspend the monitor to allow Wi-Fi can goto sleep mode

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_twt_setup(uint8_t setup_type, uint16_t mantissa, uint8_t min_twt)[](#_CPPv417bk_wifi_twt_setup7uint8_t8uint16_t7uint8_t "永久链接至目标")
:   twt set up

    参数
    :   - **setup_type** – suggest/demand

        - **mantissa** – wake_int_mantissa

        - **min_twt** – min_twt_wake_dur

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_twt_teardown(void)[](#_CPPv420bk_wifi_twt_teardownv "永久链接至目标")
:   twt tear down

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_filter_set_config(const [wifi_filter_config_t](#_CPPv420wifi_filter_config_t "wifi_filter_config_t") *filter_config)[](#_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t "永久链接至目标")
:   Set the filter configuration.

    The filter is used to configure what kind of management packets can be received by the filter callback registered by [bk_wifi_filter_register_cb()](#group__bk__api__wifi__v2_1ga0276b4fd054e03c62f79e0b52b1870c0 "#group__bk__api__wifi__v2_1ga0276b4fd054e03c62f79e0b52b1870c0").

    Per the WiFi receiving data path, the management frames are firstly received by WiFi hardware, then the hardware relays them to WiFi software (WiFi driver). Normally the hardware receives all management frames in the air, however it don’t relay all of them to WiFi driver (WiFi software), it only relays management frames necessary to STA or AP or scan or monitor, depends on which interface or function are enabled. In other word, WiFi driver only receives management frames necessary to them from hardware.

    When no filter callback is registered, all management frame processing is ended in WiFi driver unless the filter callback is registered.

    If filter callback is register and if filter_config.rx_all_default_mgmt is set to 1, then all the management frames received by WiFi driver are relayed to the filter callback. **Notified that the default management frame types can be received depends on whether STA or AP or scan or monitor are enabled or not, e.g. when only STA is enabled, the WiFi driver needs to handle PROBE response, but don’t need to handle PROBE request, so the WiFi driver only receive PROBE response from WiFi hardware**.

    Here is summary about default management frame received by WiFi:

    | Condition | Default management frame |
    | --- | --- |
    | STA connected | Management frames sent by the connected AP, such as beacon etc. |
    | AP started | Management frames sent by connected STA and probe request etc. |
    | Scan starting | Probe response and beacon frames of all APs. |
    | Monitor started | All kind of management frames |

    How about if the filter callback wants to receive more management frame types, e.g. want to receive PROBE request when only STA is enabled. We can set filter_config->rx_probe_req to receive PROBE response no matter whether AP is enabled or NOT.

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
    :   1. If this API is not called, the default filter is to relay all mamangement frames received by WiFi driver to the filter callback.

        2. If STA is enabled, the WiFi driver only receives beacon from the connected AP, if scan is enabled or filter_config->rx_all_beacon is set, the WiFi driver receives beacons of all APs.

    参数
    :   **filter_config** – configuration of filter

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_filter_get_config([wifi_filter_config_t](#_CPPv420wifi_filter_config_t "wifi_filter_config_t") *filter_config)[](#_CPPv425bk_wifi_filter_get_configP20wifi_filter_config_t "永久链接至目标")
:   Get the filter configuration.

    参数
    :   **filter_config** – store configuration of filter

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_filter_register_cb(const [wifi_filter_cb_t](#_CPPv416wifi_filter_cb_t "wifi_filter_cb_t") filter_cb)[](#_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t "永久链接至目标")
:   Register the filter user callback.


    **Attention**
    :   1. If the monitor is enabled, the management packets received by filter callback can also be received by monitor callback. If this is not what we want, we can disable filter when enabling monitor, or disable monitor when enabling filter.

        2. During WiFi scan, the filter also works.

        3. Pass NULL callback or set all fields of filter_config to 0 to disable the filter.

        4. The memory used to hold the frame buffer and frame_info will be freed immediately when the callback is returned, so don’t relay them to other task. Make a copy of them and then relay to other task if necessary.

        5. Don’t do too much work in the filter callback because it’s called in WiFi driver core thread, otherwise it may impact the WiFi performance.

    参数
    :   **filter_cb** – the filter user callback

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_mac(uint8_t *mac)[](#_CPPv419bk_wifi_sta_get_macP7uint8_t "永久链接至目标")
:   Get the MAC of BK STA.


    **Attention**
    :   1. The AP’s MAC is derived from the base MAC of the system.

        2. If you want to change the MAC of AP, call bk_set_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK STA

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_get_mac(uint8_t *mac)[](#_CPPv418bk_wifi_ap_get_macP7uint8_t "永久链接至目标")
:   Get the MAC of BK AP.


    **Attention**
    :   1. The AP’s MAC is derived from the base MAC of the system.

        2. If you want to change the MAC of AP, call bk_set_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK AP

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_raw(uint8_t *buffer, int len)[](#_CPPv416bk_wifi_send_rawP7uint8_ti "永久链接至目标")
:   Send raw 802.11 frame.


    **Attention**
    :   1. This API can be used in WiFi station, softap, or monitor mode.

        2. Only support to send non-QoS frame.

        3. The frame sequence will be overwritten by WiFi driver.

        4. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **buffer** – raw 802.11 frame

        - **len** – the length of the 802.11 frame

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_raw_ex([wifi_raw_tx_info_t](#_CPPv418wifi_raw_tx_info_t "wifi_raw_tx_info_t") *raw_tx, void *cb, void *param)[](#_CPPv419bk_wifi_send_raw_exP18wifi_raw_tx_info_tPvPv "永久链接至目标")
:   Send raw 802.11 frame.


    **Attention**
    :   1. This API can be used in WiFi station, softap, or monitor mode.

        2. Only support to send non-QoS frame.

        3. The frame sequence will be overwritten by WiFi driver.

        4. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw_tx** – : raw tx information, refer to struct [wifi_raw_tx_info_t](#structwifi__raw__tx__info__t "#structwifi__raw__tx__info__t")

        - **cb** – : send status call back

        - **param** – : send status call back paramter

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_rate_power(uint32_t rate, uint32_t power)[](#_CPPv429bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t "永久链接至目标")
:   Update raw 802.11 frame TX rate and power.

    参数
    :   - **rate** – : TX rate control

        - **power** – : TX power control

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_ac(uint8_t ac)[](#_CPPv421bk_wifi_set_tx_raw_ac7uint8_t "永久链接至目标")
:   Update raw 802.11 frame TX AC.

    参数
    :   **rate** – : TX AC

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_timeout(uint16_t timeout_ms)[](#_CPPv426bk_wifi_set_tx_raw_timeout8uint16_t "永久链接至目标")
:   Update raw 802.11 frame TX timeout.

    参数
    :   **rate** – : TX timeout

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_raw_ac(uint8_t *ac)[](#_CPPv421bk_wifi_get_tx_raw_acP7uint8_t "永久链接至目标")
:   get tx raw ac info

    参数
    :   **ac** – ac info

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_raw_timeout(uint16_t *time)[](#_CPPv426bk_wifi_get_tx_raw_timeoutP8uint16_t "永久链接至目标")
:   get tx raw timeout info

    参数
    :   **time** – timeout info

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_min_rsv_mem(uint32_t mem_bytes)[](#_CPPv423bk_wifi_set_min_rsv_mem8uint32_t "永久链接至目标")
:   Update the minimux heap memory size that Wi-Fi should reserve.


    **Attention**
    :   1. An small piece of extra memory will be malloced from heap for each TX packets delivered to Wi-Fi, so if the pending TX packets are too many for some reasons, the heap memory will be occupied too much by TX packets. To ensure the stability of whole system, this interface is provied to limit the memory size for Wi-Fi TX packets.

        2. The default minimux reserved memory size is 10K bytes

    参数
    :   **mem_bytes, :** – the expected reserved memory size(bytes)

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_min_rsv_mem(uint32_t *mem_bytes)[](#_CPPv423bk_wifi_get_min_rsv_memP8uint32_t "永久链接至目标")
:   Get the minimux heap memory size that Wi-Fi currently creserves.

    参数
    :   **mem_bytes, :** – return currently reserved memory size(bytes)

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_max_msdu_cnt(uint16_t max_cnt)[](#_CPPv427bk_wifi_set_tx_max_msdu_cnt8uint16_t "永久链接至目标")
:   Update the maximum MSDU count that Wi-Fi could handle.

    参数
    :   **max_cnt, :** – the maxmimum MSDU count

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_max_msdu_cnt(uint16_t *max_cnt)[](#_CPPv427bk_wifi_get_tx_max_msdu_cntP8uint16_t "永久链接至目标")
:   Get the maximum MSDU count configuration that Wi-Fi could handle.

    参数
    :   **max_cnt, :** – return the maxmimum MSDU count

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_capa_config([wifi_capability_t](#_CPPv417wifi_capability_t "wifi_capability_t") capa_id, uint32_t capa_val)[](#_CPPv419bk_wifi_capa_config17wifi_capability_t8uint32_t "永久链接至目标")
:   Update Wi-Fi capability configuration.

    This API is used to change some Wi-Fi capability configuration, please refer to wifi_capability_t to get the capability that has been supported.


    **Attention**
    :   1. Please keep in mind that Wi-Fi behavior may change if the capability is changed to different value compared with the default value.

        2. We strongly suggest not using this API except you are very farmiliar with the Wi-Fi specification.

        3. If you want Wi-Fi working on 11b only mode, please set 11b only mode by configurate paramter capa_id with WIFI_CAPA_ID_11B_ONLY_EN and capa_val with true BEFORE connecting AP or opening SoftAP.

    参数
    :   - **capa_id, :** – the specific capability you want to change

        - **capa_val, :** – new capability value

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_country(const [wifi_country_t](#_CPPv414wifi_country_t "wifi_country_t") *country)[](#_CPPv419bk_wifi_set_countryPK14wifi_country_t "永久链接至目标")
:   configure country info


    **Attention**
    :   1. The default country is {.cc=”CN”, .schan=1, .nchan=13, policy=WIFI_COUNTRY_POLICY_AUTO}

        2. When the country policy is WIFI_COUNTRY_POLICY_AUTO, the country info of the AP to which the station is connected is used. E.g. if the configured country info is {.cc=”USA”, .schan=1, .nchan=11} and the country info of the AP to which the station is connected is {.cc=”JP”, .schan=1, .nchan=14} then the country info that will be used is {.cc=”JP”, .schan=1, .nchan=14}. If the station disconnected from the AP the country info is set back back to the country info of the station automatically, {.cc=”USA”, .schan=1, .nchan=11} in the example.

        3. When the country policy is WIFI_COUNTRY_POLICY_MANUAL, always use the configured country info.

        4. When the country info is changed because of configuration or because the station connects to a different external AP, the country IE in probe response/beacon of the soft-AP is changed also.

        5. The country configuration is not stored into flash

        6. This API doesn’t validate the per-country rules, it’s up to the user to fill in all fields according to local regulations.

    参数
    :   **country** – the configured country info

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: WiFi is not initialized

        - BK_ERR_PARAM: invalid argument

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_country([wifi_country_t](#_CPPv414wifi_country_t "wifi_country_t") *country)[](#_CPPv419bk_wifi_get_countryP14wifi_country_t "永久链接至目标")
:   get the current country info

    参数
    :   **country** – country info

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: WiFi is not initialized

        - BK_ERR_PARAM: invalid argument

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_pm_enable(void)[](#_CPPv421bk_wifi_sta_pm_enablev "永久链接至目标")
:   enable wifi sta power management

    返回
    :   - BK_OK: on succeed

        - others: real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_pm_disable(void)[](#_CPPv422bk_wifi_sta_pm_disablev "永久链接至目标")
:   disable wifi sta power management

    返回
    :   - BK_OK: on succeed

        - others: real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_channel(void)[](#_CPPv419bk_wifi_get_channelv "永久链接至目标")
:   get current channel ID

    参数
    :   **basically** – range from 1~13

    返回
    :   - BK_OK: on succeed

        - others: real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_mac_address(char *mac)[](#_CPPv423bk_wifi_set_mac_addressPc "永久链接至目标")
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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_manual_cal_rfcali_status(void)[](#_CPPv432bk_wifi_manual_cal_rfcali_statusv "永久链接至目标")
:   Get Wi-Fi Calibration status.

    返回
    :   - BK_OK: on succeed

        - others: real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_vif_probe_req_frame_cb_register(void *cb)[](#_CPPv442bk_wifi_ap_vif_probe_req_frame_cb_registerPv "永久链接至目标")
:   Register a cb of probe request for ap.

    参数
    :   **cb** – callback function of probe request to register

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_listen_interval_req(uint8_t interval)[](#_CPPv432bk_wifi_send_listen_interval_req7uint8_t "永久链接至目标")
:   Set listen interval.

    参数
    :   **any** – value is acceptable,but 1, 3, 10 is recommended.

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_statistic_info([wifi_statistics_info_t](#_CPPv422wifi_statistics_info_t "wifi_statistics_info_t") *wifiinfo)[](#_CPPv426bk_wifi_get_statistic_infoP22wifi_statistics_info_t "永久链接至目标")
:   Get wifi statistic info.

    参数
    :   **get** – wifi info from fw

    返回
    :   -BK_OK: on success -others:real error, used for future.

void bk_wifi_ota_dtim(bool is_open)[](#_CPPv416bk_wifi_ota_dtimb "永久链接至目标")
:   set wifi ps dtim info.

    参数
    :   **dtim** – 1 open or not

    返回
    :   -void.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [wifi_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wifi_types.h")


### Structures[](#structures "永久链接至标题")

struct wifi_init_config_t[](#_CPPv418wifi_init_config_t "永久链接至目标")
:   Public Members

    uint64_t features[](#_CPPv4N18wifi_init_config_t8featuresE "永久链接至目标")
    :   WiFi feature bitmaps

    uint8_t reserved[16][](#_CPPv4N18wifi_init_config_t8reservedE "永久链接至目标")
    :   Reserved

struct wifi_channel_t[](#_CPPv414wifi_channel_t "永久链接至目标")
:   Public Members

    uint8_t primary[](#_CPPv4N14wifi_channel_t7primaryE "永久链接至目标")
    :   Primary channel

    [wifi_second_channel_t](#_CPPv421wifi_second_channel_t "wifi_second_channel_t") second[](#_CPPv4N14wifi_channel_t6secondE "永久链接至目标")
    :   Secondary cahnnel

struct bk_vise[](#_CPPv47bk_vise "永久链接至目标")

struct wifi_sta_config_t[](#_CPPv417wifi_sta_config_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N17wifi_sta_config_t4ssidE "永久链接至目标")
    :   SSID of AP to be connected

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N17wifi_sta_config_t5bssidE "永久链接至目标")
    :   BSSID of AP to be connected, fast connect only

    uint8_t channel[](#_CPPv4N17wifi_sta_config_t7channelE "永久链接至目标")
    :   Primary channel of AP to be connected, fast connect only

    [wifi_security_t](#_CPPv415wifi_security_t "wifi_security_t") security[](#_CPPv4N17wifi_sta_config_t8securityE "永久链接至目标")
    :   Security of AP to be connected

    char password[WIFI_PASSWORD_LEN][](#_CPPv4N17wifi_sta_config_t8passwordE "永久链接至目标")
    :   Security key or PMK of the wlan.

    struct [bk_vise](#_CPPv47bk_vise "bk_vise") *vsies[[NUM_WIFI_VENDOR_ELEM_FRAMES](#_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE "NUM_WIFI_VENDOR_ELEM_FRAMES")][](#_CPPv4N17wifi_sta_config_t5vsiesE "永久链接至目标")
    :   Vnedor Specific IEs

    uint8_t reserved[32][](#_CPPv4N17wifi_sta_config_t8reservedE "永久链接至目标")
    :   reserved, **must set to 0**

    int auto_reconnect_count[](#_CPPv4N17wifi_sta_config_t20auto_reconnect_countE "永久链接至目标")
    :   auto reconnect max count, 0 for always reconnect

    int auto_reconnect_timeout[](#_CPPv4N17wifi_sta_config_t22auto_reconnect_timeoutE "永久链接至目标")
    :   auto reconnect timeout in secs, 0 for no timeout

    bool disable_auto_reconnect_after_disconnect[](#_CPPv4N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE "永久链接至目标")
    :   disable auto reconnect if deauth/disassoc by AP when in connected state

struct wifi_linkstate_reason_t[](#_CPPv423wifi_linkstate_reason_t "永久链接至目标")
:   Public Members

    [wifi_link_state_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state[](#_CPPv4N23wifi_linkstate_reason_t5stateE "永久链接至目标")
    :   Wifi linkstate

    [wifi_err_reason_t](#_CPPv417wifi_err_reason_t "wifi_err_reason_t") reason_code[](#_CPPv4N23wifi_linkstate_reason_t11reason_codeE "永久链接至目标")
    :   Wifi disconnect reason code, success will be WIFI_REASON_MAX

struct wifi_link_status_t[](#_CPPv418wifi_link_status_t "永久链接至目标")
:   Public Members

    [wifi_link_state_t](#_CPPv417wifi_link_state_t "wifi_link_state_t") state[](#_CPPv4N18wifi_link_status_t5stateE "永久链接至目标")
    :   The WiFi connection status

    int aid[](#_CPPv4N18wifi_link_status_t3aidE "永久链接至目标")
    :   STA AID

    int rssi[](#_CPPv4N18wifi_link_status_t4rssiE "永久链接至目标")
    :   The RSSI of AP the BK STA is connected

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N18wifi_link_status_t4ssidE "永久链接至目标")
    :   SSID of AP the BK STA is connected

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N18wifi_link_status_t5bssidE "永久链接至目标")
    :   BSSID of AP the BK STA is connected

    uint8_t channel[](#_CPPv4N18wifi_link_status_t7channelE "永久链接至目标")
    :   Primary channel of AP the BK STA is connected

    [wifi_security_t](#_CPPv415wifi_security_t "wifi_security_t") security[](#_CPPv4N18wifi_link_status_t8securityE "永久链接至目标")
    :   Security of AP the BK STA is connected

    char password[WIFI_PASSWORD_LEN][](#_CPPv4N18wifi_link_status_t8passwordE "永久链接至目标")
    :   Passord of AP the BK STA is connected

struct wifi_scan_config_t[](#_CPPv418wifi_scan_config_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N18wifi_scan_config_t4ssidE "永久链接至目标")
    :   SSID to be scaned

    uint8_t reserved[16][](#_CPPv4N18wifi_scan_config_t8reservedE "永久链接至目标")
    :   Reserved fields, **must be zero**

struct wifi_scan_ap_info_t[](#_CPPv419wifi_scan_ap_info_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N19wifi_scan_ap_info_t4ssidE "永久链接至目标")
    :   SSID of AP found by scan

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N19wifi_scan_ap_info_t5bssidE "永久链接至目标")
    :   BSSID of AP found by scan

    int rssi[](#_CPPv4N19wifi_scan_ap_info_t4rssiE "永久链接至目标")
    :   RSSI of AP found by scan

    uint8_t channel[](#_CPPv4N19wifi_scan_ap_info_t7channelE "永久链接至目标")
    :   The channel of the AP found by scan

    [wifi_security_t](#_CPPv415wifi_security_t "wifi_security_t") security[](#_CPPv4N19wifi_scan_ap_info_t8securityE "永久链接至目标")
    :   The security type of the AP found by scan

    uint8_t reserved[16][](#_CPPv4N19wifi_scan_ap_info_t8reservedE "永久链接至目标")
    :   Reserved, **must be zero**

struct wifi_scan_result_t[](#_CPPv418wifi_scan_result_t "永久链接至目标")
:   Public Members

    int ap_num[](#_CPPv4N18wifi_scan_result_t6ap_numE "永久链接至目标")
    :   The number of AP found by scan

    [wifi_scan_ap_info_t](#_CPPv419wifi_scan_ap_info_t "wifi_scan_ap_info_t") *aps[](#_CPPv4N18wifi_scan_result_t3apsE "永久链接至目标")
    :   The APs found by scan

struct wifi_ap_config_t[](#_CPPv416wifi_ap_config_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N16wifi_ap_config_t4ssidE "永久链接至目标")
    :   The SSID of BK AP

    char password[WIFI_PASSWORD_LEN][](#_CPPv4N16wifi_ap_config_t8passwordE "永久链接至目标")
    :   Password of BK AP, ignored in an open system.

    uint8_t channel[](#_CPPv4N16wifi_ap_config_t7channelE "永久链接至目标")
    :   The channel of BK AP, 0 indicates default TODO

    [wifi_security_t](#_CPPv415wifi_security_t "wifi_security_t") security[](#_CPPv4N16wifi_ap_config_t8securityE "永久链接至目标")
    :   Security type of BK AP, default value TODO

    uint8_t hidden[](#_CPPv4N16wifi_ap_config_t6hiddenE "永久链接至目标")
    :   Whether the BK AP is hidden

    uint8_t acs[](#_CPPv4N16wifi_ap_config_t3acsE "永久链接至目标")
    :   Whether Auto Channel Selection is enabled

    uint8_t vsie_len[](#_CPPv4N16wifi_ap_config_t8vsie_lenE "永久链接至目标")
    :   Beacon/ProbeResp Vendor Specific IE len

    uint8_t vsie[255][](#_CPPv4N16wifi_ap_config_t4vsieE "永久链接至目标")
    :   Beacon/ProbeResp Vendor Specific IE

    uint8_t max_con[](#_CPPv4N16wifi_ap_config_t7max_conE "永久链接至目标")
    :   Max number of stations allowed to connect to BK AP, TODO default value?

    uint8_t max_statype_num[4][](#_CPPv4N16wifi_ap_config_t15max_statype_numE "永久链接至目标")
    :   Max number of different station types allowed to connect to BK AP

    uint8_t reserved[32][](#_CPPv4N16wifi_ap_config_t8reservedE "永久链接至目标")
    :   Reserved, **must be zero**

struct wlan_ap_sta[](#_CPPv411wlan_ap_sta "永久链接至目标")
:   Wlan station information definition.

struct wlan_ap_stas[](#_CPPv412wlan_ap_stas "永久链接至目标")
:   Wlan connected stations information definition.

struct wlan_ap_vsie[](#_CPPv412wlan_ap_vsie "永久链接至目标")
:   softap beacon/probe response’s vendor IEs Dynamic change softap’s vendor specific IEs.

struct wlan_sta_vsie[](#_CPPv413wlan_sta_vsie "永久链接至目标")
:   STA vendor IEs for (re)assoc, scan, p2p, p2p go, etc. Dynamic change STA’s vendor specific IEs.

struct wifi_monitor_config_t[](#_CPPv421wifi_monitor_config_t "永久链接至目标")
:   Public Members

    uint32_t rx_mcast_frame[](#_CPPv4N21wifi_monitor_config_t14rx_mcast_frameE "永久链接至目标")
    :   Set this bit to enable callback to receive multicast/broadcast

    uint32_t rx_dup_frame[](#_CPPv4N21wifi_monitor_config_t12rx_dup_frameE "永久链接至目标")
    :   Set this bit to enable callback to receive the duplicated

    uint32_t reserved[](#_CPPv4N21wifi_monitor_config_t8reservedE "永久链接至目标")
    :   Reserved bits, **must set to 0**

struct wifi_frame_info_t[](#_CPPv417wifi_frame_info_t "永久链接至目标")
:   Public Members

    int rssi[](#_CPPv4N17wifi_frame_info_t4rssiE "永久链接至目标")
    :   RSSI of the received frame in monitor mode

struct wifi_filter_config_t[](#_CPPv420wifi_filter_config_t "永久链接至目标")
:   Public Members

    uint32_t rx_all_default_mgmt[](#_CPPv4N20wifi_filter_config_t19rx_all_default_mgmtE "永久链接至目标")
    :   Set the bit to enable the callback to receive all management frame recived by WiFi driver

    uint32_t rx_probe_req[](#_CPPv4N20wifi_filter_config_t12rx_probe_reqE "永久链接至目标")
    :   Set the bit to enable the callback to receive probe request

    uint32_t rx_probe_rsp[](#_CPPv4N20wifi_filter_config_t12rx_probe_rspE "永久链接至目标")
    :   Set the bit to enable the callback to receive probe response

    uint32_t rx_all_beacon[](#_CPPv4N20wifi_filter_config_t13rx_all_beaconE "永久链接至目标")
    :   Set the bit to enable the callback to receive all beacon

    uint32_t rx_action[](#_CPPv4N20wifi_filter_config_t9rx_actionE "永久链接至目标")
    :   Set the bit to enable the callback to receive action frame

    uint32_t reserved[](#_CPPv4N20wifi_filter_config_t8reservedE "永久链接至目标")
    :   Reserved bits, **must set to 0**

struct wifi_country_t[](#_CPPv414wifi_country_t "永久链接至目标")
:   Public Members

    char cc[3][](#_CPPv4N14wifi_country_t2ccE "永久链接至目标")
    :   country code string

    uint8_t schan[](#_CPPv4N14wifi_country_t5schanE "永久链接至目标")
    :   start channel

    uint8_t nchan[](#_CPPv4N14wifi_country_t5nchanE "永久链接至目标")
    :   total channel number

    int8_t max_tx_power[](#_CPPv4N14wifi_country_t12max_tx_powerE "永久链接至目标")
    :   maximum tx power

    [wifi_country_policy_t](#_CPPv421wifi_country_policy_t "wifi_country_policy_t") policy[](#_CPPv4N14wifi_country_t6policyE "永久链接至目标")
    :   country policy

struct wifi_event_scan_done_t[](#_CPPv422wifi_event_scan_done_t "永久链接至目标")
:   Public Members

    uint32_t scan_id[](#_CPPv4N22wifi_event_scan_done_t7scan_idE "永久链接至目标")
    :   Scan ID

struct wifi_event_sta_connected_t[](#_CPPv426wifi_event_sta_connected_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N26wifi_event_sta_connected_t4ssidE "永久链接至目标")
    :   SSID of connected AP

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N26wifi_event_sta_connected_t5bssidE "永久链接至目标")
    :   BSSID of connected AP

struct wifi_event_sta_disconnected_t[](#_CPPv429wifi_event_sta_disconnected_t "永久链接至目标")
:   Public Members

    int disconnect_reason[](#_CPPv4N29wifi_event_sta_disconnected_t17disconnect_reasonE "永久链接至目标")
    :   Disconnect reason of BK STA

    bool local_generated[](#_CPPv4N29wifi_event_sta_disconnected_t15local_generatedE "永久链接至目标")
    :   if disconnect is request by local

struct wifi_event_ap_connected_t[](#_CPPv425wifi_event_ap_connected_t "永久链接至目标")
:   Public Members

    uint8_t mac[WIFI_MAC_LEN][](#_CPPv4N25wifi_event_ap_connected_t3macE "永久链接至目标")
    :   MAC of the STA connected to the BK AP

struct wifi_event_ap_disconnected_t[](#_CPPv428wifi_event_ap_disconnected_t "永久链接至目标")
:   Public Members

    uint8_t mac[WIFI_MAC_LEN][](#_CPPv4N28wifi_event_ap_disconnected_t3macE "永久链接至目标")
    :   MAC of the STA disconnected from the BK AP

struct wifi_statistics_info_t[](#_CPPv422wifi_statistics_info_t "永久链接至目标")
:   Wi-Fi Statistic info.

    Public Members

    uint32_t tx_success_count[](#_CPPv4N22wifi_statistics_info_t16tx_success_countE "永久链接至目标")
    :   Number of TX successes, 0 if unavailable

    uint32_t tx_retry_count[](#_CPPv4N22wifi_statistics_info_t14tx_retry_countE "永久链接至目标")
    :   Number of TX retries, 0 if unavailable

    uint32_t tx_fail_count[](#_CPPv4N22wifi_statistics_info_t13tx_fail_countE "永久链接至目标")
    :   Number of TX failures, 0 if unavailable

    uint32_t rx_success_count[](#_CPPv4N22wifi_statistics_info_t16rx_success_countE "永久链接至目标")
    :   Number of RX successes, 0 if unavailable

    uint32_t rx_crcerror_count[](#_CPPv4N22wifi_statistics_info_t17rx_crcerror_countE "永久链接至目标")
    :   Number of RX FCS errors, 0 if unavailable

    uint32_t mic_error_count[](#_CPPv4N22wifi_statistics_info_t15mic_error_countE "永久链接至目标")
    :   Number of MIC errors, 0 if unavailable

    int8_t noise[](#_CPPv4N22wifi_statistics_info_t5noiseE "永久链接至目标")
    :   Average noise level in dBm, -128 if unavailable

    uint16_t phyrate[](#_CPPv4N22wifi_statistics_info_t7phyrateE "永久链接至目标")
    :   Maximum used PHY rate, 0 if unavailable

    uint16_t txrate[](#_CPPv4N22wifi_statistics_info_t6txrateE "永久链接至目标")
    :   Average used TX rate, 0 if unavailable

    uint16_t rxrate[](#_CPPv4N22wifi_statistics_info_t6rxrateE "永久链接至目标")
    :   Average used RX rate, 0 if unavailable

    int8_t rssi[](#_CPPv4N22wifi_statistics_info_t4rssiE "永久链接至目标")
    :   Average beacon RSSI in dBm, -128 if unavailable

    uint8_t bandwidth[](#_CPPv4N22wifi_statistics_info_t9bandwidthE "永久链接至目标")
    :   Average used bandwidth, 0 if unavailable

    uint8_t idle_time_per[](#_CPPv4N22wifi_statistics_info_t13idle_time_perE "永久链接至目标")
    :   Percent of idle time, 0 if unavailable

struct raw_tx_cntrl_t[](#_CPPv414raw_tx_cntrl_t "永久链接至目标")
:   Wi-Fi RAW TX control.

    Public Members

    uint32_t tx_rate[](#_CPPv4N14raw_tx_cntrl_t7tx_rateE "永久链接至目标")
    :   RAW Data TX rate information

    uint32_t tx_power[](#_CPPv4N14raw_tx_cntrl_t8tx_powerE "永久链接至目标")
    :   RAW Data TX power information

    uint32_t tx_retry_cnt[](#_CPPv4N14raw_tx_cntrl_t12tx_retry_cntE "永久链接至目标")
    :   RAW Data TX retry count

struct wifi_raw_tx_info_t[](#_CPPv418wifi_raw_tx_info_t "永久链接至目标")
:   Wi-Fi RAW TX control.

    Public Members

    uint8_t *pkt[](#_CPPv4N18wifi_raw_tx_info_t3pktE "永久链接至目标")
    :   RAW data tx packet address

    int len[](#_CPPv4N18wifi_raw_tx_info_t3lenE "永久链接至目标")
    :   RAW data tx packet length

    [raw_tx_cntrl_t](#_CPPv414raw_tx_cntrl_t "raw_tx_cntrl_t") tx_cntrl[](#_CPPv4N18wifi_raw_tx_info_t8tx_cntrlE "永久链接至目标")
    :   RAW data tx control information


### Macros[](#macros "永久链接至标题")

BK_ERR_WIFI_NOT_INIT[](#c.BK_ERR_WIFI_NOT_INIT "永久链接至目标")
:   WiFi is not initialized, call [bk_wifi_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226 "#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226") to init the WiFi

BK_ERR_WIFI_STA_NOT_STARTED[](#c.BK_ERR_WIFI_STA_NOT_STARTED "永久链接至目标")
:   STA is not started, call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") to start the STA

BK_ERR_WIFI_AP_NOT_STARTED[](#c.BK_ERR_WIFI_AP_NOT_STARTED "永久链接至目标")
:   AP is not initialized, call [bk_wifi_ap_start()](#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5 "#group__bk__api__wifi__v2_1ga664be1db35e4ef799f2178bfc466a2e5") to start the AP

BK_ERR_WIFI_CHAN_RANGE[](#c.BK_ERR_WIFI_CHAN_RANGE "永久链接至目标")
:   Invalid channel range

BK_ERR_WIFI_COUNTRY_POLICY[](#c.BK_ERR_WIFI_COUNTRY_POLICY "永久链接至目标")
:   Invalid country policy

BK_ERR_WIFI_RESERVED_FIELD[](#c.BK_ERR_WIFI_RESERVED_FIELD "永久链接至目标")
:   Reserved fields not 0

BK_ERR_WIFI_MONITOR_IP[](#c.BK_ERR_WIFI_MONITOR_IP "永久链接至目标")
:   Monitor is in progress

BK_ERR_WIFI_STA_NOT_CONFIG[](#c.BK_ERR_WIFI_STA_NOT_CONFIG "永久链接至目标")
:   STA is not configured, call bk_wifi_sta_config() to configure it

BK_ERR_WIFI_AP_NOT_CONFIG[](#c.BK_ERR_WIFI_AP_NOT_CONFIG "永久链接至目标")
:   AP is not configured, call bk_wifi_ap_config() to configure it

BK_ERR_WIFI_DRIVER[](#c.BK_ERR_WIFI_DRIVER "永久链接至目标")
:   Internal WiFi driver error

BK_ERR_WIFI_MONITOR_ENTER[](#c.BK_ERR_WIFI_MONITOR_ENTER "永久链接至目标")
:   WiFi failed to enter monitor mode

BK_ERR_WIFI_DRIVER_DEL_VIF[](#c.BK_ERR_WIFI_DRIVER_DEL_VIF "永久链接至目标")
:   WiFi driver failed to delete WiFi virtual interface

BK_ERR_WIFI_DRIVER_AP_START[](#c.BK_ERR_WIFI_DRIVER_AP_START "永久链接至目标")
:   WiFi driver failed to start BK AP

BK_ERR_WIFI_CHAN_NUMBER[](#c.BK_ERR_WIFI_CHAN_NUMBER "永久链接至目标")
:   Invalid channel number

WIFI_MIN_CHAN_NUM[](#c.WIFI_MIN_CHAN_NUM "永久链接至目标")
:   Minimum supported channel number

WIFI_MAX_CHAN_NUM[](#c.WIFI_MAX_CHAN_NUM "永久链接至目标")
:   Maximum supported channel number

WIFI_SSID_STR_LEN[](#c.WIFI_SSID_STR_LEN "永久链接至目标")
:   Maximum **NULL-terminated** WiFi SSID length

WIFI_BSSID_LEN[](#c.WIFI_BSSID_LEN "永久链接至目标")
:   Length of BSSID

WIFI_MAC_LEN[](#c.WIFI_MAC_LEN "永久链接至目标")
:   Length of MAC

WIFI_PASSWORD_LEN[](#c.WIFI_PASSWORD_LEN "永久链接至目标")
:   Maximum **NULL-terminated** WiFi password length

WIFI_DEFAULT_INIT_CONFIG()[](#c.WIFI_DEFAULT_INIT_CONFIG "永久链接至目标")
:   default init configuration

WIFI_DEFAULT_STA_CONFIG()[](#c.WIFI_DEFAULT_STA_CONFIG "永久链接至目标")
:   default STA configuration

WIFI_DEFAULT_AP_CONFIG()[](#c.WIFI_DEFAULT_AP_CONFIG "永久链接至目标")
:   default AP configuration

WIFI_DEFAULT_SCAN_CONFIG()[](#c.WIFI_DEFAULT_SCAN_CONFIG "永久链接至目标")
:   default Scan configuration

WIFI_DEFAULT_FILTER_CONFIG()[](#c.WIFI_DEFAULT_FILTER_CONFIG "永久链接至目标")
:   default Filter configuration

BK_MAX_STA_TYPE[](#c.BK_MAX_STA_TYPE "永久链接至目标")

OUI_BEKEN[](#c.OUI_BEKEN "永久链接至目标")

WLAN_EID_VENDOR_SPECIFIC[](#c.WLAN_EID_VENDOR_SPECIFIC "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef enum [sta_type](#_CPPv48sta_type "sta_type") BK_STA_TYPE[](#_CPPv411BK_STA_TYPE "永久链接至目标")

typedef struct [wlan_ap_sta](#_CPPv411wlan_ap_sta "wlan_ap_sta") wlan_ap_sta_t[](#_CPPv413wlan_ap_sta_t "永久链接至目标")
:   Wlan station information definition.

typedef struct [wlan_ap_stas](#_CPPv412wlan_ap_stas "wlan_ap_stas") wlan_ap_stas_t[](#_CPPv414wlan_ap_stas_t "永久链接至目标")
:   Wlan connected stations information definition.

typedef struct [wlan_ap_vsie](#_CPPv412wlan_ap_vsie "wlan_ap_vsie") wlan_ap_vsie_t[](#_CPPv414wlan_ap_vsie_t "永久链接至目标")
:   softap beacon/probe response’s vendor IEs Dynamic change softap’s vendor specific IEs.

typedef struct [wlan_sta_vsie](#_CPPv413wlan_sta_vsie "wlan_sta_vsie") wlan_sta_vsie_t[](#_CPPv415wlan_sta_vsie_t "永久链接至目标")
:   STA vendor IEs for (re)assoc, scan, p2p, p2p go, etc. Dynamic change STA’s vendor specific IEs.

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_monitor_cb_t)(const uint8_t *frame, uint32_t len, const [wifi_frame_info_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") *frame_info)[](#_CPPv417wifi_monitor_cb_t "永久链接至目标")
:   Monitor callback to receive frames relayed by WiFi driver.


    **Attention**
    :   1. The memory of frame and frame_info will be freed immediately when the callback is returned. If we want to use the frame or frame_info in other task, make a copy of them and handle them accordingly.

        2. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_filter_cb_t)(const uint8_t *frame, uint32_t len, const [wifi_frame_info_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") *frame_info)[](#_CPPv416wifi_filter_cb_t "永久链接至目标")
:   Filter callback to receive frames relayed by WiFi driver.


    **Attention**
    :   1. The memory of frame and frame_info will be freed immediately when the callback is returned. If we want to use the frame or frame_info in other task, make a copy of them and handle them accordingly.

        2. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.


### Enumerations[](#enumerations "永久链接至标题")

enum wifi_event_t[](#_CPPv412wifi_event_t "永久链接至目标")
:   WiFi public event type.


    *Values:*

    enumerator EVENT_WIFI_SCAN_DONE[](#_CPPv4N12wifi_event_t20EVENT_WIFI_SCAN_DONEE "永久链接至目标")
    :   WiFi scan done event

    enumerator EVENT_WIFI_STA_CONNECTED[](#_CPPv4N12wifi_event_t24EVENT_WIFI_STA_CONNECTEDE "永久链接至目标")
    :   The BK STA is connected

    enumerator EVENT_WIFI_STA_DISCONNECTED[](#_CPPv4N12wifi_event_t27EVENT_WIFI_STA_DISCONNECTEDE "永久链接至目标")
    :   The BK STA is disconnected

    enumerator EVENT_WIFI_AP_CONNECTED[](#_CPPv4N12wifi_event_t23EVENT_WIFI_AP_CONNECTEDE "永久链接至目标")
    :   A STA is connected to the BK AP

    enumerator EVENT_WIFI_AP_DISCONNECTED[](#_CPPv4N12wifi_event_t26EVENT_WIFI_AP_DISCONNECTEDE "永久链接至目标")
    :   A STA is disconnected from the BK AP

    enumerator EVENT_WIFI_COUNT[](#_CPPv4N12wifi_event_t16EVENT_WIFI_COUNTE "永久链接至目标")
    :   WiFi event count

enum wifi_err_reason_t[](#_CPPv417wifi_err_reason_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_REASON_UNSPECIFIED[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_UNSPECIFIEDE "永久链接至目标")

    enumerator WIFI_REASON_PREV_AUTH_NOT_VALID[](#_CPPv4N17wifi_err_reason_t31WIFI_REASON_PREV_AUTH_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_DEAUTH_LEAVING[](#_CPPv4N17wifi_err_reason_t26WIFI_REASON_DEAUTH_LEAVINGE "永久链接至目标")

    enumerator WIFI_REASON_DISASSOC_DUE_TO_INACTIVITY[](#_CPPv4N17wifi_err_reason_t38WIFI_REASON_DISASSOC_DUE_TO_INACTIVITYE "永久链接至目标")

    enumerator WIFI_REASON_DISASSOC_AP_BUSY[](#_CPPv4N17wifi_err_reason_t28WIFI_REASON_DISASSOC_AP_BUSYE "永久链接至目标")

    enumerator WIFI_REASON_CLASS2_FRAME_FROM_NONAUTH_STA[](#_CPPv4N17wifi_err_reason_t41WIFI_REASON_CLASS2_FRAME_FROM_NONAUTH_STAE "永久链接至目标")

    enumerator WIFI_REASON_CLASS3_FRAME_FROM_NONASSOC_STA[](#_CPPv4N17wifi_err_reason_t42WIFI_REASON_CLASS3_FRAME_FROM_NONASSOC_STAE "永久链接至目标")

    enumerator WIFI_REASON_DISASSOC_STA_HAS_LEFT[](#_CPPv4N17wifi_err_reason_t33WIFI_REASON_DISASSOC_STA_HAS_LEFTE "永久链接至目标")

    enumerator WIFI_REASON_STA_REQ_ASSOC_WITHOUT_AUTH[](#_CPPv4N17wifi_err_reason_t38WIFI_REASON_STA_REQ_ASSOC_WITHOUT_AUTHE "永久链接至目标")

    enumerator WIFI_REASON_PWR_CAPABILITY_NOT_VALID[](#_CPPv4N17wifi_err_reason_t36WIFI_REASON_PWR_CAPABILITY_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_SUPPORTED_CHANNEL_NOT_VALID[](#_CPPv4N17wifi_err_reason_t39WIFI_REASON_SUPPORTED_CHANNEL_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_BSS_TRANSITION_DISASSOC[](#_CPPv4N17wifi_err_reason_t35WIFI_REASON_BSS_TRANSITION_DISASSOCE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_IE[](#_CPPv4N17wifi_err_reason_t22WIFI_REASON_INVALID_IEE "永久链接至目标")

    enumerator WIFI_REASON_MICHAEL_MIC_FAILURE[](#_CPPv4N17wifi_err_reason_t31WIFI_REASON_MICHAEL_MIC_FAILUREE "永久链接至目标")

    enumerator WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT[](#_CPPv4N17wifi_err_reason_t34WIFI_REASON_4WAY_HANDSHAKE_TIMEOUTE "永久链接至目标")

    enumerator WIFI_REASON_GROUP_KEY_UPDATE_TIMEOUT[](#_CPPv4N17wifi_err_reason_t36WIFI_REASON_GROUP_KEY_UPDATE_TIMEOUTE "永久链接至目标")

    enumerator WIFI_REASON_IE_IN_4WAY_DIFFERS[](#_CPPv4N17wifi_err_reason_t30WIFI_REASON_IE_IN_4WAY_DIFFERSE "永久链接至目标")

    enumerator WIFI_REASON_GROUP_CIPHER_NOT_VALID[](#_CPPv4N17wifi_err_reason_t34WIFI_REASON_GROUP_CIPHER_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_PAIRWISE_CIPHER_NOT_VALID[](#_CPPv4N17wifi_err_reason_t37WIFI_REASON_PAIRWISE_CIPHER_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_AKMP_NOT_VALID[](#_CPPv4N17wifi_err_reason_t26WIFI_REASON_AKMP_NOT_VALIDE "永久链接至目标")

    enumerator WIFI_REASON_UNSUPPORTED_RSN_IE_VERSION[](#_CPPv4N17wifi_err_reason_t38WIFI_REASON_UNSUPPORTED_RSN_IE_VERSIONE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_RSN_IE_CAPAB[](#_CPPv4N17wifi_err_reason_t32WIFI_REASON_INVALID_RSN_IE_CAPABE "永久链接至目标")

    enumerator WIFI_REASON_IEEE_802_1X_AUTH_FAILED[](#_CPPv4N17wifi_err_reason_t35WIFI_REASON_IEEE_802_1X_AUTH_FAILEDE "永久链接至目标")

    enumerator WIFI_REASON_CIPHER_SUITE_REJECTED[](#_CPPv4N17wifi_err_reason_t33WIFI_REASON_CIPHER_SUITE_REJECTEDE "永久链接至目标")

    enumerator WIFI_REASON_TDLS_TEARDOWN_UNREACHABLE[](#_CPPv4N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNREACHABLEE "永久链接至目标")

    enumerator WIFI_REASON_TDLS_TEARDOWN_UNSPECIFIED[](#_CPPv4N17wifi_err_reason_t37WIFI_REASON_TDLS_TEARDOWN_UNSPECIFIEDE "永久链接至目标")

    enumerator WIFI_REASON_SSP_REQUESTED_DISASSOC[](#_CPPv4N17wifi_err_reason_t34WIFI_REASON_SSP_REQUESTED_DISASSOCE "永久链接至目标")

    enumerator WIFI_REASON_NO_SSP_ROAMING_AGREEMENT[](#_CPPv4N17wifi_err_reason_t36WIFI_REASON_NO_SSP_ROAMING_AGREEMENTE "永久链接至目标")

    enumerator WIFI_REASON_BAD_CIPHER_OR_AKM[](#_CPPv4N17wifi_err_reason_t29WIFI_REASON_BAD_CIPHER_OR_AKME "永久链接至目标")

    enumerator WIFI_REASON_NOT_AUTHORIZED_THIS_LOCATION[](#_CPPv4N17wifi_err_reason_t40WIFI_REASON_NOT_AUTHORIZED_THIS_LOCATIONE "永久链接至目标")

    enumerator WIFI_REASON_SERVICE_CHANGE_PRECLUDES_TS[](#_CPPv4N17wifi_err_reason_t39WIFI_REASON_SERVICE_CHANGE_PRECLUDES_TSE "永久链接至目标")

    enumerator WIFI_REASON_UNSPECIFIED_QOS_REASON[](#_CPPv4N17wifi_err_reason_t34WIFI_REASON_UNSPECIFIED_QOS_REASONE "永久链接至目标")

    enumerator WIFI_REASON_NOT_ENOUGH_BANDWIDTH[](#_CPPv4N17wifi_err_reason_t32WIFI_REASON_NOT_ENOUGH_BANDWIDTHE "永久链接至目标")

    enumerator WIFI_REASON_DISASSOC_LOW_ACK[](#_CPPv4N17wifi_err_reason_t28WIFI_REASON_DISASSOC_LOW_ACKE "永久链接至目标")

    enumerator WIFI_REASON_EXCEEDED_TXOP[](#_CPPv4N17wifi_err_reason_t25WIFI_REASON_EXCEEDED_TXOPE "永久链接至目标")

    enumerator WIFI_REASON_STA_LEAVING[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_STA_LEAVINGE "永久链接至目标")

    enumerator WIFI_REASON_END_TS_BA_DLS[](#_CPPv4N17wifi_err_reason_t25WIFI_REASON_END_TS_BA_DLSE "永久链接至目标")

    enumerator WIFI_REASON_UNKNOWN_TS_BA[](#_CPPv4N17wifi_err_reason_t25WIFI_REASON_UNKNOWN_TS_BAE "永久链接至目标")

    enumerator WIFI_REASON_TIMEOUT[](#_CPPv4N17wifi_err_reason_t19WIFI_REASON_TIMEOUTE "永久链接至目标")

    enumerator WIFI_REASON_PEERKEY_MISMATCH[](#_CPPv4N17wifi_err_reason_t28WIFI_REASON_PEERKEY_MISMATCHE "永久链接至目标")

    enumerator WIFI_REASON_AUTHORIZED_ACCESS_LIMIT_REACHED[](#_CPPv4N17wifi_err_reason_t43WIFI_REASON_AUTHORIZED_ACCESS_LIMIT_REACHEDE "永久链接至目标")

    enumerator WIFI_REASON_EXTERNAL_SERVICE_REQUIREMENTS[](#_CPPv4N17wifi_err_reason_t41WIFI_REASON_EXTERNAL_SERVICE_REQUIREMENTSE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_FT_ACTION_FRAME_COUNT[](#_CPPv4N17wifi_err_reason_t41WIFI_REASON_INVALID_FT_ACTION_FRAME_COUNTE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_PMKID[](#_CPPv4N17wifi_err_reason_t25WIFI_REASON_INVALID_PMKIDE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_MDE[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_INVALID_MDEE "永久链接至目标")

    enumerator WIFI_REASON_INVALID_FTE[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_INVALID_FTEE "永久链接至目标")

    enumerator WIFI_REASON_MESH_PEERING_CANCELLED[](#_CPPv4N17wifi_err_reason_t34WIFI_REASON_MESH_PEERING_CANCELLEDE "永久链接至目标")

    enumerator WIFI_REASON_MESH_MAX_PEERS[](#_CPPv4N17wifi_err_reason_t26WIFI_REASON_MESH_MAX_PEERSE "永久链接至目标")

    enumerator WIFI_REASON_MESH_CONFIG_POLICY_VIOLATION[](#_CPPv4N17wifi_err_reason_t40WIFI_REASON_MESH_CONFIG_POLICY_VIOLATIONE "永久链接至目标")

    enumerator WIFI_REASON_MESH_CLOSE_RCVD[](#_CPPv4N17wifi_err_reason_t27WIFI_REASON_MESH_CLOSE_RCVDE "永久链接至目标")

    enumerator WIFI_REASON_MESH_MAX_RETRIES[](#_CPPv4N17wifi_err_reason_t28WIFI_REASON_MESH_MAX_RETRIESE "永久链接至目标")

    enumerator WIFI_REASON_MESH_CONFIRM_TIMEOUT[](#_CPPv4N17wifi_err_reason_t32WIFI_REASON_MESH_CONFIRM_TIMEOUTE "永久链接至目标")

    enumerator WIFI_REASON_MESH_INVALID_GTK[](#_CPPv4N17wifi_err_reason_t28WIFI_REASON_MESH_INVALID_GTKE "永久链接至目标")

    enumerator WIFI_REASON_MESH_INCONSISTENT_PARAMS[](#_CPPv4N17wifi_err_reason_t36WIFI_REASON_MESH_INCONSISTENT_PARAMSE "永久链接至目标")

    enumerator WIFI_REASON_MESH_INVALID_SECURITY_CAP[](#_CPPv4N17wifi_err_reason_t37WIFI_REASON_MESH_INVALID_SECURITY_CAPE "永久链接至目标")

    enumerator WIFI_REASON_MESH_PATH_ERROR_NO_PROXY_INFO[](#_CPPv4N17wifi_err_reason_t41WIFI_REASON_MESH_PATH_ERROR_NO_PROXY_INFOE "永久链接至目标")

    enumerator WIFI_REASON_MESH_PATH_ERROR_NO_FORWARDING_INFO[](#_CPPv4N17wifi_err_reason_t46WIFI_REASON_MESH_PATH_ERROR_NO_FORWARDING_INFOE "永久链接至目标")

    enumerator WIFI_REASON_MESH_PATH_ERROR_DEST_UNREACHABLE[](#_CPPv4N17wifi_err_reason_t44WIFI_REASON_MESH_PATH_ERROR_DEST_UNREACHABLEE "永久链接至目标")

    enumerator WIFI_REASON_MAC_ADDRESS_ALREADY_EXISTS_IN_MBSS[](#_CPPv4N17wifi_err_reason_t46WIFI_REASON_MAC_ADDRESS_ALREADY_EXISTS_IN_MBSSE "永久链接至目标")

    enumerator WIFI_REASON_MESH_CHANNEL_SWITCH_REGULATORY_REQ[](#_CPPv4N17wifi_err_reason_t46WIFI_REASON_MESH_CHANNEL_SWITCH_REGULATORY_REQE "永久链接至目标")

    enumerator WIFI_REASON_MESH_CHANNEL_SWITCH_UNSPECIFIED[](#_CPPv4N17wifi_err_reason_t43WIFI_REASON_MESH_CHANNEL_SWITCH_UNSPECIFIEDE "永久链接至目标")

    enumerator WIFI_REASON_BEACON_LOST[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_BEACON_LOSTE "永久链接至目标")
    :   The BK STA can’t detect the beacon of the connected AP

    enumerator WIFI_REASON_NO_AP_FOUND[](#_CPPv4N17wifi_err_reason_t23WIFI_REASON_NO_AP_FOUNDE "永久链接至目标")
    :   Can’t find the target AP

    enumerator WIFI_REASON_WRONG_PASSWORD[](#_CPPv4N17wifi_err_reason_t26WIFI_REASON_WRONG_PASSWORDE "永久链接至目标")
    :   The password is wrong

    enumerator WIFI_REASON_DISCONNECT_BY_APP[](#_CPPv4N17wifi_err_reason_t29WIFI_REASON_DISCONNECT_BY_APPE "永久链接至目标")
    :   The BK STA disconnected by application

    enumerator WIFI_REASON_DHCP_TIMEOUT[](#_CPPv4N17wifi_err_reason_t24WIFI_REASON_DHCP_TIMEOUTE "永久链接至目标")
    :   The BK STA dhcp timeout, 20s

    enumerator WIFI_REASON_MAX[](#_CPPv4N17wifi_err_reason_t15WIFI_REASON_MAXE "永久链接至目标")
    :   The BK STA connect success

enum wifi_security_t[](#_CPPv415wifi_security_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_SECURITY_NONE[](#_CPPv4N15wifi_security_t18WIFI_SECURITY_NONEE "永久链接至目标")
    :   Open system.

    enumerator WIFI_SECURITY_WEP[](#_CPPv4N15wifi_security_t17WIFI_SECURITY_WEPE "永久链接至目标")
    :   WEP security, **it’s unsafe security, please don’t use it**

    enumerator WIFI_SECURITY_WPA_TKIP[](#_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA_TKIPE "永久链接至目标")
    :   WPA TKIP

    enumerator WIFI_SECURITY_WPA_AES[](#_CPPv4N15wifi_security_t21WIFI_SECURITY_WPA_AESE "永久链接至目标")
    :   WPA AES

    enumerator WIFI_SECURITY_WPA_MIXED[](#_CPPv4N15wifi_security_t23WIFI_SECURITY_WPA_MIXEDE "永久链接至目标")
    :   WPA AES or TKIP

    enumerator WIFI_SECURITY_WPA2_TKIP[](#_CPPv4N15wifi_security_t23WIFI_SECURITY_WPA2_TKIPE "永久链接至目标")
    :   WPA2 TKIP

    enumerator WIFI_SECURITY_WPA2_AES[](#_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA2_AESE "永久链接至目标")
    :   WPA2 AES

    enumerator WIFI_SECURITY_WPA2_MIXED[](#_CPPv4N15wifi_security_t24WIFI_SECURITY_WPA2_MIXEDE "永久链接至目标")
    :   WPA2 AES or TKIP

    enumerator WIFI_SECURITY_WPA3_SAE[](#_CPPv4N15wifi_security_t22WIFI_SECURITY_WPA3_SAEE "永久链接至目标")
    :   WPA3 SAE

    enumerator WIFI_SECURITY_WPA3_WPA2_MIXED[](#_CPPv4N15wifi_security_t29WIFI_SECURITY_WPA3_WPA2_MIXEDE "永久链接至目标")
    :   WPA3 SAE or WPA2 AES

    enumerator WIFI_SECURITY_EAP[](#_CPPv4N15wifi_security_t17WIFI_SECURITY_EAPE "永久链接至目标")
    :   EAP

    enumerator WIFI_SECURITY_OWE[](#_CPPv4N15wifi_security_t17WIFI_SECURITY_OWEE "永久链接至目标")
    :   OWE

    enumerator WIFI_SECURITY_AUTO[](#_CPPv4N15wifi_security_t18WIFI_SECURITY_AUTOE "永久链接至目标")
    :   WiFi automatically detect the security type

enum wifi_link_state_t[](#_CPPv417wifi_link_state_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_LINKSTATE_STA_IDLE[](#_CPPv4N17wifi_link_state_t23WIFI_LINKSTATE_STA_IDLEE "永久链接至目标")
    :   sta mode is idle

    enumerator WIFI_LINKSTATE_STA_CONNECTING[](#_CPPv4N17wifi_link_state_t29WIFI_LINKSTATE_STA_CONNECTINGE "永久链接至目标")
    :   sta mode is connecting

    enumerator WIFI_LINKSTATE_STA_DISCONNECTED[](#_CPPv4N17wifi_link_state_t31WIFI_LINKSTATE_STA_DISCONNECTEDE "永久链接至目标")
    :   sta mode is disconnected

    enumerator WIFI_LINKSTATE_STA_CONNECTED[](#_CPPv4N17wifi_link_state_t28WIFI_LINKSTATE_STA_CONNECTEDE "永久链接至目标")
    :   sta mode is connected

    enumerator WIFI_LINKSTATE_STA_GOT_IP[](#_CPPv4N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE "永久链接至目标")
    :   sta mode got ip

    enumerator WIFI_LINKSTATE_AP_CONNECTED[](#_CPPv4N17wifi_link_state_t27WIFI_LINKSTATE_AP_CONNECTEDE "永久链接至目标")
    :   softap mode, a client association success

    enumerator WIFI_LINKSTATE_AP_DISCONNECTED[](#_CPPv4N17wifi_link_state_t30WIFI_LINKSTATE_AP_DISCONNECTEDE "永久链接至目标")
    :   softap mode, a client disconnect

    enumerator WIFI_LINKSTATE_AP_CONNECT_FAILED[](#_CPPv4N17wifi_link_state_t32WIFI_LINKSTATE_AP_CONNECT_FAILEDE "永久链接至目标")
    :   softap mode, a client association failed

    enumerator WIFI_LINKSTATE_MAX[](#_CPPv4N17wifi_link_state_t18WIFI_LINKSTATE_MAXE "永久链接至目标")
    :   reserved

enum wifi_country_policy_t[](#_CPPv421wifi_country_policy_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_COUNTRY_POLICY_AUTO[](#_CPPv4N21wifi_country_policy_t24WIFI_COUNTRY_POLICY_AUTOE "永久链接至目标")
    :   Country policy is auto, use the country info of AP to which the station is connected

    enumerator WIFI_COUNTRY_POLICY_MANUAL[](#_CPPv4N21wifi_country_policy_t26WIFI_COUNTRY_POLICY_MANUALE "永久链接至目标")
    :   Country policy is manual, always use the configured country info

enum wifi_second_channel_t[](#_CPPv421wifi_second_channel_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_SECOND_CHANNEL_NONE[](#_CPPv4N21wifi_second_channel_t24WIFI_SECOND_CHANNEL_NONEE "永久链接至目标")
    :   HT20 mode, no secondary channel

    enumerator WIFI_SECOND_CHANNEL_ABOVE[](#_CPPv4N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_ABOVEE "永久链接至目标")
    :   Second channel is above the primary channel

    enumerator WIFI_SECOND_CHANNEL_BELOW[](#_CPPv4N21wifi_second_channel_t25WIFI_SECOND_CHANNEL_BELOWE "永久链接至目标")
    :   Second channel is below the primary channel

enum wifi_capability_t[](#_CPPv417wifi_capability_t "永久链接至目标")
:   WiFi capability interface ID.


    *Values:*

    enumerator WIFI_CAPA_ID_ERP_EN[](#_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_ERP_ENE "永久链接至目标")
    :   Update Wi-Fi 11g support capability

    enumerator WIFI_CAPA_ID_HT_EN[](#_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HT_ENE "永久链接至目标")
    :   Update Wi-Fi 11n support capability

    enumerator WIFI_CAPA_ID_VHT_EN[](#_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_VHT_ENE "永久链接至目标")
    :   Update Wi-Fi 11ac support capability

    enumerator WIFI_CAPA_ID_HE_EN[](#_CPPv4N17wifi_capability_t18WIFI_CAPA_ID_HE_ENE "永久链接至目标")
    :   Update Wi-Fi 11ax support capability

    enumerator WIFI_CAPA_ID_TX_AMPDU_EN[](#_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_TX_AMPDU_ENE "永久链接至目标")
    :   Update Wi-Fi TX AMPDU support capability

    enumerator WIFI_CAPA_ID_RX_AMPDU_EN[](#_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_RX_AMPDU_ENE "永久链接至目标")
    :   Update Wi-Fi RX AMPDU support capability

    enumerator WIFI_CAPA_ID_TX_AMPDU_NUM[](#_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_TX_AMPDU_NUME "永久链接至目标")
    :   Update Wi-Fi TX AMPDU maximum number

    enumerator WIFI_CAPA_ID_RX_AMPDU_NUM[](#_CPPv4N17wifi_capability_t25WIFI_CAPA_ID_RX_AMPDU_NUME "永久链接至目标")
    :   Update Wi-Fi RX AMPDU maximum number

    enumerator WIFI_CAPA_ID_VHT_MCS[](#_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_VHT_MCSE "永久链接至目标")
    :   Update Wi-Fi VHT MCS

    enumerator WIFI_CAPA_ID_HE_MCS[](#_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_HE_MCSE "永久链接至目标")
    :   Update Wi-Fi HE MCS

    enumerator WIFI_CAPA_ID_B40_EN[](#_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_B40_ENE "永久链接至目标")
    :   Update Wi-Fi 40M bandwidth support capability

    enumerator WIFI_CAPA_ID_STBC_EN[](#_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_STBC_ENE "永久链接至目标")
    :   Update Wi-Fi STBC support capability

    enumerator WIFI_CAPA_ID_SGI_EN[](#_CPPv4N17wifi_capability_t19WIFI_CAPA_ID_SGI_ENE "永久链接至目标")
    :   Update Wi-Fi Short GI support capability

    enumerator WIFI_CAPA_ID_LDPC_EN[](#_CPPv4N17wifi_capability_t20WIFI_CAPA_ID_LDPC_ENE "永久链接至目标")
    :   Update Wi-Fi LDPC support capability

    enumerator WIFI_CAPA_ID_BEAMFORMEE_EN[](#_CPPv4N17wifi_capability_t26WIFI_CAPA_ID_BEAMFORMEE_ENE "永久链接至目标")
    :   Update Wi-Fi Beamforming support capability

    enumerator WIFI_CAPA_ID_11B_ONLY_EN[](#_CPPv4N17wifi_capability_t24WIFI_CAPA_ID_11B_ONLY_ENE "永久链接至目标")
    :   Update Wi-Fi 11b support capability

    enumerator WIFI_CAPA_ID_MAX[](#_CPPv4N17wifi_capability_t16WIFI_CAPA_ID_MAXE "永久链接至目标")

enum wifi_vht_mcs_support_t[](#_CPPv422wifi_vht_mcs_support_t "永久链接至目标")
:   enum wifi_vht_mcs_support_t - VHT MCS support definitions : MCSes 0-7 are supported for the number of streams : MCSes 0-8 are supported : MCSes 0-9 are supported : This number of streams isn’t supported


    *Values:*

    enumerator WIFI_VHT_MCS_SUPPORT_0_7[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E "永久链接至目标")

    enumerator WIFI_VHT_MCS_SUPPORT_0_8[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E "永久链接至目标")

    enumerator WIFI_VHT_MCS_SUPPORT_0_9[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E "永久链接至目标")

    enumerator WIFI_VHT_MCS_NOT_SUPPORTED[](#_CPPv4N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE "永久链接至目标")

enum wifi_he_mcs_support_t[](#_CPPv421wifi_he_mcs_support_t "永久链接至目标")
:   enum wifi_he_mcs_support_t - HE MCS support definitions : MCSes 0-7 are supported for the number of streams : MCSes 0-9 are supported : MCSes 0-11 are supported : This number of streams isn’t supported


    *Values:*

    enumerator WIFI_HE_MCS_SUPPORT_0_7[](#_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E "永久链接至目标")

    enumerator WIFI_HE_MCS_SUPPORT_0_9[](#_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E "永久链接至目标")

    enumerator WIFI_HE_MCS_SUPPORT_0_11[](#_CPPv4N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E "永久链接至目标")

    enumerator WIFI_HE_MCS_NOT_SUPPORTED[](#_CPPv4N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE "永久链接至目标")

enum wifi_sta_vsie[](#_CPPv413wifi_sta_vsie "永久链接至目标")
:   *Values:*

    enumerator WIFI_VENDOR_ELEM_ASSOC_REQ[](#_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE "永久链接至目标")

    enumerator WIFI_VENDOR_ELEM_PROBE_REQ[](#_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE "永久链接至目标")

    enumerator NUM_WIFI_VENDOR_ELEM_FRAMES[](#_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE "永久链接至目标")

enum sta_type[](#_CPPv48sta_type "永久链接至目标")
:   *Values:*

    enumerator STA_TYPE1[](#_CPPv4N8sta_type9STA_TYPE1E "永久链接至目标")

    enumerator STA_TYPE2[](#_CPPv4N8sta_type9STA_TYPE2E "永久链接至目标")

    enumerator STA_TYPE3[](#_CPPv4N8sta_type9STA_TYPE3E "永久链接至目标")

    enumerator STA_TYPE4[](#_CPPv4N8sta_type9STA_TYPE4E "永久链接至目标")

    enumerator MAX_STA_TYPE[](#_CPPv4N8sta_type12MAX_STA_TYPEE "永久链接至目标")
