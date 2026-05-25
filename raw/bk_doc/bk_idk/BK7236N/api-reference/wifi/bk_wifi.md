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

    - [`bk_wifi_send_listen_interval_req()`](#_CPPv432bk_wifi_send_listen_interval_req7uint8_t "bk_wifi_send_listen_interval_req") - set the listen interval

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


- [wifi.h](https://github.com/bekencorp/armino/blob/main/components/wifi.h "https://github.com/bekencorp/armino/blob/main/components/wifi.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_init(const [wifi_init_config_t](#_CPPv418wifi_init_config_t "wifi_init_config_t") *init_config)[](#_CPPv412bk_wifi_initPK18wifi_init_config_t "永久链接至目标")
:   This API initializes the WiFi driver, e.g. creating task for supplicant, allocating resource for low level WiFi driver etc.

    Usage example:

    ```
     wifi_init_config_t init_config = WIFI_DEFAULT_INIT_CONFIG();
     BK_LOG_ON_ERR(bk_wifi_init(&init_config);
    ```


    **Attention**
    :   1. This API is the 1st API that should be called before any other WiFi API can be called.


    **Attention**
    :   2. Make sure the reserved field in config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.

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


    **Attention**
    :   2. This API connect the BK STA to the configured AP automatically.


    **Attention**
    :   3. If the BK STA is already started, this API ignores the request and returns BK_OK. if you want to restart the BK STA, call [bk_wifi_sta_stop()](#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b "#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b") first and then call this API.


    **Attention**
    :   4. TODO description about fast connection

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_STA_NOT_CONFIG: the BK STA is not configured.

        - BK_ERR_WIFI_MONITOR_IP: the BK STA can’t be started because monitor is started.

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_split_init(void)[](#_CPPv422bk_wifi_sta_split_initv "永久链接至目标")
:   Init the BK STA.

    This API init is splited form bk_wifi_sta_start.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_split_start(void)[](#_CPPv423bk_wifi_sta_split_startv "永久链接至目标")
:   Start the BK STA.

    This API start is splited form bk_wifi_sta_start.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_split_connect(void)[](#_CPPv425bk_wifi_sta_split_connectv "永久链接至目标")
:   Connect the BK STA.

    This API connect is splited form bk_wifi_sta_start.

    返回
    :   - BK_OK: succeed

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
    os_strncpy(sta_config.password, "password", WIFI_PASSWORD_LEN);
    //more initialization here
    BK_LOG_ON_ERR(bk_wifi_sta_set_config(&sta_config));
    ```


    **Attention**
    :   1. Don’t call this API when the monitor is in-progress


    **Attention**
    :   2. If STA is already connected to AP, this API cases BK STA reconnects the AP.


    **Attention**
    :   3. Make sure the reserved fields in sta_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.


    **Attention**
    :   4. Auto reconnect max count and timeout can be set. When user app receives EVENT_WIFI_STA_DISCONNECTED event, it’s user app’s responsibility to reconnect to AP manually. Max count and timeout set to zero to let supplicant automatically handles connection without user app’s interaction.

    参数
    :   **sta_config** – the STA configuration

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: the STA is not initialized, call [bk_wifi_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226 "#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226") first.

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

        - The AID is only valid if @link_status->state is WIFI_LINK_CONNECTED.

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


    **Attention**
    :   2. Don’t call this API when the monitor is in-progress


    **Attention**
    :   3. If STA is already connected to AP, this API reconnects the BK STA.


    **Attention**
    :   4. TODO - multiple same SSID connect???

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


    **Attention**
    :   2. Pass NULL scan_config to scan all APs, otherwise scan the SSID specified in scan_config.ssid


    **Attention**
    :   3. Make sure the reserved fields in scan_config is zero, otherwise you may encounter compatibility issue in future if more config fields are added.


    **Attention**
    :   4. TODO scan result limits???

    参数
    :   **scan_config** – the configuration of scan

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: the STA is not initialized, call [bk_wifi_init()](#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226 "#group__bk__api__wifi__v2_1ga0ee95ecc01d57d9e4fa10220423e7226") first.

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


    **Attention**
    :   2. Don’t forget to call bk_wifi_scan_free_result(&scan_result) to free the the resource allocated in this API, otherwise memory leak.

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

void bk_wlan_sta_set_wireless_mode(uint8_t wireless_mode)[](#_CPPv429bk_wlan_sta_set_wireless_mode7uint8_t "永久链接至目标")
:   Set the wireless mode for the WLAN station.

    备注

    This API is used to configure the wireless mode (e.g., 802.11b/g/n) for the station interface.

    参数
    :   **wireless_mode** – The desired wireless mode to be configured

void bk_wlan_sta_set_retry_config(uint8_t auth_retry, uint16_t auth_retry_interval, uint8_t assoc_retry, uint16_t assoc_retry_interval, uint8_t eapol_2_retry)[](#_CPPv428bk_wlan_sta_set_retry_config7uint8_t8uint16_t7uint8_t8uint16_t7uint8_t "永久链接至目标")
:   Set the retry configuration for the WLAN station.

    Configure authentication/association retry counts and intervals for the STA.

    参数
    :   - **auth_retry** – Authentication retry count

        - **auth_retry_interval** – Authentication retry interval (unit: 100 ms)

        - **assoc_retry** – Association retry count

        - **assoc_retry_interval** – Association retry interval (unit: 100 ms)

        - **eapol_2_retry** – EAPOL-2 retry count

void bk_wlan_sta_get_tx_frame_count(uint32_t *tx_total_num, uint32_t *tx_dropped_num, uint32_t *tx_data_num)[](#_CPPv430bk_wlan_sta_get_tx_frame_countP8uint32_tP8uint32_tP8uint32_t "永久链接至目标")
:   Get the TX frame statistics of the WLAN station.

    This API retrieves the total number of transmitted frames, the number of dropped frames, and the number of transmitted data frames for the STA interface.

    备注

    The counters are typically reset on Wi-Fi initialization or STA start.

    参数
    :   - **tx_total_num** – **[out]** Pointer to store the total number of transmitted frames

        - **tx_dropped_num** – **[out]** Pointer to store the number of dropped frames

        - **tx_data_num** – **[out]** Pointer to store the number of transmitted data frames

void bk_wlan_sta_get_rx_frame_count(uint32_t *rx_total_num, uint32_t *rx_dropped_num, uint32_t *rx_data_num)[](#_CPPv430bk_wlan_sta_get_rx_frame_countP8uint32_tP8uint32_tP8uint32_t "永久链接至目标")
:   Get the RX frame statistics of the WLAN station.

    This API retrieves the total number of received frames, the number of dropped frames, and the number of received data frames for the STA interface.

    备注

    The counters are typically reset on Wi-Fi initialization or STA start.

    参数
    :   - **rx_total_num** – **[out]** Pointer to store the total number of received frames

        - **rx_dropped_num** – **[out]** Pointer to store the number of dropped frames

        - **rx_data_num** – **[out]** Pointer to store the number of received data frames

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


    **Attention**
    :   2. If [bk_wifi_ap_set_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39 "#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39") is not called, this API start the AP with default value, normally you should configure the AP first before calling this API.

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_AP_NOT_CONFIG: the WiFi AP is not configured, call [bk_wifi_ap_set_config()](#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39 "#group__bk__api__wifi__v2_1gac05d9c08d2f9212ad8568f0c6922db39") first.

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

int wlan_ap_sta_deauth(uint8_t *mac, int reason_code)[](#_CPPv418wlan_ap_sta_deauthP7uint8_ti "永久链接至目标")
:   De-authenticate a specific station associated to the BK AP.

    This API sends a de-authentication frame to the specified STA and removes it from the associated STA list of the AP.

    参数
    :   - **mac** – Pointer to the MAC address of the station to be de-authenticated

        - **reason_code** – Reason code for de-authentication

    返回
    :   - BK_OK: succeed

        - others: other errors

int wlan_ap_deauth_all_sta(void)[](#_CPPv422wlan_ap_deauth_all_stav "永久链接至目标")
:   De-authenticate all stations currently associated to the BK AP.

    This API sends a de-authentication frame to every associated STA and clears the entire associated STA list of the AP.

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_signal_info([wifi_signal_info_t](#_CPPv418wifi_signal_info_t "wifi_signal_info_t") *signal_info)[](#_CPPv427bk_wifi_sta_get_signal_infoP18wifi_signal_info_t "永久链接至目标")
:   Get the signal information of the connected AP.

    参数
    :   **signal_info** – store the signal information of the connected AP

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


    **Attention**
    :   2. When monitor mode is enabled, the STA connect will not work and [bk_wifi_sta_connect()](#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06 "#group__bk__api__wifi__v2_1ga6a74829e23ce17663cb2480d02e07c06") returns BK_ERR_WIFI_MONITOR_IP.

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


    **Attention**
    :   2. This API is only used for settting monitor channel, NOT for other purpose.


    **Attention**
    :   3. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.


    **Attention**
    :   4. The channel range can be set is from channel 1 to channel 14,

    参数
    :   **chan** – channel of monitor

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_monitor_set_channel_bonding(const [wifi_channel_t](#_CPPv414wifi_channel_t "wifi_channel_t") *chan)[](#_CPPv435bk_wifi_monitor_set_channel_bondingPK14wifi_channel_t "永久链接至目标")
:   Set monitor channel bonding.


    **Attention**
    :   1. This API will bond the monitor channel with the given channel.


    **Attention**
    :   2. This API is only used for settting monitor channel, NOT for other purpose.


    **Attention**
    :   3. This API directly change the hardware channel, it may impacts BK STA/AP if the STA or AP interface is started. TODO describe details of the impact.


    **Attention**
    :   4. The channel range can be set is from channel 1 to channel 14,

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


    **Attention**
    :   2. If STA is enabled, the WiFi driver only receives beacon from the connected AP, if scan is enabled or filter_config->rx_all_beacon is set, the WiFi driver receives beacons of all APs.

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


    **Attention**
    :   2. During WiFi scan, the filter also works.


    **Attention**
    :   3. Pass NULL callback or set all fields of filter_config to 0 to disable the filter.


    **Attention**
    :   4. The memory used to hold the frame buffer and frame_info will be freed immediately when the callback is returned, so don’t relay them to other task. Make a copy of them and then relay to other task if necessary.


    **Attention**
    :   5. Don’t do too much work in the filter callback because it’s called in WiFi driver core thread, otherwise it may impact the WiFi performance.

    参数
    :   **filter_cb** – the filter user callback

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_sta_get_mac(uint8_t *mac)[](#_CPPv419bk_wifi_sta_get_macP7uint8_t "永久链接至目标")
:   Get the MAC of BK STA.


    **Attention**
    :   1. The AP’s MAC is derived from the base MAC of the system.


    **Attention**
    :   2. If you want to change the MAC of AP, call bk_set_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK STA

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_get_mac(uint8_t *mac)[](#_CPPv418bk_wifi_ap_get_macP7uint8_t "永久链接至目标")
:   Get the MAC of BK AP.


    **Attention**
    :   1. The AP’s MAC is derived from the base MAC of the system.


    **Attention**
    :   2. If you want to change the MAC of AP, call bk_set_mac() to set the base MAC of the system.

    参数
    :   **mac** – store the MAC of BK AP

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_raw(uint8_t *buffer, int len)[](#_CPPv416bk_wifi_send_rawP7uint8_ti "永久链接至目标")
:   Send raw 802.11 frame.


    **Attention**
    :   1. This API can be used in WiFi station, softap, or monitor mode.


    **Attention**
    :   2. Only support to send non-QoS frame.


    **Attention**
    :   3. The frame sequence will be overwritten by WiFi driver.


    **Attention**
    :   4. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

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


    **Attention**
    :   2. Only support to send non-QoS frame.


    **Attention**
    :   3. The frame sequence will be overwritten by WiFi driver.


    **Attention**
    :   4. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw_tx** – raw tx information, refer to struct [wifi_raw_tx_info_t](#structwifi__raw__tx__info__t "#structwifi__raw__tx__info__t")

        - **cb** – send status call back

        - **param** – send status call back paramter

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_tx_raw_ex([wifi_raw_tx_info_t](#_CPPv418wifi_raw_tx_info_t "wifi_raw_tx_info_t") *raw_tx, void *cb, void *param)[](#_CPPv422bk_wifi_send_tx_raw_exP18wifi_raw_tx_info_tPvPv "永久链接至目标")
:   Send raw 802.11 tx frame.


    **Attention**
    :   1. This API can be used in WiFi station, softap, or monitor mode.


    **Attention**
    :   2. Only support to send non-QoS frame.


    **Attention**
    :   3. The frame sequence will be overwritten by WiFi driver.


    **Attention**
    :   4. The API doesn’t check the correctness of the raw frame, the caller need to guarantee the correctness of the frame.

    参数
    :   - **raw_tx** – raw tx information, refer to struct [wifi_raw_tx_info_t](#structwifi__raw__tx__info__t "#structwifi__raw__tx__info__t")

        - **cb** – send status call back

        - **param** – send status call back paramter

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_rate_power(uint32_t rate, uint32_t power)[](#_CPPv429bk_wifi_set_tx_raw_rate_power8uint32_t8uint32_t "永久链接至目标")
:   Update raw 802.11 frame TX rate and power.

    参数
    :   - **rate** – TX rate control

        - **power** – TX power control

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_ac(uint8_t ac)[](#_CPPv421bk_wifi_set_tx_raw_ac7uint8_t "永久链接至目标")
:   Update raw 802.11 frame TX AC.

    参数
    :   **ac** – TX AC

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_raw_timeout(uint16_t timeout_ms)[](#_CPPv426bk_wifi_set_tx_raw_timeout8uint16_t "永久链接至目标")
:   Update raw 802.11 frame TX timeout.

    参数
    :   **timeout_ms** – TX timeout in ms

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_wifi_media_mode(bool flag)[](#_CPPv427bk_wifi_set_wifi_media_modeb "永久链接至目标")
:   Configure wifi multimedia mode when the multimedia is running.

    This API is used to configure multimedia mode of Wi-Fi. Multimedia mode can enchance video fluency and make a better experience of video.


    **Attention**
    :   1. If you want to running multimedia mode,please configure this flag when open and close multimedia mode.


    **Attention**
    :   2. Please set this flag before running multimedia and clear this flag after closing multimedia.


    **Attention**
    :   3. If the flag is set when multimedia is turned on and it is not cleared after multimedia is turned off,the Wi-Fi will not be able to enter ps mode.

    参数
    :   **flag** – set true if you want to enable multimedia mode.

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_wifi_media_mode_config(bool *flag)[](#_CPPv434bk_wifi_get_wifi_media_mode_configPb "永久链接至目标")
:   get wifi media mode configuration

    参数
    :   **flag** – store configuration of wifi media mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_video_quality(uint8_t quality)[](#_CPPv425bk_wifi_set_video_quality7uint8_t "永久链接至目标")
:   Configure video quality when the video is running.

    This API is used to configure video quality.There are three mode to choose:

    Fluent definition(FD): The video transmission is relatively stable and has strong anti-interference ability,which can ensure the stable video transmission in a complex enviroment;

    Standard definition(SD):The video transmission is stable in a clean environment and is slightly stuck in a complex environment,which transmission bandwidth is improved;

    High definition(HD):The video transmission gives priority to high speed which can transmit high-bandwidth data in a clean environment, but the video transmission is relatively stuck in a complex environment;

    The default value is HD mode when the video is running.


    **Attention**
    :   1. If you want to running video mode,please configure this parameter when open video mode.


    **Attention**
    :   2. Please configure this parameter before running video mode.


    **Attention**
    :   3. Please configure bk_wifi_set_wifi_media_mode(flag) before useing this API.

    参数
    :   **quality** – set the video quality when the video is running. Three mode can be choose: 0-FD,1-SD,2-HD,default is HD.

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_video_quality_config(uint8_t *quality)[](#_CPPv432bk_wifi_get_video_quality_configP7uint8_t "永久链接至目标")
:   get video quality configuration

    参数
    :   **quality** – store configuration of video quality

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_default_ac(uint32_t ac)[](#_CPPv422bk_wifi_set_default_ac8uint32_t "永久链接至目标")
:   Configure defalut AC.

    This API is used to configure default AC,rang in [0 3]

    参数
    :   **ac** – set default AC rang in [0 3]

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_default_ac(uint32_t *ac)[](#_CPPv422bk_wifi_get_default_acP8uint32_t "永久链接至目标")
:   get default AC

    参数
    :   **ac** – store default AC

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: the parameter config is NULL

        - others: other errors

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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_min_rsv_mem(uint16_t mem_bytes)[](#_CPPv423bk_wifi_set_min_rsv_mem8uint16_t "永久链接至目标")
:   Update the minimux heap memory size that Wi-Fi should reserve.


    **Attention**
    :   1. An small piece of extra memory will be malloced from heap for each TX packets delivered to Wi-Fi, so if the pending TX packets are too many for some reasons, the heap memory will be occupied too much by TX packets. To ensure the stability of whole system, this interface is provied to limit the memory size for Wi-Fi TX packets.


    **Attention**
    :   2. The maximum valid value of memory size which could update via this API is 30K bytes


    **Attention**
    :   3. The default minimux reserved memory size is 10K bytes

    参数
    :   **mem_bytes** – the expected reserved memory size(bytes)

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_min_rsv_mem(uint16_t *mem_bytes)[](#_CPPv423bk_wifi_get_min_rsv_memP8uint16_t "永久链接至目标")
:   Get the minimux heap memory size that Wi-Fi currently creserves.

    参数
    :   **mem_bytes** – return currently reserved memory size(bytes)

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_max_msdu_cnt(uint16_t max_cnt)[](#_CPPv427bk_wifi_set_tx_max_msdu_cnt8uint16_t "永久链接至目标")
:   Update the maximum MSDU count that Wi-Fi could handle.

    参数
    :   **max_cnt** – the maxmimum MSDU count

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_max_msdu_cnt(uint16_t *max_cnt)[](#_CPPv427bk_wifi_get_tx_max_msdu_cntP8uint16_t "永久链接至目标")
:   Get the maximum MSDU count configuration that Wi-Fi could handle.

    参数
    :   **max_cnt** – return the maxmimum MSDU count

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_data_rty_num(uint8_t rty_num)[](#_CPPv424bk_wifi_set_data_rty_num7uint8_t "永久链接至目标")
:   Set data frame retry numbers.

    参数
    :   **rty_num** – data frame retry numbers

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_data_rty_num(uint32_t *rty_num)[](#_CPPv424bk_wifi_get_data_rty_numP8uint32_t "永久链接至目标")
:   Get data frame retry numbers.

    参数
    :   **rty_num** – data frame retry numbers

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_mgmt_rty_num(uint8_t rty_num)[](#_CPPv424bk_wifi_set_mgmt_rty_num7uint8_t "永久链接至目标")
:   Set management frame retry numbers.

    参数
    :   **rty_num** – management frame retry numbers

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_mgmt_rty_num(uint32_t *rty_num)[](#_CPPv424bk_wifi_get_mgmt_rty_numP8uint32_t "永久链接至目标")
:   Get management frame retry numbers.

    参数
    :   **rty_num** – management frame retry numbers

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_capa_config([wifi_capability_t](#_CPPv417wifi_capability_t "wifi_capability_t") capa_id, uint32_t capa_val)[](#_CPPv419bk_wifi_capa_config17wifi_capability_t8uint32_t "永久链接至目标")
:   Update Wi-Fi capability configuration.

    This API is used to change some Wi-Fi capability configuration, please refer to wifi_capability_t to get the capability that has been supported.


    **Attention**
    :   1. Please keep in mind that Wi-Fi behavior may change if the capability is changed to different value compared with the default value.


    **Attention**
    :   2. We strongly suggest not using this API except you are very farmiliar with the Wi-Fi specification.


    **Attention**
    :   3. If you want Wi-Fi working on 11b only mode, please set 11b only mode by configurate paramter capa_id with WIFI_CAPA_ID_11B_ONLY_EN and capa_val with TRUE.

    参数
    :   - **capa_id** – the specific capability you want to change

        - **capa_val** – new capability value

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_country(const [wifi_country_t](#_CPPv414wifi_country_t "wifi_country_t") *country)[](#_CPPv419bk_wifi_set_countryPK14wifi_country_t "永久链接至目标")
:   configure country info


    **Attention**
    :   1. The default country is {.cc=”CN”, .schan=1, .nchan=13, policy=WIFI_COUNTRY_POLICY_AUTO}


    **Attention**
    :   2. When the country policy is WIFI_COUNTRY_POLICY_AUTO, the country info of the AP to which the station is connected is used. E.g. if the configured country info is {.cc=”USA”, .schan=1, .nchan=11} and the country info of the AP to which the station is connected is {.cc=”JP”, .schan=1, .nchan=14} then the country info that will be used is {.cc=”JP”, .schan=1, .nchan=14}. If the station disconnected from the AP the country info is set back back to the country info of the station automatically, {.cc=”USA”, .schan=1, .nchan=11} in the example.


    **Attention**
    :   3. When the country policy is WIFI_COUNTRY_POLICY_MANUAL, always use the configured country info.


    **Attention**
    :   4. When the country info is changed because of configuration or because the station connects to a different external AP, the country IE in probe response/beacon of the soft-AP is changed also.


    **Attention**
    :   5. The country configuration is not stored into flash


    **Attention**
    :   6. This API doesn’t validate the per-country rules, it’s up to the user to fill in all fields according to local regulations.

    参数
    :   **country** – the configured country info

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: WiFi is not initialized

        - BK_ERR_PARAM: invalid argument

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_country_code(const char *alpha2)[](#_CPPv424bk_wifi_set_country_codePKc "永久链接至目标")
:   configure regulatory domain

    @alpha2 alpha2 ISO/IEC 3166-1 alpha

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

char *bk_wifi_get_country_code(void)[](#_CPPv424bk_wifi_get_country_codev "永久链接至目标")
:   get the current country code

    返回
    :   country code string

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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_manual_cal_rfcali_status(void)[](#_CPPv432bk_wifi_manual_cal_rfcali_statusv "永久链接至目标")
:   Get Wi-Fi Calibration status.

    返回
    :   - BK_OK: on succeed

        - others: real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ap_vif_probe_req_frame_cb_register(void *cb)[](#_CPPv442bk_wifi_ap_vif_probe_req_frame_cb_registerPv "永久链接至目标")
:   Register a cb of probe request for ap.

    参数
    :   **cb** – callback function of probe request to register

bool bk_wifi_get_lowpower_mode(void)[](#_CPPv425bk_wifi_get_lowpower_modev "永久链接至目标")
:   get if ever set dtim10.

    返回
    :   - true: has been set to >= dtim10.

        - false: never set >= dtim10 before.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_listen_interval_req(uint8_t interval)[](#_CPPv432bk_wifi_send_listen_interval_req7uint8_t "永久链接至目标")
:   Set listen interval.

    参数
    :   **any** – value is acceptable,but 1, 3, 10 is recommended.

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_sleep_mode_req(uint8_t sleep_mode)[](#_CPPv427bk_wifi_send_sleep_mode_req7uint8_t "永久链接至目标")
:   Set sleep mode.

    参数
    :   **0, 1, 2** –

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_sleep_mode(uint8_t *sleep_mode)[](#_CPPv422bk_wifi_get_sleep_modeP7uint8_t "永久链接至目标")
:   Get sleep mode.

    参数
    :   **return** – the configure sleep mode

    返回
    :   -0: min modem sleep mode -1: middle modem sleep mode -2: max modem sleep mode

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_listen_interval(uint8_t *listen_interval)[](#_CPPv427bk_wifi_get_listen_intervalP7uint8_t "永久链接至目标")
:   Get listen interval.

    参数
    :   **return** – the configure listen interval

    返回
    :   -0: not set listen interval -others:return the configure listen interval value.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_arp_set_rate_req(uint16_t arp_tx_rate)[](#_CPPv429bk_wifi_send_arp_set_rate_req8uint16_t "永久链接至目标")
:   Set arp tx rate.

    参数
    :   **any** – value is acceptable,but 1, 6 is recommended.

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_send_bcn_loss_int_req(uint8_t interval, uint8_t repeat_num)[](#_CPPv429bk_wifi_send_bcn_loss_int_req7uint8_t7uint8_t "永久链接至目标")
:   When beacon loss occurs,use beacon loss interval.

    参数
    :   - **interval** – any value is acceptable,it is recommended that this value less than listen interval

        - **repeat_num** – set beacon loss interval number,the minimum value is 1

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_bcn_loss_time(uint8_t wait_cnt, uint8_t wake_cnt)[](#_CPPv425bk_wifi_set_bcn_loss_time7uint8_t7uint8_t "永久链接至目标")
:   When beacon loss occurs,use bcn loss time.

    @usage example:(10s no beacon frame received(normal reception for the first 5s,ps off for the next 5s),disconnect from the router) DTIM10:wait_cnt = 5,wake_cnt = 50 DTIM1 :wait_cnt = 50,wake_cnt = 50

    参数
    :   - **wait_cnt** – failed to receive beacon for wait_cnt consecutive cycles, close ps,wait_cnt corresponds to dtimx(listen_interval)

        - **wake_cnt** – after ps is turned off,the beacon fails to receive for wake_cnt consecutive cycles, disconnect;wake_cnt corresponds to dtim1

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_bcn_miss_time(uint8_t bcnmiss_time)[](#_CPPv425bk_wifi_set_bcn_miss_time7uint8_t "永久链接至目标")
:   configure beacon miss time.

    bcnmiss_time: bcnmiss_time not receive the beacon,disconnected from the router;unit: second

    @usage example:(30s no beacon frame received,disconnect from the router) bcnmiss_time:30

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_conn_delay_time(uint8_t conn_delay_time)[](#_CPPv427bk_wifi_set_conn_delay_time7uint8_t "永久链接至目标")
:   set station connection delay time.

    参数
    :   **conn_delay_time** – delay time of starting station connection (in ms).

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_bcn_cc_rxed_register_cb(const [wifi_beacon_cc_rxed_t](#_CPPv421wifi_beacon_cc_rxed_t "wifi_beacon_cc_rxed_t") cc_cb, void *ctxt)[](#_CPPv431bk_wifi_bcn_cc_rxed_register_cbK21wifi_beacon_cc_rxed_tPv "永久链接至目标")
:   regist bcn cc rxed callback.

    参数
    :   **bcn** – cc the callback function.

    返回
    :   -BK_OK: on success -others:real error, used for future.

int cc_scan_start(void)[](#_CPPv413cc_scan_startv "永久链接至目标")
:   start scan procedure to find AP’s country code

    返回
    :   -BK_OK: on success -others:real error, used for future.

void cc_scan_stop(void)[](#_CPPv412cc_scan_stopv "永久链接至目标")
:   stop scan procedure to find AP’s country code

    返回
    :   success

int bk_scan_country_code(uint8_t *country_code)[](#_CPPv420bk_scan_country_codeP7uint8_t "永久链接至目标")
:   Get country code by scan.


    **Attention**
    :   Need open CONFIG_WIFI_SCAN_COUNTRY_CODE=y in config

    参数
    :   **country_code** – The point of country code buffer

    返回
    :   - > 0 : succeed, and the length of country code buffer

        - = 0 : not found

        - <= 0 : failures.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_bcn_miss_register_cb(const [wifi_bcnmiss_cb_t](#_CPPv417wifi_bcnmiss_cb_t "wifi_bcnmiss_cb_t") bcnmiss_cb)[](#_CPPv428bk_wifi_bcn_miss_register_cbK17wifi_bcnmiss_cb_t "永久链接至目标")
:   regist bcn miss callback.

    参数
    :   **bcnmiss_cb** – the callback function, this function should return bool value indicating whether disconnected from router or not.

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_bcn_recv_win(uint8_t default_win, uint8_t max_win, uint8_t step)[](#_CPPv424bk_wifi_set_bcn_recv_win7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   set beacon receive window.

    参数
    :   - **default_win** – default beacon receive window(ms),minimum is 5,less than or equal to max_win.

        - **max_win** – max beacon receive window(ms),maximum is 20.

        - **step** – increase the beacon reception time by a step value(ms)

    返回
    :   -BK_OK: on success -others:real error, used for future.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_support_wifi_mode(uint8_t *support_mode)[](#_CPPv429bk_wifi_get_support_wifi_modeP7uint8_t "永久链接至目标")
:   Get wifi support mode.

    参数
    :   **get** – wifi support info

    返回
    :   -2: support wifi6(HE) -1: support wifi4(HT) -0: support others(11n/g)

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

void bk_wifi_set_td_active_percent(uint8_t active_percent)[](#_CPPv429bk_wifi_set_td_active_percent7uint8_t "永久链接至目标")
:   Set active_percent.

    参数
    :   **{10ms-100ms}** – *

    返回
    :   -void.

void bk_wifi_mask_td_active_percent()[](#_CPPv430bk_wifi_mask_td_active_percentv "永久链接至目标")
:   mask active_percent

    参数
    :   ***** –

void bk_wifi_ap_power_register_cb(FUNC_1PARAM_PTR cb)[](#_CPPv428bk_wifi_ap_power_register_cb15FUNC_1PARAM_PTR "永久链接至目标")
:   register callback to get wifi ap power

    参数
    :   **callback** – interface *

    返回
    :   -void.

void bk_wlan_phy_open_cca(void)[](#_CPPv420bk_wlan_phy_open_ccav "永久链接至目标")

void bk_wlan_phy_close_cca(void)[](#_CPPv421bk_wlan_phy_close_ccav "永久链接至目标")

void bk_wlan_phy_show_cca(void)[](#_CPPv420bk_wlan_phy_show_ccav "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ftm_start(const [wifi_ftm_config_t](#_CPPv417wifi_ftm_config_t "wifi_ftm_config_t") *config, [wifi_ftm_results_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") *ftm_results)[](#_CPPv417bk_wifi_ftm_startPK17wifi_ftm_config_tP18wifi_ftm_results_t "永久链接至目标")
:   Start a fine timing measurement (FTM)

    This API notifies the WiFi driver to start a fine timing measurement, and get the ftm results.

    参数
    :   - **config** – the configuration of ftm

        - **ftm_results** – the results of ftm

    返回
    :   - BK_OK: succeed

        - BK_ERR_WIFI_NOT_INIT: WiFi is not initialized

        - BK_ERR_WIFI_STA_NOT_STARTED: the STA is not started, call [bk_wifi_sta_start()](#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf "#group__bk__api__wifi__v2_1gaaf144e78b9438143e21f7c75e8c23ecf") first.

        - BK_ERR_WIFI_DRIVER: WiFi low level driver has failure.

        - others: other failures.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_ftm_dump_result(const [wifi_ftm_results_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") *ftm_results)[](#_CPPv423bk_wifi_ftm_dump_resultPK18wifi_ftm_results_t "永久链接至目标")
:   Dump the ftm results.


    **Attention**
    :   call [bk_wifi_ftm_start()](#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd "#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd") first before call bk_wifi_ftm_dump_result.

    参数
    :   **ftm_results** – The ftm result to be dumped.

    返回
    :   - BK_OK: succeed

        - BK_ERR_PARAM: invalid scan result

void bk_wifi_ftm_free_result([wifi_ftm_results_t](#_CPPv418wifi_ftm_results_t "wifi_ftm_results_t") *ftm_results)[](#_CPPv423bk_wifi_ftm_free_resultP18wifi_ftm_results_t "永久链接至目标")
:   Free the ftm result.


    **Attention**
    :   This API free ftm_results->rsp which allocated in [bk_wifi_ftm_start()](#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd "#group__bk__api__wifi__v2_1ga26fdfeaa0ffcbf1ffc0562f7eb0d78dd"), it doesn’t free ftm_results. So if ftm_results is allocated by the caller, the caller need to free it.

    参数
    :   **ftm_results** – The ftm result to be freed.

    返回
    :   - BK_OK: always succeed

void bk_wifi_set_pkt_trx_dbg_cfg(uint32_t cfg_bit)[](#_CPPv427bk_wifi_set_pkt_trx_dbg_cfg8uint32_t "永久链接至目标")
:   Set Wi-Fi TX/RX debug log configuration.

    This API could enable the TX/RX debug log by setting the corresponding debug bit.


    **Attention**
    :   This API is only used for DEBUG Wi-Fi issues according to frame TX/RX, there will be a lot of logs generated after set debug bit and it will have affect on the performance. To capture the whole logs, you should increase the buadrate of UART.

    参数
    :   **cfg_bit** – Please refer to enum wifi_pkt_dbg_bit to get more detail.

    返回
    :   - void: always succeed

void bk_wifi_set_ap_channel(uint8_t channel)[](#_CPPv422bk_wifi_set_ap_channel7uint8_t "永久链接至目标")
:   Set Wi-Fi Softap Channel.

    This API could be used to change softap operation channel.

    @channel The valid channel ID should range from 1-14.


    **Attention**
    :   This API can only be used when softap is enabled and make sure the internal CSA strategy is disabled by calling API bk_feature_close_coexist_csa.

    返回
    :   - void: always succeed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_block_bcmc_en(uint8_t config)[](#_CPPv425bk_wifi_set_block_bcmc_en7uint8_t "永久链接至目标")
:   Enable Wi-Fi rx block broadcast and multicast frame.

    This API could enable Wi-Fi rx block broadcast and multicast frame.

    参数
    :   **config** – block type. 0:WIFI_BCMC_CLOSE 1:WIFI_MC_ON, 2:WIFI_BC_ON, 3:WIFI_BC_MC_ON,

    返回
    :   - void: always succeed

bool bk_wifi_get_block_bcmc_en(void)[](#_CPPv425bk_wifi_get_block_bcmc_env "永久链接至目标")
:   Get Wi-Fi rx block broadcast and multicast frame status.

    参数
    :   **void.** –

    返回
    :   - enable status

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_ani_en(bool enable)[](#_CPPv418bk_wifi_set_ani_enb "永久链接至目标")
:   Enable Wi-Fi microwave anti-interference policy.

    This API could enable Wi-Fi microwave anti-interference policy.

    参数
    :   **enable.** –

    返回
    :   - void: always succeed

bool bk_wifi_get_ani_en(void)[](#_CPPv418bk_wifi_get_ani_env "永久链接至目标")
:   Get Wi-Fi microwave anti-interference policy enable status.

    参数
    :   **void.** –

    返回
    :   - enable status

int bk_wifi_set_pwr_limit([wifi_tx_pwr_lmt_t](#_CPPv417wifi_tx_pwr_lmt_t "wifi_tx_pwr_lmt_t") *tx_pwr_lmt)[](#_CPPv421bk_wifi_set_pwr_limitP17wifi_tx_pwr_lmt_t "永久链接至目标")
:   Set Wi-Fi Power Limit.

    This API could be used to change max tx power with regulation,ratesection and channel .


    **Attention**
    :   This API can only be used to modify rf max power limit for specific regulation,rate and channel.

    参数
    :   **tx_pwr_lmt** – wifi tx power limit info

    返回
    :   - void: always succeed

bool bk_wifi_get_cal_2g(void)[](#_CPPv418bk_wifi_get_cal_2gv "永久链接至目标")
:   Get rf cal 2g information.

    This API could be used to check rf 2g calibration .

    返回
    :   - true:if rf 2g is calibrated, false: if rf 2g is not calibrated

void bk_wifi_get_noise_floor(uint8_t *noise_floor)[](#_CPPv423bk_wifi_get_noise_floorP7uint8_t "永久链接至目标")
:   Get noise floor.

    参数
    :   **noise_floor** – store noise floor

    返回
    :   - void: always succeed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_stats(uint8_t mode, struct [tx_stats_t](#_CPPv410tx_stats_t "tx_stats_t") *tx_stats)[](#_CPPv420bk_wifi_get_tx_stats7uint8_tP10tx_stats_t "永久链接至目标")
:   Get tx stats.

    ```
        PER calculation formula:  per = (tx_agg_fail + tx_singel_retry)/(tx_agg_total + tx_singel_total*SINGLE_RETRY_CNT)

        - tx_agg_fail/tx_singel_retry/tx_agg_total/tx_singel_total: get from struct tx_stats,

        - SINGLE_RETRY_CNT: get from function bk_wifi_get_data_rty_num();
    ```

    参数
    :   **config** – mode. 0:STATION 1:SOFT AP

    返回
    :   - tx_stats:tx statistics

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_get_tx_power([wifi_standard](#_CPPv413wifi_standard "wifi_standard") standard, float *powerdBm)[](#_CPPv420bk_wifi_get_tx_power13wifi_standardPf "永久链接至目标")
:   Fetch 802.11 TX power by standards.

    参数
    :   - **standard** – IEEE 80211 standard

        - **power** – TX power in dBm

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_set_tx_power([wifi_standard](#_CPPv413wifi_standard "wifi_standard") standard, float powerdBm)[](#_CPPv420bk_wifi_set_tx_power13wifi_standardf "永久链接至目标")
:   Update 802.11 TX power by standards.

    参数
    :   - **standard** – IEEE 80211 standard

        - **power** – TX power in dBm

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_disable(void)[](#_CPPv415bk_wifi_disablev "永久链接至目标")
:   Disable wifi mac.

    返回
    :   - kNoErr: succeed

        - otherwise: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_wifi_enable(void)[](#_CPPv414bk_wifi_enablev "永久链接至目标")
:   enable wifi mac

    返回
    :   - kNoErr: succeed

        - otherwise: fail


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [wifi_types.h](https://github.com/bekencorp/armino/blob/main/components/wifi_types.h "https://github.com/bekencorp/armino/blob/main/components/wifi_types.h")


### Functions[](#id2 "永久链接至标题")

[wifi_rlk_scan_cfm_cb_t](#_CPPv422wifi_rlk_scan_cfm_cb_t "wifi_rlk_scan_cfm_cb_t") wifi_rlk_scan_get_register_cfm_cb(void)[](#_CPPv433wifi_rlk_scan_get_register_cfm_cbv "永久链接至目标")


### Structures[](#structures "永久链接至标题")

struct wifi_init_config_t[](#_CPPv418wifi_init_config_t "永久链接至目标")
:   Public Members

    uint64_t features[](#_CPPv4N18wifi_init_config_t8featuresE "永久链接至目标")
    :   WiFi feature bitmaps

    void *os_funcs[](#_CPPv4N18wifi_init_config_t8os_funcsE "永久链接至目标")
    :   WiFi OS functions

    void *os_val[](#_CPPv4N18wifi_init_config_t6os_valE "永久链接至目标")
    :   WiFI Values

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

    uint8_t psk[WIFI_PASSWORD_LEN][](#_CPPv4N17wifi_sta_config_t3pskE "永久链接至目标")
    :   PSK of AP

    uint8_t ip_addr[4][](#_CPPv4N17wifi_sta_config_t7ip_addrE "永久链接至目标")
    :   IP address

    uint8_t netmask[4][](#_CPPv4N17wifi_sta_config_t7netmaskE "永久链接至目标")
    :   NET address

    uint8_t gw[4][](#_CPPv4N17wifi_sta_config_t2gwE "永久链接至目标")
    :   GW address

    uint8_t dns1[4][](#_CPPv4N17wifi_sta_config_t4dns1E "永久链接至目标")
    :   DNS address

    uint8_t is_not_support_auto_fci[](#_CPPv4N17wifi_sta_config_t23is_not_support_auto_fciE "永久链接至目标")
    :   is not support auto fast connect

    uint8_t is_user_fast_connect[](#_CPPv4N17wifi_sta_config_t20is_user_fast_connectE "永久链接至目标")
    :   is use user fast connect

    uint8_t pmf[](#_CPPv4N17wifi_sta_config_t3pmfE "永久链接至目标")
    :   is support pmf

    uint8_t tk[16][](#_CPPv4N17wifi_sta_config_t2tkE "永久链接至目标")
    :   WPA3 tk key

    int auto_reconnect_count[](#_CPPv4N17wifi_sta_config_t20auto_reconnect_countE "永久链接至目标")
    :   auto reconnect max count, 0 for always reconnect

    int auto_reconnect_timeout[](#_CPPv4N17wifi_sta_config_t22auto_reconnect_timeoutE "永久链接至目标")
    :   auto reconnect timeout in secs, 0 for no timeout

    bool disable_auto_reconnect_after_disconnect[](#_CPPv4N17wifi_sta_config_t39disable_auto_reconnect_after_disconnectE "永久链接至目标")
    :   disable auto reconnect if deauth/disassoc by AP when in connected state

    uint8_t reserved[32][](#_CPPv4N17wifi_sta_config_t8reservedE "永久链接至目标")
    :   reserved, **must set to 0**

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

    u8 scan_type[](#_CPPv4N18wifi_scan_config_t9scan_typeE "永久链接至目标")
    :   0: active scan; 1: passive scan

    u8 chan_cnt[](#_CPPv4N18wifi_scan_config_t8chan_cntE "永久链接至目标")
    :   scan channel cnt

    u8 chan_nb[WIFI_2BAND_MAX_CHAN_NUM][](#_CPPv4N18wifi_scan_config_t7chan_nbE "永久链接至目标")
    :   scan channel number 2.4g+5g

    u32 duration[](#_CPPv4N18wifi_scan_config_t8durationE "永久链接至目标")
    :   scan duration,ms

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

    uint8_t is_bridge[](#_CPPv4N19wifi_scan_ap_info_t9is_bridgeE "永久链接至目标")
    :   is AP support bridge

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

    uint8_t bridge[](#_CPPv4N16wifi_ap_config_t6bridgeE "永久链接至目标")
    :   BK AP support bridge

    uint8_t vsie_len[](#_CPPv4N16wifi_ap_config_t8vsie_lenE "永久链接至目标")
    :   Beacon/ProbeResp Vendor Specific IE len

    uint8_t vsie[255][](#_CPPv4N16wifi_ap_config_t4vsieE "永久链接至目标")
    :   Beacon/ProbeResp Vendor Specific IE

    uint8_t max_con[](#_CPPv4N16wifi_ap_config_t7max_conE "永久链接至目标")
    :   Max number of stations allowed to connect to BK AP, TODO default value?

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

    uint32_t tsf_lo[](#_CPPv4N17wifi_frame_info_t6tsf_loE "永久链接至目标")
    :   Total length for the MPDU transfer

    uint32_t tsf_hi[](#_CPPv4N17wifi_frame_info_t6tsf_hiE "永久链接至目标")
    :   TSF Low

    uint32_t recvec1a[](#_CPPv4N17wifi_frame_info_t8recvec1aE "永久链接至目标")
    :   TSF High

    uint32_t recvec1b[](#_CPPv4N17wifi_frame_info_t8recvec1bE "永久链接至目标")
    :   Receive Vector 1

    uint32_t recvec1c[](#_CPPv4N17wifi_frame_info_t8recvec1cE "永久链接至目标")
    :   Receive Vector 1

    uint32_t recvec1d[](#_CPPv4N17wifi_frame_info_t8recvec1dE "永久链接至目标")
    :   Receive Vector 1

    uint32_t recvec2a[](#_CPPv4N17wifi_frame_info_t8recvec2aE "永久链接至目标")
    :   Receive Vector 1

    uint32_t recvec2b[](#_CPPv4N17wifi_frame_info_t8recvec2bE "永久链接至目标")
    :   Receive Vector 2

struct wifi_rlk_chan_info[](#_CPPv418wifi_rlk_chan_info "永久链接至目标")
:   Public Members

    uint16_t freq[](#_CPPv4N18wifi_rlk_chan_info4freqE "永久链接至目标")
    :   Frequency of the channel.

    uint8_t noise_dbm[](#_CPPv4N18wifi_rlk_chan_info9noise_dbmE "永久链接至目标")
    :   Noise in dbm.

    uint32_t chan_time_ms[](#_CPPv4N18wifi_rlk_chan_info12chan_time_msE "永久链接至目标")
    :   Amount of time spent of the channel (in ms)

    uint32_t chan_time_busy_ms[](#_CPPv4N18wifi_rlk_chan_info17chan_time_busy_msE "永久链接至目标")
    :   Amount of time the primary channel was sensed busy.

struct wifi_rlk_base_info[](#_CPPv418wifi_rlk_base_info "永久链接至目标")

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

    uint32_t scan_use_time[](#_CPPv4N22wifi_event_scan_done_t13scan_use_timeE "永久链接至目标")
    :   scan time. us

struct wifi_event_network_found_t[](#_CPPv426wifi_event_network_found_t "永久链接至目标")
:   Public Members

    char ssid[WIFI_SSID_STR_LEN][](#_CPPv4N26wifi_event_network_found_t4ssidE "永久链接至目标")
    :   SSID found to be connected

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N26wifi_event_network_found_t5bssidE "永久链接至目标")
    :   BSSID found to be connected

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

struct wifi_event_dtim_received_t[](#_CPPv426wifi_event_dtim_received_t "永久链接至目标")
:   Public Members

    uint32_t beacon_interval[](#_CPPv4N26wifi_event_dtim_received_t15beacon_intervalE "永久链接至目标")
    :   beacon interval

    uint8_t dtim_period[](#_CPPv4N26wifi_event_dtim_received_t11dtim_periodE "永久链接至目标")
    :   dtim period

struct wifi_event_reg_change_t[](#_CPPv423wifi_event_reg_change_t "永久链接至目标")
:   Public Members

    uint8_t initiator[](#_CPPv4N23wifi_event_reg_change_t9initiatorE "永久链接至目标")
    :   0: core, 1: user, 2: driver, 3: dot11d

    uint8_t type[](#_CPPv4N23wifi_event_reg_change_t4typeE "永久链接至目标")
    :   0: country, 1: world, 2: custom, 3: intersection

    char alpha2[2][](#_CPPv4N23wifi_event_reg_change_t6alpha2E "永久链接至目标")
    :   country code

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

    uint32_t tx_ac[](#_CPPv4N14raw_tx_cntrl_t5tx_acE "永久链接至目标")
    :   RAW Data TX AC information

    uint32_t tx_rate[](#_CPPv4N14raw_tx_cntrl_t7tx_rateE "永久链接至目标")
    :   RAW Data TX rate information

    uint32_t tx_power[](#_CPPv4N14raw_tx_cntrl_t8tx_powerE "永久链接至目标")
    :   RAW Data TX power information

    uint32_t tx_retry_cnt[](#_CPPv4N14raw_tx_cntrl_t12tx_retry_cntE "永久链接至目标")
    :   RAW Data TX retry count

    uint32_t tx_timeout_ms[](#_CPPv4N14raw_tx_cntrl_t13tx_timeout_msE "永久链接至目标")
    :   RAW Data TX timeout information

    uint8_t format[](#_CPPv4N14raw_tx_cntrl_t6formatE "永久链接至目标")
    :   RAW Data TX format information

    uint8_t band_width[](#_CPPv4N14raw_tx_cntrl_t10band_widthE "永久链接至目标")
    :   RAW Data TX band width information

    uint8_t gi_type[](#_CPPv4N14raw_tx_cntrl_t7gi_typeE "永久链接至目标")
    :   RAW Data TX guard interval type information

    uint8_t ht_mcs[](#_CPPv4N14raw_tx_cntrl_t6ht_mcsE "永久链接至目标")
    :   RAW Data TX HT MCS index information

struct wifi_raw_tx_info_t[](#_CPPv418wifi_raw_tx_info_t "永久链接至目标")
:   Wi-Fi RAW TX control.

    Public Members

    uint8_t *pkt[](#_CPPv4N18wifi_raw_tx_info_t3pktE "永久链接至目标")
    :   RAW data tx packet address

    int len[](#_CPPv4N18wifi_raw_tx_info_t3lenE "永久链接至目标")
    :   RAW data tx packet length

    int type[](#_CPPv4N18wifi_raw_tx_info_t4typeE "永久链接至目标")
    :   Raw data tx packet type length

    [raw_tx_cntrl_t](#_CPPv414raw_tx_cntrl_t "raw_tx_cntrl_t") tx_cntrl[](#_CPPv4N18wifi_raw_tx_info_t8tx_cntrlE "永久链接至目标")
    :   RAW data tx control information

struct wifi_ftm_config_t[](#_CPPv417wifi_ftm_config_t "永久链接至目标")
:   FTM configuration and results.

    Wi-Fi fine timing measurement configuration.

    Public Members

    uint8_t ftm_per_burst[](#_CPPv4N17wifi_ftm_config_t13ftm_per_burstE "永久链接至目标")
    :   Number of FTMs per Burst

    uint8_t nb_ftm_rsp[](#_CPPv4N17wifi_ftm_config_t10nb_ftm_rspE "永久链接至目标")
    :   Number of FTM responders on which we do the measurements

struct wifi_ftm_rsp_info_t[](#_CPPv419wifi_ftm_rsp_info_t "永久链接至目标")
:   Wi-Fi fine timing measurement results.

    Public Members

    uint8_t bssid[WIFI_BSSID_LEN][](#_CPPv4N19wifi_ftm_rsp_info_t5bssidE "永久链接至目标")
    :   MAC Address of the FTM responder

    uint32_t rtt[](#_CPPv4N19wifi_ftm_rsp_info_t3rttE "永久链接至目标")
    :   Round Trip Time (in ns)

    float distance[](#_CPPv4N19wifi_ftm_rsp_info_t8distanceE "永久链接至目标")
    :   Distance (in m)

struct wifi_ftm_results_t[](#_CPPv418wifi_ftm_results_t "永久链接至目标")
:   Public Members

    uint8_t nb_ftm_rsp[](#_CPPv4N18wifi_ftm_results_t10nb_ftm_rspE "永久链接至目标")
    :   Number of FTM responders for which we have a measurement

    [wifi_ftm_rsp_info_t](#_CPPv419wifi_ftm_rsp_info_t "wifi_ftm_rsp_info_t") *rsp[](#_CPPv4N18wifi_ftm_results_t3rspE "永久链接至目标")
    :   Per-responder measurements

struct wifi_csi_active_mode_config_t[](#_CPPv429wifi_csi_active_mode_config_t "永久链接至目标")
:   Public Members

    bool enable[](#_CPPv4N29wifi_csi_active_mode_config_t6enableE "永久链接至目标")
    :   enable or disable csi active, true: enable, false: disable

    uint32_t interval[](#_CPPv4N29wifi_csi_active_mode_config_t8intervalE "永久链接至目标")
    :   interval of csi active, unit: ms

struct wifi_csi_filter_config_t[](#_CPPv424wifi_csi_filter_config_t "永久链接至目标")
:   Public Members

    uint8_t proto_type_bmp[](#_CPPv4N24wifi_csi_filter_config_t14proto_type_bmpE "永久链接至目标")
    :   b`0001:NON_HT,b`0010:HT, b`0100:VHT, b`1000:HE

    uint8_t cbw_bmp[](#_CPPv4N24wifi_csi_filter_config_t7cbw_bmpE "永久链接至目标")
    :   b`0001:20MHz, b`0010:40MHz, b`0011: 20Mhz || 40Mhz

    uint8_t filter_mac_addr_type[](#_CPPv4N24wifi_csi_filter_config_t20filter_mac_addr_typeE "永久链接至目标")
    :   0:all mac;1:src && dst;2: dst only; 3:src only; 4:src || dst

    uint8_t filter_src_mac_num[](#_CPPv4N24wifi_csi_filter_config_t18filter_src_mac_numE "永久链接至目标")
    :   Number of source MAC addresses to filter

    uint8_t filter_src_mac[WIFI_MAC_LEN * FILTER_SRC_MAC_MAX][](#_CPPv4N24wifi_csi_filter_config_t14filter_src_macE "永久链接至目标")
    :   Source MAC filter list (max 16 entries)

    uint8_t filter_dst_mac_num[](#_CPPv4N24wifi_csi_filter_config_t18filter_dst_mac_numE "永久链接至目标")
    :   Number of destination MAC addresses to filter

    uint8_t filter_dst_mac[WIFI_MAC_LEN * FILTER_DST_MAC_MAX][](#_CPPv4N24wifi_csi_filter_config_t14filter_dst_macE "永久链接至目标")
    :   Destination MAC filter list (max 8 entries)

    uint32_t filter_mgmt_frame_bmp[](#_CPPv4N24wifi_csi_filter_config_t21filter_mgmt_frame_bmpE "永久链接至目标")
    :   Bitmap for management frames to capture ,enable:0x80000000

    uint32_t filter_ctrl_frame_bmp[](#_CPPv4N24wifi_csi_filter_config_t21filter_ctrl_frame_bmpE "永久链接至目标")
    :   Bitmap for control frames to capture ,enable:0x80000000

    uint32_t filter_data_frame_bmp[](#_CPPv4N24wifi_csi_filter_config_t21filter_data_frame_bmpE "永久链接至目标")
    :   Bitmap for data frames to capture ,enable:0x80000000

struct wifi_csi_receive_mode_config_t[](#_CPPv430wifi_csi_receive_mode_config_t "永久链接至目标")
:   Public Members

    bool enable[](#_CPPv4N30wifi_csi_receive_mode_config_t6enableE "永久链接至目标")
    :   enable or disable csi pure receiving, true: enable, false: disable

    [wifi_csi_filter_config_t](#_CPPv424wifi_csi_filter_config_t "wifi_csi_filter_config_t") filter_config[](#_CPPv4N30wifi_csi_receive_mode_config_t13filter_configE "永久链接至目标")
    :   filter config

struct wifi_rx_pkt_t[](#_CPPv413wifi_rx_pkt_t "永久链接至目标")
:   Public Members

    uint8_t proto_type[](#_CPPv4N13wifi_rx_pkt_t10proto_typeE "永久链接至目标")
    :   0x0:non HT packet; 0x2:HT packet;0x4:VHT packet;0x5:HE packet

    uint8_t band[](#_CPPv4N13wifi_rx_pkt_t4bandE "永久链接至目标")
    :   0x0:2.4G; 0x1:5G

    uint8_t pri_chan[](#_CPPv4N13wifi_rx_pkt_t8pri_chanE "永久链接至目标")
    :   primary channel on which this packet is received

    uint8_t rate[](#_CPPv4N13wifi_rx_pkt_t4rateE "永久链接至目标")
    :   PHY rate encoding of the packet. Only valid for non-HT packet

    uint8_t mcs[](#_CPPv4N13wifi_rx_pkt_t3mcsE "永久链接至目标")
    :   Modulation Coding Scheme. Only valid for HT,VHT,HE packet

    uint8_t cbw[](#_CPPv4N13wifi_rx_pkt_t3cbwE "永久链接至目标")
    :   Channel Bandwidth of the packet. 0: 20MHz; 1: 40MHz

    int8_t rssi[](#_CPPv4N13wifi_rx_pkt_t4rssiE "永久链接至目标")
    :   Received Signal Strength Indicator(RSSI) of packet. unit: dBm

    uint8_t snr[](#_CPPv4N13wifi_rx_pkt_t3snrE "永久链接至目标")
    :   SNR of AGC stage

    uint8_t agc_gain[](#_CPPv4N13wifi_rx_pkt_t8agc_gainE "永久链接至目标")
    :   Post-AGC link gain

    uint8_t gi_type[](#_CPPv4N13wifi_rx_pkt_t7gi_typeE "永久链接至目标")
    :   Guide Interval(GI).

    uint8_t stbc[](#_CPPv4N13wifi_rx_pkt_t4stbcE "永久链接至目标")
    :   Space Time Block Code(STBC). 0: non STBC packet; 1: STBC packet

    uint8_t pkt_len[](#_CPPv4N13wifi_rx_pkt_t7pkt_lenE "永久链接至目标")
    :   length of packet including Frame Check Sequence(FCS)

    uint8_t src_mac[WIFI_MAC_LEN][](#_CPPv4N13wifi_rx_pkt_t7src_macE "永久链接至目标")
    :   Source MAC Address of the CSI info receive

    uint8_t dst_mac[WIFI_MAC_LEN][](#_CPPv4N13wifi_rx_pkt_t7dst_macE "永久链接至目标")
    :   Destination MAC Address of the CSI info receive

    uint32_t timestamp[](#_CPPv4N13wifi_rx_pkt_t9timestampE "永久链接至目标")
    :   timestamp. The local time when this packet is received. unit: microsecond

struct csi_cfr_t[](#_CPPv49csi_cfr_t "永久链接至目标")
:   Public Members

    float real[](#_CPPv4N9csi_cfr_t4realE "永久链接至目标")
    :   csi real part

    float imag[](#_CPPv4N9csi_cfr_t4imagE "永久链接至目标")
    :   csi imaginary part

struct csi_info_t[](#_CPPv410csi_info_t "永久链接至目标")
:   Public Members

    uint8_t ltf_type[](#_CPPv4N10csi_info_t8ltf_typeE "永久链接至目标")
    :   0:invalid; 1:L-LTF; 2:HT_LTF; 3: VHT_LTF; 4: HE; 5: STBC_HT_LTF; 6: STBC_VHT_LTF; 7: STBC_HE_LTF

    uint8_t sc_num[](#_CPPv4N10csi_info_t6sc_numE "永久链接至目标")
    :   The number of CSI subcarrier

    struct [csi_cfr_t](#_CPPv49csi_cfr_t "csi_cfr_t") *csi_data[](#_CPPv4N10csi_info_t8csi_dataE "永久链接至目标")
    :   pointer to csi_data, data_len is sc_num

struct wifi_csi_info_t[](#_CPPv415wifi_csi_info_t "永久链接至目标")
:   Public Members

    struct [wifi_rx_pkt_t](#_CPPv413wifi_rx_pkt_t "wifi_rx_pkt_t") rx_ctrl[](#_CPPv4N15wifi_csi_info_t7rx_ctrlE "永久链接至目标")
    :   rx packet ctrl info

    struct [csi_info_t](#_CPPv410csi_info_t "csi_info_t") csi_info[MAX_NUM][](#_CPPv4N15wifi_csi_info_t8csi_infoE "永久链接至目标")
    :   csi data info, max is 3

struct wifi_signal_info_t[](#_CPPv418wifi_signal_info_t "永久链接至目标")
:   Public Members

    uint32_t frequency[](#_CPPv4N18wifi_signal_info_t9frequencyE "永久链接至目标")
    :   frequency of the signal

    int current_signal[](#_CPPv4N18wifi_signal_info_t14current_signalE "永久链接至目标")
    :   current signal

    int avg_signal[](#_CPPv4N18wifi_signal_info_t10avg_signalE "永久链接至目标")
    :   average signal

    int current_noise[](#_CPPv4N18wifi_signal_info_t13current_noiseE "永久链接至目标")
    :   current noise

struct tx_stats_t[](#_CPPv410tx_stats_t "永久链接至目标")
:   Wi-Fi tx statistics.

    Public Members

    uint32_t tx_singel_total[](#_CPPv4N10tx_stats_t15tx_singel_totalE "永久链接至目标")
    :   tx single mpdu total count

    uint32_t tx_singel_retry[](#_CPPv4N10tx_stats_t15tx_singel_retryE "永久链接至目标")
    :   tx single mpdu retry count

    uint32_t tx_agg_total[](#_CPPv4N10tx_stats_t12tx_agg_totalE "永久链接至目标")
    :   tx mpdu of ampdu total count

    uint32_t tx_agg_fail[](#_CPPv4N10tx_stats_t11tx_agg_failE "永久链接至目标")
    :   tx mpdu of ampdu fail count

struct wifi_tx_pwr_lmt_t[](#_CPPv417wifi_tx_pwr_lmt_t "永久链接至目标")
:   Public Members

    [wifi_regulation_t](#_CPPv417wifi_regulation_t "wifi_regulation_t") regulation[](#_CPPv4N17wifi_tx_pwr_lmt_t10regulationE "永久链接至目标")
    :   region regulation 0 REGUALTION_NULL 1 REGUALTION_FCC 2 REGUALTION_ETSI 3 REGUALTION_JP 4 REGUALTION_EXT

    [wifi_ratesection_t](#_CPPv418wifi_ratesection_t "wifi_ratesection_t") ratesection[](#_CPPv4N17wifi_tx_pwr_lmt_t11ratesectionE "永久链接至目标")
    :   ratesection 0 RATE_NULL 1 RATE_CCK 2 RATE_OFDM 3 RATE_HT 4 RATE_VHT 5 RATE_HE

    uint8_t channel[](#_CPPv4N17wifi_tx_pwr_lmt_t7channelE "永久链接至目标")
    :   channel range from 1-14

    uint8_t value[](#_CPPv4N17wifi_tx_pwr_lmt_t5valueE "永久链接至目标")
    :   value max tx power


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

WIFI_MAX_SCAN_CHAN_DUR[](#c.WIFI_MAX_SCAN_CHAN_DUR "永久链接至目标")
:   scan duration param, need less than 200ms

WIFI_CHANNEL_NUM_2G4[](#c.WIFI_CHANNEL_NUM_2G4 "永久链接至目标")
:   Maximum supported 2.4G channel number

WIFI_CHANNEL_NUM_5G[](#c.WIFI_CHANNEL_NUM_5G "永久链接至目标")
:   Maximum supported 5G channel numbe

WIFI_2BAND_MAX_CHAN_NUM[](#c.WIFI_2BAND_MAX_CHAN_NUM "永久链接至目标")

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

WIFI_DEFAULT_FTM_CONFIG()[](#c.WIFI_DEFAULT_FTM_CONFIG "永久链接至目标")
:   default FTM configuration

BK_MAX_STA_TYPE[](#c.BK_MAX_STA_TYPE "永久链接至目标")

OUI_BEKEN[](#c.OUI_BEKEN "永久链接至目标")

WLAN_EID_VENDOR_SPECIFIC[](#c.WLAN_EID_VENDOR_SPECIFIC "永久链接至目标")

FILTER_SRC_MAC_MAX[](#c.FILTER_SRC_MAC_MAX "永久链接至目标")
:   CSI configuration and results.

    Wi-Fi Channel State Information configuration and results.

FILTER_DST_MAC_MAX[](#c.FILTER_DST_MAC_MAX "永久链接至目标")

MAX_NUM[](#c.MAX_NUM "永久链接至目标")


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


    **Attention**
    :   2. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

typedef struct [wifi_rlk_chan_info](#_CPPv418wifi_rlk_chan_info "wifi_rlk_chan_info") wifi_rlk_chan_info_t[](#_CPPv420wifi_rlk_chan_info_t "永久链接至目标")

typedef struct [wifi_rlk_base_info](#_CPPv418wifi_rlk_base_info "wifi_rlk_base_info") wifi_rlk_base_info_t[](#_CPPv420wifi_rlk_base_info_t "永久链接至目标")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_rlk_scan_cfm_cb_t)(void)[](#_CPPv422wifi_rlk_scan_cfm_cb_t "永久链接至目标")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_filter_cb_t)(const uint8_t *frame, uint32_t len, const [wifi_frame_info_t](#_CPPv417wifi_frame_info_t "wifi_frame_info_t") *frame_info)[](#_CPPv416wifi_filter_cb_t "永久链接至目标")
:   Filter callback to receive frames relayed by WiFi driver.


    **Attention**
    :   1. The memory of frame and frame_info will be freed immediately when the callback is returned. If we want to use the frame or frame_info in other task, make a copy of them and handle them accordingly.


    **Attention**
    :   2. Don’t do too much work in the callback because the callback is called in context of WiFi core thread, too much work may impact the performance of WiFi.

typedef void (*wifi_csi_cb_t)(struct [wifi_csi_info_t](#_CPPv415wifi_csi_info_t "wifi_csi_info_t") *info)[](#_CPPv413wifi_csi_cb_t "永久链接至目标")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_beacon_cc_rxed_t)(void *ctxt, uint8_t *cc, uint8_t cc_len)[](#_CPPv421wifi_beacon_cc_rxed_t "永久链接至目标")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_get_vsie_cb_t)(void *vendor_ie, uint8_t frame_type)[](#_CPPv418wifi_get_vsie_cb_t "永久链接至目标")
:   wifi get vsie cb interface

    Param void*
    :   vendor_ie

    Param frame
    :   type 1: probe response(or beacon) 2: assoc response

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (*wifi_bcnmiss_cb_t)(void)[](#_CPPv417wifi_bcnmiss_cb_t "永久链接至目标")
:   wifi beacon miss cb interface


### Enumerations[](#enumerations "永久链接至标题")

enum wifi_band_t[](#_CPPv411wifi_band_t "永久链接至目标")
:   enum ieee80211_band - supported frequency bands

    The bands are assigned this way because the supported bitrates differ in these bands.

    @IEEE80211_BAND_2GHZ: 2.4GHz ISM band @IEEE80211_BAND_5GHZ: around 5GHz band (4.9-5.7) @IEEE80211_BAND_6GHZ: around 6GHz band (5.925-7.125) @IEEE80211_BAND_60GHZ: around 60 GHz band (58.32 - 64.80 GHz) @IEEE80211_NUM_BANDS: number of defined bands


    *Values:*

    enumerator IEEE80211_BAND_2GHZ[](#_CPPv4N11wifi_band_t19IEEE80211_BAND_2GHZE "永久链接至目标")

    enumerator IEEE80211_BAND_5GHZ[](#_CPPv4N11wifi_band_t19IEEE80211_BAND_5GHZE "永久链接至目标")

    enumerator IEEE80211_BAND_6GHZ[](#_CPPv4N11wifi_band_t19IEEE80211_BAND_6GHZE "永久链接至目标")

    enumerator IEEE80211_BAND_60GHZ[](#_CPPv4N11wifi_band_t20IEEE80211_BAND_60GHZE "永久链接至目标")

    enumerator IEEE80211_NUM_BANDS[](#_CPPv4N11wifi_band_t19IEEE80211_NUM_BANDSE "永久链接至目标")

enum wifi_event_t[](#_CPPv412wifi_event_t "永久链接至目标")
:   WiFi public event type.


    *Values:*

    enumerator EVENT_WIFI_SCAN_DONE[](#_CPPv4N12wifi_event_t20EVENT_WIFI_SCAN_DONEE "永久链接至目标")
    :   WiFi scan done event

    enumerator EVENT_WIFI_CSI_DATA_IND[](#_CPPv4N12wifi_event_t23EVENT_WIFI_CSI_DATA_INDE "永久链接至目标")

    enumerator EVENT_WIFI_CSI_ALG_IND[](#_CPPv4N12wifi_event_t22EVENT_WIFI_CSI_ALG_INDE "永久链接至目标")

    enumerator EVENT_WIFI_START[](#_CPPv4N12wifi_event_t16EVENT_WIFI_STARTE "永久链接至目标")
    :   WiFi start event

    enumerator EVENT_WIFI_STOP[](#_CPPv4N12wifi_event_t15EVENT_WIFI_STOPE "永久链接至目标")
    :   WiFi stop event

    enumerator EVENT_WIFI_STA_CONNECTED[](#_CPPv4N12wifi_event_t24EVENT_WIFI_STA_CONNECTEDE "永久链接至目标")
    :   The BK STA is connected

    enumerator EVENT_WIFI_STA_DISCONNECTED[](#_CPPv4N12wifi_event_t27EVENT_WIFI_STA_DISCONNECTEDE "永久链接至目标")
    :   The BK STA is disconnected

    enumerator EVENT_WIFI_AP_CONNECTED[](#_CPPv4N12wifi_event_t23EVENT_WIFI_AP_CONNECTEDE "永久链接至目标")
    :   A STA is connected to the BK AP

    enumerator EVENT_WIFI_AP_DISCONNECTED[](#_CPPv4N12wifi_event_t26EVENT_WIFI_AP_DISCONNECTEDE "永久链接至目标")
    :   A STA is disconnected from the BK AP

    enumerator EVENT_WIFI_NETWORK_FOUND[](#_CPPv4N12wifi_event_t24EVENT_WIFI_NETWORK_FOUNDE "永久链接至目标")
    :   The BK STA find target AP

    enumerator EVENT_WIFI_BEACON_HINT[](#_CPPv4N12wifi_event_t22EVENT_WIFI_BEACON_HINTE "永久链接至目标")
    :   Beacon found on NO_IR channel

    enumerator EVENT_WIFI_REGDOMAIN_CHANGED[](#_CPPv4N12wifi_event_t28EVENT_WIFI_REGDOMAIN_CHANGEDE "永久链接至目标")
    :   Regulatory domain changed

    enumerator EVENT_WIFI_DTIM_RECEIVED[](#_CPPv4N12wifi_event_t24EVENT_WIFI_DTIM_RECEIVEDE "永久链接至目标")
    :   The BK STA receives DTIM from AP

    enumerator EVENT_WIFI_AWARE_WAKE_INTERVAL_START[](#_CPPv4N12wifi_event_t36EVENT_WIFI_AWARE_WAKE_INTERVAL_STARTE "永久链接至目标")
    :   The BK Aware wake interval start

    enumerator EVENT_WIFI_COUNT[](#_CPPv4N12wifi_event_t16EVENT_WIFI_COUNTE "永久链接至目标")
    :   WiFi event count

enum wifi_err_reason_t[](#_CPPv417wifi_err_reason_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_REASON_RESERVED[](#_CPPv4N17wifi_err_reason_t20WIFI_REASON_RESERVEDE "永久链接至目标")

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

    enumerator WIFI_REASON_SECURITY_LEVEL_NOT_MATCH[](#_CPPv4N17wifi_err_reason_t36WIFI_REASON_SECURITY_LEVEL_NOT_MATCHE "永久链接至目标")
    :   The AP’s security level is too low

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

    enumerator WIFI_SECURITY_TYPE_WAPI_PSK[](#_CPPv4N15wifi_security_t27WIFI_SECURITY_TYPE_WAPI_PSKE "永久链接至目标")

    enumerator WIFI_SECURITY_TYPE_WAPI_CERT[](#_CPPv4N15wifi_security_t28WIFI_SECURITY_TYPE_WAPI_CERTE "永久链接至目标")

    enumerator WIFI_SECURITY_TYPE_WAPI_UNKNOWN[](#_CPPv4N15wifi_security_t31WIFI_SECURITY_TYPE_WAPI_UNKNOWNE "永久链接至目标")

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

    enumerator WIFI_LINKSTATE_STA_CONNECT_FAILED[](#_CPPv4N17wifi_link_state_t33WIFI_LINKSTATE_STA_CONNECT_FAILEDE "永久链接至目标")
    :   sta mode is connec fail

    enumerator WIFI_LINKSTATE_STA_GOT_IP[](#_CPPv4N17wifi_link_state_t25WIFI_LINKSTATE_STA_GOT_IPE "永久链接至目标")
    :   sta mode got ip

    enumerator WIFI_LINKSTATE_STA_SCAN_DONE[](#_CPPv4N17wifi_link_state_t28WIFI_LINKSTATE_STA_SCAN_DONEE "永久链接至目标")

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

enum wifi_regulation_t[](#_CPPv417wifi_regulation_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_REGU_NULL[](#_CPPv4N17wifi_regulation_t14WIFI_REGU_NULLE "永久链接至目标")

    enumerator WIFI_REGU_FCC[](#_CPPv4N17wifi_regulation_t13WIFI_REGU_FCCE "永久链接至目标")

    enumerator WIFI_REGU_ETSI[](#_CPPv4N17wifi_regulation_t14WIFI_REGU_ETSIE "永久链接至目标")

    enumerator WIFI_REGU_MKK[](#_CPPv4N17wifi_regulation_t13WIFI_REGU_MKKE "永久链接至目标")

    enumerator WIFI_REGU_EXT[](#_CPPv4N17wifi_regulation_t13WIFI_REGU_EXTE "永久链接至目标")

enum wifi_ratesection_t[](#_CPPv418wifi_ratesection_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_RS_NULL[](#_CPPv4N18wifi_ratesection_t12WIFI_RS_NULLE "永久链接至目标")

    enumerator WIFI_RS_CCK[](#_CPPv4N18wifi_ratesection_t11WIFI_RS_CCKE "永久链接至目标")

    enumerator WIFI_RS_OFDM[](#_CPPv4N18wifi_ratesection_t12WIFI_RS_OFDME "永久链接至目标")

    enumerator WIFI_RS_HT[](#_CPPv4N18wifi_ratesection_t10WIFI_RS_HTE "永久链接至目标")

    enumerator WIFI_RS_VHT[](#_CPPv4N18wifi_ratesection_t11WIFI_RS_VHTE "永久链接至目标")

    enumerator WIFI_RS_HE[](#_CPPv4N18wifi_ratesection_t10WIFI_RS_HEE "永久链接至目标")

enum wifi_tx_raw_pkt_t[](#_CPPv417wifi_tx_raw_pkt_t "永久链接至目标")
:   *Values:*

    enumerator WIFI_TX_RAW_DATA[](#_CPPv4N17wifi_tx_raw_pkt_t16WIFI_TX_RAW_DATAE "永久链接至目标")
    :   Wi-Fi tx raw data

    enumerator WIFI_TX_RAW_SPECIAL_DATTA[](#_CPPv4N17wifi_tx_raw_pkt_t25WIFI_TX_RAW_SPECIAL_DATTAE "永久链接至目标")
    :   Wi-Fi tx raw speacial data

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

    enumerator WIFI_CAPA_ID_TX_USE_MAX_BW[](#_CPPv4N17wifi_capability_t26WIFI_CAPA_ID_TX_USE_MAX_BWE "永久链接至目标")
    :   Update Wi-Fi TX Use max bandwidth capability

    enumerator WIFI_CAPA_ID_MAX[](#_CPPv4N17wifi_capability_t16WIFI_CAPA_ID_MAXE "永久链接至目标")

enum wifi_legacy_rate_support_t[](#_CPPv426wifi_legacy_rate_support_t "永久链接至目标")
:   enum wifi legacy rate support - Legacy rate support definitions


    *Values:*

    enumerator WIFI_LEGACY_RATE_1MBPS[](#_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_1MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_2MBPS[](#_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_2MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_5_5MBPS[](#_CPPv4N26wifi_legacy_rate_support_t24WIFI_LEGACY_RATE_5_5MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_11MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_11MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_6MBPS[](#_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_6MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_9MBPS[](#_CPPv4N26wifi_legacy_rate_support_t22WIFI_LEGACY_RATE_9MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_12MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_12MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_18MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_18MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_24MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_24MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_36MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_36MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_48MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_48MBPSE "永久链接至目标")

    enumerator WIFI_LEGACY_RATE_54MBPS[](#_CPPv4N26wifi_legacy_rate_support_t23WIFI_LEGACY_RATE_54MBPSE "永久链接至目标")

enum wifi_vht_mcs_support_t[](#_CPPv422wifi_vht_mcs_support_t "永久链接至目标")
:   enum wifi_vht_mcs_support_t - VHT MCS support definitions @WIFI_VHT_MCS_SUPPORT_0_7: MCSes 0-7 are supported for the number of streams @WIFI_VHT_MCS_SUPPORT_0_8: MCSes 0-8 are supported @WIFI_VHT_MCS_SUPPORT_0_9: MCSes 0-9 are supported @WIFI_VHT_MCS_NOT_SUPPORTED: This number of streams isn’t supported


    *Values:*

    enumerator WIFI_VHT_MCS_SUPPORT_0_7[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_7E "永久链接至目标")

    enumerator WIFI_VHT_MCS_SUPPORT_0_8[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_8E "永久链接至目标")

    enumerator WIFI_VHT_MCS_SUPPORT_0_9[](#_CPPv4N22wifi_vht_mcs_support_t24WIFI_VHT_MCS_SUPPORT_0_9E "永久链接至目标")

    enumerator WIFI_VHT_MCS_NOT_SUPPORTED[](#_CPPv4N22wifi_vht_mcs_support_t26WIFI_VHT_MCS_NOT_SUPPORTEDE "永久链接至目标")

enum wifi_he_mcs_support_t[](#_CPPv421wifi_he_mcs_support_t "永久链接至目标")
:   enum wifi_he_mcs_support_t - HE MCS support definitions @WIFI_HE_MCS_SUPPORT_0_7: MCSes 0-7 are supported for the number of streams @WIFI_HE_MCS_SUPPORT_0_9: MCSes 0-9 are supported @WIFI_HE_MCS_SUPPORT_0_11: MCSes 0-11 are supported @WIFI_HE_MCS_NOT_SUPPORTED: This number of streams isn’t supported


    *Values:*

    enumerator WIFI_HE_MCS_SUPPORT_0_7[](#_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_7E "永久链接至目标")

    enumerator WIFI_HE_MCS_SUPPORT_0_9[](#_CPPv4N21wifi_he_mcs_support_t23WIFI_HE_MCS_SUPPORT_0_9E "永久链接至目标")

    enumerator WIFI_HE_MCS_SUPPORT_0_11[](#_CPPv4N21wifi_he_mcs_support_t24WIFI_HE_MCS_SUPPORT_0_11E "永久链接至目标")

    enumerator WIFI_HE_MCS_NOT_SUPPORTED[](#_CPPv4N21wifi_he_mcs_support_t25WIFI_HE_MCS_NOT_SUPPORTEDE "永久链接至目标")

enum wifi_video_quality_t[](#_CPPv420wifi_video_quality_t "永久链接至目标")
:   enum wifi_video_quality_t - video quality definitions @WIFI_VIDEO_QUALITY_FD: video quality choose Fluent definition(FD) @WIFI_VIDEO_QUALITY_SD: video quality choose Standard definition(SD) @WIFI_VIDEO_QUALITY_HD: video quality choose High definition(HD)


    *Values:*

    enumerator WIFI_VIDEO_QUALITY_FD[](#_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_FDE "永久链接至目标")

    enumerator WIFI_VIDEO_QUALITY_SD[](#_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_SDE "永久链接至目标")

    enumerator WIFI_VIDEO_QUALITY_HD[](#_CPPv4N20wifi_video_quality_t21WIFI_VIDEO_QUALITY_HDE "永久链接至目标")

enum wifi_sta_vsie[](#_CPPv413wifi_sta_vsie "永久链接至目标")
:   *Values:*

    enumerator WIFI_VENDOR_ELEM_ASSOC_REQ[](#_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_ASSOC_REQE "永久链接至目标")

    enumerator WIFI_VENDOR_ELEM_PROBE_REQ[](#_CPPv4N13wifi_sta_vsie26WIFI_VENDOR_ELEM_PROBE_REQE "永久链接至目标")

    enumerator NUM_WIFI_VENDOR_ELEM_FRAMES[](#_CPPv4N13wifi_sta_vsie27NUM_WIFI_VENDOR_ELEM_FRAMESE "永久链接至目标")

enum wifi_pkt_dbg_bit[](#_CPPv416wifi_pkt_dbg_bit "永久链接至目标")
:   *Values:*

    enumerator WIFI_TX_DBG_LOG_DATA_PKT[](#_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_DATA_PKTE "永久链接至目标")

    enumerator WIFI_TX_DBG_LOG_MGMT_PKT[](#_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_MGMT_PKTE "永久链接至目标")

    enumerator WIFI_TX_DBG_LOG_PUSH_PKT[](#_CPPv4N16wifi_pkt_dbg_bit24WIFI_TX_DBG_LOG_PUSH_PKTE "永久链接至目标")

    enumerator WIFI_RX_DBG_LOG_DATA_PKT[](#_CPPv4N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_DATA_PKTE "永久链接至目标")

    enumerator WIFI_RX_DBG_LOG_MGMT_PKT[](#_CPPv4N16wifi_pkt_dbg_bit24WIFI_RX_DBG_LOG_MGMT_PKTE "永久链接至目标")

enum sta_type[](#_CPPv48sta_type "永久链接至目标")
:   *Values:*

    enumerator STA_TYPE1[](#_CPPv4N8sta_type9STA_TYPE1E "永久链接至目标")

    enumerator STA_TYPE2[](#_CPPv4N8sta_type9STA_TYPE2E "永久链接至目标")

    enumerator STA_TYPE3[](#_CPPv4N8sta_type9STA_TYPE3E "永久链接至目标")

    enumerator STA_TYPE4[](#_CPPv4N8sta_type9STA_TYPE4E "永久链接至目标")

    enumerator MAX_STA_TYPE[](#_CPPv4N8sta_type12MAX_STA_TYPEE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_20 "永久链接至目标")
:   *Values:*

    enumerator SCAN_TYPE_CC[](#_CPPv4NUt2_2012SCAN_TYPE_CCE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_21 "永久链接至目标")
:   *Values:*

    enumerator CSI_RATE_6M[](#_CPPv4NUt2_2111CSI_RATE_6ME "永久链接至目标")

    enumerator CSI_RATE_9M[](#_CPPv4NUt2_2111CSI_RATE_9ME "永久链接至目标")

    enumerator CSI_RATE_12M[](#_CPPv4NUt2_2112CSI_RATE_12ME "永久链接至目标")

    enumerator CSI_RATE_18M[](#_CPPv4NUt2_2112CSI_RATE_18ME "永久链接至目标")

    enumerator CSI_RATE_24M[](#_CPPv4NUt2_2112CSI_RATE_24ME "永久链接至目标")

    enumerator CSI_RATE_36M[](#_CPPv4NUt2_2112CSI_RATE_36ME "永久链接至目标")

    enumerator CSI_RATE_48M[](#_CPPv4NUt2_2112CSI_RATE_48ME "永久链接至目标")

    enumerator CSI_RATE_54M[](#_CPPv4NUt2_2112CSI_RATE_54ME "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_22 "永久链接至目标")
:   BC/MC Filter.


    *Values:*

    enumerator WIFI_BCMC_CLOSE[](#_CPPv4NUt2_2215WIFI_BCMC_CLOSEE "永久链接至目标")

    enumerator WIFI_MC_ON[](#_CPPv4NUt2_2210WIFI_MC_ONE "永久链接至目标")

    enumerator WIFI_BC_ON[](#_CPPv4NUt2_2210WIFI_BC_ONE "永久链接至目标")

    enumerator WIFI_BC_MC_ON[](#_CPPv4NUt2_2213WIFI_BC_MC_ONE "永久链接至目标")

enum wifi_standard[](#_CPPv413wifi_standard "永久链接至目标")
:   IEEE 802.11 Standards.


    *Values:*

    enumerator WIFI_STANDARD_NONE[](#_CPPv4N13wifi_standard18WIFI_STANDARD_NONEE "永久链接至目标")

    enumerator WIFI_STANDARD_11A[](#_CPPv4N13wifi_standard17WIFI_STANDARD_11AE "永久链接至目标")

    enumerator WIFI_STANDARD_11B[](#_CPPv4N13wifi_standard17WIFI_STANDARD_11BE "永久链接至目标")

    enumerator WIFI_STANDARD_11G[](#_CPPv4N13wifi_standard17WIFI_STANDARD_11GE "永久链接至目标")

    enumerator WIFI_STANDARD_11N[](#_CPPv4N13wifi_standard17WIFI_STANDARD_11NE "永久链接至目标")

    enumerator WIFI_STANDARD_11AC[](#_CPPv4N13wifi_standard18WIFI_STANDARD_11ACE "永久链接至目标")

    enumerator WIFI_STANDARD_11AX[](#_CPPv4N13wifi_standard18WIFI_STANDARD_11AXE "永久链接至目标")

    enumerator WIFI_STANDARD_NONE_POLAR[](#_CPPv4N13wifi_standard24WIFI_STANDARD_NONE_POLARE "永久链接至目标")

    enumerator WIFI_STANDARD_MAX[](#_CPPv4N13wifi_standard17WIFI_STANDARD_MAXE "永久链接至目标")
