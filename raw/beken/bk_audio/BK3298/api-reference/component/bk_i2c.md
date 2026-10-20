---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_i2c.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-i2c"></a>

# BK\_I2C

<a id="bk-i2c-api-status"></a>

## BK\_I2C API Status

| API |
| --- |
| [`bk_i2c_open()`](#_CPPv411bk_i2c_open8uint32_t "bk_i2c_open") |
| [`bk_i2c_close()`](#_CPPv412bk_i2c_close8uint32_t "bk_i2c_close") |
| [`bk_i2c_master_tx_rx()`](#_CPPv419bk_i2c_master_tx_rx8uint32_tP12bk_i2c_blk_t "bk_i2c_master_tx_rx") |
| [`bk_i2c_slave_rx_tx()`](#_CPPv418bk_i2c_slave_rx_tx8uint32_tP12bk_i2c_blk_t "bk_i2c_slave_rx_tx") |

<a id="bk-i2c-api-reference"></a>

## BK\_I2C API Reference

<a id="header-file"></a>

### Header File

- [component/i2c/bk\_i2c.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/i2c/bk_i2c.h)

<a id="functions"></a>

### Functions

<a id="_CPPv411bk_i2c_open8uint32_t"></a>

<a id="_CPPv311bk_i2c_open8uint32_t"></a> <a id="_CPPv211bk_i2c_open8uint32_t"></a> <a id="bk_i2c_open__uint32_t"></a> <a id="bk__i2c_8h_1a05ebf65ce317fd7156d7df094f99c111"></a> uint32\_t bk\_i2c\_open(uint32\_t dev\_index)
:   beken I2C open.

    使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device), \< [I2C\_DEVICE\_NUM](../driver/drv_i2c.md#drv__i2c_8h_1a039d14c826b8b95ba0d9ceeeb21c4220)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv412bk_i2c_close8uint32_t"></a>

<a id="_CPPv312bk_i2c_close8uint32_t"></a> <a id="_CPPv212bk_i2c_close8uint32_t"></a> <a id="bk_i2c_close__uint32_t"></a> <a id="bk__i2c_8h_1a0e9319367d617b0efec9a16762f2137a"></a> int32\_t bk\_i2c\_close(uint32\_t handle)
:   beken I2C close.

    使用I2C结束后需要close,和 [bk\_i2c\_open()](#bk__i2c_8h_1a05ebf65ce317fd7156d7df094f99c111) 是配对的

    参数:
    :   **handle** – **\[in\]** return value of [bk\_i2c\_open()](#bk__i2c_8h_1a05ebf65ce317fd7156d7df094f99c111)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bk_i2c_master_tx_rx8uint32_tP12bk_i2c_blk_t"></a>

<a id="_CPPv319bk_i2c_master_tx_rx8uint32_tP12bk_i2c_blk_t"></a> <a id="_CPPv219bk_i2c_master_tx_rx8uint32_tP12bk_i2c_blk_t"></a> <a id="bk_i2c_master_tx_rx__uint32_t.bk_i2c_blk_tP"></a> <a id="bk__i2c_8h_1a1385910929fe352b8108e058cf22b1ef"></a> int32\_t bk\_i2c\_master\_tx\_rx(uint32\_t handle, [bk\_i2c\_blk\_t](#_CPPv412bk_i2c_blk_t "bk_i2c_blk_t") \*pt\_blk)
:   beken master I2C send and receive.

    使用I2C来发送一些数据出去,然后收一些数据回来（可选）。该函数是一个异步函数

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_i2c\_open()](#bk__i2c_8h_1a05ebf65ce317fd7156d7df094f99c111)
        - **pt\_blk** – **\[in\]** 指向待发送的结构体。pt\_blk-\>pu1\_buf 在 pt\_blk-\>pfn\_cb 调用之前不能被free重用 发送的结果会通过 pt\_blk-\>pfn\_cb 来通知

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418bk_i2c_slave_rx_tx8uint32_tP12bk_i2c_blk_t"></a>

<a id="_CPPv318bk_i2c_slave_rx_tx8uint32_tP12bk_i2c_blk_t"></a> <a id="_CPPv218bk_i2c_slave_rx_tx8uint32_tP12bk_i2c_blk_t"></a> <a id="bk_i2c_slave_rx_tx__uint32_t.bk_i2c_blk_tP"></a> <a id="bk__i2c_8h_1ac5728de9b3f26fd2259ceca00565e070"></a> int32\_t bk\_i2c\_slave\_rx\_tx(uint32\_t handle, [bk\_i2c\_blk\_t](#_CPPv412bk_i2c_blk_t "bk_i2c_blk_t") \*pt\_blk)
:   beken slave I2C receive and response.

    使用I2C来接收一些数据,然后回复一些数据（可选）。该函数是一个异步函数

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_i2c\_open()](#bk__i2c_8h_1a05ebf65ce317fd7156d7df094f99c111)
        - **pt\_blk** – **\[in\]** 指向待发送的结构体。pt\_blk-\>pu1\_buf 在 pt\_blk-\>pfn\_cb 调用之前不能被free重用 发送的结果会通过 pt\_blk-\>pfn\_cb 来通知

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413_bk_i2c_blk_t"></a>

<a id="_CPPv313_bk_i2c_blk_t"></a> <a id="_CPPv213_bk_i2c_blk_t"></a> <a id="_bk_i2c_blk_t"></a> <a id="struct__bk__i2c__blk__t"></a> struct \_bk\_i2c\_blk\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417pfunc_bk_i2c_cb_t"></a>

<a id="_CPPv317pfunc_bk_i2c_cb_t"></a> <a id="_CPPv217pfunc_bk_i2c_cb_t"></a> <a id="pfunc_bk_i2c_cb_t"></a> <a id="bk__i2c_8h_1a0c3aab899b842a97bc12ce7da5f41565"></a> typedef void (\*pfunc\_bk\_i2c\_cb\_t)(uint32\_t handle, int32\_t err\_code, void \*pv\_arg)

<a id="_CPPv412bk_i2c_blk_t"></a>

<a id="_CPPv312bk_i2c_blk_t"></a> <a id="_CPPv212bk_i2c_blk_t"></a> <a id="bk_i2c_blk_t"></a> <a id="bk__i2c_8h_1afabbbb8de57b159bcdc0505f50a21437"></a> typedef struct [\_bk\_i2c\_blk\_t](#_CPPv413_bk_i2c_blk_t "_bk_i2c_blk_t") bk\_i2c\_blk\_t
