# OS API[](#os-api "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/system/os.html "../../../../en/v1.5/api-reference/system/os.html")

> - OS抽象层主要为了适配Armino平台不同的操作系统
> - 对于不同的操作系统，OS抽象层对外提供一套统一的接口
> - 目前Armino平台OS抽象层支持的操作系统有FreeRTOS，鸿蒙OS，RTThread.


## Header File[](#header-file "永久链接至标题")


- [os.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/os.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/os.h")


## Functions[](#functions "永久链接至标题")

void rtos_enter_critical(void)[](#_CPPv419rtos_enter_criticalv "永久链接至目标")
:   Enter a critical session, all interrupts are disabled.

    返回
    :   none

void rtos_exit_critical(void)[](#_CPPv418rtos_exit_criticalv "永久链接至目标")
:   Exit a critical session, all interrupts are enabled.

    返回
    :   none

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") beken_time_get_time([beken_time_t](#_CPPv412beken_time_t "beken_time_t") *time_ptr)[](#_CPPv419beken_time_get_timeP12beken_time_t "永久链接至目标")
:   Get system time value in milliseconds.

    参数
    :   **time_ptr** – : the pointer of time value in milliseconds

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_create_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread, uint8_t priority, const char *name, [beken_thread_function_t](#_CPPv423beken_thread_function_t "beken_thread_function_t") function, uint32_t stack_size, [beken_thread_arg_t](#_CPPv418beken_thread_arg_t "beken_thread_arg_t") arg)[](#_CPPv418rtos_create_threadP14beken_thread_t7uint8_tPKc23beken_thread_function_t8uint32_t18beken_thread_arg_t "永久链接至目标")
:   Creates and starts a new thread.

    参数
    :   - **thread** – : Pointer to variable that will receive the thread handle (can be null)

        - **priority** – : A priority number.

        - **name** – : a text name for the thread (can be null)

        - **function** – : the main thread function

        - **stack_size** – : stack size for this thread

        - **arg** – : argument which will be passed to thread function

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_delete_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv418rtos_delete_threadP14beken_thread_t "永久链接至目标")
:   Deletes a terminated thread.

    参数
    :   **thread** – : the handle of the thread to delete, , NULL is the current thread

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_create_worker_thread([beken_worker_thread_t](#_CPPv421beken_worker_thread_t "beken_worker_thread_t") *worker_thread, uint8_t priority, uint32_t stack_size, uint32_t event_queue_size)[](#_CPPv425rtos_create_worker_threadP21beken_worker_thread_t7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Creates a worker thread.

    Creates a worker thread A worker thread is a thread in whose context timed and asynchronous events execute.

    参数
    :   - **worker_thread** – : a pointer to the worker thread to be created

        - **priority** – : thread priority

        - **stack_size** – : thread’s stack size in number of bytes

        - **event_queue_size** – : number of events can be pushed into the queue

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_delete_worker_thread([beken_worker_thread_t](#_CPPv421beken_worker_thread_t "beken_worker_thread_t") *worker_thread)[](#_CPPv425rtos_delete_worker_threadP21beken_worker_thread_t "永久链接至目标")
:   Deletes a worker thread.

    参数
    :   **worker_thread** – : a pointer to the worker thread to be created

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

void rtos_suspend_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv419rtos_suspend_threadP14beken_thread_t "永久链接至目标")
:   Suspend a thread.

    参数
    :   **thread** – : the handle of the thread to suspend, NULL is the current thread

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

void rtos_suspend_all_thread(void)[](#_CPPv423rtos_suspend_all_threadv "永久链接至目标")
:   Suspend all other thread.

    参数
    :   **none** –

    返回
    :   none

void rtos_resume_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv418rtos_resume_threadP14beken_thread_t "永久链接至目标")
:   resume a thread

    参数
    :   **thread** – : the handle of the thread to resume, NULL is the current thread

    返回
    :   none

long rtos_resume_all_thread(void)[](#_CPPv422rtos_resume_all_threadv "永久链接至目标")
:   Rresume all other thread.

    参数
    :   **none** –

    返回
    :   none

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_thread_join([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv416rtos_thread_joinP14beken_thread_t "永久链接至目标")
:   Sleeps until another thread has terminated.

    Causes the current thread to sleep until the specified other thread has terminated. If the processor is heavily loaded with higher priority tasks, this thread may not wake until significantly after the thread termination.

    参数
    :   **thread** – : the handle of the other thread which will terminate

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_thread_force_awake([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv423rtos_thread_force_awakeP14beken_thread_t "永久链接至目标")
:   Forcibly wakes another thread.

    Causes the specified thread to wake from suspension. This will usually cause an error or timeout in that thread, since the task it was waiting on is not complete.

    参数
    :   **thread** – : the handle of the other thread which will be woken

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

bool rtos_is_current_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv422rtos_is_current_threadP14beken_thread_t "永久链接至目标")
:   Checks if a thread is the current thread.

    Checks if a specified thread is the currently running thread

    参数
    :   **thread** – : the handle of the other thread against which the current thread will be compared

    返回
    :   true : specified thread is the current thread

        false : specified thread is not currently running

[beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *rtos_get_current_thread(void)[](#_CPPv423rtos_get_current_threadv "永久链接至目标")
:   Get current thread handler.

    返回
    :   Current RTOS thread handler

void rtos_thread_sleep(uint32_t seconds)[](#_CPPv417rtos_thread_sleep8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    参数
    :   **seconds** – : A time interval (Unit: seconds)

    返回
    :   None.

void rtos_thread_msleep(uint32_t milliseconds)[](#_CPPv418rtos_thread_msleep8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    参数
    :   **milliseconds** – : A time interval (Unit: millisecond)

    返回
    :   None.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_delay_milliseconds(uint32_t num_ms)[](#_CPPv423rtos_delay_milliseconds8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    参数
    :   **num_ms** – : A time interval (Unit: millisecond)

    返回
    :   kNoErr.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_print_thread_status(char *buffer, int length)[](#_CPPv424rtos_print_thread_statusPci "永久链接至目标")
:   Print Thread status into buffer.

    参数
    :   - **buffer, point** – to buffer to store thread status

        - **length, length** – of the buffer

    返回
    :   none

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, int max_count)[](#_CPPv419rtos_init_semaphoreP17beken_semaphore_ti "永久链接至目标")
:   Initialises a counting semaphore and set count to 0.

    参数
    :   - **semaphore** – : a pointer to the semaphore handle to be initialised

        - **max_count** – : the max count number of this semaphore

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_semaphore_ex([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, int max_count, int init_count)[](#_CPPv422rtos_init_semaphore_exP17beken_semaphore_tii "永久链接至目标")
:   Initialises a counting semaphore and set count to init count.

    参数
    :   - **semaphore** – : a pointer to the semaphore handle to be initialised

        - **max_count** – : the max count number of this semaphore

        - **init_count** – : the init count number of this semaphore

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_set_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv418rtos_set_semaphoreP17beken_semaphore_t "永久链接至目标")
:   Set (post/put/increment) a semaphore.

    参数
    :   **semaphore** – : a pointer to the semaphore handle to be set

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_get_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, uint32_t timeout_ms)[](#_CPPv418rtos_get_semaphoreP17beken_semaphore_t8uint32_t "永久链接至目标")
:   Get (wait/decrement) a semaphore.

    Attempts to get (wait/decrement) a semaphore. If semaphore is at zero already, then the calling thread will be suspended until another thread sets the semaphore with [rtos_set_semaphore](#group__BEKEN__RTOS__SEM_1ga4e132dc329ec2d651aa543928f6a5313 "#group__BEKEN__RTOS__SEM_1ga4e132dc329ec2d651aa543928f6a5313")

    参数
    :   - **semaphore** – : a pointer to the semaphore handle

        - **timeout_ms, :** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

int rtos_get_semaphore_count([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv424rtos_get_semaphore_countP17beken_semaphore_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv421rtos_deinit_semaphoreP17beken_semaphore_t "永久链接至目标")
:   De-initialise a semaphore.

    Deletes a semaphore created with [rtos_init_semaphore](#group__BEKEN__RTOS__SEM_1gab8c99e1fa5c54d1759c538ca78de93a5 "#group__BEKEN__RTOS__SEM_1gab8c99e1fa5c54d1759c538ca78de93a5")

    参数
    :   **semaphore** – : a pointer to the semaphore handle

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv415rtos_init_mutexP13beken_mutex_t "永久链接至目标")
:   Initialises a mutex.

    A mutex is different to a semaphore in that a thread that already holds the lock on the mutex can request the lock again (nested) without causing it to be suspended.

    参数
    :   **mutex** – : a pointer to the mutex handle to be initialised

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_trylock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv418rtos_trylock_mutexP13beken_mutex_t "永久链接至目标")
:   Obtains the lock on a mutex.

    Attempts to obtain the lock on a mutex. If the lock is already held by another thead, the calling thread will not be suspended until the mutex lock is released by the other thread.

    参数
    :   **mutex** – : a pointer to the mutex handle to be locked

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_lock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv415rtos_lock_mutexP13beken_mutex_t "永久链接至目标")
:   Obtains the lock on a mutex.

    Attempts to obtain the lock on a mutex. If the lock is already held by another thead, the calling thread will be suspended until the mutex lock is released by the other thread.

    参数
    :   **mutex** – : a pointer to the mutex handle to be locked

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_unlock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv417rtos_unlock_mutexP13beken_mutex_t "永久链接至目标")
:   Releases the lock on a mutex.

    Releases a currently held lock on a mutex. If another thread is waiting on the mutex lock, then it will be resumed.

    参数
    :   **mutex** – : a pointer to the mutex handle to be unlocked

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv417rtos_deinit_mutexP13beken_mutex_t "永久链接至目标")
:   De-initialise a mutex.

    Deletes a mutex created with [rtos_init_mutex](#group__BEKEN__RTOS__MUTEX_1ga206c1b0aebb6431a6407373e921b2486 "#group__BEKEN__RTOS__MUTEX_1ga206c1b0aebb6431a6407373e921b2486")

    参数
    :   **mutex** – : a pointer to the mutex handle

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, const char *name, uint32_t message_size, uint32_t number_of_messages)[](#_CPPv415rtos_init_queueP13beken_queue_tPKc8uint32_t8uint32_t "永久链接至目标")
:   Initialises a FIFO queue.

    参数
    :   - **queue** – : a pointer to the queue handle to be initialised

        - **name** – : a text string name for the queue (NULL is allowed)

        - **message_size** – : size in bytes of objects that will be held in the queue

        - **number_of_messages** – : depth of the queue - i.e. max number of objects in the queue

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_push_to_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv418rtos_push_to_queueP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Pushes an object onto a queue.

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : the object to be added to the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3")

        - **timeout_ms, :** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_push_to_queue_front([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv424rtos_push_to_queue_frontP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Pushes an object to front of the queue.

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : the object to be added to the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3")

        - **timeout_ms, :** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_pop_from_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv419rtos_pop_from_queueP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Pops an object off a queue.

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : pointer to a buffer that will receive the object being popped off the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3") , hence you must ensure the buffer is long enough or memory corruption will result

        - **timeout_ms, :** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv417rtos_deinit_queueP13beken_queue_t "永久链接至目标")
:   De-initialise a queue created with [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3").

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

bool rtos_is_queue_empty([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv419rtos_is_queue_emptyP13beken_queue_t "永久链接至目标")
:   Check if a queue is empty.

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   true : queue is empty.

        false : queue is not empty.

bool rtos_is_queue_full([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv418rtos_is_queue_fullP13beken_queue_t "永久链接至目标")
:   Check if a queue is full.

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   true : queue is empty.

        false : queue is not empty.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_send_asynchronous_event([beken_worker_thread_t](#_CPPv421beken_worker_thread_t "beken_worker_thread_t") *worker_thread, [event_handler_t](#_CPPv415event_handler_t "event_handler_t") function, void *arg)[](#_CPPv428rtos_send_asynchronous_eventP21beken_worker_thread_t15event_handler_tPv "永久链接至目标")
:   Sends an asynchronous event to the associated worker thread.

    参数
    :   - **worker_thread** – :the worker thread in which context the callback should execute from

        - **function** – : the callback function to be called from the worker thread

        - **arg** – : the argument to be passed to the callback function

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_register_timed_event([beken_timed_event_t](#_CPPv419beken_timed_event_t "beken_timed_event_t") *event_object, [beken_worker_thread_t](#_CPPv421beken_worker_thread_t "beken_worker_thread_t") *worker_thread, [event_handler_t](#_CPPv415event_handler_t "event_handler_t") function, uint32_t time_ms, void *arg)[](#_CPPv425rtos_register_timed_eventP19beken_timed_event_tP21beken_worker_thread_t15event_handler_t8uint32_tPv "永久链接至目标")
:   Requests a function be called at a regular interval

    This function registers a function that will be called at a regular interval. Since this is based on the RTOS time-slice scheduling, the accuracy is not high, and is affected by processor load.

    参数
    :   - **event_object** – : pointer to a event handle which will be initialised

        - **worker_thread** – : pointer to the worker thread in whose context the callback function runs on

        - **function** – : the callback function that is to be called regularly

        - **time_ms** – : the time period between function calls in milliseconds

        - **arg** – : an argument that will be supplied to the function when it is called

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deregister_timed_event([beken_timed_event_t](#_CPPv419beken_timed_event_t "beken_timed_event_t") *event_object)[](#_CPPv427rtos_deregister_timed_eventP19beken_timed_event_t "永久链接至目标")
:   Removes a request for a regular function execution

    This function de-registers a function that has previously been set-up with [rtos_register_timed_event](#group__BEKEN__RTOS__EVENT_1ga3287395f5f095626b02142c76aff36e7 "#group__BEKEN__RTOS__EVENT_1ga3287395f5f095626b02142c76aff36e7").

    参数
    :   **event_object** – : the event handle used with [rtos_register_timed_event](#group__BEKEN__RTOS__EVENT_1ga3287395f5f095626b02142c76aff36e7 "#group__BEKEN__RTOS__EVENT_1ga3287395f5f095626b02142c76aff36e7")

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

uint32_t rtos_get_time(void)[](#_CPPv413rtos_get_timev "永久链接至目标")
:   Gets time in miiliseconds since RTOS start.

    备注

    : Since this is only 32 bits, it will roll over every 49 days, 17 hours.

    返回
    :   Time in milliseconds since RTOS started.

uint32_t beken_ms_per_tick(void)[](#_CPPv417beken_ms_per_tickv "永久链接至目标")
:   Gets time in miiliseconds since RTOS start.

    备注

    : Since this is only 32 bits, it will roll over every 49 days, 17 hours.

    返回
    :   Time in milliseconds since RTOS started.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer, uint32_t time_ms, [timer_handler_t](#_CPPv415timer_handler_t "timer_handler_t") function, void *arg)[](#_CPPv415rtos_init_timerP13beken_timer_t8uint32_t15timer_handler_tPv "永久链接至目标")
:   Initialize a RTOS timer.

    备注

    Timer does not start running until beken_start_timer is called

    参数
    :   - **timer** – : a pointer to the timer handle to be initialised

        - **time_ms** – : Timer period in milliseconds

        - **function** – : the callback handler function that is called each time the timer expires

        - **arg** – : an argument that will be passed to the callback function

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer, uint32_t time_ms, [timer_2handler_t](#_CPPv416timer_2handler_t "timer_2handler_t") function, void *larg, void *rarg)[](#_CPPv423rtos_init_oneshot_timerP14beken2_timer_t8uint32_t16timer_2handler_tPvPv "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv425rtos_deinit_oneshot_timerP14beken2_timer_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_stop_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv423rtos_stop_oneshot_timerP14beken2_timer_t "永久链接至目标")

bool rtos_is_oneshot_timer_running([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv429rtos_is_oneshot_timer_runningP14beken2_timer_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_start_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv424rtos_start_oneshot_timerP14beken2_timer_t "永久链接至目标")

bool rtos_is_oneshot_timer_init([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv426rtos_is_oneshot_timer_initP14beken2_timer_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_oneshot_reload_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv425rtos_oneshot_reload_timerP14beken2_timer_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_change_period([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer, uint32_t time_ms)[](#_CPPv418rtos_change_periodP13beken_timer_t8uint32_t "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_oneshot_reload_timer_ex([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer, uint32_t time_ms, [timer_2handler_t](#_CPPv416timer_2handler_t "timer_2handler_t") function, void *larg, void *rarg)[](#_CPPv428rtos_oneshot_reload_timer_exP14beken2_timer_t8uint32_t16timer_2handler_tPvPv "永久链接至目标")

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_start_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv416rtos_start_timerP13beken_timer_t "永久链接至目标")
:   Starts a RTOS timer running.

    备注

    Timer must have been previously initialised with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de")

    参数
    :   **timer** – : a pointer to the timer handle to start

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_stop_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv415rtos_stop_timerP13beken_timer_t "永久链接至目标")
:   Stops a running RTOS timer.

    备注

    Timer must have been previously started with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de")

    参数
    :   **timer** – : a pointer to the timer handle to stop

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_reload_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv417rtos_reload_timerP13beken_timer_t "永久链接至目标")
:   Reloads a RTOS timer that has expired.

    备注

    This is usually called in the timer callback handler, to reschedule the timer for the next period.

    参数
    :   **timer** – : a pointer to the timer handle to reload

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv417rtos_deinit_timerP13beken_timer_t "永久链接至目标")
:   De-initialise a RTOS timer.

    备注

    Deletes a RTOS timer created with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de")

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

        kGeneralErr : if an error occurred

bool rtos_is_timer_init([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv418rtos_is_timer_initP13beken_timer_t "永久链接至目标")
:   Check if an RTOS timer is init.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if init.

        false : if not init

bool rtos_is_timer_running([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv421rtos_is_timer_runningP13beken_timer_t "永久链接至目标")
:   Check if an RTOS timer is running.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if running.

        false : if not running

uint32_t rtos_get_timer_expiry_time([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv426rtos_get_timer_expiry_timeP13beken_timer_t "永久链接至目标")

uint32_t rtos_get_next_expire_time()[](#_CPPv425rtos_get_next_expire_timev "永久链接至目标")

uint32_t rtos_get_current_timer_count(void)[](#_CPPv428rtos_get_current_timer_countv "永久链接至目标")

void rtos_start_scheduler(void)[](#_CPPv420rtos_start_schedulerv "永久链接至目标")

bool rtos_is_scheduler_started(void)[](#_CPPv425rtos_is_scheduler_startedv "永久链接至目标")

uint32_t rtos_get_cpsr(void)[](#_CPPv413rtos_get_cpsrv "永久链接至目标")

char *rtos_get_name(void)[](#_CPPv413rtos_get_namev "永久链接至目标")

char *rtos_get_version(void)[](#_CPPv416rtos_get_versionv "永久链接至目标")

size_t rtos_get_total_heap_size(void)[](#_CPPv424rtos_get_total_heap_sizev "永久链接至目标")

size_t rtos_get_free_heap_size(void)[](#_CPPv423rtos_get_free_heap_sizev "永久链接至目标")

size_t rtos_get_minimum_free_heap_size(void)[](#_CPPv431rtos_get_minimum_free_heap_sizev "永久链接至目标")

size_t rtos_get_psram_total_heap_size(void)[](#_CPPv430rtos_get_psram_total_heap_sizev "永久链接至目标")

size_t rtos_get_psram_free_heap_size(void)[](#_CPPv429rtos_get_psram_free_heap_sizev "永久链接至目标")

size_t rtos_get_psram_minimum_free_heap_size(void)[](#_CPPv437rtos_get_psram_minimum_free_heap_sizev "永久链接至目标")

uint32_t rtos_get_tick_count(void)[](#_CPPv419rtos_get_tick_countv "永久链接至目标")

uint32_t rtos_disable_int(void)[](#_CPPv416rtos_disable_intv "永久链接至目标")

void rtos_enable_int(uint32_t int_level)[](#_CPPv415rtos_enable_int8uint32_t "永久链接至目标")

uint32_t rtos_before_sleep(void)[](#_CPPv417rtos_before_sleepv "永久链接至目标")

void rtos_after_sleep(uint32_t int_level)[](#_CPPv416rtos_after_sleep8uint32_t "永久链接至目标")

bool rtos_is_in_interrupt_context(void)[](#_CPPv428rtos_is_in_interrupt_contextv "永久链接至目标")

void rtos_wait_for_interrupt(void)[](#_CPPv423rtos_wait_for_interruptv "永久链接至目标")

void rtos_shutdown(void)[](#_CPPv413rtos_shutdownv "永久链接至目标")

uint32_t rtos_disable_mie_int(void)[](#_CPPv420rtos_disable_mie_intv "永久链接至目标")
:   save the state of the MIE and then disable the plic,plmt,plic_sw in mie

    参数
    :   **void** –

    返回
    :   the state of the MIE

void rtos_enable_mie_int(uint32_t int_level)[](#_CPPv419rtos_enable_mie_int8uint32_t "永久链接至目标")
:   enable the MIE using the saving the state of the mie

    参数
    :   **int_level** – : the saving the state of the mie

    返回
    :   void


## Structures[](#structures "永久链接至标题")

struct beken_timer_t[](#_CPPv413beken_timer_t "永久链接至目标")
:   OS timer handle struct type.

    Public Members

    void *handle[](#_CPPv4N13beken_timer_t6handleE "永久链接至目标")
    :   OS timer handle pointer

    [timer_handler_t](#_CPPv415timer_handler_t "timer_handler_t") function[](#_CPPv4N13beken_timer_t8functionE "永久链接至目标")
    :   OS timer handle callback function

    void *arg[](#_CPPv4N13beken_timer_t3argE "永久链接至目标")
    :   OS timer handle callback argument

struct beken_worker_thread_t[](#_CPPv421beken_worker_thread_t "永久链接至目标")
:   OS worker thread handle struct type.

    Public Members

    [beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") thread[](#_CPPv4N21beken_worker_thread_t6threadE "永久链接至目标")
    :   OS thread handle

    [beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") event_queue[](#_CPPv4N21beken_worker_thread_t11event_queueE "永久链接至目标")
    :   OS event queue

struct beken_timed_event_t[](#_CPPv419beken_timed_event_t "永久链接至目标")
:   OS timer event struct type.

    Public Members

    [event_handler_t](#_CPPv415event_handler_t "event_handler_t") function[](#_CPPv4N19beken_timed_event_t8functionE "永久链接至目标")
    :   OS event callback function

    void *arg[](#_CPPv4N19beken_timed_event_t3argE "永久链接至目标")
    :   OS event callback argument

    [beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") timer[](#_CPPv4N19beken_timed_event_t5timerE "永久链接至目标")
    :   OS timer handle

    [beken_worker_thread_t](#_CPPv421beken_worker_thread_t "beken_worker_thread_t") *thread[](#_CPPv4N19beken_timed_event_t6threadE "永久链接至目标")
    :   OS work thread handle

struct beken2_timer_t[](#_CPPv414beken2_timer_t "永久链接至目标")
:   OS timer handle struct type.

    Public Members

    void *handle[](#_CPPv4N14beken2_timer_t6handleE "永久链接至目标")
    :   OS timer handle pointer

    [timer_2handler_t](#_CPPv416timer_2handler_t "timer_2handler_t") function[](#_CPPv4N14beken2_timer_t8functionE "永久链接至目标")
    :   OS timer handle callback function

    void *left_arg[](#_CPPv4N14beken2_timer_t8left_argE "永久链接至目标")
    :   OS timer handle callback first argument

    void *right_arg[](#_CPPv4N14beken2_timer_t9right_argE "永久链接至目标")
    :   OS timer handle callback second argument

    uint32_t beken_magic[](#_CPPv4N14beken2_timer_t11beken_magicE "永久链接至目标")
    :   OS timer magic word


## Macros[](#macros "永久链接至标题")

RTOS_TAG[](#c.RTOS_TAG "永久链接至目标")
:   OS log tag

RTOS_LOGI(...)[](#c.RTOS_LOGI "永久链接至目标")
:   Output OS Info log

RTOS_LOGW(...)[](#c.RTOS_LOGW "永久链接至目标")
:   Output OS Warning log

RTOS_LOGE(...)[](#c.RTOS_LOGE "永久链接至目标")
:   Output OS Error log

RTOS_LOGD(...)[](#c.RTOS_LOGD "永久链接至目标")
:   Output OS Debug log

GLOBAL_INT_STOP[](#c.GLOBAL_INT_STOP "永久链接至目标")
:   os stop interrupt

GLOBAL_INT_DECLARATION()[](#c.GLOBAL_INT_DECLARATION "永久链接至目标")
:   os declaration interrupt status

GLOBAL_INT_DISABLE()[](#c.GLOBAL_INT_DISABLE "永久链接至目标")
:   os read interrupt status and disable interrupt

GLOBAL_INT_RESTORE()[](#c.GLOBAL_INT_RESTORE "永久链接至目标")
:   os restore interrupt status

RTOS_SUCCESS[](#c.RTOS_SUCCESS "永久链接至目标")
:   Return Success

RTOS_FAILURE[](#c.RTOS_FAILURE "永久链接至目标")
:   Return Failure

BEKEN_DEFAULT_WORKER_PRIORITY[](#c.BEKEN_DEFAULT_WORKER_PRIORITY "永久链接至目标")
:   Default Worker Priority

BEKEN_APPLICATION_PRIORITY[](#c.BEKEN_APPLICATION_PRIORITY "永久链接至目标")
:   Application Task Priority

NanosecondsPerSecond[](#c.NanosecondsPerSecond "永久链接至目标")
:   Nanoseconds Per Second

MicrosecondsPerSecond[](#c.MicrosecondsPerSecond "永久链接至目标")
:   Microseconds Per Second

MillisecondsPerSecond[](#c.MillisecondsPerSecond "永久链接至目标")
:   Milliseconds Per Second

BEKEN_NEVER_TIMEOUT[](#c.BEKEN_NEVER_TIMEOUT "永久链接至目标")
:   Never Timeout

BEKEN_WAIT_FOREVER[](#c.BEKEN_WAIT_FOREVER "永久链接至目标")
:   Wait Forever

BEKEN_NO_WAIT[](#c.BEKEN_NO_WAIT "永久链接至目标")
:   No Wait

NANOSECONDS[](#c.NANOSECONDS "永久链接至目标")
:   Nanoseconds Per Milliseconds

MICROSECONDS[](#c.MICROSECONDS "永久链接至目标")
:   Microseconds Per Milliseconds

MILLISECONDS[](#c.MILLISECONDS "永久链接至目标")
:   One Milliseconds

SECONDS[](#c.SECONDS "永久链接至目标")
:   Milliseconds Per Second

MINUTES[](#c.MINUTES "永久链接至目标")
:   Milliseconds Per MINUTES

HOURS[](#c.HOURS "永久链接至目标")
:   Milliseconds Per HOURS

DAYS[](#c.DAYS "永久链接至目标")
:   Milliseconds Per DAYS

BEKEN_MAGIC_WORD[](#c.BEKEN_MAGIC_WORD "永久链接至目标")
:   Beken Magic word

os_printf[](#c.os_printf "永久链接至目标")
:   OS printf, will be replace with RTOS_LOGI later

os_null_printf[](#c.os_null_printf "永久链接至目标")
:   OS drop print string

rtos_init_semaphore_adv[](#c.rtos_init_semaphore_adv "永久链接至目标")
:   To be replace with rtos_init_semaphore_ex

rtos_get_sema_count[](#c.rtos_get_sema_count "永久链接至目标")
:   To be replace with rtos_get_semaphore_count


## Type Definitions[](#type-definitions "永久链接至标题")

typedef int bk_err_t[](#_CPPv48bk_err_t "永久链接至目标")
:   Return error code

typedef void *beken_thread_arg_t[](#_CPPv418beken_thread_arg_t "永久链接至目标")
:   Thread argument pointer type

typedef uint8_t beken_bool_t[](#_CPPv412beken_bool_t "永久链接至目标")
:   Bool type

typedef uint32_t beken_time_t[](#_CPPv412beken_time_t "永久链接至目标")
:   Time value in milliseconds

typedef uint32_t beken_utc_time_t[](#_CPPv416beken_utc_time_t "永久链接至目标")
:   UTC Time in seconds

typedef uint64_t beken_utc_time_ms_t[](#_CPPv419beken_utc_time_ms_t "永久链接至目标")
:   UTC Time in milliseconds

typedef uint32_t beken_event_flags_t[](#_CPPv419beken_event_flags_t "永久链接至目标")
:   Event flag type

typedef void *beken_semaphore_t[](#_CPPv417beken_semaphore_t "永久链接至目标")
:   OS Semaphore handle pointer

typedef void *beken_mutex_t[](#_CPPv413beken_mutex_t "永久链接至目标")
:   OS Mutex handle pointer

typedef void *beken_thread_t[](#_CPPv414beken_thread_t "永久链接至目标")
:   OS Thread handle pointer

typedef void *beken_queue_t[](#_CPPv413beken_queue_t "永久链接至目标")
:   OS Queue handle pointer

typedef void *beken_event_t[](#_CPPv413beken_event_t "永久链接至目标")
:   OS Event handle pointer

typedef void (*timer_handler_t)(void*)[](#_CPPv415timer_handler_t "永久链接至目标")
:   timer callback function type with one parameter

typedef void (*timer_2handler_t)(void *Larg, void *Rarg)[](#_CPPv416timer_2handler_t "永久链接至目标")
:   timer callback function type with two parameters

typedef [bk_err_t](#_CPPv48bk_err_t "bk_err_t") (*event_handler_t)(void *arg)[](#_CPPv415event_handler_t "永久链接至目标")
:   event callback function type with one parameter

typedef void (*beken_thread_function_t)([beken_thread_arg_t](#_CPPv418beken_thread_arg_t "beken_thread_arg_t") arg)[](#_CPPv423beken_thread_function_t "永久链接至目标")
:   OS Thread entry function type.


## Enumerations[](#enumerations "永久链接至标题")

enum beken_event_flags_wait_option_t[](#_CPPv431beken_event_flags_wait_option_t "永久链接至目标")
:   OS Event wait options.


    *Values:*

    enumerator WAIT_FOR_ANY_EVENT[](#_CPPv4N31beken_event_flags_wait_option_t18WAIT_FOR_ANY_EVENTE "永久链接至目标")
    :   Wait for any event

    enumerator WAIT_FOR_ALL_EVENTS[](#_CPPv4N31beken_event_flags_wait_option_t19WAIT_FOR_ALL_EVENTSE "永久链接至目标")
    :   Wait for all event
