---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/bootrom/bootrom.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="boot-rom"></a>

# BOOT ROM

<a id="bootrom-api-brief"></a>

## BOOTROM API Brief

| Application | Brief |
| --- | --- |
| [`uart_dma_open()`](#_CPPv413uart_dma_open8uint32_t "uart_dma_open") | Open UART DMA |
| [`uart_dma_close()`](#_CPPv414uart_dma_close8uint32_t "uart_dma_close") | Close UART DMA |
| [`dlp_dma_open()`](#_CPPv412dlp_dma_open8uint32_t "dlp_dma_open") | Open charging port communication (DLP) DMA |
| [`dlp_dma_close()`](#_CPPv413dlp_dma_close8uint32_t "dlp_dma_close") | Close charging port communication (DLP) DMA |

<a id="bootrom-api-reference"></a>

## BOOTROM API Reference

<a id="header-file"></a>

### Header File

- [bootrom/bootrom.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bootrom/bootrom.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413uart_dma_open8uint32_t"></a>

<a id="_CPPv313uart_dma_open8uint32_t"></a> <a id="_CPPv213uart_dma_open8uint32_t"></a> <a id="uart_dma_open__uint32_t"></a> <a id="bootrom_8h_1aae220eda6eb3611164c52b531fc98fce"></a> int32\_t uart\_dma\_open(uint32\_t dev\_index)
:   Open UART DMA.

    Set up the UART device indicated by dev\_index and configure the RX DMA to get ready for incoming UART data transmissions.

    参数:
    :   **dev\_index** – **\[in\]** UART device index, from 0(the first device)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414uart_dma_close8uint32_t"></a>

<a id="_CPPv314uart_dma_close8uint32_t"></a> <a id="_CPPv214uart_dma_close8uint32_t"></a> <a id="uart_dma_close__uint32_t"></a> <a id="bootrom_8h_1a7cc4e30816a6e9c7122e34b693b60d50"></a> int32\_t uart\_dma\_close(uint32\_t dev\_index)
:   Close UART DMA.

    Deactivate the UART device specified by dev\_index and release the RX DMA to halt the reception of incoming UART data transmissions.

    参数:
    :   **dev\_index** – **\[in\]** UART device index, from 0(the first device)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412dlp_dma_open8uint32_t"></a>

<a id="_CPPv312dlp_dma_open8uint32_t"></a> <a id="_CPPv212dlp_dma_open8uint32_t"></a> <a id="dlp_dma_open__uint32_t"></a> <a id="bootrom_8h_1acce4084362d3583846f1c2d5f32f6064"></a> int32\_t dlp\_dma\_open(uint32\_t dev\_index)
:   Open charging port communication (DLP) DMA.

    Set up the DLP device indicated by dev\_index and configure the RX DMA to get ready for incoming DLP data transmissions.

    参数:
    :   **dev\_index** – **\[in\]** DLP device index, from 0(the first device)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413dlp_dma_close8uint32_t"></a>

<a id="_CPPv313dlp_dma_close8uint32_t"></a> <a id="_CPPv213dlp_dma_close8uint32_t"></a> <a id="dlp_dma_close__uint32_t"></a> <a id="bootrom_8h_1aeb0275c40714911b9fe0730bf31cfe53"></a> int32\_t dlp\_dma\_close(uint32\_t dev\_index)
:   Close charging port communication (DLP) DMA.

    Deactivate the DLP device specified by dev\_index and release the RX DMA to halt the reception of incoming DLP data transmissions.

    参数:
    :   **dev\_index** – **\[in\]** DLP device index, from 0(the first device)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail **BOOTROM\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv410_hci_cmd_t"></a>

<a id="_CPPv310_hci_cmd_t"></a> <a id="_CPPv210_hci_cmd_t"></a> <a id="_hci_cmd_t"></a> <a id="struct__hci__cmd__t"></a> struct \_hci\_cmd\_t
:   HCI command struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10_hci_cmd_t4typeE"></a>

    <a id="_CPPv3N10_hci_cmd_t4typeE"></a> <a id="_CPPv2N10_hci_cmd_t4typeE"></a> <a id="_hci_cmd_t::type__uint8_t"></a> <a id="struct__hci__cmd__t_1a9e2d76f5013d34b88b2811a705ba1502"></a> uint8\_t type
    :   command packet type, always equal 0x01

    <a id="_CPPv4N10_hci_cmd_t6opcodeE"></a>

    <a id="_CPPv3N10_hci_cmd_t6opcodeE"></a> <a id="_CPPv2N10_hci_cmd_t6opcodeE"></a> <a id="_hci_cmd_t::opcode__uint16_t"></a> <a id="struct__hci__cmd__t_1aa0e9aeccf4465573f739fbe7b2532eeb"></a> uint16\_t opcode
    :   vendor opcode, always equal 0xfce0

    <a id="_CPPv4N10_hci_cmd_t3lenE"></a>

    <a id="_CPPv3N10_hci_cmd_t3lenE"></a> <a id="_CPPv2N10_hci_cmd_t3lenE"></a> <a id="_hci_cmd_t::len__uint8_t"></a> <a id="struct__hci__cmd__t_1a7042bcb2bf60963e9098cb9993a24196"></a> uint8\_t len
    :   parameter length, include cmd \& param

    <a id="_CPPv4N10_hci_cmd_t3cmdE"></a>

    <a id="_CPPv3N10_hci_cmd_t3cmdE"></a> <a id="_CPPv2N10_hci_cmd_t3cmdE"></a> <a id="_hci_cmd_t::cmd__uint8_t"></a> <a id="struct__hci__cmd__t_1a812bcfba95e6c2cd62f4051265d7d6d5"></a> uint8\_t cmd
    :   command

    <a id="_CPPv4N10_hci_cmd_t5paramE"></a>

    <a id="_CPPv3N10_hci_cmd_t5paramE"></a> <a id="_CPPv2N10_hci_cmd_t5paramE"></a> <a id="_hci_cmd_t::param__uint8_tA"></a> <a id="struct__hci__cmd__t_1a2d25fab959966ad4d98329420cb80a9c"></a> uint8\_t param\[0\]
    :   parameters

<a id="_CPPv416_hci_cmd_flash_t"></a>

<a id="_CPPv316_hci_cmd_flash_t"></a> <a id="_CPPv216_hci_cmd_flash_t"></a> <a id="_hci_cmd_flash_t"></a> <a id="struct__hci__cmd__flash__t"></a> struct \_hci\_cmd\_flash\_t
:   HCI flash command struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16_hci_cmd_flash_t4typeE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t4typeE"></a> <a id="_CPPv2N16_hci_cmd_flash_t4typeE"></a> <a id="_hci_cmd_flash_t::type__uint8_t"></a> <a id="struct__hci__cmd__flash__t_1a5f6152e2c8f63d9210b6c5046b271f5d"></a> uint8\_t type
    :   command packet type, always equal 0x01

    <a id="_CPPv4N16_hci_cmd_flash_t6opcodeE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t6opcodeE"></a> <a id="_CPPv2N16_hci_cmd_flash_t6opcodeE"></a> <a id="_hci_cmd_flash_t::opcode__uint16_t"></a> <a id="struct__hci__cmd__flash__t_1a46c213a3092e0cebe7a271789823cb96"></a> uint16\_t opcode
    :   vendor opcode, always equal 0xfce0

    <a id="_CPPv4N16_hci_cmd_flash_t3lenE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t3lenE"></a> <a id="_CPPv2N16_hci_cmd_flash_t3lenE"></a> <a id="_hci_cmd_flash_t::len__uint8_t"></a> <a id="struct__hci__cmd__flash__t_1a583fa1d66df75cdb7f48a2cb4c211b57"></a> uint8\_t len
    :   parameter length, always equal 0xff

    <a id="_CPPv4N16_hci_cmd_flash_t3cmdE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t3cmdE"></a> <a id="_CPPv2N16_hci_cmd_flash_t3cmdE"></a> <a id="_hci_cmd_flash_t::cmd__uint8_t"></a> <a id="struct__hci__cmd__flash__t_1a747b63ac9ecd6399e9221fdfc250edc1"></a> uint8\_t cmd
    :   flash operation, always equal 0xf4

    <a id="_CPPv4N16_hci_cmd_flash_t4flenE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t4flenE"></a> <a id="_CPPv2N16_hci_cmd_flash_t4flenE"></a> <a id="_hci_cmd_flash_t::flen__uint16_t"></a> <a id="struct__hci__cmd__flash__t_1a5b27a54c079b210b2bbb6d576f1427d0"></a> uint16\_t flen
    :   flash operation parameter length, include fcmd \& param

    <a id="_CPPv4N16_hci_cmd_flash_t4fcmdE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t4fcmdE"></a> <a id="_CPPv2N16_hci_cmd_flash_t4fcmdE"></a> <a id="_hci_cmd_flash_t::fcmd__uint8_t"></a> <a id="struct__hci__cmd__flash__t_1a422de5765091979988f37e415c0f8427"></a> uint8\_t fcmd
    :   flash operation command

    <a id="_CPPv4N16_hci_cmd_flash_t5paramE"></a>

    <a id="_CPPv3N16_hci_cmd_flash_t5paramE"></a> <a id="_CPPv2N16_hci_cmd_flash_t5paramE"></a> <a id="_hci_cmd_flash_t::param__uint8_tA"></a> <a id="struct__hci__cmd__flash__t_1ac45764f075f7bb2063f7cd05549fd72e"></a> uint8\_t param\[0\]
    :   parameters

<a id="_CPPv410_hci_evt_t"></a>

<a id="_CPPv310_hci_evt_t"></a> <a id="_CPPv210_hci_evt_t"></a> <a id="_hci_evt_t"></a> <a id="struct__hci__evt__t"></a> struct \_hci\_evt\_t
:   HCI event struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10_hci_evt_t4typeE"></a>

    <a id="_CPPv3N10_hci_evt_t4typeE"></a> <a id="_CPPv2N10_hci_evt_t4typeE"></a> <a id="_hci_evt_t::type__uint8_t"></a> <a id="struct__hci__evt__t_1ac39061581e3edee735079a88ddf6fa7d"></a> uint8\_t type
    :   event packet type, always equal 0x04

    <a id="_CPPv4N10_hci_evt_t3evtE"></a>

    <a id="_CPPv3N10_hci_evt_t3evtE"></a> <a id="_CPPv2N10_hci_evt_t3evtE"></a> <a id="_hci_evt_t::evt__uint8_t"></a> <a id="struct__hci__evt__t_1a1a4be6be654745b1c079cc0d770a7164"></a> uint8\_t evt
    :   command complete event code, always equal 0x0e

    <a id="_CPPv4N10_hci_evt_t3lenE"></a>

    <a id="_CPPv3N10_hci_evt_t3lenE"></a> <a id="_CPPv2N10_hci_evt_t3lenE"></a> <a id="_hci_evt_t::len__uint8_t"></a> <a id="struct__hci__evt__t_1a2f0349adcd6ac256da8667d9be3851b9"></a> uint8\_t len
    :   parameter length

    <a id="_CPPv4N10_hci_evt_t7rx_typeE"></a>

    <a id="_CPPv3N10_hci_evt_t7rx_typeE"></a> <a id="_CPPv2N10_hci_evt_t7rx_typeE"></a> <a id="_hci_evt_t::rx_type__uint8_t"></a> <a id="struct__hci__evt__t_1a45f4b5e8d2e06da773ae935488001f7d"></a> uint8\_t rx\_type
    :   rx command packet type, always equal 0x01

    <a id="_CPPv4N10_hci_evt_t6opcodeE"></a>

    <a id="_CPPv3N10_hci_evt_t6opcodeE"></a> <a id="_CPPv2N10_hci_evt_t6opcodeE"></a> <a id="_hci_evt_t::opcode__uint16_t"></a> <a id="struct__hci__evt__t_1afa7b85513c6ec16389f3711b25248098"></a> uint16\_t opcode
    :   rx vendor opcode, always equal 0xfce0

    <a id="_CPPv4N10_hci_evt_t3cmdE"></a>

    <a id="_CPPv3N10_hci_evt_t3cmdE"></a> <a id="_CPPv2N10_hci_evt_t3cmdE"></a> <a id="_hci_evt_t::cmd__uint8_t"></a> <a id="struct__hci__evt__t_1aa6fbb5bf5684fd915c33d3b3486d51ef"></a> uint8\_t cmd
    :   command

    <a id="_CPPv4N10_hci_evt_t5paramE"></a>

    <a id="_CPPv3N10_hci_evt_t5paramE"></a> <a id="_CPPv2N10_hci_evt_t5paramE"></a> <a id="_hci_evt_t::param__uint8_tA"></a> <a id="struct__hci__evt__t_1a99a6d96286caae1ecf919350f1ed8c66"></a> uint8\_t param\[0\]
    :   parameters

<a id="_CPPv416_hci_evt_flash_t"></a>

<a id="_CPPv316_hci_evt_flash_t"></a> <a id="_CPPv216_hci_evt_flash_t"></a> <a id="_hci_evt_flash_t"></a> <a id="struct__hci__evt__flash__t"></a> struct \_hci\_evt\_flash\_t
:   HCI flash event struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16_hci_evt_flash_t4typeE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t4typeE"></a> <a id="_CPPv2N16_hci_evt_flash_t4typeE"></a> <a id="_hci_evt_flash_t::type__uint8_t"></a> <a id="struct__hci__evt__flash__t_1aaf1af08270cc3117e428f1cff4747de2"></a> uint8\_t type
    :   event packet type, always equal 0x04

    <a id="_CPPv4N16_hci_evt_flash_t3evtE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t3evtE"></a> <a id="_CPPv2N16_hci_evt_flash_t3evtE"></a> <a id="_hci_evt_flash_t::evt__uint8_t"></a> <a id="struct__hci__evt__flash__t_1aace4862c55246ff96c25c9f7b72484c0"></a> uint8\_t evt
    :   command complete event code, always equal 0x0e

    <a id="_CPPv4N16_hci_evt_flash_t3lenE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t3lenE"></a> <a id="_CPPv2N16_hci_evt_flash_t3lenE"></a> <a id="_hci_evt_flash_t::len__uint8_t"></a> <a id="struct__hci__evt__flash__t_1a34f6e535c0b7ba0a1ed160cccd51e2eb"></a> uint8\_t len
    :   parameter length, always equal 0xff

    <a id="_CPPv4N16_hci_evt_flash_t7rx_typeE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t7rx_typeE"></a> <a id="_CPPv2N16_hci_evt_flash_t7rx_typeE"></a> <a id="_hci_evt_flash_t::rx_type__uint8_t"></a> <a id="struct__hci__evt__flash__t_1a45bd4e63cd0c089f6fa40e9885b84d54"></a> uint8\_t rx\_type
    :   rx command packet type, always equal 0x01

    <a id="_CPPv4N16_hci_evt_flash_t6opcodeE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t6opcodeE"></a> <a id="_CPPv2N16_hci_evt_flash_t6opcodeE"></a> <a id="_hci_evt_flash_t::opcode__uint16_t"></a> <a id="struct__hci__evt__flash__t_1a55d6b81e81aaf37d44f4b2a72869fb78"></a> uint16\_t opcode
    :   rx vendor opcode, always equal 0xfce0

    <a id="_CPPv4N16_hci_evt_flash_t3cmdE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t3cmdE"></a> <a id="_CPPv2N16_hci_evt_flash_t3cmdE"></a> <a id="_hci_evt_flash_t::cmd__uint8_t"></a> <a id="struct__hci__evt__flash__t_1a94e11137e99fde8fc6e7c4e26caf64f9"></a> uint8\_t cmd
    :   flash operation, always equal 0xf4

    <a id="_CPPv4N16_hci_evt_flash_t4flenE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t4flenE"></a> <a id="_CPPv2N16_hci_evt_flash_t4flenE"></a> <a id="_hci_evt_flash_t::flen__uint16_t"></a> <a id="struct__hci__evt__flash__t_1ad1dcce9ae1c6c609ed1fa46f30c480e1"></a> uint16\_t flen
    :   flash operation parameter length, include fcmd \& param

    <a id="_CPPv4N16_hci_evt_flash_t4fcmdE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t4fcmdE"></a> <a id="_CPPv2N16_hci_evt_flash_t4fcmdE"></a> <a id="_hci_evt_flash_t::fcmd__uint8_t"></a> <a id="struct__hci__evt__flash__t_1a4e060eed3f0df5e170346ca4384daeef"></a> uint8\_t fcmd
    :   flash operation command

    <a id="_CPPv4N16_hci_evt_flash_t5paramE"></a>

    <a id="_CPPv3N16_hci_evt_flash_t5paramE"></a> <a id="_CPPv2N16_hci_evt_flash_t5paramE"></a> <a id="_hci_evt_flash_t::param__uint8_tA"></a> <a id="struct__hci__evt__flash__t_1ab188ad3db9af99c22433ff61c3bbec95"></a> uint8\_t param\[0\]
    :   parameters

<a id="macros"></a>

### Macros

<a id="c.BR_LOG_INIT"></a>

<a id="bootrom_8h_1a9535ebabe2f2b615b1e799e6bfefd4da"></a> BR\_LOG\_INIT()

<a id="c.BR_LOG_DEINIT"></a>

<a id="bootrom_8h_1ac0f7692463e7bc87e3496a557d937ad7"></a> BR\_LOG\_DEINIT()

<a id="c.BR_LOG"></a>

<a id="bootrom_8h_1a1d57540c410cc8ea8c40cf3ad261dc90"></a> BR\_LOG(format, ...)

<a id="c.BR_DUMP"></a>

<a id="bootrom_8h_1a1454c0a22966ae0d71982dc367f6460f"></a> BR\_DUMP(format, ...)

<a id="c.BR_ASSERT"></a>

<a id="bootrom_8h_1a2612957f01429a4d8f8298c207cb3b82"></a> BR\_ASSERT(exp)

<a id="c.BR_LOG_DISPATCH"></a>

<a id="bootrom_8h_1a80e0ca2a03502f0fa00ba44c18378467"></a> BR\_LOG\_DISPATCH()

<a id="c.SPI_FLASH_CMD_read_status_reg"></a>

<a id="bootrom_8h_1ab98f5ec7dd3056b38180ebb3bc9589fe"></a> SPI\_FLASH\_CMD\_read\_status\_reg
:   Definition of SPI Flash commands.

<a id="c.SPI_FLASH_CMD_read_status1_reg"></a>

<a id="bootrom_8h_1ab464beb3abf68e60164fb0a9c811dde0"></a> SPI\_FLASH\_CMD\_read\_status1\_reg

<a id="c.SPI_FLASH_CMD_write_status_reg"></a>

<a id="bootrom_8h_1aaca187529e3829062cf7e432a105c880"></a> SPI\_FLASH\_CMD\_write\_status\_reg

<a id="c.SPI_FLASH_CMD_read_id"></a>

<a id="bootrom_8h_1af65edf199bab66d9b46b259862afacf4"></a> SPI\_FLASH\_CMD\_read\_id

<a id="c.SPI_FLASH_CMD_write_enable"></a>

<a id="bootrom_8h_1ab2ad7370954615a5c4442637378e2e1a"></a> SPI\_FLASH\_CMD\_write\_enable

<a id="c.SPI_FLASH_CMD_write_disable"></a>

<a id="bootrom_8h_1ac36120f95c945d62a58189224d81f8cf"></a> SPI\_FLASH\_CMD\_write\_disable

<a id="c.SPI_FLASH_CMD_read_data"></a>

<a id="bootrom_8h_1a5a2375a8ab60fc2773139720cb855119"></a> SPI\_FLASH\_CMD\_read\_data

<a id="c.SPI_FLASH_CMD_page_program"></a>

<a id="bootrom_8h_1a8ae0e7cfa8e2766f8dbb57c20304be79"></a> SPI\_FLASH\_CMD\_page\_program

<a id="c.SPI_FLASH_CMD_sector_erase"></a>

<a id="bootrom_8h_1a8612d6bdada865c6f2095a0f410f2e2a"></a> SPI\_FLASH\_CMD\_sector\_erase

<a id="c.SPI_FLASH_CMD_chip_erase"></a>

<a id="bootrom_8h_1a8be6fb7be1a581f9bcb51bfb89ad43cd"></a> SPI\_FLASH\_CMD\_chip\_erase

<a id="c.SPI_FLASH_CMD_blk_erase_32k"></a>

<a id="bootrom_8h_1aa166cf15afebe1db974ac0405cced4bf"></a> SPI\_FLASH\_CMD\_blk\_erase\_32k

<a id="c.SPI_FLASH_CMD_blk_erase_64k"></a>

<a id="bootrom_8h_1a7c77b27f7e075a681a6d1e032bdaf3c2"></a> SPI\_FLASH\_CMD\_blk\_erase\_64k

<a id="c.SPI_FLASH_STATUS_WIP_BIT"></a>

<a id="bootrom_8h_1abd20dbd52a91e430e27fb1efef476d7d"></a> SPI\_FLASH\_STATUS\_WIP\_BIT
:   Definition of SPI Flash status.

<a id="c.SPI_FLASH_STATUS_WEL_BIT"></a>

<a id="bootrom_8h_1a943fa10b948f2f9bf75f30211c74690c"></a> SPI\_FLASH\_STATUS\_WEL\_BIT

<a id="c.SPI_FLASH_STATUS_BUSY_MASK"></a>

<a id="bootrom_8h_1aa5f900772b2312ae9aeb45dcdc8d5824"></a> SPI\_FLASH\_STATUS\_BUSY\_MASK

<a id="c.SPI_FLASH_PAGE_SIZE"></a>

<a id="bootrom_8h_1a1ac80cb523124b7248207622730c0623"></a> SPI\_FLASH\_PAGE\_SIZE
:   Definition of SPI Flash page size.

<a id="c.SPI_FLASH_PAGE_MASK"></a>

<a id="bootrom_8h_1a4f8476527eff51a771e9c1bd4addbb68"></a> SPI\_FLASH\_PAGE\_MASK

<a id="c.SPI_TX_LEN_PREFIX_FOR_RX"></a>

<a id="bootrom_8h_1a7b4601954b37d67c8e85a348f2281554"></a> SPI\_TX\_LEN\_PREFIX\_FOR\_RX

<a id="c.SPI_FLASH_SECTOR_SIZE"></a>

<a id="bootrom_8h_1a00924a8ba223b2ca0e7031259b292c84"></a> SPI\_FLASH\_SECTOR\_SIZE
:   Definition of SPI Flash sector size.

    0x1000 4k

<a id="c.SPI_FLASH_SECTOR_MASK"></a>

<a id="bootrom_8h_1abffe66d6fd0dc20339b3cec1c5e8e2b4"></a> SPI\_FLASH\_SECTOR\_MASK

<a id="c.MAX_PURE_DATA_SIZE"></a>

<a id="bootrom_8h_1ab998ff4fdb4b602a8472195a4201590a"></a> MAX\_PURE\_DATA\_SIZE

<a id="c.MAX_DATA_BUF_SIZE"></a>

<a id="bootrom_8h_1af9ea4bbdbe31651d02ca44e4eb436dd1"></a> MAX\_DATA\_BUF\_SIZE

<a id="c.VALID_VENDOR_OPCODE"></a>

<a id="bootrom_8h_1ad206391533137c2b69252dc6ef43113e"></a> VALID\_VENDOR\_OPCODE
:   Definition of vendor opcode.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv49hci_cmd_t"></a>

<a id="_CPPv39hci_cmd_t"></a> <a id="_CPPv29hci_cmd_t"></a> <a id="hci_cmd_t"></a> <a id="bootrom_8h_1a2e0545a246dcd328c6f56a60b918a949"></a> typedef struct [\_hci\_cmd\_t](#_CPPv410_hci_cmd_t "_hci_cmd_t") hci\_cmd\_t
:   HCI command struct definition.

<a id="_CPPv415hci_cmd_flash_t"></a>

<a id="_CPPv315hci_cmd_flash_t"></a> <a id="_CPPv215hci_cmd_flash_t"></a> <a id="hci_cmd_flash_t"></a> <a id="bootrom_8h_1a7a20d03c12a1169f26b730852cb0e88f"></a> typedef struct [\_hci\_cmd\_flash\_t](#_CPPv416_hci_cmd_flash_t "_hci_cmd_flash_t") hci\_cmd\_flash\_t
:   HCI flash command struct definition.

<a id="_CPPv49hci_evt_t"></a>

<a id="_CPPv39hci_evt_t"></a> <a id="_CPPv29hci_evt_t"></a> <a id="hci_evt_t"></a> <a id="bootrom_8h_1a795487e22f489916d756c77dc5e1375d"></a> typedef struct [\_hci\_evt\_t](#_CPPv410_hci_evt_t "_hci_evt_t") hci\_evt\_t
:   HCI event struct definition.

<a id="_CPPv415hci_evt_flash_t"></a>

<a id="_CPPv315hci_evt_flash_t"></a> <a id="_CPPv215hci_evt_flash_t"></a> <a id="hci_evt_flash_t"></a> <a id="bootrom_8h_1a5d08790a7866c3455092a3750475bb1d"></a> typedef struct [\_hci\_evt\_flash\_t](#_CPPv416_hci_evt_flash_t "_hci_evt_flash_t") hci\_evt\_flash\_t
:   HCI flash event struct definition.

<a id="_CPPv47bkcmd_e"></a>

<a id="_CPPv37bkcmd_e"></a> <a id="_CPPv27bkcmd_e"></a> <a id="bkcmd_e"></a> <a id="bootrom_8h_1a61f216d74d615f0469997298e34cff71"></a> typedef enum [\_bkcmd\_e](#_CPPv48_bkcmd_e "_bkcmd_e") bkcmd\_e
:   vendor opcode command definition.

<a id="_CPPv413bkcmd_flash_e"></a>

<a id="_CPPv313bkcmd_flash_e"></a> <a id="_CPPv213bkcmd_flash_e"></a> <a id="bkcmd_flash_e"></a> <a id="bootrom_8h_1afd434519876726db44985f33819a2a82"></a> typedef enum [\_bkcmd\_flash\_e](#_CPPv414_bkcmd_flash_e "_bkcmd_flash_e") bkcmd\_flash\_e
:   Beken flash operation command definition.

<a id="_CPPv411evt_state_e"></a>

<a id="_CPPv311evt_state_e"></a> <a id="_CPPv211evt_state_e"></a> <a id="evt_state_e"></a> <a id="bootrom_8h_1aa8d2f67f98fd42d3bf2e49e561556cbf"></a> typedef enum [\_evt\_state\_e](#_CPPv412_evt_state_e "_evt_state_e") evt\_state\_e
:   vendor event state definition.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv48_bkcmd_e"></a>

<a id="_CPPv38_bkcmd_e"></a> <a id="_CPPv28_bkcmd_e"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575"></a> enum \_bkcmd\_e
:   vendor opcode command definition.

    *Values:*

    <a id="_CPPv4N8_bkcmd_e14LINK_CHECK_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e14LINK_CHECK_CMDE"></a> <a id="_CPPv2N8_bkcmd_e14LINK_CHECK_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a5d7159951cca4929b8636a6f73a6b988"></a> enumerator LINK\_CHECK\_CMD
    :   return 0x04 0x0e 0x04 0x01 0xe0 0xfc 0x00

    <a id="_CPPv4N8_bkcmd_e18REGISTER_WRITE_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e18REGISTER_WRITE_CMDE"></a> <a id="_CPPv2N8_bkcmd_e18REGISTER_WRITE_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575aa1ca56768932b65a890fbfb6faabef1a"></a> enumerator REGISTER\_WRITE\_CMD
    :   write certain reg

    <a id="_CPPv4N8_bkcmd_e17REGISTER_READ_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e17REGISTER_READ_CMDE"></a> <a id="_CPPv2N8_bkcmd_e17REGISTER_READ_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a33f6ad7d8d805283b8949432b29d6d98"></a> enumerator REGISTER\_READ\_CMD
    :   read certain reg value

    <a id="_CPPv4N8_bkcmd_e15CMD_ERROR_EVENTE"></a>

    <a id="_CPPv3N8_bkcmd_e15CMD_ERROR_EVENTE"></a> <a id="_CPPv2N8_bkcmd_e15CMD_ERROR_EVENTE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a8b815f5feca205d32631cd3dc6deb62e"></a> enumerator CMD\_ERROR\_EVENT

    <a id="_CPPv4N8_bkcmd_e14SYS_REBOOT_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e14SYS_REBOOT_CMDE"></a> <a id="_CPPv2N8_bkcmd_e14SYS_REBOOT_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a42c147dfd8e15879800655c0191abfd5"></a> enumerator SYS\_REBOOT\_CMD
    :   download form bootrom ok, drop ota

    <a id="_CPPv4N8_bkcmd_e24CHANGE_UART_SAMPRATE_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e24CHANGE_UART_SAMPRATE_CMDE"></a> <a id="_CPPv2N8_bkcmd_e24CHANGE_UART_SAMPRATE_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575ae82d2e69f880f035652529de7812f286"></a> enumerator CHANGE\_UART\_SAMPRATE\_CMD
    :   change UART samplerate

    <a id="_CPPv4N8_bkcmd_e21FLASH_IMAGE_CEC_CHECKE"></a>

    <a id="_CPPv3N8_bkcmd_e21FLASH_IMAGE_CEC_CHECKE"></a> <a id="_CPPv2N8_bkcmd_e21FLASH_IMAGE_CEC_CHECKE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575ad0878a0a28b3d9b6a5566d5ddf51e3fe"></a> enumerator FLASH\_IMAGE\_CEC\_CHECK
    :   flash image CEC check

    <a id="_CPPv4N8_bkcmd_e13SYS_RESET_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e13SYS_RESET_CMDE"></a> <a id="_CPPv2N8_bkcmd_e13SYS_RESET_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a3e9fdf45bf0f7060d9a569884a7f0c58"></a> enumerator SYS\_RESET\_CMD
    :   reboot by watch dog Bluetooth Tx/Rx Test

    <a id="_CPPv4N8_bkcmd_e10TX_PN9_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e10TX_PN9_CMDE"></a> <a id="_CPPv2N8_bkcmd_e10TX_PN9_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a64dc9380fa93410553e33437ad4fb64d"></a> enumerator TX\_PN9\_CMD

    <a id="_CPPv4N8_bkcmd_e10RX_PN9_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e10RX_PN9_CMDE"></a> <a id="_CPPv2N8_bkcmd_e10RX_PN9_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575abe8f90a268aa9039ba79c170039641bc"></a> enumerator RX\_PN9\_CMD

    <a id="_CPPv4N8_bkcmd_e16CEVA_BR_SEND_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e16CEVA_BR_SEND_CMDE"></a> <a id="_CPPv2N8_bkcmd_e16CEVA_BR_SEND_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575abd372bc6d8539259fbe9f7e11e8f070b"></a> enumerator CEVA\_BR\_SEND\_CMD

    <a id="_CPPv4N8_bkcmd_e16CEVA_BR_RECV_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e16CEVA_BR_RECV_CMDE"></a> <a id="_CPPv2N8_bkcmd_e16CEVA_BR_RECV_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575af2ccaa345e0bfcd3ca0c5406495410e1"></a> enumerator CEVA\_BR\_RECV\_CMD

    <a id="_CPPv4N8_bkcmd_e18BLE_ADVERTISER_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e18BLE_ADVERTISER_CMDE"></a> <a id="_CPPv2N8_bkcmd_e18BLE_ADVERTISER_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a8a5a0014f77489bf31732913bcc1148e"></a> enumerator BLE\_ADVERTISER\_CMD

    <a id="_CPPv4N8_bkcmd_e17CEVA_FHS_SEND_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e17CEVA_FHS_SEND_CMDE"></a> <a id="_CPPv2N8_bkcmd_e17CEVA_FHS_SEND_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a5119a2f09afce3bd634d0539ef0718bc"></a> enumerator CEVA\_FHS\_SEND\_CMD

    <a id="_CPPv4N8_bkcmd_e18FALSH_STAY_ROM_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e18FALSH_STAY_ROM_CMDE"></a> <a id="_CPPv2N8_bkcmd_e18FALSH_STAY_ROM_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a4f90f018e6987d4c3418414d99841f84"></a> enumerator FALSH\_STAY\_ROM\_CMD
    :   Beken Digital Test

    <a id="_CPPv4N8_bkcmd_e16TEST_CMD_CHIP_IDE"></a>

    <a id="_CPPv3N8_bkcmd_e16TEST_CMD_CHIP_IDE"></a> <a id="_CPPv2N8_bkcmd_e16TEST_CMD_CHIP_IDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a6463889e7953cb5f1ffa9202f3d8987a"></a> enumerator TEST\_CMD\_CHIP\_ID

    <a id="_CPPv4N8_bkcmd_e16TEST_CMD_RF_TXRXE"></a>

    <a id="_CPPv3N8_bkcmd_e16TEST_CMD_RF_TXRXE"></a> <a id="_CPPv2N8_bkcmd_e16TEST_CMD_RF_TXRXE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575aa325789b50feabc3d476be46980db489"></a> enumerator TEST\_CMD\_RF\_TXRX

    <a id="_CPPv4N8_bkcmd_e18TEST_CMD_DEEPSLEEPE"></a>

    <a id="_CPPv3N8_bkcmd_e18TEST_CMD_DEEPSLEEPE"></a> <a id="_CPPv2N8_bkcmd_e18TEST_CMD_DEEPSLEEPE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a699d9c7769ef9fbcc6dc8a0ad254dc91"></a> enumerator TEST\_CMD\_DEEPSLEEP

    <a id="_CPPv4N8_bkcmd_e21TEST_CMD_SUBDEEPSLEEPE"></a>

    <a id="_CPPv3N8_bkcmd_e21TEST_CMD_SUBDEEPSLEEPE"></a> <a id="_CPPv2N8_bkcmd_e21TEST_CMD_SUBDEEPSLEEPE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575afec257e4c4e298536114b5268c1f2c10"></a> enumerator TEST\_CMD\_SUBDEEPSLEEP

    <a id="_CPPv4N8_bkcmd_e19TEST_CMD_DIGITAL_OPE"></a>

    <a id="_CPPv3N8_bkcmd_e19TEST_CMD_DIGITAL_OPE"></a> <a id="_CPPv2N8_bkcmd_e19TEST_CMD_DIGITAL_OPE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a2473f05d90bcaba6e443711bfa01f250"></a> enumerator TEST\_CMD\_DIGITAL\_OP

    <a id="_CPPv4N8_bkcmd_e14TEST_CMD_DMIPSE"></a>

    <a id="_CPPv3N8_bkcmd_e14TEST_CMD_DMIPSE"></a> <a id="_CPPv2N8_bkcmd_e14TEST_CMD_DMIPSE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575ac123092122f99a46870a4fa6b9c2162a"></a> enumerator TEST\_CMD\_DMIPS

    <a id="_CPPv4N8_bkcmd_e16TEST_CMD_BR_TXRXE"></a>

    <a id="_CPPv3N8_bkcmd_e16TEST_CMD_BR_TXRXE"></a> <a id="_CPPv2N8_bkcmd_e16TEST_CMD_BR_TXRXE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a4aff782a907c3433c3829c353cefda02"></a> enumerator TEST\_CMD\_BR\_TXRX

    <a id="_CPPv4N8_bkcmd_e16TEST_CMD_LE_TXRXE"></a>

    <a id="_CPPv3N8_bkcmd_e16TEST_CMD_LE_TXRXE"></a> <a id="_CPPv2N8_bkcmd_e16TEST_CMD_LE_TXRXE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a3e16ad8bd9c6a1c8fd8b371cc8677009"></a> enumerator TEST\_CMD\_LE\_TXRX

    <a id="_CPPv4N8_bkcmd_e18TEST_CMD_BK24_TXRXE"></a>

    <a id="_CPPv3N8_bkcmd_e18TEST_CMD_BK24_TXRXE"></a> <a id="_CPPv2N8_bkcmd_e18TEST_CMD_BK24_TXRXE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a91b8de94cdb88ca8c11d4a8296ea282c"></a> enumerator TEST\_CMD\_BK24\_TXRX

    <a id="_CPPv4N8_bkcmd_e20TEST_CMD_LPO_BT_LINKE"></a>

    <a id="_CPPv3N8_bkcmd_e20TEST_CMD_LPO_BT_LINKE"></a> <a id="_CPPv2N8_bkcmd_e20TEST_CMD_LPO_BT_LINKE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a4f3a3811959c263678906eb31dc60fa1"></a> enumerator TEST\_CMD\_LPO\_BT\_LINK

    <a id="_CPPv4N8_bkcmd_e12TEST_CMD_ADCE"></a>

    <a id="_CPPv3N8_bkcmd_e12TEST_CMD_ADCE"></a> <a id="_CPPv2N8_bkcmd_e12TEST_CMD_ADCE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a2ad8f0aff5eb9ed8791c101799787724"></a> enumerator TEST\_CMD\_ADC

    <a id="_CPPv4N8_bkcmd_e17TEST_CMD_FLASH_OPE"></a>

    <a id="_CPPv3N8_bkcmd_e17TEST_CMD_FLASH_OPE"></a> <a id="_CPPv2N8_bkcmd_e17TEST_CMD_FLASH_OPE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a5200a6a9522cda7ab13db5283c451f0d"></a> enumerator TEST\_CMD\_FLASH\_OP

    <a id="_CPPv4N8_bkcmd_e12TEST_CMD_SPIE"></a>

    <a id="_CPPv3N8_bkcmd_e12TEST_CMD_SPIE"></a> <a id="_CPPv2N8_bkcmd_e12TEST_CMD_SPIE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a1b71801625dd20b4f97c8317e8d08663"></a> enumerator TEST\_CMD\_SPI

    <a id="_CPPv4N8_bkcmd_e12TEST_CMD_I2CE"></a>

    <a id="_CPPv3N8_bkcmd_e12TEST_CMD_I2CE"></a> <a id="_CPPv2N8_bkcmd_e12TEST_CMD_I2CE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575aa6aef101f4aa1eec42d5be125320aadf"></a> enumerator TEST\_CMD\_I2C

    <a id="_CPPv4N8_bkcmd_e12TEST_CMD_WDTE"></a>

    <a id="_CPPv3N8_bkcmd_e12TEST_CMD_WDTE"></a> <a id="_CPPv2N8_bkcmd_e12TEST_CMD_WDTE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a93d333dc0ab3e19dbc45ba1c3f9a28f7"></a> enumerator TEST\_CMD\_WDT

    <a id="_CPPv4N8_bkcmd_e12TEST_CMD_3DSE"></a>

    <a id="_CPPv3N8_bkcmd_e12TEST_CMD_3DSE"></a> <a id="_CPPv2N8_bkcmd_e12TEST_CMD_3DSE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575aeeb8c46f928d102fe80911170e3cfd02"></a> enumerator TEST\_CMD\_3DS

    <a id="_CPPv4N8_bkcmd_e13LOOP_MODE_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e13LOOP_MODE_CMDE"></a> <a id="_CPPv2N8_bkcmd_e13LOOP_MODE_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575af62be567ba3bd0b291c5594864b8d1c3"></a> enumerator LOOP\_MODE\_CMD

    <a id="_CPPv4N8_bkcmd_e13SYS_ERROR_RSPE"></a>

    <a id="_CPPv3N8_bkcmd_e13SYS_ERROR_RSPE"></a> <a id="_CPPv2N8_bkcmd_e13SYS_ERROR_RSPE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a32d4c733367d445c97fa186b41d087e1"></a> enumerator SYS\_ERROR\_RSP

    <a id="_CPPv4N8_bkcmd_e16SYS_UNDEFINE_INTE"></a>

    <a id="_CPPv3N8_bkcmd_e16SYS_UNDEFINE_INTE"></a> <a id="_CPPv2N8_bkcmd_e16SYS_UNDEFINE_INTE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575a18b91b9af2b33b9e6685186f78d5d3f2"></a> enumerator SYS\_UNDEFINE\_INT

    <a id="_CPPv4N8_bkcmd_e17FLASH_OPERATE_CMDE"></a>

    <a id="_CPPv3N8_bkcmd_e17FLASH_OPERATE_CMDE"></a> <a id="_CPPv2N8_bkcmd_e17FLASH_OPERATE_CMDE"></a> <a id="bootrom_8h_1a6d616d3c95f0accce71a6d17a645f575abc742925fa60a079c7acdaf3dfa87a68"></a> enumerator FLASH\_OPERATE\_CMD
    :   flash operation

<a id="_CPPv414_bkcmd_flash_e"></a>

<a id="_CPPv314_bkcmd_flash_e"></a> <a id="_CPPv214_bkcmd_flash_e"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1"></a> enum \_bkcmd\_flash\_e
:   Beken flash operation command definition.

    *Values:*

    <a id="_CPPv4N14_bkcmd_flash_e20FLASH_ADDR_WRITE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e20FLASH_ADDR_WRITE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e20FLASH_ADDR_WRITE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1acf2a8652b64f5ab444ff4464166843e6"></a> enumerator FLASH\_ADDR\_WRITE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e18FLASH_4K_WRITE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e18FLASH_4K_WRITE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e18FLASH_4K_WRITE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a682649888a0f66a408cee15706250d31"></a> enumerator FLASH\_4K\_WRITE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e19FLASH_ADDR_READ_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e19FLASH_ADDR_READ_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e19FLASH_ADDR_READ_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1adf7d7a8cb8ed7f14764e1f1a29677a7a"></a> enumerator FLASH\_ADDR\_READ\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e17FLASH_4K_READ_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e17FLASH_4K_READ_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e17FLASH_4K_READ_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1aab41f0b481f5caba3bb5e4dbea7d0591"></a> enumerator FLASH\_4K\_READ\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e21FLASH_CHIP_ERRASE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e21FLASH_CHIP_ERRASE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e21FLASH_CHIP_ERRASE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a86f2e0994f92a2ac6c79abb8ec55b8ce"></a> enumerator FLASH\_CHIP\_ERRASE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e19FLASH_4K_ERRASE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e19FLASH_4K_ERRASE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e19FLASH_4K_ERRASE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a9999d1cb3bd578fa8bd5f82fbbfcd235"></a> enumerator FLASH\_4K\_ERRASE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e17FLASH_SR_READ_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e17FLASH_SR_READ_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e17FLASH_SR_READ_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a7ea798cba7e55b7e55ded18456c2d2be"></a> enumerator FLASH\_SR\_READ\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e18FLASH_SR_WRITE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e18FLASH_SR_WRITE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e18FLASH_SR_WRITE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1acb668f918db9d8b83a95de7a7531121a"></a> enumerator FLASH\_SR\_WRITE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e16FLASH_SPI_OP_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e16FLASH_SPI_OP_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e16FLASH_SPI_OP_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a942de5ceaaec1b955be8d767aeae8872"></a> enumerator FLASH\_SPI\_OP\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e21FLASH_SIZE_ERRASE_CMDE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e21FLASH_SIZE_ERRASE_CMDE"></a> <a id="_CPPv2N14_bkcmd_flash_e21FLASH_SIZE_ERRASE_CMDE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a9205b9e3a5b2cae55ed5725ba48a59a0"></a> enumerator FLASH\_SIZE\_ERRASE\_CMD

    <a id="_CPPv4N14_bkcmd_flash_e22FLASH_JUMP_MEMORY_ADDRE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e22FLASH_JUMP_MEMORY_ADDRE"></a> <a id="_CPPv2N14_bkcmd_flash_e22FLASH_JUMP_MEMORY_ADDRE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1adf204be3a63af9dd7b8f9547b0099b69"></a> enumerator FLASH\_JUMP\_MEMORY\_ADDR
    :   for ram run

    <a id="_CPPv4N14_bkcmd_flash_e23FLASH_WRITE_MEMORY_DATAE"></a>

    <a id="_CPPv3N14_bkcmd_flash_e23FLASH_WRITE_MEMORY_DATAE"></a> <a id="_CPPv2N14_bkcmd_flash_e23FLASH_WRITE_MEMORY_DATAE"></a> <a id="bootrom_8h_1a445ebbbeb48e4e45625516029c2a5ef1a1ca5ca401a2f58f3e9035f3b2b0b1770"></a> enumerator FLASH\_WRITE\_MEMORY\_DATA
    :   for ram run

<a id="_CPPv412_evt_state_e"></a>

<a id="_CPPv312_evt_state_e"></a> <a id="_CPPv212_evt_state_e"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13b"></a> enum \_evt\_state\_e
:   vendor event state definition.

    *Values:*

    <a id="_CPPv4N12_evt_state_e9STATUS_OKE"></a>

    <a id="_CPPv3N12_evt_state_e9STATUS_OKE"></a> <a id="_CPPv2N12_evt_state_e9STATUS_OKE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba7e4a42e3b6dd63708c64cf3db6f69566"></a> enumerator STATUS\_OK

    <a id="_CPPv4N12_evt_state_e17FLASH_STATUS_BUSYE"></a>

    <a id="_CPPv3N12_evt_state_e17FLASH_STATUS_BUSYE"></a> <a id="_CPPv2N12_evt_state_e17FLASH_STATUS_BUSYE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba9f0e163a2cd4ec43acbe02344235882a"></a> enumerator FLASH\_STATUS\_BUSY

    <a id="_CPPv4N12_evt_state_e12SPI_OP_T_OUTE"></a>

    <a id="_CPPv3N12_evt_state_e12SPI_OP_T_OUTE"></a> <a id="_CPPv2N12_evt_state_e12SPI_OP_T_OUTE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13babe2c1463871d2c537ede459bac6e4abf"></a> enumerator SPI\_OP\_T\_OUT

    <a id="_CPPv4N12_evt_state_e14FLASH_OP_T_OUTE"></a>

    <a id="_CPPv3N12_evt_state_e14FLASH_OP_T_OUTE"></a> <a id="_CPPv2N12_evt_state_e14FLASH_OP_T_OUTE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba64898d190f99364ad6b66c56b58f034a"></a> enumerator FLASH\_OP\_T\_OUT

    <a id="_CPPv4N12_evt_state_e14PACK_LEN_ERRORE"></a>

    <a id="_CPPv3N12_evt_state_e14PACK_LEN_ERRORE"></a> <a id="_CPPv2N12_evt_state_e14PACK_LEN_ERRORE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba61a019d176c4b1816fdfc9893f088fdb"></a> enumerator PACK\_LEN\_ERROR

    <a id="_CPPv4N12_evt_state_e17PACK_PAYLOAD_LACKE"></a>

    <a id="_CPPv3N12_evt_state_e17PACK_PAYLOAD_LACKE"></a> <a id="_CPPv2N12_evt_state_e17PACK_PAYLOAD_LACKE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba4b1346b0c9b18aacce960e2ab1db1262"></a> enumerator PACK\_PAYLOAD\_LACK

    <a id="_CPPv4N12_evt_state_e11PARAM_ERRORE"></a>

    <a id="_CPPv3N12_evt_state_e11PARAM_ERRORE"></a> <a id="_CPPv2N12_evt_state_e11PARAM_ERRORE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13ba29b637a2d1deeee76888713aaf142a6c"></a> enumerator PARAM\_ERROR

    <a id="_CPPv4N12_evt_state_e10UNKNOW_CMDE"></a>

    <a id="_CPPv3N12_evt_state_e10UNKNOW_CMDE"></a> <a id="_CPPv2N12_evt_state_e10UNKNOW_CMDE"></a> <a id="bootrom_8h_1a1e9de28acf950a44a01df67e2675d13baa926a62d0acd85af9652751931ec7851"></a> enumerator UNKNOW\_CMD
