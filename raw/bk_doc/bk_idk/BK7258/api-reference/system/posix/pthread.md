# pthread接口介绍[](#pthread "永久链接至标题")

> - 需要包含头文件#include <posix/pthread.h>;
> - 定义了系统任务创建，销毁等相关的接口

[[English]](../../../../../en/v2.0.1/api-reference/system/posix/pthread.html "../../../../../en/v2.0.1/api-reference/system/posix/pthread.html")


## Header File[](#header-file "永久链接至标题")


- [pthread.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/pthread.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/pthread.h")


## Functions[](#functions "永久链接至标题")

int pthread_attr_destroy(pthread_attr_t *attr)[](#_CPPv420pthread_attr_destroyP14pthread_attr_t "永久链接至目标")
:   Destroy the thread attributes object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_destroy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_destroy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_destroy.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_getdetachstate(const pthread_attr_t *attr, int *detachstate)[](#_CPPv427pthread_attr_getdetachstatePK14pthread_attr_tPi "永久链接至目标")
:   Get detachstate attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getdetachstate.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getdetachstate.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getdetachstate.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_getschedparam(const pthread_attr_t *attr, struct [sched_param](sched.html#_CPPv411sched_param "sched_param") *param)[](#_CPPv426pthread_attr_getschedparamPK14pthread_attr_tP11sched_param "永久链接至目标")
:   Get schedparam attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getschedparam.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_getstacksize(const pthread_attr_t *attr, size_t *stacksize)[](#_CPPv425pthread_attr_getstacksizePK14pthread_attr_tP6size_t "永久链接至目标")
:   Get stacksize attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_getstacksize.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_init(pthread_attr_t *attr)[](#_CPPv417pthread_attr_initP14pthread_attr_t "永久链接至目标")
:   Initialize the thread attributes object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_init.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_init.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_init.html")

    备注

    Currently, only stack size, [sched_param](sched.html#structsched__param "sched.html#structsched__param"), and detach state attributes are supported. Also see pthread_attr_get*() and pthread_attr_set*().

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_setdetachstate(pthread_attr_t *attr, int detachstate)[](#_CPPv427pthread_attr_setdetachstateP14pthread_attr_ti "永久链接至目标")
:   Set detachstate attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setdetachstate.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setdetachstate.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setdetachstate.html")

    Return values
    :   - **0** – - Upon successful completion

        - **EINVAL** – - The value of detachstate is not valid. Currently, supported detach states are &#8212; PTHREAD_CREATE_DETACHED and PTHREAD_CREATE_JOINABLE.

int pthread_attr_setschedparam(pthread_attr_t *attr, const struct [sched_param](sched.html#_CPPv411sched_param "sched_param") *param)[](#_CPPv426pthread_attr_setschedparamP14pthread_attr_tPK11sched_param "永久链接至目标")
:   Set schedparam attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedparam.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedparam.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedparam.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The value of param is not valid.

        - **ENOTSUP** – - An attempt was made to set the attribute to an unsupported value.

int pthread_attr_setschedpolicy(pthread_attr_t *attr, int policy)[](#_CPPv427pthread_attr_setschedpolicyP14pthread_attr_ti "永久链接至目标")
:   Set the schedpolicy attribute.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedpolicy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedpolicy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setschedpolicy.html")

    警告

    This function is a stub and always returns 0.

    Return values
    :   **0** – - Upon successful completion.

int pthread_attr_setstacksize(pthread_attr_t *attr, size_t stacksize)[](#_CPPv425pthread_attr_setstacksizeP14pthread_attr_t6size_t "永久链接至目标")
:   Set stacksize attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setstacksize.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setstacksize.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_attr_setstacksize.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The value of stacksize is less than {PTHREAD_STACK_MIN}.

int pthread_barrier_destroy(pthread_barrier_t *barrier)[](#_CPPv423pthread_barrier_destroyP17pthread_barrier_t "永久链接至目标")
:   Destroy a barrier object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_destroy.html")

    备注

    This function does not validate whether there is any thread blocking on the barrier before destroying.

    Return values
    :   **0** – - Upon successful completion.

int pthread_barrier_init(pthread_barrier_t *barrier, const pthread_barrierattr_t *attr, unsigned count)[](#_CPPv420pthread_barrier_initP17pthread_barrier_tPK21pthread_barrierattr_tj "永久链接至目标")
:   Initialize a barrier object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_init.html")

    备注

    attr is ignored.

    备注

    [pthread_barrier_init()](#pthread_8h_1ae3328293a058e9c0641dbdbdfff3761e "#pthread_8h_1ae3328293a058e9c0641dbdbdfff3761e") is implemented with FreeRTOS event group. To ensure count fits in event group, count may be at most 8 when configUSE_16_BIT_TICKS is 1; it may be at most 24 otherwise. configUSE_16_BIT_TICKS is configured in application FreeRTOSConfig.h file, which defines how many bits tick count type has. See further details and limitation about event group and configUSE_16_BIT_TICKS in FreeRTOS site.

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The value specified by count is equal to zero.

        - **ENOMEM** – - count cannot fit into FreeRTOS event group type OR insufficient memory exists to initialize the barrier.

int pthread_barrier_wait(pthread_barrier_t *barrier)[](#_CPPv420pthread_barrier_waitP17pthread_barrier_t "永久链接至目标")
:   Synchronize at a barrier.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_barrier_wait.html")

    Return values
    :   - **PTHREAD_BARRIER_SERIAL_THREAD** – - Upon successful completion, the first thread.

        - **0** – - Upon successful completion, other thread(s).

int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*startroutine)(void*), void *arg)[](#_CPPv414pthread_createP9pthread_tPK14pthread_attr_tPFPvPvEPv "永久链接至目标")
:   Thread creation.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EAGAIN** – - Insufficient memory for either thread structure or task creation.

int pthread_cond_broadcast(pthread_cond_t *cond)[](#_CPPv422pthread_cond_broadcastP14pthread_cond_t "永久链接至目标")
:   Broadcast a condition.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_broadcast.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_cond_destroy(pthread_cond_t *cond)[](#_CPPv420pthread_cond_destroyP14pthread_cond_t "永久链接至目标")
:   Destroy condition variables.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_destroy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_destroy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_destroy.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_cond_init(pthread_cond_t *cond, const pthread_condattr_t *attr)[](#_CPPv417pthread_cond_initP14pthread_cond_tPK18pthread_condattr_t "永久链接至目标")
:   Initialize condition variables.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_init.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_init.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_init.html")

    备注

    attr is ignored and treated as NULL. Default setting is always used.

    Return values
    :   - **0** – - Upon successful completion.

        - **ENOMEM** – - Insufficient memory exists to initialize the condition variable.

int pthread_cond_signal(pthread_cond_t *cond)[](#_CPPv419pthread_cond_signalP14pthread_cond_t "永久链接至目标")
:   Signal a condition.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_signal.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_signal.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_signal.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_cond_timedwait(pthread_cond_t *cond, pthread_mutex_t *mutex, const struct [timespec](time.html#_CPPv48timespec "timespec") *abstime)[](#_CPPv422pthread_cond_timedwaitP14pthread_cond_tP15pthread_mutex_tPK8timespec "永久链接至目标")
:   Wait on a condition with a timeout.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_timedwait.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The abstime argument passed in does not refer to an initialized structure OR the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

        - **ETIMEDOUT** – - The time specified by abstime to [pthread_cond_timedwait()](#pthread_8h_1ab03e3ab6546f661d2b2f83bc12559e40 "#pthread_8h_1ab03e3ab6546f661d2b2f83bc12559e40") has passed.

int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)[](#_CPPv417pthread_cond_waitP14pthread_cond_tP15pthread_mutex_t "永久链接至目标")
:   Wait on a condition.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_cond_wait.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_equal(pthread_t t1, pthread_t t2)[](#_CPPv413pthread_equal9pthread_t9pthread_t "永久链接至目标")
:   Compare thread IDs.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_equal.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_equal.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_equal.html")

    Return values
    :   - **0** – - t1 and t2 are both not NULL && equal.

        - **non-zero** – - otherwise.

void pthread_exit(void *value_ptr)[](#_CPPv412pthread_exitPv "永久链接至目标")
:   Thread termination.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html")

    Return values
    :   **void** – - this function cannot return to its caller.

int pthread_getschedparam(pthread_t thread, int *policy, struct [sched_param](sched.html#_CPPv411sched_param "sched_param") *param)[](#_CPPv421pthread_getschedparam9pthread_tPiP11sched_param "永久链接至目标")
:   Dynamic thread scheduling parameters access.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_getschedparam.html")

    备注

    policy is always set to SCHED_OTHER by this function.

    Return values
    :   **0** – - Upon successful completion.

int pthread_join(pthread_t thread, void **retval)[](#_CPPv412pthread_join9pthread_tPPv "永久链接至目标")
:   Wait for thread termination.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EDEADLK** – - The value specified by the thread argument to [pthread_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b "#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b") does not refer to a joinable thread OR multiple simultaneous calls to [pthread_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b "#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b") specifying the same target thread OR the value specified by the thread argument to [pthread_join()](#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b "#pthread_8h_1a28a15bba47cab57cbc9f5dac9af99c8b") refers to the calling thread.

int pthread_mutex_destroy(pthread_mutex_t *mutex)[](#_CPPv421pthread_mutex_destroyP15pthread_mutex_t "永久链接至目标")
:   Destroy a mutex.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_destroy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_destroy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_destroy.html")

    备注

    If there exists a thread holding this mutex, this function returns 0 with mutex not being destroyed.

    Return values
    :   **0** – - Upon successful completion.

int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr)[](#_CPPv418pthread_mutex_initP15pthread_mutex_tPK19pthread_mutexattr_t "永久链接至目标")
:   Initialize a mutex.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_init.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **ENOMEM** – - Insufficient memory exists to initialize the mutex structure.

        - **EAGAIN** – - Unable to initialize the mutex structure member(s).

int pthread_mutex_lock(pthread_mutex_t *mutex)[](#_CPPv418pthread_mutex_lockP15pthread_mutex_t "永久链接至目标")
:   Lock a mutex.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

        - **EDEADLK** – - The mutex type is PTHREAD_MUTEX_ERRORCHECK and the current thread already owns the mutex.

int pthread_mutex_timedlock(pthread_mutex_t *mutex, const struct [timespec](time.html#_CPPv48timespec "timespec") *abstime)[](#_CPPv423pthread_mutex_timedlockP15pthread_mutex_tPK8timespec "永久链接至目标")
:   Lock a mutex with timeout.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_timedlock.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The abstime argument passed in does not refer to an initialized structure OR the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

        - **EDEADLK** – - The mutex type is PTHREAD_MUTEX_ERRORCHECK and the current thread already owns the mutex.

        - **ETIMEDOUT** – - The mutex could not be locked before the specified timeout expired.

int pthread_mutex_trylock(pthread_mutex_t *mutex)[](#_CPPv421pthread_mutex_trylockP15pthread_mutex_t "永久链接至目标")
:   Attempt to lock a mutex. Fail immediately if mutex is already locked.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_trylock.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_trylock.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_trylock.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - the abstime parameter specified a nanoseconds field value less than zero or greater than or equal to 1000 million.

        - **EDEADLK** – - The mutex type is PTHREAD_MUTEX_ERRORCHECK and the current thread already owns the mutex.

        - **EBUSY** – - The mutex could not be acquired because it was already locked.

int pthread_mutex_unlock(pthread_mutex_t *mutex)[](#_CPPv420pthread_mutex_unlockP15pthread_mutex_t "永久链接至目标")
:   Unlock a mutex.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_unlock.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_unlock.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_unlock.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EPERM** – - The mutex type is PTHREAD_MUTEX_ERRORCHECK or PTHREAD_MUTEX_RECURSIVE, and the current thread does not own the mutex.

int pthread_mutexattr_destroy(pthread_mutexattr_t *attr)[](#_CPPv425pthread_mutexattr_destroyP19pthread_mutexattr_t "永久链接至目标")
:   Destroy the mutex attributes object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_destroy.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_destroy.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_destroy.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_mutexattr_gettype(const pthread_mutexattr_t *attr, int *type)[](#_CPPv425pthread_mutexattr_gettypePK19pthread_mutexattr_tPi "永久链接至目标")
:   Get the mutex type attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_gettype.html")

    Return values
    :   **0** – - Upon successful completion.

int pthread_mutexattr_init(pthread_mutexattr_t *attr)[](#_CPPv422pthread_mutexattr_initP19pthread_mutexattr_t "永久链接至目标")
:   Initialize the mutex attributes object.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_init.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_init.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_init.html")

    备注

    Currently, only the type attribute is supported. Also see [pthread_mutexattr_settype()](#pthread_8h_1a8387c80e660e9426f801ac0217ecfae5 "#pthread_8h_1a8387c80e660e9426f801ac0217ecfae5") and [pthread_mutexattr_gettype()](#pthread_8h_1a7f064a4db96a009a5a9a7c7e5cc03599 "#pthread_8h_1a7f064a4db96a009a5a9a7c7e5cc03599").

    Return values
    :   **0** – - Upon successful completion.

int pthread_mutexattr_settype(pthread_mutexattr_t *attr, int type)[](#_CPPv425pthread_mutexattr_settypeP19pthread_mutexattr_ti "永久链接至目标")
:   Set the mutex type attribute.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_settype.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_settype.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_settype.html")

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The value type is invalid.

pthread_t pthread_self(void)[](#_CPPv412pthread_selfv "永久链接至目标")
:   Get the calling thread ID.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_self.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_self.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_self.html")

    Return values
    :   **the** – thread ID of the calling thread.

int pthread_setschedparam(pthread_t thread, int policy, const struct [sched_param](sched.html#_CPPv411sched_param "sched_param") *param)[](#_CPPv421pthread_setschedparam9pthread_tiPK11sched_param "永久链接至目标")
:   Dynamic thread scheduling parameters access.

    参见

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedparam.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedparam.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_setschedparam.html")

    备注

    policy is ignored; only priority (param.sched_priority) may be changed.

    Return values
    :   **0** – - Upon successful completion.


## Macros[](#macros "永久链接至标题")

PTHREAD_CREATE_DETACHED[](#c.PTHREAD_CREATE_DETACHED "永久链接至目标")
:   Detached.

PTHREAD_CREATE_JOINABLE[](#c.PTHREAD_CREATE_JOINABLE "永久链接至目标")
:   Joinable (default).

PTHREAD_BARRIER_SERIAL_THREAD[](#c.PTHREAD_BARRIER_SERIAL_THREAD "永久链接至目标")

PTHREAD_MUTEX_NORMAL[](#c.PTHREAD_MUTEX_NORMAL "永久链接至目标")
:   Non-robust, deadlock on relock, does not remember owner.

PTHREAD_MUTEX_ERRORCHECK[](#c.PTHREAD_MUTEX_ERRORCHECK "永久链接至目标")
:   Non-robust, error on relock, remembers owner.

PTHREAD_MUTEX_RECURSIVE[](#c.PTHREAD_MUTEX_RECURSIVE "永久链接至目标")
:   Non-robust, recursive relock, remembers owner.

PTHREAD_MUTEX_DEFAULT[](#c.PTHREAD_MUTEX_DEFAULT "永久链接至目标")
:   PTHREAD_MUTEX_NORMAL (default).
