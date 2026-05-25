# utils接口介绍[](#utils "永久链接至标题")

> - 需要包含头文件#include <posix/utils.h>;
> - 定义了posix公用的接口

[[English]](../../../../../en/v2.0.1/api-reference/system/posix/utils.html "../../../../../en/v2.0.1/api-reference/system/posix/utils.html")


## Header File[](#header-file "永久链接至标题")


- [utils.h](https://github.com/bekencorp/armino/blob/main/components/utils.h "https://github.com/bekencorp/armino/blob/main/components/utils.h")


## Functions[](#functions "永久链接至标题")

size_t UTILS_strnlen(const char *const pcString, size_t xMaxLength)[](#_CPPv413UTILS_strnlenPCKc6size_t "永久链接至目标")
:   Calculates the length of pcString, up to xMaxLength.

    参数
    :   - **pcString** – **[in]** The string to find the length of.

        - **xMaxLength** – **[in]** The limit when searching for the end of pcString.

    返回
    :   0 if pcString is NULL; otherwise, the length of pcString or xMaxLength, whichever is smaller.

int UTILS_AbsoluteTimespecToDeltaTicks(const struct [timespec](time.html#_CPPv48timespec "timespec") *const pxAbsoluteTime, const struct [timespec](time.html#_CPPv48timespec "timespec") *const pxCurrentTime, TickType_t *const pxResult)[](#_CPPv434UTILS_AbsoluteTimespecToDeltaTicksPCK8timespecPCK8timespecPC10TickType_t "永久链接至目标")
:   Calculates the number of ticks between now and a given timespec.

    参数
    :   - **pxAbsoluteTime** – **[in]** A time in the future, specified as seconds and nanoseconds since CLOCK_REALTIME’s 0.

        - **pxCurrentTime** – **[in]** current time, specified as seconds and nanoseconds.

        - **pxResult** – **[out]** Where the result of the conversion is stored. The result is rounded up for fractional ticks.

    返回
    :   0 on success. Otherwise, ETIMEDOUT if pxAbsoluteTime is in the past, or EINVAL for invalid parameters.

int UTILS_TimespecToTicks(const struct [timespec](time.html#_CPPv48timespec "timespec") *const pxTimespec, TickType_t *const pxResult)[](#_CPPv421UTILS_TimespecToTicksPCK8timespecPC10TickType_t "永久链接至目标")
:   Converts a struct timespec to FreeRTOS ticks.

    参数
    :   - **pxTimespec** – **[in]** The timespec to convert.

        - **Where** – **[out]** the result of the conversion is stored. The result is rounded up for fractional ticks.

    返回
    :   0 on success. Otherwise, EINVAL for invalid parameters.

void UTILS_NanosecondsToTimespec(int64_t llSource, struct [timespec](time.html#_CPPv48timespec "timespec") *const pxDestination)[](#_CPPv427UTILS_NanosecondsToTimespec7int64_tPC8timespec "永久链接至目标")
:   Converts an integer value to a timespec.

    参数
    :   - **llSource** – **[in]** The value to convert.

        - **pxDestination** – **[out]** Where to store the converted value.

    返回
    :   No return value.

int UTILS_TimespecAdd(const struct [timespec](time.html#_CPPv48timespec "timespec") *const x, const struct [timespec](time.html#_CPPv48timespec "timespec") *const y, struct [timespec](time.html#_CPPv48timespec "timespec") *const pxResult)[](#_CPPv417UTILS_TimespecAddPCK8timespecPCK8timespecPC8timespec "永久链接至目标")
:   Calculates pxResult = x + y.

    参数
    :   - **x** – **[in]** The first argument for addition.

        - **y** – **[in]** The second argument for addition.

        - **pxResult** – **[out]** Where the result of the calculation is stored.

    返回
    :   -1 if any argument was NULL; 1 if result is negative (overflow); otherwise, 0.

int UTILS_TimespecAddNanoseconds(const struct [timespec](time.html#_CPPv48timespec "timespec") *const x, int64_t llNanoseconds, struct [timespec](time.html#_CPPv48timespec "timespec") *const pxResult)[](#_CPPv428UTILS_TimespecAddNanosecondsPCK8timespec7int64_tPC8timespec "永久链接至目标")
:   Calculates pxResult = x + ( struct timespec ) nanosec.

    参数
    :   - **x** – **[in]** The first argument for addition.

        - **llNanoseconds** – **[in]** The second argument for addition.

        - **pxResult** – **[out]** Where the result of the calculation is stored.

    返回
    :   -1 if pxResult or x was NULL; 1 if result is negative; otherwise, 0.

int UTILS_TimespecSubtract(const struct [timespec](time.html#_CPPv48timespec "timespec") *const x, const struct [timespec](time.html#_CPPv48timespec "timespec") *const y, struct [timespec](time.html#_CPPv48timespec "timespec") *const pxResult)[](#_CPPv422UTILS_TimespecSubtractPCK8timespecPCK8timespecPC8timespec "永久链接至目标")
:   Calculates pxResult = x - y. If the result is negative contents of pResult are undefined.

    参数
    :   - **x** – **[in]** The first argument for subtraction.

        - **y** – **[in]** The second argument for subtraction.

        - **pxResult** – **[out]** Where the result of the calculation is stored.

    返回
    :   -1 if any argument was NULL; 1 if result is negative; otherwise, 0.

int UTILS_TimespecCompare(const struct [timespec](time.html#_CPPv48timespec "timespec") *const x, const struct [timespec](time.html#_CPPv48timespec "timespec") *const y)[](#_CPPv421UTILS_TimespecComparePCK8timespecPCK8timespec "永久链接至目标")
:   Compare x == y.

    参数
    :   - **x** – **[in]** The first argument for comparison.

        - **y** – **[in]** The second argument for comparison.

    返回
    :   0 if x == y; 1 if x > y; -1 if x < y or any argument was NULL

bool UTILS_ValidateTimespec(const struct [timespec](time.html#_CPPv48timespec "timespec") *const pxTimespec)[](#_CPPv422UTILS_ValidateTimespecPCK8timespec "永久链接至目标")
:   Checks that a timespec conforms to POSIX.

    A valid timespec must have 0 <= tv_nsec < 1000000000.

    参数
    :   **pxTimespec** – **[in]** The timespec to validate.

    返回
    :   true if the pxTimespec is valid, false otherwise.
