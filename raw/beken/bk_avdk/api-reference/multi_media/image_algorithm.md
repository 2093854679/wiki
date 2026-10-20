---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/image_algorithm.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="apis"></a>

# 图象算法 APIs

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [image\_scale.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/modules/image_scale.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425image_scale_crop_compressPK7uint8_tP7uint8_tjjjj"></a>

<a id="_CPPv325image_scale_crop_compressPK7uint8_tP7uint8_tjjjj"></a> <a id="_CPPv225image_scale_crop_compressPK7uint8_tP7uint8_tjjjj"></a> <a id="image_scale_crop_compress__uint8_tCP.uint8_tP.unsigned-i.unsigned-i.unsigned-i.unsigned-i"></a> <a id="image__scale_8h_1a8a87faaf54994b857ea67f891b0e2986"></a> int image\_scale\_crop\_compress(const uint8\_t \*src\_img, uint8\_t \*dst\_img, unsigned int src\_width, unsigned int src\_height, unsigned int dst\_width, unsigned int dst\_height)
:   according target image scale crop src image, and compress target image for exampe: src image is 1280\*720P and target image is 320\*480, you should crop the maximul picture to scale compress target picture. so this algorithns can crop w\*h is 480\*720 to scale 320\*480p.

<a id="_CPPv432image_scale_crop_compress_rotatePK7uint8_tP7uint8_tjjjj"></a>

<a id="_CPPv332image_scale_crop_compress_rotatePK7uint8_tP7uint8_tjjjj"></a> <a id="_CPPv232image_scale_crop_compress_rotatePK7uint8_tP7uint8_tjjjj"></a> <a id="image_scale_crop_compress_rotate__uint8_tCP.uint8_tP.unsigned-i.unsigned-i.unsigned-i.unsigned-i"></a> <a id="image__scale_8h_1a07c150bc6ae5791b244ab914629518fa"></a> int image\_scale\_crop\_compress\_rotate(const uint8\_t \*src\_img, uint8\_t \*dst\_img, unsigned int src\_width, unsigned int src\_height, unsigned int dst\_width, unsigned int dst\_height)
:   according target image scale crop src image, and compress rotate for exampe: src image is 1280\*720P and target lcd is 320\*480, so rotate is 480\*320, so you should crop the maximul picture to scale compress target picture. so this algorithns can crop w\*h is 1080\*720 to scale 480\*320p.

<a id="_CPPv419image_16bit_scalingPKhPhjjjj"></a>

<a id="_CPPv319image_16bit_scalingPKhPhjjjj"></a> <a id="_CPPv219image_16bit_scalingPKhPhjjjj"></a> <a id="image_16bit_scaling__unsigned-cCP.unsigned-cP.unsigned-i.unsigned-i.unsigned-i.unsigned-i"></a> <a id="image__scale_8h_1a43d1d4c1ae3a316713bb154bdc14117b"></a> int image\_16bit\_scaling(const unsigned char \*src\_img, unsigned char \*dst\_img, unsigned int src\_width, unsigned int src\_height, unsigned int dst\_width, unsigned int dst\_height)
:   according target image scaling src image.

<a id="_CPPv417image_center_cropPK7uint8_tP7uint8_tjjjj"></a>

<a id="_CPPv317image_center_cropPK7uint8_tP7uint8_tjjjj"></a> <a id="_CPPv217image_center_cropPK7uint8_tP7uint8_tjjjj"></a> <a id="image_center_crop__uint8_tCP.uint8_tP.unsigned-i.unsigned-i.unsigned-i.unsigned-i"></a> <a id="image__scale_8h_1ad262289af109b16c5d9b8f52930dc54d"></a> int image\_center\_crop(const uint8\_t \*src\_img, uint8\_t \*dst\_img, unsigned int src\_width, unsigned int src\_height, unsigned int dst\_width, unsigned int dst\_height)
:   only crop src image to dst image.

<a id="_CPPv422rgb565_rotate_degree90PhPhii"></a>

<a id="_CPPv322rgb565_rotate_degree90PhPhii"></a> <a id="_CPPv222rgb565_rotate_degree90PhPhii"></a> <a id="rgb565_rotate_degree90__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a61bed0510c21810cfed0db9770ac1d7d"></a> int rgb565\_rotate\_degree90(unsigned char \*src, unsigned char \*dst, int img\_width, int img\_height)
:   rgb565 clockwise rotate90

<a id="_CPPv423rgb565_rotate_degree270PhPhii"></a>

<a id="_CPPv323rgb565_rotate_degree270PhPhii"></a> <a id="_CPPv223rgb565_rotate_degree270PhPhii"></a> <a id="rgb565_rotate_degree270__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1ae82de2728d9a219d48c6e807b54261f6"></a> int rgb565\_rotate\_degree270(unsigned char \*src, unsigned char \*dst, int img\_width, int img\_height)
:   rgb565 anticlockwise rotate270

<a id="_CPPv424argb8888_rotate_degree90PhPhii"></a>

<a id="_CPPv324argb8888_rotate_degree90PhPhii"></a> <a id="_CPPv224argb8888_rotate_degree90PhPhii"></a> <a id="argb8888_rotate_degree90__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1ad289133e87d464b56545a61a41973f75"></a> int argb8888\_rotate\_degree90(unsigned char \*src, unsigned char \*dst, int img\_width, int img\_height)
:   argb888 32bit clockwise rotate90

<a id="_CPPv425argb8888_rotate_degree270PhPhii"></a>

<a id="_CPPv325argb8888_rotate_degree270PhPhii"></a> <a id="_CPPv225argb8888_rotate_degree270PhPhii"></a> <a id="argb8888_rotate_degree270__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1ab8b386555d51b4322e25567c332428f1"></a> int argb8888\_rotate\_degree270(unsigned char \*src, unsigned char \*dst, int img\_width, int img\_height)
:   argb888 32bit rotate270

<a id="_CPPv428yuyv_rotate_degree90_to_yuyvPhPhii"></a>

<a id="_CPPv328yuyv_rotate_degree90_to_yuyvPhPhii"></a> <a id="_CPPv228yuyv_rotate_degree90_to_yuyvPhPhii"></a> <a id="yuyv_rotate_degree90_to_yuyv__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a788ad162cdc42a7720ee87b7eef4034d"></a> int yuyv\_rotate\_degree90\_to\_yuyv(unsigned char \*yuyv, unsigned char \*rotatedYuyv, int width, int height)
:   yuyv data clockwise rotate90, and output yuyv

<a id="_CPPv429yuyv_rotate_degree270_to_yuyvPhPhii"></a>

<a id="_CPPv329yuyv_rotate_degree270_to_yuyvPhPhii"></a> <a id="_CPPv229yuyv_rotate_degree270_to_yuyvPhPhii"></a> <a id="yuyv_rotate_degree270_to_yuyv__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a235a7635d5acbad0e37de51f5d491418"></a> int yuyv\_rotate\_degree270\_to\_yuyv(unsigned char \*yuyv, unsigned char \*rotatedYuyv, int width, int height)
:   yuyv rotete 270 degree and output data format yuyv

    参数
    :   **1** – src yuyv data 2 rotate src yuyv 270 degrees to yuyv,the dst yuyyv 3 src width 4 src height

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429yuyv_rotate_degree180_to_yuyvPhPhii"></a>

<a id="_CPPv329yuyv_rotate_degree180_to_yuyvPhPhii"></a> <a id="_CPPv229yuyv_rotate_degree180_to_yuyvPhPhii"></a> <a id="yuyv_rotate_degree180_to_yuyv__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1aaf8f6958c749139d232cd317336fe068"></a> int yuyv\_rotate\_degree180\_to\_yuyv(unsigned char \*yuyv, unsigned char \*rotatedyuyv, int width, int height)
:   yuyv rotete 180 degree and output data format yuyv

    参数
    :   **1** – src yuyv data 2 rotate src yuyv 180 degrees to yuyv,the dst yuyyv 3 src width 4 src height

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429yuyv_rotate_degree270_to_vuyyPhPhii"></a>

<a id="_CPPv329yuyv_rotate_degree270_to_vuyyPhPhii"></a> <a id="_CPPv229yuyv_rotate_degree270_to_vuyyPhPhii"></a> <a id="yuyv_rotate_degree270_to_vuyy__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1afd4271fdf287bb702439cf64b40049c7"></a> int yuyv\_rotate\_degree270\_to\_vuyy(unsigned char \*src\_yuyv, unsigned char \*rotated\_to\_vuyy, int width, int height)
:   yuyv data rotate270, and output vuyy

<a id="_CPPv428vuyy_rotate_degree90_to_yuyvPhPhii"></a>

<a id="_CPPv328vuyy_rotate_degree90_to_yuyvPhPhii"></a> <a id="_CPPv228vuyy_rotate_degree90_to_yuyvPhPhii"></a> <a id="vuyy_rotate_degree90_to_yuyv__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a051b22647586581b03828b95b38b0f76"></a> int vuyy\_rotate\_degree90\_to\_yuyv(unsigned char \*vuyy, unsigned char \*rotatedVuyy, int width, int height)
:   vuyy clockwise rotate90, and output yuyv

<a id="_CPPv429vuyy_rotate_degree270_to_yuyvPhPhii"></a>

<a id="_CPPv329vuyy_rotate_degree270_to_yuyvPhPhii"></a> <a id="_CPPv229vuyy_rotate_degree270_to_yuyvPhPhii"></a> <a id="vuyy_rotate_degree270_to_yuyv__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a68a8f17ecf9172431cb0732a71480387"></a> int vuyy\_rotate\_degree270\_to\_yuyv(unsigned char \*vuyy, unsigned char \*rotatedVuyy, int width, int height)
:   vuyy clockwise rotate270, and output yuyv

<a id="_CPPv424yuyv2rgb_rotate_degree90PhPhii"></a>

<a id="_CPPv324yuyv2rgb_rotate_degree90PhPhii"></a> <a id="_CPPv224yuyv2rgb_rotate_degree90PhPhii"></a> <a id="yuyv2rgb_rotate_degree90__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a932c42bb422951e464e39a578041b675"></a> int yuyv2rgb\_rotate\_degree90(unsigned char \*yuyv, unsigned char \*rotatedYuyv, int width, int height)
:   yuyv to rgb data clockwise rotate90

<a id="_CPPv424vuyy2rgb_rotate_degree90PhPhii"></a>

<a id="_CPPv324vuyy2rgb_rotate_degree90PhPhii"></a> <a id="_CPPv224vuyy2rgb_rotate_degree90PhPhii"></a> <a id="vuyy2rgb_rotate_degree90__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1abcb10a585d25f9e356b2a4855dc7c75b"></a> int vuyy2rgb\_rotate\_degree90(unsigned char \*vuyy, unsigned char \*rotatedVuyy, int width, int height)
:   vuyy to rgb data clockwise rotate90

<a id="_CPPv416image_scale_initv"></a>

<a id="_CPPv316image_scale_initv"></a> <a id="_CPPv216image_scale_initv"></a> <a id="image_scale_init__void"></a> <a id="image__scale_8h_1a20a0f2f834fb6e9e6d5ba91242268961"></a> void image\_scale\_init(void)
:   image scale init

<a id="_CPPv422vuyy_to_rgb565_convertPhPhii"></a>

<a id="_CPPv322vuyy_to_rgb565_convertPhPhii"></a> <a id="_CPPv222vuyy_to_rgb565_convertPhPhii"></a> <a id="vuyy_to_rgb565_convert__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1aced12dd3e5ef68f38dbe8ec8e5a006e9"></a> int vuyy\_to\_rgb565\_convert(unsigned char \*src\_buf, unsigned char \*out\_buf, int img\_width, int img\_height)
:   uyvy422 data convert to RGB565 data

<a id="_CPPv422uyvy_to_rgb565_convertPhPhii"></a>

<a id="_CPPv322uyvy_to_rgb565_convertPhPhii"></a> <a id="_CPPv222uyvy_to_rgb565_convertPhPhii"></a> <a id="uyvy_to_rgb565_convert__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1aa863f4c9281cab8863f8fe56b01fce12"></a> int uyvy\_to\_rgb565\_convert(unsigned char \*src\_buf, unsigned char \*out\_buf, int img\_width, int img\_height)
:   uyvy422 data convert to RGB565 data

<a id="_CPPv422yuyv_to_rgb565_convertPhPhii"></a>

<a id="_CPPv322yuyv_to_rgb565_convertPhPhii"></a> <a id="_CPPv222yuyv_to_rgb565_convertPhPhii"></a> <a id="yuyv_to_rgb565_convert__unsigned-cP.unsigned-cP.i.i"></a> <a id="image__scale_8h_1a2ce0360373955a560f3f207eacfe1e6a"></a> int yuyv\_to\_rgb565\_convert(unsigned char \*src\_buf, unsigned char \*out\_buf, int img\_width, int img\_height)
:   yuyv422 data convert to RGB565 data

<a id="_CPPv422rgb565_to_uyvy_convertP8uint16_tP8uint16_tii"></a>

<a id="_CPPv322rgb565_to_uyvy_convertP8uint16_tP8uint16_tii"></a> <a id="_CPPv222rgb565_to_uyvy_convertP8uint16_tP8uint16_tii"></a> <a id="rgb565_to_uyvy_convert__uint16_tP.uint16_tP.i.i"></a> <a id="image__scale_8h_1af829e6fc864718aa62fa20a33e4d20d7"></a> int rgb565\_to\_uyvy\_convert(uint16\_t \*sourceLcdBuffer, uint16\_t \*destLcdBuffer, int img\_width, int img\_height)
:   RGB565 data convert to uyvy422 data.

<a id="_CPPv422rgb565_to_yuyv_convertP8uint16_tP8uint16_tii"></a>

<a id="_CPPv322rgb565_to_yuyv_convertP8uint16_tP8uint16_tii"></a> <a id="_CPPv222rgb565_to_yuyv_convertP8uint16_tP8uint16_tii"></a> <a id="rgb565_to_yuyv_convert__uint16_tP.uint16_tP.i.i"></a> <a id="image__scale_8h_1aabb84f0ed3658116ed861ce106b911ba"></a> int rgb565\_to\_yuyv\_convert(uint16\_t \*sourceLcdBuffer, uint16\_t \*destLcdBuffer, int img\_width, int img\_height)
:   RGB565 data convert to yuyv422 data.

<a id="_CPPv426rgb565_to_rgb565le_convertPvii"></a>

<a id="_CPPv326rgb565_to_rgb565le_convertPvii"></a> <a id="_CPPv226rgb565_to_rgb565le_convertPvii"></a> <a id="rgb565_to_rgb565le_convert__voidP.i.i"></a> <a id="image__scale_8h_1af5bd53e922a24e9cbe491054015ebbb8"></a> int rgb565\_to\_rgb565le\_convert(void \*rgb565\_buffer, int img\_width, int img\_height)

<a id="_CPPv424rgb888_to_rgb565_convertP7uint8_tP8uint16_tii"></a>

<a id="_CPPv324rgb888_to_rgb565_convertP7uint8_tP8uint16_tii"></a> <a id="_CPPv224rgb888_to_rgb565_convertP7uint8_tP8uint16_tii"></a> <a id="rgb888_to_rgb565_convert__uint8_tP.uint16_tP.i.i"></a> <a id="image__scale_8h_1a8cbc27cf8db26046386a754d2e3755bb"></a> int rgb888\_to\_rgb565\_convert(uint8\_t \*src\_buffer, uint16\_t \*dst\_buffer, int img\_width, int img\_height)

<a id="_CPPv424rgb565_to_rgb888_convertP8uint16_tP7uint8_tii"></a>

<a id="_CPPv324rgb565_to_rgb888_convertP8uint16_tP7uint8_tii"></a> <a id="_CPPv224rgb565_to_rgb888_convertP8uint16_tP7uint8_tii"></a> <a id="rgb565_to_rgb888_convert__uint16_tP.uint8_tP.i.i"></a> <a id="image__scale_8h_1a3da5efa3539343c238c903dc8fed37fa"></a> int rgb565\_to\_rgb888\_convert(uint16\_t \*src\_buffer, uint8\_t \*dst\_buffer, int img\_width, int img\_height)

<a id="_CPPv414yyuv_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv314yyuv_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv214yyuv_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="yyuv_to_rgb888__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1ad92e3619f2c89b8a38ae7163df41e79e"></a> void yyuv\_to\_rgb888(uint8\_t \*input\_ptr, uint8\_t \*output\_ptr, uint32\_t width, uint32\_t height)

<a id="_CPPv422yuyv_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv322yuyv_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv222yuyv_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="yuyv_to_rgb888_convert__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1a1aa9ee54b0a514e1f2cd9e871d56a4c7"></a> void yuyv\_to\_rgb888\_convert(uint8\_t \*input\_ptr, uint8\_t \*output\_ptr, uint32\_t width, uint32\_t height)
:   yuyv (H-\>L : YUYV) convert to rgb888

<a id="_CPPv414vuyy_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv314vuyy_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv214vuyy_to_rgb888P7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="vuyy_to_rgb888__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1af70a7dbaf015986f056956810707cb1f"></a> void vuyy\_to\_rgb888(uint8\_t \*input\_ptr, uint8\_t \*output\_ptr, uint32\_t width, uint32\_t height)

<a id="_CPPv422vyuy_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv322vyuy_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv222vyuy_to_rgb888_convertP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="vyuy_to_rgb888_convert__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1aa6b2e50cc75ba4d1b12ad815d2d73c1c"></a> void vyuy\_to\_rgb888\_convert(uint8\_t \*input\_ptr, uint8\_t \*output\_ptr, uint32\_t width, uint32\_t height)

<a id="_CPPv422rgb565_to_vuyy_convertP8uint16_tP8uint16_tii"></a>

<a id="_CPPv322rgb565_to_vuyy_convertP8uint16_tP8uint16_tii"></a> <a id="_CPPv222rgb565_to_vuyy_convertP8uint16_tP8uint16_tii"></a> <a id="rgb565_to_vuyy_convert__uint16_tP.uint16_tP.i.i"></a> <a id="image__scale_8h_1aa831926e1ca4ebd720e5c3cee82da764"></a> int rgb565\_to\_vuyy\_convert(uint16\_t \*sourceLcdBuffer, uint16\_t \*destLcdBuffer, int img\_width, int img\_height)

<a id="_CPPv414yuyv_to_rgb565P7uint8_tP7uint8_tii"></a>

<a id="_CPPv314yuyv_to_rgb565P7uint8_tP7uint8_tii"></a> <a id="_CPPv214yuyv_to_rgb565P7uint8_tP7uint8_tii"></a> <a id="yuyv_to_rgb565__uint8_tP.uint8_tP.i.i"></a> <a id="image__scale_8h_1a65c76a2141fc42884df74691484c3690"></a> int yuyv\_to\_rgb565(uint8\_t \*src\_buff, uint8\_t \*dst\_buff, int width, int height)

<a id="_CPPv414vuyy_to_rgb565P7uint8_tP7uint8_tii"></a>

<a id="_CPPv314vuyy_to_rgb565P7uint8_tP7uint8_tii"></a> <a id="_CPPv214vuyy_to_rgb565P7uint8_tP7uint8_tii"></a> <a id="vuyy_to_rgb565__uint8_tP.uint8_tP.i.i"></a> <a id="image__scale_8h_1a84fb9e1bb7c2788542ad3f90be8f69d0"></a> int vuyy\_to\_rgb565(uint8\_t \*src\_buff, uint8\_t \*dst\_buff, int width, int height)

<a id="_CPPv422argb8888_to_vuyy_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv322argb8888_to_vuyy_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv222argb8888_to_vuyy_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="argb8888_to_vuyy_blend__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1a05b50a9684b2c295af3d11399560708d"></a> void argb8888\_to\_vuyy\_blend(uint8\_t \*src, uint8\_t \*dst, uint32\_t width, uint32\_t height)

<a id="_CPPv422argb8888_to_yuyv_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv322argb8888_to_yuyv_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv222argb8888_to_yuyv_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="argb8888_to_yuyv_blend__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1a531e54ecf1959cd103251c7a3ce0451b"></a> void argb8888\_to\_yuyv\_blend(uint8\_t \*src, uint8\_t \*dst, uint32\_t width, uint32\_t height)

<a id="_CPPv424argb8888_to_rgb565_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv324argb8888_to_rgb565_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv224argb8888_to_rgb565_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="argb8888_to_rgb565_blend__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1ac3ca89de397882d3b8b8dcde0619f4bf"></a> void argb8888\_to\_rgb565\_blend(uint8\_t \*src, uint8\_t \*dst, uint32\_t width, uint32\_t height)

<a id="_CPPv424argb8888_to_rgb888_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv324argb8888_to_rgb888_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv224argb8888_to_rgb888_blendP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="argb8888_to_rgb888_blend__uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="image__scale_8h_1a1324604ef856615a60843d00ff196d00"></a> void argb8888\_to\_rgb888\_blend(uint8\_t \*src, uint8\_t \*dst, uint32\_t width, uint32\_t height)

<a id="_CPPv417vuyy_image_resizeP7uint8_tP7uint8_t8uint32_t8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv317vuyy_image_resizeP7uint8_tP7uint8_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv217vuyy_image_resizeP7uint8_tP7uint8_t8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="vuyy_image_resize__uint8_tP.uint8_tP.uint32_t.uint32_t.uint32_t.uint32_t"></a> <a id="image__scale_8h_1a754ff0b1b1f036d2b57578cad20cca3b"></a> int vuyy\_image\_resize(uint8\_t \*src\_img, uint8\_t \*dst\_img, uint32\_t src\_width, uint32\_t src\_height, uint32\_t dst\_width, uint32\_t dst\_height)

<a id="_CPPv422vuyy_image_vga_to_lvgaP7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv322vuyy_image_vga_to_lvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv222vuyy_image_vga_to_lvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="vuyy_image_vga_to_lvga__uint8_tP.uint8_tP.uint8_t"></a> <a id="image__scale_8h_1a98acc3589e59be22d3a481aba47d1cb2"></a> int vuyy\_image\_vga\_to\_lvga(uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint8\_t row\_count)

<a id="_CPPv423vuyy_image_vga_to_rsvgaP7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv323vuyy_image_vga_to_rsvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv223vuyy_image_vga_to_rsvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="vuyy_image_vga_to_rsvga__uint8_tP.uint8_tP.uint8_t"></a> <a id="image__scale_8h_1a4224a29b13df05f8c6b8b36b31cabcd0"></a> int vuyy\_image\_vga\_to\_rsvga(uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint8\_t row\_count)

<a id="_CPPv422vuyy_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv322vuyy_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv222vuyy_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="vuyy_image_vga_to_qvga__uint8_tP.uint8_tP.uint8_t"></a> <a id="image__scale_8h_1a62df0e8b88a5e5617ae2782d0829bfd9"></a> int vuyy\_image\_vga\_to\_qvga(uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint8\_t row\_count)

<a id="_CPPv422yuyv_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv322yuyv_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv222yuyv_image_vga_to_qvgaP7uint8_tP7uint8_t7uint8_t"></a> <a id="yuyv_image_vga_to_qvga__uint8_tP.uint8_tP.uint8_t"></a> <a id="image__scale_8h_1a54de512bdb439afb1d74a946093167ed"></a> int yuyv\_image\_vga\_to\_qvga(uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint8\_t row\_count)

<a id="_CPPv439bk_get_original_jpeg_encode_data_formatP7uint8_t8uint32_t"></a>

<a id="_CPPv339bk_get_original_jpeg_encode_data_formatP7uint8_t8uint32_t"></a> <a id="_CPPv239bk_get_original_jpeg_encode_data_formatP7uint8_t8uint32_t"></a> <a id="bk_get_original_jpeg_encode_data_format__uint8_tP.uint32_t"></a> <a id="image__scale_8h_1abe0b7514997c9dd4043ab6c9cb24953a"></a> yuv\_enc\_fmt\_t bk\_get\_original\_jpeg\_encode\_data\_format(uint8\_t \*src\_buf, uint32\_t length)
