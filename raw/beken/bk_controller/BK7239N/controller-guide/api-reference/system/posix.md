---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/system/posix.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="posix-apis"></a>

# POSIX APIs

<a id="id1"></a>

## POSIX APIs 介绍

> - 目前Armino平台posix接口仅支持FreeRTOS V10.4操作系统，默认关闭;
> - 若打开使用，需要打开CONFIG\_FREERTOS\_POSIX配置开关

备注

- 在使用FreeRTOS的posix功能的时候，在引用posix相关头文件之前，需要先引用FreeRTOS\_POSIX.h头文件；
- 可以在components/bk\_rtos/freertos/posix/freertos\_impl/include/portable/bk/FreeRTOS\_POSIX\_portable.h中自定义相关配置。

<a id="unistd-apis"></a>

## **unistd APIs**

> - #include \<posix/unistd.h\>
> - Defines the APIs related to system sleep

<a id="header-file"></a>

### Header File

- [unistd.h](https://github.com/bekencorp/armino/blob/main/components/unistd.h)

<a id="functions"></a>

### Functions

<a id="_CPPv45sleepj"></a>

<a id="_CPPv35sleepj"></a> <a id="_CPPv25sleepj"></a> <a id="sleep__unsigned"></a> <a id="unistd_8h_1ad4669b3813c3b4a616a738317fdc974f"></a> unsigned sleep(unsigned seconds)
:   Suspend execution for an interval of time.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sleep.html>

    备注

    Return value of a positive number is not yet supported.

    参数
    :   **seconds** – **\[in\]** The number of seconds to suspend execution.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv46usleep10useconds_t"></a>

<a id="_CPPv36usleep10useconds_t"></a> <a id="_CPPv26usleep10useconds_t"></a> <a id="usleep__useconds_t"></a> <a id="unistd_8h_1ac0383719bafa9b5b2aa25fabc586bd1f"></a> int usleep(useconds\_t usec)
:   Suspend execution for microsecond intervals.

    This is a useful, non-POSIX function.

    参数
    :   **usec** – **\[in\]** The number of microseconds to suspend execution.

    Return values
    :   **0** – \- Upon successful completion.

<a id="utils-apis"></a>

## **utils APIs**

> - #include \<posix/utils.h\>
> - Define public interfaces

<a id="id2"></a>

### Header File

- [utils.h](https://github.com/bekencorp/armino/blob/main/components/utils.h)

<a id="id3"></a>

### Functions

<a id="_CPPv413UTILS_strnlenPCKc6size_t"></a>

<a id="_CPPv313UTILS_strnlenPCKc6size_t"></a> <a id="_CPPv213UTILS_strnlenPCKc6size_t"></a> <a id="UTILS_strnlen__cCPC.s"></a> <a id="utils_8h_1ae1e06073e3115214a76205be6149d83a"></a> size\_t UTILS\_strnlen(const char \*const pcString, size\_t xMaxLength)
:   Calculates the length of pcString, up to xMaxLength.

    参数
    :   - **pcString** – **\[in\]** The string to find the length of.
        - **xMaxLength** – **\[in\]** The limit when searching for the end of pcString.

    返回
    :   0 if pcString is NULL; otherwise, the length of pcString or xMaxLength, whichever is smaller.

<a id="_CPPv434UTILS_AbsoluteTimespecToDeltaTicksPCK8timespecPCK8timespecPC10TickType_t"></a>

<a id="_CPPv334UTILS_AbsoluteTimespecToDeltaTicksPCK8timespecPCK8timespecPC10TickType_t"></a> <a id="_CPPv234UTILS_AbsoluteTimespecToDeltaTicksPCK8timespecPCK8timespecPC10TickType_t"></a> <a id="UTILS_AbsoluteTimespecToDeltaTicks__timespecCPC.timespecCPC.TickType_tPC"></a> <a id="utils_8h_1a858c841d9d8d7baed0ea06bb9ac31cb3"></a> int UTILS\_AbsoluteTimespecToDeltaTicks(const struct [timespec](#_CPPv48timespec "timespec") \*const pxAbsoluteTime, const struct [timespec](#_CPPv48timespec "timespec") \*const pxCurrentTime, TickType\_t \*const pxResult)
:   Calculates the number of ticks between now and a given timespec.

    参数
    :   - **pxAbsoluteTime** – **\[in\]** A time in the future, specified as seconds and nanoseconds since CLOCK\_REALTIME’s 0\.
        - **pxCurrentTime** – **\[in\]** current time, specified as seconds and nanoseconds.
        - **pxResult** – **\[out\]** Where the result of the conversion is stored. The result is rounded up for fractional ticks.

    返回
    :   0 on success. Otherwise, ETIMEDOUT if pxAbsoluteTime is in the past, or EINVAL for invalid parameters.

<a id="_CPPv421UTILS_TimespecToTicksPCK8timespecPC10TickType_t"></a>

<a id="_CPPv321UTILS_TimespecToTicksPCK8timespecPC10TickType_t"></a> <a id="_CPPv221UTILS_TimespecToTicksPCK8timespecPC10TickType_t"></a> <a id="UTILS_TimespecToTicks__timespecCPC.TickType_tPC"></a> <a id="utils_8h_1a5375610b0556953de42a89cd38c7ff3f"></a> int UTILS\_TimespecToTicks(const struct [timespec](#_CPPv48timespec "timespec") \*const pxTimespec, TickType\_t \*const pxResult)
:   Converts a struct timespec to FreeRTOS ticks.

    参数
    :   - **pxTimespec** – **\[in\]** The timespec to convert.
        - **Where** – **\[out\]** the result of the conversion is stored. The result is rounded up for fractional ticks.

    返回
    :   0 on success. Otherwise, EINVAL for invalid parameters.

<a id="_CPPv427UTILS_NanosecondsToTimespec7int64_tPC8timespec"></a>

<a id="_CPPv327UTILS_NanosecondsToTimespec7int64_tPC8timespec"></a> <a id="_CPPv227UTILS_NanosecondsToTimespec7int64_tPC8timespec"></a> <a id="UTILS_NanosecondsToTimespec__int64_t.timespecPC"></a> <a id="utils_8h_1a470a49f37255ae6aabb10f7943a116e0"></a> void UTILS\_NanosecondsToTimespec(int64\_t llSource, struct [timespec](#_CPPv48timespec "timespec") \*const pxDestination)
:   Converts an integer value to a timespec.

    参数
    :   - **llSource** – **\[in\]** The value to convert.
        - **pxDestination** – **\[out\]** Where to store the converted value.

    返回
    :   No return value.

<a id="_CPPv417UTILS_TimespecAddPCK8timespecPCK8timespecPC8timespec"></a>

<a id="_CPPv317UTILS_TimespecAddPCK8timespecPCK8timespecPC8timespec"></a> <a id="_CPPv217UTILS_TimespecAddPCK8timespecPCK8timespecPC8timespec"></a> <a id="UTILS_TimespecAdd__timespecCPC.timespecCPC.timespecPC"></a> <a id="utils_8h_1a296316a153cf3234bf48e0b268b29fcb"></a> int UTILS\_TimespecAdd(const struct [timespec](#_CPPv48timespec "timespec") \*const x, const struct [timespec](#_CPPv48timespec "timespec") \*const y, struct [timespec](#_CPPv48timespec "timespec") \*const pxResult)
:   Calculates pxResult \= x \+ y.

    参数
    :   - **x** – **\[in\]** The first argument for addition.
        - **y** – **\[in\]** The second argument for addition.
        - **pxResult** – **\[out\]** Where the result of the calculation is stored.

    返回
    :   -1 if any argument was NULL; 1 if result is negative (overflow); otherwise, 0\.

<a id="_CPPv428UTILS_TimespecAddNanosecondsPCK8timespec7int64_tPC8timespec"></a>

<a id="_CPPv328UTILS_TimespecAddNanosecondsPCK8timespec7int64_tPC8timespec"></a> <a id="_CPPv228UTILS_TimespecAddNanosecondsPCK8timespec7int64_tPC8timespec"></a> <a id="UTILS_TimespecAddNanoseconds__timespecCPC.int64_t.timespecPC"></a> <a id="utils_8h_1a2183fc6650a802981f72c8765d1e231e"></a> int UTILS\_TimespecAddNanoseconds(const struct [timespec](#_CPPv48timespec "timespec") \*const x, int64\_t llNanoseconds, struct [timespec](#_CPPv48timespec "timespec") \*const pxResult)
:   Calculates pxResult \= x \+ ( struct timespec ) nanosec.

    参数
    :   - **x** – **\[in\]** The first argument for addition.
        - **llNanoseconds** – **\[in\]** The second argument for addition.
        - **pxResult** – **\[out\]** Where the result of the calculation is stored.

    返回
    :   -1 if pxResult or x was NULL; 1 if result is negative; otherwise, 0\.

<a id="_CPPv422UTILS_TimespecSubtractPCK8timespecPCK8timespecPC8timespec"></a>

<a id="_CPPv322UTILS_TimespecSubtractPCK8timespecPCK8timespecPC8timespec"></a> <a id="_CPPv222UTILS_TimespecSubtractPCK8timespecPCK8timespecPC8timespec"></a> <a id="UTILS_TimespecSubtract__timespecCPC.timespecCPC.timespecPC"></a> <a id="utils_8h_1a3d3fce8c0d895a6006d7cb06a26f2b84"></a> int UTILS\_TimespecSubtract(const struct [timespec](#_CPPv48timespec "timespec") \*const x, const struct [timespec](#_CPPv48timespec "timespec") \*const y, struct [timespec](#_CPPv48timespec "timespec") \*const pxResult)
:   Calculates pxResult \= x \- y. If the result is negative contents of pResult are undefined.

    参数
    :   - **x** – **\[in\]** The first argument for subtraction.
        - **y** – **\[in\]** The second argument for subtraction.
        - **pxResult** – **\[out\]** Where the result of the calculation is stored.

    返回
    :   -1 if any argument was NULL; 1 if result is negative; otherwise, 0\.

<a id="_CPPv421UTILS_TimespecComparePCK8timespecPCK8timespec"></a>

<a id="_CPPv321UTILS_TimespecComparePCK8timespecPCK8timespec"></a> <a id="_CPPv221UTILS_TimespecComparePCK8timespecPCK8timespec"></a> <a id="UTILS_TimespecCompare__timespecCPC.timespecCPC"></a> <a id="utils_8h_1aa91f0c25033f0a2abed4d7ba63fddbf8"></a> int UTILS\_TimespecCompare(const struct [timespec](#_CPPv48timespec "timespec") \*const x, const struct [timespec](#_CPPv48timespec "timespec") \*const y)
:   Compare x \=\= y.

    参数
    :   - **x** – **\[in\]** The first argument for comparison.
        - **y** – **\[in\]** The second argument for comparison.

    返回
    :   0 if x \=\= y; 1 if x \> y; -1 if x \< y or any argument was NULL

<a id="_CPPv422UTILS_ValidateTimespecPCK8timespec"></a>

<a id="_CPPv322UTILS_ValidateTimespecPCK8timespec"></a> <a id="_CPPv222UTILS_ValidateTimespecPCK8timespec"></a> <a id="UTILS_ValidateTimespec__timespecCPC"></a> <a id="utils_8h_1a4ad9c68fd0045c8e4bbdb45e6810232e"></a> bool UTILS\_ValidateTimespec(const struct [timespec](#_CPPv48timespec "timespec") \*const pxTimespec)
:   Checks that a timespec conforms to POSIX.

    A valid timespec must have 0 \<\= tv\_nsec \< 1000000000.

    参数
    :   **pxTimespec** – **\[in\]** The timespec to validate.

    返回
    :   true if the pxTimespec is valid, false otherwise.

<a id="errno-apis"></a>

## **errno APIs**

> - Header files need to be include (#include \<posix/errno.h\>)
> - Define the meaning of the returned error value

<a id="id4"></a>

### Header File

- [errno.h](https://github.com/bekencorp/armino/blob/main/components/errno.h)

<a id="macros"></a>

### Macros

<a id="c.EPERM"></a>

<a id="errno_8h_1add669d31505a077f769cff8e66c780b3"></a> EPERM
:   Operation not permitted.

<a id="c.ENOENT"></a>

<a id="errno_8h_1a03e689f378f643d16ea7537918528a48"></a> ENOENT
:   No such file or directory.

<a id="c.EBADF"></a>

<a id="errno_8h_1ac54507d66b43ad12f9356257323c0018"></a> EBADF
:   Bad file descriptor.

<a id="c.EAGAIN"></a>

<a id="errno_8h_1af0fac1cea1165b4debec7f686edf3313"></a> EAGAIN
:   Resource unavailable, try again.

<a id="c.ENOMEM"></a>

<a id="errno_8h_1a6a05c923dad0c1208043e9c20a58c8e5"></a> ENOMEM
:   Not enough space.

<a id="c.EEXIST"></a>

<a id="errno_8h_1a0a3bef9e5c47e42917692b5dae3b5498"></a> EEXIST
:   File exists.

<a id="c.EBUSY"></a>

<a id="errno_8h_1a8368025077a0385849d6817b2007c095"></a> EBUSY
:   Device or resource busy.

<a id="c.EINVAL"></a>

<a id="errno_8h_1a2d1678d5a7cc8ce499643f3b8957def4"></a> EINVAL
:   Invalid argument.

<a id="c.ENOSPC"></a>

<a id="errno_8h_1a088abe8bad2df798edad3053d719b937"></a> ENOSPC
:   No space left on device.

<a id="c.ERANGE"></a>

<a id="errno_8h_1aa1591a4f3a86360108de5b9ba34980ca"></a> ERANGE
:   Result too large.

<a id="c.ENAMETOOLONG"></a>

<a id="errno_8h_1a41d5ab3a8a05f9c5eab536c9cfba305b"></a> ENAMETOOLONG
:   File name too long.

<a id="c.EDEADLK"></a>

<a id="errno_8h_1a55cc70ce0ba661298f3c412095dfeeb6"></a> EDEADLK
:   Resource deadlock would occur.

<a id="c.EOVERFLOW"></a>

<a id="errno_8h_1a888552a5e3c78b5883904cf5d55244ab"></a> EOVERFLOW
:   Value too large to be stored in data type.

<a id="c.ENOSYS"></a>

<a id="errno_8h_1a43785b9969e0bd1af532dbde06c5540b"></a> ENOSYS
:   Function not supported.

<a id="c.EMSGSIZE"></a>

<a id="errno_8h_1ae37becfaa095a9df5c5c788bce5aa06f"></a> EMSGSIZE
:   Message too long.

<a id="c.ENOTSUP"></a>

<a id="errno_8h_1a91457bbf35f0f1085619a99423bb1f33"></a> ENOTSUP
:   Operation not supported.

<a id="c.ETIMEDOUT"></a>

<a id="errno_8h_1a597718e59a8fc9c4d4ab63f5a34e28b1"></a> ETIMEDOUT
:   Connection timed out.

<a id="fcntl-apis"></a>

## **fcntl APIs**

> - #include \<posix/fcntl.h\>;
> - Defines the macro definition related to fcntl

<a id="id5"></a>

### Header File

- [fcntl.h](https://github.com/bekencorp/armino/blob/main/components/fcntl.h)

<a id="id6"></a>

### Macros

<a id="c.O_CLOEXEC"></a>

<a id="fcntl_8h_1ad6d8fbe4e494b4dbe051612572d3f757"></a> O\_CLOEXEC
:   Close the file descriptor upon exec().

<a id="c.O_CREAT"></a>

<a id="fcntl_8h_1a1cf6b1de1fffedaa1d26b189e9a8d2cc"></a> O\_CREAT
:   Create file if it does not exist.

<a id="c.O_DIRECTORY"></a>

<a id="fcntl_8h_1a6afd3dd2f570069804b40e6aa24fc966"></a> O\_DIRECTORY
:   Fail if file is a non-directory file.

<a id="c.O_EXCL"></a>

<a id="fcntl_8h_1a9f5acfe79fafe14b6694447bd0e9f10b"></a> O\_EXCL
:   Exclusive use flag.

<a id="c.O_NOCTTY"></a>

<a id="fcntl_8h_1a2e375ab32c7ef4581b026be28e4cc116"></a> O\_NOCTTY
:   Do not assign controlling terminal.

<a id="c.O_NOFOLLOW"></a>

<a id="fcntl_8h_1a82d4d551b214905742c9e045185d352a"></a> O\_NOFOLLOW
:   Do not follow symbolic links.

<a id="c.O_TRUNC"></a>

<a id="fcntl_8h_1ad1d67e453fb3031f40f8cd3403773813"></a> O\_TRUNC
:   Truncate flag.

<a id="c.O_TTY_INIT"></a>

<a id="fcntl_8h_1a0ee7b090d0fd09015039f6325118400f"></a> O\_TTY\_INIT
:   termios structure provides conforming behavior.

<a id="c.O_APPEND"></a>

<a id="fcntl_8h_1ae036f789407d21f07b211552d67b3214"></a> O\_APPEND
:   Set append mode.

<a id="c.O_DSYNC"></a>

<a id="fcntl_8h_1af63e33218e573b9461b5f17d0ea79f2a"></a> O\_DSYNC
:   Write according to synchronized I/O data integrity completion.

<a id="c.O_NONBLOCK"></a>

<a id="fcntl_8h_1a39d33ce33804efd4d52606d59071c6d8"></a> O\_NONBLOCK
:   Non-blocking mode.

<a id="c.O_RSYNC"></a>

<a id="fcntl_8h_1ac9cf617d7c8fba45a5062f1f7322e6f8"></a> O\_RSYNC
:   Synchronized read I/O operations.

<a id="c.O_SYNC"></a>

<a id="fcntl_8h_1aae85139bfa94236d126bb1e3b772998f"></a> O\_SYNC
:   Write according to synchronized I/O file integrity completion.

<a id="c.O_ACCMODE"></a>

<a id="fcntl_8h_1a4dc4d45e07d2abc899bcaf04b2846a87"></a> O\_ACCMODE

<a id="c.O_EXEC"></a>

<a id="fcntl_8h_1a459542206659fbe295eb4183f8b8f06c"></a> O\_EXEC
:   Open for execute only (non-directory files).

<a id="c.O_RDONLY"></a>

<a id="fcntl_8h_1a7a68c9ffaac7dbcd652225dd7c06a54b"></a> O\_RDONLY
:   Open for reading only.

<a id="c.O_RDWR"></a>

<a id="fcntl_8h_1abb0586253488ee61072b73557eeb873b"></a> O\_RDWR
:   Open for reading and writing.

<a id="c.O_SEARCH"></a>

<a id="fcntl_8h_1ac7984b2eaa7166aea31f0c4f6c91fb2d"></a> O\_SEARCH
:   Open directory for search only.

<a id="c.O_WRONLY"></a>

<a id="fcntl_8h_1a11b644a8526139c4cc1850dac1271ced"></a> O\_WRONLY
:   Open for writing only.

<a id="signal-apis"></a>

## **signal APIs**

> - #include \<posix/signal.h\>;
> - Defines the signal related APIs

<a id="id7"></a>

### Header File

- [signal.h](https://github.com/bekencorp/armino/blob/main/components/signal.h)

<a id="unions"></a>

### Unions

<a id="_CPPv46sigval"></a>

<a id="_CPPv36sigval"></a> <a id="_CPPv26sigval"></a> <a id="unionsigval"></a> union sigval
:   *#include \<signal.h\>*

    Signal value.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N6sigval9sival_intE"></a>

    <a id="_CPPv3N6sigval9sival_intE"></a> <a id="_CPPv2N6sigval9sival_intE"></a> <a id="sigval::sival_int__i"></a> <a id="unionsigval_1a560393252ee7edc37df44bf1c11bdbdd"></a> int sival\_int
    :   Integer signal value.

    <a id="_CPPv4N6sigval9sival_ptrE"></a>

    <a id="_CPPv3N6sigval9sival_ptrE"></a> <a id="_CPPv2N6sigval9sival_ptrE"></a> <a id="sigval::sival_ptr__voidP"></a> <a id="unionsigval_1a4668f1bd7463de7b70bd0022207e26ac"></a> void \*sival\_ptr
    :   Pointer signal value.

<a id="structures"></a>

### Structures

<a id="_CPPv48sigevent"></a>

<a id="_CPPv38sigevent"></a> <a id="_CPPv28sigevent"></a> <a id="sigevent"></a> <a id="structsigevent"></a> struct sigevent
:   Signal event structure.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N8sigevent12sigev_notifyE"></a>

    <a id="_CPPv3N8sigevent12sigev_notifyE"></a> <a id="_CPPv2N8sigevent12sigev_notifyE"></a> <a id="sigevent::sigev_notify__i"></a> <a id="structsigevent_1aae9a19d879c38e0c4e8a9bf738c5081e"></a> int sigev\_notify
    :   Notification type. A value of SIGEV\_SIGNAL is not supported.

    <a id="_CPPv4N8sigevent11sigev_signoE"></a>

    <a id="_CPPv3N8sigevent11sigev_signoE"></a> <a id="_CPPv2N8sigevent11sigev_signoE"></a> <a id="sigevent::sigev_signo__i"></a> <a id="structsigevent_1a5c645ec1d12bb46efc3f4097c52b665d"></a> int sigev\_signo
    :   Signal number. This member is ignored.

    <a id="_CPPv4N8sigevent11sigev_valueE"></a>

    <a id="_CPPv3N8sigevent11sigev_valueE"></a> <a id="_CPPv2N8sigevent11sigev_valueE"></a> <a id="sigevent::sigev_value__sigval"></a> <a id="structsigevent_1a757af1e34b87e3f66bbc08c514017a2c"></a> union [sigval](#_CPPv46sigval "sigval") sigev\_value
    :   Signal value. Only the sival\_ptr member is used.

    <a id="_CPPv4N8sigevent21sigev_notify_functionE"></a>

    <a id="_CPPv3N8sigevent21sigev_notify_functionE"></a> <a id="_CPPv2N8sigevent21sigev_notify_functionE"></a> <a id="structsigevent_1ae47aee413b2a2fb09fd7601cb132d03b"></a> void (\*sigev\_notify\_function)(union [sigval](#_CPPv46sigval "sigval"))
    :   Notification function.

    <a id="_CPPv4N8sigevent23sigev_notify_attributesE"></a>

    <a id="_CPPv3N8sigevent23sigev_notify_attributesE"></a> <a id="_CPPv2N8sigevent23sigev_notify_attributesE"></a> <a id="sigevent::sigev_notify_attributes__pthread_attr_tP"></a> <a id="structsigevent_1a5a687d2092b237d76eb08e2d46a5115f"></a> pthread\_attr\_t \*sigev\_notify\_attributes
    :   Notification attributes.

<a id="id8"></a>

### Macros

<a id="c.SIGEV_NONE"></a>

<a id="signal_8h_1aced9a66610d9d61756999ce4f103740e"></a> SIGEV\_NONE
:   No asynchronous notification is delivered when the event of interest occurs.

<a id="c.SIGEV_SIGNAL"></a>

<a id="signal_8h_1a06d5881eeb84e6ac35f5b801c380dbb6"></a> SIGEV\_SIGNAL
:   A queued signal, with an application-defined value, is generated when the event of interest occurs. Not supported.

<a id="c.SIGEV_THREAD"></a>

<a id="signal_8h_1a29ccb6a17fa90a1357b478f62af7fca0"></a> SIGEV\_THREAD
:   A notification function is called to perform notification.

<a id="mqueue-apis"></a>

## **mqueue APIs**

> - #include \<posix/mqueue.h\>
> - Define interfaces related to system message queues

<a id="id9"></a>

### Header File

- [mqueue.h](https://github.com/bekencorp/armino/blob/main/components/mqueue.h)

<a id="id10"></a>

### Functions

<a id="_CPPv48mq_close5mqd_t"></a>

<a id="_CPPv38mq_close5mqd_t"></a> <a id="_CPPv28mq_close5mqd_t"></a> <a id="mq_close__mqd_t"></a> <a id="mqueue_8h_1a3fbd3906296be63451c64d69be2bc371"></a> int mq\_close([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes)
:   Close a message queue.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_close.html>

    @sideeffect Possible errno values

    EBADF \- The mqdes argument is not a valid message queue descriptor.

    Return values
    :   - **0** – \- Upon successful completion
        - **-1** – \- A error occurred. errno is also set.

<a id="_CPPv410mq_getattr5mqd_tP7mq_attr"></a>

<a id="_CPPv310mq_getattr5mqd_tP7mq_attr"></a> <a id="_CPPv210mq_getattr5mqd_tP7mq_attr"></a> <a id="mq_getattr__mqd_t.mq_attrP"></a> <a id="mqueue_8h_1a5a55ce03d8466a53a36601aaca9ee328"></a> int mq\_getattr([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes, struct [mq\_attr](#_CPPv47mq_attr "mq_attr") \*mqstat)
:   Get message queue attributes.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_getattr.html>

    @sideeffect Possible errno values

    DBADF \- The mqdes argument is not a valid message queue descriptor.

    Return values
    :   - **0** – \- Upon successful completion
        - **-1** – \- A error occurred. errno is also set.

<a id="_CPPv47mq_openPKci6mode_tP7mq_attr"></a>

<a id="_CPPv37mq_openPKci6mode_tP7mq_attr"></a> <a id="_CPPv27mq_openPKci6mode_tP7mq_attr"></a> <a id="mq_open__cCP.i.mode_t.mq_attrP"></a> <a id="mqueue_8h_1ade83e7ff8d3ed30d8641355377373638"></a> [mqd\_t](#_CPPv45mqd_t "mqd_t") mq\_open(const char \*name, int oflag, mode\_t mode, struct [mq\_attr](#_CPPv47mq_attr "mq_attr") \*attr)
:   Open a message queue.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_open.html>

    @sideeffect Possible errno values

    EINVAL \- name argument is invalid (not following name pattern), OR if O\_CREAT is specified in oflag with attr argument not NULL and either mq\_maxmsg or mq\_msgsize is equal to or less than zero, OR either O\_CREAT or O\_EXCL is not set and a queue with the same name is unlinked but pending to be removed.

    EEXIST \- O\_CREAT and O\_EXCL are set and the named message queue already exists.

    ENOSPC \- There is insufficient space for the creation of the new message queue.

    ENOENT \- O\_CREAT is not set and the named message queue does not exist.

    备注

    Supported name pattern: leading \<slash\> character in name is always required; the maximum length (excluding null-terminator) of the name argument can be NAME\_MAX. The default value of NAME\_MAX in FreeRTOS\_POSIX\_portable\_default.h is 64, which can be overwritten by user.

    备注

    mode argument is not supported.

    备注

    Supported oflags: O\_RDWR, O\_CREAT, O\_EXCL, and O\_NONBLOCK.

    Return values
    :   - **Message** – queue descriptor \&#8212; Upon successful completion
        - **(mqd\_t)** – \- 1 \&#8212; An error occurred. errno is also set.

<a id="_CPPv410mq_receive5mqd_tPc6size_tPj"></a>

<a id="_CPPv310mq_receive5mqd_tPc6size_tPj"></a> <a id="_CPPv210mq_receive5mqd_tPc6size_tPj"></a> <a id="mq_receive__mqd_t.cP.s.unsigned-iP"></a> <a id="mqueue_8h_1ab89c825740fe27d3821ccbe32bd68dfa"></a> ssize\_t mq\_receive([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes, char \*msg\_ptr, size\_t msg\_len, unsigned int \*msg\_prio)
:   Receive a message from a message queue.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_receive.html>

    @sideeffect Possible errno values

    EBADF \- The mqdes argument is not a valid message queue descriptor open for reading.

    EMSGSIZE \- The specified message buffer size, msg\_len, is less than the message size attribute of the message queue.

    ETIMEDOUT \- The O\_NONBLOCK flag was not set when the message queue was opened, but no message arrived on the queue before the specified timeout expired.

    EAGAIN \- O\_NONBLOCK was set in the message description associated with mqdes, and the specified message queue is empty.

    备注

    msg\_prio argument is not supported. Messages are not checked for corruption.

    Return values
    :   - **The** – length of the selected message in bytes \- Upon successful completion. The message is removed from the queue
        - **-1** – \- An error occurred. errno is also set.

<a id="_CPPv47mq_send5mqd_tPKc6size_tj"></a>

<a id="_CPPv37mq_send5mqd_tPKc6size_tj"></a> <a id="_CPPv27mq_send5mqd_tPKc6size_tj"></a> <a id="mq_send__mqd_t.cCP.s.unsigned"></a> <a id="mqueue_8h_1a753177f77f6eec2a80b57e8a68b36bed"></a> int mq\_send([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes, const char \*msg\_ptr, size\_t msg\_len, unsigned msg\_prio)
:   Send a message to a message queue.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_send.html>

    @sideeffect Possible errno values

    EBADF \- The mqdes argument is not a valid message queue descriptor open for writing.

    EMSGSIZE \- The specified message length, msg\_len, exceeds the message size attribute of the message queue, OR insufficient memory for the message to be sent.

    ETIMEDOUT \- The O\_NONBLOCK flag was not set when the message queue was opened, but the timeout expired before the message could be added to the queue.

    EAGAIN \- The O\_NONBLOCK flag is set in the message queue description associated with mqdes, and the specified message queue is full.

    备注

    msg\_prio argument is not supported.

    Return values
    :   - **0** – \- Upon successful completion.
        - **-1** – \- An error occurred. errno is also set.

<a id="_CPPv415mq_timedreceive5mqd_tPc6size_tPjPK8timespec"></a>

<a id="_CPPv315mq_timedreceive5mqd_tPc6size_tPjPK8timespec"></a> <a id="_CPPv215mq_timedreceive5mqd_tPc6size_tPjPK8timespec"></a> <a id="mq_timedreceive__mqd_t.cP.s.unsignedP.timespecCP"></a> <a id="mqueue_8h_1a8749e8f6d2efe37457e955a21ed98691"></a> ssize\_t mq\_timedreceive([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes, char \*msg\_ptr, size\_t msg\_len, unsigned \*msg\_prio, const struct [timespec](#_CPPv48timespec "timespec") \*abstime)
:   Receive a message from a message queue with timeout.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_timedreceive.html>

    @sideeffect Possible errno values

    EBADF \- The mqdes argument is not a valid message queue descriptor open for reading.

    EMSGSIZE \- The specified message buffer size, msg\_len, is less than the message size attribute of the message queue.

    EINVAL \- The process or thread would have blocked, and the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

    ETIMEDOUT \- The O\_NONBLOCK flag was not set when the message queue was opened, but no message arrived on the queue before the specified timeout expired.

    EAGAIN \- O\_NONBLOCK was set in the message description associated with mqdes, and the specified message queue is empty.

    备注

    msg\_prio argument is not supported. Messages are not checked for corruption.

    Return values
    :   - **The** – length of the selected message in bytes \- Upon successful completion. The message is removed from the queue
        - **-1** – \- An error occurred. errno is also set.

<a id="_CPPv412mq_timedsend5mqd_tPKc6size_tjPK8timespec"></a>

<a id="_CPPv312mq_timedsend5mqd_tPKc6size_tjPK8timespec"></a> <a id="_CPPv212mq_timedsend5mqd_tPKc6size_tjPK8timespec"></a> <a id="mq_timedsend__mqd_t.cCP.s.unsigned.timespecCP"></a> <a id="mqueue_8h_1a021882ffe3cfd53c10d95d314b29ab2d"></a> int mq\_timedsend([mqd\_t](#_CPPv45mqd_t "mqd_t") mqdes, const char \*msg\_ptr, size\_t msg\_len, unsigned msg\_prio, const struct [timespec](#_CPPv48timespec "timespec") \*abstime)
:   Send a message to a message queue with timeout.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_timedsend.html>

    @sideeffect Possible errno values

    EBADF \- The mqdes argument is not a valid message queue descriptor open for writing.

    EMSGSIZE \- The specified message length, msg\_len, exceeds the message size attribute of the message queue, OR insufficient memory for the message to be sent.

    EINVAL \- The process or thread would have blocked, and the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

    ETIMEDOUT \- The O\_NONBLOCK flag was not set when the message queue was opened, but the timeout expired before the message could be added to the queue.

    EAGAIN \- The O\_NONBLOCK flag is set in the message queue description associated with mqdes, and the specified message queue is full.

    备注

    msg\_prio argument is not supported.

    Return values
    :   - **0** – \- Upon successful completion.
        - **-1** – \- An error occurred. errno is also set.

<a id="_CPPv49mq_unlinkPKc"></a>

<a id="_CPPv39mq_unlinkPKc"></a> <a id="_CPPv29mq_unlinkPKc"></a> <a id="mq_unlink__cCP"></a> <a id="mqueue_8h_1accd8c5ee36e60d990963e1d544ef4140"></a> int mq\_unlink(const char \*name)
:   Remove a message queue.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_unlink.html>

    @sideeffect Possible errno values

    EINVAL \- name argument is invalid. Refer to requirements on name argument in

    [mq\_open()](#mqueue_8h_1ade83e7ff8d3ed30d8641355377373638)

    .

    ENOENT \- The named message queue does not exist.

    Return values
    :   - **0** – \- Upon successful completion.
        - **-1** – \- An error occurred. errno is also set.

<a id="id11"></a>

### Structures

<a id="_CPPv47mq_attr"></a>

<a id="_CPPv37mq_attr"></a> <a id="_CPPv27mq_attr"></a> <a id="mq_attr"></a> <a id="structmq__attr"></a> struct mq\_attr
:   Message queue attributes.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N7mq_attr8mq_flagsE"></a>

    <a id="_CPPv3N7mq_attr8mq_flagsE"></a> <a id="_CPPv2N7mq_attr8mq_flagsE"></a> <a id="mq_attr::mq_flags__l"></a> <a id="structmq__attr_1a19c05fa88c6d1126120d800647ddb0dd"></a> long mq\_flags
    :   Message queue flags.

    <a id="_CPPv4N7mq_attr9mq_maxmsgE"></a>

    <a id="_CPPv3N7mq_attr9mq_maxmsgE"></a> <a id="_CPPv2N7mq_attr9mq_maxmsgE"></a> <a id="mq_attr::mq_maxmsg__l"></a> <a id="structmq__attr_1aa535e1fa6c07c1d189e720ba15f9af08"></a> long mq\_maxmsg
    :   Maximum number of messages.

    <a id="_CPPv4N7mq_attr10mq_msgsizeE"></a>

    <a id="_CPPv3N7mq_attr10mq_msgsizeE"></a> <a id="_CPPv2N7mq_attr10mq_msgsizeE"></a> <a id="mq_attr::mq_msgsize__l"></a> <a id="structmq__attr_1ae975d1d907081c1e53b079c981c32209"></a> long mq\_msgsize
    :   Maximum message size.

    <a id="_CPPv4N7mq_attr10mq_curmsgsE"></a>

    <a id="_CPPv3N7mq_attr10mq_curmsgsE"></a> <a id="_CPPv2N7mq_attr10mq_curmsgsE"></a> <a id="mq_attr::mq_curmsgs__l"></a> <a id="structmq__attr_1a08cfd508cef817ba351c1af8d9af50f5"></a> long mq\_curmsgs
    :   Number of messages currently queued.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv45mqd_t"></a>

<a id="_CPPv35mqd_t"></a> <a id="_CPPv25mqd_t"></a> <a id="mqd_t"></a> <a id="mqueue_8h_1aa03ac56b19aba70879b7e2934da6a507"></a> typedef void \*mqd\_t
:   Message queue descriptor.

<a id="pthread-apis"></a>

## **pthread APIs**

> - #include \<posix/pthread.h\>;
> - APIs related to system tasks, including creation, destruction, etc

<a id="id12"></a>

### Header File

- [pthread.h](https://github.com/bekencorp/armino/blob/main/components/pthread.h)

<a id="id13"></a>

### Functions

<a id="_CPPv420pthread_attr_destroyP14pthread_attr_t"></a>

<a id="_CPPv320pthread_attr_destroyP14pthread_attr_t"></a> <a id="_CPPv220pthread_attr_destroyP14pthread_attr_t"></a> <a id="pthread_attr_destroy__pthread_attr_tP"></a> <a id="pthread_8h_1a4bcdbf47c17c7dcc51e9f05f5cb56d81"></a> int pthread\_attr\_destroy(pthread\_attr\_t \*attr)
:   Destroy the thread attributes object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_destroy.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv427pthread_attr_getdetachstatePK14pthread_attr_tPi"></a>

<a id="_CPPv327pthread_attr_getdetachstatePK14pthread_attr_tPi"></a> <a id="_CPPv227pthread_attr_getdetachstatePK14pthread_attr_tPi"></a> <a id="pthread_attr_getdetachstate__pthread_attr_tCP.iP"></a> <a id="pthread_8h_1a391c34da42e68ddd24f5ee0c070d5c4f"></a> int pthread\_attr\_getdetachstate(const pthread\_attr\_t \*attr, int \*detachstate)
:   Get detachstate attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getdetachstate.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv426pthread_attr_getschedparamPK14pthread_attr_tP11sched_param"></a>

<a id="_CPPv326pthread_attr_getschedparamPK14pthread_attr_tP11sched_param"></a> <a id="_CPPv226pthread_attr_getschedparamPK14pthread_attr_tP11sched_param"></a> <a id="pthread_attr_getschedparam__pthread_attr_tCP.sched_paramP"></a> <a id="pthread_8h_1afd3d272d702481044f8a8cd253fd9b47"></a> int pthread\_attr\_getschedparam(const pthread\_attr\_t \*attr, struct [sched\_param](#_CPPv411sched_param "sched_param") \*param)
:   Get schedparam attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv425pthread_attr_getstacksizePK14pthread_attr_tP6size_t"></a>

<a id="_CPPv325pthread_attr_getstacksizePK14pthread_attr_tP6size_t"></a> <a id="_CPPv225pthread_attr_getstacksizePK14pthread_attr_tP6size_t"></a> <a id="pthread_attr_getstacksize__pthread_attr_tCP.sP"></a> <a id="pthread_8h_1ae23600d4670359ab12bfba20db2c9a37"></a> int pthread\_attr\_getstacksize(const pthread\_attr\_t \*attr, size\_t \*stacksize)
:   Get stacksize attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv417pthread_attr_initP14pthread_attr_t"></a>

<a id="_CPPv317pthread_attr_initP14pthread_attr_t"></a> <a id="_CPPv217pthread_attr_initP14pthread_attr_t"></a> <a id="pthread_attr_init__pthread_attr_tP"></a> <a id="pthread_8h_1a0b85ebb1e3aac081a4c0a5e85ae3cbe9"></a> int pthread\_attr\_init(pthread\_attr\_t \*attr)
:   Initialize the thread attributes object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_init.html>

    备注

    Currently, only stack size, [sched\_param](#structsched__param), and detach state attributes are supported. Also see pthread\_attr\_get\*() and pthread\_attr\_set\*().

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv427pthread_attr_setdetachstateP14pthread_attr_ti"></a>

<a id="_CPPv327pthread_attr_setdetachstateP14pthread_attr_ti"></a> <a id="_CPPv227pthread_attr_setdetachstateP14pthread_attr_ti"></a> <a id="pthread_attr_setdetachstate__pthread_attr_tP.i"></a> <a id="pthread_8h_1ae6ee78c307d8467b34a9b0c330993a54"></a> int pthread\_attr\_setdetachstate(pthread\_attr\_t \*attr, int detachstate)
:   Set detachstate attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setdetachstate.html>

    Return values
    :   - **0** – \- Upon successful completion
        - **EINVAL** – \- The value of detachstate is not valid. Currently, supported detach states are \&#8212; PTHREAD\_CREATE\_DETACHED and PTHREAD\_CREATE\_JOINABLE.

<a id="_CPPv426pthread_attr_setschedparamP14pthread_attr_tPK11sched_param"></a>

<a id="_CPPv326pthread_attr_setschedparamP14pthread_attr_tPK11sched_param"></a> <a id="_CPPv226pthread_attr_setschedparamP14pthread_attr_tPK11sched_param"></a> <a id="pthread_attr_setschedparam__pthread_attr_tP.sched_paramCP"></a> <a id="pthread_8h_1a579e6529f0ce482312a5e77ac61cb4d5"></a> int pthread\_attr\_setschedparam(pthread\_attr\_t \*attr, const struct [sched\_param](#_CPPv411sched_param "sched_param") \*param)
:   Set schedparam attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedparam.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The value of param is not valid.
        - **ENOTSUP** – \- An attempt was made to set the attribute to an unsupported value.

<a id="_CPPv427pthread_attr_setschedpolicyP14pthread_attr_ti"></a>

<a id="_CPPv327pthread_attr_setschedpolicyP14pthread_attr_ti"></a> <a id="_CPPv227pthread_attr_setschedpolicyP14pthread_attr_ti"></a> <a id="pthread_attr_setschedpolicy__pthread_attr_tP.i"></a> <a id="pthread_8h_1a79b4c9e71486a87ef3014f1c660b33eb"></a> int pthread\_attr\_setschedpolicy(pthread\_attr\_t \*attr, int policy)
:   Set the schedpolicy attribute.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedpolicy.html>

    警告

    This function is a stub and always returns 0\.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv425pthread_attr_setstacksizeP14pthread_attr_t6size_t"></a>

<a id="_CPPv325pthread_attr_setstacksizeP14pthread_attr_t6size_t"></a> <a id="_CPPv225pthread_attr_setstacksizeP14pthread_attr_t6size_t"></a> <a id="pthread_attr_setstacksize__pthread_attr_tP.s"></a> <a id="pthread_8h_1a812a9a455ae2ef2bb0dca4fff201a281"></a> int pthread\_attr\_setstacksize(pthread\_attr\_t \*attr, size\_t stacksize)
:   Set stacksize attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setstacksize.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The value of stacksize is less than {PTHREAD\_STACK\_MIN}.

<a id="_CPPv423pthread_barrier_destroyP17pthread_barrier_t"></a>

<a id="_CPPv323pthread_barrier_destroyP17pthread_barrier_t"></a> <a id="_CPPv223pthread_barrier_destroyP17pthread_barrier_t"></a> <a id="pthread_barrier_destroy__pthread_barrier_tP"></a> <a id="pthread_8h_1ae8ef9b4e2d7feaa1a28159991e7433ac"></a> int pthread\_barrier\_destroy(pthread\_barrier\_t \*barrier)
:   Destroy a barrier object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html>

    备注

    This function does not validate whether there is any thread blocking on the barrier before destroying.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv420pthread_barrier_initP17pthread_barrier_tPK21pthread_barrierattr_tj"></a>

<a id="_CPPv320pthread_barrier_initP17pthread_barrier_tPK21pthread_barrierattr_tj"></a> <a id="_CPPv220pthread_barrier_initP17pthread_barrier_tPK21pthread_barrierattr_tj"></a> <a id="pthread_barrier_init__pthread_barrier_tP.pthread_barrierattr_tCP.unsigned"></a> <a id="pthread_8h_1ae3328293a058e9c0641dbdbdfff3761e"></a> int pthread\_barrier\_init(pthread\_barrier\_t \*barrier, const pthread\_barrierattr\_t \*attr, unsigned count)
:   Initialize a barrier object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html>

    备注

    attr is ignored.

    备注

    [pthread\_barrier\_init()](#pthread_8h_1ae3328293a058e9c0641dbdbdfff3761e) is implemented with FreeRTOS event group. To ensure count fits in event group, count may be at most 8 when configUSE\_16\_BIT\_TICKS is 1; it may be at most 24 otherwise. configUSE\_16\_BIT\_TICKS is configured in application FreeRTOSConfig.h file, which defines how many bits tick count type has. See further details and limitation about event group and configUSE\_16\_BIT\_TICKS in FreeRTOS site.

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The value specified by count is equal to zero.
        - **ENOMEM** – \- count cannot fit into FreeRTOS event group type OR insufficient memory exists to initialize the barrier.

<a id="_CPPv420pthread_barrier_waitP17pthread_barrier_t"></a>

<a id="_CPPv320pthread_barrier_waitP17pthread_barrier_t"></a> <a id="_CPPv220pthread_barrier_waitP17pthread_barrier_t"></a> <a id="pthread_barrier_wait__pthread_barrier_tP"></a> <a id="pthread_8h_1a85f92053b4d12aa94927b364b5b757d9"></a> int pthread\_barrier\_wait(pthread\_barrier\_t \*barrier)
:   Synchronize at a barrier.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html>

    Return values
    :   - **PTHREAD\_BARRIER\_SERIAL\_THREAD** – \- Upon successful completion, the first thread.
        - **0** – \- Upon successful completion, other thread(s).

<a id="_CPPv414pthread_createP9pthread_tPK14pthread_attr_tPFPvPvEPv"></a>

<a id="_CPPv314pthread_createP9pthread_tPK14pthread_attr_tPFPvPvEPv"></a> <a id="_CPPv214pthread_createP9pthread_tPK14pthread_attr_tPFPvPvEPv"></a> <a id="pthread_8h_1acdedb73c415d4418ac8f2512a9a4596f"></a> int pthread\_create(pthread\_t \*thread, const pthread\_attr\_t \*attr, void \*(\*startroutine)(void\*), void \*arg)
:   Thread creation.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EAGAIN** – \- Insufficient memory for either thread structure or task creation.

<a id="_CPPv422pthread_cond_broadcastP14pthread_cond_t"></a>

<a id="_CPPv322pthread_cond_broadcastP14pthread_cond_t"></a> <a id="_CPPv222pthread_cond_broadcastP14pthread_cond_t"></a> <a id="pthread_cond_broadcast__pthread_cond_tP"></a> <a id="pthread_8h_1afc4b19aa8ea2dce0956579ce878b4998"></a> int pthread\_cond\_broadcast(pthread\_cond\_t \*cond)
:   Broadcast a condition.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv420pthread_cond_destroyP14pthread_cond_t"></a>

<a id="_CPPv320pthread_cond_destroyP14pthread_cond_t"></a> <a id="_CPPv220pthread_cond_destroyP14pthread_cond_t"></a> <a id="pthread_cond_destroy__pthread_cond_tP"></a> <a id="pthread_8h_1aa1587e01856a579b78effd0a1a284a47"></a> int pthread\_cond\_destroy(pthread\_cond\_t \*cond)
:   Destroy condition variables.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_destroy.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv417pthread_cond_initP14pthread_cond_tPK18pthread_condattr_t"></a>

<a id="_CPPv317pthread_cond_initP14pthread_cond_tPK18pthread_condattr_t"></a> <a id="_CPPv217pthread_cond_initP14pthread_cond_tPK18pthread_condattr_t"></a> <a id="pthread_cond_init__pthread_cond_tP.pthread_condattr_tCP"></a> <a id="pthread_8h_1ad5b6c558bcd5260289981207b9ca9687"></a> int pthread\_cond\_init(pthread\_cond\_t \*cond, const pthread\_condattr\_t \*attr)
:   Initialize condition variables.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_init.html>

    备注

    attr is ignored and treated as NULL. Default setting is always used.

    Return values
    :   - **0** – \- Upon successful completion.
        - **ENOMEM** – \- Insufficient memory exists to initialize the condition variable.

<a id="_CPPv419pthread_cond_signalP14pthread_cond_t"></a>

<a id="_CPPv319pthread_cond_signalP14pthread_cond_t"></a> <a id="_CPPv219pthread_cond_signalP14pthread_cond_t"></a> <a id="pthread_cond_signal__pthread_cond_tP"></a> <a id="pthread_8h_1a20f98235b024efb10e5c76a64f0d94e5"></a> int pthread\_cond\_signal(pthread\_cond\_t \*cond)
:   Signal a condition.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_signal.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv422pthread_cond_timedwaitP14pthread_cond_tP15pthread_mutex_tPK8timespec"></a>

<a id="_CPPv322pthread_cond_timedwaitP14pthread_cond_tP15pthread_mutex_tPK8timespec"></a> <a id="_CPPv222pthread_cond_timedwaitP14pthread_cond_tP15pthread_mutex_tPK8timespec"></a> <a id="pthread_cond_timedwait__pthread_cond_tP.pthread_mutex_tP.timespecCP"></a> <a id="pthread_8h_1ab03e3ab6546f661d2b2f83bc12559e40"></a> int pthread\_cond\_timedwait(pthread\_cond\_t \*cond, pthread\_mutex\_t \*mutex, const struct [timespec](#_CPPv48timespec "timespec") \*abstime)
:   Wait on a condition with a timeout.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The abstime argument passed in does not refer to an initialized structure OR the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.
        - **ETIMEDOUT** – \- The time specified by abstime to [pthread\_cond\_timedwait()](#pthread_8h_1ab03e3ab6546f661d2b2f83bc12559e40) has passed.

<a id="_CPPv417pthread_cond_waitP14pthread_cond_tP15pthread_mutex_t"></a>

<a id="_CPPv317pthread_cond_waitP14pthread_cond_tP15pthread_mutex_t"></a> <a id="_CPPv217pthread_cond_waitP14pthread_cond_tP15pthread_mutex_t"></a> <a id="pthread_cond_wait__pthread_cond_tP.pthread_mutex_tP"></a> <a id="pthread_8h_1a907ae104b6dfd8fc12e23e84952aa7ca"></a> int pthread\_cond\_wait(pthread\_cond\_t \*cond, pthread\_mutex\_t \*mutex)
:   Wait on a condition.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv413pthread_equal9pthread_t9pthread_t"></a>

<a id="_CPPv313pthread_equal9pthread_t9pthread_t"></a> <a id="_CPPv213pthread_equal9pthread_t9pthread_t"></a> <a id="pthread_equal__pthread_t.pthread_t"></a> <a id="pthread_8h_1a98ec817164a6641eda2341de473b659d"></a> int pthread\_equal(pthread\_t t1, pthread\_t t2)
:   Compare thread IDs.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_equal.html>

    Return values
    :   - **0** – \- t1 and t2 are both not NULL \&\& equal.
        - **non-zero** – \- otherwise.

<a id="_CPPv412pthread_exitPv"></a>

<a id="_CPPv312pthread_exitPv"></a> <a id="_CPPv212pthread_exitPv"></a> <a id="pthread_exit__voidP"></a> <a id="pthread_8h_1a090bdc13141e76205fab4cb3c5fab0e4"></a> void pthread\_exit(void \*value\_ptr)
:   Thread termination.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html>

    Return values
    :   **void** – \- this function cannot return to its caller.

<a id="_CPPv421pthread_getschedparam9pthread_tPiP11sched_param"></a>

<a id="_CPPv321pthread_getschedparam9pthread_tPiP11sched_param"></a> <a id="_CPPv221pthread_getschedparam9pthread_tPiP11sched_param"></a> <a id="pthread_getschedparam__pthread_t.iP.sched_paramP"></a> <a id="pthread_8h_1aae9850b3759769c748727e171c4c6e61"></a> int pthread\_getschedparam(pthread\_t thread, int \*policy, struct [sched\_param](#_CPPv411sched_param "sched_param") \*param)
:   Dynamic thread scheduling parameters access.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html>

    备注

    policy is always set to SCHED\_OTHER by this function.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv412pthread_join9pthread_tPPv"></a>

<a id="_CPPv312pthread_join9pthread_tPPv"></a> <a id="_CPPv212pthread_join9pthread_tPPv"></a> <a id="pthread_join__pthread_t.voidPP"></a> <a id="pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b"></a> int pthread\_join(pthread\_t thread, void \*\*retval)
:   Wait for thread termination.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EDEADLK** – \- The value specified by the thread argument to [pthread\_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b) does not refer to a joinable thread OR multiple simultaneous calls to [pthread\_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b) specifying the same target thread OR the value specified by the thread argument to [pthread\_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b) refers to the calling thread.

<a id="_CPPv421pthread_mutex_destroyP15pthread_mutex_t"></a>

<a id="_CPPv321pthread_mutex_destroyP15pthread_mutex_t"></a> <a id="_CPPv221pthread_mutex_destroyP15pthread_mutex_t"></a> <a id="pthread_mutex_destroy__pthread_mutex_tP"></a> <a id="pthread_8h_1a3cf620ff3a40af11d79cf28901dc55e2"></a> int pthread\_mutex\_destroy(pthread\_mutex\_t \*mutex)
:   Destroy a mutex.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_destroy.html>

    备注

    If there exists a thread holding this mutex, this function returns 0 with mutex not being destroyed.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv418pthread_mutex_initP15pthread_mutex_tPK19pthread_mutexattr_t"></a>

<a id="_CPPv318pthread_mutex_initP15pthread_mutex_tPK19pthread_mutexattr_t"></a> <a id="_CPPv218pthread_mutex_initP15pthread_mutex_tPK19pthread_mutexattr_t"></a> <a id="pthread_mutex_init__pthread_mutex_tP.pthread_mutexattr_tCP"></a> <a id="pthread_8h_1a7454d249ed94ad5d5e57ba1529d7a7f2"></a> int pthread\_mutex\_init(pthread\_mutex\_t \*mutex, const pthread\_mutexattr\_t \*attr)
:   Initialize a mutex.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **ENOMEM** – \- Insufficient memory exists to initialize the mutex structure.
        - **EAGAIN** – \- Unable to initialize the mutex structure member(s).

<a id="_CPPv418pthread_mutex_lockP15pthread_mutex_t"></a>

<a id="_CPPv318pthread_mutex_lockP15pthread_mutex_t"></a> <a id="_CPPv218pthread_mutex_lockP15pthread_mutex_t"></a> <a id="pthread_mutex_lock__pthread_mutex_tP"></a> <a id="pthread_8h_1a12809c44718c21544ceb280dc1a53573"></a> int pthread\_mutex\_lock(pthread\_mutex\_t \*mutex)
:   Lock a mutex.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.
        - **EDEADLK** – \- The mutex type is PTHREAD\_MUTEX\_ERRORCHECK and the current thread already owns the mutex.

<a id="_CPPv423pthread_mutex_timedlockP15pthread_mutex_tPK8timespec"></a>

<a id="_CPPv323pthread_mutex_timedlockP15pthread_mutex_tPK8timespec"></a> <a id="_CPPv223pthread_mutex_timedlockP15pthread_mutex_tPK8timespec"></a> <a id="pthread_mutex_timedlock__pthread_mutex_tP.timespecCP"></a> <a id="pthread_8h_1a5f197c3d769dee7a09d911241a7b6766"></a> int pthread\_mutex\_timedlock(pthread\_mutex\_t \*mutex, const struct [timespec](#_CPPv48timespec "timespec") \*abstime)
:   Lock a mutex with timeout.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The abstime argument passed in does not refer to an initialized structure OR the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.
        - **EDEADLK** – \- The mutex type is PTHREAD\_MUTEX\_ERRORCHECK and the current thread already owns the mutex.
        - **ETIMEDOUT** – \- The mutex could not be locked before the specified timeout expired.

<a id="_CPPv421pthread_mutex_trylockP15pthread_mutex_t"></a>

<a id="_CPPv321pthread_mutex_trylockP15pthread_mutex_t"></a> <a id="_CPPv221pthread_mutex_trylockP15pthread_mutex_t"></a> <a id="pthread_mutex_trylock__pthread_mutex_tP"></a> <a id="pthread_8h_1a27da386211db1a7e9a3b2a0db4d22144"></a> int pthread\_mutex\_trylock(pthread\_mutex\_t \*mutex)
:   Attempt to lock a mutex. Fail immediately if mutex is already locked.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_trylock.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.
        - **EDEADLK** – \- The mutex type is PTHREAD\_MUTEX\_ERRORCHECK and the current thread already owns the mutex.
        - **EBUSY** – \- The mutex could not be acquired because it was already locked.

<a id="_CPPv420pthread_mutex_unlockP15pthread_mutex_t"></a>

<a id="_CPPv320pthread_mutex_unlockP15pthread_mutex_t"></a> <a id="_CPPv220pthread_mutex_unlockP15pthread_mutex_t"></a> <a id="pthread_mutex_unlock__pthread_mutex_tP"></a> <a id="pthread_8h_1a96184290ffb60e04c53a52869cf960a2"></a> int pthread\_mutex\_unlock(pthread\_mutex\_t \*mutex)
:   Unlock a mutex.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_unlock.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EPERM** – \- The mutex type is PTHREAD\_MUTEX\_ERRORCHECK or PTHREAD\_MUTEX\_RECURSIVE, and the current thread does not own the mutex.

<a id="_CPPv425pthread_mutexattr_destroyP19pthread_mutexattr_t"></a>

<a id="_CPPv325pthread_mutexattr_destroyP19pthread_mutexattr_t"></a> <a id="_CPPv225pthread_mutexattr_destroyP19pthread_mutexattr_t"></a> <a id="pthread_mutexattr_destroy__pthread_mutexattr_tP"></a> <a id="pthread_8h_1a2321aabf58224b06021185708d0f9658"></a> int pthread\_mutexattr\_destroy(pthread\_mutexattr\_t \*attr)
:   Destroy the mutex attributes object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_destroy.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv425pthread_mutexattr_gettypePK19pthread_mutexattr_tPi"></a>

<a id="_CPPv325pthread_mutexattr_gettypePK19pthread_mutexattr_tPi"></a> <a id="_CPPv225pthread_mutexattr_gettypePK19pthread_mutexattr_tPi"></a> <a id="pthread_mutexattr_gettype__pthread_mutexattr_tCP.iP"></a> <a id="pthread_8h_1a7f064a4db96a009a5a9a7c7e5cc03599"></a> int pthread\_mutexattr\_gettype(const pthread\_mutexattr\_t \*attr, int \*type)
:   Get the mutex type attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv422pthread_mutexattr_initP19pthread_mutexattr_t"></a>

<a id="_CPPv322pthread_mutexattr_initP19pthread_mutexattr_t"></a> <a id="_CPPv222pthread_mutexattr_initP19pthread_mutexattr_t"></a> <a id="pthread_mutexattr_init__pthread_mutexattr_tP"></a> <a id="pthread_8h_1af98f6b6c483077a39d1400b1de1577b8"></a> int pthread\_mutexattr\_init(pthread\_mutexattr\_t \*attr)
:   Initialize the mutex attributes object.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_init.html>

    备注

    Currently, only the type attribute is supported. Also see [pthread\_mutexattr\_settype()](#pthread_8h_1a8387c80e660e9426f801ac0217ecfae5) and [pthread\_mutexattr\_gettype()](#pthread_8h_1a7f064a4db96a009a5a9a7c7e5cc03599).

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv425pthread_mutexattr_settypeP19pthread_mutexattr_ti"></a>

<a id="_CPPv325pthread_mutexattr_settypeP19pthread_mutexattr_ti"></a> <a id="_CPPv225pthread_mutexattr_settypeP19pthread_mutexattr_ti"></a> <a id="pthread_mutexattr_settype__pthread_mutexattr_tP.i"></a> <a id="pthread_8h_1a8387c80e660e9426f801ac0217ecfae5"></a> int pthread\_mutexattr\_settype(pthread\_mutexattr\_t \*attr, int type)
:   Set the mutex type attribute.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_settype.html>

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The value type is invalid.

<a id="_CPPv412pthread_selfv"></a>

<a id="_CPPv312pthread_selfv"></a> <a id="_CPPv212pthread_selfv"></a> <a id="pthread_self__void"></a> <a id="pthread_8h_1a4c4f5f3b4f8f45d9d897847d53b11aaa"></a> pthread\_t pthread\_self(void)
:   Get the calling thread ID.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_self.html>

    Return values
    :   **the** – thread ID of the calling thread.

<a id="_CPPv421pthread_setschedparam9pthread_tiPK11sched_param"></a>

<a id="_CPPv321pthread_setschedparam9pthread_tiPK11sched_param"></a> <a id="_CPPv221pthread_setschedparam9pthread_tiPK11sched_param"></a> <a id="pthread_setschedparam__pthread_t.i.sched_paramCP"></a> <a id="pthread_8h_1a14f50e1f5d815c90f1f4225eca5d3a8c"></a> int pthread\_setschedparam(pthread\_t thread, int policy, const struct [sched\_param](#_CPPv411sched_param "sched_param") \*param)
:   Dynamic thread scheduling parameters access.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedparam.html>

    备注

    policy is ignored; only priority (param.sched\_priority) may be changed.

    Return values
    :   **0** – \- Upon successful completion.

<a id="id14"></a>

### Macros

<a id="c.PTHREAD_CREATE_DETACHED"></a>

<a id="pthread_8h_1a391c5eb0f6b5febc48710d0be3f62394"></a> PTHREAD\_CREATE\_DETACHED
:   Detached.

<a id="c.PTHREAD_CREATE_JOINABLE"></a>

<a id="pthread_8h_1afb10d234d831c7b57768d62786748bc7"></a> PTHREAD\_CREATE\_JOINABLE
:   Joinable (default).

<a id="c.PTHREAD_BARRIER_SERIAL_THREAD"></a>

<a id="pthread_8h_1a822c63bc662ad86cfb2dcec50edbb42b"></a> PTHREAD\_BARRIER\_SERIAL\_THREAD

<a id="c.PTHREAD_MUTEX_NORMAL"></a>

<a id="pthread_8h_1aae4b650085c2599674938f503d6253cf"></a> PTHREAD\_MUTEX\_NORMAL
:   Non-robust, deadlock on relock, does not remember owner.

<a id="c.PTHREAD_MUTEX_ERRORCHECK"></a>

<a id="pthread_8h_1aaf502496651f95b06be861af7902cb23"></a> PTHREAD\_MUTEX\_ERRORCHECK
:   Non-robust, error on relock, remembers owner.

<a id="c.PTHREAD_MUTEX_RECURSIVE"></a>

<a id="pthread_8h_1a715e9644a7183d98cb2c9dd41cb89645"></a> PTHREAD\_MUTEX\_RECURSIVE
:   Non-robust, recursive relock, remembers owner.

<a id="c.PTHREAD_MUTEX_DEFAULT"></a>

<a id="pthread_8h_1a2a9b96c0491ae490c17d0b400bc427b0"></a> PTHREAD\_MUTEX\_DEFAULT
:   PTHREAD\_MUTEX\_NORMAL (default).

<a id="sched-apis"></a>

## **sched APIs**

> - #include \<posix/sched.h\>;
> - APIs related to system scheduling

<a id="id15"></a>

### Header File

- [sched.h](https://github.com/bekencorp/armino/blob/main/components/sched.h)

<a id="id16"></a>

### Functions

<a id="_CPPv422sched_get_priority_maxi"></a>

<a id="_CPPv322sched_get_priority_maxi"></a> <a id="_CPPv222sched_get_priority_maxi"></a> <a id="sched_get_priority_max__i"></a> <a id="sched_8h_1afaebd1698caeb9b9b9e614ad84edd609"></a> int sched\_get\_priority\_max(int policy)
:   Get priority limit (max).

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_max.html>

    备注

    policy is ignored.

    返回
    :   the maximum priority value (0-based) system configuration allows.

        e.g. if configMAX\_PRIORITIES \=\= 7, this function returns (configMAX\_PRIORITIES \- 1). configMAX\_PRIORITIES is configured in application FreeRTOSConfig.h file.

<a id="_CPPv422sched_get_priority_mini"></a>

<a id="_CPPv322sched_get_priority_mini"></a> <a id="_CPPv222sched_get_priority_mini"></a> <a id="sched_get_priority_min__i"></a> <a id="sched_8h_1af1f370fc36ea6b22ed42b5ee3cf82a81"></a> int sched\_get\_priority\_min(int policy)
:   Get priority limit (min).

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_min.html>

    备注

    policy is ignored.

<a id="_CPPv411sched_yieldv"></a>

<a id="_CPPv311sched_yieldv"></a> <a id="_CPPv211sched_yieldv"></a> <a id="sched_yield__void"></a> <a id="sched_8h_1a357cd4b34c13011749dfffb42b489f09"></a> int sched\_yield(void)
:   Yield the processor.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_yield.html>

    Return values
    :   **0** – \- Upon successful completion

<a id="id17"></a>

### Structures

<a id="_CPPv411sched_param"></a>

<a id="_CPPv311sched_param"></a> <a id="_CPPv211sched_param"></a> <a id="sched_param"></a> <a id="structsched__param"></a> struct sched\_param
:   Scheduling parameters required for implementation of each supported scheduling policy.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11sched_param14sched_priorityE"></a>

    <a id="_CPPv3N11sched_param14sched_priorityE"></a> <a id="_CPPv2N11sched_param14sched_priorityE"></a> <a id="sched_param::sched_priority__i"></a> <a id="structsched__param_1aa0f2640949273f2c30549ed8d1bb197e"></a> int sched\_priority
    :   Process or thread execution scheduling priority.

<a id="id18"></a>

### Macros

<a id="c.SCHED_OTHER"></a>

<a id="sched_8h_1a44c9baaf6f3c286f76783265b4938881"></a> SCHED\_OTHER
:   Another scheduling policy.

<a id="semaphore-apis"></a>

## **semaphore APIs**

> - #include \<posix/semaphore.h\>;
> - Defines the APIs related to semaphores

<a id="id19"></a>

### Header File

- [semaphore.h](https://github.com/bekencorp/armino/blob/main/components/semaphore.h)

<a id="id20"></a>

### Functions

<a id="_CPPv411sem_destroyP5sem_t"></a>

<a id="_CPPv311sem_destroyP5sem_t"></a> <a id="_CPPv211sem_destroyP5sem_t"></a> <a id="sem_destroy__sem_tP"></a> <a id="semaphore_8h_1a6bc9a7dd941a9b5e319715b767af5682"></a> int sem\_destroy([sem\_t](#_CPPv45sem_t "sem_t") \*sem)
:   Destroy an unnamed semaphore.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_destroy.html>

    备注

    Semaphore is destroyed regardless of whether there is any thread currently blocked on this semaphore.

    Return values
    :   **0** – \- upon successful completion

<a id="_CPPv412sem_getvalueP5sem_tPi"></a>

<a id="_CPPv312sem_getvalueP5sem_tPi"></a> <a id="_CPPv212sem_getvalueP5sem_tPi"></a> <a id="sem_getvalue__sem_tP.iP"></a> <a id="semaphore_8h_1a9755d3b56c40d2aec3d55b00c8f7cae8"></a> int sem\_getvalue([sem\_t](#_CPPv45sem_t "sem_t") \*sem, int \*sval)
:   Get the value of a semaphore.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_getvalue.html>

    备注

    If sem is locked, then the object to which sval points is set to zero.

    Return values
    :   **0** – \- Upon successful completion

<a id="_CPPv48sem_initP5sem_tij"></a>

<a id="_CPPv38sem_initP5sem_tij"></a> <a id="_CPPv28sem_initP5sem_tij"></a> <a id="sem_init__sem_tP.i.unsigned"></a> <a id="semaphore_8h_1a8437c38b02b5858b66f2df30f4f26435"></a> int sem\_init([sem\_t](#_CPPv45sem_t "sem_t") \*sem, int pshared, unsigned value)
:   Initialize an unnamed semaphore.

    @sideeffect Possible errno values

    EINVAL \- The value argument exceeds {SEM\_VALUE\_MAX}.

    ENOSPC \- A resource required to initialize the semaphore has been exhausted.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_init.html>

    备注

    pshared is ignored. Semaphores will always be considered “shared”.

    Return values
    :   - **0** – \- upon successful completion
        - **-1** – \- otherwise. System error variable errno is also set in this case.

<a id="_CPPv48sem_postP5sem_t"></a>

<a id="_CPPv38sem_postP5sem_t"></a> <a id="_CPPv28sem_postP5sem_t"></a> <a id="sem_post__sem_tP"></a> <a id="semaphore_8h_1a015dce85cab8477c679cc47968958247"></a> int sem\_post([sem\_t](#_CPPv45sem_t "sem_t") \*sem)
:   Unlock a semaphore.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_post.html>

    Return values
    :   **0** – \- upon successful completion

<a id="_CPPv413sem_timedwaitP5sem_tPK8timespec"></a>

<a id="_CPPv313sem_timedwaitP5sem_tPK8timespec"></a> <a id="_CPPv213sem_timedwaitP5sem_tPK8timespec"></a> <a id="sem_timedwait__sem_tP.timespecCP"></a> <a id="semaphore_8h_1a9fa286fcc7ddce4e32fa449f34a494c6"></a> int sem\_timedwait([sem\_t](#_CPPv45sem_t "sem_t") \*sem, const struct [timespec](#_CPPv48timespec "timespec") \*abstime)
:   Lock a semaphore with timeout.

    @sideeffect Possible errno values

    EINVAL \- parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million

    ETIMEDOUT \- The semaphore could not be locked before the specified timeout expired.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_timedwait.html>

    备注

    Deadlock detection is not implemented.

    Return values
    :   - **0** – \- upon successful completion
        - **-1** – \- otherwise. System error variable errno is also set in this case.

<a id="_CPPv411sem_trywaitP5sem_t"></a>

<a id="_CPPv311sem_trywaitP5sem_t"></a> <a id="_CPPv211sem_trywaitP5sem_t"></a> <a id="sem_trywait__sem_tP"></a> <a id="semaphore_8h_1a4de7a9a334b01b6373b017aaefa07cf0"></a> int sem\_trywait([sem\_t](#_CPPv45sem_t "sem_t") \*sem)
:   Lock a semaphore if available.

    @sideeffect Possible errno values

    EAGAIN \- The semaphore was already locked, so it cannot be immediately locked by the

    [sem\_trywait()](#semaphore_8h_1a4de7a9a334b01b6373b017aaefa07cf0) operation.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_trywait.html>

    Return values
    :   - **0** – \- upon successful completion
        - **-1** – \- otherwise. System error variable errno is also set in this case.

<a id="_CPPv48sem_waitP5sem_t"></a>

<a id="_CPPv38sem_waitP5sem_t"></a> <a id="_CPPv28sem_waitP5sem_t"></a> <a id="sem_wait__sem_tP"></a> <a id="semaphore_8h_1aad70020dca2241a2b78e272ca033271b"></a> int sem\_wait([sem\_t](#_CPPv45sem_t "sem_t") \*sem)
:   Lock a semaphore.

    参见

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_wait.html>

    备注

    Deadlock detection is not implemented.

    Return values
    :   - **0** – \- upon successful completion
        - **-1** – \- otherwise. System error variable errno is also set in this case.

<a id="id21"></a>

### Type Definitions

<a id="_CPPv45sem_t"></a>

<a id="_CPPv35sem_t"></a> <a id="_CPPv25sem_t"></a> <a id="sem_t"></a> <a id="semaphore_8h_1acdcd24391f60977a34f32015c2edadaa"></a> typedef PosixSemType\_t sem\_t
:   Semaphore type.

<a id="time-apis"></a>

## **time APIs**

> - #include \<posix/time.h\>;
> - Defines APIs related to timers

<a id="id22"></a>

### Header File

- [time.h](https://github.com/bekencorp/armino/blob/main/components/time.h)

<a id="id23"></a>

### Functions

<a id="_CPPv45clockv"></a>

<a id="_CPPv35clockv"></a> <a id="_CPPv25clockv"></a> <a id="clock__void"></a> <a id="time_8h_1ade863cfcca9ee19f20ca95796f8ddc1e"></a> clock\_t clock(void)
:   Report CPU time used.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock.html>

    备注

    This function does NOT report the number of ticks spent by the calling thread.

    返回
    :   The number of FreeRTOS ticks since the scheduler was started minus the ticks spent in the idle task.

<a id="_CPPv419clock_getcpuclockid5pid_tP9clockid_t"></a>

<a id="_CPPv319clock_getcpuclockid5pid_tP9clockid_t"></a> <a id="_CPPv219clock_getcpuclockid5pid_tP9clockid_t"></a> <a id="clock_getcpuclockid__pid_t.clockid_tP"></a> <a id="time_8h_1ab2cd29aa41b2b485b571f05ac22d9f7f"></a> int clock\_getcpuclockid(pid\_t pid, clockid\_t \*clock\_id)
:   Access a process CPU-time clock.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getcpuclockid.html>

    备注

    This function is currently unsupported.

    Return values
    :   **EPERM** –

<a id="_CPPv412clock_getres9clockid_tP8timespec"></a>

<a id="_CPPv312clock_getres9clockid_tP8timespec"></a> <a id="_CPPv212clock_getres9clockid_tP8timespec"></a> <a id="clock_getres__clockid_t.timespecP"></a> <a id="time_8h_1a463c567de23a4f064b415a959fe2a96b"></a> int clock\_getres(clockid\_t clock\_id, struct [timespec](#_CPPv48timespec "timespec") \*res)
:   Returns the resolution of a clock.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getres.html>

    备注

    clock\_id is ignored

    备注

    This function stores the resolution of the FreeRTOS tick count in the object res points to.

    Return values
    :   **0** – \- Upon successful execution

<a id="_CPPv413clock_gettime9clockid_tP8timespec"></a>

<a id="_CPPv313clock_gettime9clockid_tP8timespec"></a> <a id="_CPPv213clock_gettime9clockid_tP8timespec"></a> <a id="clock_gettime__clockid_t.timespecP"></a> <a id="time_8h_1a10b73e75d375e5c244e32ea46be775bf"></a> int clock\_gettime(clockid\_t clock\_id, struct [timespec](#_CPPv48timespec "timespec") \*tp)
:   Returns the current value for the specified clock, clock\_id.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_gettime.html>

    备注

    clock\_id is ignored

    备注

    this function does not check for overflows of time\_t.

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv415clock_nanosleep9clockid_tiPK8timespecP8timespec"></a>

<a id="_CPPv315clock_nanosleep9clockid_tiPK8timespecP8timespec"></a> <a id="_CPPv215clock_nanosleep9clockid_tiPK8timespecP8timespec"></a> <a id="clock_nanosleep__clockid_t.i.timespecCP.timespecP"></a> <a id="time_8h_1a924d51d78cdcd9d7dee2613fb3a33cd1"></a> int clock\_nanosleep(clockid\_t clock\_id, int flags, const struct [timespec](#_CPPv48timespec "timespec") \*rqtp, struct [timespec](#_CPPv48timespec "timespec") \*rmtp)
:   High resolution sleep with specifiable clock.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_nanosleep.html>

    备注

    clock\_id is ignored, as this function uses the FreeRTOS tick count as its clock.

    备注

    flags is ignored, if INCLUDE\_vTaskDelayUntil is 0\. i.e. the FreeRTOS function vTaskDelayUntil isn’t available.

    备注

    rmtp is also ignored, as signals are not implemented.

    Return values
    :   - **0** – \- Upon successful completion.
        - **EINVAL** – \- The rqtp argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

<a id="_CPPv413clock_settime9clockid_tPK8timespec"></a>

<a id="_CPPv313clock_settime9clockid_tPK8timespec"></a> <a id="_CPPv213clock_settime9clockid_tPK8timespec"></a> <a id="clock_settime__clockid_t.timespecCP"></a> <a id="time_8h_1ab0dbabb3e47efe9483b81235fdd0c297"></a> int clock\_settime(clockid\_t clock\_id, const struct [timespec](#_CPPv48timespec "timespec") \*tp)
:   Sets the time for the specified clock.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_settime.html>

    备注

    This function is currently unsupported, as FreeRTOS does not provide a function to modify the tick count.

    Return values
    :   **-1** – with errno set to EPERM.

<a id="_CPPv49nanosleepPK8timespecP8timespec"></a>

<a id="_CPPv39nanosleepPK8timespecP8timespec"></a> <a id="_CPPv29nanosleepPK8timespecP8timespec"></a> <a id="nanosleep__timespecCP.timespecP"></a> <a id="time_8h_1a9ce6a1ed91a601dee133c8b6cf8b721a"></a> int nanosleep(const struct [timespec](#_CPPv48timespec "timespec") \*rqtp, struct [timespec](#_CPPv48timespec "timespec") \*rmtp)
:   High resolution sleep.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/nanosleep.html>

    备注

    rmtp is ignored, as signals are not implemented.

    Return values
    :   - **0** – \- Upon successful completion.
        - **-1** – \- The rqtp argument is invalid OR the rqtp argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

<a id="_CPPv412timer_create9clockid_tP8sigeventP7timer_t"></a>

<a id="_CPPv312timer_create9clockid_tP8sigeventP7timer_t"></a> <a id="_CPPv212timer_create9clockid_tP8sigeventP7timer_t"></a> <a id="timer_create__clockid_t.sigeventP.timer_tP"></a> <a id="time_8h_1aade0bf466f5cbd364bc9ba7a73510891"></a> int timer\_create(clockid\_t clockid, struct [sigevent](#_CPPv48sigevent "sigevent") \*evp, timer\_t \*timerid)
:   Create a per-process timer.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_create.html>

    @sideeffect Possible errno values

    ENOTSUP \- If evp is NULL OR evp-\>sigen\_notify \=\= SIGEV\_SIGNAL.

    EAGAIN \- The system lacks sufficient signal queuing resources to honor the request.

    备注

    clock\_id is ignored, as this function used the FreeRTOS tick count as its clock.

    备注

    evp.sigev\_notify must be set to SIGEV\_THREAD, since signals are currently not supported.

    Return values
    :   - **0** – \- Upon successful completion, with location referenced by timerid updated.
        - **-1** – \- If an error occurs. errno is also set.

<a id="_CPPv412timer_delete7timer_t"></a>

<a id="_CPPv312timer_delete7timer_t"></a> <a id="_CPPv212timer_delete7timer_t"></a> <a id="timer_delete__timer_t"></a> <a id="time_8h_1ad114bb350d7d5d12cff3fd19bf533303"></a> int timer\_delete(timer\_t timerid)
:   Delete a per-process timer.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_delete.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv416timer_getoverrun7timer_t"></a>

<a id="_CPPv316timer_getoverrun7timer_t"></a> <a id="_CPPv216timer_getoverrun7timer_t"></a> <a id="timer_getoverrun__timer_t"></a> <a id="time_8h_1ad779f0bc22f64bd3bd977221b0ce1b8f"></a> int timer\_getoverrun(timer\_t timerid)
:   Get the timer overrun count.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_getoverrun.html>

    Return values
    :   **0** – \- Always return 0, since signals are not supported.

<a id="_CPPv413timer_gettime7timer_tP10itimerspec"></a>

<a id="_CPPv313timer_gettime7timer_tP10itimerspec"></a> <a id="_CPPv213timer_gettime7timer_tP10itimerspec"></a> <a id="timer_gettime__timer_t.itimerspecP"></a> <a id="time_8h_1a520e1913c35aa3352259dafa3259d140"></a> int timer\_gettime(timer\_t timerid, struct [itimerspec](#_CPPv410itimerspec "itimerspec") \*value)
:   Get the amount of time until the timer expires.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_gettime.html>

    Return values
    :   **0** – \- Upon successful completion.

<a id="_CPPv413timer_settime7timer_tiPK10itimerspecP10itimerspec"></a>

<a id="_CPPv313timer_settime7timer_tiPK10itimerspecP10itimerspec"></a> <a id="_CPPv213timer_settime7timer_tiPK10itimerspecP10itimerspec"></a> <a id="timer_settime__timer_t.i.itimerspecCP.itimerspecP"></a> <a id="time_8h_1a32207b51f2effa8441f4c728fd8519c0"></a> int timer\_settime(timer\_t timerid, int flags, const struct [itimerspec](#_CPPv410itimerspec "itimerspec") \*value, struct [itimerspec](#_CPPv410itimerspec "itimerspec") \*ovalue)
:   Set the time until the next expiration of the timer.

    <http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_settime.html>

    @sideeffect Possible errno values

    EINVAL \- A value structure specified a nanosecond value less than zero or greater than or equal to 1000 million, AND the it\_value member of that structure did not specify zero seconds and nanoseconds.

    Return values
    :   - **0** – \- Upon successful completion.
        - **-1** – \- An error occurred, errno is also set.

<a id="id24"></a>

### Structures

<a id="_CPPv48timespec"></a>

<a id="_CPPv38timespec"></a> <a id="_CPPv28timespec"></a> <a id="timespec"></a> <a id="structtimespec"></a> struct timespec
:   represents an elapsed time

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N8timespec6tv_secE"></a>

    <a id="_CPPv3N8timespec6tv_secE"></a> <a id="_CPPv2N8timespec6tv_secE"></a> <a id="timespec::tv_sec__time_t"></a> <a id="structtimespec_1afc3302668d7cb5952f590da69fdd4955"></a> time\_t tv\_sec
    :   Seconds.

    <a id="_CPPv4N8timespec7tv_nsecE"></a>

    <a id="_CPPv3N8timespec7tv_nsecE"></a> <a id="_CPPv2N8timespec7tv_nsecE"></a> <a id="timespec::tv_nsec__l"></a> <a id="structtimespec_1ae3c7510dafa8cbcaede866ed13c99683"></a> long tv\_nsec
    :   Nanoseconds.

<a id="_CPPv410itimerspec"></a>

<a id="_CPPv310itimerspec"></a> <a id="_CPPv210itimerspec"></a> <a id="itimerspec"></a> <a id="structitimerspec"></a> struct itimerspec
:   timer

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10itimerspec11it_intervalE"></a>

    <a id="_CPPv3N10itimerspec11it_intervalE"></a> <a id="_CPPv2N10itimerspec11it_intervalE"></a> <a id="itimerspec::it_interval__timespec"></a> <a id="structitimerspec_1a27cedae552e2b2fe0993c1b2c4ff1889"></a> struct [timespec](#_CPPv48timespec "timespec") it\_interval
    :   Timer period.

    <a id="_CPPv4N10itimerspec8it_valueE"></a>

    <a id="_CPPv3N10itimerspec8it_valueE"></a> <a id="_CPPv2N10itimerspec8it_valueE"></a> <a id="itimerspec::it_value__timespec"></a> <a id="structitimerspec_1a754dda918053251c24558b07571d6e8f"></a> struct [timespec](#_CPPv48timespec "timespec") it\_value
    :   Timer expiration.

<a id="id25"></a>

### Macros

<a id="c.MICROSECONDS_PER_SECOND"></a>

<a id="time_8h_1a8a708413d6171e7d86056793abe2cd1a"></a> MICROSECONDS\_PER\_SECOND
:   Microseconds per second.

<a id="c.NANOSECONDS_PER_SECOND"></a>

<a id="time_8h_1a5df38c677104658963501aa1e2a88e60"></a> NANOSECONDS\_PER\_SECOND
:   Nanoseconds per second.

<a id="c.NANOSECONDS_PER_TICK"></a>

<a id="time_8h_1a033850a105f65ce574fc0f7de437dd14"></a> NANOSECONDS\_PER\_TICK
:   Nanoseconds per FreeRTOS tick.

<a id="c.CLOCK_REALTIME"></a>

<a id="time_8h_1a922ce1ae64374c9410c8a999e25e82af"></a> CLOCK\_REALTIME
:   The identifier of the system-wide clock measuring real time.

<a id="c.CLOCK_MONOTONIC"></a>

<a id="time_8h_1a6fb83f5e91e704391ff796553d5e0f46"></a> CLOCK\_MONOTONIC
:   The identifier for the system-wide monotonic clock.

<a id="c.CLOCKS_PER_SEC"></a>

<a id="time_8h_1a3d9fc3c745d0880902fe3ea3d5d5f71e"></a> CLOCKS\_PER\_SEC

<a id="c.TIMER_ABSTIME"></a>

<a id="time_8h_1adde83d9ea51f12d4149f016eededde54"></a> TIMER\_ABSTIME
