---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_jpegenc_sw.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="jpegenc-apis"></a>

# JPEGENC APIs

重要

This component is for software encode not hardware encode

<a id="jpegenc-api-categories"></a>

## JPEGENC API Categories

Most of JPEGENC APIs can be categoried as:

> - JPEGENC APIs

JPEGENC APIs:
:   - [`jpeg_sw_encoder_init()`](#_CPPv420jpeg_sw_encoder_initv "jpeg_sw_encoder_init") \- init jpeg encode software module

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [jpeg\_enc\_sw.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/modules/jpeg_enc_sw.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420jpeg_sw_encoder_initv"></a>

<a id="_CPPv320jpeg_sw_encoder_initv"></a> <a id="_CPPv220jpeg_sw_encoder_initv"></a> <a id="jpeg_sw_encoder_init__void"></a> <a id="jpeg__enc__sw_8h_1a218fe71a26855b5e2cfbb0be03d6b3a9"></a> void jpeg\_sw\_encoder\_init(void)
:   Initialize the JPEG softeware encoder.

    **Attention**
    :   1\. only for software jpeg encode

    返回

<a id="structures"></a>

### Structures

<a id="_CPPv416_jpeg_sw_encoder"></a>

<a id="_CPPv316_jpeg_sw_encoder"></a> <a id="_CPPv216_jpeg_sw_encoder"></a> <a id="_jpeg_sw_encoder"></a> <a id="struct__jpeg__sw__encoder"></a> struct \_jpeg\_sw\_encoder
:   JPEG\_SW\_ENC APIs Version 1.0.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417jpeg_sw_encoder_t"></a>

<a id="_CPPv317jpeg_sw_encoder_t"></a> <a id="_CPPv217jpeg_sw_encoder_t"></a> <a id="jpeg_sw_encoder_t"></a> <a id="jpeg__enc__sw_8h_1a725185a98d806720817f5ddff2b0a386"></a> typedef struct [\_jpeg\_sw\_encoder](#_CPPv416_jpeg_sw_encoder "_jpeg_sw_encoder") jpeg\_sw\_encoder\_t
:   JPEG\_SW\_ENC APIs Version 1.0.

<a id="api-typedefs"></a>

## API Typedefs
