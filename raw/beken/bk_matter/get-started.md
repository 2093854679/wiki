# 快速入门[](#id1 "永久链接至标题")

[[English]](../../../en/v2.0.1/get-started/index.html "../../../en/v2.0.1/get-started/index.html")


## Armino Matter SDK代码下载[](#armino-matter-sdk "永久链接至标题")

您可从 gitlab 上下载 Armino Matter SDK:


```
git clone git@gitlab.bekencorp.com:armino/bk_matter.git
(git checkout到某个tag或者分支)
git submodule update --init --recursive

```

备注

从官网的gitlab下载的为最近的SDK代码，相关账号找项目上审核申请。


## Armino 构建编译环境[](#armino "永久链接至标题")

请参考: [bk7236](https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/get-started/index.html#id3 "https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/get-started/index.html#id3") [bk7258](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/get-started/index.html#id3 "https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/get-started/index.html#id3")


**注意**： 推荐使用Ubuntu22.04版本及以上版本。


## Matter 构建编译环境[](#matter "永久链接至标题")

1. 安装matter编译环境需要的依赖库


```
sudo apt-get install git gcc g++ pkg-config libssl-dev libdbus-1-dev
    libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev
    python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev
    python3-lark python3-jinja2
pip install stringcase

```


**注意**： Python要3.10及其以上版本。

2. 安装gn: 从 [这里](https://dl.bekencorp.com/tools/Matter/gn "https://dl.bekencorp.com/tools/Matter/gn") 下载


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


**zap工具简介**: [[zap]](https://github.com/project-chip/zap "https://github.com/project-chip/zap") 是一个可视化配置matter应用的工具。 关于zap工具及代码生成相关的详细内容, 可以参考 [官方文档](https://github.com/project-chip/connectedhomeip/blob/af74ecfe99276b9bef8ce21381a13ecbb128bb50/docs/code_generation.md "https://github.com/project-chip/connectedhomeip/blob/af74ecfe99276b9bef8ce21381a13ecbb128bb50/docs/code_generation.md")。
