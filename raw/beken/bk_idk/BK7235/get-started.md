---
aliases:
- 'BK7235 › get-started'
---
# 快速入门[](#id1 "永久链接至标题")


本文档以 BK7235 开发板为例，通过一个简单的示例项目向您展示

> - 如何构建Armino编译环境；
> - 以及如何配置 Armino 工程；
> - 如何编译、下载固件；


## 准备工作[](#id2 "永久链接至标题")

硬件：

> - BK7235 开发板
> - 串口烧录工具
> - 电脑（Windows 与 Ubuntu）

备注

Armino 支持在 Linux 平台和Windows+Cygwin环境编译，仅支持在 Windows 平台进行固件烧录。
如果在Linux 平台进行开发那么还需要一台 Windows 平台的电脑用于烧录；当然也可以只使用 Windows 并安装 Linux 虚拟机。

软件：

> - RISCV工具链，用于编译 Armino RISCV版本；
> - 构建工具，包含 CMake；
> - Armino 源代码；
> - 串口烧录软件；


## Armino SDK代码下载[](#armino-sdk "永久链接至标题")

您可从 gitlab 上下载 Armino:


```
mkdir -p ~/armino
cd ~/armino
git clone http://gitlab.bekencorp.com/wifi/armino.git

```

您也可从 github 上下载 Armino:


```
mkdir -p ~/armino
cd ~/armino
git clone https://github.com/bekencorp/armino.git

```

备注

从官网的gitlab下载的为最近的SDK代码，相关账号找项目上审核申请。


## 构建编译环境[](#id3 "永久链接至标题")

备注

Armino，当前支持Linux环境下编译，本章节将以Ubuntu 20.04 LTS版本为例，介绍整个编译环境的搭建。


## 工具链安装[](#id4 "永久链接至标题")

BK7256工具链下载路径如下：

