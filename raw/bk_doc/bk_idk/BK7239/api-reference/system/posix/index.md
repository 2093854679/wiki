# POSIX APIs[](#posix-apis "永久链接至标题")



## POSIX APIs 介绍[](#id1 "永久链接至标题")

> - 目前Armino平台posix接口仅支持FreeRTOS V10.4操作系统，默认关闭;
> - 若打开使用，需要打开CONFIG_FREERTOS_POSIX配置开关

备注


- 在使用FreeRTOS的posix功能的时候，在引用posix相关头文件之前，需要先引用FreeRTOS_POSIX.h头文件；

- 可以在components/bk_rtos/freertos/posix/freertos_impl/include/portable/bk/FreeRTOS_POSIX_portable.h中自定义相关配置。


- [unistd接口](unistd.md "unistd.md")

- [utils接口](utils.md "utils.md")

- [errno接口](errno.md "errno.md")

- [fcntl接口](fcntl.md "fcntl.md")

- [signal接口](signal.md "signal.md")

- [mqueue接口](mqueue.md "mqueue.md")

- [pthread接口](pthread.md "pthread.md")

- [sched接口](sched.md "sched.md")

- [semaphore接口](semaphore.md "semaphore.md")

- [time接口](time.md "time.md")
