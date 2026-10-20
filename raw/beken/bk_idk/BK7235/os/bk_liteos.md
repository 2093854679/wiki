---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/os/bk_liteos.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="liteos-m"></a>

# LiteOS-M 内核

<a id="id1"></a>

## LiteOS-M 简介

> - OpenHarmony LiteOS-M内核是面向IoT领域构建的轻量级物联网操作系统内核，具有小体积、低功耗、高性能的特点，其代码结构简单，主要包括内核最小功能集、内核抽象层、可选组件以及工程目录等，分为硬件相关层以及硬件无关层，硬件相关层提供统一的HAL（Hardware Abstraction Layer）接口，提升硬件易适配性，不同编译工具链和芯片架构的组合分类，满足AIoT类型丰富的硬件和编译工具链的拓展。其架构图如图1所示：

<a id="id6"></a>
![OpenHarmony-LiteOS-M Architecture](../../../_assets/dcd470f29c6160710397-OpenHarmony-LiteOS-M%E6%A0%B8%E5%86%85%E6%A0%B8%E6%9E%B6%E6%9E%84%E5%9B%BE.png)


OpenHarmony-LiteOS-M核内核架构图

<a id="id2"></a>

## 源码目录

> - 目录结构如下：

```
/kernel/liteos_m
├── components           # 可选组件
│   ├── backtrace        # 回溯栈支持
│   ├── cppsupport       # C++支持
│   ├── cpup             # CPUP功能
│   ├── dynlink          # 动态加载与链接
│   ├── exchook          # 异常钩子
│   ├── fs               # 文件系统
│   └── net              # Network功能
├── kal                  # 内核抽象层
│   ├── cmsis            # cmsis标准接口支持
│   └── posix            # posix标准接口支持
├── kernel               # 内核最小功能集支持
│   ├── arch             # 内核指令架构层代码
│   │   ├── arm          # arm32架构的代码
│   │   └── include      # 对外接口存放目录
│   ├── include          # 对外接口存放目录
│   └── src              # 内核最小功能集源码
├── targets              # 板级工程目录
├── utils                # 通用公共目录
```

<a id="id3"></a>

## 适用架构

> - 当前只适用于cortex-m3、cortex-m4、cortex-m7、risc-v芯片架构。

<a id="id4"></a>

## 源码获取

> - 参考(<https://gitee.com/openharmony/docs/blob/HEAD/zh-cn/device-dev/get-code/sourcecode-acquire.md>)。

<a id="id5"></a>

## LiteOS-M 版本

> - 当前Armino平台使用的版本号是：kernel\_liteos\_m-OpenHarmony-v3.0.1-LTS
