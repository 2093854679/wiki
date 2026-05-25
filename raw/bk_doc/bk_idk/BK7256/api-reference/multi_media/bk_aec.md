# AEC APIs[](#aec-apis "永久链接至标题")


重要

The AEC API v1.0 is the lastest stable AEC APIs. All new applications should use AEC API v1.0.


## AEC API Categories[](#aec-api-categories "永久链接至标题")

AEC APIs:
:   - [`aec_size()`](#_CPPv48aec_size8uint32_t "aec_size") - get AECContext size (byte)

    - [`aec_init()`](#_CPPv48aec_initP10AECContext7int16_t "aec_init") - init aec module

    - [`aec_ctrl()`](#_CPPv48aec_ctrlP10AECContext8uint32_t8uint32_t "aec_ctrl") - get and set aec parameters

    - [`aec_proc()`](#_CPPv48aec_procP10AECContextP7int16_tP7int16_tP7int16_t "aec_proc") - excute aec function


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [aec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aec.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aec.h")


### Functions[](#functions "永久链接至标题")

uint32_t aec_size(uint32_t delay)[](#_CPPv48aec_size8uint32_t "永久链接至目标")
:   Get AECContext size (byte)

    参数
    :   **delay** – delay samples

    返回
    :   - uint32_t: size(byte)

void aec_init([AECContext](#_CPPv410AECContext "AECContext") *aec, int16_t fs)[](#_CPPv48aec_initP10AECContext7int16_t "永久链接至目标")
:   Init aec.

    This API init aec function :


    - Set aec parameters

    - Init fft parameters

    Usage example:

    ```
    AECContext* aec = NULL;

    //malloc aec memory
    aec = (AECContext*)os_malloc(aec_size());

    //init aec
    aec_init(aec, 16000);
    ```

    参数
    :   - **aec** – aec parameters

        - **fs** – frame sample 8K/16K

    返回
    :   none

void aec_ctrl([AECContext](#_CPPv410AECContext "AECContext") *aec, uint32_t cmd, uint32_t arg)[](#_CPPv48aec_ctrlP10AECContext8uint32_t8uint32_t "永久链接至目标")
:   Control aec.

    This API control aec function :


    - Set aec parameters

    - Get data addr

    Usage example:

    ```
    AECContext* aec = NULL;

    //malloc aec memory
    aec = (AECContext*)os_malloc(aec_size());

    //init aec
    aec_init(aec, 16000);

    //set mic delay
    aec_ctrl(aec, AEC_CTRL_CMD_SET_MIC_DELAY, 10);
    ```

    参数
    :   - **aec** – aec parameters

        - **cmd** – control command in enum AEC_CTRL_CMD

        - **arg** – value

    返回
    :   none

void aec_proc([AECContext](#_CPPv410AECContext "AECContext") *aec, int16_t *rin, int16_t *sin, int16_t *out)[](#_CPPv48aec_procP10AECContextP7int16_tP7int16_tP7int16_t "永久链接至目标")
:   Control aec.

    This API control aec function :


    - Set aec parameters

    - Get data addr

    Usage example:

    ```
    AECContext* aec = NULL;

    //malloc aec memory
    aec = (AECContext*)os_malloc(aec_size());

    //init aec
    aec_init(aec, 16000);

    //aec excute work
    aec_proc (aec, rin, sin, out);
    ```

    参数
    :   - **aec** – aec parameters

        - **rin** – reference data

        - **sin** – source data

        - **out** – output data

    返回
    :   none


### Type Definitions[](#type-definitions "永久链接至标题")

typedef struct _AECContext AECContext[](#_CPPv410AECContext "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum AEC_CTRL_CMD[](#_CPPv412AEC_CTRL_CMD "永久链接至目标")
:   *Values:*

    enumerator AEC_CTRL_CMD_NULL[](#_CPPv4N12AEC_CTRL_CMD17AEC_CTRL_CMD_NULLE "永久链接至目标")

    enumerator AEC_CTRL_CMD_GET_MIC_DELAY[](#_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_GET_MIC_DELAYE "永久链接至目标")
    :   Get mic delay

    enumerator AEC_CTRL_CMD_SET_MIC_DELAY[](#_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_MIC_DELAYE "永久链接至目标")
    :   Set mic delay

    enumerator AEC_CTRL_CMD_GET_EC_DEPTH[](#_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_EC_DEPTHE "永久链接至目标")
    :   Get ec depth

    enumerator AEC_CTRL_CMD_SET_EC_DEPTH[](#_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_EC_DEPTHE "永久链接至目标")
    :   Set ec depth

    enumerator AEC_CTRL_CMD_GET_NS_LEVEL[](#_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_NS_LEVELE "永久链接至目标")
    :   Get ns level

    enumerator AEC_CTRL_CMD_SET_NS_LEVEL[](#_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_NS_LEVELE "永久链接至目标")
    :   Set ns level

    enumerator AEC_CTRL_CMD_GET_DRC[](#_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_GET_DRCE "永久链接至目标")
    :   Get drc

    enumerator AEC_CTRL_CMD_SET_DRC[](#_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_DRCE "永久链接至目标")
    :   Set drc

    enumerator AEC_CTRL_CMD_GET_FLAGS[](#_CPPv4N12AEC_CTRL_CMD22AEC_CTRL_CMD_GET_FLAGSE "永久链接至目标")
    :   Get flags

    enumerator AEC_CTRL_CMD_SET_FLAGS[](#_CPPv4N12AEC_CTRL_CMD22AEC_CTRL_CMD_SET_FLAGSE "永久链接至目标")
    :   Set flags

    enumerator AEC_CTRL_CMD_SET_VOL[](#_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_VOLE "永久链接至目标")
    :   Set volum

    enumerator AEC_CTRL_CMD_SET_REF_SCALE[](#_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_REF_SCALEE "永久链接至目标")
    :   Set reference scale

    enumerator AEC_CTRL_CMD_SET_TxRxThr[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxThrE "永久链接至目标")
    :   Set TxRxThr

    enumerator AEC_CTRL_CMD_SET_TxRxFlr[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxFlrE "永久链接至目标")
    :   Set TxRxFlr

    enumerator AEC_CTRL_CMD_SET_ECRSD1[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD1E "永久链接至目标")
    :   Set ECRSD1

    enumerator AEC_CTRL_CMD_SET_ECRSD2[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD2E "永久链接至目标")
    :   Set ECRSD2

    enumerator AEC_CTRL_CMD_SET_RSDBAND[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_RSDBANDE "永久链接至目标")
    :   Set RSDBAND

    enumerator AEC_CTRL_CMD_SET_NS_PARA[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_NS_PARAE "永久链接至目标")
    :   Set ns parameter

    enumerator AEC_CTRL_CMD_SET_PARAMS[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_PARAMSE "永久链接至目标")
    :   Set parameters

    enumerator AEC_CTRL_CMD_SET_EC_COE[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_EC_COEE "永久链接至目标")
    :   Set EC_COE

    enumerator AEC_CTRL_CMD_SET_DRC_TAB[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_DRC_TABE "永久链接至目标")
    :   Set DRC_TAB

    enumerator AEC_CTRL_CMD_GET_RX_BUF[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_RX_BUFE "永久链接至目标")
    :   Get rx buffer addr

    enumerator AEC_CTRL_CMD_GET_TX_BUF[](#_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_TX_BUFE "永久链接至目标")
    :   Get tx buffer addr

    enumerator AEC_CTRL_CMD_GET_OUT_BUF[](#_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_GET_OUT_BUFE "永久链接至目标")
    :   Get output buffer addr

    enumerator AEC_CTRL_CMD_GET_FRAME_SAMPLE[](#_CPPv4N12AEC_CTRL_CMD29AEC_CTRL_CMD_GET_FRAME_SAMPLEE "永久链接至目标")
    :   Get frame sample
