# factory-data 配置工具[](#factory-data "永久链接至标题")

[[English]](../../../../en/v2.0.1/matter-tools/factory-data/index.html "../../../../en/v2.0.1/matter-tools/factory-data/index.html")


## 如果使用私有的PAI、DAC证书以及其他的配置信息，需要进行以下配置[](#paidac "永久链接至标题")

1.将工程配置成使用私有配置信息的设备

> 在 connectedhomeip/src/platform/Beken/CHIPDevicePlatformConfig.h 中将 CONFIG_ENABLE_BEKEN_DEVICE_INFO 配置为 1。 如下所示：
>
> `#define  CONFIG_ENABLE_BEKEN_DEVICE_INFO  1`
>
> 注意：如果 CONFIG_ENABLE_BEKEN_DEVICE_INFO 为0，表示设备使用Matter协议默认的配置信息。

2.生成factory_data.bin的步骤

> 在工程的 toosls/matter_factory_data_generate 文件夹下配置私有设备的信息。通过配置.gen.sh脚本，以便生成想要的bin文件。
>
> `python main.py generate --cd ./cd.bin --pai ./Chip-PAI-Cert.der --dac ./Chip-DAC-Cert_01.der --dac_key ./Chip-DAC-Key_01.der --vendor_name BEKEN --vendor_id 0x1342 --product_name lighting --product_id 0x03ed -o factory_data.bin`
>
> 在 toosls/matter_factory_data_generate 文件夹中提供了三对儿DAC和DAC_KEY，dac和dac_key需要成对使用。如有需要，可以使用PAI和PAI_KEY再生成更多的DAC和DAC_KEY。可以灵活设置 vendor_name、product_name、serial-num、hardware-ver等参数。参数配置完成后，运行./gen.sh 即可生成factory_data.bin。
>
> 注意：此路径中提供的PAI、DAC和CD证书都是基于 vendor_id 为0x1342，product_id 为0x03ed生成的，这两个参数不要修改。除非根据私有的 vendor_id 和 product_id 重新签名了PAI、DAC和CD证书。

3.烧写factory_data.bin

> 在bk_loder的工具中选中factory_data.bin之所在的位置，设置factory_data.bin在Flash中的起始地址。如下所示：
>
> [![../../_images/factory_data_wirte_to_flash.png](../_images/factory_data_wirte_to_flash.png)](../../_images/factory_data_wirte_to_flash.png "../../_images/factory_data_wirte_to_flash.png")
>
> 如果设备是BK7236,factory_data.bin在Flash中的起始地址,为vendor_flash.c中全局变量bk_flash_partiton中matter_factory分区的起始地址。如果设备是BK7231n或者BK7238，factory_data.bin在Flash中的起始地址,为BkDriverFlash.c中全局变量bk7231_partiton_2M（Flash为2M大小）或者bk7231_partiton_4M（Flash为4M大小）matter factory info分区的起始地址。


## factory_data.bin包含的信息[](#factory-data-bin "永久链接至标题")

matter_factory_data_generate工具用于将Matter设备所需要等证书等出厂配置信息打包到bin文件，烧录到设备。

matter_factory_data_tool 可以将以下配置信息打包成bin文件，烧录到设备flash指定地址位置，方便生产时对设备的配置。

设备证书配置[](#id1 "永久链接至表格")

|  |  |
| --- | --- |
| cert-dclrn | 由CSA联盟颁发的CD |
| dac-cert | dac证书 |
| pai-cert | pai证书 |
| dac-pub-key | dac公钥 |
| dac-key | dac私钥 |

设备配网信息配置[](#id2 "永久链接至表格")

|  |  |
| --- | --- |
| discriminator | 配网鉴别码 |
| iteration-count | PAKE迭代次数 |
| salt | PAKE盐值 |
| verifier | PAKEPasscodeVerifier字段 |
| pin-code | 密码 |

设备基本信息配置[](#id3 "永久链接至表格")

|  |  |
| --- | --- |
| vendor-name | 设备制造商名字 |
| vendor-id | 设备制造商VID |
| product-name | 产品名字 |
| product-id | 产品PID |
| serial-num | 序列号 |
| mfg-date | 产品生产日期 |
| hardware-ver | 硬件版本号 |
| hw-ver-str | 硬件版本号字符串 |
| rd-id-uid | 轮换设备标识符 |
| product-label | 产品标签 |
| product-url | 产品url |
