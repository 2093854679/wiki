# POSIX APIs[](#posix-apis "永久链接至标题")

[[English]](../../../../../en/v2.2.1/api-reference/system/posix/index.html "../../../../../en/v2.2.1/api-reference/system/posix/index.html")


## POSIX APIs 介绍[](#id1 "永久链接至标题")

> - 目前Armino平台posix接口仅支持FreeRTOS V10.4操作系统，默认关闭;
> - 若打开使用，需要打开CONFIG_FREERTOS_POSIX配置开关

备注


- 在使用FreeRTOS的posix功能的时候，在引用posix相关头文件之前，需要先引用FreeRTOS_POSIX.h头文件；

- 可以在components/bk_rtos/freertos/posix/freertos_impl/include/portable/bk/FreeRTOS_POSIX_portable.h中自定义相关配置。


- [unistd接口](unistd.html "unistd.html")

- [utils接口](utils.html "utils.html")

- [errno接口](errno.html "errno.html")

- [fcntl接口](fcntl.html "fcntl.html")

- [signal接口](signal.html "signal.html")

- [mqueue接口](mqueue.html "mqueue.html")

- [pthread接口](pthread.html "pthread.html")

- [sched接口](sched.html "sched.html")

- [semaphore接口](semaphore.html "semaphore.html")

- [time接口](time.html "time.html")
