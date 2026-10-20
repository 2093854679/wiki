---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_dlp_box.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dlp-box-application-functions"></a>

# DLP BOX Application Functions

<a id="app-dlp-box-api-brief"></a>

## APP\_DLP\_BOX API Brief

| Application | Brief |
| --- | --- |
| [`app_dlp_box_init()`](#_CPPv416app_dlp_box_initv "app_dlp_box_init") | initialise DLP application |
| [`app_dlp_box_deinit()`](#_CPPv418app_dlp_box_deinitv "app_dlp_box_deinit") | deinit DLP application |
| [`app_dlp_box_rx_callback_register()`](#_CPPv432app_dlp_box_rx_callback_register21pfunc_dlp_box_rx_cb_t "app_dlp_box_rx_callback_register") | register DLP rx application |
| [`app_dlp_box_tx_data()`](#_CPPv419app_dlp_box_tx_dataP7uint8_t8uint32_t "app_dlp_box_tx_data") | DLP tx application |

<a id="app-dlp-box-api-reference"></a>

## APP\_DLP\_BOX API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_dlp\_box.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_dlp_box.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416app_dlp_box_initv"></a>

<a id="_CPPv316app_dlp_box_initv"></a> <a id="_CPPv216app_dlp_box_initv"></a> <a id="app_dlp_box_init__void"></a> <a id="app__dlp__box_8h_1a1b52f7b7658496c0888dfa63dc521fe7"></a> int32\_t app\_dlp\_box\_init(void)
:   initialise DLP application.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418app_dlp_box_deinitv"></a>

<a id="_CPPv318app_dlp_box_deinitv"></a> <a id="_CPPv218app_dlp_box_deinitv"></a> <a id="app_dlp_box_deinit__void"></a> <a id="app__dlp__box_8h_1a706fdc87e5d3f2028befd8ddf718e7d4"></a> int32\_t app\_dlp\_box\_deinit(void)
:   deinit DLP application.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432app_dlp_box_rx_callback_register21pfunc_dlp_box_rx_cb_t"></a>

<a id="_CPPv332app_dlp_box_rx_callback_register21pfunc_dlp_box_rx_cb_t"></a> <a id="_CPPv232app_dlp_box_rx_callback_register21pfunc_dlp_box_rx_cb_t"></a> <a id="app_dlp_box_rx_callback_register__pfunc_dlp_box_rx_cb_t"></a> <a id="app__dlp__box_8h_1a5f8f7ed5f863a11644996b3492298207"></a> int32\_t app\_dlp\_box\_rx\_callback\_register([pfunc\_dlp\_box\_rx\_cb\_t](#_CPPv421pfunc_dlp_box_rx_cb_t "pfunc_dlp_box_rx_cb_t") p\_func)
:   register DLP rx application.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419app_dlp_box_tx_dataP7uint8_t8uint32_t"></a>

<a id="_CPPv319app_dlp_box_tx_dataP7uint8_t8uint32_t"></a> <a id="_CPPv219app_dlp_box_tx_dataP7uint8_t8uint32_t"></a> <a id="app_dlp_box_tx_data__uint8_tP.uint32_t"></a> <a id="app__dlp__box_8h_1aac4d839eceb26d6abe455493fbca1de4"></a> int32\_t app\_dlp\_box\_tx\_data(uint8\_t \*p\_tx\_data, uint32\_t tx\_len)
:   DLP tx api.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.USE_ATTACH_GPIO"></a>

<a id="app__dlp__box_8h_1ad8246771a26aa40c04c2094fbc3580ca"></a> USE\_ATTACH\_GPIO

<a id="c.DLP_RX_CB_NUM"></a>

<a id="app__dlp__box_8h_1a6a78d49870cdac8e3cb510138a332028"></a> DLP\_RX\_CB\_NUM

<a id="c.DLP_DEFALUT_BAUDRATE"></a>

<a id="app__dlp__box_8h_1a63b29ecaec7b1a3955dcabff5faa84a7"></a> DLP\_DEFALUT\_BAUDRATE

<a id="c.DLP_BUFFER_MAX_SIZE"></a>

<a id="app__dlp__box_8h_1a5b29ad85ec890d3a9cb6fc21d4236d4d"></a> DLP\_BUFFER\_MAX\_SIZE

<a id="c.DLP_FRAME_MAX_TIMEOUT"></a>

<a id="app__dlp__box_8h_1acd60954fa36b3f80bf876b6eccf31aec"></a> DLP\_FRAME\_MAX\_TIMEOUT

<a id="c.DLP_CONNECT_CHECK_TIMEOUT_MS"></a>

<a id="app__dlp__box_8h_1a8748d4793fc61f7310f446e423df6999"></a> DLP\_CONNECT\_CHECK\_TIMEOUT\_MS

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421pfunc_dlp_box_rx_cb_t"></a>

<a id="_CPPv321pfunc_dlp_box_rx_cb_t"></a> <a id="_CPPv221pfunc_dlp_box_rx_cb_t"></a> <a id="pfunc_dlp_box_rx_cb_t"></a> <a id="app__dlp__box_8h_1a3c316b4cf1be4e1a56c09bdb4ac76c9e"></a> typedef int32\_t (\*pfunc\_dlp\_box\_rx\_cb\_t)(uint8\_t \*p\_rx\_data, uint16\_t rx\_len)
