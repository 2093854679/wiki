---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/flash.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flash-api"></a>

# FLASH API

FLASH 存储器API接口。

<a id="header-file"></a>

## Header File

- [flash.h](https://github.com/bekencorp/armino/blob/main/components/flash.h)

<a id="functions"></a>

## Functions

<a id="_CPPv420bk_flash_driver_initv"></a>

<a id="_CPPv320bk_flash_driver_initv"></a> <a id="_CPPv220bk_flash_driver_initv"></a> <a id="bk_flash_driver_init__void"></a> <a id="flash_8h_1a1aee026efd127960beb97c31e0d2d7ac"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_driver\_init(void)
:   Init the flash driver.

    This API init the resoure common:

    - Init flash driver control memory

    **Attention**
    :   1\. This API should be called before any other flash APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_flash_driver_deinitv"></a>

<a id="_CPPv322bk_flash_driver_deinitv"></a> <a id="_CPPv222bk_flash_driver_deinitv"></a> <a id="bk_flash_driver_deinit__void"></a> <a id="flash_8h_1a36f79a5c775598f15fae3f73258abdcf"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_driver\_deinit(void)
:   Deinit the flash driver.

    This API free all resource related to flash and disable flash.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv413bk_flash_lockv"></a>

<a id="_CPPv313bk_flash_lockv"></a> <a id="_CPPv213bk_flash_lockv"></a> <a id="bk_flash_lock__void"></a> <a id="flash_8h_1a205ed7367cdca05f5a1ace1bb66bcb54"></a> void bk\_flash\_lock(void)
:   Lock current operation.

    Uses mutex lock to protect concurrent operations of flash read/write/… The default flash driver layer API doesn’t add lock/unlock to improve performance. it should be called in APP-layer.

    Param

<a id="_CPPv415bk_flash_unlockv"></a>

<a id="_CPPv315bk_flash_unlockv"></a> <a id="_CPPv215bk_flash_unlockv"></a> <a id="bk_flash_unlock__void"></a> <a id="flash_8h_1ac81a162599c144a68997e3d42ca86cf6"></a> void bk\_flash\_unlock(void)
:   unlock current operation.

    Param

<a id="_CPPv422bk_flash_set_line_mode17flash_line_mode_t"></a>

<a id="_CPPv322bk_flash_set_line_mode17flash_line_mode_t"></a> <a id="_CPPv222bk_flash_set_line_mode17flash_line_mode_t"></a> <a id="bk_flash_set_line_mode__flash_line_mode_t"></a> <a id="flash_8h_1a901e316efa39a3520cc236dddc2f94b7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_set\_line\_mode(flash\_line\_mode\_t line\_mode)
:   Set flash line mode.

    参数
    :   **line\_mode** – flash line mode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_flash_get_line_modev"></a>

<a id="_CPPv322bk_flash_get_line_modev"></a> <a id="_CPPv222bk_flash_get_line_modev"></a> <a id="bk_flash_get_line_mode__void"></a> <a id="flash_8h_1af36b099d4825ab38109265fa74aeab22"></a> flash\_line\_mode\_t bk\_flash\_get\_line\_mode(void)
:   Get flash line mode.

    返回
    :   flash line mode

<a id="_CPPv415bk_flash_get_idv"></a>

<a id="_CPPv315bk_flash_get_idv"></a> <a id="_CPPv215bk_flash_get_idv"></a> <a id="bk_flash_get_id__void"></a> <a id="flash_8h_1a85e8336aa46d46d418cb3bbb201e2157"></a> uint32\_t bk\_flash\_get\_id(void)
:   Get flash id.

    返回
    :   flash line mode

<a id="_CPPv427bk_flash_get_capacity_bytesv"></a>

<a id="_CPPv327bk_flash_get_capacity_bytesv"></a> <a id="_CPPv227bk_flash_get_capacity_bytesv"></a> <a id="bk_flash_get_capacity_bytes__void"></a> <a id="flash_8h_1ae06c7718e075cbf30bd254a5616dbe5d"></a> uint32\_t bk\_flash\_get\_capacity\_bytes(void)
:   Get flash capacity.

    返回
    :   flash size with bytes

<a id="_CPPv421bk_flash_set_clk_dpllv"></a>

<a id="_CPPv321bk_flash_set_clk_dpllv"></a> <a id="_CPPv221bk_flash_set_clk_dpllv"></a> <a id="bk_flash_set_clk_dpll__void"></a> <a id="flash_8h_1a0034b6e55c75574d09ca6117c8213692"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_set\_clk\_dpll(void)
:   Set flash clock dpll.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_flash_set_clk_dcov"></a>

<a id="_CPPv320bk_flash_set_clk_dcov"></a> <a id="_CPPv220bk_flash_set_clk_dcov"></a> <a id="bk_flash_set_clk_dco__void"></a> <a id="flash_8h_1ae9b7f7db1d4ab0a5b3883c22326571e8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_set\_clk\_dco(void)
:   Set flash clock dco.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_flash_write_enablev"></a>

<a id="_CPPv321bk_flash_write_enablev"></a> <a id="_CPPv221bk_flash_write_enablev"></a> <a id="bk_flash_write_enable__void"></a> <a id="flash_8h_1a2a99979031c02c1e281af97b7f3ef29c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_write\_enable(void)
:   Enable flash write.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_flash_write_disablev"></a>

<a id="_CPPv322bk_flash_write_disablev"></a> <a id="_CPPv222bk_flash_write_disablev"></a> <a id="bk_flash_write_disable__void"></a> <a id="flash_8h_1a361fa60c4e09b698d5d4d91a8dc9916e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_write\_disable(void)
:   Disable flash write.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_flash_set_protect_type20flash_protect_type_t"></a>

<a id="_CPPv325bk_flash_set_protect_type20flash_protect_type_t"></a> <a id="_CPPv225bk_flash_set_protect_type20flash_protect_type_t"></a> <a id="bk_flash_set_protect_type__flash_protect_type_t"></a> <a id="flash_8h_1a99bf250d2493bd1eca20a2d8ebd4b848"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_set\_protect\_type(flash\_protect\_type\_t type)
:   Set flash protect type.

    参数
    :   **type** – flash protect type

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_flash_get_protect_typev"></a>

<a id="_CPPv325bk_flash_get_protect_typev"></a> <a id="_CPPv225bk_flash_get_protect_typev"></a> <a id="bk_flash_get_protect_type__void"></a> <a id="flash_8h_1aff0b4099fd04f92768bb1ec0f21c6554"></a> flash\_protect\_type\_t bk\_flash\_get\_protect\_type(void)
:   Get flash protect type.

    返回
    :   the flash protect type

<a id="_CPPv424bk_flash_read_status_regv"></a>

<a id="_CPPv324bk_flash_read_status_regv"></a> <a id="_CPPv224bk_flash_read_status_regv"></a> <a id="bk_flash_read_status_reg__void"></a> <a id="flash_8h_1ac6a70665bb8d992bd2c2a90b2a3bd868"></a> uint16\_t bk\_flash\_read\_status\_reg(void)
:   Get flash status register value.

    返回
    :   the flash status register value

<a id="_CPPv425bk_flash_write_status_reg8uint16_t"></a>

<a id="_CPPv325bk_flash_write_status_reg8uint16_t"></a> <a id="_CPPv225bk_flash_write_status_reg8uint16_t"></a> <a id="bk_flash_write_status_reg__uint16_t"></a> <a id="flash_8h_1a54e1b925ca26ca0ad154a77d014a4361"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_write\_status\_reg(uint16\_t status\_reg\_data)
:   Set flash status register value.

    参数
    :   **status\_reg\_data** – the flash status register data

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_flash_erase_sector8uint32_t"></a>

<a id="_CPPv321bk_flash_erase_sector8uint32_t"></a> <a id="_CPPv221bk_flash_erase_sector8uint32_t"></a> <a id="bk_flash_erase_sector__uint32_t"></a> <a id="flash_8h_1ad8c0d020fa712f64a20bc300e634d0de"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_erase\_sector(uint32\_t address)
:   Erase a sector of flash, use flash command 0x20.

    参数
    :   **address** – flash address

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv420bk_flash_erase_block8uint32_t"></a>

<a id="_CPPv320bk_flash_erase_block8uint32_t"></a> <a id="_CPPv220bk_flash_erase_block8uint32_t"></a> <a id="bk_flash_erase_block__uint32_t"></a> <a id="flash_8h_1a4606a2667f7c4e2b38aa90bed1eb5911"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_erase\_block(uint32\_t address)
:   Erase a sector of flash, use flash command 0xD8.

    参数
    :   **address** – flash address

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv425bk_flash_enter_deep_sleepv"></a>

<a id="_CPPv325bk_flash_enter_deep_sleepv"></a> <a id="_CPPv225bk_flash_enter_deep_sleepv"></a> <a id="bk_flash_enter_deep_sleep__void"></a> <a id="flash_8h_1a3019d1a0a9ce6e0a6dfb7f7bd217877c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_enter\_deep\_sleep(void)
:   Entry flash deep power-down flash, use flash command 0xB9.

    返回
    :   - BK\_OK: succeed
        - BK\_FAIL: failed

<a id="_CPPv424bk_flash_exit_deep_sleepv"></a>

<a id="_CPPv324bk_flash_exit_deep_sleepv"></a> <a id="_CPPv224bk_flash_exit_deep_sleepv"></a> <a id="bk_flash_exit_deep_sleep__void"></a> <a id="flash_8h_1a799244036900300b3dd89ca8079bded7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_exit\_deep\_sleep(void)
:   Exit flash deep power-down flash, use flash command 0xAB.

    返回
    :   - BK\_OK: succeed
        - BK\_FAIL: failed

<a id="_CPPv420bk_flash_write_bytes8uint32_tPK7uint8_t8uint32_t"></a>

<a id="_CPPv320bk_flash_write_bytes8uint32_tPK7uint8_t8uint32_t"></a> <a id="_CPPv220bk_flash_write_bytes8uint32_tPK7uint8_t8uint32_t"></a> <a id="bk_flash_write_bytes__uint32_t.uint8_tCP.uint32_t"></a> <a id="flash_8h_1a12dad57774cf302a6f096b08554f2d2d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_write\_bytes(uint32\_t address, const uint8\_t \*user\_buf, uint32\_t size)
:   Write data to flash.

    参数
    :   - **address** – address to write
        - **user\_buf** – the pointer to data which is to write
        - **size** – size to write

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv419bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv319bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv219bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t"></a> <a id="bk_flash_read_bytes__uint32_t.uint8_tP.uint32_t"></a> <a id="flash_8h_1a9a59ee730ee28fb485f219a9d3fe7c24"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_read\_bytes(uint32\_t address, uint8\_t \*user\_buf, uint32\_t size)
:   Read data from flash.

    参数
    :   - **address** – address to read
        - **user\_buf** – the buffer to read the data
        - **size** – size to read

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv418bk_flash_read_word8uint32_tP8uint32_t8uint32_t"></a>

<a id="_CPPv318bk_flash_read_word8uint32_tP8uint32_t8uint32_t"></a> <a id="_CPPv218bk_flash_read_word8uint32_tP8uint32_t8uint32_t"></a> <a id="bk_flash_read_word__uint32_t.uint32_tP.uint32_t"></a> <a id="flash_8h_1a3ef5ef27f5abceb8b0e276367be8a5f3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_read\_word(uint32\_t address, uint32\_t \*user\_buf, uint32\_t size)
:   Read data from flas.

    参数
    :   - **address** – address to read
        - **user\_buf** – the buffer to read the data, intend to psram addr must aline by 4 Bytes
        - **size** – size to read, length uint by byte

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv425bk_flash_is_driver_initedv"></a>

<a id="_CPPv325bk_flash_is_driver_initedv"></a> <a id="_CPPv225bk_flash_is_driver_initedv"></a> <a id="bk_flash_is_driver_inited__void"></a> <a id="flash_8h_1a43aecdd3ad017041bff0a019316e18c6"></a> bool bk\_flash\_is\_driver\_inited(void)
:   Get flash init flag.

    返回
    :   the flash init flag

<a id="_CPPv431bk_flash_get_current_total_sizev"></a>

<a id="_CPPv331bk_flash_get_current_total_sizev"></a> <a id="_CPPv231bk_flash_get_current_total_sizev"></a> <a id="bk_flash_get_current_total_size__void"></a> <a id="flash_8h_1a46025696cf09a1a4bfa32a0f2d74934f"></a> uint32\_t bk\_flash\_get\_current\_total\_size(void)
:   Get flash total size.

    返回
    :   the flash total size

<a id="_CPPv437bk_flash_register_ps_suspend_callback19flash_ps_callback_t"></a>

<a id="_CPPv337bk_flash_register_ps_suspend_callback19flash_ps_callback_t"></a> <a id="_CPPv237bk_flash_register_ps_suspend_callback19flash_ps_callback_t"></a> <a id="bk_flash_register_ps_suspend_callback__flash_ps_callback_t"></a> <a id="flash_8h_1a6d438d8607fc964fb92a29cd46fbded3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_register\_ps\_suspend\_callback(flash\_ps\_callback\_t ps\_suspend\_cb)
:   Register flash power save suspend callback.

    参数
    :   **ps\_suspend\_cb** – power save suspend callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_flash_register_ps_resume_callback19flash_ps_callback_t"></a>

<a id="_CPPv336bk_flash_register_ps_resume_callback19flash_ps_callback_t"></a> <a id="_CPPv236bk_flash_register_ps_resume_callback19flash_ps_callback_t"></a> <a id="bk_flash_register_ps_resume_callback__flash_ps_callback_t"></a> <a id="flash_8h_1a0ae871bb89b81d1c3f811a06f5e56bc2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_register\_ps\_resume\_callback(flash\_ps\_callback\_t ps\_resume\_cb)
:   Register flash power save resume callback.

    参数
    :   **ps\_resume\_cb** – power save resume callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_flash_clk_switch8uint32_t8uint32_t"></a>

<a id="_CPPv319bk_flash_clk_switch8uint32_t8uint32_t"></a> <a id="_CPPv219bk_flash_clk_switch8uint32_t8uint32_t"></a> <a id="bk_flash_clk_switch__uint32_t.uint32_t"></a> <a id="flash_8h_1a5e1db73a1af0c2684e802698ccaedb3a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_clk\_switch(uint32\_t flash\_speed\_type, uint32\_t modules)
:   Modify flash speed type.

    参数
    :   - **flash\_speed\_type** – the high/low type of flash clock
        - **modules** – the app module to control the flash spped

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_flash_register_wait_cb21flash_wait_callback_t"></a>

<a id="_CPPv325bk_flash_register_wait_cb21flash_wait_callback_t"></a> <a id="_CPPv225bk_flash_register_wait_cb21flash_wait_callback_t"></a> <a id="bk_flash_register_wait_cb__flash_wait_callback_t"></a> <a id="flash_8h_1a0226b26923ed262274e49b68eb747615"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_register\_wait\_cb(flash\_wait\_callback\_t wait\_cb)
:   register a callback to be called when flash is busy waiting. WARNING/NOTES:

    1. the wait\_cb code is better in ITCM to avoid running in flash. or the wait\_cb will be blocked until flash is idle. 2.The wait\_cb will be called forever until flash is idle, so the implemetion of wait\_cb should garante the programm is safe.

    BK\_OK: succeed

    - others: registered too many(\>4) wait\_cb to flash.

    参数
    :   **wait\_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait\_cb to flash. When flash is writing/erasing, it will call this wait\_cb

    返回

<a id="_CPPv427bk_flash_unregister_wait_cb21flash_wait_callback_t"></a>

<a id="_CPPv327bk_flash_unregister_wait_cb21flash_wait_callback_t"></a> <a id="_CPPv227bk_flash_unregister_wait_cb21flash_wait_callback_t"></a> <a id="bk_flash_unregister_wait_cb__flash_wait_callback_t"></a> <a id="flash_8h_1a1509c2f2d99b0916cc1af093805114cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_unregister\_wait\_cb(flash\_wait\_callback\_t wait\_cb)
:   unregister the wait\_cb from flash waiting.

    参数
    :   **wait\_cb:If** – flash is writing/erasing, it will block all of other applications. But maybe the application can’t be blocked when flash is writing/erasing. So the application should register this wait\_cb to flash. When flash is writing/erasing, it will call this wait\_cb

    返回
    :   - BK\_OK: succeed
        - others: The wait\_cb isn’t registered to flash.

<a id="_CPPv427bk_flash_set_operate_status17flash_op_status_t"></a>

<a id="_CPPv327bk_flash_set_operate_status17flash_op_status_t"></a> <a id="_CPPv227bk_flash_set_operate_status17flash_op_status_t"></a> <a id="bk_flash_set_operate_status__flash_op_status_t"></a> <a id="flash_8h_1a20179ba4f633334461160cf79c4804d1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_set\_operate\_status(flash\_op\_status\_t status)
:   Set flash operate status.

    参数
    :   **flash** – operate status

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_flash_get_operate_statusv"></a>

<a id="_CPPv327bk_flash_get_operate_statusv"></a> <a id="_CPPv227bk_flash_get_operate_statusv"></a> <a id="bk_flash_get_operate_status__void"></a> <a id="flash_8h_1a18ce35416a3c47a30383cc149e6486aa"></a> flash\_op\_status\_t bk\_flash\_get\_operate\_status(void)
:   Get flash operate status.

    返回
    :   flash operate status
