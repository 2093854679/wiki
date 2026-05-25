# OS API[](#os-api "永久链接至标题")

[[English]](../../../../en/v2.0.1/api-reference/system/os.html "../../../../en/v2.0.1/api-reference/system/os.html")

> - OS抽象层主要为了适配Armino平台不同的操作系统
> - 对于不同的操作系统，OS抽象层对外提供一套统一的接口
> - 目前Armino平台OS抽象层支持的操作系统有FreeRTOS，鸿蒙OS，RTThread.


## Header File[](#header-file "永久链接至标题")


- [os.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/os.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/os.h")


## Functions[](#functions "永久链接至标题")

uint32_t rtos_enter_critical(void)[](#_CPPv419rtos_enter_criticalv "永久链接至目标")
:   Enter a critical session, all interrupts are disabled.

    返回
    :   irq flags

void rtos_exit_critical(uint32_t flags)[](#_CPPv418rtos_exit_critical8uint32_t "永久链接至目标")
:   Exit a critical session, all interrupts are enabled.

    参数
    :   **flags** – : irq flags

    返回
    :   none

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") beken_time_get_time([beken_time_t](#_CPPv412beken_time_t "beken_time_t") *time_ptr)[](#_CPPv419beken_time_get_timeP12beken_time_t "永久链接至目标")
:   Get system time value in milliseconds.

    参数
    :   **time_ptr** – : the pointer of time value in milliseconds

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_create_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread, uint8_t priority, const char *name, [beken_thread_function_t](#_CPPv423beken_thread_function_t "beken_thread_function_t") function, uint32_t stack_size, [beken_thread_arg_t](#_CPPv418beken_thread_arg_t "beken_thread_arg_t") arg)[](#_CPPv418rtos_create_threadP14beken_thread_t7uint8_tPKc23beken_thread_function_t8uint32_t18beken_thread_arg_t "永久链接至目标")
:   Creates and starts a new thread,the task will be dynamically created in sram.

    备注

    Do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **thread** – : Pointer to variable that will receive the thread handle (can be null)

        - **priority** – : A priority number. The adaptation layer uniformly managers priorities. For the application layer,the lower the configured number,the higher the task priority.Currently supports ten priority levels from 0 to 9. recommended that the application layer use priorities from 6 to 8.

        - **name** – : a text name for the thread (can be null)

        - **function** – : the main thread function

        - **stack_size** – : stack size for this thread,size is in bytes,for example if the stack_size is defined as 2048,then 2048bytes will be allocated for stack storage.

        - **arg** – : argument which will be passed to thread function

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_create_psram_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread, uint8_t priority, const char *name, [beken_thread_function_t](#_CPPv423beken_thread_function_t "beken_thread_function_t") function, uint32_t stack_size, [beken_thread_arg_t](#_CPPv418beken_thread_arg_t "beken_thread_arg_t") arg)[](#_CPPv424rtos_create_psram_threadP14beken_thread_t7uint8_tPKc23beken_thread_function_t8uint32_t18beken_thread_arg_t "永久链接至目标")
:   Creates and starts a new thread on psram.

    备注

    Do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **thread** – : Pointer to variable that will receive the thread handle (can be null)

        - **priority** – : A priority number.he adaptation layer uniformly managers priorities. For the application layer,the lower the configured number,the higher the task priority.Currently supports ten priority levels from 0 to 9. recommended that the application layer use priorities from 6 to 8.

        - **name** – : a text name for the thread (can be null)

        - **function** – : the main thread function

        - **stack_size** – : stack size for this thread,size is in bytes,for example if the stack_size is defined as 2048,then 2048bytes will be allocated for stack storage.

        - **arg** – : argument which will be passed to thread function

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_delete_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv418rtos_delete_threadP14beken_thread_t "永久链接至目标")
:   Deletes a terminated thread.

    备注

    If you want to delete the task itself,do not call this API when the interrupts is disables(may cause the system to enter a deadlock or abnormal status))

    参数
    :   **thread** – : the handle of the thread to delete, , NULL is the current thread

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

void rtos_suspend_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv419rtos_suspend_threadP14beken_thread_t "永久链接至目标")
:   Suspend a thread.

    备注

    If you want to suspend the task itself,do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **thread** – : the handle of the thread to suspend, NULL is the current thread

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

void rtos_suspend_all_thread(void)[](#_CPPv423rtos_suspend_all_threadv "永久链接至目标")
:   Suspend all other thread.

    参数
    :   **none** –

    返回
    :   none

void rtos_resume_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv418rtos_resume_threadP14beken_thread_t "永久链接至目标")
:   resume a thread

    备注

    If you want to resume the task not itself,do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **thread** – : the handle of the thread to resume, NULL is the current thread

    返回
    :   none

void rtos_resume_all_thread(void)[](#_CPPv422rtos_resume_all_threadv "永久链接至目标")
:   Rresume all other thread.

    参数
    :   **none** –

    返回
    :   none

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_thread_join([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv416rtos_thread_joinP14beken_thread_t "永久链接至目标")
:   Sleeps until another thread has terminated.

    @Details Causes the current thread to sleep until the specified other thread has terminated. If the processor is heavily loaded with higher priority tasks, this thread may not wake until significantly after the thread termination.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **thread** – : the handle of the other thread which will terminate

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_thread_force_awake([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv423rtos_thread_force_awakeP14beken_thread_t "永久链接至目标")
:   Forcibly wakes another thread.

    @Details Causes the specified thread to wake from suspension. This will usually cause an error or timeout in that thread, since the task it was waiting on is not complete.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **thread** – : the handle of the other thread which will be removed from the block state.

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

bool rtos_is_current_thread([beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *thread)[](#_CPPv422rtos_is_current_threadP14beken_thread_t "永久链接至目标")
:   Checks if a thread is the current thread.

    @Details Checks if a specified thread is the currently running thread

    参数
    :   **thread** – : the handle of the other thread against which the current thread will be compared

    返回
    :   true : specified thread is the current thread

    返回
    :   false : specified thread is not currently running

[beken_thread_t](#_CPPv414beken_thread_t "beken_thread_t") *rtos_get_current_thread(void)[](#_CPPv423rtos_get_current_threadv "永久链接至目标")
:   Get current thread handler.

    返回
    :   Current RTOS thread handler

void rtos_thread_sleep(uint32_t seconds)[](#_CPPv417rtos_thread_sleep8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **seconds** – : A time interval (Unit: seconds)

    返回
    :   None.

void rtos_thread_msleep(uint32_t milliseconds)[](#_CPPv418rtos_thread_msleep8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **milliseconds** – : A time interval (Unit: millisecond)

    返回
    :   None.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_delay_milliseconds(uint32_t num_ms)[](#_CPPv423rtos_delay_milliseconds8uint32_t "永久链接至目标")
:   Suspend current thread for a specific time.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **num_ms** – : A time interval (Unit: millisecond)

    返回
    :   kNoErr.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, int max_count)[](#_CPPv419rtos_init_semaphoreP17beken_semaphore_ti "永久链接至目标")
:   Initialises a counting semaphore and set count to 0.

    参数
    :   - **semaphore** – : a pointer to the semaphore handle to be initialised

        - **max_count** – : the max count number of this semaphore

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_semaphore_ex([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, int max_count, int init_count)[](#_CPPv422rtos_init_semaphore_exP17beken_semaphore_tii "永久链接至目标")
:   Initialises a counting semaphore and set count to init count.

    参数
    :   - **semaphore** – : a pointer to the semaphore handle to be initialised

        - **max_count** – : the max count number of this semaphore

        - **init_count** – : the init count number of this semaphore

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_set_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv418rtos_set_semaphoreP17beken_semaphore_t "永久链接至目标")
:   Set (post/put/increment) a semaphore.

    备注

    This API can be called in task context and interrupt context.

    参数
    :   **semaphore** – : a pointer to the semaphore handle to be set

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_get_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore, uint32_t timeout_ms)[](#_CPPv418rtos_get_semaphoreP17beken_semaphore_t8uint32_t "永久链接至目标")
:   Get (wait/decrement) a semaphore.

    @Details Attempts to get (wait/decrement) a semaphore. If semaphore is at zero already, then the calling thread will be suspended until another thread sets the semaphore with [rtos_set_semaphore](#group__BEKEN__RTOS__SEM_1ga4e132dc329ec2d651aa543928f6a5313 "#group__BEKEN__RTOS__SEM_1ga4e132dc329ec2d651aa543928f6a5313")

    备注

    Do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **semaphore** – : a pointer to the semaphore handle

        - **timeout_ms** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

int rtos_get_semaphore_count([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv424rtos_get_semaphore_countP17beken_semaphore_t "永久链接至目标")
:   get current semaphore count

    参数
    :   **semaphore** – : a pointer to the semaphore handle to be set

    返回
    :   kNoErr : current semaphore count

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_semaphore([beken_semaphore_t](#_CPPv417beken_semaphore_t "beken_semaphore_t") *semaphore)[](#_CPPv421rtos_deinit_semaphoreP17beken_semaphore_t "永久链接至目标")
:   De-initialise a semaphore.

    @Details Deletes a semaphore created with [rtos_init_semaphore](#group__BEKEN__RTOS__SEM_1gab8c99e1fa5c54d1759c538ca78de93a5 "#group__BEKEN__RTOS__SEM_1gab8c99e1fa5c54d1759c538ca78de93a5")

    参数
    :   **semaphore** – : a pointer to the semaphore handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv415rtos_init_mutexP13beken_mutex_t "永久链接至目标")
:   Initialises a mutex.

    @Details A mutex is different to a semaphore in that a thread that already holds the lock on the mutex can request the lock again (nested) without causing it to be suspended.

    参数
    :   **mutex** – : a pointer to the mutex handle to be initialised

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_trylock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv418rtos_trylock_mutexP13beken_mutex_t "永久链接至目标")
:   Obtains the lock on a mutex.

    @Details Attempts to obtain the lock on a mutex. If the lock is already held by another thead, the calling thread will not be suspended until the mutex lock is released by the other thread.

    参数
    :   **mutex** – : a pointer to the mutex handle to be locked

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_lock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv415rtos_lock_mutexP13beken_mutex_t "永久链接至目标")
:   Obtains the lock on a mutex.

    @Details Attempts to obtain the lock on a mutex. If the lock is already held by another thead, the calling thread will be suspended until the mutex lock is released by the other thread.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **mutex** – : a pointer to the mutex handle to be locked

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_unlock_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv417rtos_unlock_mutexP13beken_mutex_t "永久链接至目标")
:   Releases the lock on a mutex.

    @Details Releases a currently held lock on a mutex. If another thread is waiting on the mutex lock, then it will be resumed.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **mutex** – : a pointer to the mutex handle to be unlocked

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv417rtos_deinit_mutexP13beken_mutex_t "永久链接至目标")
:   De-initialise a mutex.

    @Details Deletes a mutex created with [rtos_init_mutex](#group__BEKEN__RTOS__MUTEX_1ga206c1b0aebb6431a6407373e921b2486 "#group__BEKEN__RTOS__MUTEX_1ga206c1b0aebb6431a6407373e921b2486")

    参数
    :   **mutex** – : a pointer to the mutex handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_lock_mutex_timeout([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex, uint32_t timeout_ms)[](#_CPPv423rtos_lock_mutex_timeoutP13beken_mutex_t8uint32_t "永久链接至目标")
:   Obtains the lock on a mutex.

    @Details Attempts to obtain the lock on a mutex. If the lock is already held by another thead, the calling thread will be suspended until the mutex lock is released by the other thread or timeout.

    参数
    :   - **mutex** – : a pointer to the mutex handle to be locked

        - **timeout_ms** – : timeout for get lock

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_recursive_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv425rtos_init_recursive_mutexP13beken_mutex_t "永久链接至目标")
:   Creates a new recursive mutex type semaphore instance.

    @Details This API relies on marco CONFIG_FREERTOS_USE_RECURSIVE_MUTEXES

    参数
    :   **mutex** – : a pointer to the new recursive mutex handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_lock_recursive_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv425rtos_lock_recursive_mutexP13beken_mutex_t "永久链接至目标")
:   Obtains the lock on a recursive mutex (A mutex used recursively can be ‘taken’ repeatedly by the owner)

    @Details This API relies on marco CONFIG_FREERTOS_USE_RECURSIVE_MUTEXES

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **mutex** – : a pointer to the new recursive mutex handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_unlock_recursive_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv427rtos_unlock_recursive_mutexP13beken_mutex_t "永久链接至目标")
:   Releases the lock on a recursive mutex (A mutex used recursively can be ‘taken’ repeatedly by the owner)

    @Details This API relies on marco CONFIG_FREERTOS_USE_RECURSIVE_MUTEXES

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **mutex** – : a pointer to the new recursive mutex handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_recursive_mutex([beken_mutex_t](#_CPPv413beken_mutex_t "beken_mutex_t") *mutex)[](#_CPPv427rtos_deinit_recursive_mutexP13beken_mutex_t "永久链接至目标")
:   De-initialise a recursive mutex.

    @Details Deletes a mutex created with [rtos_init_recursive_mutex](#group__BEKEN__RTOS__MUTEX_1ga4904afaad1caa400f69a692093c4832f "#group__BEKEN__RTOS__MUTEX_1ga4904afaad1caa400f69a692093c4832f") This API relies on marco CONFIG_FREERTOS_USE_RECURSIVE_MUTEXES

    参数
    :   **mutex** – : a pointer to the recursive mutex handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, const char *name, uint32_t message_size, uint32_t number_of_messages)[](#_CPPv415rtos_init_queueP13beken_queue_tPKc8uint32_t8uint32_t "永久链接至目标")
:   Initialises a FIFO queue.

    参数
    :   - **queue** – : a pointer to the queue handle to be initialised

        - **name** – : a text string name for the queue (NULL is allowed)

        - **message_size** – : size in bytes of objects that will be held in the queue

        - **number_of_messages** – : depth of the queue - i.e. max number of objects in the queue

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_push_to_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv418rtos_push_to_queueP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Post an item to the back of a queue. The item is queued by copy, not by reference.

    备注

    This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : the object to be added to the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3")

        - **timeout_ms** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_push_to_queue_front([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv424rtos_push_to_queue_frontP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Post an item to the front of a queue. The item is queued by copy, not by reference.

    备注

    This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : the object to be added to the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3")

        - **timeout_ms** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_pop_from_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue, void *message, uint32_t timeout_ms)[](#_CPPv419rtos_pop_from_queueP13beken_queue_tPv8uint32_t "永久链接至目标")
:   Pops an object off a queue.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **queue** – : a pointer to the queue handle

        - **message** – : pointer to a buffer that will receive the object being popped off the queue. Size is assumed to be the size specified in [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3") , hence you must ensure the buffer is long enough or memory corruption will result

        - **timeout_ms** – the number of milliseconds to wait before returning

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error or timeout occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv417rtos_deinit_queueP13beken_queue_t "永久链接至目标")
:   De-initialise a queue created with [rtos_init_queue](#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3 "#group__BEKEN__RTOS__QUEUE_1gaac5e20b73f7298368b26eb5de85483c3").

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

bool rtos_is_queue_empty([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv419rtos_is_queue_emptyP13beken_queue_t "永久链接至目标")
:   Check if a queue is empty.

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   true : queue is empty.

    返回
    :   false : queue is not empty.

bool rtos_is_queue_full([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv418rtos_is_queue_fullP13beken_queue_t "永久链接至目标")
:   Check if a queue is full.

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   true : queue is empty.

    返回
    :   false : queue is not empty.

bool rtos_reset_queue([beken_queue_t](#_CPPv413beken_queue_t "beken_queue_t") *queue)[](#_CPPv416rtos_reset_queueP13beken_queue_t "永久链接至目标")
:   Reset queue.

    参数
    :   **queue** – : a pointer to the queue handle

    返回
    :   true : reset ok.

    返回
    :   false : reset fail.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags)[](#_CPPv421rtos_init_event_flagsP13beken_event_t "永久链接至目标")
:   Create a new event group

    参数
    :   **event_flags** – : pointer to a event handle which will be initialised

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[beken_event_flags_t](#_CPPv419beken_event_flags_t "beken_event_flags_t") rtos_wait_for_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags, uint32_t flags_to_wait_for, [beken_bool_t](#_CPPv412beken_bool_t "beken_bool_t") clear_set_flags, [beken_event_flags_wait_option_t](#_CPPv431beken_event_flags_wait_option_t "beken_event_flags_wait_option_t") wait_option, uint32_t timeout_ms)[](#_CPPv425rtos_wait_for_event_flagsP13beken_event_t8uint32_t12beken_bool_t31beken_event_flags_wait_option_t8uint32_t "永久链接至目标")
:   block to wait for one or more bits to be set within a previously created event group.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **event_flags** – : pointer to a event handle which will be initialised

        - **flags_to_wait_for** – : A bitwise value that indicates the bit or bits to test inside the event group. For example, to wait for bit 0 and/or bit 2 set flags_to_wait_for to 0x05. To wait for bits 0 and/or bit 1 and/or bit 2 set flags_to_wait_for to 0x07. Etc.

        - **clear_set_flags** – : If clear_set_flags is set to pdTRUE then any bits within flags_to_wait_for that are set within the event group will be cleared before returns

        - **wait_option** – : If it is set to WAIT_FOR_ALL_EVENTS then will return when either all the bits in flags_to_wait_for are set or the specified block time expires. If it is set to WAIT_FOR_ANY_EVENT then will return when any one of the bits set in flags_to_wait_for is set or the specified block time expires. The block time is specified by the timeout_ms parameter.

        - **timeout_ms** – : the time period between function calls in milliseconds

    返回
    :   The value of the event group at the time either the bits being waited for became set, or the block time expired.

void rtos_set_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags, uint32_t flags_to_set)[](#_CPPv420rtos_set_event_flagsP13beken_event_t8uint32_t "永久链接至目标")
:   Set bits within an event group.

    备注

    This API can be called in task context and interrupt context.

    参数
    :   - **event_flags** – : pointer to a event handle which will be initialised

        - **flags_to_set** –

          : A bitwise value that indicates the bit or bits to set. For example, to set bit 3 only, set flags_to_set to 0x08.

          To set bit 3 and bit 0 set flags_to_set to 0x09.

[beken_event_flags_t](#_CPPv419beken_event_flags_t "beken_event_flags_t") rtos_clear_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags, uint32_t flags_to_clear)[](#_CPPv422rtos_clear_event_flagsP13beken_event_t8uint32_t "永久链接至目标")
:   Clear bits within an event group.

    备注

    This API can be called in task context and interrupt context.

    参数
    :   - **event_flags** – : pointer to a event handle which will be initialised

        - **flags_to_clear** – :A bitwise value that indicates the bit or bits to clear in the event group. For example, to clear bit 3 only, set flags_to_clear to 0x08. To clear bit 3 and bit 0 set flags_to_clear to 0x09.

    返回
    :   The value of the event group before the specified bits were cleared

[beken_event_flags_t](#_CPPv419beken_event_flags_t "beken_event_flags_t") rtos_sync_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags, uint32_t flags_to_set, uint32_t flags_to_wait_for, uint32_t timeout_ms)[](#_CPPv421rtos_sync_event_flagsP13beken_event_t8uint32_t8uint32_t8uint32_t "永久链接至目标")
:   Atomically set bits within an event group, then wait for a combination of bits to be set within the same event group. This functionality is typically used to synchronise multiple tasks, where each task has to wait for the other tasks to reach a synchronisation point before proceeding.

    备注

    do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **event_flags** – : pointer to a event handle which will be initialised

        - **flags_to_set** – : The bits to set in the event group before determining if, and possibly waiting for, all the bits specified by the timeout_ms parameter are set.

        - **flags_to_wait_for** – : A bitwise value that indicates the bit or bits to test inside the event group. For example, to wait for bit 0 and bit 2 flags_to_wait_for to 0x05. To wait for bits 0 and bit 1 and bit 2 set flags_to_wait_for to 0x07. Etc.

        - **timeout_ms** – : the time period between function calls in milliseconds

    返回
    :   The value of the event group at the time either the bits being waited for became set, or the block time expired.

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_event_flags([beken_event_t](#_CPPv413beken_event_t "beken_event_t") *event_flags)[](#_CPPv423rtos_deinit_event_flagsP13beken_event_t "永久链接至目标")
:   Delete an event group that was previously created by a call to [rtos_init_event_flags()](#group__BEKEN__RTOS__EVENT_1gac306ea13a38248022cfca5893c0cc57c "#group__BEKEN__RTOS__EVENT_1gac306ea13a38248022cfca5893c0cc57c"). Tasks that are blocked on the event group will be unblocked and obtain 0 as the event group’s value.

    参数
    :   **event_flags** – : pointer to a event handle which will be initialised

    返回
    :   kNoErr : on success.

    返回
    :   kParamErr : if an error occurred

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
:   Initialize a RTOS periodic timer.

    备注

    Timer does not start running until beken_start_timer is called and the timer will execute periodically

    参数
    :   - **timer** – : a pointer to the timer handle to be initialised

        - **time_ms** – : Timer period in milliseconds

        - **function** – : the callback handler function that is called each time the timer expires

        - **arg** – : an argument that will be passed to the callback function

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_start_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv416rtos_start_timerP13beken_timer_t "永久链接至目标")
:   Starts a RTOS periodic timer.

    备注

    Timer must have been previously initialised with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de") This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the timer handle to start

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_stop_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv415rtos_stop_timerP13beken_timer_t "永久链接至目标")
:   Stops a running RTOS periodic timer.

    备注

    Timer must have been previously started with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the timer handle to stop

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_reload_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv417rtos_reload_timerP13beken_timer_t "永久链接至目标")
:   Reloads a RTOS periodic timer that has expired.

    备注

    This is usually called in the timer callback handler, to reschedule the timer for the next period. This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the timer handle to reload

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_timer([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv417rtos_deinit_timerP13beken_timer_t "永久链接至目标")
:   De-initialise a RTOS periodic timer.

    备注

    Deletes a RTOS timer created with [rtos_init_timer](#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de "#group__BEKEN__RTOS__TIMER_1ga977f803c06c250aff5299b621dd444de"). do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

bool rtos_is_timer_init([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv418rtos_is_timer_initP13beken_timer_t "永久链接至目标")
:   Check if an RTOS periodic timer is init.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if init.

    返回
    :   false : if not init

bool rtos_is_timer_running([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv421rtos_is_timer_runningP13beken_timer_t "永久链接至目标")
:   Check if an RTOS periodic timer is running.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if running.

    返回
    :   false : if not running

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_init_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer, uint32_t time_ms, [timer_2handler_t](#_CPPv416timer_2handler_t "timer_2handler_t") function, void *larg, void *rarg)[](#_CPPv423rtos_init_oneshot_timerP14beken2_timer_t8uint32_t16timer_2handler_tPvPv "永久链接至目标")
:   Initialize a RTOS oneshot timer.

    备注

    Timer does not start running until [rtos_start_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gaeaaae9363d21adfd6e4dc1bf0135c72a "#group__BEKEN__RTOS__TIMER_1gaeaaae9363d21adfd6e4dc1bf0135c72a") is called and the timer will only execute once

    参数
    :   - **timer** – : a pointer to the timer handle to be initialised

        - **time_ms** – : Timer period in milliseconds

        - **function** – : the callback handler function that is called each time the timer expires

        - **larg** – : an argument that will be passed to the callback function

        - **rarg** – : an argument that will be passed to the callback function

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_deinit_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv425rtos_deinit_oneshot_timerP14beken2_timer_t "永久链接至目标")
:   De-initialise a RTOS rtos_init_oneshot_timer timer.

    备注

    Deletes a RTOS timer created with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). do not call this API when interrupts are disabled (may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_start_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv424rtos_start_oneshot_timerP14beken2_timer_t "永久链接至目标")
:   start a RTOS oneshot timer

    备注

    Timer must have been previously started with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_stop_oneshot_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv423rtos_stop_oneshot_timerP14beken2_timer_t "永久链接至目标")
:   stop a RTOS oneshot timer

    备注

    Timer must have been previously started with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

bool rtos_is_oneshot_timer_running([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv429rtos_is_oneshot_timer_runningP14beken2_timer_t "永久链接至目标")
:   Check if an RTOS oneshot timer is running.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if running.

    返回
    :   false : if not running

bool rtos_is_oneshot_timer_init([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv426rtos_is_oneshot_timer_initP14beken2_timer_t "永久链接至目标")
:   Check if an RTOS oneshot timer is initialised.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   true : if initialised

    返回
    :   false : if not initialised

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_oneshot_reload_timer([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer)[](#_CPPv425rtos_oneshot_reload_timerP14beken2_timer_t "永久链接至目标")
:   re-starts a oneshot timer

    备注

    Timer must have been previously started with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_change_period([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer, uint32_t time_ms)[](#_CPPv418rtos_change_periodP13beken_timer_t8uint32_t "永久链接至目标")
:   changes the period of a oneshot timer

    备注

    Timer must have been previously started with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

[bk_err_t](#_CPPv48bk_err_t "bk_err_t") rtos_oneshot_reload_timer_ex([beken2_timer_t](#_CPPv414beken2_timer_t "beken2_timer_t") *timer, uint32_t time_ms, [timer_2handler_t](#_CPPv416timer_2handler_t "timer_2handler_t") function, void *larg, void *rarg)[](#_CPPv428rtos_oneshot_reload_timer_exP14beken2_timer_t8uint32_t16timer_2handler_tPvPv "永久链接至目标")
:   changes the period of a oneshot timer then re-start it

    备注

    Timer must have been previously started with [rtos_init_oneshot_timer](#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203 "#group__BEKEN__RTOS__TIMER_1gad0584724261ba4d9b4835bdcbc3b7203"). This API can be called in task context and interrupt context. However when calling this API in task context,the interrupt cannot be turned off(may cause the system to enter a deadlock or abnormal status)

    参数
    :   - **timer** – : a pointer to the RTOS timer handle

        - **time_ms** – : Timer period in milliseconds

        - **function** – : the callback handler function that is called each time the timer expires

        - **larg** – : an argument that will be passed to the callback function

        - **rarg** – : an argument that will be passed to the callback function

    返回
    :   kNoErr : on success.

    返回
    :   kGeneralErr : if an error occurred

uint32_t rtos_get_timer_expiry_time([beken_timer_t](#_CPPv413beken_timer_t "beken_timer_t") *timer)[](#_CPPv426rtos_get_timer_expiry_timeP13beken_timer_t "永久链接至目标")
:   Returns the time in ticks at which the timer will expire.

    参数
    :   **timer** – : a pointer to the RTOS timer handle

    返回
    :   If the timer is running then the time in ticks at which the timer will next expire is returned. If the timer is not running then the return value is undefined.

void rtos_start_scheduler(void)[](#_CPPv420rtos_start_schedulerv "永久链接至目标")
:   Starts the real time kernel tick processing. After calling the kernel has control over which tasks are executed and when.

bool rtos_is_scheduler_started(void)[](#_CPPv425rtos_is_scheduler_startedv "永久链接至目标")
:   check if the rtos scheduler is running or not

char *rtos_get_name(void)[](#_CPPv413rtos_get_namev "永久链接至目标")
:   get the name of the currently used OS

char *rtos_get_version(void)[](#_CPPv416rtos_get_versionv "永久链接至目标")
:   get the version of the currently used OS

size_t rtos_get_total_heap_size(void)[](#_CPPv424rtos_get_total_heap_sizev "永久链接至目标")
:   get the total heap size

    返回
    :   the amount of total heap space available on the system

size_t rtos_get_free_heap_size(void)[](#_CPPv423rtos_get_free_heap_sizev "永久链接至目标")
:   get the free heap size

    返回
    :   the amount of left heap space available on the system

size_t rtos_get_minimum_free_heap_size(void)[](#_CPPv431rtos_get_minimum_free_heap_sizev "永久链接至目标")
:   get the minimum heap size

    返回
    :   the minimum value remaining during the system heap space usage

size_t rtos_get_psram_total_heap_size(void)[](#_CPPv430rtos_get_psram_total_heap_sizev "永久链接至目标")
:   get the total heap size in psram

    返回
    :   the amount of total heap space in psram

size_t rtos_get_psram_free_heap_size(void)[](#_CPPv429rtos_get_psram_free_heap_sizev "永久链接至目标")
:   get the free heap size

    返回
    :   the amount of left heap space in psram

size_t rtos_get_psram_minimum_free_heap_size(void)[](#_CPPv437rtos_get_psram_minimum_free_heap_sizev "永久链接至目标")
:   get the minimum heap size in psram

    返回
    :   the minimum value remaining in psram during the system heap space usage

uint32_t rtos_get_tick_count(void)[](#_CPPv419rtos_get_tick_countv "永久链接至目标")
:   get the os tick count

    返回
    :   The count of ticks since vTaskStartScheduler was called.

uint32_t rtos_disable_int(void)[](#_CPPv416rtos_disable_intv "永久链接至目标")
:   disable interrupts and return the current interrupt status

    备注

    disable interrupt support nesting

    返回
    :   the current interrupt status

void rtos_enable_int(uint32_t int_level)[](#_CPPv415rtos_enable_int8uint32_t "永久链接至目标")
:   enable previously disabled interrupts

    备注

    this API needs to be used with [rtos_disable_int](#group__BEKEN__RTOS__SYSTEM_1ga99e8c6b5c91918fe9cfe5d1bed847761 "#group__BEKEN__RTOS__SYSTEM_1ga99e8c6b5c91918fe9cfe5d1bed847761")

    参数
    :   **int_level** – : saved interrupt status

    返回
    :   the current interrupt status

uint32_t rtos_before_sleep(void)[](#_CPPv417rtos_before_sleepv "永久链接至目标")
:   disable interrupts and return the current interrupt status

    备注

    disable interrupt support nesting. This API has the same functionality as [rtos_disable_int](#group__BEKEN__RTOS__SYSTEM_1ga99e8c6b5c91918fe9cfe5d1bed847761 "#group__BEKEN__RTOS__SYSTEM_1ga99e8c6b5c91918fe9cfe5d1bed847761")

    返回
    :   the current interrupt status

void rtos_after_sleep(uint32_t int_level)[](#_CPPv416rtos_after_sleep8uint32_t "永久链接至目标")
:   enable previously disabled interrupts

    备注

    This API has the same functionality as [rtos_enable_int](#group__BEKEN__RTOS__SYSTEM_1gaaa0099eff47f618846327600529b3499 "#group__BEKEN__RTOS__SYSTEM_1gaaa0099eff47f618846327600529b3499")

    参数
    :   **int_level** – : saved interrupt status

    返回
    :   the current interrupt status

bool rtos_is_in_interrupt_context(void)[](#_CPPv428rtos_is_in_interrupt_contextv "永久链接至目标")
:   Check if system in interrupt context.

    返回
    :   true : if in interrupt context

    返回
    :   false : if not in interrupt context

bool rtos_local_irq_disabled(void)[](#_CPPv423rtos_local_irq_disabledv "永久链接至目标")
:   Check if local irq is disabled.

    返回
    :   true : if irq is disabled

    返回
    :   false : if irq is not disabled

bool rtos_is_scheduler_suspended(void)[](#_CPPv427rtos_is_scheduler_suspendedv "永久链接至目标")
:   Check if the current scheduler is in suspended state.

    返回
    :   true : the scheduler is in suspended state

    返回
    :   false : the scheduler is not in suspended state

void rtos_shutdown(void)[](#_CPPv413rtos_shutdownv "永久链接至目标")
:   disable interrupts and the run in an infinite loop


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
