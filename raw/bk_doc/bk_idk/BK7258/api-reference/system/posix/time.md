# time接口介绍[](#time "永久链接至标题")

> - 需要包含头文件#include <posix/time.h>;
> - 定义了系统定时器相关的接口



## Header File[](#header-file "永久链接至标题")


- [time.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/time.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/time.h")


## Functions[](#functions "永久链接至标题")

clock_t clock(void)[](#_CPPv45clockv "永久链接至目标")
:   Report CPU time used.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock.html")

    备注

    This function does NOT report the number of ticks spent by the calling thread.

    返回
    :   The number of FreeRTOS ticks since the scheduler was started minus the ticks spent in the idle task.

int clock_getcpuclockid(pid_t pid, clockid_t *clock_id)[](#_CPPv419clock_getcpuclockid5pid_tP9clockid_t "永久链接至目标")
:   Access a process CPU-time clock.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getcpuclockid.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getcpuclockid.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getcpuclockid.html")

    备注

    This function is currently unsupported.

    Return values
    :   **EPERM** –

int clock_getres(clockid_t clock_id, struct [timespec](#_CPPv48timespec "timespec") *res)[](#_CPPv412clock_getres9clockid_tP8timespec "永久链接至目标")
:   Returns the resolution of a clock.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getres.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getres.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_getres.html")

    备注

    clock_id is ignored

    备注

    This function stores the resolution of the FreeRTOS tick count in the object res points to.

    Return values
    :   **0** – - Upon successful execution

int clock_gettime(clockid_t clock_id, struct [timespec](#_CPPv48timespec "timespec") *tp)[](#_CPPv413clock_gettime9clockid_tP8timespec "永久链接至目标")
:   Returns the current value for the specified clock, clock_id.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_gettime.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_gettime.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_gettime.html")

    备注

    clock_id is ignored

    备注

    this function does not check for overflows of time_t.

    Return values
    :   **0** – - Upon successful completion.

int clock_nanosleep(clockid_t clock_id, int flags, const struct [timespec](#_CPPv48timespec "timespec") *rqtp, struct [timespec](#_CPPv48timespec "timespec") *rmtp)[](#_CPPv415clock_nanosleep9clockid_tiPK8timespecP8timespec "永久链接至目标")
:   High resolution sleep with specifiable clock.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_nanosleep.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_nanosleep.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_nanosleep.html")

    备注

    clock_id is ignored, as this function uses the FreeRTOS tick count as its clock.

    备注

    flags is ignored, if INCLUDE_vTaskDelayUntil is 0. i.e. the FreeRTOS function vTaskDelayUntil isn’t available.

    备注

    rmtp is also ignored, as signals are not implemented.

    Return values
    :   - **0** – - Upon successful completion.

        - **EINVAL** – - The rqtp argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

int clock_settime(clockid_t clock_id, const struct [timespec](#_CPPv48timespec "timespec") *tp)[](#_CPPv413clock_settime9clockid_tPK8timespec "永久链接至目标")
:   Sets the time for the specified clock.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_settime.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_settime.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_settime.html")

    备注

    This function is currently unsupported, as FreeRTOS does not provide a function to modify the tick count.

    Return values
    :   **-1** – with errno set to EPERM.

int nanosleep(const struct [timespec](#_CPPv48timespec "timespec") *rqtp, struct [timespec](#_CPPv48timespec "timespec") *rmtp)[](#_CPPv49nanosleepPK8timespecP8timespec "永久链接至目标")
:   High resolution sleep.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/nanosleep.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/nanosleep.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/nanosleep.html")

    备注

    rmtp is ignored, as signals are not implemented.

    Return values
    :   - **0** – - Upon successful completion.

        - **-1** – - The rqtp argument is invalid OR the rqtp argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

int timer_create(clockid_t clockid, struct [sigevent](signal.md#_CPPv48sigevent "sigevent") *evp, timer_t *timerid)[](#_CPPv412timer_create9clockid_tP8sigeventP7timer_t "永久链接至目标")
:   Create a per-process timer.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_create.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_create.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_create.html")

    @sideeffect Possible errno values

    ENOTSUP - If evp is NULL OR evp->sigen_notify == SIGEV_SIGNAL.

    EAGAIN - The system lacks sufficient signal queuing resources to honor the request.

    备注

    clock_id is ignored, as this function used the FreeRTOS tick count as its clock.

    备注

    evp.sigev_notify must be set to SIGEV_THREAD, since signals are currently not supported.

    Return values
    :   - **0** – - Upon successful completion, with location referenced by timerid updated.

        - **-1** – - If an error occurs. errno is also set.

int timer_delete(timer_t timerid)[](#_CPPv412timer_delete7timer_t "永久链接至目标")
:   Delete a per-process timer.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_delete.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_delete.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_delete.html")

    Return values
    :   **0** – - Upon successful completion.

int timer_getoverrun(timer_t timerid)[](#_CPPv416timer_getoverrun7timer_t "永久链接至目标")
:   Get the timer overrun count.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_getoverrun.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_getoverrun.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_getoverrun.html")

    Return values
    :   **0** – - Always return 0, since signals are not supported.

int timer_gettime(timer_t timerid, struct [itimerspec](#_CPPv410itimerspec "itimerspec") *value)[](#_CPPv413timer_gettime7timer_tP10itimerspec "永久链接至目标")
:   Get the amount of time until the timer expires.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_gettime.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_gettime.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_gettime.html")

    Return values
    :   **0** – - Upon successful completion.

int timer_settime(timer_t timerid, int flags, const struct [itimerspec](#_CPPv410itimerspec "itimerspec") *value, struct [itimerspec](#_CPPv410itimerspec "itimerspec") *ovalue)[](#_CPPv413timer_settime7timer_tiPK10itimerspecP10itimerspec "永久链接至目标")
:   Set the time until the next expiration of the timer.

    [http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_settime.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_settime.html "http://pubs.opengroup.org/onlinepubs/9699919799/functions/timer_settime.html")

    @sideeffect Possible errno values

    EINVAL - A value structure specified a nanosecond value less than zero or greater than or equal to 1000 million, AND the it_value member of that structure did not specify zero seconds and nanoseconds.

    Return values
    :   - **0** – - Upon successful completion.

        - **-1** – - An error occurred, errno is also set.


## Structures[](#structures "永久链接至标题")

struct timespec[](#_CPPv48timespec "永久链接至目标")
:   represents an elapsed time

    Public Members

    time_t tv_sec[](#_CPPv4N8timespec6tv_secE "永久链接至目标")
    :   Seconds.

    long tv_nsec[](#_CPPv4N8timespec7tv_nsecE "永久链接至目标")
    :   Nanoseconds.

struct itimerspec[](#_CPPv410itimerspec "永久链接至目标")
:   timer

    Public Members

    struct [timespec](#_CPPv48timespec "timespec") it_interval[](#_CPPv4N10itimerspec11it_intervalE "永久链接至目标")
    :   Timer period.

    struct [timespec](#_CPPv48timespec "timespec") it_value[](#_CPPv4N10itimerspec8it_valueE "永久链接至目标")
    :   Timer expiration.


## Macros[](#macros "永久链接至标题")

MICROSECONDS_PER_SECOND[](#c.MICROSECONDS_PER_SECOND "永久链接至目标")
:   Microseconds per second.

NANOSECONDS_PER_SECOND[](#c.NANOSECONDS_PER_SECOND "永久链接至目标")
:   Nanoseconds per second.

NANOSECONDS_PER_TICK[](#c.NANOSECONDS_PER_TICK "永久链接至目标")
:   Nanoseconds per FreeRTOS tick.

CLOCK_REALTIME[](#c.CLOCK_REALTIME "永久链接至目标")
:   The identifier of the system-wide clock measuring real time.

CLOCK_MONOTONIC[](#c.CLOCK_MONOTONIC "永久链接至目标")
:   The identifier for the system-wide monotonic clock.

CLOCKS_PER_SEC[](#c.CLOCKS_PER_SEC "永久链接至目标")

TIMER_ABSTIME[](#c.TIMER_ABSTIME "永久链接至目标")
