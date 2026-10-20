---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_spdif.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-spdif"></a>

# DRV\_SPDIF

<a id="drv-spdif-api-status"></a>

## DRV\_SPDIF API Status

| API |
| --- |
| [`drv_spdif_init()`](#_CPPv414drv_spdif_initv "drv_spdif_init") |
| [`drv_spdif_deinit()`](#_CPPv416drv_spdif_deinitv "drv_spdif_deinit") |
| [`drv_spdif_config()`](#_CPPv416drv_spdif_configP14spdif_config_t "drv_spdif_config") |
| [`drv_spdif_enable()`](#_CPPv416drv_spdif_enablev "drv_spdif_enable") |
| [`drv_spdif_disable()`](#_CPPv417drv_spdif_disablev "drv_spdif_disable") |
| [`drv_spdif_register_isr_cbk()`](#_CPPv426drv_spdif_register_isr_cbk20pfunc_drv_spdif_cb_tPv "drv_spdif_register_isr_cbk") |
| [`drv_spdif_get_rx_samplerate()`](#_CPPv427drv_spdif_get_rx_sampleratev "drv_spdif_get_rx_samplerate") |
| [`drv_spdif_get_fifo_cnt()`](#_CPPv422drv_spdif_get_fifo_cntv "drv_spdif_get_fifo_cnt") |
| [`drv_spdif_get_fifo_address()`](#_CPPv426drv_spdif_get_fifo_addressv "drv_spdif_get_fifo_address") |
| [`drv_spdif_set_aempty_threshold()`](#_CPPv430drv_spdif_set_aempty_threshold8uint16_t "drv_spdif_set_aempty_threshold") |
| [`drv_spdif_set_afull_threshold()`](#_CPPv429drv_spdif_set_afull_threshold8uint16_t "drv_spdif_set_afull_threshold") |

<a id="drv-spdif-pin-and-gpio-map"></a>

## DRV\_SPDIF Pin and GPIO Map

| SPDIF Pin | Number |
| --- | --- |
| SPDIF\_TX | 12 |
| SPDIF\_RX | 17 |

<a id="drv-spdif-api-reference"></a>

## DRV\_SPDIF API Reference

<a id="header-file"></a>

### Header File

- [driver/spdif/drv\_spdif.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/spdif/drv_spdif.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_spdif_initv"></a>

<a id="_CPPv314drv_spdif_initv"></a> <a id="_CPPv214drv_spdif_initv"></a> <a id="drv_spdif_init__void"></a> <a id="drv__spdif_8h_1abba105fcedad03d65519a6bbea0f8312"></a> int32\_t drv\_spdif\_init(void)
:   init a spdif device.

    初始化设备，在使用spdif功能前需要调用它获取device instance

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spdif_deinitv"></a>

<a id="_CPPv316drv_spdif_deinitv"></a> <a id="_CPPv216drv_spdif_deinitv"></a> <a id="drv_spdif_deinit__void"></a> <a id="drv__spdif_8h_1a1bcb741565b0d91954aa6eb25a862dfb"></a> int32\_t drv\_spdif\_deinit(void)
:   deinit a spdif device.

    反初始化spdif设备，对drv\_spdif\_init()进行反向操作

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spdif_configP14spdif_config_t"></a>

<a id="_CPPv316drv_spdif_configP14spdif_config_t"></a> <a id="_CPPv216drv_spdif_configP14spdif_config_t"></a> <a id="drv_spdif_config__spdif_config_tP"></a> <a id="drv__spdif_8h_1aeac1c68124ab3ba7401628114f6655e2"></a> int32\_t drv\_spdif\_config([spdif\_config\_t](#_CPPv414spdif_config_t "spdif_config_t") \*p\_config)
:   config spdif parameter.

    对spdif设备参数的配置

    参数:
    :   **p\_config** – **\[in\]** 参数结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spdif_enablev"></a>

<a id="_CPPv316drv_spdif_enablev"></a> <a id="_CPPv216drv_spdif_enablev"></a> <a id="drv_spdif_enable__void"></a> <a id="drv__spdif_8h_1a8793aba829ebd0729030f35491b87954"></a> int32\_t drv\_spdif\_enable(void)
:   enable spdif tramsfer

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_spdif_disablev"></a>

<a id="_CPPv317drv_spdif_disablev"></a> <a id="_CPPv217drv_spdif_disablev"></a> <a id="drv_spdif_disable__void"></a> <a id="drv__spdif_8h_1afbb6258eb96380ed9034e7c951a2dc70"></a> int32\_t drv\_spdif\_disable(void)
:   disable spdif tramsfer

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_spdif_register_isr_cbk20pfunc_drv_spdif_cb_tPv"></a>

<a id="_CPPv326drv_spdif_register_isr_cbk20pfunc_drv_spdif_cb_tPv"></a> <a id="_CPPv226drv_spdif_register_isr_cbk20pfunc_drv_spdif_cb_tPv"></a> <a id="drv_spdif_register_isr_cbk__pfunc_drv_spdif_cb_t.voidP"></a> <a id="drv__spdif_8h_1a296d7cd0508346dbbd579cef4512d2af"></a> int32\_t drv\_spdif\_register\_isr\_cbk([pfunc\_drv\_spdif\_cb\_t](#_CPPv420pfunc_drv_spdif_cb_t "pfunc_drv_spdif_cb_t") pfn\_cb, void \*pv\_arg)
:   register spdif isr callback function

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_spdif_get_rx_sampleratev"></a>

<a id="_CPPv327drv_spdif_get_rx_sampleratev"></a> <a id="_CPPv227drv_spdif_get_rx_sampleratev"></a> <a id="drv_spdif_get_rx_samplerate__void"></a> <a id="drv__spdif_8h_1a1190143897659a92e07ade0bd39b1791"></a> [spdif\_samplerate\_e](#_CPPv418spdif_samplerate_e "spdif_samplerate_e") drv\_spdif\_get\_rx\_samplerate(void)
:   get spdif rx samplerate

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_spdif_get_fifo_cntv"></a>

<a id="_CPPv322drv_spdif_get_fifo_cntv"></a> <a id="_CPPv222drv_spdif_get_fifo_cntv"></a> <a id="drv_spdif_get_fifo_cnt__void"></a> <a id="drv__spdif_8h_1a1bfe6a710b886ecf5d5375e59155816d"></a> uint32\_t drv\_spdif\_get\_fifo\_cnt(void)
:   get the amount of data in spdif fifo

    返回:
    :   amount

<a id="_CPPv426drv_spdif_get_fifo_addressv"></a>

<a id="_CPPv326drv_spdif_get_fifo_addressv"></a> <a id="_CPPv226drv_spdif_get_fifo_addressv"></a> <a id="drv_spdif_get_fifo_address__void"></a> <a id="drv__spdif_8h_1a473c6aed173b7b6c6174f15a3e8f5956"></a> uint32\_t drv\_spdif\_get\_fifo\_address(void)
:   get spdif fifo address

    返回:
    :   address

<a id="_CPPv430drv_spdif_set_aempty_threshold8uint16_t"></a>

<a id="_CPPv330drv_spdif_set_aempty_threshold8uint16_t"></a> <a id="_CPPv230drv_spdif_set_aempty_threshold8uint16_t"></a> <a id="drv_spdif_set_aempty_threshold__uint16_t"></a> <a id="drv__spdif_8h_1a8493af3a764494c17089c41fb684d96a"></a> int32\_t drv\_spdif\_set\_aempty\_threshold(uint16\_t threshold)
:   set spdif fifo almost empty report threshold

    参数:
    :   **threshold** – **\[in\]** 门限值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_spdif_set_afull_threshold8uint16_t"></a>

<a id="_CPPv329drv_spdif_set_afull_threshold8uint16_t"></a> <a id="_CPPv229drv_spdif_set_afull_threshold8uint16_t"></a> <a id="drv_spdif_set_afull_threshold__uint16_t"></a> <a id="drv__spdif_8h_1aa6487d24938552f2b20d4942d3043339"></a> int32\_t drv\_spdif\_set\_afull\_threshold(uint16\_t threshold)
:   set spdif fifo almost full report threshold

    参数:
    :   **threshold** – **\[in\]** 门限值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv414spdif_config_t"></a>

<a id="_CPPv314spdif_config_t"></a> <a id="_CPPv214spdif_config_t"></a> <a id="spdif_config_t"></a> <a id="structspdif__config__t"></a> struct spdif\_config\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv420pfunc_drv_spdif_cb_t"></a>

<a id="_CPPv320pfunc_drv_spdif_cb_t"></a> <a id="_CPPv220pfunc_drv_spdif_cb_t"></a> <a id="pfunc_drv_spdif_cb_t"></a> <a id="drv__spdif_8h_1a77def556d350bb08a9cd49e5a78411ef"></a> typedef void (\*pfunc\_drv\_spdif\_cb\_t)([spdif\_status\_e](#_CPPv414spdif_status_e "spdif_status_e") status, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412spdif_mode_e"></a>

<a id="_CPPv312spdif_mode_e"></a> <a id="_CPPv212spdif_mode_e"></a> <a id="drv__spdif_8h_1afdf8e9688c93bd9b210ec4ba0fff13a0"></a> enum spdif\_mode\_e
:   *Values:*

    <a id="_CPPv4N12spdif_mode_e8SPDIF_RXE"></a>

    <a id="_CPPv3N12spdif_mode_e8SPDIF_RXE"></a> <a id="_CPPv2N12spdif_mode_e8SPDIF_RXE"></a> <a id="drv__spdif_8h_1afdf8e9688c93bd9b210ec4ba0fff13a0a273ce72cbbc29fbb28ff3b0a7aadbce6"></a> enumerator SPDIF\_RX

    <a id="_CPPv4N12spdif_mode_e8SPDIF_TXE"></a>

    <a id="_CPPv3N12spdif_mode_e8SPDIF_TXE"></a> <a id="_CPPv2N12spdif_mode_e8SPDIF_TXE"></a> <a id="drv__spdif_8h_1afdf8e9688c93bd9b210ec4ba0fff13a0a03b4449c29fd484f789d5fd506e3d2da"></a> enumerator SPDIF\_TX

<a id="_CPPv417spdif_chan_mode_e"></a>

<a id="_CPPv317spdif_chan_mode_e"></a> <a id="_CPPv217spdif_chan_mode_e"></a> <a id="drv__spdif_8h_1a6d110471ab3eb5ec3eb1c2462a89837c"></a> enum spdif\_chan\_mode\_e
:   *Values:*

    <a id="_CPPv4N17spdif_chan_mode_e12SPDIF_STEREOE"></a>

    <a id="_CPPv3N17spdif_chan_mode_e12SPDIF_STEREOE"></a> <a id="_CPPv2N17spdif_chan_mode_e12SPDIF_STEREOE"></a> <a id="drv__spdif_8h_1a6d110471ab3eb5ec3eb1c2462a89837ca403c8873ce3c2c789a00daff2ce11a42"></a> enumerator SPDIF\_STEREO

    <a id="_CPPv4N17spdif_chan_mode_e10SPDIF_MONOE"></a>

    <a id="_CPPv3N17spdif_chan_mode_e10SPDIF_MONOE"></a> <a id="_CPPv2N17spdif_chan_mode_e10SPDIF_MONOE"></a> <a id="drv__spdif_8h_1a6d110471ab3eb5ec3eb1c2462a89837ca4fb28c093cf88f31a2c08fbd0a3916da"></a> enumerator SPDIF\_MONO

<a id="_CPPv418spdif_samplerate_e"></a>

<a id="_CPPv318spdif_samplerate_e"></a> <a id="_CPPv218spdif_samplerate_e"></a> <a id="drv__spdif_8h_1ad105807e349d794d752d2f2f53e503a4"></a> enum spdif\_samplerate\_e
:   *Values:*

    <a id="_CPPv4N18spdif_samplerate_e11SPDIF_44_1KE"></a>

    <a id="_CPPv3N18spdif_samplerate_e11SPDIF_44_1KE"></a> <a id="_CPPv2N18spdif_samplerate_e11SPDIF_44_1KE"></a> <a id="drv__spdif_8h_1ad105807e349d794d752d2f2f53e503a4a22400fb0458cd4992526ea91cc1f1371"></a> enumerator SPDIF\_44\_1K

    <a id="_CPPv4N18spdif_samplerate_e9SPDIF_48KE"></a>

    <a id="_CPPv3N18spdif_samplerate_e9SPDIF_48KE"></a> <a id="_CPPv2N18spdif_samplerate_e9SPDIF_48KE"></a> <a id="drv__spdif_8h_1ad105807e349d794d752d2f2f53e503a4ab331482cabdbac4954079a2dbe5f2d99"></a> enumerator SPDIF\_48K

    <a id="_CPPv4N18spdif_samplerate_e9SPDIF_96KE"></a>

    <a id="_CPPv3N18spdif_samplerate_e9SPDIF_96KE"></a> <a id="_CPPv2N18spdif_samplerate_e9SPDIF_96KE"></a> <a id="drv__spdif_8h_1ad105807e349d794d752d2f2f53e503a4a6150feb6a641f14ea750d49d1845c1f0"></a> enumerator SPDIF\_96K

    <a id="_CPPv4N18spdif_samplerate_e10SPDIF_192KE"></a>

    <a id="_CPPv3N18spdif_samplerate_e10SPDIF_192KE"></a> <a id="_CPPv2N18spdif_samplerate_e10SPDIF_192KE"></a> <a id="drv__spdif_8h_1ad105807e349d794d752d2f2f53e503a4aa50a40b3faf01d706916a9f347e04bee"></a> enumerator SPDIF\_192K

<a id="_CPPv414spdif_status_e"></a>

<a id="_CPPv314spdif_status_e"></a> <a id="_CPPv214spdif_status_e"></a> <a id="drv__spdif_8h_1a6b3cc91f841d7d31295fb1c8e359de7b"></a> enum spdif\_status\_e
:   *Values:*

    <a id="_CPPv4N14spdif_status_e12SPDIF_UNDERRE"></a>

    <a id="_CPPv3N14spdif_status_e12SPDIF_UNDERRE"></a> <a id="_CPPv2N14spdif_status_e12SPDIF_UNDERRE"></a> <a id="drv__spdif_8h_1a6b3cc91f841d7d31295fb1c8e359de7baa74f6c0ed21c9b1577add8588b4bb5ad"></a> enumerator SPDIF\_UNDERR

    <a id="_CPPv4N14spdif_status_e12SPDIF_OVRERRE"></a>

    <a id="_CPPv3N14spdif_status_e12SPDIF_OVRERRE"></a> <a id="_CPPv2N14spdif_status_e12SPDIF_OVRERRE"></a> <a id="drv__spdif_8h_1a6b3cc91f841d7d31295fb1c8e359de7ba90ac65f5fd2c7fdc781bad6a3a80dbc3"></a> enumerator SPDIF\_OVRERR

    <a id="_CPPv4N14spdif_status_e13SPDIF_SYNCERRE"></a>

    <a id="_CPPv3N14spdif_status_e13SPDIF_SYNCERRE"></a> <a id="_CPPv2N14spdif_status_e13SPDIF_SYNCERRE"></a> <a id="drv__spdif_8h_1a6b3cc91f841d7d31295fb1c8e359de7baaa915b512dad2aec28bf241e590a20cf"></a> enumerator SPDIF\_SYNCERR

    <a id="_CPPv4N14spdif_status_e15SPDIF_PARITYERRE"></a>

    <a id="_CPPv3N14spdif_status_e15SPDIF_PARITYERRE"></a> <a id="_CPPv2N14spdif_status_e15SPDIF_PARITYERRE"></a> <a id="drv__spdif_8h_1a6b3cc91f841d7d31295fb1c8e359de7babae74f34a21c51ade54e1d96094c0d32"></a> enumerator SPDIF\_PARITYERR
