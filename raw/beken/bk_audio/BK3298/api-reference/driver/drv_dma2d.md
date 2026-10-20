---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_dma2d.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-dma2d"></a>

# DRV\_DMA2D

<a id="drv-dma2d-api-status"></a>

## DRV\_DMA2D API Status

| API |
| --- |
| [`drv_dma2d_init()`](#_CPPv414drv_dma2d_initv "drv_dma2d_init") |
| [`drv_dma2d_deinit()`](#_CPPv416drv_dma2d_deinitv "drv_dma2d_deinit") |
| [`drv_dma2d_init_config()`](#_CPPv421drv_dma2d_init_configP14dma2d_config_t "drv_dma2d_init_config") |
| [`drv_dma2d_layer_config()`](#_CPPv422drv_dma2d_layer_configP14dma2d_config_t13dma2d_layer_e "drv_dma2d_layer_config") |
| [`drv_dma2d_clut_config()`](#_CPPv421drv_dma2d_clut_config16dma2d_clut_cfg_t13dma2d_layer_e "drv_dma2d_clut_config") |
| [`drv_dma2d_transfer_start()`](#_CPPv424drv_dma2d_transfer_startv "drv_dma2d_transfer_start") |
| [`drv_dma2d_transfer_stop()`](#_CPPv423drv_dma2d_transfer_stopv "drv_dma2d_transfer_stop") |
| [`drv_dma2d_transfer_suspend()`](#_CPPv426drv_dma2d_transfer_suspendb "drv_dma2d_transfer_suspend") |
| [`drv_dma2d_transfer_abort()`](#_CPPv424drv_dma2d_transfer_abortb "drv_dma2d_transfer_abort") |
| [`drv_dma2d_is_transfer_done()`](#_CPPv426drv_dma2d_is_transfer_donev "drv_dma2d_is_transfer_done") |
| [`drv_dma2d_blending_config()`](#_CPPv425drv_dma2d_blending_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t "drv_dma2d_blending_config") |
| [`drv_dma2d_line_Watermar_set()`](#_CPPv427drv_dma2d_line_Watermar_set8uint32_t "drv_dma2d_line_Watermar_set") |
| [`drv_dma2d_interrupt_enable()`](#_CPPv426drv_dma2d_interrupt_enable16dma2d_int_type_eb "drv_dma2d_interrupt_enable") |
| [`drv_dma2d_interrupt_callback_register()`](#_CPPv437drv_dma2d_interrupt_callback_register20pfunc_drv_dma2d_cb_tPv "drv_dma2d_interrupt_callback_register") |

<a id="drv-dma2d-api-reference"></a>

## DRV\_DMA2D API Reference

<a id="header-file"></a>

### Header File

- [driver/dma2d/drv\_dma2d.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/dma2d/drv_dma2d.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_dma2d_initv"></a>

<a id="_CPPv314drv_dma2d_initv"></a> <a id="_CPPv214drv_dma2d_initv"></a> <a id="drv_dma2d_init__void"></a> <a id="drv__dma2d_8h_1a0a815b73c0b09f59abbf567a43174c0b"></a> int32\_t drv\_dma2d\_init(void)
:   open DMA2D peripheral clock soft reset dma2d device

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_dma2d_deinitv"></a>

<a id="_CPPv316drv_dma2d_deinitv"></a> <a id="_CPPv216drv_dma2d_deinitv"></a> <a id="drv_dma2d_deinit__void"></a> <a id="drv__dma2d_8h_1a62812fbfc757ebbfe5d9ecd9cd33c21f"></a> int32\_t drv\_dma2d\_deinit(void)
:   Deinitializes the DMA2D peripheral registers to their default reset values. close dma2d interrupt.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_dma2d_init_configP14dma2d_config_t"></a>

<a id="_CPPv321drv_dma2d_init_configP14dma2d_config_t"></a> <a id="_CPPv221drv_dma2d_init_configP14dma2d_config_t"></a> <a id="drv_dma2d_init_config__dma2d_config_tP"></a> <a id="drv__dma2d_8h_1ae382c648eefd36702e0021a5cc71ccfc"></a> int32\_t drv\_dma2d\_init\_config([dma2d\_config\_t](#_CPPv414dma2d_config_t "dma2d_config_t") \*p\_config)
:   config dma2d work mode/ data format/ offset etc.

    you can reference cli\_dma2d.c for all API usage

    Usage example:

    ```
           dma2d_config_t dma2d_config = {0};
           dma2d_config.init_cfg.mode = DMA2D_R2M;                     Mode Register to Memory
           dma2d_config.init_cfg.color_mode = DMA2D_OUTPUT_RGB565;       DMA2D Output color mode is ARGB4444 (16 bpp)
           dma2d_config.init_cfg.output_offset = 0;            No offset in output
           dma2d_config.init_cfg.red_blue_swap = DMA2D_RB_REGULAR;       No R&B swap for the output image
           dma2d_config.init_cfg.alpha_inverted = DMA2D_REGULAR_ALPHA;   No alpha inversion for the output image
           drv_dma2d_init_config(&dma2d_config);
    ```

    参数:
    :   **dma2d\_config** – **\[in\]** pointer to a [dma2d\_config\_t](#structdma2d__config__t) structure that contains the configuration information for the DMA2D.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_dma2d_layer_configP14dma2d_config_t13dma2d_layer_e"></a>

<a id="_CPPv322drv_dma2d_layer_configP14dma2d_config_t13dma2d_layer_e"></a> <a id="_CPPv222drv_dma2d_layer_configP14dma2d_config_t13dma2d_layer_e"></a> <a id="drv_dma2d_layer_config__dma2d_config_tP.dma2d_layer_e"></a> <a id="drv__dma2d_8h_1af104cc45300c2e0be9add27c7491eb35"></a> int32\_t drv\_dma2d\_layer\_config([dma2d\_config\_t](#_CPPv414dma2d_config_t "dma2d_config_t") \*p\_config, [dma2d\_layer\_e](#_CPPv413dma2d_layer_e "dma2d_layer_e") LayerIdx)
:   Configure the DMA2D background or foreground Layer include layer offset, color mode, alpha value etc.

    Usage example:

    ```
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].alpha_mode = DMA2D_REPLACE_ALPHA;
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].input_alpha = alpha_value;
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].input_color_mode = DMA2D_INPUT_RGB565;
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].input_offset = fg_offline;
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].red_blue_swap  = DMA2D_RB_REGULAR;
           dma2d_config.layer_cfg[DMA2D_FOREGROUND_LAYER].alpha_inverted = DMA2D_REGULAR_ALPHA;

           Background layer Configuration
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].alpha_mode  = DMA2D_REPLACE_ALPHA;
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].input_alpha   = 0x80;
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].input_color_mode = DMA2D_INPUT_RGB565;
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].input_offset   = bg_offline;
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].red_blue_swap   = DMA2D_RB_REGULAR;
           dma2d_config.layer_cfg[DMA2D_BACKGROUND_LAYER].alpha_inverted  = DMA2D_REGULAR_ALPHA;

           bk_dma2d_layer_config(&dma2d_config, DMA2D_FOREGROUND_LAYER);
           bk_dma2d_layer_config(&dma2d_config, DMA2D_BACKGROUND_LAYER);
    ```

    参数:
    :   - **dma2d** – **\[in\]** Pointer to a [dma2d\_config\_t](#structdma2d__config__t) structure that contains the configuration information for the DMA2D.
        - **LayerIdx** – **\[in\]** DMA2D Layer index. This parameter can be one of the following values: DMA2D\_BACKGROUND\_LAYER(0) / DMA2D\_FOREGROUND\_LAYER(1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_dma2d_transfer_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv325drv_dma2d_transfer_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv225drv_dma2d_transfer_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="drv_dma2d_transfer_config__dma2d_config_tP.uint32_t.uint32_t.uint32_t.uint32_t"></a> <a id="drv__dma2d_8h_1a81690be2f9dc67790f118f7293f03ff1"></a> int32\_t drv\_dma2d\_transfer\_config([dma2d\_config\_t](#_CPPv414dma2d_config_t "dma2d_config_t") \*p\_config, uint32\_t src\_addr, uint32\_t dst\_addr, uint32\_t width, uint32\_t height)
:   Configure the DMA2D Transfer when you use (drv\_dma2d\_init\_config) and (bk\_dma2d\_layer\_config) API, then use this API start dma2d work.

    Usage example:

    ```
           dma2d_config_t dma2d_config = {0};
           dma2d_config.init_cfg.mode   = DMA2D_R2M;                     Mode Register to Memory
           dma2d_config.init_cfg.color_mode = DMA2D_OUTPUT_RGB565;       DMA2D Output color mode is ARGB4444 (16 bpp)
           dma2d_config.init_cfg.output_offset = 0;          No offset in output
           dma2d_config.init_cfg.red_blue_swap = DMA2D_RB_REGULAR;       No R&B swap for the output image
           dma2d_config.init_cfg.alpha_inverted = DMA2D_REGULAR_ALPHA;   No alpha inversion for the output image

           drv_dma2d_init_config(&dma2d_config);
           bk_dma2d_layer_config(&dma2d_config, color, (uint32_t)dst_addr, width, high);
           drv_dma2d_transfer_start();
    ```

    参数:
    :   - **dma2d** – **\[in\]** Pointer to a [dma2d\_config\_t](#structdma2d__config__t) structure that contains the configuration information for the DMA2D.
        - **src\_addr** – **\[in\]** have two means:

          - 1: if the Memory-to-Memory or Memory-to-Memory with pixel format select, should Configure the source memory Buffer address
          - 2: if Register-to-Memory mode is selected, should configure the color value
        - **dst\_addr** – **\[in\]** The destination memory Buffer address.
        - **Width** – **\[in\]** The width of data to be transferred from source to destination (expressed in number of pixels per line).
        - **Height** – **\[in\]** The height of data to be transferred from source to destination (expressed in number of lines).

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_dma2d_clut_config16dma2d_clut_cfg_t13dma2d_layer_e"></a>

<a id="_CPPv321drv_dma2d_clut_config16dma2d_clut_cfg_t13dma2d_layer_e"></a> <a id="_CPPv221drv_dma2d_clut_config16dma2d_clut_cfg_t13dma2d_layer_e"></a> <a id="drv_dma2d_clut_config__dma2d_clut_cfg_t.dma2d_layer_e"></a> <a id="drv__dma2d_8h_1a9495656fab263173de167fdf78975870"></a> int32\_t drv\_dma2d\_clut\_config([dma2d\_clut\_cfg\_t](#_CPPv416dma2d_clut_cfg_t "dma2d_clut_cfg_t") clut\_cfg, [dma2d\_layer\_e](#_CPPv413dma2d_layer_e "dma2d_layer_e") LayerIdx)
:   Configure the DMA2D CLUT Transfer.

    API obsolete and maintained for compatibility with legacy. User is invited to resort to HAL\_DMA2D\_CLUTStartLoad() instead to benefit from code compactness, code size and improved heap usage.

    参数:
    :   - **dma2d** – **\[in\]** Pointer to a [dma2d\_config\_t](#structdma2d__config__t) structure that contains the configuration information for the DMA2D.
        - **CLUTCfg** – **\[in\]** Pointer to a DMA2D\_CLUTCfgTypeDef structure that contains the configuration information for the color look up table.
        - **LayerIdx** – **\[in\]** DMA2D Layer index. This parameter can be one of the following values: DMA2D\_BACKGROUND\_LAYER(0) / DMA2D\_FOREGROUND\_LAYER(1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_dma2d_transfer_startv"></a>

<a id="_CPPv324drv_dma2d_transfer_startv"></a> <a id="_CPPv224drv_dma2d_transfer_startv"></a> <a id="drv_dma2d_transfer_start__void"></a> <a id="drv__dma2d_8h_1a7d3be7d66e076e15fc8439bd6d6c9071"></a> int32\_t drv\_dma2d\_transfer\_start(void)
:   Start the DMA2D Transfer when config dma2d finshed, then should use this function to start transfer.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_dma2d_transfer_stopv"></a>

<a id="_CPPv323drv_dma2d_transfer_stopv"></a> <a id="_CPPv223drv_dma2d_transfer_stopv"></a> <a id="drv_dma2d_transfer_stop__void"></a> <a id="drv__dma2d_8h_1a41a4db3674ad22f7e7dd9d8613d81fea"></a> int32\_t drv\_dma2d\_transfer\_stop(void)
:   stop the DMA2D Transfer

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_dma2d_transfer_suspendb"></a>

<a id="_CPPv326drv_dma2d_transfer_suspendb"></a> <a id="_CPPv226drv_dma2d_transfer_suspendb"></a> <a id="drv_dma2d_transfer_suspend__b"></a> <a id="drv__dma2d_8h_1ab014eb4d88ce9aa8d74a1fe4c4a235e3"></a> int32\_t drv\_dma2d\_transfer\_suspend(bool xfer\_suspend)
:   suspend the DMA2D Transfer

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_dma2d_transfer_abortb"></a>

<a id="_CPPv324drv_dma2d_transfer_abortb"></a> <a id="_CPPv224drv_dma2d_transfer_abortb"></a> <a id="drv_dma2d_transfer_abort__b"></a> <a id="drv__dma2d_8h_1a018e9c54dcf1175eb7334e72ee27a453"></a> int32\_t drv\_dma2d\_transfer\_abort(bool xfer\_abort)
:   abort the DMA2D Transfer

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_dma2d_is_transfer_donev"></a>

<a id="_CPPv326drv_dma2d_is_transfer_donev"></a> <a id="_CPPv226drv_dma2d_is_transfer_donev"></a> <a id="drv_dma2d_is_transfer_done__void"></a> <a id="drv__dma2d_8h_1aea8b3c9d659724e25e47d30b3b6b8087"></a> bool drv\_dma2d\_is\_transfer\_done(void)
:   check dma2d is transfer busy or not

    返回值:
    :   - **0** – transfer stop or transfer done;
        - **1** – dma2d is work or transfer not done

    返回:
    :   transfer busy status

<a id="_CPPv425drv_dma2d_blending_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv325drv_dma2d_blending_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv225drv_dma2d_blending_configP14dma2d_config_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="drv_dma2d_blending_config__dma2d_config_tP.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t"></a> <a id="drv__dma2d_8h_1ac1e6b282d773d6150ea42abf3ad00e35"></a> int32\_t drv\_dma2d\_blending\_config([dma2d\_config\_t](#_CPPv414dma2d_config_t "dma2d_config_t") \*p\_config, uint32\_t src\_addr1, uint32\_t src\_addr2, uint32\_t dst\_addr, uint32\_t Width, uint32\_t Height)
:   Start the multi-source DMA2D Transfer with interrupt enabled.

    参数:
    :   - **dma2d** – Pointer to a [dma2d\_config\_t](#structdma2d__config__t) structure that contains the configuration information for the DMA2D.
        - **src\_addr1** – **\[in\]** The source memory Buffer address for the foreground layer.
        - **src\_addr2** – **\[in\]** The source memory Buffer address for the background layer.
        - **dst\_addr** – **\[in\]** The destination memory Buffer address.
        - **Width** – **\[in\]** The width of data to be transferred from source to destination (expressed in number of pixels per line).
        - **Height** – **\[in\]** The height of data to be transferred from source to destination (expressed in number of lines).

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_dma2d_line_Watermar_set8uint32_t"></a>

<a id="_CPPv327drv_dma2d_line_Watermar_set8uint32_t"></a> <a id="_CPPv227drv_dma2d_line_Watermar_set8uint32_t"></a> <a id="drv_dma2d_line_Watermar_set__uint32_t"></a> <a id="drv__dma2d_8h_1ad4e69dc39e5bd79566b814c21bc18823"></a> int32\_t drv\_dma2d\_line\_Watermar\_set(uint32\_t line)
:   set the line watermark.

    dma2d\_hal\_line\_Watermar\_cfg() API used with the transfer watermark interrupt. The transfer watermark interrupt is disabled once it has occurred.

    参数:
    :   **line** – **\[in\]** Line Watermark configuration (maximum 16-bit long value expected).

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_dma2d_interrupt_enable16dma2d_int_type_eb"></a>

<a id="_CPPv326drv_dma2d_interrupt_enable16dma2d_int_type_eb"></a> <a id="_CPPv226drv_dma2d_interrupt_enable16dma2d_int_type_eb"></a> <a id="drv_dma2d_interrupt_enable__dma2d_int_type_e.b"></a> <a id="drv__dma2d_8h_1afba350867b8d2b7b9f3eb2b913850460"></a> int32\_t drv\_dma2d\_interrupt\_enable([dma2d\_int\_type\_e](#_CPPv416dma2d_int_type_e "dma2d_int_type_e") int\_type, bool enable)
:   dma2d int enable.

    Usage example:

    ```
           drv_dma2d_interrupt_enable(DMA2D_TRANS_ERROR | DMA2D_TRANS_COMPLETE ,1);
    ```

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

<a id="_CPPv437drv_dma2d_interrupt_callback_register20pfunc_drv_dma2d_cb_tPv"></a>

<a id="_CPPv337drv_dma2d_interrupt_callback_register20pfunc_drv_dma2d_cb_tPv"></a> <a id="_CPPv237drv_dma2d_interrupt_callback_register20pfunc_drv_dma2d_cb_tPv"></a> <a id="drv_dma2d_interrupt_callback_register__pfunc_drv_dma2d_cb_t.voidP"></a> <a id="drv__dma2d_8h_1a1bc16f49322e84dcce405852b7638744"></a> int32\_t drv\_dma2d\_interrupt\_callback\_register([pfunc\_drv\_dma2d\_cb\_t](#_CPPv420pfunc_drv_dma2d_cb_t "pfunc_drv_dma2d_cb_t") pfn\_cb, void \*pv\_arg)
:   register dma2d interrupt callback function

    参数:
    :   - **pfn\_cb** – **\[in\]** callback function
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv416dma2d_init_cfg_t"></a>

<a id="_CPPv316dma2d_init_cfg_t"></a> <a id="_CPPv216dma2d_init_cfg_t"></a> <a id="dma2d_init_cfg_t"></a> <a id="structdma2d__init__cfg__t"></a> struct dma2d\_init\_cfg\_t
:   DMA2D Init structure definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16dma2d_init_cfg_t4modeE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t4modeE"></a> <a id="_CPPv2N16dma2d_init_cfg_t4modeE"></a> <a id="dma2d_init_cfg_t::mode__dma2d_mode_e"></a> <a id="structdma2d__init__cfg__t_1a4038fe002c6d750421d86d38d9f52798"></a> [dma2d\_mode\_e](#_CPPv412dma2d_mode_e "dma2d_mode_e") mode
    :   Configures the DMA2D transfer mode.his parameter can be one value of DMA2D\_Mode.

    <a id="_CPPv4N16dma2d_init_cfg_t10color_modeE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t10color_modeE"></a> <a id="_CPPv2N16dma2d_init_cfg_t10color_modeE"></a> <a id="dma2d_init_cfg_t::color_mode__uint32_t"></a> <a id="structdma2d__init__cfg__t_1a647c3ce68cb429d64e6cb8d51014baa4"></a> uint32\_t color\_mode
    :   Configures the color format of the output image. This parameter can be one value of DMA2D\_Output\_Color\_Mode.

    <a id="_CPPv4N16dma2d_init_cfg_t13output_offsetE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t13output_offsetE"></a> <a id="_CPPv2N16dma2d_init_cfg_t13output_offsetE"></a> <a id="dma2d_init_cfg_t::output_offset__uint32_t"></a> <a id="structdma2d__init__cfg__t_1aa9288d5f662f5a0f5b4343cfa6b69c41"></a> uint32\_t output\_offset
    :   Specifies the Offset value. This parameter must be a number between Min\_Data \= 0x0000 and Max\_Data \= 0x3FFF.

    <a id="_CPPv4N16dma2d_init_cfg_t14alpha_invertedE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t14alpha_invertedE"></a> <a id="_CPPv2N16dma2d_init_cfg_t14alpha_invertedE"></a> <a id="dma2d_init_cfg_t::alpha_inverted__uint32_t"></a> <a id="structdma2d__init__cfg__t_1a59a617e43805abf1e0b0c1df6651d5db"></a> uint32\_t alpha\_inverted
    :   Select regular or inverted alpha value for the output pixel format converter. This parameter can be one value of DMA2D\_Alpha\_Inverted.

    <a id="_CPPv4N16dma2d_init_cfg_t16line_offset_modeE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t16line_offset_modeE"></a> <a id="_CPPv2N16dma2d_init_cfg_t16line_offset_modeE"></a> <a id="dma2d_init_cfg_t::line_offset_mode__uint32_t"></a> <a id="structdma2d__init__cfg__t_1a4ac1867578de782b18b9b60c423c17d1"></a> uint32\_t line\_offset\_mode
    :   Configures how is expressed the line offset for the foreground, background and output. This parameter can be one value of DMA2D\_Line\_Offset\_Mode.

    <a id="_CPPv4N16dma2d_init_cfg_t13red_blue_swapE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t13red_blue_swapE"></a> <a id="_CPPv2N16dma2d_init_cfg_t13red_blue_swapE"></a> <a id="dma2d_init_cfg_t::red_blue_swap__red_blue_swap_e"></a> <a id="structdma2d__init__cfg__t_1a8b98ec0421f55500103964f701b095a8"></a> [red\_blue\_swap\_e](#_CPPv415red_blue_swap_e "red_blue_swap_e") red\_blue\_swap
    :   Select regular mode (RGB or ARGB) or swap mode (BGR or ABGR) for the output pixel format converter. This parameter can be one value of DMA2D\_RB\_Swap.

    <a id="_CPPv4N16dma2d_init_cfg_t12data_reverseE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t12data_reverseE"></a> <a id="_CPPv2N16dma2d_init_cfg_t12data_reverseE"></a> <a id="dma2d_init_cfg_t::data_reverse__rgb888_dataout_reverse_e"></a> <a id="structdma2d__init__cfg__t_1acb0e6c7b09df3e4f0c577bf49873b529"></a> [rgb888\_dataout\_reverse\_e](#_CPPv424rgb888_dataout_reverse_e "rgb888_dataout_reverse_e") data\_reverse
    :   in output rgb888 formart, reverse data byte by byte..

    <a id="_CPPv4N16dma2d_init_cfg_t13trans_abilityE"></a>

    <a id="_CPPv3N16dma2d_init_cfg_t13trans_abilityE"></a> <a id="_CPPv2N16dma2d_init_cfg_t13trans_abilityE"></a> <a id="dma2d_init_cfg_t::trans_ability__dma2d_trans_ability_e"></a> <a id="structdma2d__init__cfg__t_1a7d4300dd9c80722a09dc2afcf4d94847"></a> [dma2d\_trans\_ability\_e](#_CPPv421dma2d_trans_ability_e "dma2d_trans_ability_e") trans\_ability
    :   set defult MAX\_TRANS\_256BYTES

<a id="_CPPv417dma2d_layer_cfg_t"></a>

<a id="_CPPv317dma2d_layer_cfg_t"></a> <a id="_CPPv217dma2d_layer_cfg_t"></a> <a id="dma2d_layer_cfg_t"></a> <a id="structdma2d__layer__cfg__t"></a> struct dma2d\_layer\_cfg\_t
:   DMA2D Layer structure definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17dma2d_layer_cfg_t12input_offsetE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t12input_offsetE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t12input_offsetE"></a> <a id="dma2d_layer_cfg_t::input_offset__uint32_t"></a> <a id="structdma2d__layer__cfg__t_1acbeffa0425574bbba06ac27760093af3"></a> uint32\_t input\_offset
    :   Configures the DMA2D foreground or background offset. This parameter must be a number between Min\_Data \= 0x0000 and Max\_Data \= 0x3FFF.

    <a id="_CPPv4N17dma2d_layer_cfg_t16input_color_modeE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t16input_color_modeE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t16input_color_modeE"></a> <a id="dma2d_layer_cfg_t::input_color_mode__uint32_t"></a> <a id="structdma2d__layer__cfg__t_1a90430c0e8335983abef91117b0ac151d"></a> uint32\_t input\_color\_mode
    :   Configures the DMA2D foreground or background color mode. This parameter can be one value of DMA2D\_Input\_Color\_Mode.

    <a id="_CPPv4N17dma2d_layer_cfg_t10alpha_modeE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t10alpha_modeE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t10alpha_modeE"></a> <a id="dma2d_layer_cfg_t::alpha_mode__blend_alpha_mode_e"></a> <a id="structdma2d__layer__cfg__t_1af11ac959f2b85bbd91a49aa2d6fd981a"></a> [blend\_alpha\_mode\_e](#_CPPv418blend_alpha_mode_e "blend_alpha_mode_e") alpha\_mode
    :   Configures the DMA2D foreground or background alpha mode.This parameter can be one value of DMA2D\_Alpha\_Mode.

    <a id="_CPPv4N17dma2d_layer_cfg_t11input_colorE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t11input_colorE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t11input_colorE"></a> <a id="dma2d_layer_cfg_t::input_color__uint32_t"></a> <a id="structdma2d__layer__cfg__t_1a92892df93cc6e80d1eeacc7d14c72f1f"></a> uint32\_t input\_color
    :   Specifies color value in case of A8 or A4 color mode.

        备注

        In case of A8 or A4 color mode (ARGB), this parameter must be a number between Min\_Data \= 0x00000000 and Max\_Data \= 0xFFFFFF where

        - Inputcolor\[16:23\] is the red value RED\[0:7\]
        - Inputcolor\[8:15\] is the green value GREEN\[0:7\]
        - Inputcolor\[0:7\] is the blue value BLUE\[0:7\].

    <a id="_CPPv4N17dma2d_layer_cfg_t14alpha_invertedE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t14alpha_invertedE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t14alpha_invertedE"></a> <a id="dma2d_layer_cfg_t::alpha_inverted__uint32_t"></a> <a id="structdma2d__layer__cfg__t_1ad3dbdf64bd2c2efab11344de7b57501b"></a> uint32\_t alpha\_inverted
    :   Select regular or inverted alpha value.This parameter can be one value of DMA2D\_Alpha\_Inverted.

    <a id="_CPPv4N17dma2d_layer_cfg_t13red_blue_swapE"></a>

    <a id="_CPPv3N17dma2d_layer_cfg_t13red_blue_swapE"></a> <a id="_CPPv2N17dma2d_layer_cfg_t13red_blue_swapE"></a> <a id="dma2d_layer_cfg_t::red_blue_swap__red_blue_swap_e"></a> <a id="structdma2d__layer__cfg__t_1aed5b01918e9435bb438c24913b124e05"></a> [red\_blue\_swap\_e](#_CPPv415red_blue_swap_e "red_blue_swap_e") red\_blue\_swap
    :   Select regular mode (RGB or ARGB) or swap mode (BGR or ABGR). This parameter can be one value of DMA2D\_RB\_Swap.

<a id="_CPPv414dma2d_config_t"></a>

<a id="_CPPv314dma2d_config_t"></a> <a id="_CPPv214dma2d_config_t"></a> <a id="dma2d_config_t"></a> <a id="structdma2d__config__t"></a> struct dma2d\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14dma2d_config_t8init_cfgE"></a>

    <a id="_CPPv3N14dma2d_config_t8init_cfgE"></a> <a id="_CPPv2N14dma2d_config_t8init_cfgE"></a> <a id="dma2d_config_t::init_cfg__dma2d_init_cfg_t"></a> <a id="structdma2d__config__t_1a6b6d762d015789f2ce50876d796b351e"></a> [dma2d\_init\_cfg\_t](#_CPPv416dma2d_init_cfg_t "dma2d_init_cfg_t") init\_cfg
    :   dma2d init config, is the value of struct dma2d\_init\_t

    <a id="_CPPv4N14dma2d_config_t9layer_cfgE"></a>

    <a id="_CPPv3N14dma2d_config_t9layer_cfgE"></a> <a id="_CPPv2N14dma2d_config_t9layer_cfgE"></a> <a id="dma2d_config_t::layer_cfg__dma2d_layer_cfg_tA"></a> <a id="structdma2d__config__t_1ad42aae62c7c3aa32311858a1cc336313"></a> [dma2d\_layer\_cfg\_t](#_CPPv417dma2d_layer_cfg_t "dma2d_layer_cfg_t") layer\_cfg\[MAX\_DMA2D\_LAYER\]
    :   dma2d layer config, is the value of struct [dma2d\_layer\_cfg\_t](#structdma2d__layer__cfg__t) the param MAX\_DMA2D\_LAYER is select from DMA2D\_BACKGROUND\_LAYER and DMA2D\_FOREGROUND\_LAYER

<a id="_CPPv416dma2d_clut_cfg_t"></a>

<a id="_CPPv316dma2d_clut_cfg_t"></a> <a id="_CPPv216dma2d_clut_cfg_t"></a> <a id="dma2d_clut_cfg_t"></a> <a id="structdma2d__clut__cfg__t"></a> struct dma2d\_clut\_cfg\_t
:   DMA2D CLUT Structure definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16dma2d_clut_cfg_t5pclutE"></a>

    <a id="_CPPv3N16dma2d_clut_cfg_t5pclutE"></a> <a id="_CPPv2N16dma2d_clut_cfg_t5pclutE"></a> <a id="dma2d_clut_cfg_t::pclut__uint32_tP"></a> <a id="structdma2d__clut__cfg__t_1aecf5c0502ce5fd104a8ade14e1af0e54"></a> uint32\_t \*pclut
    :   Configures the DMA2D CLUT memory address.

    <a id="_CPPv4N16dma2d_clut_cfg_t15club_color_modeE"></a>

    <a id="_CPPv3N16dma2d_clut_cfg_t15club_color_modeE"></a> <a id="_CPPv2N16dma2d_clut_cfg_t15club_color_modeE"></a> <a id="dma2d_clut_cfg_t::club_color_mode__uint32_t"></a> <a id="structdma2d__clut__cfg__t_1a71bb5eaa6ff2a07bf3e2ba0028767370"></a> uint32\_t club\_color\_mode
    :   Configures the DMA2D CLUT color mode. This parameter can be one value of DMA2D\_CLUT\_CM.

    <a id="_CPPv4N16dma2d_clut_cfg_t4sizeE"></a>

    <a id="_CPPv3N16dma2d_clut_cfg_t4sizeE"></a> <a id="_CPPv2N16dma2d_clut_cfg_t4sizeE"></a> <a id="dma2d_clut_cfg_t::size__uint32_t"></a> <a id="structdma2d__clut__cfg__t_1a51bace6dc3904009269ba51f6f877a64"></a> uint32\_t size
    :   Configures the DMA2D CLUT size. This parameter must be a number between Min\_Data \= 0x00 and Max\_Data \= 0xFF.

<a id="macros"></a>

### Macros

<a id="c.MAX_DMA2D_LAYER"></a>

<a id="drv__dma2d_8h_1a1f76fcd25373b98c2ddd245de4a9c7bd"></a> MAX\_DMA2D\_LAYER
:   DMA2D maximum number of layers

<a id="c.DMA2D_REGULAR_ALPHA"></a>

<a id="drv__dma2d_8h_1a727afc37b9c65346f5bb0bcdfedbb0be"></a> DMA2D\_REGULAR\_ALPHA
:   No modification of the alpha channel value

<a id="c.DMA2D_INVERTED_ALPHA"></a>

<a id="drv__dma2d_8h_1aafd4c3a0adaf2f8a925c3059ead37f7c"></a> DMA2D\_INVERTED\_ALPHA
:   Invert the alpha channel value

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv420pfunc_drv_dma2d_cb_t"></a>

<a id="_CPPv320pfunc_drv_dma2d_cb_t"></a> <a id="_CPPv220pfunc_drv_dma2d_cb_t"></a> <a id="pfunc_drv_dma2d_cb_t"></a> <a id="drv__dma2d_8h_1a6065ad401f4f3d22c06cf507b9838d4b"></a> typedef void (\*pfunc\_drv\_dma2d\_cb\_t)([dm2d\_isr\_id\_e](#_CPPv413dm2d_isr_id_e "dm2d_isr_id_e") isr\_id, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv413dm2d_isr_id_e"></a>

<a id="_CPPv313dm2d_isr_id_e"></a> <a id="_CPPv213dm2d_isr_id_e"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0e"></a> enum dm2d\_isr\_id\_e
:   if USE\_HAL\_DMA2D\_REGISTER\_CALLBACKS \= 1, define int isr register id

    *Values:*

    <a id="_CPPv4N13dm2d_isr_id_e19DMA2D_CFG_ERROR_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e19DMA2D_CFG_ERROR_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e19DMA2D_CFG_ERROR_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0ea2ade09af47d1b4080af5e6d94c1c360b"></a> enumerator DMA2D\_CFG\_ERROR\_ISR

    <a id="_CPPv4N13dm2d_isr_id_e29DMA2D_CLUT_TRANS_COMPLETE_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e29DMA2D_CLUT_TRANS_COMPLETE_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e29DMA2D_CLUT_TRANS_COMPLETE_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0ea1ee51bce10ad0196ad8eeceb16324f0c"></a> enumerator DMA2D\_CLUT\_TRANS\_COMPLETE\_ISR

    <a id="_CPPv4N13dm2d_isr_id_e26DMA2D_CLUT_TRANS_ERROR_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e26DMA2D_CLUT_TRANS_ERROR_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e26DMA2D_CLUT_TRANS_ERROR_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0ea3abda4ecd3cff1b2c82cd58ec6598b79"></a> enumerator DMA2D\_CLUT\_TRANS\_ERROR\_ISR

    <a id="_CPPv4N13dm2d_isr_id_e24DMA2D_WARTERMARK_INT_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e24DMA2D_WARTERMARK_INT_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e24DMA2D_WARTERMARK_INT_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0ea890946575e171c1825bf94a0b45d2947"></a> enumerator DMA2D\_WARTERMARK\_INT\_ISR

    <a id="_CPPv4N13dm2d_isr_id_e24DMA2D_TRANS_COMPLETE_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e24DMA2D_TRANS_COMPLETE_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e24DMA2D_TRANS_COMPLETE_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0eae3ee8176e5b7e0c25c2073d1bd5a1c92"></a> enumerator DMA2D\_TRANS\_COMPLETE\_ISR

    <a id="_CPPv4N13dm2d_isr_id_e21DMA2D_TRANS_ERROR_ISRE"></a>

    <a id="_CPPv3N13dm2d_isr_id_e21DMA2D_TRANS_ERROR_ISRE"></a> <a id="_CPPv2N13dm2d_isr_id_e21DMA2D_TRANS_ERROR_ISRE"></a> <a id="drv__dma2d_8h_1a31a18ba526acd9ff2cb375ab47acdd0ea83cf266c2c127cf8b2fbbd52dfcde596"></a> enumerator DMA2D\_TRANS\_ERROR\_ISR

<a id="_CPPv418blend_alpha_mode_e"></a>

<a id="_CPPv318blend_alpha_mode_e"></a> <a id="_CPPv218blend_alpha_mode_e"></a> <a id="drv__dma2d_8h_1a512a0f840f258e71d77fa10921c2d0a3"></a> enum blend\_alpha\_mode\_e
:   DMA2D alpha mode

    *Values:*

    <a id="_CPPv4N18blend_alpha_mode_e20DMA2D_NO_MODIF_ALPHAE"></a>

    <a id="_CPPv3N18blend_alpha_mode_e20DMA2D_NO_MODIF_ALPHAE"></a> <a id="_CPPv2N18blend_alpha_mode_e20DMA2D_NO_MODIF_ALPHAE"></a> <a id="drv__dma2d_8h_1a512a0f840f258e71d77fa10921c2d0a3a944e897f7c45ab32facc01d4375620cd"></a> enumerator DMA2D\_NO\_MODIF\_ALPHA
    :   define DMA2D Alpha Mode: No modification of the alpha channel value

    <a id="_CPPv4N18blend_alpha_mode_e19DMA2D_REPLACE_ALPHAE"></a>

    <a id="_CPPv3N18blend_alpha_mode_e19DMA2D_REPLACE_ALPHAE"></a> <a id="_CPPv2N18blend_alpha_mode_e19DMA2D_REPLACE_ALPHAE"></a> <a id="drv__dma2d_8h_1a512a0f840f258e71d77fa10921c2d0a3ab4278df22f0b7c1af037a778f8e0a190"></a> enumerator DMA2D\_REPLACE\_ALPHA
    :   Replace original alpha channel value by programmed alpha value

    <a id="_CPPv4N18blend_alpha_mode_e19DMA2D_COMBINE_ALPHAE"></a>

    <a id="_CPPv3N18blend_alpha_mode_e19DMA2D_COMBINE_ALPHAE"></a> <a id="_CPPv2N18blend_alpha_mode_e19DMA2D_COMBINE_ALPHAE"></a> <a id="drv__dma2d_8h_1a512a0f840f258e71d77fa10921c2d0a3ae7704f5083ad09f46ff4f6de512e5c9a"></a> enumerator DMA2D\_COMBINE\_ALPHA
    :   Replace original foreground image alpha channel value by ALPHA\[7:0\] multiplied with original alpha channel value

<a id="_CPPv415red_blue_swap_e"></a>

<a id="_CPPv315red_blue_swap_e"></a> <a id="_CPPv215red_blue_swap_e"></a> <a id="drv__dma2d_8h_1a6b3fc9aadddbf4e314c52980318424d1"></a> enum red\_blue\_swap\_e
:   DMA2D bule swap define

    *Values:*

    <a id="_CPPv4N15red_blue_swap_e16DMA2D_RB_REGULARE"></a>

    <a id="_CPPv3N15red_blue_swap_e16DMA2D_RB_REGULARE"></a> <a id="_CPPv2N15red_blue_swap_e16DMA2D_RB_REGULARE"></a> <a id="drv__dma2d_8h_1a6b3fc9aadddbf4e314c52980318424d1a681cedec1b226d7dd13a5380ef8f9bd1"></a> enumerator DMA2D\_RB\_REGULAR
    :   Select regular mode (RGB or ARGB)

    <a id="_CPPv4N15red_blue_swap_e13DMA2D_RB_SWAPE"></a>

    <a id="_CPPv3N15red_blue_swap_e13DMA2D_RB_SWAPE"></a> <a id="_CPPv2N15red_blue_swap_e13DMA2D_RB_SWAPE"></a> <a id="drv__dma2d_8h_1a6b3fc9aadddbf4e314c52980318424d1a8c41084cb63c180c67254046c6d16931"></a> enumerator DMA2D\_RB\_SWAP
    :   Select swap mode (BGR or ABGR) \* \= 0

<a id="_CPPv413dma2d_layer_e"></a>

<a id="_CPPv313dma2d_layer_e"></a> <a id="_CPPv213dma2d_layer_e"></a> <a id="drv__dma2d_8h_1a6ff38cec780eff0b0133e8f51a3d9ef4"></a> enum dma2d\_layer\_e
:   DMA2D Layer define

    *Values:*

    <a id="_CPPv4N13dma2d_layer_e22DMA2D_BACKGROUND_LAYERE"></a>

    <a id="_CPPv3N13dma2d_layer_e22DMA2D_BACKGROUND_LAYERE"></a> <a id="_CPPv2N13dma2d_layer_e22DMA2D_BACKGROUND_LAYERE"></a> <a id="drv__dma2d_8h_1a6ff38cec780eff0b0133e8f51a3d9ef4ad513832f6ad974060b5fa3907c4f67ef"></a> enumerator DMA2D\_BACKGROUND\_LAYER
    :   DMA2D Background Layer (layer 0\)

    <a id="_CPPv4N13dma2d_layer_e22DMA2D_FOREGROUND_LAYERE"></a>

    <a id="_CPPv3N13dma2d_layer_e22DMA2D_FOREGROUND_LAYERE"></a> <a id="_CPPv2N13dma2d_layer_e22DMA2D_FOREGROUND_LAYERE"></a> <a id="drv__dma2d_8h_1a6ff38cec780eff0b0133e8f51a3d9ef4a7408100c90977b80b4c0f2be6c3723b1"></a> enumerator DMA2D\_FOREGROUND\_LAYER
    :   DMA2D Foreground Layer (layer 1\)

<a id="_CPPv412dma2d_mode_e"></a>

<a id="_CPPv312dma2d_mode_e"></a> <a id="_CPPv212dma2d_mode_e"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889"></a> enum dma2d\_mode\_e
:   DMA2D\_Mode

    *Values:*

    <a id="_CPPv4N12dma2d_mode_e9DMA2D_M2ME"></a>

    <a id="_CPPv3N12dma2d_mode_e9DMA2D_M2ME"></a> <a id="_CPPv2N12dma2d_mode_e9DMA2D_M2ME"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889ab4c23b4221ad43235a0251e1c0ace8b4"></a> enumerator DMA2D\_M2M
    :   DMA2D memory to memory transfer mode

    <a id="_CPPv4N12dma2d_mode_e13DMA2D_M2M_PFCE"></a>

    <a id="_CPPv3N12dma2d_mode_e13DMA2D_M2M_PFCE"></a> <a id="_CPPv2N12dma2d_mode_e13DMA2D_M2M_PFCE"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889af455e3664ff46d21b0140517b5117e09"></a> enumerator DMA2D\_M2M\_PFC
    :   DMA2D memory to memory with pixel format conversion transfer mode

    <a id="_CPPv4N12dma2d_mode_e15DMA2D_M2M_BLENDE"></a>

    <a id="_CPPv3N12dma2d_mode_e15DMA2D_M2M_BLENDE"></a> <a id="_CPPv2N12dma2d_mode_e15DMA2D_M2M_BLENDE"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889aefeff04036abac70f74b476e4be9db39"></a> enumerator DMA2D\_M2M\_BLEND
    :   DMA2D memory to memory with blending transfer mode

    <a id="_CPPv4N12dma2d_mode_e9DMA2D_R2ME"></a>

    <a id="_CPPv3N12dma2d_mode_e9DMA2D_R2ME"></a> <a id="_CPPv2N12dma2d_mode_e9DMA2D_R2ME"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889a224cd974482f6059b0d53952b09d8b81"></a> enumerator DMA2D\_R2M
    :   DMA2D register to memory transfer mode

    <a id="_CPPv4N12dma2d_mode_e18DMA2D_M2M_BLEND_FGE"></a>

    <a id="_CPPv3N12dma2d_mode_e18DMA2D_M2M_BLEND_FGE"></a> <a id="_CPPv2N12dma2d_mode_e18DMA2D_M2M_BLEND_FGE"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889a25316c91e294f4769f6f0ff1a83c79b6"></a> enumerator DMA2D\_M2M\_BLEND\_FG
    :   DMA2D memory to memory with blending transfer mode and fixed color FG

    <a id="_CPPv4N12dma2d_mode_e18DMA2D_M2M_BLEND_BGE"></a>

    <a id="_CPPv3N12dma2d_mode_e18DMA2D_M2M_BLEND_BGE"></a> <a id="_CPPv2N12dma2d_mode_e18DMA2D_M2M_BLEND_BGE"></a> <a id="drv__dma2d_8h_1a174576025c3fa9c7f5b38df409da7889adb4f2ca3726d9535653efbb3d950ef8d"></a> enumerator DMA2D\_M2M\_BLEND\_BG
    :   DMA2D memory to memory with blending transfer mode and fixed color BG

<a id="_CPPv424rgb888_dataout_reverse_e"></a>

<a id="_CPPv324rgb888_dataout_reverse_e"></a> <a id="_CPPv224rgb888_dataout_reverse_e"></a> <a id="drv__dma2d_8h_1abdcf73119f3fee061c293a890f4a253f"></a> enum rgb888\_dataout\_reverse\_e
:   DMA2D reb888 formart data reverse define

    *Values:*

    <a id="_CPPv4N24rgb888_dataout_reverse_e10NO_REVERSEE"></a>

    <a id="_CPPv3N24rgb888_dataout_reverse_e10NO_REVERSEE"></a> <a id="_CPPv2N24rgb888_dataout_reverse_e10NO_REVERSEE"></a> <a id="drv__dma2d_8h_1abdcf73119f3fee061c293a890f4a253fad9e8b8eb800a7a9f3282273f61987e00"></a> enumerator NO\_REVERSE
    :   in output rgb888 formart, not reverse data byte by byte

    <a id="_CPPv4N24rgb888_dataout_reverse_e7REVERSEE"></a>

    <a id="_CPPv3N24rgb888_dataout_reverse_e7REVERSEE"></a> <a id="_CPPv2N24rgb888_dataout_reverse_e7REVERSEE"></a> <a id="drv__dma2d_8h_1abdcf73119f3fee061c293a890f4a253fa906b7cc20b42994dda4da492767c1de9"></a> enumerator REVERSE
    :   in output rgb888 formart, reverse data byte by byte

<a id="_CPPv416out_color_mode_e"></a>

<a id="_CPPv316out_color_mode_e"></a> <a id="_CPPv216out_color_mode_e"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5"></a> enum out\_color\_mode\_e
:   DMA2D\_Output\_Color\_Mode

    *Values:*

    <a id="_CPPv4N16out_color_mode_e21DMA2D_OUTPUT_ARGB8888E"></a>

    <a id="_CPPv3N16out_color_mode_e21DMA2D_OUTPUT_ARGB8888E"></a> <a id="_CPPv2N16out_color_mode_e21DMA2D_OUTPUT_ARGB8888E"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5a8c8e4c059ec93d76aeba77b3ab2e1263"></a> enumerator DMA2D\_OUTPUT\_ARGB8888
    :   ARGB8888 DMA2D color mode

    <a id="_CPPv4N16out_color_mode_e19DMA2D_OUTPUT_RGB888E"></a>

    <a id="_CPPv3N16out_color_mode_e19DMA2D_OUTPUT_RGB888E"></a> <a id="_CPPv2N16out_color_mode_e19DMA2D_OUTPUT_RGB888E"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5ac4640719178927386325412a7e652ab6"></a> enumerator DMA2D\_OUTPUT\_RGB888
    :   RGB888 DMA2D color mode

    <a id="_CPPv4N16out_color_mode_e19DMA2D_OUTPUT_RGB565E"></a>

    <a id="_CPPv3N16out_color_mode_e19DMA2D_OUTPUT_RGB565E"></a> <a id="_CPPv2N16out_color_mode_e19DMA2D_OUTPUT_RGB565E"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5a3f88fe21358f8521c73193e01f9ea5ba"></a> enumerator DMA2D\_OUTPUT\_RGB565
    :   RGB565 DMA2D color mode

    <a id="_CPPv4N16out_color_mode_e21DMA2D_OUTPUT_ARGB1555E"></a>

    <a id="_CPPv3N16out_color_mode_e21DMA2D_OUTPUT_ARGB1555E"></a> <a id="_CPPv2N16out_color_mode_e21DMA2D_OUTPUT_ARGB1555E"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5a269775fb36b22a74db22dfc6365369bf"></a> enumerator DMA2D\_OUTPUT\_ARGB1555
    :   ARGB1555 DMA2D color mode

    <a id="_CPPv4N16out_color_mode_e21DMA2D_OUTPUT_ARGB4444E"></a>

    <a id="_CPPv3N16out_color_mode_e21DMA2D_OUTPUT_ARGB4444E"></a> <a id="_CPPv2N16out_color_mode_e21DMA2D_OUTPUT_ARGB4444E"></a> <a id="drv__dma2d_8h_1a7b4c7970da2bac2f2f7db2fc6ed0d4b5acfab7422b5ad7376de6cb31e0db66b83"></a> enumerator DMA2D\_OUTPUT\_ARGB4444
    :   ARGB4444 DMA2D color mode

<a id="_CPPv418input_color_mode_e"></a>

<a id="_CPPv318input_color_mode_e"></a> <a id="_CPPv218input_color_mode_e"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59e"></a> enum input\_color\_mode\_e
:   DMA2D\_Input\_Color\_Mode

    *Values:*

    <a id="_CPPv4N18input_color_mode_e20DMA2D_INPUT_ARGB8888E"></a>

    <a id="_CPPv3N18input_color_mode_e20DMA2D_INPUT_ARGB8888E"></a> <a id="_CPPv2N18input_color_mode_e20DMA2D_INPUT_ARGB8888E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea21ac464db71c078c0fec407396240e9d"></a> enumerator DMA2D\_INPUT\_ARGB8888
    :   ARGB8888 DMA2D color mode

    <a id="_CPPv4N18input_color_mode_e18DMA2D_INPUT_RGB888E"></a>

    <a id="_CPPv3N18input_color_mode_e18DMA2D_INPUT_RGB888E"></a> <a id="_CPPv2N18input_color_mode_e18DMA2D_INPUT_RGB888E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea6de0d3b45bb036eff87dfdfea70b6a56"></a> enumerator DMA2D\_INPUT\_RGB888
    :   RGB888 DMA2D color mode

    <a id="_CPPv4N18input_color_mode_e18DMA2D_INPUT_RGB565E"></a>

    <a id="_CPPv3N18input_color_mode_e18DMA2D_INPUT_RGB565E"></a> <a id="_CPPv2N18input_color_mode_e18DMA2D_INPUT_RGB565E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea9c5aad132a779d4d25c793c9b5284a5f"></a> enumerator DMA2D\_INPUT\_RGB565
    :   RGB565 DMA2D color mode

    <a id="_CPPv4N18input_color_mode_e20DMA2D_INPUT_ARGB1555E"></a>

    <a id="_CPPv3N18input_color_mode_e20DMA2D_INPUT_ARGB1555E"></a> <a id="_CPPv2N18input_color_mode_e20DMA2D_INPUT_ARGB1555E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ead26602d4750419bf0a4386e102311cf5"></a> enumerator DMA2D\_INPUT\_ARGB1555
    :   ARGB1555 DMA2D color mode

    <a id="_CPPv4N18input_color_mode_e20DMA2D_INPUT_ARGB4444E"></a>

    <a id="_CPPv3N18input_color_mode_e20DMA2D_INPUT_ARGB4444E"></a> <a id="_CPPv2N18input_color_mode_e20DMA2D_INPUT_ARGB4444E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea6845c5d28916eb38d7f1fc91875a2cbb"></a> enumerator DMA2D\_INPUT\_ARGB4444
    :   ARGB4444 DMA2D color mode

    <a id="_CPPv4N18input_color_mode_e14DMA2D_INPUT_L8E"></a>

    <a id="_CPPv3N18input_color_mode_e14DMA2D_INPUT_L8E"></a> <a id="_CPPv2N18input_color_mode_e14DMA2D_INPUT_L8E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea96791c6736d6ac30ac876fbe5e315eb6"></a> enumerator DMA2D\_INPUT\_L8

    <a id="_CPPv4N18input_color_mode_e16DMA2D_INPUT_AL44E"></a>

    <a id="_CPPv3N18input_color_mode_e16DMA2D_INPUT_AL44E"></a> <a id="_CPPv2N18input_color_mode_e16DMA2D_INPUT_AL44E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea537a233ec5470dc2ad69bde0415fabbc"></a> enumerator DMA2D\_INPUT\_AL44

    <a id="_CPPv4N18input_color_mode_e16DMA2D_INPUT_AL88E"></a>

    <a id="_CPPv3N18input_color_mode_e16DMA2D_INPUT_AL88E"></a> <a id="_CPPv2N18input_color_mode_e16DMA2D_INPUT_AL88E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea51cc30807bb6a1ee1ad2152e412083df"></a> enumerator DMA2D\_INPUT\_AL88

    <a id="_CPPv4N18input_color_mode_e14DMA2D_INPUT_L4E"></a>

    <a id="_CPPv3N18input_color_mode_e14DMA2D_INPUT_L4E"></a> <a id="_CPPv2N18input_color_mode_e14DMA2D_INPUT_L4E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea9db488b5acf1f7d10935c98177fbacad"></a> enumerator DMA2D\_INPUT\_L4

    <a id="_CPPv4N18input_color_mode_e14DMA2D_INPUT_A8E"></a>

    <a id="_CPPv3N18input_color_mode_e14DMA2D_INPUT_A8E"></a> <a id="_CPPv2N18input_color_mode_e14DMA2D_INPUT_A8E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea05c690235d572fddddc39fb2ec4e68f7"></a> enumerator DMA2D\_INPUT\_A8

    <a id="_CPPv4N18input_color_mode_e14DMA2D_INPUT_A4E"></a>

    <a id="_CPPv3N18input_color_mode_e14DMA2D_INPUT_A4E"></a> <a id="_CPPv2N18input_color_mode_e14DMA2D_INPUT_A4E"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59ea8f1993a03f955f004b175ac365fc8e50"></a> enumerator DMA2D\_INPUT\_A4

    <a id="_CPPv4N18input_color_mode_e16DMA2D_INPUT_YUYVE"></a>

    <a id="_CPPv3N18input_color_mode_e16DMA2D_INPUT_YUYVE"></a> <a id="_CPPv2N18input_color_mode_e16DMA2D_INPUT_YUYVE"></a> <a id="drv__dma2d_8h_1a4d875a30bf50851f3e079f30b667d59eae017f4ff93c1f84317b4b6ea29f0003f"></a> enumerator DMA2D\_INPUT\_YUYV

<a id="_CPPv416dma2d_int_type_e"></a>

<a id="_CPPv316dma2d_int_type_e"></a> <a id="_CPPv216dma2d_int_type_e"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595"></a> enum dma2d\_int\_type\_e
:   dma2d int type

    *Values:*

    <a id="_CPPv4N16dma2d_int_type_e15DMA2D_CFG_ERRORE"></a>

    <a id="_CPPv3N16dma2d_int_type_e15DMA2D_CFG_ERRORE"></a> <a id="_CPPv2N16dma2d_int_type_e15DMA2D_CFG_ERRORE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a34e43318f2c7f4a8d627121c482ab1ec"></a> enumerator DMA2D\_CFG\_ERROR

    <a id="_CPPv4N16dma2d_int_type_e25DMA2D_CLUT_TRANS_COMPLETEE"></a>

    <a id="_CPPv3N16dma2d_int_type_e25DMA2D_CLUT_TRANS_COMPLETEE"></a> <a id="_CPPv2N16dma2d_int_type_e25DMA2D_CLUT_TRANS_COMPLETEE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a7a063a54163156e5d69bbd2f541b8130"></a> enumerator DMA2D\_CLUT\_TRANS\_COMPLETE

    <a id="_CPPv4N16dma2d_int_type_e22DMA2D_CLUT_TRANS_ERRORE"></a>

    <a id="_CPPv3N16dma2d_int_type_e22DMA2D_CLUT_TRANS_ERRORE"></a> <a id="_CPPv2N16dma2d_int_type_e22DMA2D_CLUT_TRANS_ERRORE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a8219ce7cc6e314e4f189cccbe09c44ff"></a> enumerator DMA2D\_CLUT\_TRANS\_ERROR

    <a id="_CPPv4N16dma2d_int_type_e20DMA2D_WARTERMARK_INTE"></a>

    <a id="_CPPv3N16dma2d_int_type_e20DMA2D_WARTERMARK_INTE"></a> <a id="_CPPv2N16dma2d_int_type_e20DMA2D_WARTERMARK_INTE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a7b9dbb6138ec3e83e5f6bbe38b35fa76"></a> enumerator DMA2D\_WARTERMARK\_INT

    <a id="_CPPv4N16dma2d_int_type_e20DMA2D_TRANS_COMPLETEE"></a>

    <a id="_CPPv3N16dma2d_int_type_e20DMA2D_TRANS_COMPLETEE"></a> <a id="_CPPv2N16dma2d_int_type_e20DMA2D_TRANS_COMPLETEE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a78650903c721e01829672ee824cc6157"></a> enumerator DMA2D\_TRANS\_COMPLETE

    <a id="_CPPv4N16dma2d_int_type_e17DMA2D_TRANS_ERRORE"></a>

    <a id="_CPPv3N16dma2d_int_type_e17DMA2D_TRANS_ERRORE"></a> <a id="_CPPv2N16dma2d_int_type_e17DMA2D_TRANS_ERRORE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595ace29072fa5692d0d883aada80f51be62"></a> enumerator DMA2D\_TRANS\_ERROR

    <a id="_CPPv4N16dma2d_int_type_e13DMA2D_ALL_INIE"></a>

    <a id="_CPPv3N16dma2d_int_type_e13DMA2D_ALL_INIE"></a> <a id="_CPPv2N16dma2d_int_type_e13DMA2D_ALL_INIE"></a> <a id="drv__dma2d_8h_1a824188cdf394663e10f172a9448d3595a318bdccd4e36d8990c94db36a5e2f254"></a> enumerator DMA2D\_ALL\_INI

<a id="_CPPv418dma2d_int_status_e"></a>

<a id="_CPPv318dma2d_int_status_e"></a> <a id="_CPPv218dma2d_int_status_e"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701"></a> enum dma2d\_int\_status\_e
:   dma2d int status

    *Values:*

    <a id="_CPPv4N18dma2d_int_status_e24DMA2D_TRANS_ERROR_STATUSE"></a>

    <a id="_CPPv3N18dma2d_int_status_e24DMA2D_TRANS_ERROR_STATUSE"></a> <a id="_CPPv2N18dma2d_int_status_e24DMA2D_TRANS_ERROR_STATUSE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701a383e4f485e63621f28745587f56625ac"></a> enumerator DMA2D\_TRANS\_ERROR\_STATUS

    <a id="_CPPv4N18dma2d_int_status_e27DMA2D_TRANS_COMPLETE_STATUSE"></a>

    <a id="_CPPv3N18dma2d_int_status_e27DMA2D_TRANS_COMPLETE_STATUSE"></a> <a id="_CPPv2N18dma2d_int_status_e27DMA2D_TRANS_COMPLETE_STATUSE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701a7b80f49b4d1095e325a76b45129124df"></a> enumerator DMA2D\_TRANS\_COMPLETE\_STATUS

    <a id="_CPPv4N18dma2d_int_status_e27DMA2D_WARTERMARK_INT_STATUSE"></a>

    <a id="_CPPv3N18dma2d_int_status_e27DMA2D_WARTERMARK_INT_STATUSE"></a> <a id="_CPPv2N18dma2d_int_status_e27DMA2D_WARTERMARK_INT_STATUSE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701acfe9e7092b029622687e02fa8b8e0ed6"></a> enumerator DMA2D\_WARTERMARK\_INT\_STATUS

    <a id="_CPPv4N18dma2d_int_status_e29DMA2D_CLUT_TRANS_ERROR_STATUSE"></a>

    <a id="_CPPv3N18dma2d_int_status_e29DMA2D_CLUT_TRANS_ERROR_STATUSE"></a> <a id="_CPPv2N18dma2d_int_status_e29DMA2D_CLUT_TRANS_ERROR_STATUSE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701a3e184134b1353ea3040065d4f9f25ac9"></a> enumerator DMA2D\_CLUT\_TRANS\_ERROR\_STATUS

    <a id="_CPPv4N18dma2d_int_status_e31DMA2D_CLUT_TRANS_COMPLETE_STATUE"></a>

    <a id="_CPPv3N18dma2d_int_status_e31DMA2D_CLUT_TRANS_COMPLETE_STATUE"></a> <a id="_CPPv2N18dma2d_int_status_e31DMA2D_CLUT_TRANS_COMPLETE_STATUE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701a9a646cda23e22e215a07d0a39750f3b0"></a> enumerator DMA2D\_CLUT\_TRANS\_COMPLETE\_STATU

    <a id="_CPPv4N18dma2d_int_status_e22DMA2D_CFG_ERROR_STATUSE"></a>

    <a id="_CPPv3N18dma2d_int_status_e22DMA2D_CFG_ERROR_STATUSE"></a> <a id="_CPPv2N18dma2d_int_status_e22DMA2D_CFG_ERROR_STATUSE"></a> <a id="drv__dma2d_8h_1a8de600a304561f275bb7fcd561f92701a13f702c1c99f5e315695a9e98e030e3b"></a> enumerator DMA2D\_CFG\_ERROR\_STATUS

<a id="_CPPv421dma2d_trans_ability_e"></a>

<a id="_CPPv321dma2d_trans_ability_e"></a> <a id="_CPPv221dma2d_trans_ability_e"></a> <a id="drv__dma2d_8h_1a0dc5b6804c920f59e7f43a687fa00976"></a> enum dma2d\_trans\_ability\_e
:   *Values:*

    <a id="_CPPv4N21dma2d_trans_ability_e18MAX_TRANS_256BYTESE"></a>

    <a id="_CPPv3N21dma2d_trans_ability_e18MAX_TRANS_256BYTESE"></a> <a id="_CPPv2N21dma2d_trans_ability_e18MAX_TRANS_256BYTESE"></a> <a id="drv__dma2d_8h_1a0dc5b6804c920f59e7f43a687fa00976a4a34310917509c731191fa261f9f0da6"></a> enumerator MAX\_TRANS\_256BYTES

    <a id="_CPPv4N21dma2d_trans_ability_e14TRANS_192BYTESE"></a>

    <a id="_CPPv3N21dma2d_trans_ability_e14TRANS_192BYTESE"></a> <a id="_CPPv2N21dma2d_trans_ability_e14TRANS_192BYTESE"></a> <a id="drv__dma2d_8h_1a0dc5b6804c920f59e7f43a687fa00976a65ee4357d006f639043106d25560effc"></a> enumerator TRANS\_192BYTES

    <a id="_CPPv4N21dma2d_trans_ability_e14TRANS_128BYTESE"></a>

    <a id="_CPPv3N21dma2d_trans_ability_e14TRANS_128BYTESE"></a> <a id="_CPPv2N21dma2d_trans_ability_e14TRANS_128BYTESE"></a> <a id="drv__dma2d_8h_1a0dc5b6804c920f59e7f43a687fa00976a49b046d70041dc5036be0b23e70c2f46"></a> enumerator TRANS\_128BYTES

    <a id="_CPPv4N21dma2d_trans_ability_e13TRANS_64BYTESE"></a>

    <a id="_CPPv3N21dma2d_trans_ability_e13TRANS_64BYTESE"></a> <a id="_CPPv2N21dma2d_trans_ability_e13TRANS_64BYTESE"></a> <a id="drv__dma2d_8h_1a0dc5b6804c920f59e7f43a687fa00976a1baa4ef777ac4fc68537c11a224b97db"></a> enumerator TRANS\_64BYTES
