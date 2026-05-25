# JPEGENC APIs[](#jpegenc-apis "永久链接至标题")


重要

This component is for software encode not hardware encode


## JPEGENC API Categories[](#jpegenc-api-categories "永久链接至标题")

Most of JPEGENC APIs can be categoried as:

> - JPEGENC APIs

JPEGENC APIs:
:   - [`jpeg_sw_encoder_init()`](#_CPPv420jpeg_sw_encoder_initv "jpeg_sw_encoder_init") - init jpeg encode software module


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [jpeg_enc_sw.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc_sw.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc_sw.h")


### Functions[](#functions "永久链接至标题")

void jpeg_sw_encoder_init(void)[](#_CPPv420jpeg_sw_encoder_initv "永久链接至目标")
:   Initialize the JPEG softeware encoder.


    **Attention**
    :   1. only for software jpeg encode

    返回


### Structures[](#structures "永久链接至标题")

struct _jpeg_sw_encoder[](#_CPPv416_jpeg_sw_encoder "永久链接至目标")
:   JPEG_SW_ENC APIs Version 1.0.


### Type Definitions[](#type-definitions "永久链接至标题")

typedef struct [_jpeg_sw_encoder](#_CPPv416_jpeg_sw_encoder "_jpeg_sw_encoder") jpeg_sw_encoder_t[](#_CPPv417jpeg_sw_encoder_t "永久链接至目标")
:   JPEG_SW_ENC APIs Version 1.0.


## API Typedefs[](#api-typedefs "永久链接至标题")
