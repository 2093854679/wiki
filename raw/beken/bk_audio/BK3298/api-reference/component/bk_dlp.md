---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_dlp.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-dlp"></a>

# BK\_DLP

<a id="bk-dlp-api-status"></a>

## BK\_DLP API Status

| API |
| --- |
| [`bk_dlp_open()`](#_CPPv411bk_dlp_open8uint32_t "bk_dlp_open") |
| [`bk_dlp_close()`](#_CPPv412bk_dlp_close8uint32_t "bk_dlp_close") |
| [`bk_dlp_config()`](#_CPPv413bk_dlp_config8uint32_tP12bk_dlp_cfg_t "bk_dlp_config") |
| [`bk_dlp_start()`](#_CPPv412bk_dlp_start8uint32_tb "bk_dlp_start") |
| [`bk_dlp_stop()`](#_CPPv411bk_dlp_stop8uint32_t "bk_dlp_stop") |
| [`bk_dlp_write()`](#_CPPv412bk_dlp_write8uint32_tP7uint8_t8uint16_t "bk_dlp_write") |
| [`bk_dlp_write_keep_active()`](#_CPPv424bk_dlp_write_keep_active8uint32_tP7uint8_t8uint16_t8uint32_t "bk_dlp_write_keep_active") |
| [`bk_dlp_read()`](#_CPPv411bk_dlp_read8uint32_tP7uint8_t8uint16_t17pfunc_bk_dlp_cb_t "bk_dlp_read") |
| [`bk_dlp_reg_notify_callback()`](#_CPPv426bk_dlp_reg_notify_callback8uint32_t21pfunc_bk_dlp_notify_t "bk_dlp_reg_notify_callback") |
| [`bk_dlp_get_remain_bytes()`](#_CPPv423bk_dlp_get_remain_bytes8uint32_t "bk_dlp_get_remain_bytes") |
| [`bk_dlp_rx_enable()`](#_CPPv416bk_dlp_rx_enable8uint32_tb "bk_dlp_rx_enable") |
| [`bk_dlp_is_dlp_active()`](#_CPPv420bk_dlp_is_dlp_activev "bk_dlp_is_dlp_active") |
| [`bk_dlp_ana_enable()`](#_CPPv417bk_dlp_ana_enableb "bk_dlp_ana_enable") |

<a id="bk-dlp-api-reference"></a>

## BK\_DLP API Reference

<a id="header-file"></a>

### Header File

- [component/dlp/bk\_dlp.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/dlp/bk_dlp.h)

<a id="functions"></a>

### Functions

<a id="_CPPv411bk_dlp_open8uint32_t"></a>

<a id="_CPPv311bk_dlp_open8uint32_t"></a> <a id="_CPPv211bk_dlp_open8uint32_t"></a> <a id="bk_dlp_open__uint32_t"></a> <a id="bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5"></a> uint32\_t bk\_dlp\_open(uint32\_t dev\_index)
:   beken dlp open interface.

    提供dlp open的接口,使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, always equal 0

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv412bk_dlp_close8uint32_t"></a>

<a id="_CPPv312bk_dlp_close8uint32_t"></a> <a id="_CPPv212bk_dlp_close8uint32_t"></a> <a id="bk_dlp_close__uint32_t"></a> <a id="bk__dlp_8h_1a7ab349a37d0ee7b6f3aaae1fb36a4ee5"></a> int32\_t bk\_dlp\_close(uint32\_t handle)
:   beken dlp close.

    使用DLP结束后需要close,调用前需要先 [bk\_dlp\_stop()](#bk__dlp_8h_1a7ca586b3726aa4d8511796173f9bcb0f)

    参数:
    :   **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_dlp_config8uint32_tP12bk_dlp_cfg_t"></a>

<a id="_CPPv313bk_dlp_config8uint32_tP12bk_dlp_cfg_t"></a> <a id="_CPPv213bk_dlp_config8uint32_tP12bk_dlp_cfg_t"></a> <a id="bk_dlp_config__uint32_t.bk_dlp_cfg_tP"></a> <a id="bk__dlp_8h_1ab72c2e5abdc3d2c2d01d8027fe9eb5b7"></a> int32\_t bk\_dlp\_config(uint32\_t handle, [bk\_dlp\_cfg\_t](#_CPPv412bk_dlp_cfg_t "bk_dlp_cfg_t") \*pt\_cfg)
:   dlp config interface.

    在 [bk\_dlp\_start()](#bk__dlp_8h_1a2f6164a4e3f803a4e4bf2afed7f4128d) 之前需要先进行相关参数的配置

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **pt\_cfg** – **\[in\]** pointer to the config struct

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_dlp_start8uint32_tb"></a>

<a id="_CPPv312bk_dlp_start8uint32_tb"></a> <a id="_CPPv212bk_dlp_start8uint32_tb"></a> <a id="bk_dlp_start__uint32_t.b"></a> <a id="bk__dlp_8h_1a2f6164a4e3f803a4e4bf2afed7f4128d"></a> int32\_t bk\_dlp\_start(uint32\_t handle, bool master\_tx\_first)
:   beken dlp start.

    start DLP function after config dlp parameter

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **master\_tx\_first** – **\[in\]** true: tx first for master false: rx first for slave

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411bk_dlp_stop8uint32_t"></a>

<a id="_CPPv311bk_dlp_stop8uint32_t"></a> <a id="_CPPv211bk_dlp_stop8uint32_t"></a> <a id="bk_dlp_stop__uint32_t"></a> <a id="bk__dlp_8h_1a7ca586b3726aa4d8511796173f9bcb0f"></a> int32\_t bk\_dlp\_stop(uint32\_t handle)
:   beken dlp stop.

    stop dlp function, 和 [bk\_dlp\_start()](#bk__dlp_8h_1a2f6164a4e3f803a4e4bf2afed7f4128d) 的动作相反

    参数:
    :   **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_dlp_write8uint32_tP7uint8_t8uint16_t"></a>

<a id="_CPPv312bk_dlp_write8uint32_tP7uint8_t8uint16_t"></a> <a id="_CPPv212bk_dlp_write8uint32_tP7uint8_t8uint16_t"></a> <a id="bk_dlp_write__uint32_t.uint8_tP.uint16_t"></a> <a id="bk__dlp_8h_1aa6b13eb2ce1958dc6c70ee0720258257"></a> int32\_t bk\_dlp\_write(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len)
:   beken dlp write interface.

    使用DLP来发送一些数据出去,该函数是一个同步发送函数，在送走数据后才会返回

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **pu1\_buf** – **\[in\]** pointer to the send buffer
        - **buf\_len** – **\[in\]** send buffer length in bytes

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424bk_dlp_write_keep_active8uint32_tP7uint8_t8uint16_t8uint32_t"></a>

<a id="_CPPv324bk_dlp_write_keep_active8uint32_tP7uint8_t8uint16_t8uint32_t"></a> <a id="_CPPv224bk_dlp_write_keep_active8uint32_tP7uint8_t8uint16_t8uint32_t"></a> <a id="bk_dlp_write_keep_active__uint32_t.uint8_tP.uint16_t.uint32_t"></a> <a id="bk__dlp_8h_1a844b42ebd099051e9edc5d9d447712c4"></a> int32\_t bk\_dlp\_write\_keep\_active(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len, uint32\_t active\_timeout\_ms)
:   beken dlp write interface.

    使用DLP来发送一些数据出去,该函数是一个同步发送函数，在送走数据后才会返回 和bk\_dlp\_write()不同的是该函数会自动让DLP保持active而不发生reset

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **pu1\_buf** – **\[in\]** pointer to the send buffer
        - **buf\_len** – **\[in\]** send buffer length in bytes
        - **active\_timeout\_ms** – **\[in\]** active DLP after this time

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411bk_dlp_read8uint32_tP7uint8_t8uint16_t17pfunc_bk_dlp_cb_t"></a>

<a id="_CPPv311bk_dlp_read8uint32_tP7uint8_t8uint16_t17pfunc_bk_dlp_cb_t"></a> <a id="_CPPv211bk_dlp_read8uint32_tP7uint8_t8uint16_t17pfunc_bk_dlp_cb_t"></a> <a id="bk_dlp_read__uint32_t.uint8_tP.uint16_t.pfunc_bk_dlp_cb_t"></a> <a id="bk__dlp_8h_1a78fee8a1ff72059d3f79eeb13f46cb07"></a> int32\_t bk\_dlp\_read(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len, [pfunc\_bk\_dlp\_cb\_t](#_CPPv417pfunc_bk_dlp_cb_t "pfunc_bk_dlp_cb_t") pfn\_cb)
:   beken dlp read interface.

    使用DLP收一些数据回来,如果pfn\_cb\=\=NULL，则该函数从dlp收完数据后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等后面数据收完后通过 pfn\_cb进行通知

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **pu1\_buf** – **\[in\]** pointer to the receive buffer
        - **buf\_len** – **\[in\]** receive buffer length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async recevie. it can be NULL if you do not want async recevie

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bk_dlp_reg_notify_callback8uint32_t21pfunc_bk_dlp_notify_t"></a>

<a id="_CPPv326bk_dlp_reg_notify_callback8uint32_t21pfunc_bk_dlp_notify_t"></a> <a id="_CPPv226bk_dlp_reg_notify_callback8uint32_t21pfunc_bk_dlp_notify_t"></a> <a id="bk_dlp_reg_notify_callback__uint32_t.pfunc_bk_dlp_notify_t"></a> <a id="bk__dlp_8h_1acf37f4e8c31d20e9eebcb2611a90aebd"></a> int32\_t bk\_dlp\_reg\_notify\_callback(uint32\_t handle, [pfunc\_bk\_dlp\_notify\_t](#_CPPv421pfunc_bk_dlp_notify_t "pfunc_bk_dlp_notify_t") pfn\_notify)
:   register notify callback for DLP.

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **pfn\_notify** – **\[in\]** 回调函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423bk_dlp_get_remain_bytes8uint32_t"></a>

<a id="_CPPv323bk_dlp_get_remain_bytes8uint32_t"></a> <a id="_CPPv223bk_dlp_get_remain_bytes8uint32_t"></a> <a id="bk_dlp_get_remain_bytes__uint32_t"></a> <a id="bk__dlp_8h_1aeaa26c77abc1f02d6b94c07f6fb9b79d"></a> uint32\_t bk\_dlp\_get\_remain\_bytes(uint32\_t handle)
:   get current rx remain bytes which is not read for user.

    参数:
    :   **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)

    返回:
    :   remain bytes

<a id="_CPPv416bk_dlp_rx_enable8uint32_tb"></a>

<a id="_CPPv316bk_dlp_rx_enable8uint32_tb"></a> <a id="_CPPv216bk_dlp_rx_enable8uint32_tb"></a> <a id="bk_dlp_rx_enable__uint32_t.b"></a> <a id="bk__dlp_8h_1a1b4b74fb3801bab37c1e53276d2fcf1a"></a> int32\_t bk\_dlp\_rx\_enable(uint32\_t handle, bool enable)
:   enable or disable DLP rx.

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_dlp\_open()](#bk__dlp_8h_1a7d6ae36ef4083a3b69ca17700bbc67a5)
        - **enable** – **\[in\]** true: enable rx false: disable rx

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420bk_dlp_is_dlp_activev"></a>

<a id="_CPPv320bk_dlp_is_dlp_activev"></a> <a id="_CPPv220bk_dlp_is_dlp_activev"></a> <a id="bk_dlp_is_dlp_active__void"></a> <a id="bk__dlp_8h_1afeb3b6b904e12df3c1f7545640054bae"></a> bool bk\_dlp\_is\_dlp\_active(void)
:   check DLP is active or not.

    返回:
    :   DLP active state

<a id="_CPPv417bk_dlp_ana_enableb"></a>

<a id="_CPPv317bk_dlp_ana_enableb"></a> <a id="_CPPv217bk_dlp_ana_enableb"></a> <a id="bk_dlp_ana_enable__b"></a> <a id="bk__dlp_8h_1a2e64515036ceb98247e7b05e0d3c3c86"></a> void bk\_dlp\_ana\_enable(bool enable)
:   enable/disable DLP analog switch.

    参数:
    :   **enable** – **\[in\]** true: 打开模拟开关 false: 关闭模拟开关

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv413_bk_dlp_cfg_t"></a>

<a id="_CPPv313_bk_dlp_cfg_t"></a> <a id="_CPPv213_bk_dlp_cfg_t"></a> <a id="_bk_dlp_cfg_t"></a> <a id="struct__bk__dlp__cfg__t"></a> struct \_bk\_dlp\_cfg\_t

<a id="macros"></a>

### Macros

<a id="c.DLP_ACTIVE_PERIOD_MS"></a>

<a id="bk__dlp_8h_1a7e239a0fb72eed03dc6f3e5a3d66c547"></a> DLP\_ACTIVE\_PERIOD\_MS

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417pfunc_bk_dlp_cb_t"></a>

<a id="_CPPv317pfunc_bk_dlp_cb_t"></a> <a id="_CPPv217pfunc_bk_dlp_cb_t"></a> <a id="pfunc_bk_dlp_cb_t"></a> <a id="bk__dlp_8h_1a12ce0810504628a5f74c8f5a91d67043"></a> typedef void (\*pfunc\_bk\_dlp\_cb\_t)(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len, bool attach)

<a id="_CPPv421pfunc_bk_dlp_notify_t"></a>

<a id="_CPPv321pfunc_bk_dlp_notify_t"></a> <a id="_CPPv221pfunc_bk_dlp_notify_t"></a> <a id="pfunc_bk_dlp_notify_t"></a> <a id="bk__dlp_8h_1a5a719e227d23c91c5f621edcec633115"></a> typedef void (\*pfunc\_bk\_dlp\_notify\_t)(bool attach, uint16\_t remain\_bytes)

<a id="_CPPv412bk_dlp_cfg_t"></a>

<a id="_CPPv312bk_dlp_cfg_t"></a> <a id="_CPPv212bk_dlp_cfg_t"></a> <a id="bk_dlp_cfg_t"></a> <a id="bk__dlp_8h_1abfedf531e140d9751d64911ec2cc8673"></a> typedef struct [\_bk\_dlp\_cfg\_t](#_CPPv413_bk_dlp_cfg_t "_bk_dlp_cfg_t") bk\_dlp\_cfg\_t
