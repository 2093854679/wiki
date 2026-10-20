---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/dma.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dma-api"></a>

# DMA API

DMA (Direct Memory Access) 直接内存访问API接口。

<a id="header-file"></a>

## Header File

- [dma.h](https://github.com/bekencorp/armino/blob/main/components/dma.h)

<a id="functions"></a>

## Functions

<a id="_CPPv418bk_dma_driver_initv"></a>

<a id="_CPPv318bk_dma_driver_initv"></a> <a id="_CPPv218bk_dma_driver_initv"></a> <a id="bk_dma_driver_init__void"></a> <a id="dma_8h_1a73b2d9b8bc2ffc0f58ecc31155baaf7a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_driver\_init(void)
:   Init the DMA driver.

    This API init the resoure common to all dma channels:

    - Init dma driver control memory

    This API should be called before any other dma APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_dma_driver_deinitv"></a>

<a id="_CPPv320bk_dma_driver_deinitv"></a> <a id="_CPPv220bk_dma_driver_deinitv"></a> <a id="bk_dma_driver_deinit__void"></a> <a id="dma_8h_1a80d12069cb2caa4e4a7fe22b3db2d8f9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_driver\_deinit(void)
:   Deinit the DMA driver.

    This API free all resource related to dma and power down all dma channels.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv412bk_dma_alloc3u16"></a>

<a id="_CPPv312bk_dma_alloc3u16"></a> <a id="_CPPv212bk_dma_alloc3u16"></a> <a id="bk_dma_alloc__u16"></a> <a id="dma_8h_1abde0b892831794141d591546265049c2"></a> dma\_id\_t bk\_dma\_alloc(u16 user\_id)
:   Allocate a DMA channel.

    This API should be called before any other dma channel APIs.

    **Attention**
    :   : This API can only be called in task context,

        - and can’t be called in context that interrupt is disabled.

    参数
    :   **user\_id** – DMA channel applicant

    返回
    :   DMA channel id.

        - \> DMA\_ID\_MAX: no free DMA channel.

<a id="_CPPv411bk_dma_free3u168dma_id_t"></a>

<a id="_CPPv311bk_dma_free3u168dma_id_t"></a> <a id="_CPPv211bk_dma_free3u168dma_id_t"></a> <a id="bk_dma_free__u16.dma_id_t"></a> <a id="dma_8h_1a853b26fe303ecb50e2036b3e45de7ece"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_free(u16 user\_id, dma\_id\_t id)
:   Free the DMA channel.

    **Attention**
    :   : This API can only be called in task context,

        - and can’t be called in context that interrupt is disabled.

    参数
    :   - **user\_id** – DMA channel applicant, the same as in bk\_dma\_alloc.
        - **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_dma_user8dma_id_t"></a>

<a id="_CPPv311bk_dma_user8dma_id_t"></a> <a id="_CPPv211bk_dma_user8dma_id_t"></a> <a id="bk_dma_user__dma_id_t"></a> <a id="dma_8h_1a0d03bf702fe84f0bab68fbce3195569d"></a> uint32\_t bk\_dma\_user(dma\_id\_t id)
:   get the user of DMA channel

    参数
    :   **id** – DMA channel

    返回
    :   DMA channel user\_id.

        - u32: high u16 is the CPU\_ID, low 16 bits is the applicant\_id.

<a id="_CPPv411bk_dma_init8dma_id_tPK12dma_config_t"></a>

<a id="_CPPv311bk_dma_init8dma_id_tPK12dma_config_t"></a> <a id="_CPPv211bk_dma_init8dma_id_tPK12dma_config_t"></a> <a id="bk_dma_init__dma_id_t.dma_config_tCP"></a> <a id="dma_8h_1a376d9a3e80dae84a1152e997115f960f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_init(dma\_id\_t id, const dma\_config\_t \*config)
:   Init the DMA channel.

    **Attention**
    :   1\. the higher channel priority value, the higher the priority

    参数
    :   - **id** – DMA channel
        - **config** – DMA configuration

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_DMA\_NOT\_INIT: DMA driver not init
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_DMA\_ID: invalid DMA channel
        - BK\_ERR\_DMA\_INVALID\_ADDR: invalid DMA address
        - others: other errors.

<a id="_CPPv413bk_dma_deinit8dma_id_t"></a>

<a id="_CPPv313bk_dma_deinit8dma_id_t"></a> <a id="_CPPv213bk_dma_deinit8dma_id_t"></a> <a id="bk_dma_deinit__dma_id_t"></a> <a id="dma_8h_1a0c8faae79624cbc99e9c55fc881925c9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_deinit(dma\_id\_t id)
:   Deinit a DMA channel.

    This API deinit the DMA channel:

    - Stop the DMA channel
    - Reset all configuration of DMA channel to default value

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv412bk_dma_start8dma_id_t"></a>

<a id="_CPPv312bk_dma_start8dma_id_t"></a> <a id="_CPPv212bk_dma_start8dma_id_t"></a> <a id="bk_dma_start__dma_id_t"></a> <a id="dma_8h_1aa6a1606f8ff5984db237fc8b34db5cde"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_start(dma\_id\_t id)
:   Start a DMA channel.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_dma_stop8dma_id_t"></a>

<a id="_CPPv311bk_dma_stop8dma_id_t"></a> <a id="_CPPv211bk_dma_stop8dma_id_t"></a> <a id="bk_dma_stop__dma_id_t"></a> <a id="dma_8h_1a5ccb3ecdcbd33fa05782cc1166ef60cf"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_stop(dma\_id\_t id)
:   Stop a DMA channel.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv412bk_dma_write8dma_id_tPK7uint8_t8uint32_t"></a>

<a id="_CPPv312bk_dma_write8dma_id_tPK7uint8_t8uint32_t"></a> <a id="_CPPv212bk_dma_write8dma_id_tPK7uint8_t8uint32_t"></a> <a id="bk_dma_write__dma_id_t.uint8_tCP.uint32_t"></a> <a id="dma_8h_1a3ad2cce0dec4040397e056c8531a933b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_write(dma\_id\_t id, const uint8\_t \*data, uint32\_t size)
:   Transfer data from memory to peripheral.

    参数
    :   - **id** – DMA channel
        - **data** – DMA transfer data
        - **size** – data size

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_dma_read8dma_id_tP7uint8_t8uint32_t"></a>

<a id="_CPPv311bk_dma_read8dma_id_tP7uint8_t8uint32_t"></a> <a id="_CPPv211bk_dma_read8dma_id_tP7uint8_t8uint32_t"></a> <a id="bk_dma_read__dma_id_t.uint8_tP.uint32_t"></a> <a id="dma_8h_1add6ed3b997cf88979d806fb43088b8d5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_read(dma\_id\_t id, uint8\_t \*data, uint32\_t size)
:   Transfer data from peripheral to memory.

    参数
    :   - **id** – DMA channel
        - **data** – DMA transfer data
        - **size** – data size

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_dma_enable_finish_interrupt8dma_id_t"></a>

<a id="_CPPv330bk_dma_enable_finish_interrupt8dma_id_t"></a> <a id="_CPPv230bk_dma_enable_finish_interrupt8dma_id_t"></a> <a id="bk_dma_enable_finish_interrupt__dma_id_t"></a> <a id="dma_8h_1a4daac7f221a2dcf83eeafc6fbfcd72a7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_finish\_interrupt(dma\_id\_t id)
:   Enable DMA finish intterrup.

    @NOTES before enable interrupt, please confirm have called bk\_dma\_register\_isr.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_dma_disable_finish_interrupt8dma_id_t"></a>

<a id="_CPPv331bk_dma_disable_finish_interrupt8dma_id_t"></a> <a id="_CPPv231bk_dma_disable_finish_interrupt8dma_id_t"></a> <a id="bk_dma_disable_finish_interrupt__dma_id_t"></a> <a id="dma_8h_1a3b3ac562a3a82c5459ba24c7cc6a07d1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_finish\_interrupt(dma\_id\_t id)
:   Disable DMA finish intterrup.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv435bk_dma_enable_half_finish_interrupt8dma_id_t"></a>

<a id="_CPPv335bk_dma_enable_half_finish_interrupt8dma_id_t"></a> <a id="_CPPv235bk_dma_enable_half_finish_interrupt8dma_id_t"></a> <a id="bk_dma_enable_half_finish_interrupt__dma_id_t"></a> <a id="dma_8h_1a4f2e0ba07755655b91dcf5697a8ace86"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_half\_finish\_interrupt(dma\_id\_t id)
:   Enable DMA half finish intterrup.

    @NOTES before enable interrupt, please confirm have called bk\_dma\_register\_isr.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_dma_disable_half_finish_interrupt8dma_id_t"></a>

<a id="_CPPv336bk_dma_disable_half_finish_interrupt8dma_id_t"></a> <a id="_CPPv236bk_dma_disable_half_finish_interrupt8dma_id_t"></a> <a id="bk_dma_disable_half_finish_interrupt__dma_id_t"></a> <a id="dma_8h_1ab45d98b1e096263d5bd3dd74386b9062"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_half\_finish\_interrupt(dma\_id\_t id)
:   Disable DMA half finish intterrup.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t"></a>

<a id="_CPPv319bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t"></a> <a id="_CPPv219bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t"></a> <a id="bk_dma_register_isr__dma_id_t.dma_isr_t.dma_isr_t"></a> <a id="dma_8h_1a20e473bb6de815ce031aa24647992074"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_register\_isr(dma\_id\_t id, dma\_isr\_t half\_finish\_isr, dma\_isr\_t finish\_isr)
:   Register the interrupt service routine for DMA channel.

    This API regist dma isr callback function.

    参数
    :   - **id** – DMA channel
        - **half\_finish\_isr** – DMA half finish callback
        - **finish\_isr** – DMA finish callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_dma_get_transfer_len_max8dma_id_t"></a>

<a id="_CPPv327bk_dma_get_transfer_len_max8dma_id_t"></a> <a id="_CPPv227bk_dma_get_transfer_len_max8dma_id_t"></a> <a id="bk_dma_get_transfer_len_max__dma_id_t"></a> <a id="dma_8h_1ae16b21c969d4252fb6308e848553b6f9"></a> uint32\_t bk\_dma\_get\_transfer\_len\_max(dma\_id\_t id)
:   get DMA transfer max length in one round, default value is 65536 bytes.

    参数
    :   **id** – DMA channel

    返回
    :   - max len: how many bytes can be copy by DMA in one round.

<a id="_CPPv423bk_dma_set_transfer_len8dma_id_t8uint32_t"></a>

<a id="_CPPv323bk_dma_set_transfer_len8dma_id_t8uint32_t"></a> <a id="_CPPv223bk_dma_set_transfer_len8dma_id_t8uint32_t"></a> <a id="bk_dma_set_transfer_len__dma_id_t.uint32_t"></a> <a id="dma_8h_1a118e528f09d01587dcfcbe59c0b667fe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_set\_transfer\_len(dma\_id\_t id, uint32\_t tran\_len)
:   Set DMA transfer length.

    参数
    :   - **id** – DMA channel
        - **tran\_len** – DMA transfer length, the tran\_len should be \<\= bk\_dma\_get\_transfer\_len\_max() bytes.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t"></a>

<a id="_CPPv319bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t"></a> <a id="_CPPv219bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t"></a> <a id="bk_dma_set_src_addr__dma_id_t.uint32_t.uint32_t"></a> <a id="dma_8h_1a0f5a03f0f26e3f9ad7919049e9790da3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_set\_src\_addr(dma\_id\_t id, uint32\_t start\_addr, uint32\_t end\_addr)
:   Set DMA source address.

    **Attention**
    :   1\. address should be zero when there is no value, e.g. bk\_dma\_set\_src\_addr(1, 0x80210C, 0\)

    参数
    :   - **id** – DMA channel
        - **start\_addr** – DMA source start address
        - **end\_addr** – DMA source end address

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_dma_set_src_start_addr8dma_id_t8uint32_t"></a>

<a id="_CPPv325bk_dma_set_src_start_addr8dma_id_t8uint32_t"></a> <a id="_CPPv225bk_dma_set_src_start_addr8dma_id_t8uint32_t"></a> <a id="bk_dma_set_src_start_addr__dma_id_t.uint32_t"></a> <a id="dma_8h_1a7290d18c07625b277dfac24de7771512"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_set\_src\_start\_addr(dma\_id\_t id, uint32\_t start\_addr)
:   Set DMA source start address.

    参数
    :   - **id** – DMA channel
        - **start\_addr** – DMA source start address

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t"></a>

<a id="_CPPv320bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t"></a> <a id="_CPPv220bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t"></a> <a id="bk_dma_set_dest_addr__dma_id_t.uint32_t.uint32_t"></a> <a id="dma_8h_1a298de6f08997dea0576e81eae1c2c102"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_set\_dest\_addr(dma\_id\_t id, uint32\_t start\_addr, uint32\_t end\_addr)
:   Set DMA dest address.

    **Attention**
    :   1\. address should be zero when there is no value, e.g. bk\_dma\_set\_dest\_addr(1, 0x80210C, 0\)

    参数
    :   - **id** – DMA channel
        - **start\_addr** – DMA dest start address
        - **end\_addr** – DMA dest end address

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_dma_set_dest_start_addr8dma_id_t8uint32_t"></a>

<a id="_CPPv326bk_dma_set_dest_start_addr8dma_id_t8uint32_t"></a> <a id="_CPPv226bk_dma_set_dest_start_addr8dma_id_t8uint32_t"></a> <a id="bk_dma_set_dest_start_addr__dma_id_t.uint32_t"></a> <a id="dma_8h_1afa31ad5ed8f44ca27dc1d0506843cb48"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_set\_dest\_start\_addr(dma\_id\_t id, uint32\_t start\_addr)
:   Set DMA dest start address.

    参数
    :   - **id** – DMA channel
        - **start\_addr** – DMA dest start address

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_dma_enable_src_addr_increase8dma_id_t"></a>

<a id="_CPPv331bk_dma_enable_src_addr_increase8dma_id_t"></a> <a id="_CPPv231bk_dma_enable_src_addr_increase8dma_id_t"></a> <a id="bk_dma_enable_src_addr_increase__dma_id_t"></a> <a id="dma_8h_1a9fdce512c415977373bde7e6962e3ff1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_src\_addr\_increase(dma\_id\_t id)
:   Enable DMA source address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv432bk_dma_disable_src_addr_increase8dma_id_t"></a>

<a id="_CPPv332bk_dma_disable_src_addr_increase8dma_id_t"></a> <a id="_CPPv232bk_dma_disable_src_addr_increase8dma_id_t"></a> <a id="bk_dma_disable_src_addr_increase__dma_id_t"></a> <a id="dma_8h_1a42e084adc21c26df39807376f438e0a1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_src\_addr\_increase(dma\_id\_t id)
:   Disable DMA source address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_dma_enable_src_addr_loop8dma_id_t"></a>

<a id="_CPPv327bk_dma_enable_src_addr_loop8dma_id_t"></a> <a id="_CPPv227bk_dma_enable_src_addr_loop8dma_id_t"></a> <a id="bk_dma_enable_src_addr_loop__dma_id_t"></a> <a id="dma_8h_1a4dc7e313f407ecbe1f7a811ef5e6cda1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_src\_addr\_loop(dma\_id\_t id)
:   Enable DMA source address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_dma_disable_src_addr_loop8dma_id_t"></a>

<a id="_CPPv328bk_dma_disable_src_addr_loop8dma_id_t"></a> <a id="_CPPv228bk_dma_disable_src_addr_loop8dma_id_t"></a> <a id="bk_dma_disable_src_addr_loop__dma_id_t"></a> <a id="dma_8h_1a91f403004c4097936bcd1fdde183525b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_src\_addr\_loop(dma\_id\_t id)
:   Disable DMA source address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv432bk_dma_enable_dest_addr_increase8dma_id_t"></a>

<a id="_CPPv332bk_dma_enable_dest_addr_increase8dma_id_t"></a> <a id="_CPPv232bk_dma_enable_dest_addr_increase8dma_id_t"></a> <a id="bk_dma_enable_dest_addr_increase__dma_id_t"></a> <a id="dma_8h_1a5c717db94762a6f1bfbdb8511701c29a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_dest\_addr\_increase(dma\_id\_t id)
:   Enable DMA dest address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv433bk_dma_disable_dest_addr_increase8dma_id_t"></a>

<a id="_CPPv333bk_dma_disable_dest_addr_increase8dma_id_t"></a> <a id="_CPPv233bk_dma_disable_dest_addr_increase8dma_id_t"></a> <a id="bk_dma_disable_dest_addr_increase__dma_id_t"></a> <a id="dma_8h_1a587ad797d2627e4475dc66c2082e59b2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_dest\_addr\_increase(dma\_id\_t id)
:   Disable DMA dest address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_dma_enable_dest_addr_loop8dma_id_t"></a>

<a id="_CPPv328bk_dma_enable_dest_addr_loop8dma_id_t"></a> <a id="_CPPv228bk_dma_enable_dest_addr_loop8dma_id_t"></a> <a id="bk_dma_enable_dest_addr_loop__dma_id_t"></a> <a id="dma_8h_1af2fbaaf1f18d9842680d3510e6c01fa4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_enable\_dest\_addr\_loop(dma\_id\_t id)
:   Enable DMA dest address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_dma_disable_dest_addr_loop8dma_id_t"></a>

<a id="_CPPv329bk_dma_disable_dest_addr_loop8dma_id_t"></a> <a id="_CPPv229bk_dma_disable_dest_addr_loop8dma_id_t"></a> <a id="bk_dma_disable_dest_addr_loop__dma_id_t"></a> <a id="dma_8h_1a1e34578a5f3c89961476d1ab1dcaced5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_disable\_dest\_addr\_loop(dma\_id\_t id)
:   Disable DMA dest address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_dma_get_remain_len8dma_id_t"></a>

<a id="_CPPv321bk_dma_get_remain_len8dma_id_t"></a> <a id="_CPPv221bk_dma_get_remain_len8dma_id_t"></a> <a id="bk_dma_get_remain_len__dma_id_t"></a> <a id="dma_8h_1aceadc57e8f0f338e7832832a096102e5"></a> uint32\_t bk\_dma\_get\_remain\_len(dma\_id\_t id)
:   Get DMA transfer remain length.

    参数
    :   **id** – DMA channel

    返回
    :   DMA transfer remain length

<a id="_CPPv424bk_dma_get_enable_status8dma_id_t"></a>

<a id="_CPPv324bk_dma_get_enable_status8dma_id_t"></a> <a id="_CPPv224bk_dma_get_enable_status8dma_id_t"></a> <a id="bk_dma_get_enable_status__dma_id_t"></a> <a id="dma_8h_1a084d1d2afb3976ea82fbeee12868f4ed"></a> uint32\_t bk\_dma\_get\_enable\_status(dma\_id\_t id)
:   Gets the current DMA channel working status.

    参数
    :   **id** – DMA channel

    返回
    :   - 0: Channel idle state
        - others: Channel busy state.

<a id="_CPPv423bk_dma_flush_src_buffer8dma_id_t"></a>

<a id="_CPPv323bk_dma_flush_src_buffer8dma_id_t"></a> <a id="_CPPv223bk_dma_flush_src_buffer8dma_id_t"></a> <a id="bk_dma_flush_src_buffer__dma_id_t"></a> <a id="dma_8h_1a7e95b713bd0f87f2316278acb8cedef0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dma\_flush\_src\_buffer(dma\_id\_t id)
:   flush reserved data in dma internal buffer I.E:If source data width is not 4bytes, and data size isn’t 4bytes align, but dest data width is 4bytes, then maybe 1\~3 bytes data reserved in dma internal buffer, then the left 1\~3 bytes data not copy to dest address.

    参数
    :   - **id** – DMA channel
        - **attr** – DMA privileged attr

    返回
    :   - 0: Channel idle state
        - others: Channel busy state.
