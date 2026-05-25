# fcntl接口介绍[](#fcntl "永久链接至标题")

> - 需要包含头文件#include <posix/fcntl.h>;
> - 定义了posix接口file cntrol相关的宏定义

[[English]](../../../../../en/v2.0.1/api-reference/system/posix/fcntl.html "../../../../../en/v2.0.1/api-reference/system/posix/fcntl.html")


## Header File[](#header-file "永久链接至标题")


- [fcntl.h](https://github.com/bekencorp/armino/blob/main/components/fcntl.h "https://github.com/bekencorp/armino/blob/main/components/fcntl.h")


## Macros[](#macros "永久链接至标题")

O_CLOEXEC[](#c.O_CLOEXEC "永久链接至目标")
:   Close the file descriptor upon exec().

O_CREAT[](#c.O_CREAT "永久链接至目标")
:   Create file if it does not exist.

O_DIRECTORY[](#c.O_DIRECTORY "永久链接至目标")
:   Fail if file is a non-directory file.

O_EXCL[](#c.O_EXCL "永久链接至目标")
:   Exclusive use flag.

O_NOCTTY[](#c.O_NOCTTY "永久链接至目标")
:   Do not assign controlling terminal.

O_NOFOLLOW[](#c.O_NOFOLLOW "永久链接至目标")
:   Do not follow symbolic links.

O_TRUNC[](#c.O_TRUNC "永久链接至目标")
:   Truncate flag.

O_TTY_INIT[](#c.O_TTY_INIT "永久链接至目标")
:   termios structure provides conforming behavior.

O_APPEND[](#c.O_APPEND "永久链接至目标")
:   Set append mode.

O_DSYNC[](#c.O_DSYNC "永久链接至目标")
:   Write according to synchronized I/O data integrity completion.

O_NONBLOCK[](#c.O_NONBLOCK "永久链接至目标")
:   Non-blocking mode.

O_RSYNC[](#c.O_RSYNC "永久链接至目标")
:   Synchronized read I/O operations.

O_SYNC[](#c.O_SYNC "永久链接至目标")
:   Write according to synchronized I/O file integrity completion.

O_ACCMODE[](#c.O_ACCMODE "永久链接至目标")

O_EXEC[](#c.O_EXEC "永久链接至目标")
:   Open for execute only (non-directory files).

O_RDONLY[](#c.O_RDONLY "永久链接至目标")
:   Open for reading only.

O_RDWR[](#c.O_RDWR "永久链接至目标")
:   Open for reading and writing.

O_SEARCH[](#c.O_SEARCH "永久链接至目标")
:   Open directory for search only.

O_WRONLY[](#c.O_WRONLY "永久链接至目标")
:   Open for writing only.
