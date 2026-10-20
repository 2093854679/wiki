---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_aec.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aec-apis"></a>

# AEC APIs

重要

The AEC API v1.0 is the lastest stable AEC APIs. All new applications should use AEC API v1.0.

<a id="aec-api-categories"></a>

## AEC API Categories

AEC APIs:
:   - [`aec_size()`](#_CPPv48aec_size8uint32_t "aec_size") \- get AECContext size (byte)
    - [`aec_init()`](#_CPPv48aec_initP10AECContext7int16_t "aec_init") \- init aec module
    - [`aec_ctrl()`](#_CPPv48aec_ctrlP10AECContext8uint32_t8uint32_t "aec_ctrl") \- get and set aec parameters
    - [`aec_proc()`](#_CPPv48aec_procP10AECContextP7int16_tP7int16_tP7int16_t "aec_proc") \- excute aec function

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [aec.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/modules/aec.h)

<a id="functions"></a>

### Functions

<a id="_CPPv48aec_size8uint32_t"></a>

<a id="_CPPv38aec_size8uint32_t"></a> <a id="_CPPv28aec_size8uint32_t"></a> <a id="aec_size__uint32_t"></a> <a id="group__AEC_1gace11cdf714a3fc0679f26f5ba64ef083"></a> uint32\_t aec\_size(uint32\_t delay)
:   Get AECContext size (byte)

    参数
    :   **delay** – delay samples

    返回
    :   - uint32\_t: size(byte)

<a id="_CPPv48aec_initP10AECContext7int16_t"></a>

<a id="_CPPv38aec_initP10AECContext7int16_t"></a> <a id="_CPPv28aec_initP10AECContext7int16_t"></a> <a id="aec_init__AECContextP.int16_t"></a> <a id="group__AEC_1ga76b46a1897c4f375bb403fb40b3ad80f"></a> void aec\_init([AECContext](#_CPPv410AECContext "AECContext") \*aec, int16\_t fs)
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

<a id="_CPPv48aec_ctrlP10AECContext8uint32_t8uint32_t"></a>

<a id="_CPPv38aec_ctrlP10AECContext8uint32_t8uint32_t"></a> <a id="_CPPv28aec_ctrlP10AECContext8uint32_t8uint32_t"></a> <a id="aec_ctrl__AECContextP.uint32_t.uint32_t"></a> <a id="group__AEC_1gae61fce33aa5e03533e7789a1e20b26c7"></a> void aec\_ctrl([AECContext](#_CPPv410AECContext "AECContext") \*aec, uint32\_t cmd, uint32\_t arg)
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
        - **cmd** – control command in enum AEC\_CTRL\_CMD
        - **arg** – value

    返回
    :   none

<a id="_CPPv48aec_procP10AECContextP7int16_tP7int16_tP7int16_t"></a>

<a id="_CPPv38aec_procP10AECContextP7int16_tP7int16_tP7int16_t"></a> <a id="_CPPv28aec_procP10AECContextP7int16_tP7int16_tP7int16_t"></a> <a id="aec_proc__AECContextP.int16_tP.int16_tP.int16_tP"></a> <a id="group__AEC_1ga14327d8f21d1e6d3ae3aca314311b49b"></a> void aec\_proc([AECContext](#_CPPv410AECContext "AECContext") \*aec, int16\_t \*rin, int16\_t \*sin, int16\_t \*out)
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

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410AECContext"></a>

<a id="_CPPv310AECContext"></a> <a id="_CPPv210AECContext"></a> <a id="AECContext"></a> <a id="aec_8h_1ac36fca448a2e1e1dfe3604f46a85b931"></a> typedef struct \_AECContext AECContext

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412AEC_CTRL_CMD"></a>

<a id="_CPPv312AEC_CTRL_CMD"></a> <a id="_CPPv212AEC_CTRL_CMD"></a> <a id="group__AEC_1ga10feb632630099348d5cef50c763314b"></a> enum AEC\_CTRL\_CMD
:   *Values:*

    <a id="_CPPv4N12AEC_CTRL_CMD17AEC_CTRL_CMD_NULLE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD17AEC_CTRL_CMD_NULLE"></a> <a id="_CPPv2N12AEC_CTRL_CMD17AEC_CTRL_CMD_NULLE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba714ccea67fbc470a92c03c0bd1e08e77"></a> enumerator AEC\_CTRL\_CMD\_NULL

    <a id="_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_GET_MIC_DELAYE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD26AEC_CTRL_CMD_GET_MIC_DELAYE"></a> <a id="_CPPv2N12AEC_CTRL_CMD26AEC_CTRL_CMD_GET_MIC_DELAYE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba11b130fd72d2e53780bac22402265f4f"></a> enumerator AEC\_CTRL\_CMD\_GET\_MIC\_DELAY
    :   Get mic delay

    <a id="_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_MIC_DELAYE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_MIC_DELAYE"></a> <a id="_CPPv2N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_MIC_DELAYE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314baabd7d70ceb294049590d1b74c6c4f927"></a> enumerator AEC\_CTRL\_CMD\_SET\_MIC\_DELAY
    :   Set mic delay

    <a id="_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_EC_DEPTHE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_EC_DEPTHE"></a> <a id="_CPPv2N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_EC_DEPTHE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba7264a979ff7d0ced986b6baff1b3a240"></a> enumerator AEC\_CTRL\_CMD\_GET\_EC\_DEPTH
    :   Get ec depth

    <a id="_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_EC_DEPTHE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_EC_DEPTHE"></a> <a id="_CPPv2N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_EC_DEPTHE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba21dc1f2c154022cd804d48d97b6a8d94"></a> enumerator AEC\_CTRL\_CMD\_SET\_EC\_DEPTH
    :   Set ec depth

    <a id="_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_NS_LEVELE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_NS_LEVELE"></a> <a id="_CPPv2N12AEC_CTRL_CMD25AEC_CTRL_CMD_GET_NS_LEVELE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba341ad442ef18f56c8429b15865ace126"></a> enumerator AEC\_CTRL\_CMD\_GET\_NS\_LEVEL
    :   Get ns level

    <a id="_CPPv4N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_NS_LEVELE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_NS_LEVELE"></a> <a id="_CPPv2N12AEC_CTRL_CMD25AEC_CTRL_CMD_SET_NS_LEVELE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bae67ad9f97bc36ace7729452abd483d61"></a> enumerator AEC\_CTRL\_CMD\_SET\_NS\_LEVEL
    :   Set ns level

    <a id="_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_GET_DRCE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD20AEC_CTRL_CMD_GET_DRCE"></a> <a id="_CPPv2N12AEC_CTRL_CMD20AEC_CTRL_CMD_GET_DRCE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba9abf9720581c0380dcb6ebacb5cbafd3"></a> enumerator AEC\_CTRL\_CMD\_GET\_DRC
    :   Get drc

    <a id="_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_DRCE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_DRCE"></a> <a id="_CPPv2N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_DRCE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba01144cbca41e5cdc2573f9f2f29a0fa7"></a> enumerator AEC\_CTRL\_CMD\_SET\_DRC
    :   Set drc

    <a id="_CPPv4N12AEC_CTRL_CMD22AEC_CTRL_CMD_GET_FLAGSE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD22AEC_CTRL_CMD_GET_FLAGSE"></a> <a id="_CPPv2N12AEC_CTRL_CMD22AEC_CTRL_CMD_GET_FLAGSE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bacb4a02dc70593a5db609cf67ee6712ea"></a> enumerator AEC\_CTRL\_CMD\_GET\_FLAGS
    :   Get flags

    <a id="_CPPv4N12AEC_CTRL_CMD22AEC_CTRL_CMD_SET_FLAGSE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD22AEC_CTRL_CMD_SET_FLAGSE"></a> <a id="_CPPv2N12AEC_CTRL_CMD22AEC_CTRL_CMD_SET_FLAGSE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba61d2aa1f75f828cace98f687a734c3e0"></a> enumerator AEC\_CTRL\_CMD\_SET\_FLAGS
    :   Set flags

    <a id="_CPPv4N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_VOLE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_VOLE"></a> <a id="_CPPv2N12AEC_CTRL_CMD20AEC_CTRL_CMD_SET_VOLE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba53839f331603687b9dafb76a348bae1a"></a> enumerator AEC\_CTRL\_CMD\_SET\_VOL
    :   Set volum

    <a id="_CPPv4N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_REF_SCALEE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_REF_SCALEE"></a> <a id="_CPPv2N12AEC_CTRL_CMD26AEC_CTRL_CMD_SET_REF_SCALEE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bad23df5699990b81bf5c79451d8194fa0"></a> enumerator AEC\_CTRL\_CMD\_SET\_REF\_SCALE
    :   Set reference scale

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxThrE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxThrE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxThrE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba77f60f7f300c6ccf786db9674c1540cf"></a> enumerator AEC\_CTRL\_CMD\_SET\_TxRxThr
    :   Set TxRxThr

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxFlrE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxFlrE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_TxRxFlrE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba544c47b493a9cbc95d7f70b977a228d4"></a> enumerator AEC\_CTRL\_CMD\_SET\_TxRxFlr
    :   Set TxRxFlr

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD1E"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD1E"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD1E"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bab5351f12386790bdb00229e7883134d3"></a> enumerator AEC\_CTRL\_CMD\_SET\_ECRSD1
    :   Set ECRSD1

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD2E"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD2E"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_ECRSD2E"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba3ee1406767d48566f280694525b04a64"></a> enumerator AEC\_CTRL\_CMD\_SET\_ECRSD2
    :   Set ECRSD2

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_RSDBANDE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_RSDBANDE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_RSDBANDE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bade289333e46cdfd118e96c2b4a1e7324"></a> enumerator AEC\_CTRL\_CMD\_SET\_RSDBAND
    :   Set RSDBAND

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_NS_PARAE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_NS_PARAE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_NS_PARAE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba5777ebb1a14d0e7ad3e5bd5d845e8b81"></a> enumerator AEC\_CTRL\_CMD\_SET\_NS\_PARA
    :   Set ns parameter

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_PARAMSE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_PARAMSE"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_PARAMSE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba21a2bde64860a62b330df819bd5e947a"></a> enumerator AEC\_CTRL\_CMD\_SET\_PARAMS
    :   Set parameters

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_EC_COEE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_EC_COEE"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_SET_EC_COEE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bae63a45ab3d69d22c1b161550efca36d7"></a> enumerator AEC\_CTRL\_CMD\_SET\_EC\_COE
    :   Set EC\_COE

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_DRC_TABE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_DRC_TABE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_SET_DRC_TABE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314bad3c73c664f27aeef02cc49994fbc841f"></a> enumerator AEC\_CTRL\_CMD\_SET\_DRC\_TAB
    :   Set DRC\_TAB

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_RX_BUFE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_RX_BUFE"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_RX_BUFE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba7f8d82832b3ad37dd0b3f4d33c469aba"></a> enumerator AEC\_CTRL\_CMD\_GET\_RX\_BUF
    :   Get rx buffer addr

    <a id="_CPPv4N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_TX_BUFE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_TX_BUFE"></a> <a id="_CPPv2N12AEC_CTRL_CMD23AEC_CTRL_CMD_GET_TX_BUFE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314baa505c0a5179f9581b6d8213de1cf98f6"></a> enumerator AEC\_CTRL\_CMD\_GET\_TX\_BUF
    :   Get tx buffer addr

    <a id="_CPPv4N12AEC_CTRL_CMD24AEC_CTRL_CMD_GET_OUT_BUFE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD24AEC_CTRL_CMD_GET_OUT_BUFE"></a> <a id="_CPPv2N12AEC_CTRL_CMD24AEC_CTRL_CMD_GET_OUT_BUFE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba15f6333eaf6e82d0c951b3f81a15971b"></a> enumerator AEC\_CTRL\_CMD\_GET\_OUT\_BUF
    :   Get output buffer addr

    <a id="_CPPv4N12AEC_CTRL_CMD29AEC_CTRL_CMD_GET_FRAME_SAMPLEE"></a>

    <a id="_CPPv3N12AEC_CTRL_CMD29AEC_CTRL_CMD_GET_FRAME_SAMPLEE"></a> <a id="_CPPv2N12AEC_CTRL_CMD29AEC_CTRL_CMD_GET_FRAME_SAMPLEE"></a> <a id="group__AEC_1gga10feb632630099348d5cef50c763314ba82e9bae63da01f01d39ae5c77d71d9c1"></a> enumerator AEC\_CTRL\_CMD\_GET\_FRAME\_SAMPLE
    :   Get frame sample

<a id="reference-link"></a>

## Reference link

> [API Reference :](bk_aec.md) Introduced the AEC API interface
>
> [User and Developer Guide :](../../audio_algorithms/aec.md) Introduced common usage scenarios of AEC
