---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_mp3.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="mp3-apis"></a>

# MP3 APIs

重要

The MP3 API v1.0 is the lastest stable MP3 APIs. It supports MPEG-1, MPEG-2 and MPEG-2.5 standard Layer3 decoding. All new applications should use MP3 API v1.0.

<a id="mp3-api-categories"></a>

## MP3 API Categories

MP3 APIs:
:   - [`MP3InitDecoder()`](#_CPPv414MP3InitDecoderv "MP3InitDecoder") \- allocate memory for platform-specific data and clear all the user-accessible fields
    - [`MP3FreeDecoder()`](#_CPPv414MP3FreeDecoder11HMP3Decoder "MP3FreeDecoder") \- free platform-specific data allocated by InitMP3Decoder and zero out the contents of MP3DecInfo struct
    - [`MP3FindSyncWord()`](#_CPPv415MP3FindSyncWordPhi "MP3FindSyncWord") \- locate the next byte-alinged sync word in the raw mp3 stream
    - [`MP3Decode()`](#_CPPv49MP3Decode11HMP3DecoderPPhPiPsi "MP3Decode") \- decode one frame of MP3 data
    - [`MP3GetLastFrameInfo()`](#_CPPv419MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo "MP3GetLastFrameInfo") \- get info about last MP3 frame decoded (number of sampled decoded, sample rate, bitrate, etc.)
    - [`MP3GetNextFrameInfo()`](#_CPPv419MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh "MP3GetNextFrameInfo") \- parse MP3 frame header

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [mp3dec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/mp3dec.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414MP3InitDecoderv"></a>

<a id="_CPPv314MP3InitDecoderv"></a> <a id="_CPPv214MP3InitDecoderv"></a> <a id="MP3InitDecoder__void"></a> <a id="mp3dec_8h_1ad815dab14b2935369c15eb2491bdae37"></a> [HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") MP3InitDecoder(void)
:   Init the decoder of MP3.

    This API init the mp3 decoder module:

    - allocate memory for platform-specific data
    - clear all the user-accessible fields

    参数
    :   **None** –

    返回
    :   None

<a id="_CPPv414MP3FreeDecoder11HMP3Decoder"></a>

<a id="_CPPv314MP3FreeDecoder11HMP3Decoder"></a> <a id="_CPPv214MP3FreeDecoder11HMP3Decoder"></a> <a id="MP3FreeDecoder__HMP3Decoder"></a> <a id="mp3dec_8h_1ad25601e9d6320981423c457d9788bf6d"></a> void MP3FreeDecoder([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder)
:   Free the decoder of MP3.

    This API free the mp3 decoder module:

    - free platform-specific data allocated by InitMP3Decoder
    - zero out the contents of MP3DecInfo struct

    参数
    :   **HMP3Decoder** – valid MP3 decoder instance pointer

    返回
    :   None

<a id="_CPPv49MP3Decode11HMP3DecoderPPhPiPsi"></a>

<a id="_CPPv39MP3Decode11HMP3DecoderPPhPiPsi"></a> <a id="_CPPv29MP3Decode11HMP3DecoderPPhPiPsi"></a> <a id="MP3Decode__HMP3Decoder.unsigned-cPP.iP.shortP.i"></a> <a id="mp3dec_8h_1a5edfefe61cb0db9bf484565799b53f17"></a> int MP3Decode([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, unsigned char \*\*inbuf, int \*bytesLeft, short \*outbuf, int useSize)
:   Decode one frame of MP3 data.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer
        - **inbuf** – double pointer to buffer of MP3 data (containing headers \+ mainData)
        - **bytesLeft** – number of valid bytes remaining in inbuf
        - **outbuf** – pointer to outbuf, big enough to hold one frame of decoded PCM samples
        - **useSize** – flag indicating whether MP3 data is normal MPEG format (useSize \= 0\) or reformatted as “self-contained” frames (useSize \= 1\)

    返回
    :   error code, defined in mp3dec.h (0 means no error, \< 0 means error)

<a id="_CPPv419MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo"></a>

<a id="_CPPv319MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo"></a> <a id="_CPPv219MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo"></a> <a id="MP3GetLastFrameInfo__HMP3Decoder.MP3FrameInfoP"></a> <a id="mp3dec_8h_1a2071201a8fb14d270e0eedb7dc80b5f2"></a> void MP3GetLastFrameInfo([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, [MP3FrameInfo](#_CPPv412MP3FrameInfo "MP3FrameInfo") \*mp3FrameInfo)
:   Get info about last MP3 frame decoded.

    This API get the info about last mp3 decoded:

    - number of sampled decoded, sample rate, bitrate, etc.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer
        - **mp3FrameInfo** – pointer to MP3FrameInfo struct

    返回
    :   None

<a id="_CPPv419MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh"></a>

<a id="_CPPv319MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh"></a> <a id="_CPPv219MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh"></a> <a id="MP3GetNextFrameInfo__HMP3Decoder.MP3FrameInfoP.unsigned-cP"></a> <a id="mp3dec_8h_1afd79b0985cb05b9688b79aa24c97608c"></a> int MP3GetNextFrameInfo([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, [MP3FrameInfo](#_CPPv412MP3FrameInfo "MP3FrameInfo") \*mp3FrameInfo, unsigned char \*buf)
:   Parse MP3 frame header.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer
        - **mp3FrameInfo** – pointer to MP3FrameInfo struct
        - **buf** – pointer to buffer containing valid MP3 frame header

    返回
    :   error code, defined in mp3dec.h (0 means no error, \< 0 means error)

<a id="_CPPv415MP3FindSyncWordPhi"></a>

<a id="_CPPv315MP3FindSyncWordPhi"></a> <a id="_CPPv215MP3FindSyncWordPhi"></a> <a id="MP3FindSyncWord__unsigned-cP.i"></a> <a id="mp3dec_8h_1aea994f2cd1aa181b69ec2239cb15868f"></a> int MP3FindSyncWord(unsigned char \*buf, int nBytes)
:   locate the next byte-alinged sync word in the raw mp3 stream

    参数
    :   - **buf** – buffer to search for sync word
        - **nBytes** – max number of bytes to search in buffer

    返回
    :   - offset to first sync word (bytes from start of buf)
        - -1 if sync not found after searching nBytes

<a id="_CPPv416MP3SetBuffMethodPFPv6size_tEPFvPvEPFPvPvh6size_tE"></a>

<a id="_CPPv316MP3SetBuffMethodPFPv6size_tEPFvPvEPFPvPvh6size_tE"></a> <a id="_CPPv216MP3SetBuffMethodPFPv6size_tEPFvPvEPFPvPvh6size_tE"></a> <a id="mp3dec_8h_1a037c1e58a60e1f6a72c45ab122d67520"></a> int MP3SetBuffMethod(void \*(\*alloc)(size\_t size), void (\*free)(void \*buff), void \*(\*mset)(void \*s, unsigned char c, size\_t n))
:   indicate decoder which function to alloc free and memset This function must call before MP3InitDecoder or after MP3FreeDecoder.

    参数
    :   - **alloc** – alloc function
        - **free** – free function
        - **mset** – memset function

    返回
    :   - 0: success
        - other: err

<a id="structures"></a>

### Structures

<a id="_CPPv413_MP3FrameInfo"></a>

<a id="_CPPv313_MP3FrameInfo"></a> <a id="_CPPv213_MP3FrameInfo"></a> <a id="_MP3FrameInfo"></a> <a id="struct__MP3FrameInfo"></a> struct \_MP3FrameInfo

<a id="macros"></a>

### Macros

<a id="c.MAINBUF_SIZE"></a>

<a id="mp3dec_8h_1ac573437344d2a4bf65465a69bc9af057"></a> MAINBUF\_SIZE

<a id="c.MAX_NGRAN"></a>

<a id="mp3dec_8h_1ad84212b58ba787eabd6d82faed148ed4"></a> MAX\_NGRAN

<a id="c.MAX_NCHAN"></a>

<a id="mp3dec_8h_1a240dda341783cfa7555d346882298eb5"></a> MAX\_NCHAN

<a id="c.MAX_NSAMP"></a>

<a id="mp3dec_8h_1ae2981341264af607cbdbf3e47f6402e1"></a> MAX\_NSAMP

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411HMP3Decoder"></a>

<a id="_CPPv311HMP3Decoder"></a> <a id="_CPPv211HMP3Decoder"></a> <a id="HMP3Decoder"></a> <a id="mp3dec_8h_1a642ac5136c8ed3abf6ba3188a0ed6a49"></a> typedef void \*HMP3Decoder

<a id="_CPPv412MP3FrameInfo"></a>

<a id="_CPPv312MP3FrameInfo"></a> <a id="_CPPv212MP3FrameInfo"></a> <a id="MP3FrameInfo"></a> <a id="mp3dec_8h_1a4bc67ce69be089ebefa7a7d94ee8a5e6"></a> typedef struct [\_MP3FrameInfo](#_CPPv413_MP3FrameInfo "_MP3FrameInfo") MP3FrameInfo

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411MPEGVersion"></a>

<a id="_CPPv311MPEGVersion"></a> <a id="_CPPv211MPEGVersion"></a> <a id="mp3dec_8h_1ac2d41287c78fcc372e01a9ae30d5994a"></a> enum MPEGVersion
:   *Values:*

    <a id="_CPPv4N11MPEGVersion5MPEG1E"></a>

    <a id="_CPPv3N11MPEGVersion5MPEG1E"></a> <a id="_CPPv2N11MPEGVersion5MPEG1E"></a> <a id="mp3dec_8h_1ac2d41287c78fcc372e01a9ae30d5994aa762371aa5d006c42a0f7d4c474996acb"></a> enumerator MPEG1

    <a id="_CPPv4N11MPEGVersion5MPEG2E"></a>

    <a id="_CPPv3N11MPEGVersion5MPEG2E"></a> <a id="_CPPv2N11MPEGVersion5MPEG2E"></a> <a id="mp3dec_8h_1ac2d41287c78fcc372e01a9ae30d5994aa3a26a6d8f677e5de6054ef061c3da766"></a> enumerator MPEG2

    <a id="_CPPv4N11MPEGVersion6MPEG25E"></a>

    <a id="_CPPv3N11MPEGVersion6MPEG25E"></a> <a id="_CPPv2N11MPEGVersion6MPEG25E"></a> <a id="mp3dec_8h_1ac2d41287c78fcc372e01a9ae30d5994aa02dfbefc1cf38e2b2bb21ab49f266181"></a> enumerator MPEG25

<a id="_CPPv49err_mp3_t"></a>

<a id="_CPPv39err_mp3_t"></a> <a id="_CPPv29err_mp3_t"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7"></a> enum err\_mp3\_t
:   *Values:*

    <a id="_CPPv4N9err_mp3_t12ERR_MP3_NONEE"></a>

    <a id="_CPPv3N9err_mp3_t12ERR_MP3_NONEE"></a> <a id="_CPPv2N9err_mp3_t12ERR_MP3_NONEE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a3ec9ee57c5407c971c0bc6143f781b87"></a> enumerator ERR\_MP3\_NONE

    <a id="_CPPv4N9err_mp3_t24ERR_MP3_INDATA_UNDERFLOWE"></a>

    <a id="_CPPv3N9err_mp3_t24ERR_MP3_INDATA_UNDERFLOWE"></a> <a id="_CPPv2N9err_mp3_t24ERR_MP3_INDATA_UNDERFLOWE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a52150b697c525c08d77e79184ad1a433"></a> enumerator ERR\_MP3\_INDATA\_UNDERFLOW

    <a id="_CPPv4N9err_mp3_t26ERR_MP3_MAINDATA_UNDERFLOWE"></a>

    <a id="_CPPv3N9err_mp3_t26ERR_MP3_MAINDATA_UNDERFLOWE"></a> <a id="_CPPv2N9err_mp3_t26ERR_MP3_MAINDATA_UNDERFLOWE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a53763c658f773e575f7959876fe345e3"></a> enumerator ERR\_MP3\_MAINDATA\_UNDERFLOW

    <a id="_CPPv4N9err_mp3_t25ERR_MP3_FREE_BITRATE_SYNCE"></a>

    <a id="_CPPv3N9err_mp3_t25ERR_MP3_FREE_BITRATE_SYNCE"></a> <a id="_CPPv2N9err_mp3_t25ERR_MP3_FREE_BITRATE_SYNCE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7aa11c82f50a81b40816c38cd435c9ba58"></a> enumerator ERR\_MP3\_FREE\_BITRATE\_SYNC

    <a id="_CPPv4N9err_mp3_t21ERR_MP3_OUT_OF_MEMORYE"></a>

    <a id="_CPPv3N9err_mp3_t21ERR_MP3_OUT_OF_MEMORYE"></a> <a id="_CPPv2N9err_mp3_t21ERR_MP3_OUT_OF_MEMORYE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a60a4451d499ea0cedbc320cd17a112ba"></a> enumerator ERR\_MP3\_OUT\_OF\_MEMORY

    <a id="_CPPv4N9err_mp3_t20ERR_MP3_NULL_POINTERE"></a>

    <a id="_CPPv3N9err_mp3_t20ERR_MP3_NULL_POINTERE"></a> <a id="_CPPv2N9err_mp3_t20ERR_MP3_NULL_POINTERE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7ac8c88a531b54126fb71cc6450c3de49c"></a> enumerator ERR\_MP3\_NULL\_POINTER

    <a id="_CPPv4N9err_mp3_t27ERR_MP3_INVALID_FRAMEHEADERE"></a>

    <a id="_CPPv3N9err_mp3_t27ERR_MP3_INVALID_FRAMEHEADERE"></a> <a id="_CPPv2N9err_mp3_t27ERR_MP3_INVALID_FRAMEHEADERE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a64d6b3441dd2552a0b0a2288562108e3"></a> enumerator ERR\_MP3\_INVALID\_FRAMEHEADER

    <a id="_CPPv4N9err_mp3_t24ERR_MP3_INVALID_SIDEINFOE"></a>

    <a id="_CPPv3N9err_mp3_t24ERR_MP3_INVALID_SIDEINFOE"></a> <a id="_CPPv2N9err_mp3_t24ERR_MP3_INVALID_SIDEINFOE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7abb0bb14ed2a2d06509c9f052fc099b68"></a> enumerator ERR\_MP3\_INVALID\_SIDEINFO

    <a id="_CPPv4N9err_mp3_t25ERR_MP3_INVALID_SCALEFACTE"></a>

    <a id="_CPPv3N9err_mp3_t25ERR_MP3_INVALID_SCALEFACTE"></a> <a id="_CPPv2N9err_mp3_t25ERR_MP3_INVALID_SCALEFACTE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a079f726b0148dcce6ffeb492027a47dd"></a> enumerator ERR\_MP3\_INVALID\_SCALEFACT

    <a id="_CPPv4N9err_mp3_t25ERR_MP3_INVALID_HUFFCODESE"></a>

    <a id="_CPPv3N9err_mp3_t25ERR_MP3_INVALID_HUFFCODESE"></a> <a id="_CPPv2N9err_mp3_t25ERR_MP3_INVALID_HUFFCODESE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a57ef9fea074d203de7c0eb0039ebc07d"></a> enumerator ERR\_MP3\_INVALID\_HUFFCODES

    <a id="_CPPv4N9err_mp3_t26ERR_MP3_INVALID_DEQUANTIZEE"></a>

    <a id="_CPPv3N9err_mp3_t26ERR_MP3_INVALID_DEQUANTIZEE"></a> <a id="_CPPv2N9err_mp3_t26ERR_MP3_INVALID_DEQUANTIZEE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a7ce83e71f62ab231ca68ac29b3cdaa0a"></a> enumerator ERR\_MP3\_INVALID\_DEQUANTIZE

    <a id="_CPPv4N9err_mp3_t21ERR_MP3_INVALID_IMDCTE"></a>

    <a id="_CPPv3N9err_mp3_t21ERR_MP3_INVALID_IMDCTE"></a> <a id="_CPPv2N9err_mp3_t21ERR_MP3_INVALID_IMDCTE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a14351ac1f44ecf0e8057b56a39db12dc"></a> enumerator ERR\_MP3\_INVALID\_IMDCT

    <a id="_CPPv4N9err_mp3_t23ERR_MP3_INVALID_SUBBANDE"></a>

    <a id="_CPPv3N9err_mp3_t23ERR_MP3_INVALID_SUBBANDE"></a> <a id="_CPPv2N9err_mp3_t23ERR_MP3_INVALID_SUBBANDE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a772e21f8ab1a9b69b02134b5540c1a31"></a> enumerator ERR\_MP3\_INVALID\_SUBBAND

    <a id="_CPPv4N9err_mp3_t11ERR_UNKNOWNE"></a>

    <a id="_CPPv3N9err_mp3_t11ERR_UNKNOWNE"></a> <a id="_CPPv2N9err_mp3_t11ERR_UNKNOWNE"></a> <a id="mp3dec_8h_1ae6b88be3f6b68d50519284d03d875fa7a5c708decdcbd7d8c9fddd8d9e75828a1"></a> enumerator ERR\_UNKNOWN
