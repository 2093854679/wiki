# signal接口介绍[](#signal "永久链接至标题")

> - 需要包含头文件#include <posix/signal.h>;
> - 定义了系统信号相关的接口

[[English]](../../../../../en/v2.0.1/api-reference/system/posix/signal.html "../../../../../en/v2.0.1/api-reference/system/posix/signal.html")


## Header File[](#header-file "永久链接至标题")


- [signal.h](https://github.com/bekencorp/armino/blob/main/components/signal.h "https://github.com/bekencorp/armino/blob/main/components/signal.h")


## Unions[](#unions "永久链接至标题")

union sigval[](#_CPPv46sigval "永久链接至目标")
:   *#include <signal.h>*

    Signal value.

    Public Members

    int sival_int[](#_CPPv4N6sigval9sival_intE "永久链接至目标")
    :   Integer signal value.

    void *sival_ptr[](#_CPPv4N6sigval9sival_ptrE "永久链接至目标")
    :   Pointer signal value.


## Structures[](#structures "永久链接至标题")

struct sigevent[](#_CPPv48sigevent "永久链接至目标")
:   Signal event structure.

    Public Members

    int sigev_notify[](#_CPPv4N8sigevent12sigev_notifyE "永久链接至目标")
    :   Notification type. A value of SIGEV_SIGNAL is not supported.

    int sigev_signo[](#_CPPv4N8sigevent11sigev_signoE "永久链接至目标")
    :   Signal number. This member is ignored.

    union [sigval](#_CPPv46sigval "sigval") sigev_value[](#_CPPv4N8sigevent11sigev_valueE "永久链接至目标")
    :   Signal value. Only the sival_ptr member is used.

    void (*sigev_notify_function)(union [sigval](#_CPPv46sigval "sigval"))[](#_CPPv4N8sigevent21sigev_notify_functionE "永久链接至目标")
    :   Notification function.

    pthread_attr_t *sigev_notify_attributes[](#_CPPv4N8sigevent23sigev_notify_attributesE "永久链接至目标")
    :   Notification attributes.


## Macros[](#macros "永久链接至标题")

SIGEV_NONE[](#c.SIGEV_NONE "永久链接至目标")
:   No asynchronous notification is delivered when the event of interest occurs.

SIGEV_SIGNAL[](#c.SIGEV_SIGNAL "永久链接至目标")
:   A queued signal, with an application-defined value, is generated when the event of interest occurs. Not supported.

SIGEV_THREAD[](#c.SIGEV_THREAD "永久链接至目标")
:   A notification function is called to perform notification.
