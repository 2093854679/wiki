---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ipc/bk7259/zh_CN/v4.0.1/projects/ptz_camera_frame/index.html
sdk_family: bk_ipc
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ptz-camera-frame-bk7259-smp"></a>

# ptz\_camera\_frame（BK7259 SMP 解决方案）

<a id="id1"></a>

## 1 这个工程是什么

`ptz_camera_frame` \= `ptz_camera` \+ 行中断 3DNR（时域降噪）。

除视频编码链路外，所有功能都与 `ptz_camera` 完全相同，而且:strong:不是复制一份代码：
`ap/CMakeLists.txt` 和 `cp/CMakeLists.txt` 直接编译 `../ptz_camera` 下的源文件，
所以云端注册、状态机、PTZ 电机、人形检测跟随、补光灯 / ISP 日夜策略、二维码配网、
ASR、BLE 配网、AP powerdown 保活等逻辑不可能与 `ptz_camera` 产生分叉。

工程本地只有 5 个源文件：

| 文件 | 说明 |
| --- | --- |
| `ap/ap_main.c` | `ptz_camera` 的同名文件 \+ 一行 `pt_dnr` CLI 注册；板级/ISP 配置刻意保持一字不差 |
| `ap/src/pt_frame_dnr_line.c` | 行中断组帧器：ring 取段、MVE 混合、双缓冲、帧尾发布、逐帧自动 alpha 决策 |
| `ap/src/pt_dma_copy.c` | HPDMA ch0 裸搬运，用于在行中断里预取 history |
| `ap/src/ptz_frame_bringup.c` | 帧模式 H264 编码器的创建/销毁 \+ `pt_dnr` CLI \+ OSD 接管 |
| `cp/vnd_cal.h` | 转发头（见 §4） |

<a id="id2"></a>

## 2 视频链路的差异

两个工程的 ISP 都工作在 **flexa（行）模式**，`ap_main.c` 的 camera board 配置完全一致
（GC20C3，1920×1080@20fps，NV12，MP 通道）。差异只在 ring buffer 之后：

```
ptz_camera（CONFIG_PT_MP_H264_FRAME_MODE 未定义）
  ISP MP flexa ring (SRAM)
    └─ bk_flexa_isp_h264e_bond_start：硬件 bond，编码器逐片消费，无降噪

ptz_camera_frame（CONFIG_PT_MP_H264_FRAME_MODE=y）
  ISP MP flexa ring (SRAM)
    └─ ISR_TYPE_16LINE_DONE（68 次/帧）
         ├─ HPDMA：history 16 行 PSRAM -> HSRAM 暂存
         └─ MVE blend（.itcm）：ring + history -> 组帧双缓冲（PSRAM，write-through）
    └─ ISR_TYPE_FRAME_COMPLETE：发布整帧，翻转双缓冲
         └─ worker 线程 -> 帧模式 H264 编码器
              └─ encoded_data_manager -> doorbell 图传（与 ptz_camera 相同）
```

编码器下游（encoded-data manager、doorbell 图传、背压丢帧策略、时间戳 OSD）保持不变。
码控沿用 `ptz_camera` 的 `CONFIG_H264_QP_PRESET_BALANCED` （1.5Mbps），
GOP 沿用 `app_codec.c` 里 flexa 编码器用的 **40**，
因此两个工程产出的码流特性可以直接对比。

分支切换点在 `components/smart_ipc/src/doorbell_devices.c`：它按
`CONFIG_PT_MP_H264_FRAME_MODE` 决定调用 `pt_camera_frame_codec_bond_start()`
还是走原来的 `app_h264e_turn_on()` \+ flexa bond。该宏在 `ptz_camera` 中未定义，
所以这个新工程对 `ptz_camera` 零影响。

