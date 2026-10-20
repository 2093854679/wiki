---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/get-started/index.html
sdk_family: bk_matter
chip: BK7235,BK7236,BK7256,BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速入门

<a id="armino-matter-sdk"></a>

## Armino Matter SDK代码下载

您可从 gitlab 上下载 Armino Matter SDK:

```
git clone git@gitlab.bekencorp.com:armino/bk_matter.git
(git checkout到某个tag或者分支)
git submodule update --init --recursive
```

备注

从官网的gitlab下载的为最近的SDK代码，相关账号找项目上审核申请。

<a id="armino"></a>

## Armino 构建编译环境

请参考: [bk7236](../bk_idk/BK7236/get-started.md#id3) [bk7258](../bk_idk/BK7258/get-started.md)

**注意**： 推荐使用Ubuntu22.04版本及以上版本。

<a id="matter"></a>

## Matter 构建编译环境

1. 安装matter编译环境需要的依赖库

```
sudo apt-get install git gcc g++ pkg-config libssl-dev libdbus-1-dev
    libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev
    python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev
    python3-lark python3-jinja2
pip install stringcase
```

**注意**： Python要3.10及其以上版本。

2. 安装gn: 从 [这里](https://dl.bekencorp.com/tools/Matter/gn) 下载

```
sudo cp gn /usr/local/bin
sudo chmod +x /usr/local/bin
```

3. 确保 `ninja` 和 `gn` 已经安装成功

```
# 如果执行失败，请检查第一步依赖是否全部安装成功
ninja --version
# 如果执行失败，请检查第二部gn是否安装成功
gn --version
```

4. 编译

```
make bk7236 PROJECT=matter
# 注：首次make，建议先执行make clean。
#     如果编译过程中缺少python模块，编译器会提示ModuleNotFoundError，按照Error提示使用 pip install 安装相应的python模块即可继续编译。
```

5. 配置zap工具

```
# 当编译因找不到zap-cli或者zap工具出现错误时，需要将zap工具的路径添加到环境变量中，具体如下：
# 将zap工具加入 PATH 在shell直接执行临时修改PATH或者添加到 ~/.bashrc 中永久修改PATH
export PATH=<path-to-connectedhomeip>/zap/:$PATH
# 如果将zap路径添加到~/.bashrc中永久修改环境变量，立即生效需要执行
source ~/.bashrc
```

**zap工具简介**: [\[zap\]](https://github.com/project-chip/zap) 是一个可视化配置matter应用的工具。 关于zap工具及代码生成相关的详细内容, 可以参考 [官方文档](https://github.com/project-chip/connectedhomeip/blob/af74ecfe99276b9bef8ce21381a13ecbb128bb50/docs/code_generation.md)。
