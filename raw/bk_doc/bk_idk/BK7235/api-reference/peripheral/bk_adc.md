# SARADC[](#saradc "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_adc.html "../../../../en/v1.5/api-reference/peripheral/bk_adc.html")

Beken chip supports get every adc channel value function for user.


## ADC API Status[](#adc-api-status "永久链接至标题")

| API | BK7235A | BK7235B | BK7235 |
| --- | --- | --- | --- |
| [`bk_adc_driver_init()`](#_CPPv418bk_adc_driver_initv "bk_adc_driver_init") | Y | Y | Y |
| `bk_adc_aquire()` | Y | Y | Y |
| [`bk_adc_release()`](#_CPPv414bk_adc_releasev "bk_adc_release") | Y | Y | Y |
| [`bk_adc_driver_deinit()`](#_CPPv420bk_adc_driver_deinitv "bk_adc_driver_deinit") | Y | Y | Y |
| [`bk_adc_init()`](#_CPPv411bk_adc_init10adc_chan_t "bk_adc_init") | Y | Y | Y |
| [`bk_adc_deinit()`](#_CPPv413bk_adc_deinit10adc_chan_t "bk_adc_deinit") | Y | Y | Y |
| [`bk_adc_start()`](#_CPPv412bk_adc_startv "bk_adc_start") | Y | Y | Y |
| [`bk_adc_stop()`](#_CPPv411bk_adc_stopv "bk_adc_stop") | Y | Y | Y |
| [`bk_adc_read_raw()`](#_CPPv415bk_adc_read_rawP8uint16_t8uint32_t8uint32_t "bk_adc_read_raw") | Y | Y | Y |
| [`bk_adc_read()`](#_CPPv411bk_adc_readP8uint16_t8uint32_t "bk_adc_read") | Y | Y | Y |
| [`bk_adc_register_isr()`](#_CPPv419bk_adc_register_isr9adc_isr_t8uint32_t "bk_adc_register_isr") | Y | Y | Y |
| [`bk_adc_set_clk()`](#_CPPv414bk_adc_set_clk13adc_src_clk_t8uint32_t "bk_adc_set_clk") | Y | Y | Y |
| [`bk_adc_set_channel()`](#_CPPv418bk_adc_set_channel10adc_chan_t "bk_adc_set_channel") | Y | Y | Y |
| [`bk_adc_set_sample_rate()`](#_CPPv422bk_adc_set_sample_rate8uint32_t "bk_adc_set_sample_rate") | Y | Y | Y |
| [`bk_adc_set_filter()`](#_CPPv417bk_adc_set_filter8uint32_t "bk_adc_set_filter") | Y | Y | Y |
| [`bk_adc_set_steady_time()`](#_CPPv422bk_adc_set_steady_time8uint32_t "bk_adc_set_steady_time") | Y | Y | Y |
| [`bk_adc_set_sample_cnt()`](#_CPPv421bk_adc_set_sample_cnt8uint32_t "bk_adc_set_sample_cnt") | Y | Y | Y |
| `bk_adc_enable_saturate()` | Y | Y | Y |
| `bk_adc_disable_saturate()` | Y | Y | Y |
| `bk_adc_set_saturate()` | Y | Y | Y |
| [`bk_adc_get_saturate()`](#_CPPv419bk_adc_get_saturateP19adc_saturate_mode_t "bk_adc_get_saturate") | Y | Y | Y |
| [`bk_adc_set_config()`](#_CPPv417bk_adc_set_configP12adc_config_t "bk_adc_set_config") | Y | Y | Y |
| [`bk_adc_set_mode()`](#_CPPv415bk_adc_set_mode10adc_mode_t "bk_adc_set_mode") | Y | Y | Y |
| [`bk_adc_get_mode()`](#_CPPv415bk_adc_get_modev "bk_adc_get_mode") | Y | Y | Y |


## ADC Channel Number[](#adc-channel-number "永久链接至标题")

| Capability | BK7235A | BK7235B | BK7235 |
| --- | --- | --- | --- |
| Channel Number | 6 | 6 | 6 |


## ADC API Reference[](#adc-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [adc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/adc.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/adc.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_driver_init(void)[](#_CPPv418bk_adc_driver_initv "永久链接至目标")
:   Init the ADC driver.

    This API init the resoure common to all ADC id:


    - Init ADC driver control memory


    **Attention**
    :   1. This API should be called before any other ADC APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_acquire(void)[](#_CPPv414bk_adc_acquirev "永久链接至目标")
:   lock the runing ADC channel

    This API lock ADC channel which is runing.

    参数
    :   **id** – ADC id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_release()[](#_CPPv414bk_adc_releasev "永久链接至目标")
:   release the runing ADC channel

    This API release ADC channel which is runing.

    参数
    :   **id** – ADC id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_driver_deinit(void)[](#_CPPv420bk_adc_driver_deinitv "永久链接至目标")
:   Deinit the ADC driver.

    This API free all resource related to ADC and power down all ADC.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_init([adc_chan_t](#_CPPv410adc_chan_t "adc_chan_t") adc_id)[](#_CPPv411bk_adc_init10adc_chan_t "永久链接至目标")
:   Init the ADC.

    This API init the ADC:


    - Power up the ADC

    - Map the ADC id to dedicated GPIO port

    - Set adc work channel

    参数
    :   - **id** – ADC channel

        - **size** – ADC recieve data size

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_NOT_INIT: ADC driver not init

        - BK_ERR_ADC_INVALID_ID: ADC id is invalid

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_deinit([adc_chan_t](#_CPPv410adc_chan_t "adc_chan_t") id)[](#_CPPv413bk_adc_deinit10adc_chan_t "永久链接至目标")
:   Deinit the ADC id.

    This API deinit the ADC id:


    - Stop the ADC

    - Disable the ADC id interrupt

    - Power down the ADC

    - Unmap gpio id


    **Attention**
    :   1. This API should be called before use adc.

    参数
    :   **id** – ADC id

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_NOT_INIT: ADC driver not init

        - BK_ERR_ADC_INVALID_ID: ADC id is invalid

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_start(void)[](#_CPPv412bk_adc_startv "永久链接至目标")
:   Start the ADC.

    This API start adc:


    - enable the ADC id interrupt

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_BUSY: ADC is busy

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_stop(void)[](#_CPPv411bk_adc_stopv "永久链接至目标")
:   Stop the ADC.

    This API stop adc:


    - disable the ADC en bit

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_BUSY: ADC is busy

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_read_raw(uint16_t *read_buf, uint32_t size, uint32_t timeout)[](#_CPPv415bk_adc_read_rawP8uint16_t8uint32_t8uint32_t "永久链接至目标")
:   Start read the raw ADC data.


    **Attention**
    :   1. The read_buf is in unit of uint16_t, the application needs to malloc (size * 2) bytes for read_buf.

        2. The maximum value of size is CONFIG_ADC_BUF_SIZE, if the size exceeds CONFIG_ADC_BUF_SIZE, the API returns BK_ERR_ADC_SIZE_TOO_BIG.

    参数
    :   - **read_buf** – application malloc buffer which save the current adc value

        - **size** – the size of read_buf, the unit of size is uint16_t

        - **timeout** – adc read semaphore timeout

    返回
    :   - BK_ERR_ADC_BUSY: ADC is busy

        - BK_ERR_ADC_INVALID_MODE: ADC mode is invalid

        - BK_ERR_ADC_SIZE_TOO_BIG: size is too big

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_read(uint16_t *data, uint32_t timeout)[](#_CPPv411bk_adc_readP8uint16_t8uint32_t "永久链接至目标")
:   Start read the average value of sampling data.


    - BK_ERR_ADC_BUSY: ADC is busy

    - BK_ERR_ADC_INVALID_MODE: ADC mode is invalid

    - others: other errors.

    参数
    :   - **data** – store the average value of all sample values in ADC software buffers

        - **timeout** – adc read semaphore timeout

    返回

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_register_isr([adc_isr_t](#_CPPv49adc_isr_t "adc_isr_t") isr, uint32_t param)[](#_CPPv419bk_adc_register_isr9adc_isr_t8uint32_t "永久链接至目标")
:   Register the adc interrupt service routine.

    参数
    :   - **isr** – ADC intterrupt callback

        - **param** – ADC sample data size which depend on user

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_NOT_INIT: adc not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_clk([adc_src_clk_t](#_CPPv413adc_src_clk_t "adc_src_clk_t") src_clk, uint32_t clk)[](#_CPPv414bk_adc_set_clk13adc_src_clk_t8uint32_t "永久链接至目标")
:   set ADC source clock and work frequence

    This API set adc clock source and frequence

    参数
    :   - **src_clk** – adc source clock

        - **clk** – adc work clock :adc clk

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_INVALID_SCLK_MODE: ADC source clock is invalid

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_channel([adc_chan_t](#_CPPv410adc_chan_t "adc_chan_t") adc_id)[](#_CPPv418bk_adc_set_channel10adc_chan_t "永久链接至目标")
:   set ADC work channel

    This API set adc work channel

    参数
    :   **adc_id** – adc channel

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_INVALID_ID: ADC invalid id

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_sample_rate(uint32_t sample_rate)[](#_CPPv422bk_adc_set_sample_rate8uint32_t "永久链接至目标")
:   set ADC sample rate

    This API set adc work sample rate, period = (16 + sample_rate)*adc_clk mcu output 16 adc_clks every period

    参数
    :   **sample_rate** – adc sample rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_filter(uint32_t filter)[](#_CPPv417bk_adc_set_filter8uint32_t "永久链接至目标")
:   set ADC filter

    This API set adc filter, the value default < 64, data output rate = period/(filter + 1)

    参数
    :   **filter** – adc filter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_steady_time(uint32_t steady_ctrl)[](#_CPPv422bk_adc_set_steady_time8uint32_t "永久链接至目标")
:   set ADC steady time

    This API set adc filter, adc wait (steady_ctrl +1)*8 adc_clks to send valid

    参数
    :   **steady_ctrl** – adc steady time

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_sample_cnt(uint32_t cnt)[](#_CPPv421bk_adc_set_sample_cnt8uint32_t "永久链接至目标")
:   set ADC sample cnt

    This API sets ADC sample cnt per-interrupt, the ADC raises the interrupt when every time it samples number of cnt times. The maximum value of cnt is 32.

    参数
    :   **cnt** – per-interrupt sample cnt

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_saturate_mode([adc_saturate_mode_t](#_CPPv419adc_saturate_mode_t "adc_saturate_mode_t") mode)[](#_CPPv424bk_adc_set_saturate_mode19adc_saturate_mode_t "永久链接至目标")
:   set adc saturate

    This API set adc saturate, auto process adc fifo data in cpu ,just get the data from reg ADC_DATA_16

    参数
    :   **mode** – adc saturate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_get_saturate([adc_saturate_mode_t](#_CPPv419adc_saturate_mode_t "adc_saturate_mode_t") *mode)[](#_CPPv419bk_adc_get_saturateP19adc_saturate_mode_t "永久链接至目标")
:   get adc saturate

    This API get adc saturate

    返回
    :   - adc_saturate_mode_t: adc saturate mode

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_enable_bypass_clalibration(void)[](#_CPPv433bk_adc_enable_bypass_clalibrationv "永久链接至目标")
:   enable ADC bypass calibration

    返回
    :   - BK_OK: succeed

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_disable_bypass_clalibration(void)[](#_CPPv434bk_adc_disable_bypass_clalibrationv "永久链接至目标")
:   disable ADC bypass calibration

    返回
    :   - BK_OK: succeed

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_config([adc_config_t](#_CPPv412adc_config_t "adc_config_t") *config)[](#_CPPv417bk_adc_set_configP12adc_config_t "永久链接至目标")
:   adc set config

    This API config adc params

    参数
    :   **config** – adc parameter settings

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM : param is null

        - BK_ERR_ADC_INVALID_MODE:adc invalid mode

        - BK_ERR_ADC_INVALID_SCLK_MODE: ADC source clock is invalid

        - BK_ERR_ADC_INVALID_ID: ADC id is invalid

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_adc_set_mode([adc_mode_t](#_CPPv410adc_mode_t "adc_mode_t") adc_mode)[](#_CPPv415bk_adc_set_mode10adc_mode_t "永久链接至目标")
:   adc set mode

    This API config adc mode

    参数
    :   **mode** – : adc mode:


        - 0: sleep mode: adc is power down in this mode

        - 1: single step mode: adc finish sample data convesion once after enable adc and wait mcu to read sample data. The mode will turn to sleep mode after mcu read this sample date It must be enabled again when you want to sample next data.

        - 2: software control mode: adc gengerate interrupt after sample data convesion wait mcu to read sample data. adc will convert sample data after mcu reading this sample date from data register and software cleaning int flag.

        - 3: continous mode:adc wait adc_setting time to sample data, and generate int flag after finish sample data convesion, then always repeat last sample way. This mode don’t depend on muc reading data register.

    返回
    :   - BK_OK: succeed

        - BK_ERR_ADC_INVALID_MODE:adc invalid mode

        - others: other errors.

[adc_mode_t](#_CPPv410adc_mode_t "adc_mode_t") bk_adc_get_mode(void)[](#_CPPv415bk_adc_get_modev "永久链接至目标")
:   get adc mode

    This API get adc work mode

    返回
    :   - adc_mode_t: adc_mode


## ADC API Typedefs[](#adc-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [adc_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/adc_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/adc_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_ADC_NOT_INIT[](#c.BK_ERR_ADC_NOT_INIT "永久链接至目标")
:   ADC driver not init

BK_ERR_ADC_INVALID_CHAN[](#c.BK_ERR_ADC_INVALID_CHAN "永久链接至目标")
:   ADC chan number is invalid

BK_ERR_ADC_BUSY[](#c.BK_ERR_ADC_BUSY "永久链接至目标")
:   ADC channel is busy

BK_ERR_ADC_INVALID_MODE[](#c.BK_ERR_ADC_INVALID_MODE "永久链接至目标")
:   ADC invalid mode

BK_ERR_ADC_CHAN_NOT_INIT[](#c.BK_ERR_ADC_CHAN_NOT_INIT "永久链接至目标")
:   ADC chan not init

BK_ERR_ADC_INVALID_SCLK_MODE[](#c.BK_ERR_ADC_INVALID_SCLK_MODE "永久链接至目标")
:   ADC no such source clock

BK_ERR_ADC_INIT_MUTEX[](#c.BK_ERR_ADC_INIT_MUTEX "永久链接至目标")
:   ADC mutex lock

BK_ERR_ADC_GET_READ_SEMA[](#c.BK_ERR_ADC_GET_READ_SEMA "永久链接至目标")
:   ADC get semaphore error

BK_ERR_ADC_INIT_READ_SEMA[](#c.BK_ERR_ADC_INIT_READ_SEMA "永久链接至目标")
:   ADC read data error

BK_ERR_ADC_SIZE_TOO_BIG[](#c.BK_ERR_ADC_SIZE_TOO_BIG "永久链接至目标")
:   ADC read size is bigger than adc driver buffer size

CONFIG_ADC_BUF_SIZE[](#c.CONFIG_ADC_BUF_SIZE "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*adc_isr_t)(uint32_t param)[](#_CPPv49adc_isr_t "永久链接至目标")
:   ADC interrupt service routine.


### Header File[](#id2 "永久链接至标题")


- [hal/hal_adc_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_adc_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_adc_types.h")


### Structures[](#structures "永久链接至标题")

struct adc_config_t[](#_CPPv412adc_config_t "永久链接至目标")
:   Public Members

    uint32_t clk[](#_CPPv4N12adc_config_t3clkE "永久链接至目标")
    :   ADC sample clock division: adc_clk=clk/[2*(pre_div +1)]

    uint32_t sample_rate[](#_CPPv4N12adc_config_t11sample_rateE "永久链接至目标")
    :   ADC sample rate, every period ouput 16 adc_clks in continuous mode period = (16+samp_rate)*adc_clk

    uint32_t adc_filter[](#_CPPv4N12adc_config_t10adc_filterE "永久链接至目标")
    :   ADC filter: the output data rate = period/(adc_filter +1)

    uint32_t steady_ctrl[](#_CPPv4N12adc_config_t11steady_ctrlE "永久链接至目标")
    :   ADC steady_ctrl : steady time = (steady_ctrl +1)*8 adc_clk

    [adc_mode_t](#_CPPv410adc_mode_t "adc_mode_t") adc_mode[](#_CPPv4N12adc_config_t8adc_modeE "永久链接至目标")
    :   ADC mode set

    [adc_src_clk_t](#_CPPv413adc_src_clk_t "adc_src_clk_t") src_clk[](#_CPPv4N12adc_config_t7src_clkE "永久链接至目标")
    :   ADC source clcok choose

    [adc_chan_t](#_CPPv410adc_chan_t "adc_chan_t") chan[](#_CPPv4N12adc_config_t4chanE "永久链接至目标")
    :   ADC work channel

    [adc_saturate_mode_t](#_CPPv419adc_saturate_mode_t "adc_saturate_mode_t") saturate_mode[](#_CPPv4N12adc_config_t13saturate_modeE "永久链接至目标")
    :   ADC saturate_mode

    uint32_t is_open[](#_CPPv4N12adc_config_t7is_openE "永久链接至目标")
    :   ADC channel is open or not

    uint16_t *output_buf[](#_CPPv4N12adc_config_t10output_bufE "永久链接至目标")
    :   ADC channel output buffer

    int32_t output_buf_len[](#_CPPv4N12adc_config_t14output_buf_lenE "永久链接至目标")
    :   ADC channel output buffer length

struct adc_gpio_map_t[](#_CPPv414adc_gpio_map_t "永久链接至目标")


### Macros[](#id3 "永久链接至标题")

CONFIG_ADC_STATIS[](#c.CONFIG_ADC_STATIS "永久链接至目标")

ADC_ACURACY_10_BIT[](#c.ADC_ACURACY_10_BIT "永久链接至目标")

ADC_ACURACY_12_BIT[](#c.ADC_ACURACY_12_BIT "永久链接至目标")

ADC_READ_SEMAPHORE_WAIT_TIME[](#c.ADC_READ_SEMAPHORE_WAIT_TIME "永久链接至目标")

ADC_SRC_DCO_CLK[](#c.ADC_SRC_DCO_CLK "永久链接至目标")

ADC_SRC_DPLL_CLK[](#c.ADC_SRC_DPLL_CLK "永久链接至目标")

ADC_SRC_26M_CLK[](#c.ADC_SRC_26M_CLK "永久链接至目标")

ADC_SRC_32M_CLK[](#c.ADC_SRC_32M_CLK "永久链接至目标")

ADC_FIFO_LEVEL_MAX[](#c.ADC_FIFO_LEVEL_MAX "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum adc_src_clk_t[](#_CPPv413adc_src_clk_t "永久链接至目标")
:   *Values:*

    enumerator ADC_SCLK_DCO[](#_CPPv4N13adc_src_clk_t12ADC_SCLK_DCOE "永久链接至目标")
    :   ADC source clock dco

    enumerator ADC_SCLK_XTAL_26M[](#_CPPv4N13adc_src_clk_t17ADC_SCLK_XTAL_26ME "永久链接至目标")
    :   ADC source clock xtal 26M

    enumerator ADC_SCLK_DPLL[](#_CPPv4N13adc_src_clk_t13ADC_SCLK_DPLLE "永久链接至目标")
    :   ADC source clock dpll

    enumerator ADC_SCLK_32M[](#_CPPv4N13adc_src_clk_t12ADC_SCLK_32ME "永久链接至目标")
    :   ADC source clock 32M

    enumerator ADC_SCLK_NONE[](#_CPPv4N13adc_src_clk_t13ADC_SCLK_NONEE "永久链接至目标")
    :   ADC has not such source clock

enum adc_mode_t[](#_CPPv410adc_mode_t "永久链接至目标")
:   *Values:*

    enumerator ADC_SLEEP_MODE[](#_CPPv4N10adc_mode_t14ADC_SLEEP_MODEE "永久链接至目标")
    :   ADC sleep mode

    enumerator ADC_SINGLE_STEP_MODE[](#_CPPv4N10adc_mode_t20ADC_SINGLE_STEP_MODEE "永久链接至目标")
    :   ADC single step mode

    enumerator ADC_SOFTWARE_CONTRL_MODE[](#_CPPv4N10adc_mode_t24ADC_SOFTWARE_CONTRL_MODEE "永久链接至目标")
    :   ADC software control mode

    enumerator ADC_CONTINUOUS_MODE[](#_CPPv4N10adc_mode_t19ADC_CONTINUOUS_MODEE "永久链接至目标")
    :   ADC continuous mode

    enumerator ADC_NONE_MODE[](#_CPPv4N10adc_mode_t13ADC_NONE_MODEE "永久链接至目标")

enum adc_chan_t[](#_CPPv410adc_chan_t "永久链接至目标")
:   *Values:*

    enumerator ADC_1[](#_CPPv4N10adc_chan_t5ADC_1E "永久链接至目标")

    enumerator ADC_2[](#_CPPv4N10adc_chan_t5ADC_2E "永久链接至目标")

    enumerator ADC_3[](#_CPPv4N10adc_chan_t5ADC_3E "永久链接至目标")

    enumerator ADC_4[](#_CPPv4N10adc_chan_t5ADC_4E "永久链接至目标")

    enumerator ADC_5[](#_CPPv4N10adc_chan_t5ADC_5E "永久链接至目标")

    enumerator ADC_6[](#_CPPv4N10adc_chan_t5ADC_6E "永久链接至目标")

    enumerator ADC_7[](#_CPPv4N10adc_chan_t5ADC_7E "永久链接至目标")

    enumerator ADC_8[](#_CPPv4N10adc_chan_t5ADC_8E "永久链接至目标")

    enumerator ADC_9[](#_CPPv4N10adc_chan_t5ADC_9E "永久链接至目标")

    enumerator ADC_10[](#_CPPv4N10adc_chan_t6ADC_10E "永久链接至目标")

    enumerator ADC_11[](#_CPPv4N10adc_chan_t6ADC_11E "永久链接至目标")

    enumerator ADC_12[](#_CPPv4N10adc_chan_t6ADC_12E "永久链接至目标")

    enumerator ADC_13[](#_CPPv4N10adc_chan_t6ADC_13E "永久链接至目标")

    enumerator ADC_MAX[](#_CPPv4N10adc_chan_t7ADC_MAXE "永久链接至目标")

enum adc_saturate_mode_t[](#_CPPv419adc_saturate_mode_t "永久链接至目标")
:   *Values:*

    enumerator ADC_SATURATE_MODE_NONE[](#_CPPv4N19adc_saturate_mode_t22ADC_SATURATE_MODE_NONEE "永久链接至目标")

    enumerator ADC_SATURATE_MODE_0[](#_CPPv4N19adc_saturate_mode_t19ADC_SATURATE_MODE_0E "永久链接至目标")

    enumerator ADC_SATURATE_MODE_1[](#_CPPv4N19adc_saturate_mode_t19ADC_SATURATE_MODE_1E "永久链接至目标")

    enumerator ADC_SATURATE_MODE_2[](#_CPPv4N19adc_saturate_mode_t19ADC_SATURATE_MODE_2E "永久链接至目标")

    enumerator ADC_SATURATE_MODE_3[](#_CPPv4N19adc_saturate_mode_t19ADC_SATURATE_MODE_3E "永久链接至目标")
