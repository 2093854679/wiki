# 图象算法 APIs[](#apis "永久链接至标题")



## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [image_scale.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/image_scale.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/image_scale.h")


### Functions[](#functions "永久链接至标题")

int image_scale_crop_compress(const uint8_t *src_img, uint8_t *dst_img, unsigned int src_width, unsigned int src_height, unsigned int dst_width, unsigned int dst_height)[](#_CPPv425image_scale_crop_compressPK7uint8_tP7uint8_tjjjj "永久链接至目标")
:   according target image scale crop src image, and compress target image for exampe: src image is 1280*720P and target image is 320*480, you should crop the maximul picture to scale compress target picture. so this algorithns can crop w*h is 480*720 to scale 320*480p.

int image_scale_crop_compress_rotate(const uint8_t *src_img, uint8_t *dst_img, unsigned int src_width, unsigned int src_height, unsigned int dst_width, unsigned int dst_height)[](#_CPPv432image_scale_crop_compress_rotatePK7uint8_tP7uint8_tjjjj "永久链接至目标")
:   according target image scale crop src image, and compress rotate for exampe: src image is 1280*720P and target lcd is 320*480, so rotate is 480*320, so you should crop the maximul picture to scale compress target picture. so this algorithns can crop w*h is 1080*720 to scale 480*320p.

int image_16bit_scaling(const unsigned char *src_img, unsigned char *dst_img, unsigned int src_width, unsigned int src_height, unsigned int dst_width, unsigned int dst_height)[](#_CPPv419image_16bit_scalingPKhPhjjjj "永久链接至目标")
:   according target image scaling src image.

int image_center_crop(const uint8_t *src_img, uint8_t *dst_img, unsigned int src_width, unsigned int src_height, unsigned int dst_width, unsigned int dst_height)[](#_CPPv417image_center_cropPK7uint8_tP7uint8_tjjjj "永久链接至目标")
:   only crop src image to dst image.

int rgb565_rotate_degree90(unsigned char *src, unsigned char *dst, int img_width, int img_height)[](#_CPPv422rgb565_rotate_degree90PhPhii "永久链接至目标")
:   rgb565 clockwise rotate90

int rgb565_rotate_degree270(unsigned char *src, unsigned char *dst, int img_width, int img_height)[](#_CPPv423rgb565_rotate_degree270PhPhii "永久链接至目标")
:   rgb565 anticlockwise rotate270

int argb8888_rotate_degree90(unsigned char *src, unsigned char *dst, int img_width, int img_height)[](#_CPPv424argb8888_rotate_degree90PhPhii "永久链接至目标")
:   argb888 32bit clockwise rotate90

int argb8888_rotate_degree270(unsigned char *src, unsigned char *dst, int img_width, int img_height)[](#_CPPv425argb8888_rotate_degree270PhPhii "永久链接至目标")
:   argb888 32bit rotate270

int yuyv_rotate_degree90_to_yuyv(unsigned char *yuyv, unsigned char *rotatedYuyv, int width, int height)[](#_CPPv428yuyv_rotate_degree90_to_yuyvPhPhii "永久链接至目标")
:   yuyv data clockwise rotate90, and output yuyv

int yuyv_rotate_degree270_to_yuyv(unsigned char *yuyv, unsigned char *rotatedYuyv, int width, int height)[](#_CPPv429yuyv_rotate_degree270_to_yuyvPhPhii "永久链接至目标")
:   yuyv rotete 270 degree and output data format yuyv

    参数
    :   **1** – src yuyv data 2 rotate src yuyv 270 degrees to yuyv,the dst yuyyv 3 src width 4 src height

    返回
    :   - BK_OK: succeed

        - others: other errors.

int yuyv_rotate_degree180_to_yuyv(unsigned char *yuyv, unsigned char *rotatedyuyv, int width, int height)[](#_CPPv429yuyv_rotate_degree180_to_yuyvPhPhii "永久链接至目标")
:   yuyv rotete 180 degree and output data format yuyv

    参数
    :   **1** – src yuyv data 2 rotate src yuyv 180 degrees to yuyv,the dst yuyyv 3 src width 4 src height

    返回
    :   - BK_OK: succeed

        - others: other errors.

int yuyv_rotate_degree270_to_vuyy(unsigned char *src_yuyv, unsigned char *rotated_to_vuyy, int width, int height)[](#_CPPv429yuyv_rotate_degree270_to_vuyyPhPhii "永久链接至目标")
:   yuyv data rotate270, and output vuyy

int vuyy_rotate_degree90_to_yuyv(unsigned char *vuyy, unsigned char *rotatedVuyy, int width, int height)[](#_CPPv428vuyy_rotate_degree90_to_yuyvPhPhii "永久链接至目标")
:   vuyy clockwise rotate90, and output yuyv

int vuyy_rotate_degree270_to_yuyv(unsigned char *vuyy, unsigned char *rotatedVuyy, int width, int height)[](#_CPPv429vuyy_rotate_degree270_to_yuyvPhPhii "永久链接至目标")
:   vuyy clockwise rotate270, and output yuyv

int yuyv2rgb_rotate_degree90(unsigned char *yuyv, unsigned char *rotatedYuyv, int width, int height)[](#_CPPv424yuyv2rgb_rotate_degree90PhPhii "永久链接至目标")
:   yuyv to rgb data clockwise rotate90

int vuyy2rgb_rotate_degree90(unsigned char *vuyy, unsigned char *rotatedVuyy, int width, int height)[](#_CPPv424vuyy2rgb_rotate_degree90PhPhii "永久链接至目标")
:   vuyy to rgb data clockwise rotate90

void image_scale_init(void)[](#_CPPv416image_scale_initv "永久链接至目标")
:   image scale init

int vuyy_to_rgb565_convert(unsigned char *src_buf, unsigned char *out_buf, int img_width, int img_height)[](#_CPPv422vuyy_to_rgb565_convertPhPhii "永久链接至目标")
:   uyvy422 data convert to RGB565 data

int uyvy_to_rgb565_convert(unsigned char *src_buf, unsigned char *out_buf, int img_width, int img_height)[](#_CPPv422uyvy_to_rgb565_convertPhPhii "永久链接至目标")
:   uyvy422 data convert to RGB565 data

int yuyv_to_rgb565_convert(unsigned char *src_buf, unsigned char *out_buf, int img_width, int img_height)[](#_CPPv422yuyv_to_rgb565_convertPhPhii "永久链接至目标")
:   yuyv422 data convert to RGB565 data

int rgb565_to_uyvy_convert(uint16_t *sourceLcdBuffer, uint16_t *destLcdBuffer, int img_width, int img_height)[](#_CPPv422rgb565_to_uyvy_convertP8uint16_tP8uint16_tii "永久链接至目标")
:   RGB565 data convert to uyvy422 data.

int rgb565_to_yuyv_convert(uint16_t *sourceLcdBuffer, uint16_t *destLcdBuffer, int img_width, int img_height)[](#_CPPv422rgb565_to_yuyv_convertP8uint16_tP8uint16_tii "永久链接至目标")
:   RGB565 data convert to yuyv422 data.

int rgb565_to_rgb565le_convert(void *rgb565_buffer, int img_width, int img_height)[](#_CPPv426rgb565_to_rgb565le_convertPvii "永久链接至目标")

int rgb888_to_rgb565_convert(uint8_t *src_buffer, uint16_t *dst_buffer, int img_width, int img_height)[](#_CPPv424rgb888_to_rgb565_convertP7uint8_tP8uint16_tii "永久链接至目标")

int rgb565_to_rgb888_convert(uint16_t *src_buffer, uint8_t *dst_buffer, int img_width, int img_height)[](#_CPPv424rgb565_to_rgb888_convertP8uint16_tP7uint8_tii "永久链接至目标")

void yyuv_to_rgb888(uint8_t *input_ptr, uint8_t *output_ptr, uint32_t width, uint32_t height)[](#_CPPv414yyuv_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

void yuyv_to_rgb888_convert(uint8_t *input_ptr, uint8_t *output_ptr, uint32_t width, uint32_t height)[](#_CPPv422yuyv_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   yuyv (H->L : YUYV) convert to rgb888

void vuyy_to_rgb888(uint8_t *input_ptr, uint8_t *output_ptr, uint32_t width, uint32_t height)[](#_CPPv414vuyy_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

void vyuy_to_rgb888_convert(uint8_t *input_ptr, uint8_t *output_ptr, uint32_t width, uint32_t height)[](#_CPPv422vyuy_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

int rgb565_to_vuyy_convert(uint16_t *sourceLcdBuffer, uint16_t *destLcdBuffer, int img_width, int img_height)[](#_CPPv422rgb565_to_vuyy_convertP8uint16_tP8uint16_tii "永久链接至目标")

int yuyv_to_rgb565(uint8_t *src_buff, uint8_t *dst_buff, int width, int height)[](#_CPPv414yuyv_to_rgb565P7uint8_tP7uint8_tii "永久链接至目标")

int vuyy_to_rgb565(uint8_t *src_buff, uint8_t *dst_buff, int width, int height)[](#_CPPv414vuyy_to_rgb565P7uint8_tP7uint8_tii "永久链接至目标")

void argb8888_to_vuyy_blend(uint8_t *src, uint8_t *dst, uint32_t width, uint32_t height)[](#_CPPv422argb8888_to_vuyy_blendP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

void argb8888_to_yuyv_blend(uint8_t *src, uint8_t *dst, uint32_t width, uint32_t height)[](#_CPPv422argb8888_to_yuyv_blendP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

void argb8888_to_rgb565_blend(uint8_t *src, uint8_t *dst, uint32_t width, uint32_t height)[](#_CPPv424argb8888_to_rgb565_blendP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

void argb8888_to_rgb888_blend(uint8_t *src, uint8_t *dst, uint32_t width, uint32_t height)[](#_CPPv424argb8888_to_rgb888_blendP7uint8_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

int vuyy_image_resize(uint8_t *src_img, uint8_t *dst_img, uint32_t src_width, uint32_t src_height, uint32_t dst_width, uint32_t dst_height)[](#_CPPv417vuyy_image_resizeP7uint8_tP7uint8_t8uint32_t8uint32_t8uint32_t8uint32_t "永久链接至目标")

int vuyy_image_vga_to_lvga(uint8_t *src_buf, uint8_t *dst_buf, uint8_t row_count)[](#_CPPv422vuyy_image_vga_to_lvgaP7uint8_tP7uint8_t7uint8_t "永久链接至目标")

int vuyy_image_vga_to_rsvga(uint8_t *src_buf, uint8_t *dst_buf, uint8_t row_count)[](#_CPPv423vuyy_image_vga_to_rsvgaP7uint8_tP7uint8_t7uint8_t "永久链接至目标")

int vuyy_image_vga_to_qvga(uint8_t *src_buf, uint8_t *dst_buf, uint8_t row_count)[](#_CPPv422vuyy_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t "永久链接至目标")

int yuyv_image_vga_to_qvga(uint8_t *src_buf, uint8_t *dst_buf, uint8_t row_count)[](#_CPPv422yuyv_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t "永久链接至目标")

yuv_enc_fmt_t bk_get_original_jpeg_encode_data_format(uint8_t *src_buf, uint32_t length)[](#_CPPv439bk_get_original_jpeg_encode_data_formatP7uint8_t8uint32_t "永久链接至目标")
