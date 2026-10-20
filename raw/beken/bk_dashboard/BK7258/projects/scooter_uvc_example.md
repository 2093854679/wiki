---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_dashboard/bk7258/zh_CN/v3.1.1/projects/scooter_uvc_example/index.html
sdk_family: bk_dashboard
chip: BK7258
processor: ''
sdk_version: v3.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="scooter-uvc"></a>

# Scooter项目 UVC示例工程

<a id="id1"></a>

## 快速开始

取码、编译环境和通用烧录见
[BK7258 两轮车方案快速入门](../get-started.md)。

本工程编译：

```
cd ~/armino/bk_solution_dashboard/projects/scooter_uvc_example
make bk7258 SDK_DIR=~/armino/bk_avdk_smp
```

本工程产物：

```
build/bk7258/scooter_uvc_example/package/all-app.bin
```

将该文件按方案快速入门中的 BKFIL 步骤烧录。BK3515NS 从控烧录见同一页。

<a id="id2"></a>

## 注意事项

- 暂时不支持投屏导航。

本工程（`scooter_uvc_example`）主要用于测试 UVC 功能（设备接入、预览显示链路、帧队列与解码显示流程）。

## 模块导航

- [两轮车方案简介](../intro.md)
- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [配套软件](../software.md)
- [参考工程](../projects.md)
- [scooter_1024_600开发指南](scooter_1024_600.md)
- [scooter_480_272开发指南](scooter_480_272.md)
- [scooter_480_272_v2开发指南](scooter_480_272_v2.md)
- [scooter_800_480开发指南](scooter_800_480.md)
- [scooter_800_480_v2开发指南](scooter_800_480_v2.md)
