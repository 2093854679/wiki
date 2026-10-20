---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/api-reference/system/mem.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="memory-api"></a>

# MEMORY API

> - OS抽象层对所有的内存申请以及释放接口都做了封装

<a id="header-file"></a>

## Header File

- [mem.h](https://github.com/bekencorp/armino/blob/main/components/mem.h)

<a id="functions"></a>

## Functions

<a id="_CPPv49os_memcpyPvPKv6UINT32"></a>

<a id="_CPPv39os_memcpyPvPKv6UINT32"></a> <a id="_CPPv29os_memcpyPvPKv6UINT32"></a> <a id="os_memcpy__voidP.voidCP.UINT32"></a> <a id="mem_8h_1ad2fbeff19f5fb83eb027793e37cb31b1"></a> void \*os\_memcpy(void \*out, const void \*in, UINT32 n)
:   copies data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memcpy

    参数
    :   - **out** – : the pointer of source memory location
        - **in** – : the pointer of destinated memory location
        - **n** – : the specified length

<a id="_CPPv414os_memcpy_wordP8uint32_tPK8uint32_t8uint32_t"></a>

<a id="_CPPv314os_memcpy_wordP8uint32_tPK8uint32_t8uint32_t"></a> <a id="_CPPv214os_memcpy_wordP8uint32_tPK8uint32_t8uint32_t"></a> <a id="os_memcpy_word__uint32_tP.uint32_tCP.uint32_t"></a> <a id="mem_8h_1af8d7c789ad347187112a8f99ab48462e"></a> static inline void os\_memcpy\_word(uint32\_t \*out, const uint32\_t \*in, uint32\_t n)

<a id="_CPPv414os_memset_wordP8uint32_t7int32_t8uint32_t"></a>

<a id="_CPPv314os_memset_wordP8uint32_t7int32_t8uint32_t"></a> <a id="_CPPv214os_memset_wordP8uint32_t7int32_t8uint32_t"></a> <a id="os_memset_word__uint32_tP.int32_t.uint32_t"></a> <a id="mem_8h_1aa84a347bcbbb72f21ab8f11dc4462a91"></a> static inline void os\_memset\_word(uint32\_t \*b, int32\_t c, uint32\_t n)

<a id="_CPPv49os_memcmpPKvPKv6UINT32"></a>

<a id="_CPPv39os_memcmpPKvPKv6UINT32"></a> <a id="_CPPv29os_memcmpPKvPKv6UINT32"></a> <a id="os_memcmp__voidCP.voidCP.UINT32"></a> <a id="mem_8h_1a1ac44484c07d02c25bfc1ec713dd82e5"></a> INT32 os\_memcmp(const void \*s1, const void \*s2, UINT32 n)
:   comparing the size of two memory blocks by specified length

    备注

    this function is a wrapper for memcmp

    参数
    :   - **s1** – : the pointer of a memory block
        - **s2** – : the pointer of other memory block
        - **n** – : the specified length

    返回
    :   the comarison results

<a id="_CPPv410os_memmovePvPKv6UINT32"></a>

<a id="_CPPv310os_memmovePvPKv6UINT32"></a> <a id="_CPPv210os_memmovePvPKv6UINT32"></a> <a id="os_memmove__voidP.voidCP.UINT32"></a> <a id="mem_8h_1a628dffeb612c0a69157f4bce0c382af8"></a> void \*os\_memmove(void \*out, const void \*in, UINT32 n)
:   move data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memmove

    参数
    :   - **out** – : the pointer of source memory location
        - **in** – : the pointer of destinated memory location
        - **n** – : the specified length

<a id="_CPPv415os_memcmp_constPKvPKv6size_t"></a>

<a id="_CPPv315os_memcmp_constPKvPKv6size_t"></a> <a id="_CPPv215os_memcmp_constPKvPKv6size_t"></a> <a id="os_memcmp_const__voidCP.voidCP.s"></a> <a id="mem_8h_1a296e7c104994ed04b91824c5c7dad826"></a> int os\_memcmp\_const(const void \*a, const void \*b, size\_t len)
:   copies data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memcpy

    参数
    :   - **a** – : the pointer of source memory location
        - **b** – : the pointer of destinated memory location
        - **len** – : the specified length

<a id="_CPPv49os_memsetPvi6UINT32"></a>

<a id="_CPPv39os_memsetPvi6UINT32"></a> <a id="_CPPv29os_memsetPvi6UINT32"></a> <a id="os_memset__voidP.i.UINT32"></a> <a id="mem_8h_1a365bbcacee95e9540924f5716a67b44b"></a> void \*os\_memset(void \*b, int c, UINT32 len)
:   fill or copy a given value into the specified len bytes of the specified memory

    备注

    this function is a wrapper for memset

    参数
    :   - **b** – : the pointer of the specified memory
        - **c** – : the given value
        - **len** – : the specified length

<a id="_CPPv410os_reallocPv6size_t"></a>

<a id="_CPPv310os_reallocPv6size_t"></a> <a id="_CPPv210os_reallocPv6size_t"></a> <a id="os_realloc__voidP.s"></a> <a id="mem_8h_1a85b4d559dcc26eebbf45948a8b89bfa8"></a> void \*os\_realloc(void \*ptr, size\_t size)
:   reallocate memory

    备注

    this API cannot be called in interrupt context

    参数
    :   - **ptr** – : the pointer of the specified memory
        - **size** – : the reallocate memory length

<a id="_CPPv416bk_psram_reallocPv6size_t"></a>

<a id="_CPPv316bk_psram_reallocPv6size_t"></a> <a id="_CPPv216bk_psram_reallocPv6size_t"></a> <a id="bk_psram_realloc__voidP.s"></a> <a id="mem_8h_1ab30f3c6f6fbd7234b4c07d86ba3b441f"></a> void \*bk\_psram\_realloc(void \*ptr, size\_t size)
:   reallocate memory in psram

    备注

    this API cannot be called in interrupt context

    参数
    :   - **ptr** – : the pointer of the specified memory
        - **size** – : the reallocate memory length

<a id="_CPPv413psram_reallocPv6size_t"></a>

<a id="_CPPv313psram_reallocPv6size_t"></a> <a id="_CPPv213psram_reallocPv6size_t"></a> <a id="psram_realloc__voidP.s"></a> <a id="mem_8h_1a4c07b910691fe0526dae974986df31cc"></a> void \*psram\_realloc(void \*ptr, size\_t size)

<a id="_CPPv49os_malloc6size_t"></a>

<a id="_CPPv39os_malloc6size_t"></a> <a id="_CPPv29os_malloc6size_t"></a> <a id="os_malloc__s"></a> <a id="mem_8h_1a9b493410962f80a9540ba875256e5836"></a> void \*os\_malloc(size\_t size)
:   request memory according to the specified size

    备注

    This API cannot be called in interrupt context. When macro CONFIG\_USE\_PSRAM\_HEAP\_AT\_SRAM\_OOM is configured, if sram is insufficient,the system will try to request memory form psram

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv414os_sram_malloc6size_t"></a>

<a id="_CPPv314os_sram_malloc6size_t"></a> <a id="_CPPv214os_sram_malloc6size_t"></a> <a id="os_sram_malloc__s"></a> <a id="mem_8h_1a8d42e7ce2f4b1a16ba58afe7d649b738"></a> void \*os\_sram\_malloc(size\_t size)
:   request memory according to the specified size

    备注

    This API cannot be called in interrupt context. and only request memory in sram when call this API

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv47os_freePv"></a>

<a id="_CPPv37os_freePv"></a> <a id="_CPPv27os_freePv"></a> <a id="os_free__voidP"></a> <a id="mem_8h_1a19e18feddb1432638b0b57fb70ee2ff1"></a> void os\_free(void \*ptr)
:   release preciously reuqested memory

    备注

    This API cannot be called in interrupt context.

    参数
    :   **ptr** – : the pointer of the handle previously requested

<a id="_CPPv49os_zalloc6size_t"></a>

<a id="_CPPv39os_zalloc6size_t"></a> <a id="_CPPv29os_zalloc6size_t"></a> <a id="os_zalloc__s"></a> <a id="mem_8h_1aa3941c5693466d194ef568dfe2f299e6"></a> void \*os\_zalloc(size\_t size)
:   request memory of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for memset and malloc

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv412psram_malloc6size_t"></a>

<a id="_CPPv312psram_malloc6size_t"></a> <a id="_CPPv212psram_malloc6size_t"></a> <a id="psram_malloc__s"></a> <a id="mem_8h_1a6cee33eea9726ca2ee777507f1581ea3"></a> void \*psram\_malloc(size\_t size)
:   request memory in psram according to the specified size

    备注

    This API cannot be called in interrupt context.

    参数
    :   **size** – : requested pspram memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv412psram_zalloc6size_t"></a>

<a id="_CPPv312psram_zalloc6size_t"></a> <a id="_CPPv212psram_zalloc6size_t"></a> <a id="psram_zalloc__s"></a> <a id="mem_8h_1a0b29a3792fa60214a944dc1ef3381269"></a> void \*psram\_zalloc(size\_t size)
:   request psram memory of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for psram\_malloc and memset

    参数
    :   **size** – : requested psram memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv414os_sram_calloc6size_t6size_t"></a>

<a id="_CPPv314os_sram_calloc6size_t6size_t"></a> <a id="_CPPv214os_sram_calloc6size_t6size_t"></a> <a id="os_sram_calloc__s.s"></a> <a id="mem_8h_1a637ac490454c5d5cca6c0ec6f5896d6f"></a> void \*os\_sram\_calloc(size\_t a, size\_t b)
:   request memory in sram of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for os\_sram\_malloc and memset

    参数
    :   - **a** – : the number of elements to allocate
        - **b** – : the size of each element in bytes

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv414os_sram_zalloc6size_t"></a>

<a id="_CPPv314os_sram_zalloc6size_t"></a> <a id="_CPPv214os_sram_zalloc6size_t"></a> <a id="os_sram_zalloc__s"></a> <a id="mem_8h_1aabb36c2b16695944ef5fd809c100eb93"></a> void \*os\_sram\_zalloc(size\_t size)
:   request memory in sram of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for os\_sram\_malloc and memset

    参数
    :   **size** – : requested memory size in sram

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv428bk_psram_heap_get_used_countv"></a>

<a id="_CPPv328bk_psram_heap_get_used_countv"></a> <a id="_CPPv228bk_psram_heap_get_used_countv"></a> <a id="bk_psram_heap_get_used_count__void"></a> <a id="mem_8h_1aaefaa4cfd29388c2f45cd8ed7be05f29"></a> uint32\_t bk\_psram\_heap\_get\_used\_count(void)
:   get the current used psram size

    返回
    :   psram size has been used

<a id="_CPPv428bk_psram_heap_get_used_statev"></a>

<a id="_CPPv328bk_psram_heap_get_used_statev"></a> <a id="_CPPv228bk_psram_heap_get_used_statev"></a> <a id="bk_psram_heap_get_used_state__void"></a> <a id="mem_8h_1a5aa754a7e7a6ad658c42a9740ad22ad6"></a> void bk\_psram\_heap\_get\_used\_state(void)
:   get detailed information about the current psram in use

<a id="_CPPv423bk_psram_heap_dump_datav"></a>

<a id="_CPPv323bk_psram_heap_dump_datav"></a> <a id="_CPPv223bk_psram_heap_dump_datav"></a> <a id="bk_psram_heap_dump_data__void"></a> <a id="mem_8h_1ad99d556875d4682466d93a1b7db5f9f0"></a> void bk\_psram\_heap\_dump\_data(void)

<a id="_CPPv421os_malloc_wifi_buffer6size_t"></a>

<a id="_CPPv321os_malloc_wifi_buffer6size_t"></a> <a id="_CPPv221os_malloc_wifi_buffer6size_t"></a> <a id="os_malloc_wifi_buffer__s"></a> <a id="mem_8h_1a4fb6194f86d898c3219b23ab4ac05277"></a> void \*os\_malloc\_wifi\_buffer(size\_t size)
:   request memory according to the specified size

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

<a id="_CPPv426os_show_memory_config_infov"></a>

<a id="_CPPv326os_show_memory_config_infov"></a> <a id="_CPPv226os_show_memory_config_infov"></a> <a id="os_show_memory_config_info__void"></a> <a id="mem_8h_1a36b0a4b34d9b176db76dee56d3cc35bb"></a> void os\_show\_memory\_config\_info(void)
:   show current system memory information

<a id="macros"></a>

## Macros

<a id="c.os_write_word"></a>

<a id="mem_8h_1a25287c9425e9f02f93e78cec9a59f458"></a> os\_write\_word(addr, val)
:   write value by word size

<a id="c.os_read_word"></a>

<a id="mem_8h_1aa62bceb44ab313d8720c91e3cef055af"></a> os\_read\_word(addr, val)
:   read value by word size

<a id="c.os_get_word"></a>

<a id="mem_8h_1ae71df85dcd2cf6926aaff94202bc5eb0"></a> os\_get\_word(addr)
:   get value by word size

<a id="c.psram_free"></a>

<a id="mem_8h_1a57ee65c70397866a222f050e1251dad6"></a> psram\_free

<a id="enumerations"></a>

## Enumerations

<a id="_CPPv416beken_mem_type_t"></a>

<a id="_CPPv316beken_mem_type_t"></a> <a id="_CPPv216beken_mem_type_t"></a> <a id="mem_8h_1a197a8ff74af34020741bc86a675d6e26"></a> enum beken\_mem\_type\_t
:   Memory type for mempool.

    *Values:*

    <a id="_CPPv4N16beken_mem_type_t21HEAP_MEM_TYPE_DEFAULTE"></a>

    <a id="_CPPv3N16beken_mem_type_t21HEAP_MEM_TYPE_DEFAULTE"></a> <a id="_CPPv2N16beken_mem_type_t21HEAP_MEM_TYPE_DEFAULTE"></a> <a id="mem_8h_1a197a8ff74af34020741bc86a675d6e26af96816228a11886e48bd8aef61115fb3"></a> enumerator HEAP\_MEM\_TYPE\_DEFAULT
    :   Default heap memory type

    <a id="_CPPv4N16beken_mem_type_t18HEAP_MEM_TYPE_SRAME"></a>

    <a id="_CPPv3N16beken_mem_type_t18HEAP_MEM_TYPE_SRAME"></a> <a id="_CPPv2N16beken_mem_type_t18HEAP_MEM_TYPE_SRAME"></a> <a id="mem_8h_1a197a8ff74af34020741bc86a675d6e26a1ef55a61db33b1cf18476dafadab52b6"></a> enumerator HEAP\_MEM\_TYPE\_SRAM
    :   SRAM heap memory type

    <a id="_CPPv4N16beken_mem_type_t19HEAP_MEM_TYPE_PSRAME"></a>

    <a id="_CPPv3N16beken_mem_type_t19HEAP_MEM_TYPE_PSRAME"></a> <a id="_CPPv2N16beken_mem_type_t19HEAP_MEM_TYPE_PSRAME"></a> <a id="mem_8h_1a197a8ff74af34020741bc86a675d6e26a3fbe5f328371762d334e0eed321cbd37"></a> enumerator HEAP\_MEM\_TYPE\_PSRAM
    :   PSRAM heap memory type

    <a id="_CPPv4N16beken_mem_type_t12MEM_TYPE_MAXE"></a>

    <a id="_CPPv3N16beken_mem_type_t12MEM_TYPE_MAXE"></a> <a id="_CPPv2N16beken_mem_type_t12MEM_TYPE_MAXE"></a> <a id="mem_8h_1a197a8ff74af34020741bc86a675d6e26abc3abf961af8c1ab270e48fa3f0f24e3"></a> enumerator MEM\_TYPE\_MAX
