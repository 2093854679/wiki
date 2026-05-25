# DMA[](#dma "永久链接至标题")

[[English]](../../../../en/v2.0.1/api-reference/peripheral/bk_dma.html "../../../../en/v2.0.1/api-reference/peripheral/bk_dma.html")


## DMA API Status[](#dma-api-status "永久链接至标题")

| API | BK7258 |
| --- | --- |
| [`bk_dma_driver_init()`](#_CPPv418bk_dma_driver_initv "bk_dma_driver_init") | Y |
| [`bk_dma_driver_deinit()`](#_CPPv420bk_dma_driver_deinitv "bk_dma_driver_deinit") | Y |
| [`bk_dma_alloc()`](#_CPPv412bk_dma_alloc3u16 "bk_dma_alloc") | Y |
| `bk_fixed_dma_alloc()` | Y |
| [`bk_dma_free()`](#_CPPv411bk_dma_free3u168dma_id_t "bk_dma_free") | Y |
| [`bk_dma_user()`](#_CPPv411bk_dma_user8dma_id_t "bk_dma_user") | Y |
| [`bk_dma_init()`](#_CPPv411bk_dma_init8dma_id_tPK12dma_config_t "bk_dma_init") | Y |
| [`bk_dma_deinit()`](#_CPPv413bk_dma_deinit8dma_id_t "bk_dma_deinit") | Y |
| [`bk_dma_start()`](#_CPPv412bk_dma_start8dma_id_t "bk_dma_start") | Y |
| [`bk_dma_stop()`](#_CPPv411bk_dma_stop8dma_id_t "bk_dma_stop") | Y |
| [`bk_dma_write()`](#_CPPv412bk_dma_write8dma_id_tPK7uint8_t8uint32_t "bk_dma_write") | Y |
| [`bk_dma_read()`](#_CPPv411bk_dma_read8dma_id_tP7uint8_t8uint32_t "bk_dma_read") | Y |
| [`bk_dma_enable_finish_interrupt()`](#_CPPv430bk_dma_enable_finish_interrupt8dma_id_t "bk_dma_enable_finish_interrupt") | Y |
| [`bk_dma_disable_finish_interrupt()`](#_CPPv431bk_dma_disable_finish_interrupt8dma_id_t "bk_dma_disable_finish_interrupt") | Y |
| [`bk_dma_enable_half_finish_interrupt()`](#_CPPv435bk_dma_enable_half_finish_interrupt8dma_id_t "bk_dma_enable_half_finish_interrupt") | Y |
| [`bk_dma_disable_half_finish_interrupt()`](#_CPPv436bk_dma_disable_half_finish_interrupt8dma_id_t "bk_dma_disable_half_finish_interrupt") | Y |
| [`bk_dma_register_isr()`](#_CPPv419bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t "bk_dma_register_isr") | Y |
| `bk_dma_register_bus_err_isr()` | Y |
| [`bk_dma_set_src_addr()`](#_CPPv419bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t "bk_dma_set_src_addr") | Y |
| [`bk_dma_set_dest_addr()`](#_CPPv420bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t "bk_dma_set_dest_addr") | Y |
| [`bk_dma_set_dest_start_addr()`](#_CPPv426bk_dma_set_dest_start_addr8dma_id_t8uint32_t "bk_dma_set_dest_start_addr") | Y |
| [`bk_dma_set_transfer_len()`](#_CPPv423bk_dma_set_transfer_len8dma_id_t8uint32_t "bk_dma_set_transfer_len") | Y |
| [`bk_dma_get_remain_len()`](#_CPPv421bk_dma_get_remain_len8dma_id_t "bk_dma_get_remain_len") | Y |
| [`bk_dma_enable_src_addr_increase()`](#_CPPv431bk_dma_enable_src_addr_increase8dma_id_t "bk_dma_enable_src_addr_increase") | Y |
| [`bk_dma_disable_src_addr_increase()`](#_CPPv432bk_dma_disable_src_addr_increase8dma_id_t "bk_dma_disable_src_addr_increase") | Y |
| [`bk_dma_enable_src_addr_loop()`](#_CPPv427bk_dma_enable_src_addr_loop8dma_id_t "bk_dma_enable_src_addr_loop") | Y |
| [`bk_dma_disable_src_addr_loop()`](#_CPPv428bk_dma_disable_src_addr_loop8dma_id_t "bk_dma_disable_src_addr_loop") | Y |
| [`bk_dma_enable_dest_addr_increase()`](#_CPPv432bk_dma_enable_dest_addr_increase8dma_id_t "bk_dma_enable_dest_addr_increase") | Y |
| [`bk_dma_disable_dest_addr_increase()`](#_CPPv433bk_dma_disable_dest_addr_increase8dma_id_t "bk_dma_disable_dest_addr_increase") | Y |
| [`bk_dma_enable_dest_addr_loop()`](#_CPPv428bk_dma_enable_dest_addr_loop8dma_id_t "bk_dma_enable_dest_addr_loop") | Y |
| [`bk_dma_disable_dest_addr_loop()`](#_CPPv429bk_dma_disable_dest_addr_loop8dma_id_t "bk_dma_disable_dest_addr_loop") | Y |
| [`bk_dma_get_enable_status()`](#_CPPv424bk_dma_get_enable_status8dma_id_t "bk_dma_get_enable_status") | Y |
| [`bk_dma_flush_src_buffer()`](#_CPPv423bk_dma_flush_src_buffer8dma_id_t "bk_dma_flush_src_buffer") | Y |


## DMA Channel Number[](#dma-channel-number "永久链接至标题")

| Capability | BK7258 |
| --- | --- |
| Channel Number | 16 |


## DMA API Reference[](#dma-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [dma.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dma.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dma.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_driver_init(void)[](#_CPPv418bk_dma_driver_initv "永久链接至目标")
:   Init the DMA driver.

    This API init the resoure common to all dma channels:


    - Init dma driver control memory

    This API should be called before any other dma APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_driver_deinit(void)[](#_CPPv420bk_dma_driver_deinitv "永久链接至目标")
:   Deinit the DMA driver.

    This API free all resource related to dma and power down all dma channels.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[dma_id_t](#_CPPv48dma_id_t "dma_id_t") bk_dma_alloc(u16 user_id)[](#_CPPv412bk_dma_alloc3u16 "永久链接至目标")
:   Allocate a DMA channel.

    This API should be called before any other dma channel APIs.


    **Attention**
    :   : This API can only be called in task context,


        - and can’t be called in context that interrupt is disabled.

    参数
    :   **user_id** – DMA channel applicant

    返回
    :   DMA channel id.


        - > DMA_ID_MAX: no free DMA channel.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_free(u16 user_id, [dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv411bk_dma_free3u168dma_id_t "永久链接至目标")
:   Free the DMA channel.


    **Attention**
    :   : This API can only be called in task context,


        - and can’t be called in context that interrupt is disabled.

    参数
    :   - **user_id** – DMA channel applicant, the same as in bk_dma_alloc.

        - **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_dma_user([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv411bk_dma_user8dma_id_t "永久链接至目标")
:   get the user of DMA channel

    参数
    :   **id** – DMA channel

    返回
    :   DMA channel user_id.


        - u32: high u16 is the CPU_ID, low 16 bits is the applicant_id.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_init([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, const [dma_config_t](#_CPPv412dma_config_t "dma_config_t") *config)[](#_CPPv411bk_dma_init8dma_id_tPK12dma_config_t "永久链接至目标")
:   Init the DMA channel.


    **Attention**
    :   1. the higher channel priority value, the higher the priority

    参数
    :   - **id** – DMA channel

        - **config** – DMA configuration

    返回
    :   - BK_OK: succeed

        - BK_ERR_DMA_NOT_INIT: DMA driver not init

        - BK_ERR_NULL_PARAM: config is NULL

        - BK_ERR_DMA_ID: invalid DMA channel

        - BK_ERR_DMA_INVALID_ADDR: invalid DMA address

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_deinit([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv413bk_dma_deinit8dma_id_t "永久链接至目标")
:   Deinit a DMA channel.

    This API deinit the DMA channel:


    - Stop the DMA channel

    - Reset all configuration of DMA channel to default value

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_start([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv412bk_dma_start8dma_id_t "永久链接至目标")
:   Start a DMA channel.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_stop([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv411bk_dma_stop8dma_id_t "永久链接至目标")
:   Stop a DMA channel.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_write([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, const uint8_t *data, uint32_t size)[](#_CPPv412bk_dma_write8dma_id_tPK7uint8_t8uint32_t "永久链接至目标")
:   Transfer data from memory to peripheral.

    参数
    :   - **id** – DMA channel

        - **data** – DMA transfer data

        - **size** – data size

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_read([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint8_t *data, uint32_t size)[](#_CPPv411bk_dma_read8dma_id_tP7uint8_t8uint32_t "永久链接至目标")
:   Transfer data from peripheral to memory.

    参数
    :   - **id** – DMA channel

        - **data** – DMA transfer data

        - **size** – data size

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_finish_interrupt([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv430bk_dma_enable_finish_interrupt8dma_id_t "永久链接至目标")
:   Enable DMA finish intterrup.

    @NOTES before enable interrupt, please confirm have called bk_dma_register_isr.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_finish_interrupt([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv431bk_dma_disable_finish_interrupt8dma_id_t "永久链接至目标")
:   Disable DMA finish intterrup.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_half_finish_interrupt([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv435bk_dma_enable_half_finish_interrupt8dma_id_t "永久链接至目标")
:   Enable DMA half finish intterrup.

    @NOTES before enable interrupt, please confirm have called bk_dma_register_isr.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_half_finish_interrupt([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv436bk_dma_disable_half_finish_interrupt8dma_id_t "永久链接至目标")
:   Disable DMA half finish intterrup.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_register_isr([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, [dma_isr_t](#_CPPv49dma_isr_t "dma_isr_t") half_finish_isr, [dma_isr_t](#_CPPv49dma_isr_t "dma_isr_t") finish_isr)[](#_CPPv419bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t "永久链接至目标")
:   Register the interrupt service routine for DMA channel.

    This API regist dma isr callback function.

    参数
    :   - **id** – DMA channel

        - **half_finish_isr** – DMA half finish callback

        - **finish_isr** – DMA finish callback

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_dma_get_transfer_len_max([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv427bk_dma_get_transfer_len_max8dma_id_t "永久链接至目标")
:   get DMA transfer max length in one round, default value is 65536 bytes.

    参数
    :   **id** – DMA channel

    返回
    :   - max len: how many bytes can be copy by DMA in one round.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_set_transfer_len([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint32_t tran_len)[](#_CPPv423bk_dma_set_transfer_len8dma_id_t8uint32_t "永久链接至目标")
:   Set DMA transfer length.

    参数
    :   - **id** – DMA channel

        - **tran_len** – DMA transfer length, the tran_len should be <= bk_dma_get_transfer_len_max() bytes.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_set_src_addr([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint32_t start_addr, uint32_t end_addr)[](#_CPPv419bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t "永久链接至目标")
:   Set DMA source address.


    **Attention**
    :   1. address should be zero when there is no value, e.g. bk_dma_set_src_addr(1, 0x80210C, 0)

    参数
    :   - **id** – DMA channel

        - **start_addr** – DMA source start address

        - **end_addr** – DMA source end address

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_set_src_start_addr([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint32_t start_addr)[](#_CPPv425bk_dma_set_src_start_addr8dma_id_t8uint32_t "永久链接至目标")
:   Set DMA source start address.

    参数
    :   - **id** – DMA channel

        - **start_addr** – DMA source start address

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_set_dest_addr([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint32_t start_addr, uint32_t end_addr)[](#_CPPv420bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t "永久链接至目标")
:   Set DMA dest address.


    **Attention**
    :   1. address should be zero when there is no value, e.g. bk_dma_set_dest_addr(1, 0x80210C, 0)

    参数
    :   - **id** – DMA channel

        - **start_addr** – DMA dest start address

        - **end_addr** – DMA dest end address

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_set_dest_start_addr([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id, uint32_t start_addr)[](#_CPPv426bk_dma_set_dest_start_addr8dma_id_t8uint32_t "永久链接至目标")
:   Set DMA dest start address.

    参数
    :   - **id** – DMA channel

        - **start_addr** – DMA dest start address

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_src_addr_increase([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv431bk_dma_enable_src_addr_increase8dma_id_t "永久链接至目标")
:   Enable DMA source address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_src_addr_increase([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv432bk_dma_disable_src_addr_increase8dma_id_t "永久链接至目标")
:   Disable DMA source address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_src_addr_loop([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv427bk_dma_enable_src_addr_loop8dma_id_t "永久链接至目标")
:   Enable DMA source address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_src_addr_loop([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv428bk_dma_disable_src_addr_loop8dma_id_t "永久链接至目标")
:   Disable DMA source address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_dest_addr_increase([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv432bk_dma_enable_dest_addr_increase8dma_id_t "永久链接至目标")
:   Enable DMA dest address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_dest_addr_increase([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv433bk_dma_disable_dest_addr_increase8dma_id_t "永久链接至目标")
:   Disable DMA dest address increase.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_enable_dest_addr_loop([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv428bk_dma_enable_dest_addr_loop8dma_id_t "永久链接至目标")
:   Enable DMA dest address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_disable_dest_addr_loop([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv429bk_dma_disable_dest_addr_loop8dma_id_t "永久链接至目标")
:   Disable DMA dest address loop.

    参数
    :   **id** – DMA channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_dma_get_remain_len([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv421bk_dma_get_remain_len8dma_id_t "永久链接至目标")
:   Get DMA transfer remain length.

    参数
    :   **id** – DMA channel

    返回
    :   DMA transfer remain length

uint32_t bk_dma_get_enable_status([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv424bk_dma_get_enable_status8dma_id_t "永久链接至目标")
:   Gets the current DMA channel working status.

    参数
    :   **id** – DMA channel

    返回
    :   - 0: Channel idle state

        - others: Channel busy state.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dma_flush_src_buffer([dma_id_t](#_CPPv48dma_id_t "dma_id_t") id)[](#_CPPv423bk_dma_flush_src_buffer8dma_id_t "永久链接至目标")
:   flush reserved data in dma internal buffer I.E:If source data width is not 4bytes, and data size isn’t 4bytes align, but dest data width is 4bytes, then maybe 1~3 bytes data reserved in dma internal buffer, then the left 1~3 bytes data not copy to dest address.

    参数
    :   - **id** – DMA channel

        - **attr** – DMA privileged attr

    返回
    :   - 0: Channel idle state

        - others: Channel busy state.


## DMA API Typedefs[](#dma-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [dma_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dma_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dma_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_DMA_ID[](#c.BK_ERR_DMA_ID "永久链接至目标")
:   DMA id is invalid

BK_ERR_DMA_NOT_INIT[](#c.BK_ERR_DMA_NOT_INIT "永久链接至目标")
:   DMA driver not init

BK_ERR_DMA_ID_NOT_INIT[](#c.BK_ERR_DMA_ID_NOT_INIT "永久链接至目标")
:   DMA id not init

BK_ERR_DMA_ID_NOT_START[](#c.BK_ERR_DMA_ID_NOT_START "永久链接至目标")
:   DMA id not start

BK_ERR_DMA_INVALID_ADDR[](#c.BK_ERR_DMA_INVALID_ADDR "永久链接至目标")
:   DMA addr is invalid

BK_ERR_DMA_ID_REINIT[](#c.BK_ERR_DMA_ID_REINIT "永久链接至目标")
:   DMA id has inited, if reinit,please de-init firstly

BK_ERR_DMA_TRANS_LEN[](#c.BK_ERR_DMA_TRANS_LEN "永久链接至目标")
:   DMA trans len is invalid


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*dma_isr_t)([dma_id_t](#_CPPv48dma_id_t "dma_id_t") dma_id)[](#_CPPv49dma_isr_t "永久链接至目标")
:   DMA interrupt service routine.


### Header File[](#id2 "永久链接至标题")


- [hal/hal_dma_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_dma_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_dma_types.h")


### Structures[](#structures "永久链接至标题")

struct dma_port_config_t[](#_CPPv417dma_port_config_t "永久链接至目标")
:   Public Members

    [dma_dev_t](#_CPPv49dma_dev_t "dma_dev_t") dev[](#_CPPv4N17dma_port_config_t3devE "永久链接至目标")
    :   DMA device

    [dma_data_width_t](#_CPPv416dma_data_width_t "dma_data_width_t") width[](#_CPPv4N17dma_port_config_t5widthE "永久链接至目标")
    :   DMA data width

    [dma_addr_inc_t](#_CPPv414dma_addr_inc_t "dma_addr_inc_t") addr_inc_en[](#_CPPv4N17dma_port_config_t11addr_inc_enE "永久链接至目标")
    :   enable/disable DMA address increase

    [dma_addr_loop_t](#_CPPv415dma_addr_loop_t "dma_addr_loop_t") addr_loop_en[](#_CPPv4N17dma_port_config_t12addr_loop_enE "永久链接至目标")
    :   enable/disable DMA address loop

    uint32_t start_addr[](#_CPPv4N17dma_port_config_t10start_addrE "永久链接至目标")
    :   DMA start address

    uint32_t end_addr[](#_CPPv4N17dma_port_config_t8end_addrE "永久链接至目标")
    :   DMA end address

struct dma_config_t[](#_CPPv412dma_config_t "永久链接至目标")
:   Public Members

    [dma_work_mode_t](#_CPPv415dma_work_mode_t "dma_work_mode_t") mode[](#_CPPv4N12dma_config_t4modeE "永久链接至目标")
    :   DMA work mode

    [dma_chan_priority_t](#_CPPv419dma_chan_priority_t "dma_chan_priority_t") chan_prio[](#_CPPv4N12dma_config_t9chan_prioE "永久链接至目标")
    :   DMA channel prioprity

    [dma_port_config_t](#_CPPv417dma_port_config_t "dma_port_config_t") src[](#_CPPv4N12dma_config_t3srcE "永久链接至目标")
    :   DMA source configuration

    [dma_port_config_t](#_CPPv417dma_port_config_t "dma_port_config_t") dst[](#_CPPv4N12dma_config_t3dstE "永久链接至目标")
    :   DMA dest configuration

    [dma_pixel_trans_type_t](#_CPPv422dma_pixel_trans_type_t "dma_pixel_trans_type_t") trans_type[](#_CPPv4N12dma_config_t10trans_typeE "永久链接至目标")
    :   DMA TRANS TYPE

    uint32_t dest_wr_intlv[](#_CPPv4N12dma_config_t13dest_wr_intlvE "永久链接至目标")
    :   DMA Destination Write operate interval.unit is cycle

    uint32_t src_rd_intlv[](#_CPPv4N12dma_config_t12src_rd_intlvE "永久链接至目标")
    :   DMA Source Read operate interval.unit is cycle


### Macros[](#id3 "永久链接至标题")

BK_ERR_DMA_HAL_INVALID_ADDR[](#c.BK_ERR_DMA_HAL_INVALID_ADDR "永久链接至目标")


### Type Definitions[](#id4 "永久链接至标题")

typedef uint8_t dma_unit_t[](#_CPPv410dma_unit_t "永久链接至目标")
:   DMA uint id

typedef uint8_t dma_chan_priority_t[](#_CPPv419dma_chan_priority_t "永久链接至目标")
:   DMA channel priority:the value is higher then the priority is higher


### Enumerations[](#enumerations "永久链接至标题")

enum dma_int_id_t[](#_CPPv412dma_int_id_t "永久链接至目标")
:   CPU core for DMA Interrupt Differentiation Notification.

    @Enumeration option selection core notifies DMA to interrupt after completion of transport

    @Notification of terminal selection based on channel operation


    *Values:*

    enumerator DMA_INT_0[](#_CPPv4N12dma_int_id_t9DMA_INT_0E "永久链接至目标")
    :   DMA INT 0

    enumerator DMA_INT_1[](#_CPPv4N12dma_int_id_t9DMA_INT_1E "永久链接至目标")
    :   DMA INT 1

    enumerator DMA_INT_2[](#_CPPv4N12dma_int_id_t9DMA_INT_2E "永久链接至目标")
    :   DMA INT 2

    enumerator DMA_INT_3[](#_CPPv4N12dma_int_id_t9DMA_INT_3E "永久链接至目标")
    :   DMA INT 3

    enumerator DMA_INT_MAX[](#_CPPv4N12dma_int_id_t11DMA_INT_MAXE "永久链接至目标")
    :   DMA channel max

enum dma_dev_t[](#_CPPv49dma_dev_t "永久链接至目标")
:   *Values:*

    enumerator DMA_DEV_DTCM[](#_CPPv4N9dma_dev_t12DMA_DEV_DTCME "永久链接至目标")
    :   DMA device DTCM

    enumerator DMA_DEV_LA[](#_CPPv4N9dma_dev_t10DMA_DEV_LAE "永久链接至目标")
    :   DMA device LA

    enumerator DMA_DEV_HSSPI[](#_CPPv4N9dma_dev_t13DMA_DEV_HSSPIE "永久链接至目标")
    :   DMA device HSSPI

    enumerator DMA_DEV_AUDIO[](#_CPPv4N9dma_dev_t13DMA_DEV_AUDIOE "永久链接至目标")
    :   DMA device AUDIO

    enumerator DMA_DEV_AUDIO_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_AUDIO_RXE "永久链接至目标")
    :   DMA device AUDIO

    enumerator DMA_DEV_SDIO[](#_CPPv4N9dma_dev_t12DMA_DEV_SDIOE "永久链接至目标")
    :   DMA device SDIO

    enumerator DMA_DEV_SDIO_RX[](#_CPPv4N9dma_dev_t15DMA_DEV_SDIO_RXE "永久链接至目标")
    :   DMA device SDIO

    enumerator DMA_DEV_UART1[](#_CPPv4N9dma_dev_t13DMA_DEV_UART1E "永久链接至目标")
    :   DMA device UART1

    enumerator DMA_DEV_UART1_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_UART1_RXE "永久链接至目标")
    :   DMA device UART1

    enumerator DMA_DEV_UART2[](#_CPPv4N9dma_dev_t13DMA_DEV_UART2E "永久链接至目标")
    :   DMA device UART2

    enumerator DMA_DEV_UART2_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_UART2_RXE "永久链接至目标")
    :   DMA device UART 2 RX

    enumerator DMA_DEV_UART3[](#_CPPv4N9dma_dev_t13DMA_DEV_UART3E "永久链接至目标")
    :   DMA device UART3

    enumerator DMA_DEV_UART3_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_UART3_RXE "永久链接至目标")
    :   DMA device UART3

    enumerator DMA_DEV_I2S[](#_CPPv4N9dma_dev_t11DMA_DEV_I2SE "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S_CH1[](#_CPPv4N9dma_dev_t15DMA_DEV_I2S_CH1E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S_CH2[](#_CPPv4N9dma_dev_t15DMA_DEV_I2S_CH2E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S_RX[](#_CPPv4N9dma_dev_t14DMA_DEV_I2S_RXE "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S_RX_CH1[](#_CPPv4N9dma_dev_t18DMA_DEV_I2S_RX_CH1E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S_RX_CH2[](#_CPPv4N9dma_dev_t18DMA_DEV_I2S_RX_CH2E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S1[](#_CPPv4N9dma_dev_t12DMA_DEV_I2S1E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S1_RX[](#_CPPv4N9dma_dev_t15DMA_DEV_I2S1_RXE "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S2[](#_CPPv4N9dma_dev_t12DMA_DEV_I2S2E "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_I2S2_RX[](#_CPPv4N9dma_dev_t15DMA_DEV_I2S2_RXE "永久链接至目标")
    :   DMA device I2S

    enumerator DMA_DEV_GSPI0[](#_CPPv4N9dma_dev_t13DMA_DEV_GSPI0E "永久链接至目标")
    :   DMA device GSPI1

    enumerator DMA_DEV_GSPI0_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_GSPI0_RXE "永久链接至目标")
    :   DMA device GSPI1

    enumerator DMA_DEV_GSPI1[](#_CPPv4N9dma_dev_t13DMA_DEV_GSPI1E "永久链接至目标")
    :   DMA device GSPI2

    enumerator DMA_DEV_GSPI1_RX[](#_CPPv4N9dma_dev_t16DMA_DEV_GSPI1_RXE "永久链接至目标")
    :   DMA device GSPI2

    enumerator DMA_DEV_GSPI2[](#_CPPv4N9dma_dev_t13DMA_DEV_GSPI2E "永久链接至目标")
    :   DMA device GSPI3

    enumerator DMA_DEV_JPEG[](#_CPPv4N9dma_dev_t12DMA_DEV_JPEGE "永久链接至目标")
    :   DMA device JPEG

    enumerator DMA_DEV_PSRAM_VIDEO[](#_CPPv4N9dma_dev_t19DMA_DEV_PSRAM_VIDEOE "永久链接至目标")
    :   DMA device PSRAM VIDEO

    enumerator DMA_DEV_PSRAM_AUDIO[](#_CPPv4N9dma_dev_t19DMA_DEV_PSRAM_AUDIOE "永久链接至目标")
    :   DMA device PSRAM AUDIO

    enumerator DMA_DEV_USB[](#_CPPv4N9dma_dev_t11DMA_DEV_USBE "永久链接至目标")
    :   DMA device USB

    enumerator DMA_DEV_LCD_CMD[](#_CPPv4N9dma_dev_t15DMA_DEV_LCD_CMDE "永久链接至目标")
    :   DMA device LCD CMD

    enumerator DMA_DEV_LCD_DATA[](#_CPPv4N9dma_dev_t16DMA_DEV_LCD_DATAE "永久链接至目标")
    :   DMA device LCD DATA

    enumerator DMA_DEV_DISP_RX[](#_CPPv4N9dma_dev_t15DMA_DEV_DISP_RXE "永久链接至目标")
    :   DMA device DISP RX

    enumerator DMA_DEV_SDMADC_RX[](#_CPPv4N9dma_dev_t17DMA_DEV_SDMADC_RXE "永久链接至目标")
    :   DMA device SDMADC RX

    enumerator DMA_DEV_AHB_MEM[](#_CPPv4N9dma_dev_t15DMA_DEV_AHB_MEME "永久链接至目标")
    :   DMA device AHB_MEM

    enumerator DMA_DEV_SPI0[](#_CPPv4N9dma_dev_t12DMA_DEV_SPI0E "永久链接至目标")
    :   DMA device SPI 0

    enumerator DMA_DEV_SPI1[](#_CPPv4N9dma_dev_t12DMA_DEV_SPI1E "永久链接至目标")
    :   DMA device SPI 1

    enumerator DMA_DEV_H264[](#_CPPv4N9dma_dev_t12DMA_DEV_H264E "永久链接至目标")
    :   DMA device H264

    enumerator DMA_DEV_MAX[](#_CPPv4N9dma_dev_t11DMA_DEV_MAXE "永久链接至目标")

enum dma_data_width_t[](#_CPPv416dma_data_width_t "永久链接至目标")
:   *Values:*

    enumerator DMA_DATA_WIDTH_8BITS[](#_CPPv4N16dma_data_width_t20DMA_DATA_WIDTH_8BITSE "永久链接至目标")
    :   DMA data width 8bit

    enumerator DMA_DATA_WIDTH_16BITS[](#_CPPv4N16dma_data_width_t21DMA_DATA_WIDTH_16BITSE "永久链接至目标")
    :   DMA data width 16bit

    enumerator DMA_DATA_WIDTH_32BITS[](#_CPPv4N16dma_data_width_t21DMA_DATA_WIDTH_32BITSE "永久链接至目标")
    :   DMA data width 32bit

enum dma_work_mode_t[](#_CPPv415dma_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator DMA_WORK_MODE_SINGLE[](#_CPPv4N15dma_work_mode_t20DMA_WORK_MODE_SINGLEE "永久链接至目标")
    :   DMA work mode single_mode

    enumerator DMA_WORK_MODE_REPEAT[](#_CPPv4N15dma_work_mode_t20DMA_WORK_MODE_REPEATE "永久链接至目标")
    :   DMA work mode repeat_mode (forever repeat until software clear dma_en)

enum dma_priority_mode_t[](#_CPPv419dma_priority_mode_t "永久链接至目标")
:   *Values:*

    enumerator DMA_PRIO_MODE_ROUND_ROBIN[](#_CPPv4N19dma_priority_mode_t25DMA_PRIO_MODE_ROUND_ROBINE "永久链接至目标")
    :   DMA priority mode round-robin(all dma priority are the same)

    enumerator DMA_PRIO_MODE_FIXED_PRIO[](#_CPPv4N19dma_priority_mode_t24DMA_PRIO_MODE_FIXED_PRIOE "永久链接至目标")
    :   DMA priority mode fixed prio(depend on chan_prio)

enum dma_addr_inc_t[](#_CPPv414dma_addr_inc_t "永久链接至目标")
:   *Values:*

    enumerator DMA_ADDR_INC_DISABLE[](#_CPPv4N14dma_addr_inc_t20DMA_ADDR_INC_DISABLEE "永久链接至目标")
    :   DMA disable addrress increase

    enumerator DMA_ADDR_INC_ENABLE[](#_CPPv4N14dma_addr_inc_t19DMA_ADDR_INC_ENABLEE "永久链接至目标")
    :   DMA enable addrress increase

enum dma_addr_loop_t[](#_CPPv415dma_addr_loop_t "永久链接至目标")
:   *Values:*

    enumerator DMA_ADDR_LOOP_DISABLE[](#_CPPv4N15dma_addr_loop_t21DMA_ADDR_LOOP_DISABLEE "永久链接至目标")
    :   DMA disable addrress loop

    enumerator DMA_ADDR_LOOP_ENABLE[](#_CPPv4N15dma_addr_loop_t20DMA_ADDR_LOOP_ENABLEE "永久链接至目标")
    :   DMA enable addrress loop

enum dma_sec_attr_t[](#_CPPv414dma_sec_attr_t "永久链接至目标")
:   *Values:*

    enumerator DMA_ATTR_NON_SEC[](#_CPPv4N14dma_sec_attr_t16DMA_ATTR_NON_SECE "永久链接至目标")
    :   DMA non-secure attr

    enumerator DMA_ATTR_SEC[](#_CPPv4N14dma_sec_attr_t12DMA_ATTR_SECE "永久链接至目标")
    :   DMA secure attr

enum dma_burst_len_t[](#_CPPv415dma_burst_len_t "永久链接至目标")
:   *Values:*

    enumerator BURST_LEN_SINGLE[](#_CPPv4N15dma_burst_len_t16BURST_LEN_SINGLEE "永久链接至目标")

    enumerator BURST_LEN_INC4[](#_CPPv4N15dma_burst_len_t14BURST_LEN_INC4E "永久链接至目标")

    enumerator BURST_LEN_INC8[](#_CPPv4N15dma_burst_len_t14BURST_LEN_INC8E "永久链接至目标")

    enumerator BURST_LEN_INC16[](#_CPPv4N15dma_burst_len_t15BURST_LEN_INC16E "永久链接至目标")

enum dma_pixel_trans_type_t[](#_CPPv422dma_pixel_trans_type_t "永久链接至目标")
:   *Values:*

    enumerator DMA_TRANS_DEFAULT[](#_CPPv4N22dma_pixel_trans_type_t17DMA_TRANS_DEFAULTE "永久链接至目标")
    :   DMA TRANS DEFAULT

    enumerator DMA_TRANS_RGB_TO_YUV[](#_CPPv4N22dma_pixel_trans_type_t20DMA_TRANS_RGB_TO_YUVE "永久链接至目标")
    :   DMA TRANS RGB_TO_YUV

    enumerator DMA_TRANS_YUV_TO_RGB[](#_CPPv4N22dma_pixel_trans_type_t20DMA_TRANS_YUV_TO_RGBE "永久链接至目标")
    :   DMA TRANS YUV_TO_RGB

    enumerator DMA_TRANS_MAX[](#_CPPv4N22dma_pixel_trans_type_t13DMA_TRANS_MAXE "永久链接至目标")

enum dma_id_t[](#_CPPv48dma_id_t "永久链接至目标")
:   *Values:*

    enumerator DMA_ID_0[](#_CPPv4N8dma_id_t8DMA_ID_0E "永久链接至目标")
    :   DMA channel 0

    enumerator DMA_ID_1[](#_CPPv4N8dma_id_t8DMA_ID_1E "永久链接至目标")
    :   DMA channel 1

    enumerator DMA_ID_2[](#_CPPv4N8dma_id_t8DMA_ID_2E "永久链接至目标")
    :   DMA channel 2

    enumerator DMA_ID_3[](#_CPPv4N8dma_id_t8DMA_ID_3E "永久链接至目标")
    :   DMA channel 3

    enumerator DMA_ID_4[](#_CPPv4N8dma_id_t8DMA_ID_4E "永久链接至目标")
    :   DMA channel 4

    enumerator DMA_ID_5[](#_CPPv4N8dma_id_t8DMA_ID_5E "永久链接至目标")
    :   DMA channel 5

    enumerator DMA_ID_6[](#_CPPv4N8dma_id_t8DMA_ID_6E "永久链接至目标")
    :   DMA channel 6

    enumerator DMA_ID_7[](#_CPPv4N8dma_id_t8DMA_ID_7E "永久链接至目标")
    :   DMA channel 7

    enumerator DMA_ID_8[](#_CPPv4N8dma_id_t8DMA_ID_8E "永久链接至目标")
    :   DMA channel 8

    enumerator DMA_ID_9[](#_CPPv4N8dma_id_t8DMA_ID_9E "永久链接至目标")
    :   DMA channel 9

    enumerator DMA_ID_10[](#_CPPv4N8dma_id_t9DMA_ID_10E "永久链接至目标")
    :   DMA channel 10

    enumerator DMA_ID_11[](#_CPPv4N8dma_id_t9DMA_ID_11E "永久链接至目标")
    :   DMA channel 11

    enumerator DMA_ID_12[](#_CPPv4N8dma_id_t9DMA_ID_12E "永久链接至目标")
    :   DMA channel 12

    enumerator DMA_ID_13[](#_CPPv4N8dma_id_t9DMA_ID_13E "永久链接至目标")
    :   DMA channel 13

    enumerator DMA_ID_14[](#_CPPv4N8dma_id_t9DMA_ID_14E "永久链接至目标")
    :   DMA channel 14

    enumerator DMA_ID_15[](#_CPPv4N8dma_id_t9DMA_ID_15E "永久链接至目标")
    :   DMA channel 15

    enumerator DMA_ID_MAX[](#_CPPv4N8dma_id_t10DMA_ID_MAXE "永久链接至目标")
    :   DMA channel max
