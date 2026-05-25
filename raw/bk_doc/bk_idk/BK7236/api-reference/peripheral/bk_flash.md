# FLASH[](#flash "永久链接至标题")


## FLASH API Status[](#flash-api-status "永久链接至标题")

| API | BK7236 | BK7236_cp1 |
| --- | --- | --- |
| [`bk_flash_driver_init()`](#_CPPv420bk_flash_driver_initv "bk_flash_driver_init") | Y | Y |
| [`bk_flash_driver_deinit()`](#_CPPv422bk_flash_driver_deinitv "bk_flash_driver_deinit") | Y | Y |
| [`bk_flash_set_line_mode()`](#_CPPv422bk_flash_set_line_mode17flash_line_mode_t "bk_flash_set_line_mode") | Y | Y |
| [`bk_flash_get_line_mode()`](#_CPPv422bk_flash_get_line_modev "bk_flash_get_line_mode") | Y | Y |
| [`bk_flash_get_id()`](#_CPPv415bk_flash_get_idv "bk_flash_get_id") | Y | Y |
| [`bk_flash_set_clk_dpll()`](#_CPPv421bk_flash_set_clk_dpllv "bk_flash_set_clk_dpll") | Y | Y |
| [`bk_flash_set_clk_dco()`](#_CPPv420bk_flash_set_clk_dcov "bk_flash_set_clk_dco") | Y | Y |
| [`bk_flash_write_enable()`](#_CPPv421bk_flash_write_enablev "bk_flash_write_enable") | Y | Y |
| [`bk_flash_write_disable()`](#_CPPv422bk_flash_write_disablev "bk_flash_write_disable") | Y | Y |
| [`bk_flash_set_protect_type()`](#_CPPv425bk_flash_set_protect_type20flash_protect_type_t "bk_flash_set_protect_type") | Y | Y |
| [`bk_flash_get_protect_type()`](#_CPPv425bk_flash_get_protect_typev "bk_flash_get_protect_type") | Y | Y |
| [`bk_flash_read_status_reg()`](#_CPPv424bk_flash_read_status_regv "bk_flash_read_status_reg") | Y | Y |
| [`bk_flash_write_status_reg()`](#_CPPv425bk_flash_write_status_reg8uint16_t "bk_flash_write_status_reg") | Y | Y |
| [`bk_flash_erase_sector()`](#_CPPv421bk_flash_erase_sector8uint32_t "bk_flash_erase_sector") | Y | Y |
| [`bk_flash_write_bytes()`](#_CPPv420bk_flash_write_bytes8uint32_tPK7uint8_t8uint32_t "bk_flash_write_bytes") | Y | Y |
| [`bk_flash_read_bytes()`](#_CPPv419bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t "bk_flash_read_bytes") | Y | Y |


## FLASH API Reference[](#flash-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [flash.h](https://github.com/bekencorp/armino/blob/main/components/flash.h "https://github.com/bekencorp/armino/blob/main/components/flash.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_driver_init(void)[](#_CPPv420bk_flash_driver_initv "永久链接至目标")
:   Init the flash driver.

    This API init the resoure common:


    - Init flash driver control memory


    **Attention**
    :   1. This API should be called before any other flash APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_driver_deinit(void)[](#_CPPv422bk_flash_driver_deinitv "永久链接至目标")
:   Deinit the flash driver.

    This API free all resource related to flash and disable flash.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_set_line_mode([flash_line_mode_t](#_CPPv417flash_line_mode_t "flash_line_mode_t") line_mode)[](#_CPPv422bk_flash_set_line_mode17flash_line_mode_t "永久链接至目标")
:   Set flash line mode.

    参数
    :   **line_mode** – flash line mode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[flash_line_mode_t](#_CPPv417flash_line_mode_t "flash_line_mode_t") bk_flash_get_line_mode(void)[](#_CPPv422bk_flash_get_line_modev "永久链接至目标")
:   Get flash line mode.

    返回
    :   flash line mode

uint32_t bk_flash_get_id(void)[](#_CPPv415bk_flash_get_idv "永久链接至目标")
:   Get flash id.

    返回
    :   flash line mode

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_set_clk_dpll(void)[](#_CPPv421bk_flash_set_clk_dpllv "永久链接至目标")
:   Set flash clock dpll.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_set_clk_dco(void)[](#_CPPv420bk_flash_set_clk_dcov "永久链接至目标")
:   Set flash clock dco.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_write_enable(void)[](#_CPPv421bk_flash_write_enablev "永久链接至目标")
:   Enable flash write.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_write_disable(void)[](#_CPPv422bk_flash_write_disablev "永久链接至目标")
:   Disable flash write.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_set_protect_type([flash_protect_type_t](#_CPPv420flash_protect_type_t "flash_protect_type_t") type)[](#_CPPv425bk_flash_set_protect_type20flash_protect_type_t "永久链接至目标")
:   Set flash protect type.

    参数
    :   **type** – flash protect type

    返回
    :   - BK_OK: succeed

        - others: other errors.

[flash_protect_type_t](#_CPPv420flash_protect_type_t "flash_protect_type_t") bk_flash_get_protect_type(void)[](#_CPPv425bk_flash_get_protect_typev "永久链接至目标")
:   Get flash protect type.

    返回
    :   the flash protect type

uint16_t bk_flash_read_status_reg(void)[](#_CPPv424bk_flash_read_status_regv "永久链接至目标")
:   Get flash status register value.

    返回
    :   the flash status register value

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_write_status_reg(uint16_t status_reg_data)[](#_CPPv425bk_flash_write_status_reg8uint16_t "永久链接至目标")
:   Set flash status register value.

    参数
    :   **status_reg_data** – the flash status register data

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_erase_sector(uint32_t address)[](#_CPPv421bk_flash_erase_sector8uint32_t "永久链接至目标")
:   Erase a sector of flash, use flash command 0x20.

    参数
    :   **address** – flash address

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_erase_block(uint32_t address)[](#_CPPv420bk_flash_erase_block8uint32_t "永久链接至目标")
:   Erase a sector of flash, use flash command 0xD8.

    参数
    :   **address** – flash address

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_enter_deep_sleep(void)[](#_CPPv425bk_flash_enter_deep_sleepv "永久链接至目标")
:   Entry flash deep power-down flash, use flash command 0xB9.

    返回
    :   - BK_OK: succeed

        - BK_FAIL: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_exit_deep_sleep(void)[](#_CPPv424bk_flash_exit_deep_sleepv "永久链接至目标")
:   Exit flash deep power-down flash, use flash command 0xAB.

    返回
    :   - BK_OK: succeed

        - BK_FAIL: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_write_bytes(uint32_t address, const uint8_t *user_buf, uint32_t size)[](#_CPPv420bk_flash_write_bytes8uint32_tPK7uint8_t8uint32_t "永久链接至目标")
:   Write data to flash.

    参数
    :   - **address** – address to write

        - **user_buf** – the pointer to data which is to write

        - **size** – size to write

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_read_bytes(uint32_t address, uint8_t *user_buf, uint32_t size)[](#_CPPv419bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t "永久链接至目标")
:   Read data from flash.

    参数
    :   - **address** – address to read

        - **user_buf** – the buffer to read the data

        - **size** – size to read

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_read_word(uint32_t address, uint32_t *user_buf, uint32_t size)[](#_CPPv418bk_flash_read_word8uint32_tP8uint32_t8uint32_t "永久链接至目标")
:   Read data from flas.

    参数
    :   - **address** – address to read

        - **user_buf** – the buffer to read the data, intend to psram addr must aline by 4 Bytes

        - **size** – size to read, length uint by byte

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

bool bk_flash_is_driver_inited(void)[](#_CPPv425bk_flash_is_driver_initedv "永久链接至目标")
:   Get flash init flag.

    返回
    :   the flash init flag

uint32_t bk_flash_get_current_total_size(void)[](#_CPPv431bk_flash_get_current_total_sizev "永久链接至目标")
:   Get flash total size.

    返回
    :   the flash total size

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_register_ps_suspend_callback([flash_ps_callback_t](#_CPPv419flash_ps_callback_t "flash_ps_callback_t") ps_suspend_cb)[](#_CPPv437bk_flash_register_ps_suspend_callback19flash_ps_callback_t "永久链接至目标")
:   Register flash power save suspend callback.

    参数
    :   **ps_suspend_cb** – power save suspend callback

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_register_ps_resume_callback([flash_ps_callback_t](#_CPPv419flash_ps_callback_t "flash_ps_callback_t") ps_resume_cb)[](#_CPPv436bk_flash_register_ps_resume_callback19flash_ps_callback_t "永久链接至目标")
:   Register flash power save resume callback.

    参数
    :   **ps_resume_cb** – power save resume callback

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_clk_switch(uint32_t flash_speed_type, uint32_t modules)[](#_CPPv419bk_flash_clk_switch8uint32_t8uint32_t "永久链接至目标")
:   Modify flash speed type.

    参数
    :   - **flash_speed_type** – the high/low type of flash clock

        - **modules** – the app module to control the flash spped

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_register_wait_cb([flash_wait_callback_t](#_CPPv421flash_wait_callback_t "flash_wait_callback_t") wait_cb)[](#_CPPv425bk_flash_register_wait_cb21flash_wait_callback_t "永久链接至目标")
:   register a callback to be called when flash is busy waiting. WARNING/NOTES:

    1. the wait_cb code is better in ITCM to avoid running in flash. or the wait_cb will be blocked until flash is idle. 2.The wait_cb will be called forever until flash is idle, so the implemetion of wait_cb should garante the programm is safe.

    BK_OK: succeed


    - others: registered too many(>4) wait_cb to flash.

    参数
    :   **wait_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait_cb to flash. When flash is writing/erasing, it will call this wait_cb

    返回

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_unregister_wait_cb([flash_wait_callback_t](#_CPPv421flash_wait_callback_t "flash_wait_callback_t") wait_cb)[](#_CPPv427bk_flash_unregister_wait_cb21flash_wait_callback_t "永久链接至目标")
:   unregister the wait_cb from flash waiting.

    参数
    :   **wait_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait_cb to flash. When flash is writing/erasing, it will call this wait_cb

    返回
    :   - BK_OK: succeed

        - others: The wait_cb isn’t registered to flash.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_set_operate_status([flash_op_status_t](#_CPPv417flash_op_status_t "flash_op_status_t") status)[](#_CPPv427bk_flash_set_operate_status17flash_op_status_t "永久链接至目标")
:   Set flash operate status.

    参数
    :   **flash** – operate status

    返回
    :   - BK_OK: succeed

        - others: other errors.

[flash_op_status_t](#_CPPv417flash_op_status_t "flash_op_status_t") bk_flash_get_operate_status(void)[](#_CPPv427bk_flash_get_operate_statusv "永久链接至目标")
:   Get flash operate status.

    返回
    :   flash operate status

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") mb_flash_register_op_notify(void *notify_cb)[](#_CPPv427mb_flash_register_op_notifyPv "永久链接至目标")
:   register a callback to be called when flash is busy waiting.

    参数
    :   **wait_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait_cb to flash. When flash is writing/erasing, it will call this wait_cb

    返回
    :   - BK_OK: succeed

        - others: registered too many(>4) wait_cb to flash.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") mb_flash_unregister_op_notify(void *notify_cb)[](#_CPPv429mb_flash_unregister_op_notifyPv "永久链接至目标")
:   unregister the wait_cb from flash waiting.

    参数
    :   **wait_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait_cb to flash. When flash is writing/erasing, it will call this wait_cb

    返回
    :   - BK_OK: succeed

        - others: The wait_cb isn’t registered to flash.

uint32_t flash_get_excute_enable()[](#_CPPv423flash_get_excute_enablev "永久链接至目标")


## FLASH API Typedefs[](#flash-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [flash_types.h](https://github.com/bekencorp/armino/blob/main/components/flash_types.h "https://github.com/bekencorp/armino/blob/main/components/flash_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_FLASH_NOT_INIT[](#c.BK_ERR_FLASH_NOT_INIT "永久链接至目标")
:   FLASH driver not init

BK_ERR_FLASH_ADDR_OUT_OF_RANGE[](#c.BK_ERR_FLASH_ADDR_OUT_OF_RANGE "永久链接至目标")
:   FLASH address is out of range

BK_ERR_FLASH_PARTITION_NOT_FOUND[](#c.BK_ERR_FLASH_PARTITION_NOT_FOUND "永久链接至目标")
:   FLASH partition not found

BK_ERR_FLASH_WAIT_CB_FULL[](#c.BK_ERR_FLASH_WAIT_CB_FULL "永久链接至目标")
:   FLASH wait cb is registered too much

BK_ERR_FLASH_WAIT_CB_NOT_REGISTER[](#c.BK_ERR_FLASH_WAIT_CB_NOT_REGISTER "永久链接至目标")
:   FLASH wait cb is not registered but tried to unregister

FLASH_ATE_BIT[](#c.FLASH_ATE_BIT "永久链接至目标")

FLASH_MAC_BIT[](#c.FLASH_MAC_BIT "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*flash_ps_callback_t)(void)[](#_CPPv419flash_ps_callback_t "永久链接至目标")

typedef void (*flash_wait_callback_t)(void)[](#_CPPv421flash_wait_callback_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum flash_line_mode_t[](#_CPPv417flash_line_mode_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_LINE_MODE_TWO[](#_CPPv4N17flash_line_mode_t19FLASH_LINE_MODE_TWOE "永久链接至目标")
    :   flash line mode 2

    enumerator FLASH_LINE_MODE_FOUR[](#_CPPv4N17flash_line_mode_t20FLASH_LINE_MODE_FOURE "永久链接至目标")
    :   flash line mode 4

enum flash_protect_type_t[](#_CPPv420flash_protect_type_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_PROTECT_NONE[](#_CPPv4N20flash_protect_type_t18FLASH_PROTECT_NONEE "永久链接至目标")
    :   flash protect type none

    enumerator FLASH_PROTECT_ALL[](#_CPPv4N20flash_protect_type_t17FLASH_PROTECT_ALLE "永久链接至目标")
    :   flash protect type all

    enumerator FLASH_PROTECT_HALF[](#_CPPv4N20flash_protect_type_t18FLASH_PROTECT_HALFE "永久链接至目标")
    :   flash protect type half

    enumerator FLASH_UNPROTECT_LAST_BLOCK[](#_CPPv4N20flash_protect_type_t26FLASH_UNPROTECT_LAST_BLOCKE "永久链接至目标")
    :   flash protect type unprotect last block

enum flash_speed_type_t[](#_CPPv418flash_speed_type_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_SPEED_HIGH[](#_CPPv4N18flash_speed_type_t16FLASH_SPEED_HIGHE "永久链接至目标")

    enumerator FLASH_SPEED_LOW[](#_CPPv4N18flash_speed_type_t15FLASH_SPEED_LOWE "永久链接至目标")

enum flash_ctrl_module_t[](#_CPPv419flash_ctrl_module_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_ATE[](#_CPPv4N19flash_ctrl_module_t9FLASH_ATEE "永久链接至目标")

    enumerator FLASH_MAC[](#_CPPv4N19flash_ctrl_module_t9FLASH_MACE "永久链接至目标")

enum flash_op_status_t[](#_CPPv417flash_op_status_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_OP_IDLE[](#_CPPv4N17flash_op_status_t13FLASH_OP_IDLEE "永久链接至目标")

    enumerator FLASH_OP_BUSY[](#_CPPv4N17flash_op_status_t13FLASH_OP_BUSYE "永久链接至目标")


### Header File[](#id2 "永久链接至标题")


- [hal/hal_flash_types.h](https://github.com/bekencorp/armino/blob/main/components/hal/hal_flash_types.h "https://github.com/bekencorp/armino/blob/main/components/hal/hal_flash_types.h")


### Type Definitions[](#id3 "永久链接至标题")

typedef uint8_t flash_unit_t[](#_CPPv412flash_unit_t "永久链接至目标")
:   flash uint id


### Enumerations[](#id4 "永久链接至标题")

enum flash_op_cmd_t[](#_CPPv414flash_op_cmd_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_OP_CMD_WREN[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_WRENE "永久链接至目标")
    :   flash command write enable

    enumerator FLASH_OP_CMD_WRDI[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_WRDIE "永久链接至目标")
    :   flash command write disable

    enumerator FLASH_OP_CMD_RDSR[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_RDSRE "永久链接至目标")
    :   flash command read status register

    enumerator FLASH_OP_CMD_WRSR[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_WRSRE "永久链接至目标")
    :   flash command write status register

    enumerator FLASH_OP_CMD_READ[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_READE "永久链接至目标")
    :   flash command read data

    enumerator FLASH_OP_CMD_RDSR2[](#_CPPv4N14flash_op_cmd_t18FLASH_OP_CMD_RDSR2E "永久链接至目标")
    :   flash command read status register-2

    enumerator FLASH_OP_CMD_WRSR2[](#_CPPv4N14flash_op_cmd_t18FLASH_OP_CMD_WRSR2E "永久链接至目标")
    :   flash command write status register-2

    enumerator FLASH_OP_CMD_PP[](#_CPPv4N14flash_op_cmd_t15FLASH_OP_CMD_PPE "永久链接至目标")
    :   flash command page program

    enumerator FLASH_OP_CMD_SE[](#_CPPv4N14flash_op_cmd_t15FLASH_OP_CMD_SEE "永久链接至目标")
    :   flash command sector erase

    enumerator FLASH_OP_CMD_BE1[](#_CPPv4N14flash_op_cmd_t16FLASH_OP_CMD_BE1E "永久链接至目标")
    :   flash command block erase-1

    enumerator FLASH_OP_CMD_BE2[](#_CPPv4N14flash_op_cmd_t16FLASH_OP_CMD_BE2E "永久链接至目标")
    :   flash command block erase-2

    enumerator FLASH_OP_CMD_CE[](#_CPPv4N14flash_op_cmd_t15FLASH_OP_CMD_CEE "永久链接至目标")
    :   flash command chip erase

    enumerator FLASH_OP_CMD_DP[](#_CPPv4N14flash_op_cmd_t15FLASH_OP_CMD_DPE "永久链接至目标")

    enumerator FLASH_OP_CMD_RFDP[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_RFDPE "永久链接至目标")

    enumerator FLASH_OP_CMD_RDID[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_RDIDE "永久链接至目标")
    :   flash command read device id

    enumerator FLASH_OP_CMD_HPM[](#_CPPv4N14flash_op_cmd_t16FLASH_OP_CMD_HPME "永久链接至目标")
    :   flash command high performance mode

    enumerator FLASH_OP_CMD_CRMR[](#_CPPv4N14flash_op_cmd_t17FLASH_OP_CMD_CRMRE "永久链接至目标")

    enumerator FLASH_OP_CMD_CRMR2[](#_CPPv4N14flash_op_cmd_t18FLASH_OP_CMD_CRMR2E "永久链接至目标")

enum flash_mode_t[](#_CPPv412flash_mode_t "永久链接至目标")
:   *Values:*

    enumerator FLASH_MODE_STANDARD[](#_CPPv4N12flash_mode_t19FLASH_MODE_STANDARDE "永久链接至目标")
    :   flash standard mode

    enumerator FLASH_MODE_DUAL[](#_CPPv4N12flash_mode_t15FLASH_MODE_DUALE "永久链接至目标")
    :   flash dual mode

    enumerator FLASH_MODE_QUAD[](#_CPPv4N12flash_mode_t15FLASH_MODE_QUADE "永久链接至目标")
    :   flash quad mode
