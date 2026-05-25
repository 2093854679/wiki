# **OTA cli命令**[](#ota-cli "永久链接至标题")

[[English]](../../../../../en/v2.2.1/examples/cli/ota/ota_cli.html "../../../../../en/v2.2.1/examples/cli/ota/ota_cli.html")

重要


*用于ota升级测试使用*


- [http_ota](#ota-otacli "#ota-otacli") :OTA升级命令


## [http_ota](#ota-cli "#ota-cli") **:执行OTA升级命令**[](#http-ota-ota "永久链接至标题")


**命令**


```
http_ota url

```


**参数**


```
url:想要升级的rbl文件位置（通常位于HTTP服务器上）

```


**使用场景**


```
1）通过编译生成想要升级版本的rbl文件

2）rbl文件所在路径---build/app/bk7239n/encrypt/app_pack.rbl

3）在windows电脑上使用Everything创建HTTP服务器,拷贝url

4）使用命令进行升级：

        http_ota http://192.168.21.101/D%3A/E/build/app_pack.rbl

```


**响应**


```
CMDRSP:OK

CMDRSP:ERROR

```

备注


*本命令在CONFIG_OTA_HTTP开启且CONFIG_SECURITY_OTA不开启下生效!*
