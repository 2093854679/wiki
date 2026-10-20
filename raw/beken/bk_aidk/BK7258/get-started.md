---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/get-started/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速入门

<a id="armino-aidk-sdk"></a>

## Armino AIDK SDK代码下载

您可从 gitlab 上下载 Armino AIDK SDK, 分支信息如下:

```
mkdir -p ~/armino
cd ~/armino
git clone --recurse-submodules https://gitlab.bekencorp.com/armino/bk_ai/bk_aidk.git -b ai_release/v2.0.1
```

AIDK在gitlab上的分支是ai\_release/v2.0.1, 如果需要取特定的版本, 可以将branch\_name替换成tag:

```
git clone --recurse-submodules https://gitlab.bekencorp.com/armino/bk_ai/bk_aidk.git -b ai_release/v2.0.1.x
```

如果您还没有gitlab账号, 您可从 [github](https://github.com/bekencorp/bk_aidk) 上下载 Armino AIDK SDK, 分支信息如下:

```
mkdir -p ~/armino
cd ~/armino
git clone --recurse-submodules git@github.com:bekencorp/bk_aidk.git -b ai_release/v2.0.1
```

备注

github上bk\_avdk\_ai仓库和bk\_idk\_ai仓库都是bk\_aidk仓库的子仓库, 使用上述git clone –recurse-submodules命令下载bk\_aidk仓库即可

<a id="armino-aidk"></a>

## Armino AIDK 工程编译

进入AIDK目录，编译beken\_genie工程:

```
cd ~/armino
make bk7258 PROJECT=beken_genie
```

在编译完成后，在build/beken\_genie/bk7258目录下将生成all-app.bin，使用烧录工具烧录到开发板即可。

<a id="id2"></a>

## 环境配置及烧录代码

Armino 支持在 Windows/Linux 平台进行固件烧录, 烧录方法参考烧录工具中指导文档。
以Windows 平台为例， Armino 目前支持 UART 烧录。

具体 [烧录流程](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v_ai_2.0.1/get-started/index.html) 请参考 [IDK](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v_ai_2.0.1/index.html)
