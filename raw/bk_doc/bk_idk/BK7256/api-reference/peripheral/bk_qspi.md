# QSPI[](#qspi "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_qspi.html "../../../../en/v1.5/api-reference/peripheral/bk_qspi.html")


## QSPI API Reference[](#qspi-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [qspi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_driver_init(void)[](#_CPPv419bk_qspi_driver_initv "永久链接至目标")
:   Init the QSPI driver.

    This API init the resoure common:


    - Init QSPI driver control memory


    **Attention**
    :   1. This API should be called before any other QSPI APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_driver_deinit(void)[](#_CPPv421bk_qspi_driver_deinitv "永久链接至目标")
:   Deinit the QSPI driver.

    This API free all resource related to QSPI and disable QSPI.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_init(const [qspi_config_t](#_CPPv413qspi_config_t "qspi_config_t") *config)[](#_CPPv412bk_qspi_initPK13qspi_config_t "永久链接至目标")
:   Init the QSPI.

    This API init the QSPI:


    - Power up the QSPI

    - Configure the QSPI clock

    - Map the QSPI to dedicated GPIO port

    - Enabel QSPI interrupt

    参数
    :   **config** – QSPI parameter settings

    返回
    :   - BK_OK: succeed

        - BK_ERR_QSPI_NOT_INIT: QSPI driver not init

        - BK_ERR_NULL_PARAM: QSPI config parameter is NULL

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_deinit(void)[](#_CPPv414bk_qspi_deinitv "永久链接至目标")
:   Deinit the QSPI.

    This API deinit the QSPI:


    - Disable the QSPI interrupt

    - Power down the QSPI

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_command(const [qspi_cmd_t](#_CPPv410qspi_cmd_t "qspi_cmd_t") *cmd)[](#_CPPv415bk_qspi_commandPK10qspi_cmd_t "永久链接至目标")
:   Init the QSPI command.

    参数
    :   **cmd** – QSPI device command

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_write(const void *data, uint32_t size)[](#_CPPv413bk_qspi_writePKv8uint32_t "永久链接至目标")
:   QSPI indirect mode write.

    参数
    :   - **base_addr** – QSPI write address

        - **data** – QSPI write data

        - **size** – the size of QSPI write data

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_read(void *data, uint32_t size)[](#_CPPv412bk_qspi_readPv8uint32_t "永久链接至目标")
:   QSPI indirect mode read.

    参数
    :   - **base_addr** – QSPI read address

        - **data** – QSPI read data

        - **size** – the size of QSPI read data

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_register_tx_isr([qspi_isr_t](#_CPPv410qspi_isr_t "qspi_isr_t") isr, void *param)[](#_CPPv423bk_qspi_register_tx_isr10qspi_isr_tPv "永久链接至目标")
:   Register the TX interrupt service routine for QSPI.

    参数
    :   - **isr** – QSPI TX callback

        - **param** – QSPI TX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_register_rx_isr([qspi_isr_t](#_CPPv410qspi_isr_t "qspi_isr_t") isr, void *param)[](#_CPPv423bk_qspi_register_rx_isr10qspi_isr_tPv "永久链接至目标")
:   Register the RX interrupt service routine for QSPI.

    参数
    :   - **isr** – QSPI RX callback

        - **param** – QSPI RX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.


## QSPI PSRAM API Reference[](#qspi-psram-api-reference "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [qspi_psram.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi_psram.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi_psram.h")


### Functions[](#id2 "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_init(void)[](#_CPPv418bk_qspi_psram_initv "永久链接至目标")
:   Init the QSPI psram.

    返回
    :   - BK_OK: succeed

        - BK_ERR_QSPI_NOT_INIT: QSPI driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_deinit(void)[](#_CPPv420bk_qspi_psram_deinitv "永久链接至目标")
:   Deinit the QSPI psram.

    返回
    :   - BK_OK: succeed

        - BK_ERR_QSPI_NOT_INIT: QSPI driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_enter_quad_mode(void)[](#_CPPv429bk_qspi_psram_enter_quad_modev "永久链接至目标")
:   QSPI psram enter quad mode.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_exit_quad_mode(void)[](#_CPPv428bk_qspi_psram_exit_quad_modev "永久链接至目标")
:   QSPI psram exit quad mode.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_quad_write(void)[](#_CPPv424bk_qspi_psram_quad_writev "永久链接至目标")
:   QSPI psram init quad write.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_single_write(void)[](#_CPPv426bk_qspi_psram_single_writev "永久链接至目标")
:   QSPI psram init single write.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_quad_read(void)[](#_CPPv423bk_qspi_psram_quad_readv "永久链接至目标")
:   QSPI psram init quad read.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_single_read(void)[](#_CPPv425bk_qspi_psram_single_readv "永久链接至目标")
:   QSPI psram init single read.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_write(uint32_t base_addr, const void *data, uint32_t size)[](#_CPPv419bk_qspi_psram_write8uint32_tPKv8uint32_t "永久链接至目标")
:   QSPI psram write data.

    参数
    :   - **base_addr** – QSPI write address

        - **data** – QSPI write data

        - **size** – the size of QSPI write data

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_qspi_psram_read(uint32_t base_addr, void *data, uint32_t size)[](#_CPPv418bk_qspi_psram_read8uint32_tPv8uint32_t "永久链接至目标")
:   QSPI psram read data.

    参数
    :   - **base_addr** – QSPI read address

        - **data** – QSPI read data

        - **size** – the size of QSPI read data

    返回
    :   - BK_OK: succeed

        - others: other errors.


## QSPI API Typedefs[](#qspi-api-typedefs "永久链接至标题")


### Header File[](#id3 "永久链接至标题")


- [qspi_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/qspi_types.h")


### Structures[](#structures "永久链接至标题")

struct qspi_driver_t[](#_CPPv413qspi_driver_t "永久链接至目标")

struct qspi_callback_t[](#_CPPv415qspi_callback_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

BK_ERR_QSPI_NOT_INIT[](#c.BK_ERR_QSPI_NOT_INIT "永久链接至目标")
:   QSPI driver not init

BK_ERR_QSPI_ID_NOT_INIT[](#c.BK_ERR_QSPI_ID_NOT_INIT "永久链接至目标")
:   QSPI id not init


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*qspi_isr_t)([qspi_id_t](#_CPPv49qspi_id_t "qspi_id_t") id, void *param)[](#_CPPv410qspi_isr_t "永久链接至目标")
:   QSPI interrupt service routine.


### Header File[](#id4 "永久链接至标题")


- [hal/hal_qspi_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_qspi_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_qspi_types.h")


### Structures[](#id5 "永久链接至标题")

struct qspi_config_t[](#_CPPv413qspi_config_t "永久链接至目标")
:   Public Members

    [qspi_src_clk_t](#_CPPv414qspi_src_clk_t "qspi_src_clk_t") src_clk[](#_CPPv4N13qspi_config_t7src_clkE "永久链接至目标")
    :   QSPI source clock

    uint32_t src_clk_div[](#_CPPv4N13qspi_config_t11src_clk_divE "永久链接至目标")
    :   QSPI source clock divide number

    uint32_t clk_div[](#_CPPv4N13qspi_config_t7clk_divE "永久链接至目标")
    :   QSPI controller clock divide number

struct qspi_cmd_t[](#_CPPv410qspi_cmd_t "永久链接至目标")
:   Public Members

    [qspi_wire_mode_t](#_CPPv416qspi_wire_mode_t "qspi_wire_mode_t") wire_mode[](#_CPPv4N10qspi_cmd_t9wire_modeE "永久链接至目标")
    :   wire mode

    [qspi_work_mode](#_CPPv414qspi_work_mode "qspi_work_mode") work_mode[](#_CPPv4N10qspi_cmd_t9work_modeE "永久链接至目标")
    :   work mode

    [qspi_op_t](#_CPPv49qspi_op_t "qspi_op_t") op[](#_CPPv4N10qspi_cmd_t2opE "永久链接至目标")
    :   QSPI operation

    uint32_t cmd[](#_CPPv4N10qspi_cmd_t3cmdE "永久链接至目标")
    :   QSPI command

    uint32_t addr[](#_CPPv4N10qspi_cmd_t4addrE "永久链接至目标")
    :   QSPI address

    uint32_t dummy_cycle[](#_CPPv4N10qspi_cmd_t11dummy_cycleE "永久链接至目标")
    :   QSPI dummy cycle

    uint32_t data_len[](#_CPPv4N10qspi_cmd_t8data_lenE "永久链接至目标")
    :   QSPI data length

    [qspi_device_t](#_CPPv413qspi_device_t "qspi_device_t") device[](#_CPPv4N10qspi_cmd_t6deviceE "永久链接至目标")
    :   QSPI slave device


### Type Definitions[](#id6 "永久链接至标题")

typedef uint8_t qspi_unit_t[](#_CPPv411qspi_unit_t "永久链接至目标")
:   QSPI uint id

typedef uint8_t qspi_id_t[](#_CPPv49qspi_id_t "永久链接至目标")
:   QSPI id


### Enumerations[](#enumerations "永久链接至标题")

enum qspi_op_t[](#_CPPv49qspi_op_t "永久链接至目标")
:   *Values:*

    enumerator QSPI_READ[](#_CPPv4N9qspi_op_t9QSPI_READE "永久链接至目标")
    :   QSPI read operation

    enumerator QSPI_WRITE[](#_CPPv4N9qspi_op_t10QSPI_WRITEE "永久链接至目标")
    :   QSPI write operation

enum qspi_src_clk_t[](#_CPPv414qspi_src_clk_t "永久链接至目标")
:   *Values:*

    enumerator QSPI_SCLK_DCO[](#_CPPv4N14qspi_src_clk_t13QSPI_SCLK_DCOE "永久链接至目标")
    :   QSPI source clock dco

    enumerator QSPI_SCLK_XTAL_26M[](#_CPPv4N14qspi_src_clk_t18QSPI_SCLK_XTAL_26ME "永久链接至目标")
    :   QSPI source clock xtal 26M

    enumerator QSPI_SCLK_80M[](#_CPPv4N14qspi_src_clk_t13QSPI_SCLK_80ME "永久链接至目标")
    :   QSPI source clock 80M

    enumerator QSPI_SCLK_120M[](#_CPPv4N14qspi_src_clk_t14QSPI_SCLK_120ME "永久链接至目标")
    :   QSPI source clock 120M

    enumerator QSPI_SCLK_320M[](#_CPPv4N14qspi_src_clk_t14QSPI_SCLK_320ME "永久链接至目标")
    :   QSPI source clock 320M

    enumerator QSPI_SCLK_480M[](#_CPPv4N14qspi_src_clk_t14QSPI_SCLK_480ME "永久链接至目标")
    :   QSPI source clock 480M

enum qspi_work_mode[](#_CPPv414qspi_work_mode "永久链接至目标")
:   *Values:*

    enumerator MEMORY_MAPPED_MODE[](#_CPPv4N14qspi_work_mode18MEMORY_MAPPED_MODEE "永久链接至目标")

    enumerator INDIRECT_MODE[](#_CPPv4N14qspi_work_mode13INDIRECT_MODEE "永久链接至目标")

enum qspi_wire_mode_t[](#_CPPv416qspi_wire_mode_t "永久链接至目标")
:   *Values:*

    enumerator QSPI_1WIRE[](#_CPPv4N16qspi_wire_mode_t10QSPI_1WIREE "永久链接至目标")
    :   QSPI 1_wire mode, standard SPI

    enumerator QSPI_2WIRE[](#_CPPv4N16qspi_wire_mode_t10QSPI_2WIREE "永久链接至目标")
    :   QSPI 2_wire mode, DUAL SPI

    enumerator QSPI_4WIRE[](#_CPPv4N16qspi_wire_mode_t10QSPI_4WIREE "永久链接至目标")
    :   QSPI 4_wire mode, QUAD SPI

enum qspi_device_t[](#_CPPv413qspi_device_t "永久链接至目标")
:   *Values:*

    enumerator QSPI_PSRAM[](#_CPPv4N13qspi_device_t10QSPI_PSRAME "永久链接至目标")
    :   QSPI PSRAM

    enumerator QSPI_FLASH[](#_CPPv4N13qspi_device_t10QSPI_FLASHE "永久链接至目标")
    :   QSPI FLASH

    enumerator QSPI_OLED[](#_CPPv4N13qspi_device_t9QSPI_OLEDE "永久链接至目标")
    :   QSPI OLED
