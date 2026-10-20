---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/adc.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="adc-api"></a>

# ADC API

ADC (Analog-to-Digital Converter) 模数转换器API接口。

<a id="header-file"></a>

## Header File

- [adc.h](https://github.com/bekencorp/armino/blob/main/components/adc.h)

<a id="functions"></a>

## Functions

<a id="_CPPv418bk_adc_driver_initv"></a>

<a id="_CPPv318bk_adc_driver_initv"></a> <a id="_CPPv218bk_adc_driver_initv"></a> <a id="bk_adc_driver_init__void"></a> <a id="group__bk__api__adc_1ga684e48484c76e3b06cb958deab3bb31c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_driver\_init(void)
:   Init the ADC driver.

    This API init the resoure common to all ADC id:

    - Init ADC driver control memory

    **Attention**
    :   1\. This API should be called before any other ADC APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414bk_adc_acquirev"></a>

<a id="_CPPv314bk_adc_acquirev"></a> <a id="_CPPv214bk_adc_acquirev"></a> <a id="bk_adc_acquire__void"></a> <a id="group__bk__api__adc_1gad5680a6994fc0fb9d511b99ddbaf413a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_acquire(void)
:   lock the runing ADC channel

    This API lock ADC channel which is runing.

    参数
    :   **id** – ADC id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414bk_adc_releasev"></a>

<a id="_CPPv314bk_adc_releasev"></a> <a id="_CPPv214bk_adc_releasev"></a> <a id="bk_adc_release"></a> <a id="group__bk__api__adc_1ga64ed3c9fd2993162237fcbfd5ece8938"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_release()
:   release the runing ADC channel

    This API release ADC channel which is runing.

    参数
    :   **id** – ADC id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_adc_driver_deinitv"></a>

<a id="_CPPv320bk_adc_driver_deinitv"></a> <a id="_CPPv220bk_adc_driver_deinitv"></a> <a id="bk_adc_driver_deinit__void"></a> <a id="group__bk__api__adc_1ga1cab56766442da4369c77b089f07ef9b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_driver\_deinit(void)
:   Deinit the ADC driver.

    This API free all resource related to ADC and power down all ADC.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_adc_init10adc_chan_t"></a>

<a id="_CPPv311bk_adc_init10adc_chan_t"></a> <a id="_CPPv211bk_adc_init10adc_chan_t"></a> <a id="bk_adc_init__adc_chan_t"></a> <a id="group__bk__api__adc_1ga99c945973b47e3eca9edc063e174cc7f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_init(adc\_chan\_t adc\_id)
:   Init the ADC.

    This API init the ADC:

    - Power up the ADC
    - Map the ADC id to dedicated GPIO port
    - Set adc work channel

    参数
    :   - **id** – ADC channel
        - **size** – ADC recieve data size

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_NOT\_INIT: ADC driver not init
        - BK\_ERR\_ADC\_INVALID\_ID: ADC id is invalid
        - others: other errors.

<a id="_CPPv413bk_adc_deinit10adc_chan_t"></a>

<a id="_CPPv313bk_adc_deinit10adc_chan_t"></a> <a id="_CPPv213bk_adc_deinit10adc_chan_t"></a> <a id="bk_adc_deinit__adc_chan_t"></a> <a id="group__bk__api__adc_1ga23b94dc65f032ae17da87e868aec3f04"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_deinit(adc\_chan\_t id)
:   Deinit the ADC id.

    This API deinit the ADC id:

    - Stop the ADC
    - Disable the ADC id interrupt
    - Power down the ADC
    - Unmap gpio id

    **Attention**
    :   1\. This API should be called before use adc.

    参数
    :   **id** – ADC id

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_NOT\_INIT: ADC driver not init
        - BK\_ERR\_ADC\_INVALID\_ID: ADC id is invalid
        - others: other errors.

<a id="_CPPv412bk_adc_startv"></a>

<a id="_CPPv312bk_adc_startv"></a> <a id="_CPPv212bk_adc_startv"></a> <a id="bk_adc_start__void"></a> <a id="group__bk__api__adc_1ga252d590fe1c9e9e5718c65a31f8c4559"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_start(void)
:   Start the ADC.

    This API start adc:

    - enable the ADC id interrupt

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_BUSY: ADC is busy
        - others: other errors.

<a id="_CPPv411bk_adc_stopv"></a>

<a id="_CPPv311bk_adc_stopv"></a> <a id="_CPPv211bk_adc_stopv"></a> <a id="bk_adc_stop__void"></a> <a id="group__bk__api__adc_1gaa9fd8fac599692028959169fc54768ad"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_stop(void)
:   Stop the ADC.

    This API stop adc:

    - disable the ADC en bit

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_BUSY: ADC is busy
        - others: other errors.

<a id="_CPPv415bk_adc_read_rawP8uint16_t8uint32_t8uint32_t"></a>

<a id="_CPPv315bk_adc_read_rawP8uint16_t8uint32_t8uint32_t"></a> <a id="_CPPv215bk_adc_read_rawP8uint16_t8uint32_t8uint32_t"></a> <a id="bk_adc_read_raw__uint16_tP.uint32_t.uint32_t"></a> <a id="group__bk__api__adc_1ga810b203a3974846f6f68e84358aa6e35"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_read\_raw(uint16\_t \*read\_buf, uint32\_t size, uint32\_t timeout)
:   Start read the raw ADC data in continuous mode.

    **Attention**
    :   1\. The read\_buf is in unit of uint16\_t, the application needs to malloc (size \* 2\) bytes for read\_buf.

    **Attention**
    :   2\. The maximum value of size is CONFIG\_ADC\_BUF\_SIZE, if the size exceeds CONFIG\_ADC\_BUF\_SIZE, the API returns BK\_ERR\_ADC\_SIZE\_TOO\_BIG.

    参数
    :   - **read\_buf** – application malloc buffer which save the current adc value
        - **size** – the size of read\_buf, the unit of size is uint16\_t
        - **timeout** – adc read semaphore timeout

    返回
    :   - BK\_ERR\_ADC\_BUSY: ADC is busy
        - BK\_ERR\_ADC\_INVALID\_MODE: ADC mode is invalid
        - BK\_ERR\_ADC\_SIZE\_TOO\_BIG: size is too big
        - others: other errors.

<a id="_CPPv423bk_adc_read_raw_pollingP8uint16_t8uint32_t8uint32_t"></a>

<a id="_CPPv323bk_adc_read_raw_pollingP8uint16_t8uint32_t8uint32_t"></a> <a id="_CPPv223bk_adc_read_raw_pollingP8uint16_t8uint32_t8uint32_t"></a> <a id="bk_adc_read_raw_polling__uint16_tP.uint32_t.uint32_t"></a> <a id="group__bk__api__adc_1ga225f4dbb2bdddd85fe1e2c81a3532338"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_read\_raw\_polling(uint16\_t \*read\_buf, uint32\_t size, uint32\_t timeout)
:   Start read the raw ADC data in polling mode.

    **Attention**
    :   1\. The read\_buf is in unit of uint16\_t, the application needs to malloc (size \* 2\) bytes for read\_buf.

    **Attention**
    :   2\. This API reads ADC FIFO by polling and does not depend on ISR or semaphore notification.

    参数
    :   - **read\_buf** – application malloc buffer which save the current adc value
        - **size** – the size of read\_buf, the unit of size is uint16\_t
        - **timeout** – adc polling timeout in milliseconds

    返回
    :   - BK\_ERR\_ADC\_BUSY: ADC is busy
        - BK\_ERR\_ADC\_INVALID\_MODE: ADC mode is invalid
        - others: other errors.

<a id="_CPPv418bk_adc_single_readP8uint16_t"></a>

<a id="_CPPv318bk_adc_single_readP8uint16_t"></a> <a id="_CPPv218bk_adc_single_readP8uint16_t"></a> <a id="bk_adc_single_read__uint16_tP"></a> <a id="group__bk__api__adc_1ga9431bd97e046ab34eba81c146d7fdf59"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_single\_read(uint16\_t \*data)
:   Start read the raw ADC data in single mode.

    参数
    :   **data** – ADC sample data

    返回
    :   - BK\_OK: success.

<a id="_CPPv411bk_adc_readP8uint16_t8uint32_t"></a>

<a id="_CPPv311bk_adc_readP8uint16_t8uint32_t"></a> <a id="_CPPv211bk_adc_readP8uint16_t8uint32_t"></a> <a id="bk_adc_read__uint16_tP.uint32_t"></a> <a id="group__bk__api__adc_1ga648053302fa9186907fc723c77b3f17f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_read(uint16\_t \*data, uint32\_t timeout)
:   Start read the average value of sampling data.

    - BK\_ERR\_ADC\_BUSY: ADC is busy
    - BK\_ERR\_ADC\_INVALID\_MODE: ADC mode is invalid
    - others: other errors.

    参数
    :   - **data** – store the average value of all sample values in ADC software buffers
        - **timeout** – adc read semaphore timeout

    返回

<a id="_CPPv419bk_adc_register_isr9adc_isr_t8uint32_t"></a>

<a id="_CPPv319bk_adc_register_isr9adc_isr_t8uint32_t"></a> <a id="_CPPv219bk_adc_register_isr9adc_isr_t8uint32_t"></a> <a id="bk_adc_register_isr__adc_isr_t.uint32_t"></a> <a id="group__bk__api__adc_1ga127f9b2b6913c420df064aa8f35dd679"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_register\_isr(adc\_isr\_t isr, uint32\_t param)
:   Register the adc interrupt service routine.

    参数
    :   - **isr** – ADC intterrupt callback
        - **param** – ADC sample data size which depend on user

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_NOT\_INIT: adc not init
        - others: other errors.

<a id="_CPPv428bk_adc_register_isr_callback9adc_isr_t8uint32_t"></a>

<a id="_CPPv328bk_adc_register_isr_callback9adc_isr_t8uint32_t"></a> <a id="_CPPv228bk_adc_register_isr_callback9adc_isr_t8uint32_t"></a> <a id="bk_adc_register_isr_callback__adc_isr_t.uint32_t"></a> <a id="group__bk__api__adc_1ga1abef073411796bbbd2ae66740f41892"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_register\_isr\_callback(adc\_isr\_t isr, uint32\_t param)
:   Register the adc interrupt service routine.

    参数
    :   - **isr** – ADC intterrupt callback
        - **param** – ADC sample data size which depend on user

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_NOT\_INIT: adc not init
        - others: other errors.

<a id="_CPPv414bk_adc_set_clk13adc_src_clk_t8uint32_t"></a>

<a id="_CPPv314bk_adc_set_clk13adc_src_clk_t8uint32_t"></a> <a id="_CPPv214bk_adc_set_clk13adc_src_clk_t8uint32_t"></a> <a id="bk_adc_set_clk__adc_src_clk_t.uint32_t"></a> <a id="group__bk__api__adc_1ga6b62c0998f5a21a36e3b5d6e6a430b09"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_clk(adc\_src\_clk\_t src\_clk, uint32\_t clk)
:   set ADC source clock and work frequence

    This API set adc clock source and frequence

    参数
    :   - **src\_clk** – adc source clock
        - **clk** – adc work clock :adc clk

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_INVALID\_SCLK\_MODE: ADC source clock is invalid
        - others: other errors.

<a id="_CPPv418bk_adc_set_channel10adc_chan_t"></a>

<a id="_CPPv318bk_adc_set_channel10adc_chan_t"></a> <a id="_CPPv218bk_adc_set_channel10adc_chan_t"></a> <a id="bk_adc_set_channel__adc_chan_t"></a> <a id="group__bk__api__adc_1ga6bbf3cfb04b3864819eb8a85c325954e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_channel(adc\_chan\_t adc\_id)
:   set ADC work channel

    This API set adc work channel

    参数
    :   **adc\_id** – adc channel

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_INVALID\_ID: ADC invalid id
        - others: other errors.

<a id="_CPPv422bk_adc_set_sample_rate8uint32_t"></a>

<a id="_CPPv322bk_adc_set_sample_rate8uint32_t"></a> <a id="_CPPv222bk_adc_set_sample_rate8uint32_t"></a> <a id="bk_adc_set_sample_rate__uint32_t"></a> <a id="group__bk__api__adc_1ga8968ce1f7c61824cfdb967cddc3478f1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_sample\_rate(uint32\_t sample\_rate)
:   set ADC sample rate

    This API set adc work sample rate, period \= (16 \+ sample\_rate)\*adc\_clk mcu output 16 adc\_clks every period

    参数
    :   **sample\_rate** – adc sample rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_adc_set_filter8uint32_t"></a>

<a id="_CPPv317bk_adc_set_filter8uint32_t"></a> <a id="_CPPv217bk_adc_set_filter8uint32_t"></a> <a id="bk_adc_set_filter__uint32_t"></a> <a id="group__bk__api__adc_1ga51e961413bd4719c4c5986dad53841ca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_filter(uint32\_t filter)
:   set ADC filter

    This API set adc filter, the value default \< 64, data output rate \= period/(filter \+ 1\)

    参数
    :   **filter** – adc filter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_adc_set_steady_time8uint32_t"></a>

<a id="_CPPv322bk_adc_set_steady_time8uint32_t"></a> <a id="_CPPv222bk_adc_set_steady_time8uint32_t"></a> <a id="bk_adc_set_steady_time__uint32_t"></a> <a id="group__bk__api__adc_1ga313e473f2d3e33d19e6378ba095c6122"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_steady\_time(uint32\_t steady\_ctrl)
:   set ADC steady time

    This API set adc filter, adc wait (steady\_ctrl \+1)\*8 adc\_clks to send valid

    参数
    :   **steady\_ctrl** – adc steady time

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_adc_set_sample_cnt8uint32_t"></a>

<a id="_CPPv321bk_adc_set_sample_cnt8uint32_t"></a> <a id="_CPPv221bk_adc_set_sample_cnt8uint32_t"></a> <a id="bk_adc_set_sample_cnt__uint32_t"></a> <a id="group__bk__api__adc_1gaa8eca5b05e2e634defd34861c3475c7f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_sample\_cnt(uint32\_t cnt)
:   set ADC sample cnt

    This API sets ADC sample cnt per-interrupt, the ADC raises the interrupt when every time it samples number of cnt times. The maximum value of cnt is 32\.

    参数
    :   **cnt** – per-interrupt sample cnt

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_adc_set_saturate_mode19adc_saturate_mode_t"></a>

<a id="_CPPv324bk_adc_set_saturate_mode19adc_saturate_mode_t"></a> <a id="_CPPv224bk_adc_set_saturate_mode19adc_saturate_mode_t"></a> <a id="bk_adc_set_saturate_mode__adc_saturate_mode_t"></a> <a id="group__bk__api__adc_1ga76871725d13d595bb993ad31ecc0e855"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_saturate\_mode(adc\_saturate\_mode\_t mode)
:   set adc saturate

    This API set adc saturate, auto process adc fifo data in cpu ,just get the data from reg ADC\_DATA\_16

    参数
    :   **mode** – adc saturate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_adc_get_saturateP19adc_saturate_mode_t"></a>

<a id="_CPPv319bk_adc_get_saturateP19adc_saturate_mode_t"></a> <a id="_CPPv219bk_adc_get_saturateP19adc_saturate_mode_t"></a> <a id="bk_adc_get_saturate__adc_saturate_mode_tP"></a> <a id="group__bk__api__adc_1gad7b6ea9ea20167759fd1713ab4275dbc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_get\_saturate(adc\_saturate\_mode\_t \*mode)
:   get adc saturate

    This API get adc saturate

    返回
    :   - adc\_saturate\_mode\_t: adc saturate mode

<a id="_CPPv433bk_adc_enable_bypass_clalibrationv"></a>

<a id="_CPPv333bk_adc_enable_bypass_clalibrationv"></a> <a id="_CPPv233bk_adc_enable_bypass_clalibrationv"></a> <a id="bk_adc_enable_bypass_clalibration__void"></a> <a id="group__bk__api__adc_1ga0657e69221bb57e9c10af2b6ce929899"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_enable\_bypass\_clalibration(void)
:   enable ADC bypass calibration

    返回
    :   - BK\_OK: succeed

<a id="_CPPv434bk_adc_disable_bypass_clalibrationv"></a>

<a id="_CPPv334bk_adc_disable_bypass_clalibrationv"></a> <a id="_CPPv234bk_adc_disable_bypass_clalibrationv"></a> <a id="bk_adc_disable_bypass_clalibration__void"></a> <a id="group__bk__api__adc_1ga41d941cee2d5a3461e37baeb4f0b1272"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_disable\_bypass\_clalibration(void)
:   disable ADC bypass calibration

    返回
    :   - BK\_OK: succeed

<a id="_CPPv417bk_adc_set_configP12adc_config_t"></a>

<a id="_CPPv317bk_adc_set_configP12adc_config_t"></a> <a id="_CPPv217bk_adc_set_configP12adc_config_t"></a> <a id="bk_adc_set_config__adc_config_tP"></a> <a id="group__bk__api__adc_1ga90a99d57dfe3020a02fb9d9e96f2c6db"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_config(adc\_config\_t \*config)
:   adc set config

    This API config adc params

    参数
    :   **config** – adc parameter settings

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM : param is null
        - BK\_ERR\_ADC\_INVALID\_MODE:adc invalid mode
        - BK\_ERR\_ADC\_INVALID\_SCLK\_MODE: ADC source clock is invalid
        - BK\_ERR\_ADC\_INVALID\_ID: ADC id is invalid
        - others: other errors.

<a id="_CPPv415bk_adc_set_mode10adc_mode_t"></a>

<a id="_CPPv315bk_adc_set_mode10adc_mode_t"></a> <a id="_CPPv215bk_adc_set_mode10adc_mode_t"></a> <a id="bk_adc_set_mode__adc_mode_t"></a> <a id="group__bk__api__adc_1ga4c279ac3f55d129745f1ecd81230f9af"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_adc\_set\_mode(adc\_mode\_t adc\_mode)
:   adc set mode

    This API config adc mode

    参数
    :   **mode** – : adc mode:

        - 0: sleep mode: adc is power down in this mode
        - 1: single step mode: adc finish sample data convesion once after enable adc and wait mcu to read sample data. The mode will turn to sleep mode after mcu read this sample date It must be enabled again when you want to sample next data.
        - 2: software control mode: adc gengerate interrupt after sample data convesion wait mcu to read sample data. adc will convert sample data after mcu reading this sample date from data register and software cleaning int flag.
        - 3: continous mode:adc wait adc\_setting time to sample data, and generate int flag after finish sample data convesion, then always repeat last sample way. This mode don’t depend on muc reading data register.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_ADC\_INVALID\_MODE:adc invalid mode
        - others: other errors.

<a id="_CPPv415bk_adc_get_modev"></a>

<a id="_CPPv315bk_adc_get_modev"></a> <a id="_CPPv215bk_adc_get_modev"></a> <a id="bk_adc_get_mode__void"></a> <a id="group__bk__api__adc_1ga66a8f42fe602d669b99c568eadfd4506"></a> adc\_mode\_t bk\_adc\_get\_mode(void)
:   get adc mode

    This API get adc work mode

    返回
    :   - adc\_mode\_t: adc\_mode

<a id="_CPPv421bk_adc_data_calculate8uint16_t10adc_chan_t"></a>

<a id="_CPPv321bk_adc_data_calculate8uint16_t10adc_chan_t"></a> <a id="_CPPv221bk_adc_data_calculate8uint16_t10adc_chan_t"></a> <a id="bk_adc_data_calculate__uint16_t.adc_chan_t"></a> <a id="group__bk__api__adc_1gafea009b9e21359b30cd81d17cfd1401f"></a> float bk\_adc\_data\_calculate(uint16\_t adc\_val, adc\_chan\_t adc\_chan)
:   adc calculate voltage

    参数
    :   - **adc\_val** – adc value
        - **adc\_chan** – adc channel

    返回
    :   voltage value, the unit is mv
