---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_dashboard/bk7258/zh_CN/v3.1.1/get-started/index.html
sdk_family: bk_dashboard
chip: BK7258
processor: ''
sdk_version: v3.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速入门

本节说明 BK7258 两轮车方案如何获取代码、安装编译环境、编译工程以及烧录固件，帮助您快速上手。

<a id="quick-start"></a>

<a id="id2"></a>

## 获取代码

BK7258 两轮车方案和 Armino SMP SDK 均同步发布至 GitHub、Gitee 和 GitLab，可根据网络环境及访问权限选择代码源。

BK7258 两轮车方案：

- GitHub：<https://github.com/bekencorp/bk_solution_dashboard>
- Gitee：<https://gitee.com/bekencorp/bk_solution_dashboard>
- GitLab：<https://gitlab.bekencorp.com/armino/smp_solution/bk_solution_dashboard>

Armino SMP SDK：

- GitHub：<https://github.com/bekencorp/bk_avdk_smp>
- Gitee：<https://gitee.com/bekencorp/bk_avdk_smp>
- GitLab：<https://gitlab.bekencorp.com/armino/bk_avdk_smp>

GitHub 和 Gitee 可公开访问。GitLab 仅面向企业客户开放；企业客户如需访问，请联系对接的 FAE 或销售人员申请开通权限。

**Windows 用户注意**：使用 Git for Windows 获取代码时，建议在克隆前关闭自动换行符转换，避免脚本或源文件被转换为 CRLF 而导致编译失败。Linux、macOS 和 WSL 环境无需执行。

```
git config --global core.autocrlf false
```

如果代码已经克隆，修改该配置不会自动恢复文件，建议设置后重新克隆。

以下命令以 GitHub 和 `release/v3.1.1.8` 标签为例。**实际获取代码时，请选择最新发布的标签，并确保方案代码与 SDK 使用完全相同的标签**。使用其他代码源时，替换对应的仓库地址即可。

