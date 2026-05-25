# unistd接口介绍[](#unistd "永久链接至标题")

> - 需要包含头文件#include <posix/unistd.h>;
> - 定义了系统sleep相关的接口



## Header File[](#header-file "永久链接至标题")


- [unistd.h](https://github.com/bekencorp/armino/blob/main/components/unistd.h "https://github.com/bekencorp/armino/blob/main/components/unistd.h")


## Functions[](#functions "永久链接至标题")

unsigned sleep(unsigned seconds)[](#_CPPv45sleepj "永久链接至目标")
:   Suspend execution for an interval of time.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sleep.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sleep.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/sleep.html")

    备注

    Return value of a positive number is not yet supported.

    参数
    :   **seconds** – **[in]** The number of seconds to suspend execution.

    Return values
    :   **0** – - Upon successful completion.

int usleep(useconds_t usec)[](#_CPPv46usleep10useconds_t "永久链接至目标")
:   Suspend execution for microsecond intervals.

    This is a useful, non-POSIX function.

    参数
    :   **usec** – **[in]** The number of microseconds to suspend execution.

    Return values
    :   **0** – - Upon successful completion.