\> 函数名 `pt_camera_frame_codec_bond_start/stop` 由该组件硬编码，
\> 虽然工程叫 `ptz_camera_frame`，也:strong:[<a id="id4"></a>
\`](#id3)不要\`改名。

<a id="id5"></a>

## 3 配置项

`ap/Kconfig.projbuild`：

| 配置 | 默认 | 说明 |
| --- | --- | --- |
| `CONFIG_PT_MP_H264_FRAME_MODE` | y | 关掉它，本工程在功能上就退化成 `ptz_camera` |
| `CONFIG_PT_DNR_LINE_BOOST_ISP_IRQ` | y | 把 `INT_SRC_ISP_MI` 优先级从默认 6 抬到 5 |
| `CONFIG_PT_DNR_LINE_ISP_IRQ_PRIO` | 5 | 数值越小越紧急 |
| `CONFIG_PT_DNR_LINE_DROP_ON_IFRAME` | y | I 帧编码期间放弃正在组装的帧，避免撕裂 |

`ap/config/bk7259_ap/defconfig` 相对 `ptz_camera` 只多两行：
`CONFIG_PT_MP_H264_FRAME_MODE=y` 与 `CONFIG_BK_ENCODER_H264_FRAME_TASK_PRIORITY=1`。

<a id="cp-vnd-cal-h"></a>

## 4 关于 `cp/vnd_cal.h`

CP 侧代码 100% 复用 `../ptz_camera/cp`，但 SDK 的 `cp/components/bk_init/bk_init.c`
用 `#include "vnd_cal.h"` 去找它，依赖构建系统隐式添加的 `-I<工程>/cp`，
而这个路径只会指向本工程目录。因此这里放一个转发头指向 `../ptz_camera/cp/vnd_cal.h`，
而不是复制一份校准表。

<a id="cli"></a>

## 5 CLI

在 `ptz_camera` 的 `pt_state` / `pt_cloud` / `pt_isp_luma` 之外，本工程多一条：

```
pt_dnr status              # 模式 + 最近一次 AUTO 评估 + 发布/丢帧计数
pt_dnr auto | on | off     # AUTO = 恒 blend + 决策树 alpha；on/off 手动强制
pt_dnr alpha <1..255>      # 手动当前帧权重，会切换到 manual-on
pt_dnr tbl get             # 打印 AUTO alpha 决策树（叶子 a..o）
pt_dnr tbl set <a-o> <1..255> [...]  # 运行时修改决策树叶子
pt_dnr trace on | off      # 逐帧打印 AUTO alpha 决策
```

AUTO 下每帧都做 blend，与 `isp_h264_tuning_3dnr` 一致；权重来自 15 叶决策
树，输入是 ISO（噪声）和上一编码帧的 intra 8x8 CU 数（运动量）：ISO 越高
降噪越强，运动越大降噪越弱以避免拖影。`pt_dnr alpha` 会切换到 manual-on
从而绕过决策树；`pt_dnr off` 直通不 blend。

`pt_dnr status` 里三个丢帧计数的含义不同，排查时不要混用：
`drop_busy` 表示编码器或网络消费不过来，`drop_iframe` 是 I 帧保护主动丢的，
`drop_isp_err` 表示 ISP 报了坏帧。

<a id="id6"></a>

## 6 快速开始

取码、编译环境和通用烧录见
[BK7259 IPC 方案快速入门](../get-started.md)。

本工程编译：

```
cd ~/armino/bk_solution_ipc/projects/ptz_camera_frame
make bk7259 SDK_DIR=~/armino/bk_avdk_smp PROJECT=ptz_camera_frame
```

本工程产物：

```
build/bk7259/ptz_camera_frame/package/all-app.bin
```

将该文件按方案快速入门中的 BKFIL 步骤烧录。

\> AP FLASH 占用约 99.4%（4148K 分区），仅比 `ptz_camera` 多约 9KB。
\> 后续再往 AP 侧加功能前，需要先确认 `partitions/bk7259/auto_partitions.csv` 的余量。