> 工具链下载：
> [http://dl.bekencorp.com/tools/toolchain/](http://dl.bekencorp.com/tools/toolchain/ "http://dl.bekencorp.com/tools/toolchain/")
> 在此目录下获取最新版本，如：toolchain_v5.2.1.tgz

工具包下载后，通过如下操作命令解压至 /opt/risc-v目录下:


```
$ sudo tar -zxvf toolchain_v5.2.1.tgz -C /

```

备注

工具链默认路径在middleware/soc/bk7256/bk7256.defconfig文件中定义，客户可自行配置:


```
CONFIG_TOOLCHAIN_PATH="/opt/risc-v/nds32le-elf-mculib-v5/bin"

```

工具链也可支持相对路径配置，如工具链放在sdk目录下:


```
CONFIG_TOOLCHAIN_PATH="toolchain_v5.2.1/nds32le-elf-mculib-v5/bin"

```


## 程序编译依赖库安装[](#id5 "永久链接至标题")

在终端输入下述命令安装 python3，CMake，Ninja， Crypto以及依赖库:


```
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install build-essential cmake python3 python3-pip doxygen ninja-build libc6:i386 libstdc++6:i386 libncurses5-dev lib32z1 -y
sudo pip3 install pycrypto click

```


## 文档编译依赖库安装[](#id6 "永久链接至标题")

在终端上输入如下命令安装文档编译所需要的 python 依赖:


```
sudo pip3 install sphinx_rtd_theme future breathe blockdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-nwdiag sphinxcontrib.blockdiag

```

设置Python默认版本:


```
sudo ln -s /usr/bin/python3 /usr/bin/python

```


## 编译工程[](#id7 "永久链接至标题")

在终端下输入下述命令编译 Armino 默认工程，PROJECT为可选参数，默认为app，默认工程为启动 WiFi，BLE，初始化常见驱动，并启动 Armino 默认 Cli 程序:


```
cd ~/armino
make bk7235

```


- BK7235平台默认工程使用的是FreeRTOS V10.4系统:

  ```
  components/os_source/freertos_v10
  ```

- BK7235平台支持鸿蒙OS V3.0.1系统，可编译harmony工程:

  ```
  cd ~/armino
  make bk7235 PROJECT=harmony
  ```

- 当然您也可以编译任何其他 armino/projects 下的工程，命令如下:

  ```
  cd ~/armino
  make bk7235 PROJECT=examples/get-started/hello_world
  ```


## 在Windows平台下开发[](#windows "永久链接至标题")

目前Armino SDK已支持在Cygwin+Windows环境下编译。在http://dl.bekencorp.com/tools/bk_cygwin 可以下载到我们适配好的cygwin环境包。我们从Armino v1.7.0.2版本开始完全支持在Cygwin环境下编译。


### 准备工作[](#id8 "永久链接至标题")


- 1.从我们的下载服务器下载Cygwin环境包并解压缩在任意路径。

- 2.如上文所提获取Armino SDK

备注


- 可以tar格式或其他除zip以外的压缩格式下载我们的SDK，因为我们发现zip格式压缩时会改变我们SDK中的软链接导致编译错误。

- 在Cygwin环境下通过tar -vxf ${SDK压缩包} 解压缩SDK，unzip解压同样会导致后续工作出现错误。

- 如果以git clone的方式获取我们的sdk也需要在Cygwin环境下执行，直接在windows下进行clone也会改变sdk中的软连接。


### 编译工程[](#id9 "永久链接至标题")


- 1、进入Cygwin终端环境：运行Cygwin所在目录下Cygwin.bat将会打开另一个类Linux的终端窗口。终端窗口默认登陆时工作路径为${Cygwin}/home/${username}/。

- 2、打开sdk所在路径：Cygwin中本地磁盘挂载在/cygdrive目录下，可以通过cd指令进行访问，如访问本地C盘根目录即cd /cygdrive/c。

- 3、编译SDK：打开sdk目录后即可通过make编译sdk 如编译BK7235m mcu工程则输入make bk7235 PROJECT=mcu。


## 配置工程[](#id10 "永久链接至标题")


- 您可以通过 menuconfig 来更改 Armino 默认配置项，以bk7235为例进行操作说明

  > - 终端键入命令,其中ARMINO_SOC用于指定芯片:
  >
  >   ```
  >   cd ~/armino
  >   make menuconfig ARMINO_SOC=bk7235
  >   ```
  > - menuconfig配置界面呈现如下图:
  >   :   ![menuconfig gui](../_images/menuconfig.png)
  >
  >
  >       Menuconfig[](#id15 "永久链接至图片")
  > - 通过上下键选择，并按回车键进入组件配置项的目录：
  >   (Top)–>ARMINO Configuration–>Components Configuration
  > - 配置当前目录所罗列的组件配置项，并按”S”键保存
  > - 保存后，从menuconfig配置界面配置的差异配置项将更新到工程配置文件projects/app/config/bk7235.config中
  > - 终端输入命令，编译工程bk7235:
  >
  >   ```
  >   cd ~/armino
  >   make bk7235
  >   ```
  > - 编译时将以工程配置文件 Override 芯片配置文件 Override 默认配置的优先级进行差异化配置
  >   如： bk7235.config >> bk7235.defconfig >> KConfig

- 您也可以直接通过工程配置文件来进行差异化配置:

  ```
  工程配置文件 Override 芯片配置文件 Override 默认配置
  如： bk7235.config >> bk7235.defconfig >> KConfig

  + 工程配置文件示例：
      projects/app/config/bk7235.config
      projects/harmony/config/bk7235.config
      projects/customization/bk7235_config1/config/bk7235.config

  + 芯片配置文件示例：
      middleware/soc/bk7235/bk7235.defconfig

  + KConfig配置文件示例：
      middleware/arch/riscv/Kconfig
      components/bk_cli/Kconfig
  ```

- 重要的配置说明
  :   - 操作系统配置为FreeRTOS V10:

        ```
        #
        # FreeRTOS
        #
        CONFIG_FREERTOS=y
        # CONFIG_LITEOS_M is not set
        CONFIG_FREERTOS_V9=n
        CONFIG_FREERTOS_V10=y
        ```

      - 操作系统配置为鸿蒙OS:

        ```
        # LITEOS_M
        CONFIG_LITEOS_M_V3=y
        CONFIG_LITEOS_M_BK=y

        # FreeRTOS
        CONFIG_FREERTOS=n
        CONFIG_FREERTOS_V9=n
        CONFIG_FREERTOS_V10=n
        ```

- 系列芯片宏的使用与差异

  > - 宏CONFIG_SOC_BK7256XX 表示BK7256系列:
  >
  >   ```
  >   属于BK7235/BK7237/BK7256公共芯片宏，CPU1也需要定义该宏
  >           配置方式：CONFIG_SOC_BK7256XX=y
  >   ```
  > - 区分同系列芯片的宏(不用于区分其他芯片):
  >
  >   ```
  >   CONFIG_SOC_BK7235, CPU1需要定义该宏和CONFIG_SLAVE_CORE组合区分BK7235_CPU1
  >   配置方式：CONFIG_SOC_BK7235=y
  >   ```
  > - 字符串系列芯片的宏(用于编译阶段区分其他芯片):
  >
  >   ```
  >   cpu0/cpu1有区分：
  >           CPU0写法：CONFIG_SOC_STR="bk7235"
  >           CPU1写法：CONFIG_SOC_STR="bk7235_cp1"
  >   ```
  > - 双核CPU0,CPU1相关宏区分(用于代码区分):
  >
  >   ```
  >   CONFIG_DUAL_CORE            #双核功能
  >   CONFIG_MASTER_CORE          #依赖于CONFIG_DUAL_CORE，CPU0与CPU1的区别
  >   CONFIG_SLAVE_CORE           #依赖于CONFIG_DUAL_CORE，CPU0与CPU1的区别
  >   单核：上面的三个宏都不定义
  >   ```


## 新建工程[](#id11 "永久链接至标题")

默认工程为projects/app，新建工程可参考projects/harmony工程


## 烧录代码[](#id12 "永久链接至标题")

在 Windows 平台上， Armino 目前支持 UART 烧录。


### 通过串口烧录[](#id13 "永久链接至标题")

备注

Armino支持UART烧录，推荐使用 CH340 串口工具小板进行下载。

串口烧录工具如下图所示:

![Uart](../_images/download_tool_uart.png)

UART[](#id16 "永久链接至图片")

烧录工具获取：

> [http://dl.bekencorp.com/tools/flash/](http://dl.bekencorp.com/tools/flash/ "http://dl.bekencorp.com/tools/flash/")
> 在此目录下获取最新版本，如：BEKEN_BKFIL_V2.1.4.0_20231011.zip

bk_writer.exe 界面及相关配置如下图所示：

![Bkwrite GUI](../_images/download_uart_bk7256.png)

bkwriter GUI[](#id17 "永久链接至图片")

烧录串口UART1，点击``烧录``进行版本烧录, 烧录完成之后掉电重启设备。


## 串口Log及Command Line[](#logcommand-line "永久链接至标题")


- 目前BK7235平台，串口Log及Command Line命令输入在UART1口；可通过help命令查看支持命令列表；

- CPU1的Log也通过CPU0的UART1串口输出，CPU1的Log带“cpu1”标记；

- CPU1的Command Line可通过CPU0的UART1执行，如:

  ```
  cpu1 help //输出cpu1的命令列表
  cpu1 time //输出cpu1的当前运行时间
  ```


## 编译选项及链接选项[](#id14 "永久链接至标题")

> - BK7235平台，默认编译选项”-mstrict-align”，链接选项”-Wl,–defsym,memcpy=memcpy_ss”
> - 若单独编译lib库，需要增加编译选项”-mstrict-align”
> - 若不使用平台的链接命令，如编译鸿蒙系统，对于Andes v5.1.1工具链，需要增加链接选项”-Wl,–defsym,memcpy=memcpy_ss”
