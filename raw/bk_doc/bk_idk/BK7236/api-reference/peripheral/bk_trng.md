# TRNG[](#trng "永久链接至标题")


## TRNG API Status[](#trng-api-status "永久链接至标题")

| API | BK7236 | BK7236_cp1 |
| --- | --- | --- |
| [`bk_trng_driver_init()`](#_CPPv419bk_trng_driver_initv "bk_trng_driver_init") | Y | Y |
| [`bk_trng_driver_deinit()`](#_CPPv421bk_trng_driver_deinitv "bk_trng_driver_deinit") | Y | Y |
| [`bk_trng_start()`](#_CPPv413bk_trng_startv "bk_trng_start") | Y | Y |
| [`bk_trng_stop()`](#_CPPv412bk_trng_stopv "bk_trng_stop") | Y | Y |
| [`bk_rand()`](#_CPPv47bk_randv "bk_rand") | Y | Y |


## TRNG API Reference[](#trng-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [trng.h](https://github.com/bekencorp/armino/blob/main/components/trng.h "https://github.com/bekencorp/armino/blob/main/components/trng.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_trng_driver_init(void)[](#_CPPv419bk_trng_driver_initv "永久链接至目标")
:   Init the TRNG driver.

    This API init the resoure common:


    - Init TRNG driver control memory


    **Attention**
    :   1. This API should be called before any other TRNG APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_trng_driver_deinit(void)[](#_CPPv421bk_trng_driver_deinitv "永久链接至目标")
:   Deinit the TRNG driver.

    This API free all resource related to TRNG and disable TRNG.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_trng_start(void)[](#_CPPv413bk_trng_startv "永久链接至目标")
:   Start the TRNG.

    返回
    :   - BK_OK: succeed

        - BK_ERR_TRNG_DRIVER_NOT_INIT: TRNG driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_trng_stop(void)[](#_CPPv412bk_trng_stopv "永久链接至目标")
:   Stop the TRNG.

    返回
    :   - BK_OK: succeed

        - BK_ERR_TRNG_DRIVER_NOT_INIT: TRNG driver not init

        - others: other errors.

int bk_rand(void)[](#_CPPv47bk_randv "永久链接至目标")
:   Get the random number.

    返回
    :   random number between 0 and RAND_MAX


## TRNG API Typedefs[](#trng-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [trng_types.h](https://github.com/bekencorp/armino/blob/main/components/trng_types.h "https://github.com/bekencorp/armino/blob/main/components/trng_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_TRNG_DRIVER_NOT_INIT[](#c.BK_ERR_TRNG_DRIVER_NOT_INIT "永久链接至目标")
:   TRNG driver not init


### Header File[](#id2 "永久链接至标题")


- [hal/hal_trng_types.h](https://github.com/bekencorp/armino/blob/main/components/hal/hal_trng_types.h "https://github.com/bekencorp/armino/blob/main/components/hal/hal_trng_types.h")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint8_t trng_unit_t[](#_CPPv411trng_unit_t "永久链接至目标")
:   trng uint id
