---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_jpeg_dec_hw.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-jpeg-dec-hw"></a>

# BK\_JPEG\_DEC\_HW

<a id="bk-jpeg-dec-hw-api-status"></a>

## BK\_JPEG\_DEC\_HW API Status

| API |
| --- |
| [`bk_jpeg_dec_hw_init()`](#_CPPv419bk_jpeg_dec_hw_initv "bk_jpeg_dec_hw_init") |
| [`bk_jpeg_dec_hw_deinit()`](#_CPPv421bk_jpeg_dec_hw_deinitv "bk_jpeg_dec_hw_deinit") |
| [`bk_jpeg_dec_hw_start()`](#_CPPv420bk_jpeg_dec_hw_start8uint32_tPhPh "bk_jpeg_dec_hw_start") |
| [`bk_jpeg_dec_hw_isr_register()`](#_CPPv427bk_jpeg_dec_hw_isr_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t "bk_jpeg_dec_hw_isr_register") |

<a id="bk-jpeg-dec-hw-api-reference"></a>

## BK\_JPEG\_DEC\_HW API Reference

<a id="header-file"></a>

### Header File

- [component/jpeg\_dec\_hw/bk\_jpeg\_dec\_hw.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/jpeg_dec_hw/bk_jpeg_dec_hw.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_jpeg_dec_hw_initv"></a>

<a id="_CPPv319bk_jpeg_dec_hw_initv"></a> <a id="_CPPv219bk_jpeg_dec_hw_initv"></a> <a id="bk_jpeg_dec_hw_init__void"></a> <a id="bk__jpeg__dec__hw_8h_1a2111fafb9cc5e051964a5d4ceffe3b62"></a> int32\_t bk\_jpeg\_dec\_hw\_init(void)
:   init a jpeg decoder device. alloc jpeg decoder work buff alloc dma channel create a sempahore

    BK jpeg硬件解码初始化函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421bk_jpeg_dec_hw_deinitv"></a>

<a id="_CPPv321bk_jpeg_dec_hw_deinitv"></a> <a id="_CPPv221bk_jpeg_dec_hw_deinitv"></a> <a id="bk_jpeg_dec_hw_deinit__void"></a> <a id="bk__jpeg__dec__hw_8h_1a4e8b15480a524b7a72f163215f6dbc7e"></a> int32\_t bk\_jpeg\_dec\_hw\_deinit(void)
:   deinit a jpeg decoder device. free dma channel free a sempahore free jpeg decoder work buff

    BK jpeg硬件解码反初始化函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420bk_jpeg_dec_hw_start8uint32_tPhPh"></a>

<a id="_CPPv320bk_jpeg_dec_hw_start8uint32_tPhPh"></a> <a id="_CPPv220bk_jpeg_dec_hw_start8uint32_tPhPh"></a> <a id="bk_jpeg_dec_hw_start__uint32_t.unsigned-cP.unsigned-cP"></a> <a id="bk__jpeg__dec__hw_8h_1a11481c65a5b883414f8d31b7e43d7971"></a> int32\_t bk\_jpeg\_dec\_hw\_start(uint32\_t length, unsigned char \*input\_buf, unsigned char \*output\_buf)
:   jpeg图片解码函数

    图片数据需要搬运到sram的图片缓存空间中然后再解码。数据是用cpu进行搬运

    参数:
    :   - **length** – **\[in\]** jpeg图片数据大小
        - **input\_buf** – **\[in\]** 指向需要解码的数据空间
        - **output\_buf** – **\[in\]** 指向存储解码数据的空间

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427bk_jpeg_dec_hw_isr_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a>

<a id="_CPPv327bk_jpeg_dec_hw_isr_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a> <a id="_CPPv227bk_jpeg_dec_hw_isr_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a> <a id="bk_jpeg_dec_hw_isr_register__jpeg_dec_hw_isr_type_e.pfunc_drv_jpeg_dec_cb_t"></a> <a id="bk__jpeg__dec__hw_8h_1a4c1b96b05e83982b55887b685f0f6c44"></a> int32\_t bk\_jpeg\_dec\_hw\_isr\_register([jpeg\_dec\_hw\_isr\_type\_e](../driver/drv_jpeg_dec.md#_CPPv422jpeg_dec_hw_isr_type_e "jpeg_dec_hw_isr_type_e") isr\_id, [pfunc\_drv\_jpeg\_dec\_cb\_t](../driver/drv_jpeg_dec.md#_CPPv423pfunc_drv_jpeg_dec_cb_t "pfunc_drv_jpeg_dec_cb_t") cb\_isr)
:   bk register intrrupt callback function

    BK层注册中断回调函数，直接注册到DRV层

    参数:
    :   - **isr\_id** – **\[in\]** DEC\_END\_OF\_FRAME\&#8212;解码完成中断 DEC\_END\_OF\_LINE\_NUM\&#8212;按行解码中断，默认是解码2行来一次中断
        - **pfn\_cb** – **\[in\]** 回调函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.CONFIG_JEEG_DEC_DMA"></a>

<a id="bk__jpeg__dec__hw_8h_1a811962c5ed1c746a40f5a11f8876a5fa"></a> CONFIG\_JEEG\_DEC\_DMA

<a id="c.JPEG_SRAM_ADDRESS"></a>

<a id="bk__jpeg__dec__hw_8h_1ab5a9f4f45d4174f0aaca51ebea2f3e53"></a> JPEG\_SRAM\_ADDRESS
