---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_dma2d.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-dma2d"></a>

# BK\_DMA2D

<a id="bk-dma2d-api-status"></a>

## BK\_DMA2D API Status

| API |
| --- |
| [`bk_dma2d_init()`](#_CPPv413bk_dma2d_initv "bk_dma2d_init") |
| [`bk_dma2d_deinit()`](#_CPPv415bk_dma2d_deinitv "bk_dma2d_deinit") |
| [`bk_dma2d_int_enable()`](#_CPPv419bk_dma2d_int_enable16dma2d_int_type_eb "bk_dma2d_int_enable") |
| [`bk_dma2d_register_int_callback_isr()`](#_CPPv434bk_dma2d_register_int_callback_isr13dm2d_isr_id_e19pfunc_bk_dma2d_cb_tPv "bk_dma2d_register_int_callback_isr") |
| [`bk_dma2d_memcpy()`](#_CPPv415bk_dma2d_memcpyP17bk_dma2d_memcpy_t "bk_dma2d_memcpy") |
| [`bk_dma2d_pixel_convert()`](#_CPPv422bk_dma2d_pixel_convertP24bk_dma2d_pixel_convert_t "bk_dma2d_pixel_convert") |
| [`bk_dma2d_blend()`](#_CPPv414bk_dma2d_blendP16bk_dma2d_blend_t "bk_dma2d_blend") |
| [`bk_dma2d_fill()`](#_CPPv413bk_dma2d_fillP15bk_dma2d_fill_t "bk_dma2d_fill") |
| [`bk_dma2d_is_transfer_busy()`](#_CPPv425bk_dma2d_is_transfer_busyv "bk_dma2d_is_transfer_busy") |

<a id="bk-dma2d-api-reference"></a>

## BK\_DMA2D API Reference

<a id="header-file"></a>

### Header File

- [component/dma2d/bk\_dma2d.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/dma2d/bk_dma2d.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413bk_dma2d_initv"></a>

<a id="_CPPv313bk_dma2d_initv"></a> <a id="_CPPv213bk_dma2d_initv"></a> <a id="bk_dma2d_init__void"></a> <a id="bk__dma2d_8h_1a296477ccc43de55322c51439e04bfd9d"></a> int32\_t bk\_dma2d\_init(void)
:   Deinitializes the DMA2D peripheral registers to their default reset values.

    - reset the dma2d driver init reg

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415bk_dma2d_deinitv"></a>

<a id="_CPPv315bk_dma2d_deinitv"></a> <a id="_CPPv215bk_dma2d_deinitv"></a> <a id="bk_dma2d_deinit__void"></a> <a id="bk__dma2d_8h_1a2fef2ee253a7e8b2194dff0d83bc65f7"></a> int32\_t bk\_dma2d\_deinit(void)
:   Deinitializes the DMA2D peripheral registers to their default reset values.

    - reset the dma2d driver init reg

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bk_dma2d_int_enable16dma2d_int_type_eb"></a>

<a id="_CPPv319bk_dma2d_int_enable16dma2d_int_type_eb"></a> <a id="_CPPv219bk_dma2d_int_enable16dma2d_int_type_eb"></a> <a id="bk_dma2d_int_enable__dma2d_int_type_e.b"></a> <a id="bk__dma2d_8h_1a814ea07b348af2675c1865a220933888"></a> int32\_t bk\_dma2d\_int\_enable([dma2d\_int\_type\_e](../driver/drv_dma2d.md#_CPPv416dma2d_int_type_e "dma2d_int_type_e") int\_type, bool enable)
:   dma2d int enable.

    Usage example: bk\_dma2d\_register\_int\_callback\_isr(DMA2D\_CFG\_ERROR\_ISR, function\_cbk, pa\_arg); bk\_dma2d\_register\_int\_callback\_isr(DMA2D\_TRANS\_COMPLETE\_ISR, function\_cbk1, pa\_arg1); bk\_dma2d\_int\_enable(DMA2D\_TRANS\_ERROR \| DMA2D\_TRANS\_COMPLETE ,1);

    参数:
    :   - **int\_type** – **\[in\]** select from dma2d\_int\_type\_t, include int type:

          - DMA2D\_CFG\_ERROR
          - DMA2D\_CLUT\_TRANS\_COMPLETE
          - DMA2D\_CLUT\_TRANS\_ERROR
          - DMA2D\_WARTERMARK\_INT
          - DMA2D\_TRANS\_COMPLETE
          - DMA2D\_TRANS\_ERROR
        - **enable** – **\[in\]** 1:enable int, 0 disable int

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434bk_dma2d_register_int_callback_isr13dm2d_isr_id_e19pfunc_bk_dma2d_cb_tPv"></a>

<a id="_CPPv334bk_dma2d_register_int_callback_isr13dm2d_isr_id_e19pfunc_bk_dma2d_cb_tPv"></a> <a id="_CPPv234bk_dma2d_register_int_callback_isr13dm2d_isr_id_e19pfunc_bk_dma2d_cb_tPv"></a> <a id="bk_dma2d_register_int_callback_isr__dm2d_isr_id_e.pfunc_bk_dma2d_cb_t.voidP"></a> <a id="bk__dma2d_8h_1aa806fed6a4973d990eaace998c83b8d6"></a> int32\_t bk\_dma2d\_register\_int\_callback\_isr([dm2d\_isr\_id\_e](../driver/drv_dma2d.md#_CPPv413dm2d_isr_id_e "dm2d_isr_id_e") isr\_id, [pfunc\_bk\_dma2d\_cb\_t](#_CPPv419pfunc_bk_dma2d_cb_t "pfunc_bk_dma2d_cb_t") cb\_isr, void \*pv\_arg)
:   register dma2d int type isr open the macro #define USE\_HAL\_DMA2D\_REGISTER\_CALLBACKS 1

    参数:
    :   - **isr\_id** – **\[in\]** based on int type, a int type can register a isr, select from: typedef enum { DMA2D\_CFG\_ERROR\_ISR \= 0, DMA2D\_CLUT\_TRANS\_COMPLETE\_ISR, DMA2D\_CLUT\_TRANS\_ERROR\_ISR, DMA2D\_WARTERMARK\_INT\_ISR, DMA2D\_TRANS\_COMPLETE\_ISR, DMA2D\_TRANS\_ERROR\_ISR, }dm2d\_isr\_id;
        - **cb\_isr** – **\[in\]** the user register int callback function
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415bk_dma2d_memcpyP17bk_dma2d_memcpy_t"></a>

<a id="_CPPv315bk_dma2d_memcpyP17bk_dma2d_memcpy_t"></a> <a id="_CPPv215bk_dma2d_memcpyP17bk_dma2d_memcpy_t"></a> <a id="bk_dma2d_memcpy__bk_dma2d_memcpy_tP"></a> <a id="bk__dma2d_8h_1a603108817afc931d7a5e82e31ef48787"></a> int32\_t bk\_dma2d\_memcpy([bk\_dma2d\_memcpy\_t](#_CPPv417bk_dma2d_memcpy_t "bk_dma2d_memcpy_t") \*p\_memcopy)
:   config dma2d memcopy

    参数:
    :   **p\_memcopy** – **\[in\]** [bk\_dma2d\_memcpy\_t](#structbk__dma2d__memcpy__t) struct to config pixel convert params

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bk_dma2d_pixel_convertP24bk_dma2d_pixel_convert_t"></a>

<a id="_CPPv322bk_dma2d_pixel_convertP24bk_dma2d_pixel_convert_t"></a> <a id="_CPPv222bk_dma2d_pixel_convertP24bk_dma2d_pixel_convert_t"></a> <a id="bk_dma2d_pixel_convert__bk_dma2d_pixel_convert_tP"></a> <a id="bk__dma2d_8h_1a017bb5bd509acfd6c305f8dd2e7e8aa7"></a> int32\_t bk\_dma2d\_pixel\_convert([bk\_dma2d\_pixel\_convert\_t](#_CPPv424bk_dma2d_pixel_convert_t "bk_dma2d_pixel_convert_t") \*pixel\_convert)
:   config dma2d pixel revert

    参数:
    :   **pixel\_convert** – **\[in\]** [bk\_dma2d\_pixel\_convert\_t](#structbk__dma2d__pixel__convert__t) struct to config pixel convert params

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414bk_dma2d_blendP16bk_dma2d_blend_t"></a>

<a id="_CPPv314bk_dma2d_blendP16bk_dma2d_blend_t"></a> <a id="_CPPv214bk_dma2d_blendP16bk_dma2d_blend_t"></a> <a id="bk_dma2d_blend__bk_dma2d_blend_tP"></a> <a id="bk__dma2d_8h_1acfb1e570c0f2725ff49c4ac3a8462b3f"></a> int32\_t bk\_dma2d\_blend([bk\_dma2d\_blend\_t](#_CPPv416bk_dma2d_blend_t "bk_dma2d_blend_t") \*dma2d\_blebnd)
:   config dma2d blend

    参数:
    :   **dma2d\_blebnd** – **\[in\]** [bk\_dma2d\_blend\_t](#structbk__dma2d__blend__t) struct to config blend params

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_dma2d_fillP15bk_dma2d_fill_t"></a>

<a id="_CPPv313bk_dma2d_fillP15bk_dma2d_fill_t"></a> <a id="_CPPv213bk_dma2d_fillP15bk_dma2d_fill_t"></a> <a id="bk_dma2d_fill__bk_dma2d_fill_tP"></a> <a id="bk__dma2d_8h_1aa6c5f0efa34471752d1cb715ea175483"></a> int32\_t bk\_dma2d\_fill([bk\_dma2d\_fill\_t](#_CPPv415bk_dma2d_fill_t "bk_dma2d_fill_t") \*fill)
:   config dma2d fill color

    参数:
    :   **fill** – **\[in\]** [bk\_dma2d\_fill\_t](#structbk__dma2d__fill__t) struct to config dma2d fill params

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425bk_dma2d_is_transfer_busyv"></a>

<a id="_CPPv325bk_dma2d_is_transfer_busyv"></a> <a id="_CPPv225bk_dma2d_is_transfer_busyv"></a> <a id="bk_dma2d_is_transfer_busy__void"></a> <a id="bk__dma2d_8h_1ac3efde61ac58e36cb607c1ed0f1e01fb"></a> bool bk\_dma2d\_is\_transfer\_busy(void)
:   this API is check dma2d is transfer busy or not

    返回值:
    :   - **0** – transfer stop or transfer done;
        - **1** – dma2d is work or transfer not done

    返回:
    :   transfer status

<a id="structures"></a>

### Structures

<a id="_CPPv417bk_dma2d_memcpy_t"></a>

<a id="_CPPv317bk_dma2d_memcpy_t"></a> <a id="_CPPv217bk_dma2d_memcpy_t"></a> <a id="bk_dma2d_memcpy_t"></a> <a id="structbk__dma2d__memcpy__t"></a> struct bk\_dma2d\_memcpy\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17bk_dma2d_memcpy_t10input_addrE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t10input_addrE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t10input_addrE"></a> <a id="bk_dma2d_memcpy_t::input_addr__voidP"></a> <a id="structbk__dma2d__memcpy__t_1adcc52b975455b8b4190e806703e0a051"></a> void \*input\_addr
    :   memcpy or partical copy start addr, in other word, the lcd frame addr add offset addr is the start copy addr

    <a id="_CPPv4N17bk_dma2d_memcpy_t11output_addrE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t11output_addrE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t11output_addrE"></a> <a id="bk_dma2d_memcpy_t::output_addr__voidP"></a> <a id="structbk__dma2d__memcpy__t_1a6f21e818d0e2089710b7409016f7678f"></a> void \*output\_addr
    :   memcpy or partical copy dst addr, in other word, the dst frame addr add dst offset addr is the end copy addr

    <a id="_CPPv4N17bk_dma2d_memcpy_t5xsizeE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t5xsizeE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t5xsizeE"></a> <a id="bk_dma2d_memcpy_t::xsize__uint32_t"></a> <a id="structbk__dma2d__memcpy__t_1ade213121ca802010cd09161a8f29366c"></a> uint32\_t xsize
    :   he memcpy or partical copy width

    <a id="_CPPv4N17bk_dma2d_memcpy_t5ysizeE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t5ysizeE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t5ysizeE"></a> <a id="bk_dma2d_memcpy_t::ysize__uint32_t"></a> <a id="structbk__dma2d__memcpy__t_1a42fc52f35857f3e2e7b3b11cdf3f49a7"></a> uint32\_t ysize
    :   the memcpy or partical copy hight

    <a id="_CPPv4N17bk_dma2d_memcpy_t14intput_offlineE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t14intput_offlineE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t14intput_offlineE"></a> <a id="bk_dma2d_memcpy_t::intput_offline__uint32_t"></a> <a id="structbk__dma2d__memcpy__t_1a56fc90e42b71d6a11cd3cff94f09de14"></a> uint32\_t intput\_offline
    :   for partical copy this is to calculate start copy addr based frame addr, uint by pixel

    <a id="_CPPv4N17bk_dma2d_memcpy_t14output_offlineE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t14output_offlineE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t14output_offlineE"></a> <a id="bk_dma2d_memcpy_t::output_offline__uint32_t"></a> <a id="structbk__dma2d__memcpy__t_1abf8a6e31b1bb42eaa3e8001f17ee44ba"></a> uint32\_t output\_offline
    :   for partical copy this is to calculate copy to dst addr based frame addr, uint by pixel

    <a id="_CPPv4N17bk_dma2d_memcpy_t10color_modeE"></a>

    <a id="_CPPv3N17bk_dma2d_memcpy_t10color_modeE"></a> <a id="_CPPv2N17bk_dma2d_memcpy_t10color_modeE"></a> <a id="bk_dma2d_memcpy_t::color_mode__out_color_mode_e"></a> <a id="structbk__dma2d__memcpy__t_1aa776492fa529e8179a6f44c1ba5bef3a"></a> [out\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv416out_color_mode_e "out_color_mode_e") color\_mode
    :   The pixel convert src color mode

<a id="_CPPv424bk_dma2d_pixel_convert_t"></a>

<a id="_CPPv324bk_dma2d_pixel_convert_t"></a> <a id="_CPPv224bk_dma2d_pixel_convert_t"></a> <a id="bk_dma2d_pixel_convert_t"></a> <a id="structbk__dma2d__pixel__convert__t"></a> struct bk\_dma2d\_pixel\_convert\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t10input_addrE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t10input_addrE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t10input_addrE"></a> <a id="bk_dma2d_pixel_convert_t::input_addr__voidP"></a> <a id="structbk__dma2d__pixel__convert__t_1a64b73259a1463cbe43794e12044f2b67"></a> void \*input\_addr
    :   The pixel convert src addr

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t11output_addrE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t11output_addrE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t11output_addrE"></a> <a id="bk_dma2d_pixel_convert_t::output_addr__voidP"></a> <a id="structbk__dma2d__pixel__convert__t_1a8f09c1bede96ca19ccbe575828a10c45"></a> void \*output\_addr
    :   The pixel convert dst addr

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t5xsizeE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t5xsizeE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t5xsizeE"></a> <a id="bk_dma2d_pixel_convert_t::xsize__uint32_t"></a> <a id="structbk__dma2d__pixel__convert__t_1a6380c73efa1454408eb698d1ba612ae0"></a> uint32\_t xsize
    :   image width

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t5ysizeE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t5ysizeE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t5ysizeE"></a> <a id="bk_dma2d_pixel_convert_t::ysize__uint32_t"></a> <a id="structbk__dma2d__pixel__convert__t_1aaea27ac481277dafdbf37ab7eda0a935"></a> uint32\_t ysize
    :   image height

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t16input_color_modeE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t16input_color_modeE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t16input_color_modeE"></a> <a id="bk_dma2d_pixel_convert_t::input_color_mode__input_color_mode_e"></a> <a id="structbk__dma2d__pixel__convert__t_1a57eb13a964ddf9eae32bebf1e581972d"></a> [input\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv418input_color_mode_e "input_color_mode_e") input\_color\_mode
    :   The pixel convert src color mode

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t17output_color_modeE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t17output_color_modeE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t17output_color_modeE"></a> <a id="bk_dma2d_pixel_convert_t::output_color_mode__out_color_mode_e"></a> <a id="structbk__dma2d__pixel__convert__t_1abfa6ee5dffbf6cb3e128d38e1989715b"></a> [out\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv416out_color_mode_e "out_color_mode_e") output\_color\_mode
    :   The pixel convert dst color mode

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t14intput_offlineE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t14intput_offlineE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t14intput_offlineE"></a> <a id="bk_dma2d_pixel_convert_t::intput_offline__uint32_t"></a> <a id="structbk__dma2d__pixel__convert__t_1a1d8cffb0bbc797dbaf644d8ebd45f309"></a> uint32\_t intput\_offline
    :   set src offset addr, mem start addr to pixel convert

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t14output_offlineE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t14output_offlineE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t14output_offlineE"></a> <a id="bk_dma2d_pixel_convert_t::output_offline__uint32_t"></a> <a id="structbk__dma2d__pixel__convert__t_1a828f00b6300524c97d4bc17aa4386fc8"></a> uint32\_t output\_offline
    :   set dst offset addr, write to mem dst addr

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t20intput_red_blue_swapE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t20intput_red_blue_swapE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t20intput_red_blue_swapE"></a> <a id="bk_dma2d_pixel_convert_t::intput_red_blue_swap__red_blue_swap_e"></a> <a id="structbk__dma2d__pixel__convert__t_1a9f4081e9e00d78185c50ff826b19f742"></a> [red\_blue\_swap\_e](../driver/drv_dma2d.md#_CPPv415red_blue_swap_e "red_blue_swap_e") intput\_red\_blue\_swap
    :   src img red blue swap, select DMA2D\_RB\_SWAP or DMA2D\_RB\_REGULAR

    <a id="_CPPv4N24bk_dma2d_pixel_convert_t20output_red_blue_swapE"></a>

    <a id="_CPPv3N24bk_dma2d_pixel_convert_t20output_red_blue_swapE"></a> <a id="_CPPv2N24bk_dma2d_pixel_convert_t20output_red_blue_swapE"></a> <a id="bk_dma2d_pixel_convert_t::output_red_blue_swap__red_blue_swap_e"></a> <a id="structbk__dma2d__pixel__convert__t_1a16535283978e1087e4790a76da8add30"></a> [red\_blue\_swap\_e](../driver/drv_dma2d.md#_CPPv415red_blue_swap_e "red_blue_swap_e") output\_red\_blue\_swap
    :   src img red blue swap, select DMA2D\_RB\_SWAP or DMA2D\_RB\_REGULAR

<a id="_CPPv416bk_dma2d_blend_t"></a>

<a id="_CPPv316bk_dma2d_blend_t"></a> <a id="_CPPv216bk_dma2d_blend_t"></a> <a id="bk_dma2d_blend_t"></a> <a id="structbk__dma2d__blend__t"></a> struct bk\_dma2d\_blend\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16bk_dma2d_blend_t8pfg_addrE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t8pfg_addrE"></a> <a id="_CPPv2N16bk_dma2d_blend_t8pfg_addrE"></a> <a id="bk_dma2d_blend_t::pfg_addr__voidP"></a> <a id="structbk__dma2d__blend__t_1ae1b638edae78664d527c5ff743225435"></a> void \*pfg\_addr
    :   The source memory Buffer address for the foreground layer..

    <a id="_CPPv4N16bk_dma2d_blend_t8pbg_addrE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t8pbg_addrE"></a> <a id="_CPPv2N16bk_dma2d_blend_t8pbg_addrE"></a> <a id="bk_dma2d_blend_t::pbg_addr__voidP"></a> <a id="structbk__dma2d__blend__t_1a62771dfb60c449067a72236c547131a9"></a> void \*pbg\_addr
    :   he source memory Buffer address for the background layer…

    <a id="_CPPv4N16bk_dma2d_blend_t9pdst_addrE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t9pdst_addrE"></a> <a id="_CPPv2N16bk_dma2d_blend_t9pdst_addrE"></a> <a id="bk_dma2d_blend_t::pdst_addr__voidP"></a> <a id="structbk__dma2d__blend__t_1ae64a2be7b94ef61b7c28d8d4ab762b22"></a> void \*pdst\_addr
    :   The output memory Buffer address ..

    <a id="_CPPv4N16bk_dma2d_blend_t13fg_color_modeE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t13fg_color_modeE"></a> <a id="_CPPv2N16bk_dma2d_blend_t13fg_color_modeE"></a> <a id="bk_dma2d_blend_t::fg_color_mode__input_color_mode_e"></a> <a id="structbk__dma2d__blend__t_1a7795c1a524cad5ab6634944a3109f459"></a> [input\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv418input_color_mode_e "input_color_mode_e") fg\_color\_mode
    :   fg color mode..

    <a id="_CPPv4N16bk_dma2d_blend_t13bg_color_modeE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t13bg_color_modeE"></a> <a id="_CPPv2N16bk_dma2d_blend_t13bg_color_modeE"></a> <a id="bk_dma2d_blend_t::bg_color_mode__input_color_mode_e"></a> <a id="structbk__dma2d__blend__t_1a3b909645b9000d6eb7336aaa223ad5d0"></a> [input\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv418input_color_mode_e "input_color_mode_e") bg\_color\_mode
    :   bg color mode..

    <a id="_CPPv4N16bk_dma2d_blend_t14dst_color_modeE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t14dst_color_modeE"></a> <a id="_CPPv2N16bk_dma2d_blend_t14dst_color_modeE"></a> <a id="bk_dma2d_blend_t::dst_color_mode__out_color_mode_e"></a> <a id="structbk__dma2d__blend__t_1a0e012ea518575fd935fa5a8114fb4a3a"></a> [out\_color\_mode\_e](../driver/drv_dma2d.md#_CPPv416out_color_mode_e "out_color_mode_e") dst\_color\_mode
    :   out color mode..

    <a id="_CPPv4N16bk_dma2d_blend_t10fg_offlineE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t10fg_offlineE"></a> <a id="_CPPv2N16bk_dma2d_blend_t10fg_offlineE"></a> <a id="bk_dma2d_blend_t::fg_offline__uint32_t"></a> <a id="structbk__dma2d__blend__t_1acd9c93ad61b2dd1f9f67673590ec6fcf"></a> uint32\_t fg\_offline
    :   for partical copy this is to calculate start addr based on fg frame addr, uint by pixel

    <a id="_CPPv4N16bk_dma2d_blend_t10bg_offlineE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t10bg_offlineE"></a> <a id="_CPPv2N16bk_dma2d_blend_t10bg_offlineE"></a> <a id="bk_dma2d_blend_t::bg_offline__uint32_t"></a> <a id="structbk__dma2d__blend__t_1a9b22020458f96c656716a7f71cdde99d"></a> uint32\_t bg\_offline
    :   for partical copy this is to calculate start addr based on bg frame addr, uint by pixel

    <a id="_CPPv4N16bk_dma2d_blend_t12dest_offlineE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t12dest_offlineE"></a> <a id="_CPPv2N16bk_dma2d_blend_t12dest_offlineE"></a> <a id="bk_dma2d_blend_t::dest_offline__uint32_t"></a> <a id="structbk__dma2d__blend__t_1a53719e2e47a56a994f46c9468db9044d"></a> uint32\_t dest\_offline
    :   for partical copy this is to calculate output addr based on dst frame addr, uint by pixel

    <a id="_CPPv4N16bk_dma2d_blend_t5xsizeE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t5xsizeE"></a> <a id="_CPPv2N16bk_dma2d_blend_t5xsizeE"></a> <a id="bk_dma2d_blend_t::xsize__uint32_t"></a> <a id="structbk__dma2d__blend__t_1aad0916834e3081aafb6f4767a79e6253"></a> uint32\_t xsize
    :   dma2d blend x size..

    <a id="_CPPv4N16bk_dma2d_blend_t5ysizeE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t5ysizeE"></a> <a id="_CPPv2N16bk_dma2d_blend_t5ysizeE"></a> <a id="bk_dma2d_blend_t::ysize__uint32_t"></a> <a id="structbk__dma2d__blend__t_1a523941b463dc42d37ac8ad5c7a0e16e0"></a> uint32\_t ysize
    :   dma2d blend y size..

    <a id="_CPPv4N16bk_dma2d_blend_t14fg_alpha_valueE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t14fg_alpha_valueE"></a> <a id="_CPPv2N16bk_dma2d_blend_t14fg_alpha_valueE"></a> <a id="bk_dma2d_blend_t::fg_alpha_value__uint8_t"></a> <a id="structbk__dma2d__blend__t_1ab9bafd08c081203a1b726218fb8c56d8"></a> uint8\_t fg\_alpha\_value
    :   config fg alpha..

    <a id="_CPPv4N16bk_dma2d_blend_t14bg_alpha_valueE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t14bg_alpha_valueE"></a> <a id="_CPPv2N16bk_dma2d_blend_t14bg_alpha_valueE"></a> <a id="bk_dma2d_blend_t::bg_alpha_value__uint8_t"></a> <a id="structbk__dma2d__blend__t_1a811768d5074993576480b338a8b6d4f9"></a> uint8\_t bg\_alpha\_value
    :   config bg alpha.

    <a id="_CPPv4N16bk_dma2d_blend_t13red_bule_swapE"></a>

    <a id="_CPPv3N16bk_dma2d_blend_t13red_bule_swapE"></a> <a id="_CPPv2N16bk_dma2d_blend_t13red_bule_swapE"></a> <a id="bk_dma2d_blend_t::red_bule_swap__red_blue_swap_e"></a> <a id="structbk__dma2d__blend__t_1a71773ce99fe314fb3977e17be5a699de"></a> [red\_blue\_swap\_e](../driver/drv_dma2d.md#_CPPv415red_blue_swap_e "red_blue_swap_e") red\_bule\_swap
    :   DMA2D\_RB\_SWAP or DMA2D\_RB\_REGULAR

<a id="_CPPv415bk_dma2d_fill_t"></a>

<a id="_CPPv315bk_dma2d_fill_t"></a> <a id="_CPPv215bk_dma2d_fill_t"></a> <a id="bk_dma2d_fill_t"></a> <a id="structbk__dma2d__fill__t"></a> struct bk\_dma2d\_fill\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15bk_dma2d_fill_t9frameaddrE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t9frameaddrE"></a> <a id="_CPPv2N15bk_dma2d_fill_t9frameaddrE"></a> <a id="bk_dma2d_fill_t::frameaddr__voidP"></a> <a id="structbk__dma2d__fill__t_1a9a17554f5fcd9878ee01bb0ed647794d"></a> void \*frameaddr
    :   dma2d fill frame baseaddr , normally LCD start frame addr

    <a id="_CPPv4N15bk_dma2d_fill_t11frame_xsizeE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t11frame_xsizeE"></a> <a id="_CPPv2N15bk_dma2d_fill_t11frame_xsizeE"></a> <a id="bk_dma2d_fill_t::frame_xsize__uint16_t"></a> <a id="structbk__dma2d__fill__t_1a719d479c85ac9ac37eb1d8542d3ccadc"></a> uint16\_t frame\_xsize
    :   img/lcd x size

    <a id="_CPPv4N15bk_dma2d_fill_t11frame_ysizeE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t11frame_ysizeE"></a> <a id="_CPPv2N15bk_dma2d_fill_t11frame_ysizeE"></a> <a id="bk_dma2d_fill_t::frame_ysize__uint16_t"></a> <a id="structbk__dma2d__fill__t_1a8174479513b14eddb53839bb07237ab9"></a> uint16\_t frame\_ysize
    :   img/lcd y size

    <a id="_CPPv4N15bk_dma2d_fill_t4xposE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t4xposE"></a> <a id="_CPPv2N15bk_dma2d_fill_t4xposE"></a> <a id="bk_dma2d_fill_t::xpos__uint16_t"></a> <a id="structbk__dma2d__fill__t_1a1f1fbeb969cfd5819af1c84d2da3761e"></a> uint16\_t xpos
    :   dma2d fill x pos based on frame\_xsize

    <a id="_CPPv4N15bk_dma2d_fill_t4yposE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t4yposE"></a> <a id="_CPPv2N15bk_dma2d_fill_t4yposE"></a> <a id="bk_dma2d_fill_t::ypos__uint16_t"></a> <a id="structbk__dma2d__fill__t_1ae6f531064d80e9e68e9e234ac29576a9"></a> uint16\_t ypos
    :   dma2d fill y pos based on frame\_ysize

    <a id="_CPPv4N15bk_dma2d_fill_t5widthE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t5widthE"></a> <a id="_CPPv2N15bk_dma2d_fill_t5widthE"></a> <a id="bk_dma2d_fill_t::width__uint16_t"></a> <a id="structbk__dma2d__fill__t_1ad6e67e5566bbd859016cff6edf04e660"></a> uint16\_t width
    :   dma2d fill width

    <a id="_CPPv4N15bk_dma2d_fill_t4highE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t4highE"></a> <a id="_CPPv2N15bk_dma2d_fill_t4highE"></a> <a id="bk_dma2d_fill_t::high__uint16_t"></a> <a id="structbk__dma2d__fill__t_1abdcaeefba2fafa1b7a09cb3d713df864"></a> uint16\_t high
    :   dma2d fill height

    <a id="_CPPv4N15bk_dma2d_fill_t5colorE"></a>

    <a id="_CPPv3N15bk_dma2d_fill_t5colorE"></a> <a id="_CPPv2N15bk_dma2d_fill_t5colorE"></a> <a id="bk_dma2d_fill_t::color__uint16_t"></a> <a id="structbk__dma2d__fill__t_1a4ded4ebc43e8b4a4b218cd63574ee041"></a> uint16\_t color
    :   dma2d fill color

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv419pfunc_bk_dma2d_cb_t"></a>

<a id="_CPPv319pfunc_bk_dma2d_cb_t"></a> <a id="_CPPv219pfunc_bk_dma2d_cb_t"></a> <a id="pfunc_bk_dma2d_cb_t"></a> <a id="bk__dma2d_8h_1a79f292df785d089781cb14196c38b8ff"></a> typedef void (\*pfunc\_bk\_dma2d\_cb\_t)(void \*pv\_arg)
