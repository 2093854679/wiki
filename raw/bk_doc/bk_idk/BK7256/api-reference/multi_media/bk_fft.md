# FFT APIs[](#fft-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/multi_media/bk_fft.html "../../../../en/v1.5/api-reference/multi_media/bk_fft.html")

重要

The FFT API v1.0 is the lastest stable FFT APIs. All new applications should use FFT API v1.0.


## FFT Interface[](#fft-interface "永久链接至标题")

The BK FFT Driver supports following functional interfaces:

> - FFT function
> - IFFT function

Each function can be operated independently. However both function share the same resources, only one function can exit and work at a time.

E.g. if the FFT function is working, the IFFT funtion can not work. And calling IFFT functional interface will fail when FFT function is working.


## FFT API Categories[](#fft-api-categories "永久链接至标题")

Most of FFT APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk_fft, the APIs may be common for all functions and interfaces, e.g. bk_fft_driver_init() etc.
> - FFT function APIs.
>
>   The APIs provide support for FFT and IFFT function. e.g. bk_fft_enable() etc.

Common APIs:
:   - [`bk_fft_driver_init()`](#_CPPv418bk_fft_driver_initv "bk_fft_driver_init") - init FFT

    - [`bk_fft_driver_deinit()`](#_CPPv420bk_fft_driver_deinitv "bk_fft_driver_deinit") - deinit FFT

    - [`bk_fft_is_busy()`](#_CPPv414bk_fft_is_busyv "bk_fft_is_busy") - get FFT work status

    - [`bk_fft_output_read()`](#_CPPv418bk_fft_output_readP7int16_tP7int16_t8uint32_t "bk_fft_output_read") - get FFT/IFFT output data

FFT function APIs:
:   - [`bk_fft_enable()`](#_CPPv413bk_fft_enableP11fft_input_t "bk_fft_enable") - start FFT/IFFT function


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [fft.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft.h")


### Functions[](#functions "永久链接至标题")

bool bk_fft_is_busy(void)[](#_CPPv414bk_fft_is_busyv "永久链接至目标")
:   Get the fft module working status.

    返回
    :   - TRUE: fft is busying

        - FALSE: fft is not busying

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_fft_enable([fft_input_t](#_CPPv411fft_input_t "fft_input_t") *fft_conf)[](#_CPPv413bk_fft_enableP11fft_input_t "永久链接至目标")
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
    :   **fft_conf** – fft/ifft parameters

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_fft_driver_init(void)[](#_CPPv418bk_fft_driver_initv "永久链接至目标")
:   Init fft module driver.

    This API init fft driver :


    - power on

    - enable interrupts

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_fft_driver_deinit(void)[](#_CPPv420bk_fft_driver_deinitv "永久链接至目标")
:   Deinit fft module driver.

    This API deinit fft driver :


    - Power down clock

    - disable interrupts

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_fft_output_read(int16_t *i_output, int16_t *q_output, uint32_t size)[](#_CPPv418bk_fft_output_readP7int16_tP7int16_t8uint32_t "永久链接至目标")
:   Read fft data.

    This API read fft data after processing complete

    参数
    :   - **i_output** – save fft data

        - **q_output** – save fft data

        - **size** – read size if i_output

    返回
    :   - BK_OK: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [fft_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/fft_types.h")


### Structures[](#structures "永久链接至标题")

struct fft_int_config_t[](#_CPPv416fft_int_config_t "永久链接至目标")

struct fft_driver_t[](#_CPPv412fft_driver_t "永久链接至目标")

struct fft_status_t[](#_CPPv412fft_status_t "永久链接至目标")
:   Public Members

    bool fft_done[](#_CPPv4N12fft_status_t8fft_doneE "永久链接至目标")
    :   FFT fft process done

    bool fir_done[](#_CPPv4N12fft_status_t8fir_doneE "永久链接至目标")
    :   FFT fir process done

    bool self_proc_done[](#_CPPv4N12fft_status_t14self_proc_doneE "永久链接至目标")
    :   FFT self process done

    bool start_trigger[](#_CPPv4N12fft_status_t13start_triggerE "永久链接至目标")
    :   FFT start trigger flag

    uint32_t bit_ext[](#_CPPv4N12fft_status_t7bit_extE "永久链接至目标")
    :   FFT fft bit extend

struct fft_int_status[](#_CPPv414fft_int_status "永久链接至目标")

struct fft_input_t[](#_CPPv411fft_input_t "永久链接至目标")

struct fft_fir_input_t[](#_CPPv415fft_fir_input_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

BK_ERR_FFT_NOT_INIT[](#c.BK_ERR_FFT_NOT_INIT "永久链接至目标")
:   FFT driver not init

BK_ERR_FFT_PARAM[](#c.BK_ERR_FFT_PARAM "永久链接至目标")
:   FFT parameter invalid


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*fft_isr_t)(void *param)[](#_CPPv49fft_isr_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum fft_work_mode_t[](#_CPPv415fft_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator FFT_WORK_MODE_FFT[](#_CPPv4N15fft_work_mode_t17FFT_WORK_MODE_FFTE "永久链接至目标")
    :   FFT fft work mode

    enumerator FFT_WORK_MODE_IFFT[](#_CPPv4N15fft_work_mode_t18FFT_WORK_MODE_IFFTE "永久链接至目标")
    :   FFT ifft work mode

    enumerator FFT_WORK_MODE_MAX[](#_CPPv4N15fft_work_mode_t17FFT_WORK_MODE_MAXE "永久链接至目标")

enum fft_mode_t[](#_CPPv410fft_mode_t "永久链接至目标")
:   *Values:*

    enumerator FFT_MODE_NORMAL[](#_CPPv4N10fft_mode_t15FFT_MODE_NORMALE "永久链接至目标")
    :   FFT normal mode

    enumerator FFT_MODE_BK5130[](#_CPPv4N10fft_mode_t15FFT_MODE_BK5130E "永久链接至目标")
    :   FFT bk5130 mode

    enumerator FFT_MODE_MAX[](#_CPPv4N10fft_mode_t12FFT_MODE_MAXE "永久链接至目标")

enum fft_ifft_en_t[](#_CPPv413fft_ifft_en_t "永久链接至目标")
:   *Values:*

    enumerator FFT_IFFT_DISABLE[](#_CPPv4N13fft_ifft_en_t16FFT_IFFT_DISABLEE "永久链接至目标")
    :   IFFT disable

    enumerator FFT_IFFT_ENABLE[](#_CPPv4N13fft_ifft_en_t15FFT_IFFT_ENABLEE "永久链接至目标")
    :   IFFT enable

    enumerator FFT_IFFT_MAX[](#_CPPv4N13fft_ifft_en_t12FFT_IFFT_MAXE "永久链接至目标")

enum fft_int_en_t[](#_CPPv412fft_int_en_t "永久链接至目标")
:   *Values:*

    enumerator FFT_INT_DISABLE[](#_CPPv4N12fft_int_en_t15FFT_INT_DISABLEE "永久链接至目标")
    :   FFT interrupt disable

    enumerator FFT_INT_ENABLE[](#_CPPv4N12fft_int_en_t14FFT_INT_ENABLEE "永久链接至目标")
    :   FFT interrupt enable

    enumerator FFT_INT_MAX[](#_CPPv4N12fft_int_en_t11FFT_INT_MAXE "永久链接至目标")

enum fft_enable_t[](#_CPPv412fft_enable_t "永久链接至目标")
:   *Values:*

    enumerator FFT_DISABLE[](#_CPPv4N12fft_enable_t11FFT_DISABLEE "永久链接至目标")
    :   FFT disable

    enumerator FFT_ENABLE[](#_CPPv4N12fft_enable_t10FFT_ENABLEE "永久链接至目标")
    :   FFT enable

    enumerator FFT_ENABLE_MAX[](#_CPPv4N12fft_enable_t14FFT_ENABLE_MAXE "永久链接至目标")

enum fft_gat_t[](#_CPPv49fft_gat_t "永久链接至目标")
:   *Values:*

    enumerator FFT_GAT_ON[](#_CPPv4N9fft_gat_t10FFT_GAT_ONE "永久链接至目标")
    :   FFT gat on

    enumerator FFT_GAT_OFF[](#_CPPv4N9fft_gat_t11FFT_GAT_OFFE "永久链接至目标")
    :   FFT gat off

    enumerator FFT_GAT_MAX[](#_CPPv4N9fft_gat_t11FFT_GAT_MAXE "永久链接至目标")

enum fft_fir_mode_t[](#_CPPv414fft_fir_mode_t "永久链接至目标")
:   *Values:*

    enumerator FFT_FIR_MODE_SIGNAL[](#_CPPv4N14fft_fir_mode_t19FFT_FIR_MODE_SIGNALE "永久链接至目标")
    :   FIR signal mode

    enumerator FFT_FIR_MODE_DUAL[](#_CPPv4N14fft_fir_mode_t17FFT_FIR_MODE_DUALE "永久链接至目标")
    :   FIR dual mode

    enumerator FFT_FIR_MODE_MAX[](#_CPPv4N14fft_fir_mode_t16FFT_FIR_MODE_MAXE "永久链接至目标")

enum fft_fir_int_en_t[](#_CPPv416fft_fir_int_en_t "永久链接至目标")
:   *Values:*

    enumerator FFT_FIR_INT_DISABLE[](#_CPPv4N16fft_fir_int_en_t19FFT_FIR_INT_DISABLEE "永久链接至目标")
    :   FIR interrupt disable

    enumerator FFT_FIR_INT_ENABLE[](#_CPPv4N16fft_fir_int_en_t18FFT_FIR_INT_ENABLEE "永久链接至目标")
    :   FIR interrupt enable

    enumerator FFT_FIR_INT_MAX[](#_CPPv4N16fft_fir_int_en_t15FFT_FIR_INT_MAXE "永久链接至目标")

enum fft_fir_en_t[](#_CPPv412fft_fir_en_t "永久链接至目标")
:   *Values:*

    enumerator FFT_FIR_DISABLE[](#_CPPv4N12fft_fir_en_t15FFT_FIR_DISABLEE "永久链接至目标")
    :   FIR disable

    enumerator FFT_FIR_ENABLE[](#_CPPv4N12fft_fir_en_t14FFT_FIR_ENABLEE "永久链接至目标")
    :   FIR enable

    enumerator FFT_FIR_ENABLE_MAX[](#_CPPv4N12fft_fir_en_t18FFT_FIR_ENABLE_MAXE "永久链接至目标")

enum fft_self_proc_mode_t[](#_CPPv420fft_self_proc_mode_t "永久链接至目标")
:   *Values:*

    enumerator FFT_SELF_PROC_MODE0[](#_CPPv4N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE0E "永久链接至目标")
    :   Self process mode1

    enumerator FFT_SELF_PROC_MODE1[](#_CPPv4N20fft_self_proc_mode_t19FFT_SELF_PROC_MODE1E "永久链接至目标")
    :   Self process mode2

    enumerator FFT_SELF_PROC_MODE_MAX[](#_CPPv4N20fft_self_proc_mode_t22FFT_SELF_PROC_MODE_MAXE "永久链接至目标")

enum fft_memory_config_t[](#_CPPv419fft_memory_config_t "永久链接至目标")
:   *Values:*

    enumerator FFT_SELECT_MEMORY0[](#_CPPv4N19fft_memory_config_t18FFT_SELECT_MEMORY0E "永久链接至目标")
    :   FFT select Memroy0

    enumerator FFT_SELECT_MEMORY1[](#_CPPv4N19fft_memory_config_t18FFT_SELECT_MEMORY1E "永久链接至目标")
    :   FFT select Memroy1

    enumerator FFT_SELECT_MEMORY_MAX[](#_CPPv4N19fft_memory_config_t21FFT_SELECT_MEMORY_MAXE "永久链接至目标")
