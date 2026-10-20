---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_sbc.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sbc-apis"></a>

# SBC APIs

重要

The SBC Driver is just only APIs for SBC decoding function. And the SBC API v1.0 is the lastest and stable SBC decoder APIs. All new applications should use SBC API v1.0.

<a id="sbc-user-guide"></a>

## SBC User Guide

The sbc and msbc are used as follow:

<a id="id2"></a>
![SBC User Guide Flow](../../../../_assets/18ecee6e99f93a2cca4c-sbc_user_guide_flow.png)


SBC User Guide Flow

<a id="sbc-interface"></a>

## SBC Interface

The BK SBC Driver supports following functions:

> - sbc function
> - msbc function

The SBC Driver support msbc decoder function. If the application need to use msbc decoder function, Just use the bk\_sbc\_decoder\_support msbc() to enable msbc function.

<a id="sbc-api-categories"></a>

## SBC API Categories

Most of SBC APIs can be categoried as:

> - Common or sbc APIs
>
>   The common APIs are prefixed with bk\_sbc, the APIs may be common for sbc and msbc interfaces, e.g. bk\_sbc\_decoder\_init() etc.
> - MSBC function APIs.
>
>   The APIs provide support for msbc function. e.g. bk\_sbc\_decoder\_support msbc().

Common APIs:
:   - [`bk_sbc_decoder_init()`](#_CPPv419bk_sbc_decoder_initP19sbcdecodercontext_t "bk_sbc_decoder_init") \- init the sbc module
    - [`bk_sbc_decoder_deinit()`](#_CPPv421bk_sbc_decoder_deinitv "bk_sbc_decoder_deinit") \- deinit the sbc module
    - [`bk_sbc_decoder_bit_allocation()`](#_CPPv429bk_sbc_decoder_bit_allocationP18sbccommoncontext_t "bk_sbc_decoder_bit_allocation") \- calculate the bit allocation
    - [`bk_sbc_decoder_frame_decode()`](#_CPPv427bk_sbc_decoder_frame_decodeP19sbcdecodercontext_tPK7uint8_t8uint32_t "bk_sbc_decoder_frame_decode") \- decode one sbc frame
    - [`bk_sbc_decoder_interrupt_enable()`](#_CPPv431bk_sbc_decoder_interrupt_enableb "bk_sbc_decoder_interrupt_enable") \- enable or disable the sbc interrupt
    - [`bk_sbc_decoder_support_msbc()`](#_CPPv427bk_sbc_decoder_support_msbcb "bk_sbc_decoder_support_msbc") \- enable or disable msbc decoder function
    - [`bk_sbc_decoder_register_sbc_isr()`](#_CPPv431bk_sbc_decoder_register_sbc_isr17sbc_decoder_isr_tPv "bk_sbc_decoder_register_sbc_isr") \- register sbc isr

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [sbc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/sbc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv427bk_sbc_decoder_frame_decodeP19sbcdecodercontext_tPK7uint8_t8uint32_t"></a>

<a id="_CPPv327bk_sbc_decoder_frame_decodeP19sbcdecodercontext_tPK7uint8_t8uint32_t"></a> <a id="_CPPv227bk_sbc_decoder_frame_decodeP19sbcdecodercontext_tPK7uint8_t8uint32_t"></a> <a id="bk_sbc_decoder_frame_decode__sbcdecodercontext_tP.uint8_tCP.uint32_t"></a> <a id="group__sbc_1ga6c459bc6c6793c756e2393e85f375c6d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_frame\_decode([sbcdecodercontext\_t](#_CPPv419sbcdecodercontext_t "sbcdecodercontext_t") \*sbc, const uint8\_t \*data, uint32\_t length)
:   SBC decoder decode one frame.

    This API decode one frame by sbc decoder.

    Usage example:

    [sbcdecodercontext\_t](#structsbcdecodercontext__t) sbc\_decoder; bk\_sbc\_decoder\_frame\_decode(\&sbc\_decoder, sbc\_data, 512);

    **Attention**
    :   1\. the output PCM data please refer to the follows variables:

        - sbc-\>pcm\_sample: means output PCM data address
        - sbc-\>pcm\_length: means output PCM data length in sample
        - sbc-\>channel\_number: means output PCM data channels

    参数
    :   **sbc, :** – sbc decoder context pointer;

        - data: buffer to be decoded;
        - length: the length of input buffer;

    返回
    :   - consumed: buffer length by decoder if no error ocurs, else error code (always small than 0\) will be return.

<a id="_CPPv429bk_sbc_decoder_bit_allocationP18sbccommoncontext_t"></a>

<a id="_CPPv329bk_sbc_decoder_bit_allocationP18sbccommoncontext_t"></a> <a id="_CPPv229bk_sbc_decoder_bit_allocationP18sbccommoncontext_t"></a> <a id="bk_sbc_decoder_bit_allocation__sbccommoncontext_tP"></a> <a id="group__sbc_1ga3a2a3d649f0db91b256a78c5b7f2384e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_bit\_allocation([sbccommoncontext\_t](#_CPPv418sbccommoncontext_t "sbccommoncontext_t") \*sbc)
:   SBC bit allocation calculate for both encoder and decoder.

    This API calculate sbc bit allocation.

    参数
    :   **sbc, :** – sbc decoder context pointer

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_sbc_decoder_initP19sbcdecodercontext_t"></a>

<a id="_CPPv319bk_sbc_decoder_initP19sbcdecodercontext_t"></a> <a id="_CPPv219bk_sbc_decoder_initP19sbcdecodercontext_t"></a> <a id="bk_sbc_decoder_init__sbcdecodercontext_tP"></a> <a id="group__sbc_1gabb4f8393396ae0f110d76c79019ff000"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_init([sbcdecodercontext\_t](#_CPPv419sbcdecodercontext_t "sbcdecodercontext_t") \*sbc)
:   SBC decoder initialize.

    This API init the sbc decoder function.

    参数
    :   **sbc, :** – sbc decoder context pointer

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_sbc_decoder_deinitv"></a>

<a id="_CPPv321bk_sbc_decoder_deinitv"></a> <a id="_CPPv221bk_sbc_decoder_deinitv"></a> <a id="bk_sbc_decoder_deinit__void"></a> <a id="group__sbc_1ga856ea222f4385d0aeb225682a9b73457"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_deinit(void)
:   SBC decoder deinit.

    This API deinit the sbc decoder function.

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_sbc_decoder_interrupt_enableb"></a>

<a id="_CPPv331bk_sbc_decoder_interrupt_enableb"></a> <a id="_CPPv231bk_sbc_decoder_interrupt_enableb"></a> <a id="bk_sbc_decoder_interrupt_enable__b"></a> <a id="group__sbc_1ga36ea51af5914910032d7db7db976dc74"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_interrupt\_enable(bool enable)
:   enable/disable sbc interrupt

    This API enable or disable sbc interrupt:

    - reigster interrupt service handle
    - enable or disable sbc interrupt

    参数
    :   **enable, :** – enable —— 1, disable —— 0

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_sbc_decoder_support_msbcb"></a>

<a id="_CPPv327bk_sbc_decoder_support_msbcb"></a> <a id="_CPPv227bk_sbc_decoder_support_msbcb"></a> <a id="bk_sbc_decoder_support_msbc__b"></a> <a id="group__sbc_1gad7619a3a1ec08b170b1b4d00d19b923a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_support\_msbc(bool enable)
:   enable/disable msbc decoder

    This API enable/disable msbc decoder.

    参数
    :   **enable, :** – enable —— 1, disable —— 0

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_sbc_decoder_register_sbc_isr17sbc_decoder_isr_tPv"></a>

<a id="_CPPv331bk_sbc_decoder_register_sbc_isr17sbc_decoder_isr_tPv"></a> <a id="_CPPv231bk_sbc_decoder_register_sbc_isr17sbc_decoder_isr_tPv"></a> <a id="bk_sbc_decoder_register_sbc_isr__sbc_decoder_isr_t.voidP"></a> <a id="group__sbc_1gaa00264c0acbbc0caeca7ec95a3b5568b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_sbc\_decoder\_register\_sbc\_isr([sbc\_decoder\_isr\_t](#_CPPv417sbc_decoder_isr_t "sbc_decoder_isr_t") isr, void \*param)
:   Register sbc decoder isr.

    This API register sbc decoder isr.

    参数
    :   **isr, :** – sbc decoder isr callback;

        - param: sbc decoder isr callback parameter;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [sbc\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/sbc_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv418sbccommoncontext_t"></a>

<a id="_CPPv318sbccommoncontext_t"></a> <a id="_CPPv218sbccommoncontext_t"></a> <a id="sbccommoncontext_t"></a> <a id="structsbccommoncontext__t"></a> struct sbccommoncontext\_t
:   SBC decoder context.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18sbccommoncontext_t6blocksE"></a>

    <a id="_CPPv3N18sbccommoncontext_t6blocksE"></a> <a id="_CPPv2N18sbccommoncontext_t6blocksE"></a> <a id="sbccommoncontext_t::blocks__int8_t"></a> <a id="structsbccommoncontext__t_1a10a2053b7a53d6798afcec5b7da866a6"></a> int8\_t blocks
    :   block number

    <a id="_CPPv4N18sbccommoncontext_t8subbandsE"></a>

    <a id="_CPPv3N18sbccommoncontext_t8subbandsE"></a> <a id="_CPPv2N18sbccommoncontext_t8subbandsE"></a> <a id="sbccommoncontext_t::subbands__int8_t"></a> <a id="structsbccommoncontext__t_1ad1b7624758e2c04d16fa9df0e8ee3716"></a> int8\_t subbands
    :   subbands number

    <a id="_CPPv4N18sbccommoncontext_t4joinE"></a>

    <a id="_CPPv3N18sbccommoncontext_t4joinE"></a> <a id="_CPPv2N18sbccommoncontext_t4joinE"></a> <a id="sbccommoncontext_t::join__uint8_t"></a> <a id="structsbccommoncontext__t_1a95a2a339ea407e9789847e25ab936d87"></a> uint8\_t join
    :   bit number x set means joint stereo has been used in subband x

    <a id="_CPPv4N18sbccommoncontext_t7bitpoolE"></a>

    <a id="_CPPv3N18sbccommoncontext_t7bitpoolE"></a> <a id="_CPPv2N18sbccommoncontext_t7bitpoolE"></a> <a id="sbccommoncontext_t::bitpool__uint8_t"></a> <a id="structsbccommoncontext__t_1a0dfd52599d2486af0e228800b96619a6"></a> uint8\_t bitpool
    :   indicate the size of the bit allocation pool that has been used for encoding the stream

    <a id="_CPPv4N18sbccommoncontext_t12channel_modeE"></a>

    <a id="_CPPv3N18sbccommoncontext_t12channel_modeE"></a> <a id="_CPPv2N18sbccommoncontext_t12channel_modeE"></a> <a id="sbccommoncontext_t::channel_mode__int8_t"></a> <a id="structsbccommoncontext__t_1a8ecf59c223845acb8e23c761afa7df51"></a> int8\_t channel\_mode
    :   channel mode

    <a id="_CPPv4N18sbccommoncontext_t17sample_rate_indexE"></a>

    <a id="_CPPv3N18sbccommoncontext_t17sample_rate_indexE"></a> <a id="_CPPv2N18sbccommoncontext_t17sample_rate_indexE"></a> <a id="sbccommoncontext_t::sample_rate_index__int8_t"></a> <a id="structsbccommoncontext__t_1afe8c45d2fbdc0cbc55a06ab7f1828fce"></a> int8\_t sample\_rate\_index
    :   sample rate index, 0:16000, 1:32000, 2:44100, 3:48000

    <a id="_CPPv4N18sbccommoncontext_t17allocation_methodE"></a>

    <a id="_CPPv3N18sbccommoncontext_t17allocation_methodE"></a> <a id="_CPPv2N18sbccommoncontext_t17allocation_methodE"></a> <a id="sbccommoncontext_t::allocation_method__int8_t"></a> <a id="structsbccommoncontext__t_1ace73708acb48693bb721668d462ecbab"></a> int8\_t allocation\_method
    :   allocation method

    <a id="_CPPv4N18sbccommoncontext_t9reserved8E"></a>

    <a id="_CPPv3N18sbccommoncontext_t9reserved8E"></a> <a id="_CPPv2N18sbccommoncontext_t9reserved8E"></a> <a id="sbccommoncontext_t::reserved8__int8_t"></a> <a id="structsbccommoncontext__t_1ac66a04a415478ca01f796d1b01b97c13"></a> int8\_t reserved8
    :   dummy, reserved for byte align

    <a id="_CPPv4N18sbccommoncontext_t4bitsE"></a>

    <a id="_CPPv3N18sbccommoncontext_t4bitsE"></a> <a id="_CPPv2N18sbccommoncontext_t4bitsE"></a> <a id="sbccommoncontext_t::bits__int8_tAA"></a> <a id="structsbccommoncontext__t_1a179a74e755c4d98abca683d2066688a6"></a> int8\_t bits\[2\]\[8\]
    :   calculate result by bit allocation

    <a id="_CPPv4N18sbccommoncontext_t12scale_factorE"></a>

    <a id="_CPPv3N18sbccommoncontext_t12scale_factorE"></a> <a id="_CPPv2N18sbccommoncontext_t12scale_factorE"></a> <a id="sbccommoncontext_t::scale_factor__int8_tAA"></a> <a id="structsbccommoncontext__t_1aa460fec3b80a1c29770d56057ec67d01"></a> int8\_t scale\_factor\[2\]\[8\]
    :   only the lower 4 bits of every element are to be used

    <a id="_CPPv4N18sbccommoncontext_t3memE"></a>

    <a id="_CPPv3N18sbccommoncontext_t3memE"></a> <a id="_CPPv2N18sbccommoncontext_t3memE"></a> <a id="sbccommoncontext_t::mem__int32_tAA"></a> <a id="structsbccommoncontext__t_1ae7d54ac695066c2c548721b69b6230b0"></a> int32\_t mem\[2\]\[8\]
    :   Memory used as bit need and levels

<a id="_CPPv419sbcdecodercontext_t"></a>

<a id="_CPPv319sbcdecodercontext_t"></a> <a id="_CPPv219sbcdecodercontext_t"></a> <a id="sbcdecodercontext_t"></a> <a id="structsbcdecodercontext__t"></a> struct sbcdecodercontext\_t
:   SBC decoder context.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19sbcdecodercontext_t14channel_numberE"></a>

    <a id="_CPPv3N19sbcdecodercontext_t14channel_numberE"></a> <a id="_CPPv2N19sbcdecodercontext_t14channel_numberE"></a> <a id="sbcdecodercontext_t::channel_number__int8_t"></a> <a id="structsbcdecodercontext__t_1a7ec300df2497fdacc19e3e5afdce10bf"></a> int8\_t channel\_number
    :   channels number

    <a id="_CPPv4N19sbcdecodercontext_t10pcm_lengthE"></a>

    <a id="_CPPv3N19sbcdecodercontext_t10pcm_lengthE"></a> <a id="_CPPv2N19sbcdecodercontext_t10pcm_lengthE"></a> <a id="sbcdecodercontext_t::pcm_length__uint8_t"></a> <a id="structsbcdecodercontext__t_1ad640cf9c9888fdc7c0c26cc6b2c1fa4d"></a> uint8\_t pcm\_length
    :   PCM length

    <a id="_CPPv4N19sbcdecodercontext_t11sample_rateE"></a>

    <a id="_CPPv3N19sbcdecodercontext_t11sample_rateE"></a> <a id="_CPPv2N19sbcdecodercontext_t11sample_rateE"></a> <a id="sbcdecodercontext_t::sample_rate__uint16_t"></a> <a id="structsbcdecodercontext__t_1a68763767b37917698c89a14e4e8c0354"></a> uint16\_t sample\_rate
    :   sample rate

    <a id="_CPPv4N19sbcdecodercontext_t10pcm_sampleE"></a>

    <a id="_CPPv3N19sbcdecodercontext_t10pcm_sampleE"></a> <a id="_CPPv2N19sbcdecodercontext_t10pcm_sampleE"></a> <a id="sbcdecodercontext_t::pcm_sample__int32_tAA"></a> <a id="structsbcdecodercontext__t_1aaf42d27edd8fcfa6fea5712f2bbb3205"></a> int32\_t pcm\_sample\[2\]\[128\]
    :   PCM frame buffer

    <a id="_CPPv4N19sbcdecodercontext_t5vfifoE"></a>

    <a id="_CPPv3N19sbcdecodercontext_t5vfifoE"></a> <a id="_CPPv2N19sbcdecodercontext_t5vfifoE"></a> <a id="sbcdecodercontext_t::vfifo__int32_tAA"></a> <a id="structsbcdecodercontext__t_1a986fcb153eae82b64fb84d1395e09941"></a> int32\_t vfifo\[2\]\[170\]
    :   FIFO V for subbands synthesis calculation.

<a id="_CPPv412sbc_config_t"></a>

<a id="_CPPv312sbc_config_t"></a> <a id="_CPPv212sbc_config_t"></a> <a id="sbc_config_t"></a> <a id="structsbc__config__t"></a> struct sbc\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12sbc_config_t11channel_numE"></a>

    <a id="_CPPv3N12sbc_config_t11channel_numE"></a> <a id="_CPPv2N12sbc_config_t11channel_numE"></a> <a id="sbc_config_t::channel_num__sbc_channel_num_t"></a> <a id="structsbc__config__t_1a79e6117aadddb2d6280981f7cb6a2c0d"></a> [sbc\_channel\_num\_t](#_CPPv417sbc_channel_num_t "sbc_channel_num_t") channel\_num
    :   channels number

    <a id="_CPPv4N12sbc_config_t8subbandsE"></a>

    <a id="_CPPv3N12sbc_config_t8subbandsE"></a> <a id="_CPPv2N12sbc_config_t8subbandsE"></a> <a id="sbc_config_t::subbands__sbc_subband_number_t"></a> <a id="structsbc__config__t_1aee4611ba567b37a79236268fae9c3ead"></a> [sbc\_subband\_number\_t](#_CPPv420sbc_subband_number_t "sbc_subband_number_t") subbands
    :   subband number

    <a id="_CPPv4N12sbc_config_t8chn_combE"></a>

    <a id="_CPPv3N12sbc_config_t8chn_combE"></a> <a id="_CPPv2N12sbc_config_t8chn_combE"></a> <a id="sbc_config_t::chn_comb__sbc_chn_comb_t"></a> <a id="structsbc__config__t_1ada94154132a649ca107eed59b424070a"></a> [sbc\_chn\_comb\_t](#_CPPv414sbc_chn_comb_t "sbc_chn_comb_t") chn\_comb
    :   pcm output struct

    <a id="_CPPv4N12sbc_config_t6blocksE"></a>

    <a id="_CPPv3N12sbc_config_t6blocksE"></a> <a id="_CPPv2N12sbc_config_t6blocksE"></a> <a id="sbc_config_t::blocks__sbc_blocks_number_t"></a> <a id="structsbc__config__t_1aae35fdb93dd3620dadf7b70662a45f13"></a> [sbc\_blocks\_number\_t](#_CPPv419sbc_blocks_number_t "sbc_blocks_number_t") blocks
    :   block number

<a id="macros"></a>

### Macros

<a id="c.SBC_SYNCWORD"></a>

<a id="sbc__types_8h_1a71241adb94f8cf69aa29126e1534dd74"></a> SBC\_SYNCWORD
:   SBC synchronize word

<a id="c.MSBC_SYNCWORD"></a>

<a id="sbc__types_8h_1a80df9496f9ef5f29db79f3d7e866ad99"></a> MSBC\_SYNCWORD
:   MSBC synchronize word

<a id="c.SBC_CHANNEL_MODE_MONO"></a>

<a id="sbc__types_8h_1ae74a629210dc448f3a76a6f83713fae6"></a> SBC\_CHANNEL\_MODE\_MONO
:   SBC channel mode : MONO

<a id="c.SBC_CHANNEL_MODE_DUAL"></a>

<a id="sbc__types_8h_1ad8f733fb90981a1bfc142f00d8fe1609"></a> SBC\_CHANNEL\_MODE\_DUAL
:   SBC channel mode : Dual Channels

<a id="c.SBC_CHANNEL_MODE_STEREO"></a>

<a id="sbc__types_8h_1a78ecb92f5c80838b6b5a24a0e802b2d5"></a> SBC\_CHANNEL\_MODE\_STEREO
:   SBC channel mode : Stereo

<a id="c.SBC_CHANNEL_MODE_JOINT_STEREO"></a>

<a id="sbc__types_8h_1a2d8ffa756ad75decf5ef9fd38ffb8644"></a> SBC\_CHANNEL\_MODE\_JOINT\_STEREO
:   SBC channel mode : Joint Stereo

<a id="c.SBC_DECODER_ERRORS"></a>

<a id="sbc__types_8h_1ac0097332d4e448a73736654088993354"></a> SBC\_DECODER\_ERRORS

<a id="c.SBC_DECODER_ERROR_BUFFER_OVERFLOW"></a>

<a id="sbc__types_8h_1a989760b6fb9ebab8da6c5ada945494d0"></a> SBC\_DECODER\_ERROR\_BUFFER\_OVERFLOW
:   buffer overflow

<a id="c.SBC_DECODER_ERROR_SYNC_INCORRECT"></a>

<a id="sbc__types_8h_1a823457a5e4833366c750075684efde8a"></a> SBC\_DECODER\_ERROR\_SYNC\_INCORRECT
:   synchronize incorrect

<a id="c.SBC_DECODER_ERROR_BITPOOL_OUT_BOUNDS"></a>

<a id="sbc__types_8h_1a39b4f615d625c49cb0072ae11e730536"></a> SBC\_DECODER\_ERROR\_BITPOOL\_OUT\_BOUNDS
:   bitpool out of bounds

<a id="c.SBC_DECODER_ERROR_STREAM_EMPTY"></a>

<a id="sbc__types_8h_1a660c1bfa293f5fcf503d287fd4e76352"></a> SBC\_DECODER\_ERROR\_STREAM\_EMPTY
:   stream empty

<a id="c.SBC_DECODER_ERROR_OK"></a>

<a id="sbc__types_8h_1ad8a9cde1c013ac37cf30854a07852a41"></a> SBC\_DECODER\_ERROR\_OK
:   no error

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417sbc_decoder_isr_t"></a>

<a id="_CPPv317sbc_decoder_isr_t"></a> <a id="_CPPv217sbc_decoder_isr_t"></a> <a id="sbc_decoder_isr_t"></a> <a id="sbc__types_8h_1a1ac444eb518322e3335b05f400bf872f"></a> typedef void (\*sbc\_decoder\_isr\_t)(void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv418sbc_sample_rates_t"></a>

<a id="_CPPv318sbc_sample_rates_t"></a> <a id="_CPPv218sbc_sample_rates_t"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995d"></a> enum sbc\_sample\_rates\_t
:   *Values:*

    <a id="_CPPv4N18sbc_sample_rates_t21SBC_SAMPLE_RATE_16000E"></a>

    <a id="_CPPv3N18sbc_sample_rates_t21SBC_SAMPLE_RATE_16000E"></a> <a id="_CPPv2N18sbc_sample_rates_t21SBC_SAMPLE_RATE_16000E"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995da66bda4bbe6b2cec572211979e0bfce77"></a> enumerator SBC\_SAMPLE\_RATE\_16000
    :   SBC sampling frequency : 16.0KHz

    <a id="_CPPv4N18sbc_sample_rates_t21SBC_SAMPLE_RATE_32000E"></a>

    <a id="_CPPv3N18sbc_sample_rates_t21SBC_SAMPLE_RATE_32000E"></a> <a id="_CPPv2N18sbc_sample_rates_t21SBC_SAMPLE_RATE_32000E"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995da49ac04f5a8348f4d16b02b90b5684d27"></a> enumerator SBC\_SAMPLE\_RATE\_32000
    :   SBC sampling frequency : 32.0KHz

    <a id="_CPPv4N18sbc_sample_rates_t21SBC_SAMPLE_RATE_44100E"></a>

    <a id="_CPPv3N18sbc_sample_rates_t21SBC_SAMPLE_RATE_44100E"></a> <a id="_CPPv2N18sbc_sample_rates_t21SBC_SAMPLE_RATE_44100E"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995da3438b8dd634a22de354bc2f70a29db03"></a> enumerator SBC\_SAMPLE\_RATE\_44100
    :   SBC sampling frequency : 44.1KHz

    <a id="_CPPv4N18sbc_sample_rates_t21SBC_SAMPLE_RATE_48000E"></a>

    <a id="_CPPv3N18sbc_sample_rates_t21SBC_SAMPLE_RATE_48000E"></a> <a id="_CPPv2N18sbc_sample_rates_t21SBC_SAMPLE_RATE_48000E"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995da27b97edc46700a72a55275e7e99e9458"></a> enumerator SBC\_SAMPLE\_RATE\_48000
    :   SBC sampling frequency : 48.0KHz

    <a id="_CPPv4N18sbc_sample_rates_t19SBC_SAMPLE_RATE_MAXE"></a>

    <a id="_CPPv3N18sbc_sample_rates_t19SBC_SAMPLE_RATE_MAXE"></a> <a id="_CPPv2N18sbc_sample_rates_t19SBC_SAMPLE_RATE_MAXE"></a> <a id="sbc__types_8h_1a6537935830e39685686f17a98316995da4a08275991319a89b35f28c87a1f80be"></a> enumerator SBC\_SAMPLE\_RATE\_MAX

<a id="_CPPv417sbc_channel_num_t"></a>

<a id="_CPPv317sbc_channel_num_t"></a> <a id="_CPPv217sbc_channel_num_t"></a> <a id="sbc__types_8h_1ab69fb999be107b4c66d280b9c3b273f3"></a> enum sbc\_channel\_num\_t
:   *Values:*

    <a id="_CPPv4N17sbc_channel_num_t19SBC_CHANNEL_NUM_ONEE"></a>

    <a id="_CPPv3N17sbc_channel_num_t19SBC_CHANNEL_NUM_ONEE"></a> <a id="_CPPv2N17sbc_channel_num_t19SBC_CHANNEL_NUM_ONEE"></a> <a id="sbc__types_8h_1ab69fb999be107b4c66d280b9c3b273f3a4bc7eeec53851f14248142b82b7620e3"></a> enumerator SBC\_CHANNEL\_NUM\_ONE
    :   SBC channel number : 1 channel

    <a id="_CPPv4N17sbc_channel_num_t19SBC_CHANNEL_NUM_TWOE"></a>

    <a id="_CPPv3N17sbc_channel_num_t19SBC_CHANNEL_NUM_TWOE"></a> <a id="_CPPv2N17sbc_channel_num_t19SBC_CHANNEL_NUM_TWOE"></a> <a id="sbc__types_8h_1ab69fb999be107b4c66d280b9c3b273f3aae00ab0f58d2042c8a8150f2e7100398"></a> enumerator SBC\_CHANNEL\_NUM\_TWO
    :   SBC channel number : 2 channels

    <a id="_CPPv4N17sbc_channel_num_t24SBC_CHANNEL_MODE_INVALIDE"></a>

    <a id="_CPPv3N17sbc_channel_num_t24SBC_CHANNEL_MODE_INVALIDE"></a> <a id="_CPPv2N17sbc_channel_num_t24SBC_CHANNEL_MODE_INVALIDE"></a> <a id="sbc__types_8h_1ab69fb999be107b4c66d280b9c3b273f3a4a92f145cd7b45b8f3bc119abaaec95f"></a> enumerator SBC\_CHANNEL\_MODE\_INVALID

<a id="_CPPv420sbc_subband_number_t"></a>

<a id="_CPPv320sbc_subband_number_t"></a> <a id="_CPPv220sbc_subband_number_t"></a> <a id="sbc__types_8h_1a6c636b3574a6e042d170c5be4f2871de"></a> enum sbc\_subband\_number\_t
:   *Values:*

    <a id="_CPPv4N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_4E"></a>

    <a id="_CPPv3N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_4E"></a> <a id="_CPPv2N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_4E"></a> <a id="sbc__types_8h_1a6c636b3574a6e042d170c5be4f2871dea0d447ff4ccc6f5ed83289d4d8bfcde51"></a> enumerator SBC\_SUBBAND\_NUMBER\_4
    :   SBC subbands number 4

    <a id="_CPPv4N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_8E"></a>

    <a id="_CPPv3N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_8E"></a> <a id="_CPPv2N20sbc_subband_number_t20SBC_SUBBAND_NUMBER_8E"></a> <a id="sbc__types_8h_1a6c636b3574a6e042d170c5be4f2871dea92069b842c14c8429d3f7f9e29b3837d"></a> enumerator SBC\_SUBBAND\_NUMBER\_8
    :   SBC subbands number 8

    <a id="_CPPv4N20sbc_subband_number_t15SBC_SUBBAND_MAXE"></a>

    <a id="_CPPv3N20sbc_subband_number_t15SBC_SUBBAND_MAXE"></a> <a id="_CPPv2N20sbc_subband_number_t15SBC_SUBBAND_MAXE"></a> <a id="sbc__types_8h_1a6c636b3574a6e042d170c5be4f2871dead83df0e56464fede35563eb162c2fa09"></a> enumerator SBC\_SUBBAND\_MAX

<a id="_CPPv414sbc_chn_comb_t"></a>

<a id="_CPPv314sbc_chn_comb_t"></a> <a id="_CPPv214sbc_chn_comb_t"></a> <a id="sbc__types_8h_1aec4193650c27eb99c943bcbb67ece258"></a> enum sbc\_chn\_comb\_t
:   *Values:*

    <a id="_CPPv4N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_SINGLEE"></a>

    <a id="_CPPv3N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_SINGLEE"></a> <a id="_CPPv2N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_SINGLEE"></a> <a id="sbc__types_8h_1aec4193650c27eb99c943bcbb67ece258a5936290bbe59d2a25f78877c4fd38fb8"></a> enumerator SBC\_DECODE\_OUTPUT\_SINGLE
    :   SBC decoder output struct:{16’d0, pcm}

    <a id="_CPPv4N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_DOUBLEE"></a>

    <a id="_CPPv3N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_DOUBLEE"></a> <a id="_CPPv2N14sbc_chn_comb_t24SBC_DECODE_OUTPUT_DOUBLEE"></a> <a id="sbc__types_8h_1aec4193650c27eb99c943bcbb67ece258adc295fdc09c6d4348a789e6a3ab9a02c"></a> enumerator SBC\_DECODE\_OUTPUT\_DOUBLE
    :   SBC decoder output struct:{pcm\_chn2, pcm\_chn1}

    <a id="_CPPv4N14sbc_chn_comb_t25SBC_DECODE_OUTPUT_INVALIDE"></a>

    <a id="_CPPv3N14sbc_chn_comb_t25SBC_DECODE_OUTPUT_INVALIDE"></a> <a id="_CPPv2N14sbc_chn_comb_t25SBC_DECODE_OUTPUT_INVALIDE"></a> <a id="sbc__types_8h_1aec4193650c27eb99c943bcbb67ece258aa437fb8a11a1e098e9439a70d833fed1"></a> enumerator SBC\_DECODE\_OUTPUT\_INVALID

<a id="_CPPv419sbc_blocks_number_t"></a>

<a id="_CPPv319sbc_blocks_number_t"></a> <a id="_CPPv219sbc_blocks_number_t"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1"></a> enum sbc\_blocks\_number\_t
:   *Values:*

    <a id="_CPPv4N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_4E"></a>

    <a id="_CPPv3N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_4E"></a> <a id="_CPPv2N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_4E"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1af5ff930906135205dd50cd2fe1f5e6c3"></a> enumerator SBC\_BLOCK\_NUMBER\_4
    :   SBC blocks number 4

    <a id="_CPPv4N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_8E"></a>

    <a id="_CPPv3N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_8E"></a> <a id="_CPPv2N19sbc_blocks_number_t18SBC_BLOCK_NUMBER_8E"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1ac7338194901060b27cf6699ee7a546d3"></a> enumerator SBC\_BLOCK\_NUMBER\_8
    :   SBC blocks number 8

    <a id="_CPPv4N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_12E"></a>

    <a id="_CPPv3N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_12E"></a> <a id="_CPPv2N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_12E"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1a66b317336896d679dc0007e4fb470412"></a> enumerator SBC\_BLOCK\_NUMBER\_12
    :   SBC blocks number 12

    <a id="_CPPv4N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_16E"></a>

    <a id="_CPPv3N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_16E"></a> <a id="_CPPv2N19sbc_blocks_number_t19SBC_BLOCK_NUMBER_16E"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1a8681e32e764c86b6f3079b7cf3560a25"></a> enumerator SBC\_BLOCK\_NUMBER\_16
    :   SBC blocks number 16

    <a id="_CPPv4N19sbc_blocks_number_t20SBC_BLOCK_NUMBER_MAXE"></a>

    <a id="_CPPv3N19sbc_blocks_number_t20SBC_BLOCK_NUMBER_MAXE"></a> <a id="_CPPv2N19sbc_blocks_number_t20SBC_BLOCK_NUMBER_MAXE"></a> <a id="sbc__types_8h_1a4f62bd6b32fb9584f0c248d3e5db28e1a18382666a5d91faaef5f404605f9dc31"></a> enumerator SBC\_BLOCK\_NUMBER\_MAX

<a id="_CPPv423sbc_allocation_method_t"></a>

<a id="_CPPv323sbc_allocation_method_t"></a> <a id="_CPPv223sbc_allocation_method_t"></a> <a id="sbc__types_8h_1afa87e4f8b98310212c8cdece0cb46ca2"></a> enum sbc\_allocation\_method\_t
:   *Values:*

    <a id="_CPPv4N23sbc_allocation_method_t30SBC_ALLOCATION_METHOD_LOUDNESSE"></a>

    <a id="_CPPv3N23sbc_allocation_method_t30SBC_ALLOCATION_METHOD_LOUDNESSE"></a> <a id="_CPPv2N23sbc_allocation_method_t30SBC_ALLOCATION_METHOD_LOUDNESSE"></a> <a id="sbc__types_8h_1afa87e4f8b98310212c8cdece0cb46ca2a74e6e35651cc23cb167be236e7b9505b"></a> enumerator SBC\_ALLOCATION\_METHOD\_LOUDNESS
    :   SBC allocation method : Loudness

    <a id="_CPPv4N23sbc_allocation_method_t25SBC_ALLOCATION_METHOD_SNRE"></a>

    <a id="_CPPv3N23sbc_allocation_method_t25SBC_ALLOCATION_METHOD_SNRE"></a> <a id="_CPPv2N23sbc_allocation_method_t25SBC_ALLOCATION_METHOD_SNRE"></a> <a id="sbc__types_8h_1afa87e4f8b98310212c8cdece0cb46ca2a40e029bdd9b11a7fe75f21f283a8e257"></a> enumerator SBC\_ALLOCATION\_METHOD\_SNR
    :   SBC allocation method : SNR

    <a id="_CPPv4N23sbc_allocation_method_t29SBC_ALLOCATION_METHOD_INVALIDE"></a>

    <a id="_CPPv3N23sbc_allocation_method_t29SBC_ALLOCATION_METHOD_INVALIDE"></a> <a id="_CPPv2N23sbc_allocation_method_t29SBC_ALLOCATION_METHOD_INVALIDE"></a> <a id="sbc__types_8h_1afa87e4f8b98310212c8cdece0cb46ca2a0d3b02ea9f3e8f6ec24e78ead5349ecc"></a> enumerator SBC\_ALLOCATION\_METHOD\_INVALID
