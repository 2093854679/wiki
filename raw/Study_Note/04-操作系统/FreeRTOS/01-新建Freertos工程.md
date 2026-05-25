## 01-FreeRTOS工程创建

![image-20251020112627195](markdown-img/01-新建Freertos工程.assets/image-20251020112627195.png)

![image-20251020112845549](markdown-img/01-新建Freertos工程.assets/image-20251020112845549.png)

编译出现的问题：

```
Error: L6218E: Undefined symbol Image$$ARM_LIB_STACK$$ZI$$Limit (referred from startup_armcm3.o)

```

分析：

这个错误依然说明：
 链接器（ARM Linker）**没有生成堆栈边界符号**
 `Image$$ARM_LIB_STACK$$ZI$$Limit`。

> 该符号通常由链接脚本（Scatter File 或自动生成的内存布局）提供。
>  启动文件 `startup_ARMCM3.s` 里引用它来设置堆栈初始值。

解决方法:

![image-20251020115041628](markdown-img/01-新建Freertos工程.assets/image-20251020115041628.png)

找到该文件的磁盘位置，复制绝对路径到下方位置

<img src="markdown-img/01-新建Freertos工程.assets/image-20251020115128884.png" alt="image-20251020115128884" style="zoom:50%;" />

## 02-裸机系统

![image-20251020162406791](markdown-img/01-新建Freertos工程.assets/image-20251020162406791.png)

## 03-前后台系统

![image-20251020162445108](markdown-img/01-新建Freertos工程.assets/image-20251020162445108.png)

## 04-多任务系统

![image-20251020162506496](markdown-img/01-新建Freertos工程.assets/image-20251020162506496.png)

## 05-对比

![image-20251020162630795](markdown-img/01-新建Freertos工程.assets/image-20251020162630795.png)