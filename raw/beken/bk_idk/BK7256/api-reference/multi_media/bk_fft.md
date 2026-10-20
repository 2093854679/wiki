---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_fft.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="fft-apis"></a>

# FFT APIs

重要

The FFT API v1.0 is the lastest stable FFT APIs. All new applications should use FFT API v1.0.

<a id="fft-interface"></a>

## FFT Interface

The BK FFT Driver supports following functional interfaces:

> - FFT function
> - IFFT function

Each function can be operated independently. However both function share the same resources, only one function can exit and work at a time.

E.g. if the FFT function is working, the IFFT funtion can not work. And calling IFFT functional interface will fail when FFT function is working.

<a id="fft-api-categories"></a>

## FFT API Categories

Most of FFT APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk\_fft, the APIs may be common for all functions and interfaces, e.g. bk\_fft\_driver\_init() etc.
> - FFT function APIs.
>
>   The APIs provide support for FFT and IFFT function. e.g. bk\_fft\_enable() etc.

Common APIs:
:   - [`bk_fft_driver_init()`](#_CPPv418bk_fft_driver_initv "bk_fft_driver_init") \- init FFT
    - [`bk_fft_driver_deinit()`](#_CPPv420bk_fft_driver_deinitv "bk_fft_driver_deinit") \- deinit FFT
    - [`bk_fft_is_busy()`](#_CPPv414bk_fft_is_busyv "bk_fft_is_busy") \- get FFT work status
    - [`bk_fft_output_read()`](#_CPPv418bk_fft_output_readP7int16_tP7int16_t8uint32_t "bk_fft_output_read") \- get FFT/IFFT output data

FFT function APIs:
:   - [`bk_fft_enable()`](#_CPPv413bk_fft_enableP11fft_input_t "bk_fft_enable") \- start FFT/IFFT function

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [fft.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414bk_fft_is_busyv"></a>

<a id="_CPPv314bk_fft_is_busyv"></a> <a id="_CPPv214bk_fft_is_busyv"></a> <a id="bk_fft_is_busy__void"></a> <a id="group__bk__api__fft_1ga21eb803c46a51ba61593753c622cb7d7"></a> bool bk\_fft\_is\_busy(void)
:   Get the fft module working status.

    返回
    :   - TRUE: fft is busying
        - FALSE: fft is not busying

<a id="_CPPv413bk_fft_enableP11fft_input_t"></a>

<a id="_CPPv313bk_fft_enableP11fft_input_t"></a> <a id="_CPPv213bk_fft_enableP11fft_input_t"></a> <a id="bk_fft_enable__fft_input_tP"></a> <a id="group__bk__api__fft_1ga6edf61f283df74dd3c526fbe40c5c14c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_fft\_enable([fft\_input\_t](#_CPPv411fft_input_t "fft_input_t") \*fft\_conf)
:   Enable fft module to process fft/ifft function.

    This API process fft/ifft function :

    - Set fft work mode: fft/ifft
    - Configure the fft/ifft parameters
    - start trigger
    - enable interrupts

    Usage example:

    ```
    //init fft driver
    bk_fft_driver_init();

    fft_conf.inbuf = os_malloc(4*1024);
    os_memset(fft_conf.inbuf, 0, 4*1024);

    fft_conf.mode = FFT_WORK_MODE_FFT;
    fft_conf.size = 1024;

    //start fft
    bk_fft_enable(&fft_conf);

    //wait fft complete
    while(fft_busy_flag)
        bk_fft_is_busy(&fft_busy_flag);
    CLI_LOGI("fft complete\r\n");
    //read output data
    bk_fft_output_read(data_proc_i, data_proc_q, 2 * 1024);
    ```

    参数
    :   **fft\_conf** – fft/ifft parameters

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_fft_driver_initv"></a>

<a id="_CPPv318bk_fft_driver_initv"></a> <a id="_CPPv218bk_fft_driver_initv"></a> <a id="bk_fft_driver_init__void"></a> <a id="group__bk__api__fft_1gaf888fe4f7ef5c5f4de47bff9c16a39a4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_fft\_driver\_init(void)
:   Init fft module driver.

    This API init fft driver :

    - power on
    - enable interrupts

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_fft_driver_deinitv"></a>

<a id="_CPPv320bk_fft_driver_deinitv"></a> <a id="_CPPv220bk_fft_driver_deinitv"></a> <a id="bk_fft_driver_deinit__void"></a> <a id="group__bk__api__fft_1gaf48a2b6a2262d1cb20a7e61b3fdc01e3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_fft\_driver\_deinit(void)
:   Deinit fft module driver.

    This API deinit fft driver :

    - Power down clock
    - disable interrupts

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_fft_output_readP7int16_tP7int16_t8uint32_t"></a>

<a id="_CPPv318bk_fft_output_readP7int16_tP7int16_t8uint32_t"></a> <a id="_CPPv218bk_fft_output_readP7int16_tP7int16_t8uint32_t"></a> <a id="bk_fft_output_read__int16_tP.int16_tP.uint32_t"></a> <a id="group__bk__api__fft_1ga1eebe6cd4065d8cd480d080c0861bdd9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_fft\_output\_read(int16\_t \*i\_output, int16\_t \*q\_output, uint32\_t size)
:   Read fft data.

    This API read fft data after processing complete

    参数
    :   - **i\_output** – save fft data
        - **q\_output** – save fft data
        - **size** – read size if i\_output

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [fft\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv416fft_int_config_t"></a>

<a id="_CPPv316fft_int_config_t"></a> <a id="_CPPv216fft_int_config_t"></a> <a id="fft_int_config_t"></a> <a id="structfft__int__config__t"></a> struct fft\_int\_config\_t

<a id="_CPPv412fft_driver_t"></a>

<a id="_CPPv312fft_driver_t"></a> <a id="_CPPv212fft_driver_t"></a> <a id="fft_driver_t"></a> <a id="structfft__driver__t"></a> struct fft\_driver\_t

<a id="_CPPv412fft_status_t"></a>

<a id="_CPPv312fft_status_t"></a> <a id="_CPPv212fft_status_t"></a> <a id="fft_status_t"></a> <a id="structfft__status__t"></a> struct fft\_status\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12fft_status_t8fft_doneE"></a>

    <a id="_CPPv3N12fft_status_t8fft_doneE"></a> <a id="_CPPv2N12fft_status_t8fft_doneE"></a> <a id="fft_status_t::fft_done__b"></a> <a id="structfft__status__t_1a8654b3f3acc930394a8828b8a21dfd65"></a> bool fft\_done
    :   FFT fft process done

    <a id="_CPPv4N12fft_status_t8fir_doneE"></a>

    <a id="_CPPv3N12fft_status_t8fir_doneE"></a> <a id="_CPPv2N12fft_status_t8fir_doneE"></a> <a id="fft_status_t::fir_done__b"></a> <a id="structfft__status__t_1ac3cd29cff5be28bc7b577a808528a55b"></a> bool fir\_done
    :   FFT fir process done

    <a id="_CPPv4N12fft_status_t14self_proc_doneE"></a>

    <a id="_CPPv3N12fft_status_t14self_proc_doneE"></a> <a id="_CPPv2N12fft_status_t14self_proc_doneE"></a> <a id="fft_status_t::self_proc_done__b"></a> <a id="structfft__status__t_1a3c8bdc60605c3f159a1510cbb388b15b"></a> bool self\_proc\_done
    :   FFT self process done

    <a id="_CPPv4N12fft_status_t13start_triggerE"></a>

    <a id="_CPPv3N12fft_status_t13start_triggerE"></a> <a id="_CPPv2N12fft_status_t13start_triggerE"></a> <a id="fft_status_t::start_trigger__b"></a> <a id="structfft__status__t_1a32cd37342746c4b2a41598a930aac218"></a> bool start\_trigger
    :   FFT start trigger flag

    <a id="_CPPv4N12fft_status_t7bit_extE"></a>

    <a id="_CPPv3N12fft_status_t7bit_extE"></a> <a id="_CPPv2N12fft_status_t7bit_extE"></a> <a id="fft_status_t::bit_ext__uint32_t"></a> <a id="structfft__status__t_1ac8479f8ebc49bc9690639a7757a59996"></a> uint32\_t bit\_ext
    :   FFT fft bit extend

<a id="_CPPv414fft_int_status"></a>

<a id="_CPPv314fft_int_status"></a> <a id="_CPPv214fft_int_status"></a> <a id="fft_int_status"></a> <a id="structfft__int__status"></a> struct fft\_int\_status

<a id="_CPPv411fft_input_t"></a>

<a id="_CPPv311fft_input_t"></a> <a id="_CPPv211fft_input_t"></a> <a id="fft_input_t"></a> <a id="structfft__input__t"></a> struct fft\_input\_t

<a id="_CPPv415fft_fir_input_t"></a>

<a id="_CPPv315fft_fir_input_t"></a> <a id="_CPPv215fft_fir_input_t"></a> <a id="fft_fir_input_t"></a> <a id="structfft__fir__input__t"></a> struct fft\_fir\_input\_t

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_FFT_NOT_INIT"></a>

<a id="group__bk__api__fft__defs_1ga5b6bdff5a8f4b02dfba84cf4c1d5fc98"></a> BK\_ERR\_FFT\_NOT\_INIT
:   FFT driver not init

<a id="c.BK_ERR_FFT_PARAM"></a>

<a id="group__bk__api__fft__defs_1gaa886c388e7cc363d75b89b9b01256026"></a> BK\_ERR\_FFT\_PARAM
:   FFT parameter invalid

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv49fft_isr_t"></a>

<a id="_CPPv39fft_isr_t"></a> <a id="_CPPv29fft_isr_t"></a> <a id="fft_isr_t"></a> <a id="fft__types_8h_1abf33a054dcda784ee4da11b51228c2d6"></a> typedef void (\*fft\_isr\_t)(void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv415fft_work_mode_t"></a>

<a id="_CPPv315fft_work_mode_t"></a> <a id="_CPPv215fft_work_mode_t"></a> <a id="group__bk__api__aud__enum_1ga9a118f5f2140f9682c4274b9904ff925"></a> enum fft\_work\_mode\_t
:   *Values:*

    <a id="_CPPv4N15fft_work_mode_t17FFT_WORK_MODE_FFTE"></a>

    <a id="_CPPv3N15fft_work_mode_t17FFT_WORK_MODE_FFTE"></a> <a id="_CPPv2N15fft_work_mode_t17FFT_WORK_MODE_FFTE"></a> <a id="group__bk__api__aud__enum_1gga9a118f5f2140f9682c4274b9904ff925a0ecabd68341ebecc105e4102c16dff80"></a> enumerator FFT\_WORK\_MODE\_FFT
    :   FFT fft work mode

    <a id="_CPPv4N15fft_work_mode_t18FFT_WORK_MODE_IFFTE"></a>

    <a id="_CPPv3N15fft_work_mode_t18FFT_WORK_MODE_IFFTE"></a> <a id="_CPPv2N15fft_work_mode_t18FFT_WORK_MODE_IFFTE"></a> <a id="group__bk__api__aud__enum_1gga9a118f5f2140f9682c4274b9904ff925ae7eb920067562d55a561c3b5ba94ee72"></a> enumerator FFT\_WORK\_MODE\_IFFT
    :   FFT ifft work mode

    <a id="_CPPv4N15fft_work_mode_t17FFT_WORK_MODE_MAXE"></a>

    <a id="_CPPv3N15fft_work_mode_t17FFT_WORK_MODE_MAXE"></a> <a id="_CPPv2N15fft_work_mode_t17FFT_WORK_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga9a118f5f2140f9682c4274b9904ff925a59a447dd65c8bef81911c69dae580f29"></a> enumerator FFT\_WORK\_MODE\_MAX

<a id="_CPPv410fft_mode_t"></a>

<a id="_CPPv310fft_mode_t"></a> <a id="_CPPv210fft_mode_t"></a> <a id="group__bk__api__aud__enum_1ga86f1e46308bfcaf8ceccb822f1d72c57"></a> enum fft\_mode\_t
:   *Values:*

    <a id="_CPPv4N10fft_mode_t15FFT_MODE_NORMALE"></a>

    <a id="_CPPv3N10fft_mode_t15FFT_MODE_NORMALE"></a> <a id="_CPPv2N10fft_mode_t15FFT_MODE_NORMALE"></a> <a id="group__bk__api__aud__enum_1gga86f1e46308bfcaf8ceccb822f1d72c57aeb075a1a28040a2e0a3de22efdbf6edd"></a> enumerator FFT\_MODE\_NORMAL
    :   FFT normal mode

    <a id="_CPPv4N10fft_mode_t15FFT_MODE_BK5130E"></a>

    <a id="_CPPv3N10fft_mode_t15FFT_MODE_BK5130E"></a> <a id="_CPPv2N10fft_mode_t15FFT_MODE_BK5130E"></a> <a id="group__bk__api__aud__enum_1gga86f1e46308bfcaf8ceccb822f1d72c57a7fc25a61b182b9c4dd2f3adbf061f7cc"></a> enumerator FFT\_MODE\_BK5130
    :   FFT bk5130 mode

    <a id="_CPPv4N10fft_mode_t12FFT_MODE_MAXE"></a>

    <a id="_CPPv3N10fft_mode_t12FFT_MODE_MAXE"></a> <a id="_CPPv2N10fft_mode_t12FFT_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga86f1e46308bfcaf8ceccb822f1d72c57a4991298585998a9536ce47dd16976259"></a> enumerator FFT\_MODE\_MAX

<a id="_CPPv413fft_ifft_en_t"></a>

<a id="_CPPv313fft_ifft_en_t"></a> <a id="_CPPv213fft_ifft_en_t"></a> <a id="group__bk__api__aud__enum_1ga02d2059e0fb8d5c44a299fccf033384c"></a> enum fft\_ifft\_en\_t
:   *Values:*

    <a id="_CPPv4N13fft_ifft_en_t16FFT_IFFT_DISABLEE"></a>

    <a id="_CPPv3N13fft_ifft_en_t16FFT_IFFT_DISABLEE"></a> <a id="_CPPv2N13fft_ifft_en_t16FFT_IFFT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga02d2059e0fb8d5c44a299fccf033384cadafe06e97312a8555fdcc6dbd39c0c99"></a> enumerator FFT\_IFFT\_DISABLE
    :   IFFT disable

    <a id="_CPPv4N13fft_ifft_en_t15FFT_IFFT_ENABLEE"></a>

    <a id="_CPPv3N13fft_ifft_en_t15FFT_IFFT_ENABLEE"></a> <a id="_CPPv2N13fft_ifft_en_t15FFT_IFFT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga02d2059e0fb8d5c44a299fccf033384cad94cf7fc35c3078bc0ba1a835158a78e"></a> enumerator FFT\_IFFT\_ENABLE
    :   IFFT enable

    <a id="_CPPv4N13fft_ifft_en_t12FFT_IFFT_MAXE"></a>

    <a id="_CPPv3N13fft_ifft_en_t12FFT_IFFT_MAXE"></a> <a id="_CPPv2N13fft_ifft_en_t12FFT_IFFT_MAXE"></a> <a id="group__bk__api__aud__enum_1gga02d2059e0fb8d5c44a299fccf033384cae2ace85026e8bb2a3c32094ca61c1b75"></a> enumerator FFT\_IFFT\_MAX

<a id="_CPPv412fft_int_en_t"></a>

<a id="_CPPv312fft_int_en_t"></a> <a id="_CPPv212fft_int_en_t"></a> <a id="group__bk__api__aud__enum_1ga5a4fb2286a31e2346ef662a6409c96da"></a> enum fft\_int\_en\_t
:   *Values:*

    <a id="_CPPv4N12fft_int_en_t15FFT_INT_DISABLEE"></a>

    <a id="_CPPv3N12fft_int_en_t15FFT_INT_DISABLEE"></a> <a id="_CPPv2N12fft_int_en_t15FFT_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga5a4fb2286a31e2346ef662a6409c96daa54d2a363956d9d690e90cf4d245618d5"></a> enumerator FFT\_INT\_DISABLE
    :   FFT interrupt disable

    <a id="_CPPv4N12fft_int_en_t14FFT_INT_ENABLEE"></a>

    <a id="_CPPv3N12fft_int_en_t14FFT_INT_ENABLEE"></a> <a id="_CPPv2N12fft_int_en_t14FFT_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga5a4fb2286a31e2346ef662a6409c96daa2865778a92a2071568b2a11d8e2607d6"></a> enumerator FFT\_INT\_ENABLE
    :   FFT interrupt enable

    <a id="_CPPv4N12fft_int_en_t11FFT_INT_MAXE"></a>

    <a id="_CPPv3N12fft_int_en_t11FFT_INT_MAXE"></a> <a id="_CPPv2N12fft_int_en_t11FFT_INT_MAXE"></a> <a id="group__bk__api__aud__enum_1gga5a4fb2286a31e2346ef662a6409c96daae8ea0897630e9f17128e002c47d45bfd"></a> enumerator FFT\_INT\_MAX

<a id="_CPPv412fft_enable_t"></a>

<a id="_CPPv312fft_enable_t"></a> <a id="_CPPv212fft_enable_t"></a> <a id="group__bk__api__aud__enum_1ga2bf11ee9b95345f44257693ba810c239"></a> enum fft\_enable\_t
:   *Values:*

    <a id="_CPPv4N12fft_enable_t11FFT_DISABLEE"></a>

    <a id="_CPPv3N12fft_enable_t11FFT_DISABLEE"></a> <a id="_CPPv2N12fft_enable_t11FFT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga2bf11ee9b95345f44257693ba810c239abc76b71c51eade1c38f24043207c914d"></a> enumerator FFT\_DISABLE
    :   FFT disable

    <a id="_CPPv4N12fft_enable_t10FFT_ENABLEE"></a>

    <a id="_CPPv3N12fft_enable_t10FFT_ENABLEE"></a> <a id="_CPPv2N12fft_enable_t10FFT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga2bf11ee9b95345f44257693ba810c239a3fed9ec14ed66db9253e1bfe1b9398eb"></a> enumerator FFT\_ENABLE
    :   FFT enable

    <a id="_CPPv4N12fft_enable_t14FFT_ENABLE_MAXE"></a>

    <a id="_CPPv3N12fft_enable_t14FFT_ENABLE_MAXE"></a> <a id="_CPPv2N12fft_enable_t14FFT_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga2bf11ee9b95345f44257693ba810c239afc55f8e7d1d867f083280e0efaf21066"></a> enumerator FFT\_ENABLE\_MAX

<a id="_CPPv49fft_gat_t"></a>

<a id="_CPPv39fft_gat_t"></a> <a id="_CPPv29fft_gat_t"></a> <a id="group__bk__api__aud__enum_1ga7c7cfab4373b5c7628bb63a5302fc788"></a> enum fft\_gat\_t
:   *Values:*

    <a id="_CPPv4N9fft_gat_t10FFT_GAT_ONE"></a>

    <a id="_CPPv3N9fft_gat_t10FFT_GAT_ONE"></a> <a id="_CPPv2N9fft_gat_t10FFT_GAT_ONE"></a> <a id="group__bk__api__aud__enum_1gga7c7cfab4373b5c7628bb63a5302fc788a7954d15ce65e75baefb3c46bc6fd572d"></a> enumerator FFT\_GAT\_ON
    :   FFT gat on

    <a id="_CPPv4N9fft_gat_t11FFT_GAT_OFFE"></a>

    <a id="_CPPv3N9fft_gat_t11FFT_GAT_OFFE"></a> <a id="_CPPv2N9fft_gat_t11FFT_GAT_OFFE"></a> <a id="group__bk__api__aud__enum_1gga7c7cfab4373b5c7628bb63a5302fc788a73c75483d50a3350f5e3aa3ee8bf8597"></a> enumerator FFT\_GAT\_OFF
    :   FFT gat off

    <a id="_CPPv4N9fft_gat_t11FFT_GAT_MAXE"></a>

    <a id="_CPPv3N9fft_gat_t11FFT_GAT_MAXE"></a> <a id="_CPPv2N9fft_gat_t11FFT_GAT_MAXE"></a> <a id="group__bk__api__aud__enum_1gga7c7cfab4373b5c7628bb63a5302fc788afbfb88b0acc489bef9c7b8c6df29bda7"></a> enumerator FFT\_GAT\_MAX

<a id="_CPPv414fft_fir_mode_t"></a>

<a id="_CPPv314fft_fir_mode_t"></a> <a id="_CPPv214fft_fir_mode_t"></a> <a id="group__bk__api__aud__enum_1gad8c901bfd4447804788cd5cea6189610"></a> enum fft\_fir\_mode\_t
:   *Values:*

    <a id="_CPPv4N14fft_fir_mode_t19FFT_FIR_MODE_SIGNALE"></a>

    <a id="_CPPv3N14fft_fir_mode_t19FFT_FIR_MODE_SIGNALE"></a> <a id="_CPPv2N14fft_fir_mode_t19FFT_FIR_MODE_SIGNALE"></a> <a id="group__bk__api__aud__enum_1ggad8c901bfd4447804788cd5cea6189610a19e929a0262bbc93bfcc0bdd4618ca1f"></a> enumerator FFT\_FIR\_MODE\_SIGNAL
    :   FIR signal mode

    <a id="_CPPv4N14fft_fir_mode_t17FFT_FIR_MODE_DUALE"></a>

    <a id="_CPPv3N14fft_fir_mode_t17FFT_FIR_MODE_DUALE"></a> <a id="_CPPv2N14fft_fir_mode_t17FFT_FIR_MODE_DUALE"></a> <a id="group__bk__api__aud__enum_1ggad8c901bfd4447804788cd5cea6189610a69c94c709f456fe89b6ba0cceb9270a4"></a> enumerator FFT\_FIR\_MODE\_DUAL
    :   FIR dual mode

    <a id="_CPPv4N14fft_fir_mode_t16FFT_FIR_MODE_MAXE"></a>

    <a id="_CPPv3N14fft_fir_mode_t16FFT_FIR_MODE_MAXE"></a> <a id="_CPPv2N14fft_fir_mode_t16FFT_FIR_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggad8c901bfd4447804788cd5cea6189610a1aab84e12f212e155400acade7384985"></a> enumerator FFT\_FIR\_MODE\_MAX

<a id="_CPPv416fft_fir_int_en_t"></a>

<a id="_CPPv316fft_fir_int_en_t"></a> <a id="_CPPv216fft_fir_int_en_t"></a> <a id="group__bk__api__aud__enum_1gab792f45677ef0b196f13775a1438f2e9"></a> enum fft\_fir\_int\_en\_t
:   *Values:*

    <a id="_CPPv4N16fft_fir_int_en_t19FFT_FIR_INT_DISABLEE"></a>

    <a id="_CPPv3N16fft_fir_int_en_t19FFT_FIR_INT_DISABLEE"></a> <a id="_CPPv2N16fft_fir_int_en_t19FFT_FIR_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggab792f45677ef0b196f13775a1438f2e9a0ab28426a2cad98772706a1b3cd7e3eb"></a> enumerator FFT\_FIR\_INT\_DISABLE
    :   FIR interrupt disable

    <a id="_CPPv4N16fft_fir_int_en_t18FFT_FIR_INT_ENABLEE"></a>

    <a id="_CPPv3N16fft_fir_int_en_t18FFT_FIR_INT_ENABLEE"></a> <a id="_CPPv2N16fft_fir_int_en_t18FFT_FIR_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggab792f45677ef0b196f13775a1438f2e9a6feeda5daca17f6af212f0ef2690fd43"></a> enumerator FFT\_FIR\_INT\_ENABLE
    :   FIR interrupt enable

    <a id="_CPPv4N16fft_fir_int_en_t15FFT_FIR_INT_MAXE"></a>

    <a id="_CPPv3N16fft_fir_int_en_t15FFT_FIR_INT_MAXE"></a> <a id="_CPPv2N16fft_fir_int_en_t15FFT_FIR_INT_MAXE"></a> <a id="group__bk__api__aud__enum_1ggab792f45677ef0b196f13775a1438f2e9ac7c134dd7cf68c3d8458b01535924feb"></a> enumerator FFT\_FIR\_INT\_MAX

<a id="_CPPv412fft_fir_en_t"></a>

<a id="_CPPv312fft_fir_en_t"></a> <a id="_CPPv212fft_fir_en_t"></a> <a id="group__bk__api__aud__enum_1ga5d3ed5a941637ac117dfab6111fe2ea8"></a> enum fft\_fir\_en\_t
:   *Values:*

    <a id="_CPPv4N12fft_fir_en_t15FFT_FIR_DISABLEE"></a>

    <a id="_CPPv3N12fft_fir_en_t15FFT_FIR_DISABLEE"></a> <a id="_CPPv2N12fft_fir_en_t15FFT_FIR_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga5d3ed5a941637ac117dfab6111fe2ea8a05161f64d537be0caa945c72295a39fa"></a> enumerator FFT\_FIR\_DISABLE
    :   FIR disable

    <a id="_CPPv4N12fft_fir_en_t14FFT_FIR_ENABLEE"></a>

    <a id="_CPPv3N12fft_fir_en_t14FFT_FIR_ENABLEE"></a> <a id="_CPPv2N12fft_fir_en_t14FFT_FIR_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga5d3ed5a941637ac117dfab6111fe2ea8ad58e19c11bfde351b3700840788a703a"></a> enumerator FFT\_FIR\_ENABLE
    :   FIR enable

    <a id="_CPPv4N12fft_fir_en_t18FFT_FIR_ENABLE_MAXE"></a>

    <a id="_CPPv3N12fft_fir_en_t18FFT_FIR_ENABLE_MAXE"></a> <a id="_CPPv2N12fft_fir_en_t18FFT_FIR_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga5d3ed5a941637ac117dfab6111fe2ea8acdcecf0a85cae5c0e978823807469298"></a> enumerator FFT\_FIR\_ENABLE\_MAX

<a id="_CPPv420fft_self_proc_mode_t"></a>

<a id="_CPPv320fft_self_proc_mode_t"></a> <a id="_CPPv220fft_self_proc_mode_t"></a> <a id="group__bk__api__aud__enum_1ga514fa25f0a6900ee2f198d953f7410e2"></a> enum fft\_self\_proc\_mode\_t
:   *Values:*

    <a id="_CPPv4N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE0E"></a>

    <a id="_CPPv3N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE0E"></a> <a id="_CPPv2N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE0E"></a> <a id="group__bk__api__aud__enum_1gga514fa25f0a6900ee2f198d953f7410e2ac23d97895d114095a89e0e3935523654"></a> enumerator FFT\_SELF\_PROC\_MODE0
    :   Self process mode1

    <a id="_CPPv4N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE1E"></a>

    <a id="_CPPv3N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE1E"></a> <a id="_CPPv2N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE1E"></a> <a id="group__bk__api__aud__enum_1gga514fa25f0a6900ee2f198d953f7410e2a7c052a6d98e6ae7d1322f1b7d86d283f"></a> enumerator FFT\_SELF\_PROC\_MODE1
    :   Self process mode2

    <a id="_CPPv4N20fft_self_proc_mode_t22FFT_SELF_PROC_MODE_MAXE"></a>

    <a id="_CPPv3N20fft_self_proc_mode_t22FFT_SELF_PROC_MODE_MAXE"></a> <a id="_CPPv2N20fft_self_proc_mode_t22FFT_SELF_PROC_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga514fa25f0a6900ee2f198d953f7410e2a73c8f310f5e172f4f90fb1889fbf1cb0"></a> enumerator FFT\_SELF\_PROC\_MODE\_MAX

<a id="_CPPv419fft_memory_config_t"></a>

<a id="_CPPv319fft_memory_config_t"></a> <a id="_CPPv219fft_memory_config_t"></a> <a id="group__bk__api__aud__enum_1gae6c8aa0f041b2e0af19ec3b518f28b4a"></a> enum fft\_memory\_config\_t
:   *Values:*

    <a id="_CPPv4N19fft_memory_config_t18FFT_SELECT_MEMORY0E"></a>

    <a id="_CPPv3N19fft_memory_config_t18FFT_SELECT_MEMORY0E"></a> <a id="_CPPv2N19fft_memory_config_t18FFT_SELECT_MEMORY0E"></a> <a id="group__bk__api__aud__enum_1ggae6c8aa0f041b2e0af19ec3b518f28b4aa2c85371d7dbc9136f639aedf631be244"></a> enumerator FFT\_SELECT\_MEMORY0
    :   FFT select Memroy0

    <a id="_CPPv4N19fft_memory_config_t18FFT_SELECT_MEMORY1E"></a>

    <a id="_CPPv3N19fft_memory_config_t18FFT_SELECT_MEMORY1E"></a> <a id="_CPPv2N19fft_memory_config_t18FFT_SELECT_MEMORY1E"></a> <a id="group__bk__api__aud__enum_1ggae6c8aa0f041b2e0af19ec3b518f28b4aa5ed69ce553580b260794c34402ab840f"></a> enumerator FFT\_SELECT\_MEMORY1
    :   FFT select Memroy1

    <a id="_CPPv4N19fft_memory_config_t21FFT_SELECT_MEMORY_MAXE"></a>

    <a id="_CPPv3N19fft_memory_config_t21FFT_SELECT_MEMORY_MAXE"></a> <a id="_CPPv2N19fft_memory_config_t21FFT_SELECT_MEMORY_MAXE"></a> <a id="group__bk__api__aud__enum_1ggae6c8aa0f041b2e0af19ec3b518f28b4aaa1cccfe8a5f314c661344018a0d568cb"></a> enumerator FFT\_SELECT\_MEMORY\_MAX
