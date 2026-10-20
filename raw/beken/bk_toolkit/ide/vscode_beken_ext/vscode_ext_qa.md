---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ide/ide/zh_CN/v2.0.1/vscode_beken_ext/vscode_ext_qa/index.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 常见问题

<a id="debug-can-not-open-usb"></a>

## 1\. `Debug`报错: `Can not open usb`

<a id="id2"></a>
![debug_error_1](../../../_assets/9d69cdf407983e9f65ac-debug_error_1.png)


debug\_error\_1

可能原因:

1. 硬件连接断开
2. 驱动未安装 (见`Debug`**驱动安装**步骤)

<a id="debug-gb-server-assertion-info-addrbits-0-failed-file-cygdrive-d-jenkins-workspace-build-system-3-source-packages-openoc-0-10-0-src-target-riscv-riscv-011-c-line-435-function-dbus-scan"></a>

## 2\. Debug报错: `[GB_SERVER] assertion "info-›addrbits != 0" failed: file "/cygdrive/d/Jenkins/workspace/build-system-3/source-packages/openoc-0.10.0/src/target/riscv/riscv-011.c", line 435, function: dbus scan`

<a id="id3"></a>
![debug_error_0](../../../_assets/23a3c645acda2420ae00-debug_error_0.png)


debug\_error\_0

可能原因: 未设置DEBUG模式 （见`Debug`**软件设置DEBUG模式**步骤）

## 模块导航

- [文档](../vscode_beken_ext.md)
- [简介](vscode_ext_guide.md)
- [安装](vscode_ext_install.md)
- [使用说明](vscode_ext_usage.md)
- [版本历史](vscode_ext_history.md)
