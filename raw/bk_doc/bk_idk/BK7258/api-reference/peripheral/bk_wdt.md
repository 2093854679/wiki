# WDT[](#wdt "永久链接至标题")

[[English]](../../../../en/v2.0.1/api-reference/peripheral/bk_wdt.html "../../../../en/v2.0.1/api-reference/peripheral/bk_wdt.html")


## WDT API Status[](#wdt-api-status "永久链接至标题")

| API | BK7258 | BK7258_cp1 |
| --- | --- | --- |
| [`bk_wdt_driver_init()`](#_CPPv418bk_wdt_driver_initv "bk_wdt_driver_init") | Y | Y |
| [`bk_wdt_driver_deinit()`](#_CPPv420bk_wdt_driver_deinitv "bk_wdt_driver_deinit") | Y | Y |
| [`bk_wdt_start()`](#_CPPv412bk_wdt_start8uint32_t "bk_wdt_start") | Y | Y |
| [`bk_wdt_stop()`](#_CPPv411bk_wdt_stopv "bk_wdt_stop") | Y | Y |
| [`bk_wdt_feed()`](#_CPPv411bk_wdt_feedv "bk_wdt_feed") | Y | Y |


## WDT API Reference[](#wdt-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [wdt.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wdt.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wdt.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_wdt_driver_init(void)[](#_CPPv418bk_wdt_driver_initv "永久链接至目标")
:   Init the WDT driver.

    This API init the resoure common:


    - Init WDT driver control memory


    **Attention**
    :   1. This API should be called before any other WDT APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_wdt_driver_deinit(void)[](#_CPPv420bk_wdt_driver_deinitv "永久链接至目标")
:   Deinit the WDT driver.

    This API free all resource related to WDT and power down WDT.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_wdt_start(uint32_t timeout_ms)[](#_CPPv412bk_wdt_start8uint32_t "永久链接至目标")
:   Start the WDT.

    This API start the WDT:


    - Power up the WDT

    - Init the watch dog timer period

    参数
    :   **timeout_ms** – WDT period

    返回
    :   - BK_OK: succeed

        - BK_ERR_WDT_DRIVER_NOT_INIT: WDT driver not init

        - BK_ERR_WDT_INVALID_PERIOD: WDT invalid period

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_wdt_stop(void)[](#_CPPv411bk_wdt_stopv "永久链接至目标")
:   Stop the WDT.

    This API stop the WDT:


    - Reset all configuration of WDT to default value

    - Power down the WDT

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_wdt_feed(void)[](#_CPPv411bk_wdt_feedv "永久链接至目标")
:   Feed the WDT.

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_wdt_get_feed_time(void)[](#_CPPv420bk_wdt_get_feed_timev "永久链接至目标")
:   Get feed watchdog time.

    返回
    :   - BK_OK: succeed

        - others: other errors.

void bk_wdt_set_feed_time(uint32_t dw_set_time)[](#_CPPv420bk_wdt_set_feed_time8uint32_t "永久链接至目标")
:   set feed watchdog time

    返回
    :   - NULL

bool bk_wdt_is_driver_inited(void)[](#_CPPv423bk_wdt_is_driver_initedv "永久链接至目标")
:   Get wdt driver init flag.

    返回
    :   - BK_OK: succeed

        - others: other errors.


## WDT API Typedefs[](#wdt-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [wdt_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wdt_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/wdt_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_WDT_DRIVER_NOT_INIT[](#c.BK_ERR_WDT_DRIVER_NOT_INIT "永久链接至目标")
:   WDT driver not init

BK_ERR_WDT_NOT_INIT[](#c.BK_ERR_WDT_NOT_INIT "永久链接至目标")
:   WDT not init

BK_ERR_WDT_INVALID_PERIOD[](#c.BK_ERR_WDT_INVALID_PERIOD "永久链接至目标")
:   WDT invalid period

BK_ERR_WDT_DEBUG_DISABLED[](#c.BK_ERR_WDT_DEBUG_DISABLED "永久链接至目标")
:   WDT disabled via cmdline flag


### Header File[](#id2 "永久链接至标题")


- [hal/hal_wdt_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_wdt_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_wdt_types.h")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint8_t wdt_unit_t[](#_CPPv410wdt_unit_t "永久链接至目标")
:   wdt uint id
