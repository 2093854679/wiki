# MP3 APIs[](#mp3-apis "永久链接至标题")


重要

The MP3 API v1.0 is the lastest stable MP3 APIs. It supports MPEG-1, MPEG-2 and MPEG-2.5 standard Layer3 decoding. All new applications should use MP3 API v1.0.


## MP3 API Categories[](#mp3-api-categories "永久链接至标题")

MP3 APIs:
:   - [`MP3InitDecoder()`](#_CPPv414MP3InitDecoderv "MP3InitDecoder") - allocate memory for platform-specific data and clear all the user-accessible fields

    - [`MP3FreeDecoder()`](#_CPPv414MP3FreeDecoder11HMP3Decoder "MP3FreeDecoder") - free platform-specific data allocated by InitMP3Decoder and zero out the contents of MP3DecInfo struct

    - [`MP3FindSyncWord()`](#_CPPv415MP3FindSyncWordPhi "MP3FindSyncWord") - locate the next byte-alinged sync word in the raw mp3 stream

    - [`MP3Decode()`](#_CPPv49MP3Decode11HMP3DecoderPPhPiPsi "MP3Decode") - decode one frame of MP3 data

    - [`MP3GetLastFrameInfo()`](#_CPPv419MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo "MP3GetLastFrameInfo") - get info about last MP3 frame decoded (number of sampled decoded, sample rate, bitrate, etc.)

    - [`MP3GetNextFrameInfo()`](#_CPPv419MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh "MP3GetNextFrameInfo") - parse MP3 frame header


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [mp3dec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/mp3dec.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/mp3dec.h")


### Functions[](#functions "永久链接至标题")

[HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") MP3InitDecoder(void)[](#_CPPv414MP3InitDecoderv "永久链接至目标")
:   Init the decoder of MP3.

    This API init the mp3 decoder module:


    - allocate memory for platform-specific data

    - clear all the user-accessible fields

    参数
    :   **None** –

    返回
    :   None

void MP3FreeDecoder([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder)[](#_CPPv414MP3FreeDecoder11HMP3Decoder "永久链接至目标")
:   Free the decoder of MP3.

    This API free the mp3 decoder module:


    - free platform-specific data allocated by InitMP3Decoder

    - zero out the contents of MP3DecInfo struct

    参数
    :   **HMP3Decoder** – valid MP3 decoder instance pointer

    返回
    :   None

int MP3Decode([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, unsigned char **inbuf, int *bytesLeft, short *outbuf, int useSize)[](#_CPPv49MP3Decode11HMP3DecoderPPhPiPsi "永久链接至目标")
:   Decode one frame of MP3 data.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer

        - **inbuf** – double pointer to buffer of MP3 data (containing headers + mainData)

        - **bytesLeft** – number of valid bytes remaining in inbuf

        - **outbuf** – pointer to outbuf, big enough to hold one frame of decoded PCM samples

        - **useSize** – flag indicating whether MP3 data is normal MPEG format (useSize = 0) or reformatted as “self-contained” frames (useSize = 1)

    返回
    :   error code, defined in mp3dec.h (0 means no error, < 0 means error)

void MP3GetLastFrameInfo([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, [MP3FrameInfo](#_CPPv412MP3FrameInfo "MP3FrameInfo") *mp3FrameInfo)[](#_CPPv419MP3GetLastFrameInfo11HMP3DecoderP12MP3FrameInfo "永久链接至目标")
:   Get info about last MP3 frame decoded.

    This API get the info about last mp3 decoded:


    - number of sampled decoded, sample rate, bitrate, etc.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer

        - **mp3FrameInfo** – pointer to MP3FrameInfo struct

    返回
    :   None

int MP3GetNextFrameInfo([HMP3Decoder](#_CPPv411HMP3Decoder "HMP3Decoder") hMP3Decoder, [MP3FrameInfo](#_CPPv412MP3FrameInfo "MP3FrameInfo") *mp3FrameInfo, unsigned char *buf)[](#_CPPv419MP3GetNextFrameInfo11HMP3DecoderP12MP3FrameInfoPh "永久链接至目标")
:   Parse MP3 frame header.

    参数
    :   - **hMP3Decoder** – valid MP3 decoder instance pointer

        - **mp3FrameInfo** – pointer to MP3FrameInfo struct

        - **buf** – pointer to buffer containing valid MP3 frame header

    返回
    :   error code, defined in mp3dec.h (0 means no error, < 0 means error)

int MP3FindSyncWord(unsigned char *buf, int nBytes)[](#_CPPv415MP3FindSyncWordPhi "永久链接至目标")
:   locate the next byte-alinged sync word in the raw mp3 stream

    参数
    :   - **buf** – buffer to search for sync word

        - **nBytes** – max number of bytes to search in buffer

    返回
    :   - offset to first sync word (bytes from start of buf)

        - -1 if sync not found after searching nBytes

int MP3SetBuffMethod(void *(*alloc)(size_t size), void (*free)(void *buff), void *(*mset)(void *s, unsigned char c, size_t n))[](#_CPPv416MP3SetBuffMethodPFPv6size_tEPFvPvEPFPvPvh6size_tE "永久链接至目标")
:   indicate decoder which function to alloc free and memset This function must call before MP3InitDecoder or after MP3FreeDecoder.

    参数
    :   - **alloc** – alloc function

        - **free** – free function

        - **mset** – memset function

    返回
    :   - 0: success

        - other: err


### Structures[](#structures "永久链接至标题")

struct _MP3FrameInfo[](#_CPPv413_MP3FrameInfo "永久链接至目标")


### Macros[](#macros "永久链接至标题")

MAINBUF_SIZE[](#c.MAINBUF_SIZE "永久链接至目标")

MAX_NGRAN[](#c.MAX_NGRAN "永久链接至目标")

MAX_NCHAN[](#c.MAX_NCHAN "永久链接至目标")

MAX_NSAMP[](#c.MAX_NSAMP "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void *HMP3Decoder[](#_CPPv411HMP3Decoder "永久链接至目标")

typedef struct [_MP3FrameInfo](#_CPPv413_MP3FrameInfo "_MP3FrameInfo") MP3FrameInfo[](#_CPPv412MP3FrameInfo "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum MPEGVersion[](#_CPPv411MPEGVersion "永久链接至目标")
:   *Values:*

    enumerator MPEG1[](#_CPPv4N11MPEGVersion5MPEG1E "永久链接至目标")

    enumerator MPEG2[](#_CPPv4N11MPEGVersion5MPEG2E "永久链接至目标")

    enumerator MPEG25[](#_CPPv4N11MPEGVersion6MPEG25E "永久链接至目标")

enum err_mp3_t[](#_CPPv49err_mp3_t "永久链接至目标")
:   *Values:*

    enumerator ERR_MP3_NONE[](#_CPPv4N9err_mp3_t12ERR_MP3_NONEE "永久链接至目标")

    enumerator ERR_MP3_INDATA_UNDERFLOW[](#_CPPv4N9err_mp3_t24ERR_MP3_INDATA_UNDERFLOWE "永久链接至目标")

    enumerator ERR_MP3_MAINDATA_UNDERFLOW[](#_CPPv4N9err_mp3_t26ERR_MP3_MAINDATA_UNDERFLOWE "永久链接至目标")

    enumerator ERR_MP3_FREE_BITRATE_SYNC[](#_CPPv4N9err_mp3_t25ERR_MP3_FREE_BITRATE_SYNCE "永久链接至目标")

    enumerator ERR_MP3_OUT_OF_MEMORY[](#_CPPv4N9err_mp3_t21ERR_MP3_OUT_OF_MEMORYE "永久链接至目标")

    enumerator ERR_MP3_NULL_POINTER[](#_CPPv4N9err_mp3_t20ERR_MP3_NULL_POINTERE "永久链接至目标")

    enumerator ERR_MP3_INVALID_FRAMEHEADER[](#_CPPv4N9err_mp3_t27ERR_MP3_INVALID_FRAMEHEADERE "永久链接至目标")

    enumerator ERR_MP3_INVALID_SIDEINFO[](#_CPPv4N9err_mp3_t24ERR_MP3_INVALID_SIDEINFOE "永久链接至目标")

    enumerator ERR_MP3_INVALID_SCALEFACT[](#_CPPv4N9err_mp3_t25ERR_MP3_INVALID_SCALEFACTE "永久链接至目标")

    enumerator ERR_MP3_INVALID_HUFFCODES[](#_CPPv4N9err_mp3_t25ERR_MP3_INVALID_HUFFCODESE "永久链接至目标")

    enumerator ERR_MP3_INVALID_DEQUANTIZE[](#_CPPv4N9err_mp3_t26ERR_MP3_INVALID_DEQUANTIZEE "永久链接至目标")

    enumerator ERR_MP3_INVALID_IMDCT[](#_CPPv4N9err_mp3_t21ERR_MP3_INVALID_IMDCTE "永久链接至目标")

    enumerator ERR_MP3_INVALID_SUBBAND[](#_CPPv4N9err_mp3_t23ERR_MP3_INVALID_SUBBANDE "永久链接至目标")

    enumerator ERR_UNKNOWN[](#_CPPv4N9err_mp3_t11ERR_UNKNOWNE "永久链接至目标")
