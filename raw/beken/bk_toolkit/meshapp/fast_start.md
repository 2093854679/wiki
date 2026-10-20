---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/app/zh_CN/latest/fast_start/index.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速开始

<a id="id2"></a>

## 准备硬件

<a id="id3"></a>

### 串口板

串⼝板主要⽤于 USB 转串⼝。串口板如下图所示，图中标注位置的功能如下:

**位置1**: 需要短接，短接后被测板开机会进入到射频测试模式

**位置2**: 给被测模组供电的开关

**位置3**: 和电脑端USB相连接口

**位置4**: UART连接接口，需要和被测模组的DL UART相连

**位置5**: 和电脑端USB相连接口,功能同位置3

<a id="id8"></a>
[![serial_board](../../_assets/a00d5577536419a0e405-serial_board.jpg)](../../_assets/a00d5577536419a0e405-serial_board.jpg)


串口板

<a id="tester"></a>

### 校准板(TESTER)

校准板用于校准被测模组的射频性能。以下简称TESTER。如下图所示，图中标注位置的功能如下:

**位置1**: 和电脑端USB相连接口

**位置2**: 和被测模组SMA头相接接口

<a id="id9"></a>
[![tester_board](../../_assets/f86619dd29952197613e-tester_board.jpg)](../../_assets/f86619dd29952197613e-tester_board.jpg)


校准板

<a id="dut"></a>

### 被测模组或开发板(DUT)

被测模组或开发板为测试对象，以下简称DUT。如下图所示，图中标注位置的功能如下:

**位置1**: UART接口，用于和串口板\*\*位置4\*\*相连

**位置2**: 射频口，用于和校准板的\*\*位置2\*\*相连

<a id="id10"></a>
[![dut](../../_assets/c24012854054be872c22-dut.jpg)](../../_assets/c24012854054be872c22-dut.jpg)


DUT

<a id="id4"></a>

## 硬件连接

硬件连接示意图如下所示。

<a id="id11"></a>
[![serial_board](../../_assets/ff39d08f925918e956b5-connect_struct.png)](../../_assets/ff39d08f925918e956b5-connect_struct.png)


硬件连接示意图

<a id="testerdut"></a>

### 将串口板、TESTER、DUT相连接

连接后如下图所示。

[![connect](../../_assets/e82458f3c8e69d4c69e9-connect.jpg)](../../_assets/e82458f3c8e69d4c69e9-connect.jpg)

<a id="testerusb"></a>

### 将TESTER和串口板分别连接到电脑的USB口

连接后在设备管理器上可以看到对应的端口，如下图所示

[![serial_port](../../_assets/dabf1648320521f648a9-serial_port.png)](../../_assets/dabf1648320521f648a9-serial_port.png)

<a id="id5"></a>

## 软件配置

<a id="site"></a>

### 添加测试站点(SITE)

点击”Add Site” 按钮后，在工具窗口的右边会新加一个SITE，如下图所示。

[![add_site](../../_assets/c5b4274b1fc6d54c010e-add_site.png)](../../_assets/c5b4274b1fc6d54c010e-add_site.png)

<a id="id6"></a>

### 配置SITE信息

菜单栏点击 “Configuration” \=\> “SITE” 后，在弹出的SITE配置窗口中配置SITE。

其中包括:

**TESTER**: 串口号选择

**DUT**: 串口号选择

**MAC\_START**: 需要写入DUT的MAC地址

**MAC\_NUM**: 当前SITE需要测试多少块模组。

**MAC\_CURRENT**: 当前测试使用的MAC地址(执行测试时自动生成)

**ATTEN**: 线损值

备注

配置后，首次执行时，MAC\_CURRENT 为 MAC\_START 的值。后面每次执行时，会自动基于MAC\_CURRENT字段的值\+1，如果超出MAC\_START \+ MAC\_NUM 则不再变化

[![site_cfg](../../_assets/49cdb6c253a417f199c8-site_cfg.png)](../../_assets/49cdb6c253a417f199c8-site_cfg.png)

<a id="case"></a>

### CASE执行相关配置

菜单栏点击 “Configuration” \=\> “TEST CASE” 后，在弹出窗口中配置。

**Auto Start After Detect Dut**: “YES” 表示连接DUT后会自动开始执行测试

**Continue After Case fail**: “YES” 表示测试过程中其中一条CASE fail后继续执行后面的case

**DUT CHIP**: 选择DUT 芯片名称

**LOG LEVEL**: 选择log等级

[![case_set](../../_assets/4b36fd3ab7416124c9e4-case_set.png)](../../_assets/4b36fd3ab7416124c9e4-case_set.png)

<a id="id7"></a>

## 执行测试

点击”START” 开始执行测试

[![test_res](../../_assets/2ab53959edf1e77af461-test_res.png)](../../_assets/2ab53959edf1e77af461-test_res.png)
