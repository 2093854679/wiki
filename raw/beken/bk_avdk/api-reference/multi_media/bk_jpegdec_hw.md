# Hardware JPEGDEC APIs[](#hardware-jpegdec-apis "永久链接至标题")



## JPEGDEC API Categories[](#jpegdec-api-categories "永久链接至标题")

JPEGDEC APIs:
:   - [`bk_jpeg_dec_driver_init()`](#_CPPv423bk_jpeg_dec_driver_initv "bk_jpeg_dec_driver_init") - init jpeg decode hardware module

    - [`bk_jpeg_dec_driver_deinit()`](#_CPPv425bk_jpeg_dec_driver_deinitv "bk_jpeg_dec_driver_deinit") - deinit jpeg decode hardware module

    - [`bk_jpeg_dec_hw_start()`](#_CPPv420bk_jpeg_dec_hw_start8uint32_tPhPh "bk_jpeg_dec_hw_start") - start jpeg decode

    - [`bk_jpeg_dec_stop()`](#_CPPv416bk_jpeg_dec_stopv "bk_jpeg_dec_stop") - stop jpeg decode

    - [`bk_jpeg_dec_isr_register()`](#_CPPv424bk_jpeg_dec_isr_register14jpeg_dec_isr_t "bk_jpeg_dec_isr_register") - register jpeg dec complete callback


## HW JPEG DECODE Config[](#hw-jpeg-decode-config "永久链接至标题")

![jpeg dec Overview](../_images/hw_jpeg_decode.png)

Figure 1. jpeg decode config flow[](#id2 "永久链接至图片")


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [jpeg_dec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_dec.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_dec.h")


### Functions[](#functions "永久链接至标题")

bk_err_t bk_jpeg_dec_driver_init(void)[](#_CPPv423bk_jpeg_dec_driver_initv "永久链接至目标")
:   HW JPEG DEC API.

    this api open the jpeg decode clk

bk_err_t bk_jpeg_dec_driver_deinit(void)[](#_CPPv425bk_jpeg_dec_driver_deinitv "永久链接至目标")
:   this api close the jpeg decode clk


    - disable jpeg decode

bk_err_t bk_jpeg_dec_line_int_dis(void)[](#_CPPv424bk_jpeg_dec_line_int_disv "永久链接至目标")
:   this api used for jpeg decode config

    this api used for jpeg decode line interrupt config decode can select a frame complete done isr(defult) , or this decode lin_num enter int isr

    Usage example:

    ```
     if x pixel 320, you set bk_jpeg_dec_line_int_en(32), every 32 line will enter isr, in all ten times
     if x pixel 240, you set bk_jpeg_dec_line_int_en(24), every 24 line will enter isr, in all ten times
    ```

    this api used for disable jpeg decode line num int

    参数
    :   - **xpixel** – jpeg decode picture x pixel

          - input_buf decode input data addr

            - output_buf decode output data addr

        - **lin_num** – decode line num ,should multiple of 8,

    返回
    :   - BK_OK: succeed

        - others: other errors.

    返回

    返回
    :   - BK_OK: succeed

        - others: other errors.

    返回

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_jpeg_dec_hw_start(uint32_t length, unsigned char *input_buf, unsigned char *output_buf)[](#_CPPv420bk_jpeg_dec_hw_start8uint32_tPhPh "永久链接至目标")
:   this api start jpeg decode

    参数
    :   **length** – jpeg length


        - input_buf jpeg data src addr

        - output_buf jpeg decode output addr

    返回
    :   0: jpeg decode ok; others: error

bk_err_t bk_jpeg_dec_dma_start(uint32_t length, unsigned char *input_buf, unsigned char *output_buf)[](#_CPPv421bk_jpeg_dec_dma_start8uint32_tPhPh "永久链接至目标")
:   this api start jpeg decode

    参数
    :   **length** – jpeg length


        - input_buf jpeg data src addr

        - output_buf jpeg decode output addr

    返回
    :   0: jpeg decode ok; others: error

bk_err_t bk_jpeg_dec_stop(void)[](#_CPPv416bk_jpeg_dec_stopv "永久链接至目标")
:   stop jpeg decode

    返回
    :   0: jpeg decode stop ok; others: error

bk_err_t bk_jpeg_dec_out_format(pixel_format_t pixel_fmt)[](#_CPPv422bk_jpeg_dec_out_format14pixel_format_t "永久链接至目标")
:   set jpeg decode out format, useful in bk7258

    参数
    :   **pixel_fmt** – select, PIXEL_FMT_YUYV(default), PIXEL_FMT_VUYY, PIXEL_FMT_VYUY (not commonly used),PIXEL_FMT_YYUV(not commonly used)

    返回
    :   BK_OK

void bk_jpeg_dec_line_num_set([line_num_t](#_CPPv410line_num_t "line_num_t") line_num)[](#_CPPv424bk_jpeg_dec_line_num_set10line_num_t "永久链接至目标")
:   when set decode by line, use this api config decode by how many lines

    参数
    :   **select** – according to line_num_t enum,like 8/16/24/32….etc. multiple of 8 line

void bk_jpeg_dec_by_line_start(void)[](#_CPPv425bk_jpeg_dec_by_line_startv "永久链接至目标")
:   start decode in every line decode isr

bk_err_t jpeg_dec_set_dst_addr(unsigned char *output_buf)[](#_CPPv421jpeg_dec_set_dst_addrPh "永久链接至目标")
:   set decode output addr,this api is changed by line decode mode isr

bool bk_jpeg_dec_by_line_is_last_line_complete(void)[](#_CPPv441bk_jpeg_dec_by_line_is_last_line_completev "永久链接至目标")
:   check decode by line is decode last line complete

    返回
    :   return true: last line complete

bk_err_t bk_jpeg_dec_isr_register(jpeg_dec_isr_t jpeg_dec_isr)[](#_CPPv424bk_jpeg_dec_isr_register14jpeg_dec_isr_t "永久链接至目标")
:   This API is direct registerjpeg dec cpu isr.

    参数
    :   **isr** – isr function

    返回
    :   - BK_OK: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [jpeg_dec_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_dec_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_dec_types.h")


### Structures[](#structures "永久链接至标题")

struct jpeg_dec_res_t[](#_CPPv414jpeg_dec_res_t "永久链接至目标")
:   jpeg dec isr return value

    Public Members

    uint8_t ok[](#_CPPv4N14jpeg_dec_res_t2okE "永久链接至目标")
    :   jpeg decoder success

    uint16_t pixel_x[](#_CPPv4N14jpeg_dec_res_t7pixel_xE "永久链接至目标")
    :   jpeg x pixel

    uint16_t pixel_y[](#_CPPv4N14jpeg_dec_res_t7pixel_yE "永久链接至目标")
    :   jpeg y pixel

    uint32_t size[](#_CPPv4N14jpeg_dec_res_t4sizeE "永久链接至目标")
    :   jpeg size

    [jpeg_encode_mode_t](#_CPPv418jpeg_encode_mode_t "jpeg_encode_mode_t") jpeg_enc_mode[](#_CPPv4N14jpeg_dec_res_t13jpeg_enc_modeE "永久链接至目标")
    :   jpeg encode mode


### Macros[](#macros "永久链接至标题")

USE_JPEG_DEC_COMPLETE_CALLBACKS[](#c.USE_JPEG_DEC_COMPLETE_CALLBACKS "永久链接至目标")
:   set 1, register jpeg decode complete callback, set 0, register jpeg dec cpu isr


### Type Definitions[](#type-definitions "永久链接至标题")

typedef enum [_line_num](#_CPPv49_line_num "_line_num") line_num_t[](#_CPPv410line_num_t "永久链接至目标")

typedef void (*jpeg_dec_isr_cb_t)([jpeg_dec_res_t](#_CPPv414jpeg_dec_res_t "jpeg_dec_res_t") *result)[](#_CPPv417jpeg_dec_isr_cb_t "永久链接至目标")
:   refistrer type jpeg decode complete isr function

    param return jpeg x pixel , y pixel , and jpeg size

    Return
    :   - BK_OK: succeed

        - others: other errors. jpegdec int isr register func type


### Enumerations[](#enumerations "永久链接至标题")

enum jpeg_encode_mode_t[](#_CPPv418jpeg_encode_mode_t "永久链接至目标")
:   *Values:*

    enumerator JPEG_ENCODE_UNSTD[](#_CPPv4N18jpeg_encode_mode_t17JPEG_ENCODE_UNSTDE "永久链接至目标")

    enumerator JPEG_ENCODE_YUV420[](#_CPPv4N18jpeg_encode_mode_t18JPEG_ENCODE_YUV420E "永久链接至目标")

    enumerator JPEG_ENCODE_YUV422[](#_CPPv4N18jpeg_encode_mode_t18JPEG_ENCODE_YUV422E "永久链接至目标")

    enumerator JPEG_ENCODE_YUV444[](#_CPPv4N18jpeg_encode_mode_t18JPEG_ENCODE_YUV444E "永久链接至目标")

enum JRESULT[](#_CPPv47JRESULT "永久链接至目标")
:   Error code


    *Values:*

    enumerator JDR_OK[](#_CPPv4N7JRESULT6JDR_OKE "永久链接至目标")
    :   0: Succeeded

    enumerator JDR_INTR[](#_CPPv4N7JRESULT8JDR_INTRE "永久链接至目标")
    :   1: Interrupted by output function

    enumerator JDR_INP[](#_CPPv4N7JRESULT7JDR_INPE "永久链接至目标")
    :   2: Device error or wrong termination of input stream

    enumerator JDR_MEM1[](#_CPPv4N7JRESULT8JDR_MEM1E "永久链接至目标")
    :   3: Insufficient memory pool for the image

    enumerator JDR_MEM2[](#_CPPv4N7JRESULT8JDR_MEM2E "永久链接至目标")
    :   4: Insufficient stream input buffer

    enumerator JDR_PAR[](#_CPPv4N7JRESULT7JDR_PARE "永久链接至目标")
    :   5: Parameter error

    enumerator JDR_FMT1[](#_CPPv4N7JRESULT8JDR_FMT1E "永久链接至目标")
    :   6: Data format error (may be damaged data)

    enumerator JDR_FMT2[](#_CPPv4N7JRESULT8JDR_FMT2E "永久链接至目标")
    :   7: Right format but not supported

    enumerator JDR_FMT3[](#_CPPv4N7JRESULT8JDR_FMT3E "永久链接至目标")
    :   8: Not supported JPEG standard

enum _line_num[](#_CPPv49_line_num "永久链接至目标")
:   *Values:*

    enumerator LINE_8[](#_CPPv4N9_line_num6LINE_8E "永久链接至目标")

    enumerator LINE_16[](#_CPPv4N9_line_num7LINE_16E "永久链接至目标")

    enumerator LINE_24[](#_CPPv4N9_line_num7LINE_24E "永久链接至目标")

    enumerator LINE_32[](#_CPPv4N9_line_num7LINE_32E "永久链接至目标")

    enumerator LINE_40[](#_CPPv4N9_line_num7LINE_40E "永久链接至目标")

    enumerator LINE_48[](#_CPPv4N9_line_num7LINE_48E "永久链接至目标")

enum jpeg_dec_isr_type_t[](#_CPPv419jpeg_dec_isr_type_t "永久链接至目标")
:   *Values:*

    enumerator DEC_END_OF_FRAME[](#_CPPv4N19jpeg_dec_isr_type_t16DEC_END_OF_FRAMEE "永久链接至目标")
    :   select jpeg decode a complete frame enter isr callback

    enumerator DEC_EVERY_LINE_INT[](#_CPPv4N19jpeg_dec_isr_type_t18DEC_EVERY_LINE_INTE "永久链接至目标")
    :   select jpeg decode by line num enter isr callback

    enumerator DEC_ERR[](#_CPPv4N19jpeg_dec_isr_type_t7DEC_ERRE "永久链接至目标")

    enumerator DEC_ISR_MAX[](#_CPPv4N19jpeg_dec_isr_type_t11DEC_ISR_MAXE "永久链接至目标")
