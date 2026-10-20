---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ipc/bk7259/zh_CN/v4.0.1/get-started/index.html
sdk_family: bk_ipc
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速入门

本节说明 BK7259 IPC 方案如何获取代码、安装编译环境、编译工程以及烧录固件，帮助您快速上手。

<a id="quick-start"></a>

<a id="id2"></a>

## 获取代码

BK7259 IPC 解决方案和 Armino SMP SDK 均同步发布至 GitHub、Gitee 和 GitLab，可根据网络环境及访问权限选择代码源。

BK7259 IPC 解决方案：

- GitHub：\<<https://github.com/bekencorp/bk_solution_ipc>\>
- Gitee：\<<https://gitee.com/bekencorp/bk_solution_ipc>\>
- GitLab：\<<https://gitlab.bekencorp.com/armino/smp_solution/bk_solution_ipc>\>

Armino SMP SDK：

- GitHub：\<<https://github.com/bekencorp/bk_avdk_smp>\>
- Gitee：\<<https://gitee.com/bekencorp/bk_avdk_smp>\>
- GitLab：\<<https://gitlab.bekencorp.com/armino/bk_avdk_smp>\>

GitHub 和 Gitee 可公开访问。GitLab 仅面向企业客户开放；企业客户如需访问，请联系对接的 FAE 或销售人员申请开通权限。

**Windows 用户注意**：使用 Git for Windows 获取代码时，建议在克隆前关闭自动换行符转换，避免脚本或源文件被转换为 CRLF 而导致编译失败。Linux、macOS 和 WSL 环境无需执行。

```
git config --global core.autocrlf false
```

如果代码已经克隆，修改该配置不会自动恢复文件，建议设置后重新克隆。

以下命令以 GitHub 和 `release/v4.0.1.7` 标签为例。**实际获取代码时，请选择最新发布的标签，并确保方案代码与 SDK 使用完全相同的标签**。使用其他代码源时，替换对应的仓库地址即可。

```
mkdir -p ~/armino && cd ~/armino

# Armino SMP SDK
git clone --branch release/v4.0.1.7 https://github.com/bekencorp/bk_avdk_smp.git

# BK7259 IPC 解决方案
git clone --branch release/v4.0.1.7 https://github.com/bekencorp/bk_solution_ipc.git
```

<a id="setup-env"></a>

<a id="id3"></a>

## 编译环境安装

Armino SMP 支持本地编译和 Docker 编译，可根据开发平台选择以下方式部署编译环境。

<a id="linux"></a>

### Linux 本地编译

进入 SDK 目录并运行环境安装脚本：

```
# 安装脚本位于 bk_avdk_smp 仓库内
cd ~/armino/bk_avdk_smp
sudo bash tools/env_tools/setup/armino_env_setup.sh
```

<a id="windows"></a>

### Windows 本地编译

下载并安装 [Armino Bash](https://dl.bekencorp.com/tools/arminosdk/WindowsInstaller/Armino-Bash-Setup_0.3.0.exe)。

<a id="docker"></a>

### Docker 编译

Docker 编译镜像为 [bekencorp/armino-idk](https://hub.docker.com/r/bekencorp/armino-idk/tags)，请选择 `1.5` 或更高版本的镜像标签，支持 Windows / Linux / macOS。

详细安装步骤请参阅 [环境部署及编译](../../bk_avdk_smp/get-started.md#smp-get-started-env)。

<a id="build-project"></a>

<a id="id5"></a>

## 编译工程

以 `ipc` 工程为例（位于 `projects/ipc`），通过 `SDK_DIR` 指向 Armino SMP SDK 后本地编译：

```
cd ~/armino/bk_solution_ipc/projects/ipc
make bk7259 SDK_DIR=~/armino/bk_avdk_smp PROJECT=ipc
```

也支持 Docker 编译（Linux / macOS 用 `./dbuild.sh`，Windows PowerShell 用 `.\dbuild.ps1`）：

```
cd ~/armino/bk_solution_ipc/projects/ipc
export SDK_DIR=~/armino/bk_avdk_smp
./dbuild.sh make bk7259 PROJECT=ipc
```

编译成功后，用于烧录的固件文件位于以下路径（相对于 `bk_solution_ipc/` 仓库根目录）：

```
projects/ipc/build/bk7259/ipc/package/all-app.bin
```

其他工程请将命令中的路径与 `PROJECT` 参数替换为对应的 `projects/<工程名>`。

<a id="flash-firmware"></a>

<a id="id6"></a>

## 烧录固件

可选择以下任一方式烧录固件：

- 下载并使用 [BKFIL 本地烧录工具](https://dl.bekencorp.com/tools/bkfil/v4)
- 使用 [BKFIL 网页烧录工具](https://connect.aclsemi.com/)

烧录时请选择上一节编译生成的 `all-app.bin` 固件文件。

详细烧录流程请参阅 [烧录代码](../../bk_avdk_smp/get-started.md#smp-get-started-flash)。

<a id="id9"></a>

## 相关资源

- 应用处理器 AP 配置和使用，请参考 [Armino AP](../../bk_avdk_smp/ap_doc/index.md)
- 通信处理器 CP 配置和使用，请参考 [Armino CP](../../bk_avdk_smp/cp_doc/index.md)
