---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_mbox.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-mbox"></a>

# BK\_MBOX

<a id="bk-mbox-api-status"></a>

## BK\_MBOX API Status

| API |
| --- |
| [`bk_mbox_open()`](#_CPPv412bk_mbox_open7int32_t "bk_mbox_open") |
| [`bk_mbox_close()`](#_CPPv413bk_mbox_close8uint32_t "bk_mbox_close") |
| [`bk_mbox_write()`](#_CPPv413bk_mbox_write8uint32_tP7uint8_t8uint16_t "bk_mbox_write") |
| [`bk_mbox_write_wait_response()`](#_CPPv427bk_mbox_write_wait_response8uint32_tP7uint8_t8uint16_t "bk_mbox_write_wait_response") |
| [`bk_mbox_read()`](#_CPPv412bk_mbox_read8uint32_tP7uint8_tP8uint16_t "bk_mbox_read") |
| [`bk_mbox_rx_data_is_ready()`](#_CPPv424bk_mbox_rx_data_is_ready8uint32_t "bk_mbox_rx_data_is_ready") |
| [`bk_mbox_reg_rx_ready_callback()`](#_CPPv429bk_mbox_reg_rx_ready_callback8uint32_t20pfunc_mbox_rxready_tPv "bk_mbox_reg_rx_ready_callback") |
| [`bk_mbox_release()`](#_CPPv415bk_mbox_release8uint32_t "bk_mbox_release") |

<a id="bk-mbox-api-reference"></a>

## BK\_MBOX API Reference

<a id="header-file"></a>

### Header File

- [component/mbox/bk\_mbox.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/mbox/bk_mbox.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_mbox_open7int32_t"></a>

<a id="_CPPv312bk_mbox_open7int32_t"></a> <a id="_CPPv212bk_mbox_open7int32_t"></a> <a id="bk_mbox_open__int32_t"></a> <a id="bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297"></a> uint32\_t bk\_mbox\_open(int32\_t remote\_cpu)
:   beken mailbox open.

    参数:
    :   **remote\_cpu** – **\[in\]** CPU\_ID\_xx

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv413bk_mbox_close8uint32_t"></a>

<a id="_CPPv313bk_mbox_close8uint32_t"></a> <a id="_CPPv213bk_mbox_close8uint32_t"></a> <a id="bk_mbox_close__uint32_t"></a> <a id="bk__mbox_8h_1ac92fe08ae4e4f3abeb15c2e1d43e8c44"></a> int32\_t bk\_mbox\_close(uint32\_t handle)
:   beken mailbox close.

    使用mailbox结束后需要close,和 [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297) 是配对的

    参数:
    :   **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_mbox_write8uint32_tP7uint8_t8uint16_t"></a>

<a id="_CPPv313bk_mbox_write8uint32_tP7uint8_t8uint16_t"></a> <a id="_CPPv213bk_mbox_write8uint32_tP7uint8_t8uint16_t"></a> <a id="bk_mbox_write__uint32_t.uint8_tP.uint16_t"></a> <a id="bk__mbox_8h_1a98b05c2379e3ce70ea576c97556e7cbf"></a> int32\_t bk\_mbox\_write(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len)
:   通过mailbox送数据给对方cpu，该函数立即返回

    硬件FIFO数量固定，尽量使用一收一发的工作模式

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)
        - **pu1\_buf** – **\[in\]** pointer to the tx buffer
        - **buf\_len** – **\[in\]** tx buffer length in bytes

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427bk_mbox_write_wait_response8uint32_tP7uint8_t8uint16_t"></a>

<a id="_CPPv327bk_mbox_write_wait_response8uint32_tP7uint8_t8uint16_t"></a> <a id="_CPPv227bk_mbox_write_wait_response8uint32_tP7uint8_t8uint16_t"></a> <a id="bk_mbox_write_wait_response__uint32_t.uint8_tP.uint16_t"></a> <a id="bk__mbox_8h_1ac91a5871b62c0cc69afc057e06e6aed7"></a> int32\_t bk\_mbox\_write\_wait\_response(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len)
:   通过mailbox送数据给对方cpu

    该函数会等到有对方cpu回复后再返回，但是用户需要自己去读取数据

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)
        - **pu1\_buf** – **\[in\]** pointer to the tx buffer
        - **buf\_len** – **\[in\]** tx buffer length in bytes

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_mbox_read8uint32_tP7uint8_tP8uint16_t"></a>

<a id="_CPPv312bk_mbox_read8uint32_tP7uint8_tP8uint16_t"></a> <a id="_CPPv212bk_mbox_read8uint32_tP7uint8_tP8uint16_t"></a> <a id="bk_mbox_read__uint32_t.uint8_tP.uint16_tP"></a> <a id="bk__mbox_8h_1a79a6320b017b86d5e93466e14f1aabfa"></a> int32\_t bk\_mbox\_read(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t \*pu2\_buf\_len)
:   read data from maiblox

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)
        - **pu1\_buf** – **\[in\]** pointer to the rx buffer
        - **pu2\_buf\_len** – **\[out\]** 输出参数，表示这次接收的数据长度

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424bk_mbox_rx_data_is_ready8uint32_t"></a>

<a id="_CPPv324bk_mbox_rx_data_is_ready8uint32_t"></a> <a id="_CPPv224bk_mbox_rx_data_is_ready8uint32_t"></a> <a id="bk_mbox_rx_data_is_ready__uint32_t"></a> <a id="bk__mbox_8h_1a77d5fdaab429f6469133c43d3d729e2b"></a> bool bk\_mbox\_rx\_data\_is\_ready(uint32\_t handle)
:   check if rx data is ready or not.

    参数:
    :   **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)

    返回:
    :   true: data is ready false: no data

<a id="_CPPv429bk_mbox_reg_rx_ready_callback8uint32_t20pfunc_mbox_rxready_tPv"></a>

<a id="_CPPv329bk_mbox_reg_rx_ready_callback8uint32_t20pfunc_mbox_rxready_tPv"></a> <a id="_CPPv229bk_mbox_reg_rx_ready_callback8uint32_t20pfunc_mbox_rxready_tPv"></a> <a id="bk_mbox_reg_rx_ready_callback__uint32_t.pfunc_mbox_rxready_t.voidP"></a> <a id="bk__mbox_8h_1a835474200d7c207b703ad12ee95e3e16"></a> int32\_t bk\_mbox\_reg\_rx\_ready\_callback(uint32\_t handle, [pfunc\_mbox\_rxready\_t](#_CPPv420pfunc_mbox_rxready_t "pfunc_mbox_rxready_t") pfn\_cb, void \*pv\_arg)
:   register rx ready callback.

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)
        - **pfn\_cb** – **\[in\]** callback function for rx ready
        - **pv\_arg** – **\[in\]** argument for callback

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415bk_mbox_release8uint32_t"></a>

<a id="_CPPv315bk_mbox_release8uint32_t"></a> <a id="_CPPv215bk_mbox_release8uint32_t"></a> <a id="bk_mbox_release__uint32_t"></a> <a id="bk__mbox_8h_1ae7f0b9f333edd76c3d6e7e58eaa7b7df"></a> void bk\_mbox\_release(uint32\_t handle)
:   release mailbox for main cpu.

    参数:
    :   **handle** – **\[in\]** return value of [bk\_mbox\_open()](#bk__mbox_8h_1ad378ba13e7d9af43664cc81af53c8297)

    返回:
    :   N/A

<a id="macros"></a>

### Macros

<a id="c.MBOX_EXCHG_MAX_WORD"></a>

<a id="bk__mbox_8h_1a33036e3a02f8782c5cfd8a9785458521"></a> MBOX\_EXCHG\_MAX\_WORD

<a id="c.CacheOffset"></a>

<a id="bk__mbox_8h_1aeb13ce827a8223fff79303e3a7dfff29"></a> CacheOffset

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv420pfunc_mbox_rxready_t"></a>

<a id="_CPPv320pfunc_mbox_rxready_t"></a> <a id="_CPPv220pfunc_mbox_rxready_t"></a> <a id="pfunc_mbox_rxready_t"></a> <a id="bk__mbox_8h_1a83eb7a00d5cace96bf1296d5f2c41e52"></a> typedef void (\*pfunc\_mbox\_rxready\_t)(void \*pv\_arg)

<a id="_CPPv415MAILBOX_CMD_SET"></a>

<a id="_CPPv315MAILBOX_CMD_SET"></a> <a id="_CPPv215MAILBOX_CMD_SET"></a> <a id="MAILBOX_CMD_SET"></a> <a id="bk__mbox_8h_1af4755d92d281336afb7b144dbb139e0c"></a> typedef enum [\_MAILBOX\_CMD\_SET](#_CPPv416_MAILBOX_CMD_SET "_MAILBOX_CMD_SET") MAILBOX\_CMD\_SET

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv416_MAILBOX_CMD_SET"></a>

<a id="_CPPv316_MAILBOX_CMD_SET"></a> <a id="_CPPv216_MAILBOX_CMD_SET"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5"></a> enum \_MAILBOX\_CMD\_SET
:   *Values:*

    <a id="_CPPv4N16_MAILBOX_CMD_SET22MAILBOX_CMD_ENC_SUBSETE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET22MAILBOX_CMD_ENC_SUBSETE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET22MAILBOX_CMD_ENC_SUBSETE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a38815c24ede9abad861f3c1304bd5c71"></a> enumerator MAILBOX\_CMD\_ENC\_SUBSET

    <a id="_CPPv4N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_INITE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_INITE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_INITE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a1db23ca124c2dd043eb2faef97b5669f"></a> enumerator MAILBOX\_CMD\_ENC\_INIT

    <a id="_CPPv4N16_MAILBOX_CMD_SET21MAILBOX_CMD_ENC_UINITE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET21MAILBOX_CMD_ENC_UINITE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET21MAILBOX_CMD_ENC_UINITE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a603b9e79b6bc4017cf92a49d150abe85"></a> enumerator MAILBOX\_CMD\_ENC\_UINIT

    <a id="_CPPv4N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_TRIGE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_TRIGE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET20MAILBOX_CMD_ENC_TRIGE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a2909f258b2060764f1995533b0151807"></a> enumerator MAILBOX\_CMD\_ENC\_TRIG

    <a id="_CPPv4N16_MAILBOX_CMD_SET23MAILBOX_CMD_TEST_SUBSETE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET23MAILBOX_CMD_TEST_SUBSETE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET23MAILBOX_CMD_TEST_SUBSETE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a421c32c63c9711fde7733b515b148cb7"></a> enumerator MAILBOX\_CMD\_TEST\_SUBSET

    <a id="_CPPv4N16_MAILBOX_CMD_SET24MAILBOX_CMD_OTHER_SUBSETE"></a>

    <a id="_CPPv3N16_MAILBOX_CMD_SET24MAILBOX_CMD_OTHER_SUBSETE"></a> <a id="_CPPv2N16_MAILBOX_CMD_SET24MAILBOX_CMD_OTHER_SUBSETE"></a> <a id="bk__mbox_8h_1aaeb75ca589cc76fb053b9c61e7ed15d5a0dba879a4f831e47e6a90961612d1138"></a> enumerator MAILBOX\_CMD\_OTHER\_SUBSET
