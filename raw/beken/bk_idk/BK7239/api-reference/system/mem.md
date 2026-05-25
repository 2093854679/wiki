# MEMORY API[](#memory-api "永久链接至标题")


> - OS抽象层对所有的内存申请以及释放接口都做了封装


## Header File[](#header-file "永久链接至标题")


- [mem.h](https://github.com/bekencorp/armino/blob/main/components/mem.h "https://github.com/bekencorp/armino/blob/main/components/mem.h")


## Functions[](#functions "永久链接至标题")

void *os_memcpy(void *out, const void *in, UINT32 n)[](#_CPPv49os_memcpyPvPKv6UINT32 "永久链接至目标")
:   copies data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memcpy

    参数
    :   - **out** – : the pointer of source memory location

        - **in** – : the pointer of destinated memory location

        - **n** – : the specified length

static inline void os_memcpy_word(uint32_t *out, const uint32_t *in, uint32_t n)[](#_CPPv414os_memcpy_wordP8uint32_tPK8uint32_t8uint32_t "永久链接至目标")

static inline void os_memset_word(uint32_t *b, int32_t c, uint32_t n)[](#_CPPv414os_memset_wordP8uint32_t7int32_t8uint32_t "永久链接至目标")

INT32 os_memcmp(const void *s1, const void *s2, UINT32 n)[](#_CPPv49os_memcmpPKvPKv6UINT32 "永久链接至目标")
:   comparing the size of two memory blocks by specified length

    备注

    this function is a wrapper for memcmp

    参数
    :   - **s1** – : the pointer of a memory block

        - **s2** – : the pointer of other memory block

        - **n** – : the specified length

    返回
    :   the comarison results

void *os_memmove(void *out, const void *in, UINT32 n)[](#_CPPv410os_memmovePvPKv6UINT32 "永久链接至目标")
:   move data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memmove

    参数
    :   - **out** – : the pointer of source memory location

        - **in** – : the pointer of destinated memory location

        - **n** – : the specified length

int os_memcmp_const(const void *a, const void *b, size_t len)[](#_CPPv415os_memcmp_constPKvPKv6size_t "永久链接至目标")
:   copies data from one memory location to another memory location with specified length

    备注

    this function is a wrapper for memcpy

    参数
    :   - **a** – : the pointer of source memory location

        - **b** – : the pointer of destinated memory location

        - **len** – : the specified length

void *os_memset(void *b, int c, UINT32 len)[](#_CPPv49os_memsetPvi6UINT32 "永久链接至目标")
:   fill or copy a given value into the specified len bytes of the specified memory

    备注

    this function is a wrapper for memset

    参数
    :   - **b** – : the pointer of the specified memory

        - **c** – : the given value

        - **len** – : the specified length

void *os_realloc(void *ptr, size_t size)[](#_CPPv410os_reallocPv6size_t "永久链接至目标")
:   reallocate memory

    备注

    this API cannot be called in interrupt context

    参数
    :   - **ptr** – : the pointer of the specified memory

        - **size** – : the reallocate memory length

void *bk_psram_realloc(void *ptr, size_t size)[](#_CPPv416bk_psram_reallocPv6size_t "永久链接至目标")
:   reallocate memory in psram

    备注

    this API cannot be called in interrupt context

    参数
    :   - **ptr** – : the pointer of the specified memory

        - **size** – : the reallocate memory length

void *psram_realloc(void *ptr, size_t size)[](#_CPPv413psram_reallocPv6size_t "永久链接至目标")

void *os_malloc(size_t size)[](#_CPPv49os_malloc6size_t "永久链接至目标")
:   request memory according to the specified size

    备注

    This API cannot be called in interrupt context. When macro CONFIG_USE_PSRAM_HEAP_AT_SRAM_OOM is configured, if sram is insufficient,the system will try to request memory form psram

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void *os_sram_malloc(size_t size)[](#_CPPv414os_sram_malloc6size_t "永久链接至目标")
:   request memory according to the specified size

    备注

    This API cannot be called in interrupt context. and only request memory in sram when call this API

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void os_free(void *ptr)[](#_CPPv47os_freePv "永久链接至目标")
:   release preciously reuqested memory

    备注

    This API cannot be called in interrupt context.

    参数
    :   **ptr** – : the pointer of the handle previously requested

void *os_zalloc(size_t size)[](#_CPPv49os_zalloc6size_t "永久链接至目标")
:   request memory of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for memset and malloc

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void *psram_malloc(size_t size)[](#_CPPv412psram_malloc6size_t "永久链接至目标")
:   request memory in psram according to the specified size

    备注

    This API cannot be called in interrupt context.

    参数
    :   **size** – : requested pspram memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void *psram_zalloc(size_t size)[](#_CPPv412psram_zalloc6size_t "永久链接至目标")
:   request psram memory of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for psram_malloc and memset

    参数
    :   **size** – : requested psram memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void *os_sram_calloc(size_t a, size_t b)[](#_CPPv414os_sram_calloc6size_t6size_t "永久链接至目标")
:   request memory in sram of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for os_sram_malloc and memset

    参数
    :   - **a** – : the number of elements to allocate

        - **b** – : the size of each element in bytes

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void *os_sram_zalloc(size_t size)[](#_CPPv414os_sram_zalloc6size_t "永久链接至目标")
:   request memory in sram of a specified size and auotmatically initializes the allocated memory to zero

    备注

    This API cannot be called in interrupt context. and this function is a wrapper for os_sram_malloc and memset

    参数
    :   **size** – : requested memory size in sram

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

uint32_t bk_psram_heap_get_used_count(void)[](#_CPPv428bk_psram_heap_get_used_countv "永久链接至目标")
:   get the current used psram size

    返回
    :   psram size has been used

void bk_psram_heap_get_used_state(void)[](#_CPPv428bk_psram_heap_get_used_statev "永久链接至目标")
:   get detailed information about the current psram in use

void bk_psram_heap_dump_data(void)[](#_CPPv423bk_psram_heap_dump_datav "永久链接至目标")

void *os_malloc_wifi_buffer(size_t size)[](#_CPPv421os_malloc_wifi_buffer6size_t "永久链接至目标")
:   request memory according to the specified size

    参数
    :   **size** – : requested memory size

    返回
    :   if request success, return the pointer of the memory, otherwise NULL is returned

void os_show_memory_config_info(void)[](#_CPPv426os_show_memory_config_infov "永久链接至目标")
:   show current system memory information


## Macros[](#macros "永久链接至标题")

os_write_word(addr, val)[](#c.os_write_word "永久链接至目标")
:   write value by word size

os_read_word(addr, val)[](#c.os_read_word "永久链接至目标")
:   read value by word size

os_get_word(addr)[](#c.os_get_word "永久链接至目标")
:   get value by word size

psram_free[](#c.psram_free "永久链接至目标")


## Enumerations[](#enumerations "永久链接至标题")

enum beken_mem_type_t[](#_CPPv416beken_mem_type_t "永久链接至目标")
:   Memory type for mempool.


    *Values:*

    enumerator HEAP_MEM_TYPE_DEFAULT[](#_CPPv4N16beken_mem_type_t21HEAP_MEM_TYPE_DEFAULTE "永久链接至目标")
    :   Default heap memory type

    enumerator HEAP_MEM_TYPE_SRAM[](#_CPPv4N16beken_mem_type_t18HEAP_MEM_TYPE_SRAME "永久链接至目标")
    :   SRAM heap memory type

    enumerator HEAP_MEM_TYPE_PSRAM[](#_CPPv4N16beken_mem_type_t19HEAP_MEM_TYPE_PSRAME "永久链接至目标")
    :   PSRAM heap memory type

    enumerator MEM_TYPE_MAX[](#_CPPv4N16beken_mem_type_t12MEM_TYPE_MAXE "永久链接至目标")
