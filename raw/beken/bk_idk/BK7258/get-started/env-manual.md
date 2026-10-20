---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/get-started/env-manual.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="env-manual"></a>

<a id="id1"></a>

# 本地部署

<a id="id2"></a>

## 构建编译环境

备注

Armino 编译环境要求Ubuntu 20.04 LTS 版本及以上，Centos 7版本及以上，Archlinux或者Debian 11版本及以上，本章节将以 Ubuntu 20.04 LTS 版本为例，介绍整个编译环境的搭建。

编译环境可以使用环境安装脚本进行安装，也可以手动安装，这里推荐使用使用安装脚本方式。如果在sdk目录中没有安装脚本，可以从beken服务器上下载安装脚本。

- 脚本安装：

  > 如果sdk中存在安装脚本，那么进入sdk目录后执行安装脚本，按照安装脚本引导即可完成构建环境安装:
  >
  > ```
  > cd ~/armino/bk_idk
  > sudo bash tools/env_tools/setup/armino_env_setup.sh
  > ```
  >
  > 如果sdk中不存在安装脚本，可以从 [链接](https://dl.bekencorp.com/d/tools/arminosdk/autoinstall_script/armino_env_setup.sh) 处下载并执行。
- 手动安装：

  > 手动安装请参考 [链接](manual_install.md#manual-install)

备注

工具链默认路径在 middleware/soc/bk7258/bk7258.defconfig 文件中定义，如果您更改了工具链路径，需要在配置文件中重新配置工具链路径:

```
CONFIG_TOOLCHAIN_PATH="/opt/gcc-arm-none-eabi-10.3-2021.10/bin"
```

<a id="id4"></a>

## 编译工程

在终端下输入下述命令编译 Armino 默认工程，PROJECT为可选参数，默认为app，默认工程为启动 WiFi，BLE，初始化常见驱动，并启动 Armino 默认 Cli 程序:

```
cd ~/armino/bk_idk
make bk7258
```

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [准备工作](../get-started.md)
- [Armino SDK 代码下载](../get-started.md)
- [环境部署及编译](../get-started.md)
- [Docker部署](env-docker.md)
- [配置工程](../get-started.md)
- [新建工程](../get-started.md)
- [烧录代码](../get-started.md)
- [串口 Log 及 Command Line](../get-started.md)
- [H/W 参考手册](../hw-reference.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [OS 相关参考](../os.md)
- [样例演示](../examples.md)
- [应用开发](../application.md)
- [开发与贡献代码流程](../process.md)
- [云平台](../cloud.md)
- [工程与示例](../projects/projects.md)