```
mkdir -p ~/armino && cd ~/armino

# Armino SMP SDK
git clone --branch release/v3.1.1.8 https://github.com/bekencorp/bk_avdk_smp.git

# BK7258 两轮车方案
git clone --branch release/v3.1.1.8 https://github.com/bekencorp/bk_solution_dashboard.git
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

详细安装步骤请参阅 [环境部署及编译](../../bk_avdk_smp/BK7258/get-started.md#smp-get-started-env)。

<a id="build-project"></a>

<a id="id5"></a>

## 编译工程

以 `scooter_800_480` 工程为例（位于 `projects/scooter_800_480`），通过 `SDK_DIR` 指向 Armino SMP SDK 后本地编译：

```
cd ~/armino/bk_solution_dashboard/projects/scooter_800_480
make bk7258 SDK_DIR=~/armino/bk_avdk_smp        # 也可先 export SDK_DIR 再执行 make bk7258
```

也支持 Docker 编译（Linux / macOS 用 `./dbuild.sh`，Windows PowerShell 用 `.\dbuild.ps1`）：

```
cd ~/armino/bk_solution_dashboard/projects/scooter_800_480
export SDK_DIR=~/armino/bk_avdk_smp
./dbuild.sh make bk7258
```

编译成功后，用于烧录的固件文件位于以下路径（相对于 `bk_solution_dashboard/` 仓库根目录）：

```
projects/scooter_800_480/build/bk7258/scooter_800_480/package/all-app.bin
```

其他工程请将命令中的路径替换为对应的 `projects/<工程名>`。

<a id="flash-firmware"></a>

<a id="id6"></a>

## 烧录固件

<a id="id7"></a>

### 烧录主控

可选择以下任一方式烧录 BK7258 主控固件：

- 下载并使用 [BKFIL 本地烧录工具](https://dl.bekencorp.com/tools/bkfil/v4)
- 使用 [BKFIL 网页烧录工具](https://connect.aclsemi.com/)

烧录时请选择上一节编译生成的 `all-app.bin` 固件文件。

主控详细烧录流程请参阅 [烧录代码](../../bk_avdk_smp/BK7258/get-started.md#smp-get-started-flash)。

<a id="id10"></a>

### 烧录从控

除 BK7258 主控固件外，BK3515NS 蓝牙从控还需单独烧录。
支持使用 BKFIL 烧录。

步骤 1：引出母板上 H2 的 BT\_P0 / BT\_P1 / BT\_RST / VBAT / GND，按以下方法接入串口小板

> - BT\_P0: 串口小板 rx，注意某些串口小板 tx / rx 是反的
> - BT\_P1: 串口小板 tx，注意某些串口小板 tx / rx 是反的
> - BT\_RST: 高
> - VBAT: 3.3V 供电
> - GND: 地

下载 [3515 固件](https://dl.bekencorp.com/armino_bin/smp_solution/bk_solution_dashboard/3515n_controller)

对应关系:

| EVB版本 | 对应固件目录 | 3515使用串口 | bk7258使用串口 |
| --- | --- | --- | --- |
| V1.1 20250904 | EVB\_v1.1\_20250904 | P10 P11 | P30 P31 |
| V1.2 20251027 | EVB\_v1.2\_20251027 | P0 P1 | P30 P31 |

步骤 2：打开 BKFIL

步骤 3：选择 flash 烧录，选择刚刚下载的 3515 固件。选择串口设置，更改对应的串口号

步骤 4：同时按住母板的 3515NS RESET / 7258 RESET 键，等待 5 秒，点击 BKFIL 下载按钮

步骤 5：松开 3515NS RESET，此时可以看到正在下载；如果失败，从步骤 4 重试

步骤 6：烧录成功会提示 Download successful，此时可以松开 7258 RESET

步骤 7：拔掉所有引出的线，按 7258 RESET 复位

也支持 [Beken\_BT\_Toolkit](https://dl.bekencorp.com/tools/Beken_Toolkit) 烧录方式，步骤同上，更换工具即可。

备注

尽量让母板不工作可以提高烧录成功率。

<a id="bk3515ns"></a>

### BK3515NS 校准

步骤 1：3515NS 需要发送命令校准，请参考

> - [BK3515NS Bluetooth Module Guide](https://dl.bekencorp.com/doc/smp_solution/bk_solution_dashboard/BK3515NS%20Bluetooth%20Module%20Guide/BK3515NS%20Bluetooth%20Module%20Guide.docx) 的 **频偏设置** 及 **功率设置** 章节
> - [rf测试\_hci交互](https://dl.bekencorp.com/doc/smp_solution/bk_solution_dashboard/rf%E6%B5%8B%E8%AF%95_hci%E4%BA%A4%E4%BA%92/rf%E6%B5%8B%E8%AF%95_hci%E4%BA%A4%E4%BA%92.txt) 的 **classic步骤** 章节进行非信令测试

步骤 2：校准完成后，参考该文件的进入 DUT 模式后，可以进行信令测试

步骤 3：校准值可以通过 3515 飞线发送命令保存，也可以保存在主控 CPU 端，然后开启 `components/bluetooth_secondary_controller/bsc_main.c` 的 `bsc_init` 函数中的 `TCI_READ_FRQ_OFFSET_FROM_FLASH` 和 `TCI_WRITE_POWER_TO_FLASH` 相关代码写入。

备注

如果从主控端下发，可以通过 `TCI_READ_FRQ_OFFSET_FROM_FLASH` 和 `TCI_READ_POWER_FROM_FLASH` 读取，和现有的比较，以避免每次开机写入。

<a id="id12"></a>

## 相关资源

- 应用处理器 AP 配置和使用，请参考 [Armino AP](../../bk_avdk_smp/BK7258/ap_doc/index.md)
- 通信处理器 CP 配置和使用，请参考 [Armino CP](../../bk_avdk_smp/BK7258/cp_doc/index.md)
