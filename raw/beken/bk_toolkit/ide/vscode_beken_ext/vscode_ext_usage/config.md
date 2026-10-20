---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ide/ide/zh_CN/v2.0.1/vscode_beken_ext/vscode_ext_usage/config.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 配置

插件安装完成后，点击侧边栏BEKEN图标，即可开始使用插件。

插件使用之前请先按照说明进行相应的配置。

点击BEKEN图标进入插件，选择`BASE-FUNC` -\> `Config`
进入插件配置页面，如下图：

<a id="id5"></a>
![初始](../../../../_assets/57d2f6aad45d680d7fb1-%E5%88%9D%E5%A7%8B.png)


初始

<a id="id2"></a>

## 环境配置

环境配置主要是配置插件功能所需要的各种工具路径。

<a id="toolchain"></a>

### Toolchain

1. 点击`ToolChain`配置中的`Download`，跳转到`ToolChain`下载链接，进行下载

<a id="id6"></a>
![toolchain_download](../../../../_assets/422c57524a3238e20e92-toolchain_download.png)


toolchain\_download

<a id="id7"></a>
![toolchain_download2](../../../../_assets/098dcb90f2219908a33a-toolchain_download2.png)


toolchain\_download2

2. 下载完成以后，对`arminoToolChain.zip`进行解压，点击`ToolChain`配置中的`Set`选择解压后的`arminoToolChain`目录即可，插件会对ToolChain中相关的工具进行检测并显示出检测结果，检测结果没有错误即说明`ToolChain`配置成功!

<a id="id8"></a>
![toolchain_download4](../../../../_assets/6b2d3cadf44293ffd2d2-toolchain_download4.png)


toolchain\_download4

> 注: ToolChain配置属于全局配置，所有beken工程共享同一个配置。

<a id="bkfil"></a>

### BKFIL

1. 点击`BKFIL`配置中的`Download`，跳转到`BKFIL`下载链接，选择需要的`BKFIL`版本，点击页面中的`下载`按钮，即可进行下载
2. 下载完成以后，对下载后的.zip文件进行解压，点击`BKFIL`配置中的`Set`选择解压后的`bk_loader.exe`文件即可。

   <a id="id9"></a>
   ![bkfil_download](../../../../_assets/bcc6ebeb0e4eb4bb71e5-bkfil_download.png)


   bkfil\_download

> 注: BKFIL配置属于全局配置，所有beken工程共享同一个配置。

<a id="id3"></a>

## 工程配置

环境配置完成以后，即可进行工程配置。

<a id="sdk"></a>

### SDK

1. `SDK`配置中提供默认的`gitlab`仓库地址，也可点击输入框进行编辑，自定义`git`仓库地址。点击`Download`按钮进行下载。

   <a id="id10"></a>
   ![sdk_download_0](../../../../_assets/628ed00448c9ac47e0b4-sdk_download_0.png)


   sdk\_download\_0
2. 下载时需要输入`gitlab`用户名、密码，然后选择需要下载的`tag`进行下载即可，插件会打开vscode终端，进行下载。

<a id="project"></a>

### Project

`SDK`下载完成以后，即可在VSCode中打开项目，Project会读取当前项目中的数据。

<a id="id11"></a>
![project_config](../../../../_assets/4adad472d1f8e2724a55-project_config.png)


project\_config

<a id="soc"></a>

#### soc

soc读取路径: `根目录/middleware/soc`

<a id="project-1"></a>

<a id="id4"></a>

#### Project

project路径读取: 根目录/projects

<a id="build-cmd"></a>

#### Build cmd

`Build cmd`配置提供默认的`Build`命令，也可以点击输入框进行编辑，自定义`Build`命令。

<a id="device"></a>

### Device

<a id="id12"></a>
![device](../../../../_assets/8dae9227403ebd012ca2-device.png)


device

<a id="serial"></a>

#### Serial

烧录:raw-latex:擦除时所用的板卡Uart口

<a id="baudrate"></a>

#### Baudrate

烧录:raw-latex:擦除时所用的波特率
