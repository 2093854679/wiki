---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_dma.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-dma"></a>

# DRV\_DMA

<a id="drv-dma-api-status"></a>

## DRV\_DMA API Status

| API |
| --- |
| [`drv_dma_device_init()`](#_CPPv419drv_dma_device_init8uint32_t "drv_dma_device_init") |
| [`drv_dma_device_deinit()`](#_CPPv421drv_dma_device_deinit8uint32_t "drv_dma_device_deinit") |
| [`drv_dma_chn_alloc()`](#_CPPv417drv_dma_chn_alloc8uint32_t7int32_t "drv_dma_chn_alloc") |
| [`drv_dma_chn_free()`](#_CPPv416drv_dma_chn_free8uint32_t "drv_dma_chn_free") |
| [`drv_dma_cfg_callback()`](#_CPPv420drv_dma_cfg_callback8uint32_t7int32_t14pfunc_dma_cb_t14pfunc_dma_cb_tPv "drv_dma_cfg_callback") |
| [`drv_dma_cfg_param()`](#_CPPv417drv_dma_cfg_param8uint32_t10dma_mode_e16dma_data_width_e16dma_data_width_e16dma_burst_type_e16dma_burst_type_e "drv_dma_cfg_param") |
| [`drv_dma_cfg_hw_request()`](#_CPPv422drv_dma_cfg_hw_request8uint32_t13dma_from_to_e13dma_req_mux_e "drv_dma_cfg_hw_request") |
| [`drv_dma_load()`](#_CPPv412drv_dma_load8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t "drv_dma_load") |
| [`drv_dma_update_loop_pause_addr()`](#_CPPv430drv_dma_update_loop_pause_addr8uint32_t13dma_from_to_e8uint32_t "drv_dma_update_loop_pause_addr") |
| [`drv_dma_chn_enable()`](#_CPPv418drv_dma_chn_enable8uint32_tb "drv_dma_chn_enable") |
| [`drv_dma_chn_is_enabled()`](#_CPPv422drv_dma_chn_is_enabled8uint32_t "drv_dma_chn_is_enabled") |
| [`drv_dma_get_remain_len()`](#_CPPv422drv_dma_get_remain_len8uint32_t "drv_dma_get_remain_len") |
| [`drv_dma_get_src_read_addr()`](#_CPPv425drv_dma_get_src_read_addr8uint32_t "drv_dma_get_src_read_addr") |
| [`drv_dma_get_dst_write_addr()`](#_CPPv426drv_dma_get_dst_write_addr8uint32_t "drv_dma_get_dst_write_addr") |
| [`drv_dma_flush_unaligned_data()`](#_CPPv428drv_dma_flush_unaligned_data8uint32_t "drv_dma_flush_unaligned_data") |
| [`drv_dma_wait_flush_unaligned_data_done()`](#_CPPv438drv_dma_wait_flush_unaligned_data_done8uint32_t "drv_dma_wait_flush_unaligned_data_done") |
| [`drv_dma_get_loop_pause_addr()`](#_CPPv427drv_dma_get_loop_pause_addr8uint32_t13dma_from_to_e "drv_dma_get_loop_pause_addr") |

<a id="drv-dma-api-reference"></a>

## DRV\_DMA API Reference

<a id="header-file"></a>

### Header File

- [driver/dma/drv\_dma.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/dma/drv_dma.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419drv_dma_device_init8uint32_t"></a>

<a id="_CPPv319drv_dma_device_init8uint32_t"></a> <a id="_CPPv219drv_dma_device_init8uint32_t"></a> <a id="drv_dma_device_init__uint32_t"></a> <a id="drv__dma_8h_1a89e26a38d6099f522ab643ef328d2733"></a> int32\_t drv\_dma\_device\_init(uint32\_t dev\_index)
:   init a dma device.

    初始化dma设备，通常是在系统开始初始化的时候调用一次

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_dma_device_deinit8uint32_t"></a>

<a id="_CPPv321drv_dma_device_deinit8uint32_t"></a> <a id="_CPPv221drv_dma_device_deinit8uint32_t"></a> <a id="drv_dma_device_deinit__uint32_t"></a> <a id="drv__dma_8h_1a30e70db6cace440a38cf57ae3e3267fc"></a> int32\_t drv\_dma\_device\_deinit(uint32\_t dev\_index)
:   deinit a dma device.

    反初始化dma设备，所有的dma channel都没用的时候才能返回成功，通常可能不会被调用

    参数:
    :   **dev\_index** – **\[in\]** device index, same as [drv\_dma\_device\_init()](#drv__dma_8h_1a89e26a38d6099f522ab643ef328d2733)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_dma_chn_alloc8uint32_t7int32_t"></a>

<a id="_CPPv317drv_dma_chn_alloc8uint32_t7int32_t"></a> <a id="_CPPv217drv_dma_chn_alloc8uint32_t7int32_t"></a> <a id="drv_dma_chn_alloc__uint32_t.int32_t"></a> <a id="drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47"></a> uint32\_t drv\_dma\_chn\_alloc(uint32\_t dev\_index, int32\_t req\_chn\_index)
:   alloc a dma channel.

    从这个dma设备中分配出一个dma channel，后续操作dma channel需要用到该函数的返回值

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device)
        - **req\_chn\_index** – **\[in\]** -1: 不指定，随机分配 \>\=0: 指定对应的channel

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   dma channel instance

<a id="_CPPv416drv_dma_chn_free8uint32_t"></a>

<a id="_CPPv316drv_dma_chn_free8uint32_t"></a> <a id="_CPPv216drv_dma_chn_free8uint32_t"></a> <a id="drv_dma_chn_free__uint32_t"></a> <a id="drv__dma_8h_1a3d4ed109b106645b3533b77c5d658a94"></a> int32\_t drv\_dma\_chn\_free(uint32\_t chn\_instance)
:   free dma channel.

    释放dma channel，当不再使用该channel时需要调用该函数以让该channel被其他人使用

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_dma_cfg_callback8uint32_t7int32_t14pfunc_dma_cb_t14pfunc_dma_cb_tPv"></a>

<a id="_CPPv320drv_dma_cfg_callback8uint32_t7int32_t14pfunc_dma_cb_t14pfunc_dma_cb_tPv"></a> <a id="_CPPv220drv_dma_cfg_callback8uint32_t7int32_t14pfunc_dma_cb_t14pfunc_dma_cb_tPv"></a> <a id="drv_dma_cfg_callback__uint32_t.int32_t.pfunc_dma_cb_t.pfunc_dma_cb_t.voidP"></a> <a id="drv__dma_8h_1abb1714df8fb8d86bfe5cc2e06e1f84a0"></a> int32\_t drv\_dma\_cfg\_callback(uint32\_t chn\_instance, int32\_t priority, [pfunc\_dma\_cb\_t](#_CPPv414pfunc_dma_cb_t "pfunc_dma_cb_t") pfn\_half, [pfunc\_dma\_cb\_t](#_CPPv414pfunc_dma_cb_t "pfunc_dma_cb_t") pfn\_finish, void \*pv\_cb\_arg)
:   config dma channel callback.

    配置dma搬移完成的callback，如果不想处理callback，对应的参数传NULL即可 如果不想处理callback，也应该调用该函数，避免误调上次使用该channel的人的callback

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **priority** – **\[in\]** 该channel的优先级(0\~7), 7是最高优先级
        - **pfn\_half** – **\[in\]** 搬移完成一半的时候出的callback
        - **pfn\_finish** – **\[in\]** 全部搬移完成出的callback
        - **pv\_cb\_arg** – **\[in\]** callback带的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_dma_cfg_param8uint32_t10dma_mode_e16dma_data_width_e16dma_data_width_e16dma_burst_type_e16dma_burst_type_e"></a>

<a id="_CPPv317drv_dma_cfg_param8uint32_t10dma_mode_e16dma_data_width_e16dma_data_width_e16dma_burst_type_e16dma_burst_type_e"></a> <a id="_CPPv217drv_dma_cfg_param8uint32_t10dma_mode_e16dma_data_width_e16dma_data_width_e16dma_burst_type_e16dma_burst_type_e"></a> <a id="drv_dma_cfg_param__uint32_t.dma_mode_e.dma_data_width_e.dma_data_width_e.dma_burst_type_e.dma_burst_type_e"></a> <a id="drv__dma_8h_1a66fb4db094b1fa72797d38c46b0c5689"></a> int32\_t drv\_dma\_cfg\_param(uint32\_t chn\_instance, [dma\_mode\_e](#_CPPv410dma_mode_e "dma_mode_e") mode, [dma\_data\_width\_e](#_CPPv416dma_data_width_e "dma_data_width_e") src\_data\_width, [dma\_data\_width\_e](#_CPPv416dma_data_width_e "dma_data_width_e") dst\_data\_width, [dma\_burst\_type\_e](#_CPPv416dma_burst_type_e "dma_burst_type_e") src\_burst\_len, [dma\_burst\_type\_e](#_CPPv416dma_burst_type_e "dma_burst_type_e") dst\_burst\_len)
:   config dma channel parameter.

    配置该dma channel的一些参数, 需要在 [drv\_dma\_load()](#drv__dma_8h_1a46e90f3bb21a2e39ee7b875c8255af52) 之前调用

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **mode** – **\[in\]** see dma\_mode\_e
        - **src\_data\_width** – **\[in\]** source data width, see dma\_data\_width\_e
        - **dst\_data\_width** – **\[in\]** destination data width, see dma\_data\_width\_e
        - **src\_burst\_len** – **\[in\]** source burst length, see dma\_burst\_type\_e
        - **dst\_burst\_len** – **\[in\]** destination burst length, see dma\_burst\_type\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_dma_cfg_hw_request8uint32_t13dma_from_to_e13dma_req_mux_e"></a>

<a id="_CPPv322drv_dma_cfg_hw_request8uint32_t13dma_from_to_e13dma_req_mux_e"></a> <a id="_CPPv222drv_dma_cfg_hw_request8uint32_t13dma_from_to_e13dma_req_mux_e"></a> <a id="drv_dma_cfg_hw_request__uint32_t.dma_from_to_e.dma_req_mux_e"></a> <a id="drv__dma_8h_1ab051728758eab09a57f0e5171b23adaa"></a> int32\_t drv\_dma\_cfg\_hw\_request(uint32\_t chn\_instance, [dma\_from\_to\_e](#_CPPv413dma_from_to_e "dma_from_to_e") e\_src\_dst, dma\_req\_mux\_e e\_req)
:   config HW request for this dma channel.

    对该dma channel的源和目标选择对应的硬件request信号，外设使用dma的时候需要进行配置

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **e\_src\_dst** – **\[in\]** 选择源还是目标，see dma\_from\_to\_e
        - **e\_req** – **\[in\]** dma request, see dma\_req\_mux\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412drv_dma_load8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv312drv_dma_load8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv212drv_dma_load8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="drv_dma_load__uint32_t.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t"></a> <a id="drv__dma_8h_1a46e90f3bb21a2e39ee7b875c8255af52"></a> int32\_t drv\_dma\_load(uint32\_t chn\_instance, uint32\_t transmit\_bytes, uint32\_t src\_addr\_start, uint32\_t dst\_addr\_start, uint32\_t src\_addr\_end, uint32\_t dst\_addr\_end)
:   load dma address and length.

    加载dma搬移的长度和地址，end地址也需要配置，用来判断是否是不动的FIFO地址 调用该函数前应该先调用 [drv\_dma\_cfg\_param()](#drv__dma_8h_1a66fb4db094b1fa72797d38c46b0c5689) 和 [drv\_dma\_cfg\_hw\_request()](#drv__dma_8h_1ab051728758eab09a57f0e5171b23adaa)

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **transmit\_bytes** – **\[in\]** 以byte为单位的搬移长度
        - **src\_addr\_start** – **\[in\]** 搬移源的开始地址，需要和data width对齐
        - **dst\_addr\_start** – **\[in\]** 搬移目标的开始地址，需要和data width对齐
        - **src\_addr\_end** – **\[in\]** 搬移源的结束地址，对于memory to memory, 该地址等于transmit\_bytes \+ src\_addr\_start
        - **dst\_addr\_end** – **\[in\]** 搬移目标的结束地址，对于memory to memory, 该地址等于transmit\_bytes \+ dst\_addr\_start

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430drv_dma_update_loop_pause_addr8uint32_t13dma_from_to_e8uint32_t"></a>

<a id="_CPPv330drv_dma_update_loop_pause_addr8uint32_t13dma_from_to_e8uint32_t"></a> <a id="_CPPv230drv_dma_update_loop_pause_addr8uint32_t13dma_from_to_e8uint32_t"></a> <a id="drv_dma_update_loop_pause_addr__uint32_t.dma_from_to_e.uint32_t"></a> <a id="drv__dma_8h_1a4900fe37beba8cd5c4bb847c19405095"></a> int32\_t drv\_dma\_update\_loop\_pause\_addr(uint32\_t chn\_instance, [dma\_from\_to\_e](#_CPPv413dma_from_to_e "dma_from_to_e") e\_src\_dst, uint32\_t addr)
:   config pause address in loop mode.

    对于循环重复搬移的情况，涉及到读写数据的同步问题，该地址用来告诉dma读写的时候不用越过它 例如，将memory数据循环搬到codec中，如果软件动作太慢，则dma会搬到一些软件还未填写的数据 如果软件配置了pause address，则dma会在到达这个地址后等到软件填了数据，更新地址后再进行搬数

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **e\_src\_dst** – **\[in\]** 配置源还是目标，see dma\_from\_to\_e
        - **addr** – **\[in\]** pause address for dma

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_dma_chn_enable8uint32_tb"></a>

<a id="_CPPv318drv_dma_chn_enable8uint32_tb"></a> <a id="_CPPv218drv_dma_chn_enable8uint32_tb"></a> <a id="drv_dma_chn_enable__uint32_t.b"></a> <a id="drv__dma_8h_1a8a7454ce52d8adca6f5105b2e80e1061"></a> int32\_t drv\_dma\_chn\_enable(uint32\_t chn\_instance, bool enable)
:   enable dma channel or not.

    使能该dma channel

    参数:
    :   - **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_dma_chn_is_enabled8uint32_t"></a>

<a id="_CPPv322drv_dma_chn_is_enabled8uint32_t"></a> <a id="_CPPv222drv_dma_chn_is_enabled8uint32_t"></a> <a id="drv_dma_chn_is_enabled__uint32_t"></a> <a id="drv__dma_8h_1a5c8fc7b3a49aefe6232c2e0ddce9e486"></a> bool drv\_dma\_chn\_is\_enabled(uint32\_t chn\_instance)
:   check the dma channel is enabled or not.

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回值:
    :   - **true** – dma channel is enabled
        - **false** – dma channel is not enabled

    返回:
    :   is enabled

<a id="_CPPv422drv_dma_get_remain_len8uint32_t"></a>

<a id="_CPPv322drv_dma_get_remain_len8uint32_t"></a> <a id="_CPPv222drv_dma_get_remain_len8uint32_t"></a> <a id="drv_dma_get_remain_len__uint32_t"></a> <a id="drv__dma_8h_1a26cfe832f1566565e91b54bbb1a16c48"></a> uint32\_t drv\_dma\_get\_remain\_len(uint32\_t chn\_instance)
:   get remain length.

    dma还未完成搬移，通过该函数可以知道还剩多少数据未搬

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回:
    :   left size in bytes.

<a id="_CPPv425drv_dma_get_src_read_addr8uint32_t"></a>

<a id="_CPPv325drv_dma_get_src_read_addr8uint32_t"></a> <a id="_CPPv225drv_dma_get_src_read_addr8uint32_t"></a> <a id="drv_dma_get_src_read_addr__uint32_t"></a> <a id="drv__dma_8h_1a3fef327f3a23776efd94c1e1461c9cf2"></a> uint32\_t drv\_dma\_get\_src\_read\_addr(uint32\_t chn\_instance)
:   get source read address.

    获取此时dma搬移源的读地址(下一个要读的地址)

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回:
    :   source read pointer

<a id="_CPPv426drv_dma_get_dst_write_addr8uint32_t"></a>

<a id="_CPPv326drv_dma_get_dst_write_addr8uint32_t"></a> <a id="_CPPv226drv_dma_get_dst_write_addr8uint32_t"></a> <a id="drv_dma_get_dst_write_addr__uint32_t"></a> <a id="drv__dma_8h_1a76a3f15129d7a19f5c9626e121e87591"></a> uint32\_t drv\_dma\_get\_dst\_write\_addr(uint32\_t chn\_instance)
:   get destination write address.

    获取此时dma搬移目标的写地址(下一个要写的地址)

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回:
    :   destination write pointer

<a id="_CPPv428drv_dma_flush_unaligned_data8uint32_t"></a>

<a id="_CPPv328drv_dma_flush_unaligned_data8uint32_t"></a> <a id="_CPPv228drv_dma_flush_unaligned_data8uint32_t"></a> <a id="drv_dma_flush_unaligned_data__uint32_t"></a> <a id="drv__dma_8h_1a9cdee8bd2e5dc3301df1f22ff0cd57c7"></a> int32\_t drv\_dma\_flush\_unaligned\_data(uint32\_t chn\_instance)
:   flush unaligned data in dma channel.

    如果因为对齐原因导致dma无法送出部分数据，可以调用该接口

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv438drv_dma_wait_flush_unaligned_data_done8uint32_t"></a>

<a id="_CPPv338drv_dma_wait_flush_unaligned_data_done8uint32_t"></a> <a id="_CPPv238drv_dma_wait_flush_unaligned_data_done8uint32_t"></a> <a id="drv_dma_wait_flush_unaligned_data_done__uint32_t"></a> <a id="drv__dma_8h_1a426ae8f5fde47e719abe47fa07ee06c9"></a> void drv\_dma\_wait\_flush\_unaligned\_data\_done(uint32\_t chn\_instance)
:   wait flush unaligned data finish.

    该函数会阻塞直到dma将flush动作完成，实际上是很快完成的的，通常不会在该函数中while住

    参数:
    :   **chn\_instance** – **\[in\]** return value of [drv\_dma\_chn\_alloc()](#drv__dma_8h_1a223ca2bbec61c0e1280e061f0d758e47)

    返回:
    :   N/A

<a id="_CPPv427drv_dma_get_loop_pause_addr8uint32_t13dma_from_to_e"></a>

<a id="_CPPv327drv_dma_get_loop_pause_addr8uint32_t13dma_from_to_e"></a> <a id="_CPPv227drv_dma_get_loop_pause_addr8uint32_t13dma_from_to_e"></a> <a id="drv_dma_get_loop_pause_addr__uint32_t.dma_from_to_e"></a> <a id="drv__dma_8h_1aaa5f73fe6a866089c862e00db18ba948"></a> int32\_t drv\_dma\_get\_loop\_pause\_addr(uint32\_t chn\_instance, [dma\_from\_to\_e](#_CPPv413dma_from_to_e "dma_from_to_e") e\_src\_dst)
:   drv\_dma\_get\_loop\_pause\_addr brief description

    得到当前的pause地址

    参见

    备注

    参数:
    :   - **chn\_instance** – **\[in\]**
        - **e\_src\_dst** – **\[in\]**

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.DMA_DEVICE_NUM"></a>

<a id="drv__dma_8h_1a3085b64d364a2b4842b8146ec7cce236"></a> DMA\_DEVICE\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410dma_mode_e"></a>

<a id="_CPPv310dma_mode_e"></a> <a id="_CPPv210dma_mode_e"></a> <a id="dma_mode_e"></a> <a id="drv__dma_8h_1ac0d332ae2ac81946973e11f5893ca364"></a> typedef enum [\_dma\_mode\_e](#_CPPv411_dma_mode_e "_dma_mode_e") dma\_mode\_e

<a id="_CPPv413dma_from_to_e"></a>

<a id="_CPPv313dma_from_to_e"></a> <a id="_CPPv213dma_from_to_e"></a> <a id="dma_from_to_e"></a> <a id="drv__dma_8h_1a5f633a52bba78059c0ff21628a692114"></a> typedef enum [\_dma\_from\_to\_e](#_CPPv414_dma_from_to_e "_dma_from_to_e") dma\_from\_to\_e

<a id="_CPPv416dma_data_width_e"></a>

<a id="_CPPv316dma_data_width_e"></a> <a id="_CPPv216dma_data_width_e"></a> <a id="dma_data_width_e"></a> <a id="drv__dma_8h_1a7cc3eaa4b281f7b2029fe7a7e6d9189e"></a> typedef enum [\_dma\_data\_width\_e](#_CPPv417_dma_data_width_e "_dma_data_width_e") dma\_data\_width\_e

<a id="_CPPv416dma_burst_type_e"></a>

<a id="_CPPv316dma_burst_type_e"></a> <a id="_CPPv216dma_burst_type_e"></a> <a id="dma_burst_type_e"></a> <a id="drv__dma_8h_1a99f3ef5b0134dbe73cb5a09dbb417527"></a> typedef enum [\_dma\_burst\_type\_e](#_CPPv417_dma_burst_type_e "_dma_burst_type_e") dma\_burst\_type\_e

<a id="_CPPv414pfunc_dma_cb_t"></a>

<a id="_CPPv314pfunc_dma_cb_t"></a> <a id="_CPPv214pfunc_dma_cb_t"></a> <a id="pfunc_dma_cb_t"></a> <a id="drv__dma_8h_1acd98995b2533a20a6380e35fd7b4f544"></a> typedef void (\*pfunc\_dma\_cb\_t)(uint32\_t chn\_instance, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411_dma_mode_e"></a>

<a id="_CPPv311_dma_mode_e"></a> <a id="_CPPv211_dma_mode_e"></a> <a id="drv__dma_8h_1ac5576dbb6f2757914580242dd72ec76c"></a> enum \_dma\_mode\_e
:   *Values:*

    <a id="_CPPv4N11_dma_mode_e19DRV_DMA_SINGLE_XFERE"></a>

    <a id="_CPPv3N11_dma_mode_e19DRV_DMA_SINGLE_XFERE"></a> <a id="_CPPv2N11_dma_mode_e19DRV_DMA_SINGLE_XFERE"></a> <a id="drv__dma_8h_1ac5576dbb6f2757914580242dd72ec76ca77f7e9160afeea5c20fea8e1331354b8"></a> enumerator DRV\_DMA\_SINGLE\_XFER

    <a id="_CPPv4N11_dma_mode_e19DRV_DMA_LOOP_REPEATE"></a>

    <a id="_CPPv3N11_dma_mode_e19DRV_DMA_LOOP_REPEATE"></a> <a id="_CPPv2N11_dma_mode_e19DRV_DMA_LOOP_REPEATE"></a> <a id="drv__dma_8h_1ac5576dbb6f2757914580242dd72ec76ca7dae6f8679c4f345ca0e36dff1e38db1"></a> enumerator DRV\_DMA\_LOOP\_REPEAT
    :   single transfer

        repeat forever

<a id="_CPPv414_dma_from_to_e"></a>

<a id="_CPPv314_dma_from_to_e"></a> <a id="_CPPv214_dma_from_to_e"></a> <a id="drv__dma_8h_1aa410a302d100ca47009c8b34c3542055"></a> enum \_dma\_from\_to\_e
:   *Values:*

    <a id="_CPPv4N14_dma_from_to_e14DRV_DMA_SOURCEE"></a>

    <a id="_CPPv3N14_dma_from_to_e14DRV_DMA_SOURCEE"></a> <a id="_CPPv2N14_dma_from_to_e14DRV_DMA_SOURCEE"></a> <a id="drv__dma_8h_1aa410a302d100ca47009c8b34c3542055aa395fea664ade32ff389e04f4d36bb0c"></a> enumerator DRV\_DMA\_SOURCE

    <a id="_CPPv4N14_dma_from_to_e19DRV_DMA_DESTINATIONE"></a>

    <a id="_CPPv3N14_dma_from_to_e19DRV_DMA_DESTINATIONE"></a> <a id="_CPPv2N14_dma_from_to_e19DRV_DMA_DESTINATIONE"></a> <a id="drv__dma_8h_1aa410a302d100ca47009c8b34c3542055a2db13aaf428b7b112e66a611cb5bd0c4"></a> enumerator DRV\_DMA\_DESTINATION
    :   from source

        to destination

<a id="_CPPv417_dma_data_width_e"></a>

<a id="_CPPv317_dma_data_width_e"></a> <a id="_CPPv217_dma_data_width_e"></a> <a id="drv__dma_8h_1aaaf156092294f3e86b47876e8bc5736b"></a> enum \_dma\_data\_width\_e
:   *Values:*

    <a id="_CPPv4N17_dma_data_width_e13DRV_DMA_1BYTEE"></a>

    <a id="_CPPv3N17_dma_data_width_e13DRV_DMA_1BYTEE"></a> <a id="_CPPv2N17_dma_data_width_e13DRV_DMA_1BYTEE"></a> <a id="drv__dma_8h_1aaaf156092294f3e86b47876e8bc5736bac810506e5aa70f9d43fadb45ffdbed2b"></a> enumerator DRV\_DMA\_1BYTE

    <a id="_CPPv4N17_dma_data_width_e13DRV_DMA_2BYTEE"></a>

    <a id="_CPPv3N17_dma_data_width_e13DRV_DMA_2BYTEE"></a> <a id="_CPPv2N17_dma_data_width_e13DRV_DMA_2BYTEE"></a> <a id="drv__dma_8h_1aaaf156092294f3e86b47876e8bc5736ba1b197f7c7c995c8930c472125d610f96"></a> enumerator DRV\_DMA\_2BYTE
    :   1byte

    <a id="_CPPv4N17_dma_data_width_e13DRV_DMA_4BYTEE"></a>

    <a id="_CPPv3N17_dma_data_width_e13DRV_DMA_4BYTEE"></a> <a id="_CPPv2N17_dma_data_width_e13DRV_DMA_4BYTEE"></a> <a id="drv__dma_8h_1aaaf156092294f3e86b47876e8bc5736baf4c6c7f2d3128e39c8aec5a430cd61b2"></a> enumerator DRV\_DMA\_4BYTE
    :   2bytes, half word

<a id="_CPPv417_dma_burst_type_e"></a>

<a id="_CPPv317_dma_burst_type_e"></a> <a id="_CPPv217_dma_burst_type_e"></a> <a id="drv__dma_8h_1a4427cfe00a6bb1537f51c31bb13d6d1a"></a> enum \_dma\_burst\_type\_e
:   *Values:*

    <a id="_CPPv4N17_dma_burst_type_e14DRV_DMA_SINGLEE"></a>

    <a id="_CPPv3N17_dma_burst_type_e14DRV_DMA_SINGLEE"></a> <a id="_CPPv2N17_dma_burst_type_e14DRV_DMA_SINGLEE"></a> <a id="drv__dma_8h_1a4427cfe00a6bb1537f51c31bb13d6d1aa2decd5c37d4d54119a2dcbc1b415792c"></a> enumerator DRV\_DMA\_SINGLE

    <a id="_CPPv4N17_dma_burst_type_e14DRV_DMA_4ITEMSE"></a>

    <a id="_CPPv3N17_dma_burst_type_e14DRV_DMA_4ITEMSE"></a> <a id="_CPPv2N17_dma_burst_type_e14DRV_DMA_4ITEMSE"></a> <a id="drv__dma_8h_1a4427cfe00a6bb1537f51c31bb13d6d1aa3d30d1131462ed68181928572caeff2d"></a> enumerator DRV\_DMA\_4ITEMS
    :   single, no burst transfer

    <a id="_CPPv4N17_dma_burst_type_e14DRV_DMA_8ITEMSE"></a>

    <a id="_CPPv3N17_dma_burst_type_e14DRV_DMA_8ITEMSE"></a> <a id="_CPPv2N17_dma_burst_type_e14DRV_DMA_8ITEMSE"></a> <a id="drv__dma_8h_1a4427cfe00a6bb1537f51c31bb13d6d1aa6b69172408cb018d99a0bca262d837af"></a> enumerator DRV\_DMA\_8ITEMS
    :   4 burst at a time

    <a id="_CPPv4N17_dma_burst_type_e15DRV_DMA_16ITEMSE"></a>

    <a id="_CPPv3N17_dma_burst_type_e15DRV_DMA_16ITEMSE"></a> <a id="_CPPv2N17_dma_burst_type_e15DRV_DMA_16ITEMSE"></a> <a id="drv__dma_8h_1a4427cfe00a6bb1537f51c31bb13d6d1aa76e713140c81f7a38791ed8a8e246cce"></a> enumerator DRV\_DMA\_16ITEMS
    :   8 burst at a time
