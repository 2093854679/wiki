---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/api-reference/nand_disk_note.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="nand"></a>

# Nand磁盘使用注意事项

<a id="id1"></a>

## nand磁盘连接注意事项

当USB线通过Type-C线先连接开发板时，因Type-C线默认的USB DP/DN数据线检测设备时，此时板子的USB驱动未初始化，导致USB Host(计算机)无法直接与板子连接通信，可以在PC端设备管理器中再次刷新USB设备，识别出板子的U盘功能。

<a id="id2"></a>

## 磁盘格式化注意事项

在windows平台上，第一次对nand磁盘进行格式化时，可能由于没有文件系统，没有办法直接格式化。在文件浏览器中只出现盘符，而无法格式化，如下图。

<a id="id3"></a>
![nand disk not formatted.](../../../_assets/83a7998a21a0d527b503-disk_fomat_computer.png)


nand disk not formatted

出现这种情况时，需要打开磁盘管理窗口，并找到nand磁盘，如下图。

<a id="id4"></a>
![disk management windows.](../../../_assets/446f9c5dcf2d6c95e847-disk_fomat_disk_manager.png)


disk management windows

通过新建卷来进行格式化磁盘，文件系统格式选择FAT32，并设置盘符和分配单元大小。

<a id="id5"></a>
![add disk for nand disk .](../../../_assets/48c52cdf35f054d4de3a-disk_fomat_new_disk.png)


add disk for nand disk

<a id="id6"></a>
![set file system format for nand disk.](../../../_assets/6138e8a3c39d1b328c6a-disk_fomat_type.png)


set file system format for nand disk

之后再文件管理器中即可正常使用nand磁盘，如下图。

<a id="id7"></a>
![normal nand disk.](../../../_assets/8697438dabc077503b25-disk_fomat_normal.png)


normal nand disk

## 模块导航

- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [API 参考](../api-reference.md)
- [api-reference](../api-reference.md)
- [Gsensor API使用及算法demo](gsensor_link.md)
- [Nfc API介绍](nfc_link.md)
- [aud_intf API使用说明](bk_aud_intf.md)
- [TensorFlow Lite Micro开发指南](tensorflow.md)
- [参考工程](../projects.md)
- [第三方文档](../thirdparty.md)
