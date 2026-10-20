---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_wdt.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-wdt"></a>

# DRV\_WDT

<a id="drv-wdt-api-status"></a>

## DRV\_WDT API Status

| API |
| --- |
| [`drv_wdt_enable()`](#_CPPv414drv_wdt_enableb "drv_wdt_enable") |
| [`drv_wdt_set()`](#_CPPv411drv_wdt_set8uint32_t "drv_wdt_set") |

<a id="drv-wdt-api-reference"></a>

## DRV\_WDT API Reference

<a id="header-file"></a>

### Header File

- [driver/wdt/drv\_wdt.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/wdt/drv_wdt.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_wdt_enableb"></a>

<a id="_CPPv314drv_wdt_enableb"></a> <a id="_CPPv214drv_wdt_enableb"></a> <a id="drv_wdt_enable__b"></a> <a id="drv__wdt_8h_1a73a7acf6473592c5ca7dd8ad285dd877"></a> void drv\_wdt\_enable(bool enable)

<a id="_CPPv411drv_wdt_set8uint32_t"></a>

<a id="_CPPv311drv_wdt_set8uint32_t"></a> <a id="_CPPv211drv_wdt_set8uint32_t"></a> <a id="drv_wdt_set__uint32_t"></a> <a id="drv__wdt_8h_1a04a8d8c1d96bf554b55c780c4fe4fbc1"></a> void drv\_wdt\_set(uint32\_t val\_period)

<a id="macros"></a>

### Macros

<a id="c.WATCH_DOG_TIMEOUT_SECONDS"></a>

<a id="drv__wdt_8h_1acaf63a8a99f8306105c15be9dd9376c9"></a> WATCH\_DOG\_TIMEOUT\_SECONDS

<a id="c.WATCH_DOG_DISABLE"></a>

<a id="drv__wdt_8h_1ac70dfc24e5f8b37adc9b5b9b1a1a8729"></a> WATCH\_DOG\_DISABLE()
:   disable watch dog

    备注

    通常它需要和 WATCH\_DOG\_ENABLE() 匹配使用

<a id="c.WATCH_DOG_ENABLE"></a>

<a id="drv__wdt_8h_1ad93786d862a09710b499e8463872d62b"></a> WATCH\_DOG\_ENABLE()
:   enable watch dog, it will automatically count and restart the whole chip when it reaches the threshold.

    备注

    通常它需要和 WATCH\_DOG\_DISABLE() 匹配使用

<a id="c.WATCH_DOG_FEED"></a>

<a id="drv__wdt_8h_1a55c2765039d7cc0ff9cb42d87aade10a"></a> WATCH\_DOG\_FEED()
:   feed the watch dog

<a id="c.REBOOT_WITH_WATCHDOG"></a>

<a id="drv__wdt_8h_1a9babad2c7bbac8081412083c08de2bd8"></a> REBOOT\_WITH\_WATCHDOG(x)
:   reboot with watch dog by a small timeout value

<a id="c._WDT_CLOCK_DIV"></a>

<a id="drv__wdt_8h_1a356e3a0f47c03052cb8e87ce2e0e05d9"></a> \_WDT\_CLOCK\_DIV

<a id="c._WDT_PERIOD_VALUE"></a>

<a id="drv__wdt_8h_1a1ecb8ae663fb34b7a02c34bebe133e24"></a> \_WDT\_PERIOD\_VALUE

<a id="c.WDT_PERIOD_SECOND"></a>

<a id="drv__wdt_8h_1aa2c8361a71170311a00668b6b41999f1"></a> WDT\_PERIOD\_SECOND(x)
