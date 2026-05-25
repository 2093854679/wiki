# sched接口介绍[](#sched "永久链接至标题")

> - 需要包含头文件#include <posix/sched.h>;
> - 定义了系统调度相关的接口

[[English]](../../../../../en/v2.2.1/api-reference/system/posix/sched.html "../../../../../en/v2.2.1/api-reference/system/posix/sched.html")


## Header File[](#header-file "永久链接至标题")


- [sched.h](https://github.com/bekencorp/armino/blob/main/components/sched.h "https://github.com/bekencorp/armino/blob/main/components/sched.h")


## Functions[](#functions "永久链接至标题")

int sched_get_priority_max(int policy)[](#_CPPv422sched_get_priority_maxi "永久链接至目标")
:   Get priority limit (max).

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_max.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_max.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_max.html")

    备注

    policy is ignored.

    返回
    :   the maximum priority value (0-based) system configuration allows.

        e.g. if configMAX_PRIORITIES == 7, this function returns (configMAX_PRIORITIES - 1). configMAX_PRIORITIES is configured in application FreeRTOSConfig.h file.

int sched_get_priority_min(int policy)[](#_CPPv422sched_get_priority_mini "永久链接至目标")
:   Get priority limit (min).

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_min.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_min.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_min.html")

    备注

    policy is ignored.

int sched_yield(void)[](#_CPPv411sched_yieldv "永久链接至目标")
:   Yield the processor.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_yield.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_yield.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_yield.html")

    Return values
    :   **0** – - Upon successful completion


## Structures[](#structures "永久链接至标题")

struct sched_param[](#_CPPv411sched_param "永久链接至目标")
:   Scheduling parameters required for implementation of each supported scheduling policy.

    Public Members

    int sched_priority[](#_CPPv4N11sched_param14sched_priorityE "永久链接至目标")
    :   Process or thread execution scheduling priority.


## Macros[](#macros "永久链接至标题")

SCHED_OTHER[](#c.SCHED_OTHER "永久链接至目标")
:   Another scheduling policy.
