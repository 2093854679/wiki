---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/i2c.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="i2c-api"></a>

# I2C API

I2C (Inter-Integrated Circuit) 两线制串行通信API接口。

<a id="header-file"></a>

## Header File

- [i2c.h](https://github.com/bekencorp/armino/blob/main/components/i2c.h)

<a id="functions"></a>

## Functions

<a id="_CPPv418bk_i2c_driver_initv"></a>

<a id="_CPPv318bk_i2c_driver_initv"></a> <a id="_CPPv218bk_i2c_driver_initv"></a> <a id="bk_i2c_driver_init__void"></a> <a id="i2c_8h_1a7a66021ef6c20b8b70ee659e491bed93"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_driver\_init(void)
:   Init the I2C driver.

    This API init the resoure common:

    - Init I2C driver control memory

    **Attention**
    :   1\. This API should be called before any other I2C APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_i2c_driver_deinitv"></a>

<a id="_CPPv320bk_i2c_driver_deinitv"></a> <a id="_CPPv220bk_i2c_driver_deinitv"></a> <a id="bk_i2c_driver_deinit__void"></a> <a id="i2c_8h_1ac216878ee86d85f1d366afd269274976"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_driver\_deinit(void)
:   Deinit the I2C driver.

    This API free all resource related to I2C and disable I2C.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_i2c_init8i2c_id_tPK12i2c_config_t"></a>

<a id="_CPPv311bk_i2c_init8i2c_id_tPK12i2c_config_t"></a> <a id="_CPPv211bk_i2c_init8i2c_id_tPK12i2c_config_t"></a> <a id="bk_i2c_init__i2c_id_t.i2c_config_tCP"></a> <a id="i2c_8h_1a184ca212e6e602b164349469c4cbc506"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_init(i2c\_id\_t id, const i2c\_config\_t \*cfg)
:   Init the I2C id.

    This API init the I2C id:

    - Power up the I2C id
    - Configure the I2C id clock
    - Map the I2C id to dedicated GPIO port
    - Set the I2C parameters
    - Start the I2C id

    **Attention**
    :   Multifunction GPIO initialization affects other functions

    参数
    :   - **id** – I2C id
        - **config** – I2C parameter settings

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C config paramter is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - others: other errors.

<a id="_CPPv413bk_i2c_deinit8i2c_id_t"></a>

<a id="_CPPv313bk_i2c_deinit8i2c_id_t"></a> <a id="_CPPv213bk_i2c_deinit8i2c_id_t"></a> <a id="bk_i2c_deinit__i2c_id_t"></a> <a id="i2c_8h_1a02c72d467407aab151ef26f839ce23b8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_deinit(i2c\_id\_t id)
:   Deinit the I2C id.

    This API deinit the I2C id:

    - Stop the I2C id
    - Disable the I2C id interrupt
    - Power down the I2C id

    参数
    :   **id** – I2C id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_i2c_master_write8i2c_id_t8uint32_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv319bk_i2c_master_write8i2c_id_t8uint32_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv219bk_i2c_master_write8i2c_id_t8uint32_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_master_write__i2c_id_t.uint32_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="i2c_8h_1a2c200ace339b65368d5816b420de025b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_master\_write(i2c\_id\_t id, uint32\_t dev\_addr, const uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   Write data to the I2C port from a given buffer and length, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **dev\_addr** – slave device address
        - **data** – pointer to the buffer
        - **size** – data length to write
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv426bk_i2c_master_write_noaddr8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv326bk_i2c_master_write_noaddr8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv226bk_i2c_master_write_noaddr8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_master_write_noaddr__i2c_id_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="i2c_8h_1a6a4cbb4478adeb5bfe8bfd872a3b56d7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_master\_write\_noaddr(i2c\_id\_t id, const uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   Write data to the I2C port from a given buffer and length without slave address, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **data** – pointer to the buffer
        - **size** – data length to write
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv418bk_i2c_master_read8i2c_id_t8uint32_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv318bk_i2c_master_read8i2c_id_t8uint32_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv218bk_i2c_master_read8i2c_id_t8uint32_tP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_master_read__i2c_id_t.uint32_t.uint8_tP.uint32_t.uint32_t"></a> <a id="i2c_8h_1a494ef80524cb8299959369b68e527988"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_master\_read(i2c\_id\_t id, uint32\_t dev\_addr, uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   I2C read data from I2C buffer, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **dev\_addr** – slave device address
        - **data** – pointer to the buffer
        - **size** – data length to read
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv425bk_i2c_master_read_noaddr8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv325bk_i2c_master_read_noaddr8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv225bk_i2c_master_read_noaddr8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_master_read_noaddr__i2c_id_t.uint8_tP.uint32_t.uint32_t"></a> <a id="i2c_8h_1a87123c2f1c44975f9fa7b15a96658576"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_master\_read\_noaddr(i2c\_id\_t id, uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   I2C read data from I2C buffer without slave address, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **data** – pointer to the buffer
        - **size** – data length to read
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv418bk_i2c_slave_write8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv318bk_i2c_slave_write8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv218bk_i2c_slave_write8i2c_id_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_slave_write__i2c_id_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="i2c_8h_1ad6b0bd4713f6a57d6a0bd763cef475aa"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_slave\_write(i2c\_id\_t id, const uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   Write data to the I2C port from a given buffer and length, It shall only be called in I2C slave mode.

    参数
    :   - **id** – I2C id
        - **data** – pointer to the buffer
        - **size** – data length to write
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv417bk_i2c_slave_read8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv317bk_i2c_slave_read8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv217bk_i2c_slave_read8i2c_id_tP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_i2c_slave_read__i2c_id_t.uint8_tP.uint32_t.uint32_t"></a> <a id="i2c_8h_1ad10549f4dce8d3f25fa7b33dfcf65602"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_slave\_read(i2c\_id\_t id, uint8\_t \*data, uint32\_t size, uint32\_t timeout\_ms)
:   I2C read data from I2C buffer, It shall only be called in I2C slave mode.

    参数
    :   - **id** – I2C id
        - **dev\_addr** – slave device address
        - **data** – pointer to the buffer
        - **size** – data length to read
        - **timeout\_ms** – timeout ms

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv419bk_i2c_memory_write8i2c_id_tPK15i2c_mem_param_t"></a>

<a id="_CPPv319bk_i2c_memory_write8i2c_id_tPK15i2c_mem_param_t"></a> <a id="_CPPv219bk_i2c_memory_write8i2c_id_tPK15i2c_mem_param_t"></a> <a id="bk_i2c_memory_write__i2c_id_t.i2c_mem_param_tCP"></a> <a id="i2c_8h_1af89f2793d0b32fc051cad0a4fa080b6e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_memory\_write(i2c\_id\_t id, const i2c\_mem\_param\_t \*mem\_param)
:   Write data to the specific memory address from a given buffer and length, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **mem\_param** – memory parameter

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C mem\_param is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv418bk_i2c_memory_read8i2c_id_tPK15i2c_mem_param_t"></a>

<a id="_CPPv318bk_i2c_memory_read8i2c_id_tPK15i2c_mem_param_t"></a> <a id="_CPPv218bk_i2c_memory_read8i2c_id_tPK15i2c_mem_param_t"></a> <a id="bk_i2c_memory_read__i2c_id_t.i2c_mem_param_tCP"></a> <a id="i2c_8h_1a11116a62d1d2a019bb9aab2a1c373860"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_memory\_read(i2c\_id\_t id, const i2c\_mem\_param\_t \*mem\_param)
:   I2C read data from I2C specific memory address, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id
        - **mem\_param** – memory parameter

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C mem\_param is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv420bk_i2c_set_baud_rate8i2c_id_t8uint32_t"></a>

<a id="_CPPv320bk_i2c_set_baud_rate8i2c_id_t8uint32_t"></a> <a id="_CPPv220bk_i2c_set_baud_rate8i2c_id_t8uint32_t"></a> <a id="bk_i2c_set_baud_rate__i2c_id_t.uint32_t"></a> <a id="i2c_8h_1a3255bcfc4c8c84c102eca9affcc55a89"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_set\_baud\_rate(i2c\_id\_t id, uint32\_t baud\_rate)
:   I2C set baud rate.

    参数
    :   - **id** – I2C id
        - **baud\_rate** – baud rate

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv424bk_i2c_set_slave_address8i2c_id_t8uint16_t"></a>

<a id="_CPPv324bk_i2c_set_slave_address8i2c_id_t8uint16_t"></a> <a id="_CPPv224bk_i2c_set_slave_address8i2c_id_t8uint16_t"></a> <a id="bk_i2c_set_slave_address__i2c_id_t.uint16_t"></a> <a id="i2c_8h_1a9403c85084322227737de7257a206e57"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_set\_slave\_address(i2c\_id\_t id, uint16\_t slave\_addr)
:   Set slave address when current role is i2c slave.

    参数
    :   - **id** – I2C id
        - **slave\_addr** – slave address

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - others: other errors.

<a id="_CPPv423bk_i2c_enable_interrupt8i2c_id_t"></a>

<a id="_CPPv323bk_i2c_enable_interrupt8i2c_id_t"></a> <a id="_CPPv223bk_i2c_enable_interrupt8i2c_id_t"></a> <a id="bk_i2c_enable_interrupt__i2c_id_t"></a> <a id="i2c_8h_1a4888dbd887d98a1890e461f644afbe11"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_enable\_interrupt(i2c\_id\_t id)
:   Enable I2C interrupt.

    参数
    :   **id** – I2C id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_i2c_disable_interrupt8i2c_id_t"></a>

<a id="_CPPv324bk_i2c_disable_interrupt8i2c_id_t"></a> <a id="_CPPv224bk_i2c_disable_interrupt8i2c_id_t"></a> <a id="bk_i2c_disable_interrupt__i2c_id_t"></a> <a id="i2c_8h_1ac4178ac94172dfbb7b0b5014290d0604"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_disable\_interrupt(i2c\_id\_t id)
:   Disable I2C interrupt.

    参数
    :   **id** – I2C id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_i2c_is_bus_busy8i2c_id_t"></a>

<a id="_CPPv318bk_i2c_is_bus_busy8i2c_id_t"></a> <a id="_CPPv218bk_i2c_is_bus_busy8i2c_id_t"></a> <a id="bk_i2c_is_bus_busy__i2c_id_t"></a> <a id="i2c_8h_1ab75e8269f42a7c4220abd7e9757c2a98"></a> bool bk\_i2c\_is\_bus\_busy(i2c\_id\_t id)
:   Check if I2C is busy.

    参数
    :   **id** – I2C id

    返回
    :   true: busy, false: not busy

<a id="_CPPv421bk_i2c_get_cur_action8i2c_id_t"></a>

<a id="_CPPv321bk_i2c_get_cur_action8i2c_id_t"></a> <a id="_CPPv221bk_i2c_get_cur_action8i2c_id_t"></a> <a id="bk_i2c_get_cur_action__i2c_id_t"></a> <a id="i2c_8h_1ae38d57ce673314ee8e50abd8a1918625"></a> uint32\_t bk\_i2c\_get\_cur\_action(i2c\_id\_t id)
:   Get i2c current action, such as start,stop,send write\_addr.

    参数
    :   **id** – I2C id

    返回
    :   i2c action

<a id="_CPPv421bk_i2c_timer_callbackiPv"></a>

<a id="_CPPv321bk_i2c_timer_callbackiPv"></a> <a id="_CPPv221bk_i2c_timer_callbackiPv"></a> <a id="bk_i2c_timer_callback__i.voidP"></a> <a id="i2c_8h_1a87a8aa8f706332fde445118f72c670f3"></a> void bk\_i2c\_timer\_callback(int id, void \*myTimer)
:   bk\_i2c\_timer\_callback

    This API set timer call back

    返回

<a id="_CPPv419bk_i2c_get_busstatei"></a>

<a id="_CPPv319bk_i2c_get_busstatei"></a> <a id="_CPPv219bk_i2c_get_busstatei"></a> <a id="bk_i2c_get_busstate__i"></a> <a id="i2c_8h_1a4392f74fc3d6db4bbd1e470cec098407"></a> uint8\_t bk\_i2c\_get\_busstate(int id)
:   bk\_i2c\_get\_busstate

    This API get bus status idle or busy

    返回
    :   - 1: idle
        - 0: busy.

<a id="_CPPv421bk_i2c_get_transstatei"></a>

<a id="_CPPv321bk_i2c_get_transstatei"></a> <a id="_CPPv221bk_i2c_get_transstatei"></a> <a id="bk_i2c_get_transstate__i"></a> <a id="i2c_8h_1af4b096bfd84615ac065bc236de40f9c1"></a> uint8\_t bk\_i2c\_get\_transstate(int id)
:   bk\_i2c\_get\_transstate

    This API get bus status idle or busy

    返回
    :   - 1: ok
        - 0: fail.

<a id="_CPPv414bk_i2c_init_v28i2c_id_tPK12i2c_config_t"></a>

<a id="_CPPv314bk_i2c_init_v28i2c_id_tPK12i2c_config_t"></a> <a id="_CPPv214bk_i2c_init_v28i2c_id_tPK12i2c_config_t"></a> <a id="bk_i2c_init_v2__i2c_id_t.i2c_config_tCP"></a> <a id="i2c_8h_1a7d7d71ca235420f1dcd273689b63caca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_init\_v2(i2c\_id\_t id, const i2c\_config\_t \*cfg)
:   Init the SIM I2C id.

    This API init the I2C id:

    - Power up the I2C id
    - Configure the I2C id clock
    - Map the I2C id to dedicated GPIO port
    - Set the I2C parameters
    - Start the I2C id

    **Attention**
    :   Multifunction GPIO initialization affects other functions

    参数
    :   - **id** – I2C id
        - **config** – I2C parameter settings

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C config paramter is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - others: other errors.

<a id="_CPPv416bk_i2c_deinit_v28i2c_id_t"></a>

<a id="_CPPv316bk_i2c_deinit_v28i2c_id_t"></a> <a id="_CPPv216bk_i2c_deinit_v28i2c_id_t"></a> <a id="bk_i2c_deinit_v2__i2c_id_t"></a> <a id="i2c_8h_1aa9e810e3b510ea83febba1bbd20e87a4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_deinit\_v2(i2c\_id\_t id)
:   Deinit the SIM I2C driver.

    This API free all resource related to I2C and disable I2C.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_i2c_memory_write_v28i2c_id_tPK15i2c_mem_param_t"></a>

<a id="_CPPv322bk_i2c_memory_write_v28i2c_id_tPK15i2c_mem_param_t"></a> <a id="_CPPv222bk_i2c_memory_write_v28i2c_id_tPK15i2c_mem_param_t"></a> <a id="bk_i2c_memory_write_v2__i2c_id_t.i2c_mem_param_tCP"></a> <a id="i2c_8h_1a57a07f6ce9a2490bda059156ec910afa"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_memory\_write\_v2(i2c\_id\_t id, const i2c\_mem\_param\_t \*mem\_param)
:   Write data to the specific memory address from a given buffer and length, It shall only be called in SIM I2C master mode.

    参数
    :   - **id** – I2C id
        - **mem\_param** – memory parameter

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C mem\_param is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.

<a id="_CPPv421bk_i2c_memory_read_v28i2c_id_tPK15i2c_mem_param_t"></a>

<a id="_CPPv321bk_i2c_memory_read_v28i2c_id_tPK15i2c_mem_param_t"></a> <a id="_CPPv221bk_i2c_memory_read_v28i2c_id_tPK15i2c_mem_param_t"></a> <a id="bk_i2c_memory_read_v2__i2c_id_t.i2c_mem_param_tCP"></a> <a id="i2c_8h_1a8709d8990703d449faf43ad42a86c92e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_i2c\_memory\_read\_v2(i2c\_id\_t id, const i2c\_mem\_param\_t \*mem\_param)
:   SIM I2C read data from I2C specific memory address, It shall only be called in SIM I2C master mode.

    参数
    :   - **id** – I2C id
        - **mem\_param** – memory parameter

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: I2C mem\_param is NULL
        - BK\_ERR\_I2C\_NOT\_INIT: I2C driver not init
        - BK\_ERR\_I2C\_INVALID\_ID: I2C id number is invalid
        - BK\_ERR\_I2C\_ID\_NOT\_INIT: I2C id not init
        - others: other errors.
