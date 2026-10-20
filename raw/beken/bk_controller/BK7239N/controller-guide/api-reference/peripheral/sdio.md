---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/sdio.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sdio-api"></a>

# SDIO API

SDIO (Secure Digital Input/Output) 安全数字输入输出API接口。

<a id="header-file"></a>

## Header File

- [sdio\_host.h](https://github.com/bekencorp/armino/blob/main/components/sdio_host.h)

<a id="functions"></a>

## Functions

<a id="_CPPv424bk_sdio_host_driver_initv"></a>

<a id="_CPPv324bk_sdio_host_driver_initv"></a> <a id="_CPPv224bk_sdio_host_driver_initv"></a> <a id="bk_sdio_host_driver_init__void"></a> <a id="sdio__host_8h_1a6710a4fe7e99e6eb415f422dfca0d915"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_driver\_init(void)
:   Init the sdio host driver.

    This API init the resoure common:

    - Init sdio host driver control memory

    **Attention**
    :   1\. This API should be called before any other sdio host APIs

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_sdio_host_driver_deinitv"></a>

<a id="_CPPv326bk_sdio_host_driver_deinitv"></a> <a id="_CPPv226bk_sdio_host_driver_deinitv"></a> <a id="bk_sdio_host_driver_deinit__void"></a> <a id="sdio__host_8h_1a1144c6d928758cc938e27615fd3afb1c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_driver\_deinit(void)
:   Deinit the sdio host driver.

    This API free all resource related to sdio host and disable sdio host

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_sdio_host_initPK18sdio_host_config_t"></a>

<a id="_CPPv317bk_sdio_host_initPK18sdio_host_config_t"></a> <a id="_CPPv217bk_sdio_host_initPK18sdio_host_config_t"></a> <a id="bk_sdio_host_init__sdio_host_config_tCP"></a> <a id="sdio__host_8h_1a666680fc7ccc064692bdfc92a48fa5a2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_init(const sdio\_host\_config\_t \*config)
:   Init the sdio host.

    This API init the sdio host:

    - Power up the sdio
    - Configure the sdio clock soure to 26M
    - Enable sdio host interrupt
    - Map the sdio to dedicated GPIO port
    - Set the clock frequency and bus width

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - others: other errors.

<a id="_CPPv419bk_sdio_host_deinitv"></a>

<a id="_CPPv319bk_sdio_host_deinitv"></a> <a id="_CPPv219bk_sdio_host_deinitv"></a> <a id="bk_sdio_host_deinit__void"></a> <a id="sdio__host_8h_1a871e7c986d8ffac8508069a3fd18408a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_deinit(void)
:   Deinit the sdio host.

    This API deinit the sdio host:

    - Reset all configuration of sdio host to default value
    - Clear sdio host interrupt status
    - Power down the sdio host
    - Disable sdio host interrupt

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - others: other errors.

<a id="_CPPv427bk_sdio_host_set_clock_freq22sdio_host_clock_freq_t"></a>

<a id="_CPPv327bk_sdio_host_set_clock_freq22sdio_host_clock_freq_t"></a> <a id="_CPPv227bk_sdio_host_set_clock_freq22sdio_host_clock_freq_t"></a> <a id="bk_sdio_host_set_clock_freq__sdio_host_clock_freq_t"></a> <a id="sdio__host_8h_1a783fc75ec68ce2fc59b4b0c5c6833df0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_set\_clock\_freq(sdio\_host\_clock\_freq\_t clock\_freq)
:   Set the sdio host clock frequency.

    参数
    :   **clock\_freq** – clock frequency

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - others: other errors.

<a id="_CPPv425bk_sdio_host_send_commandPK19sdio_host_cmd_cfg_t"></a>

<a id="_CPPv325bk_sdio_host_send_commandPK19sdio_host_cmd_cfg_t"></a> <a id="_CPPv225bk_sdio_host_send_commandPK19sdio_host_cmd_cfg_t"></a> <a id="bk_sdio_host_send_command__sdio_host_cmd_cfg_tCP"></a> <a id="sdio__host_8h_1ae930ad013e843d504d5772c4442efe6f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_send\_command(const sdio\_host\_cmd\_cfg\_t \*command)
:   Send the command from host to slave.

    参数
    :   **command** – the configuration information for the command

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_NULL\_PARAM: command is NULL
        - others: other errors.

<a id="_CPPv430bk_sdio_host_wait_cmd_response8uint32_t"></a>

<a id="_CPPv330bk_sdio_host_wait_cmd_response8uint32_t"></a> <a id="_CPPv230bk_sdio_host_wait_cmd_response8uint32_t"></a> <a id="bk_sdio_host_wait_cmd_response__uint32_t"></a> <a id="sdio__host_8h_1ac99d6c8fb9813a92bc3630d56e47999d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_wait\_cmd\_response(uint32\_t cmd\_index)
:   Host wait for salve command response.

    参数
    :   **cmd\_index** – the command index

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_SDIO\_HOST\_CMD\_RSP\_TIMEOUT: sdio host wait slave command over time
        - BK\_ERR\_SDIO\_HOST\_CMD\_RSP\_CRC\_FAIL: sdio host wait slave command crc fail
        - others: other errors.

<a id="_CPPv433bk_sdio_host_get_cmd_rsp_argument20sdio_host_response_t"></a>

<a id="_CPPv333bk_sdio_host_get_cmd_rsp_argument20sdio_host_response_t"></a> <a id="_CPPv233bk_sdio_host_get_cmd_rsp_argument20sdio_host_response_t"></a> <a id="bk_sdio_host_get_cmd_rsp_argument__sdio_host_response_t"></a> <a id="sdio__host_8h_1af6c9ec633f9a1fb9515ed66b3f19e1c8"></a> uint32\_t bk\_sdio\_host\_get\_cmd\_rsp\_argument(sdio\_host\_response\_t argument\_index)
:   Get the command response.

    参数
    :   **argument\_index** – the command argument index

    返回
    :   the response register value

<a id="_CPPv424bk_sdio_host_config_dataPK23sdio_host_data_config_t"></a>

<a id="_CPPv324bk_sdio_host_config_dataPK23sdio_host_data_config_t"></a> <a id="_CPPv224bk_sdio_host_config_dataPK23sdio_host_data_config_t"></a> <a id="bk_sdio_host_config_data__sdio_host_data_config_tCP"></a> <a id="sdio__host_8h_1a72b558e7d57b6a97589f2dda91d02557"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_config\_data(const sdio\_host\_data\_config\_t \*data\_config)
:   Config the data.

    参数
    :   **data\_config** – the configuration information for the data

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_NULL\_PARAM: data\_config is NULL
        - others: other errors.

<a id="_CPPv429bk_sdio_host_set_data_timeout8uint32_t"></a>

<a id="_CPPv329bk_sdio_host_set_data_timeout8uint32_t"></a> <a id="_CPPv229bk_sdio_host_set_data_timeout8uint32_t"></a> <a id="bk_sdio_host_set_data_timeout__uint32_t"></a> <a id="sdio__host_8h_1a18f2d99ec4428723573bed8a9143a1f9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_set\_data\_timeout(uint32\_t timeout)
:   Set the data timeout.

    参数
    :   **timeout** – the data timeout

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - others: other errors.

<a id="_CPPv423bk_sdio_host_write_fifoPK7uint8_t8uint32_t"></a>

<a id="_CPPv323bk_sdio_host_write_fifoPK7uint8_t8uint32_t"></a> <a id="_CPPv223bk_sdio_host_write_fifoPK7uint8_t8uint32_t"></a> <a id="bk_sdio_host_write_fifo__uint8_tCP.uint32_t"></a> <a id="sdio__host_8h_1a73cbae44634a8e5cfe03ef27a942f943"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_write\_fifo(const uint8\_t \*write\_data, uint32\_t data\_size)
:   Write data to tx fifo.

    参数
    :   - **write\_data** – pointer to data to write
        - **data\_size** – size of data to be sent, the data\_size value should be aligned with 512 bytes.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_NULL\_PARAM: write\_data is NULL
        - BK\_ERR\_SDIO\_HOST\_DATA\_TIMEOUT: sdio host wait slave data timeout
        - BK\_ERR\_SDIO\_HOST\_DATA\_CRC\_FAIL: sdio host receive slave data crc fail
        - others: other errors.

<a id="_CPPv430bk_sdio_host_wait_receive_datav"></a>

<a id="_CPPv330bk_sdio_host_wait_receive_datav"></a> <a id="_CPPv230bk_sdio_host_wait_receive_datav"></a> <a id="bk_sdio_host_wait_receive_data__void"></a> <a id="sdio__host_8h_1a128c83a4d621fe31ac777ee28a80db93"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_wait\_receive\_data(void)
:   Host wait slave data.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_NOT\_INIT: sdio host driver not init
        - BK\_ERR\_SDIO\_HOST\_DATA\_TIMEOUT: sdio host wait slave data timeout
        - BK\_ERR\_SDIO\_HOST\_DATA\_CRC\_FAIL: sdio host receive slave data crc fail
        - others: other errors.

<a id="_CPPv422bk_sdio_host_read_fifoP8uint32_t"></a>

<a id="_CPPv322bk_sdio_host_read_fifoP8uint32_t"></a> <a id="_CPPv222bk_sdio_host_read_fifoP8uint32_t"></a> <a id="bk_sdio_host_read_fifo__uint32_tP"></a> <a id="sdio__host_8h_1ad1f65353e489302e437e76b9b5f9444c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_read\_fifo(uint32\_t \*save\_v\_p)
:   Read data from rx fifo with timeout mode.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_READ\_DATA\_FAIL: sdio host read data from FIFO timeout
        - \*save\_v\_p:if success, will save read value to this pointer.

<a id="_CPPv427bk_sdio_host_read_blks_fifoP7uint8_t8uint32_t"></a>

<a id="_CPPv327bk_sdio_host_read_blks_fifoP7uint8_t8uint32_t"></a> <a id="_CPPv227bk_sdio_host_read_blks_fifoP7uint8_t8uint32_t"></a> <a id="bk_sdio_host_read_blks_fifo__uint8_tP.uint32_t"></a> <a id="sdio__host_8h_1af34d692157494fe1db80fff7d9161aca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sdio\_host\_read\_blks\_fifo(uint8\_t \*read\_data, uint32\_t blk\_cnt)
:   Read many blocks data from rx fifo with timeout mode.

    参数
    :   **blk\_cnt:read** – how many blocks data out from SDIO FIFO. the block\_size is 512 bytes.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SDIO\_HOST\_READ\_DATA\_FAIL: sdio host read data from FIFO timeout
        - \*read\_data:if success, will save read value to this pointer.
