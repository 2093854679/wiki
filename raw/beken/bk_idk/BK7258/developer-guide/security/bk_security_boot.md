---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/developer-guide/security/bk_security_boot.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 安全启动

安全启动用于对要执行的程序进行校验，只有在确保程序合法且完整时下才允许启动系统，否则启动失败。
安全启动是系统的安全基础。

<a id="id2"></a>

## 概述

BK7258 支持传统下载模式与安全启动模式。当 EFUSE BIT(3) 为 0 时为传统下载模式，为 1 时为安全启动模式。

![8](../../../../_assets/c5653b6de781ecb46ce8-bl1_overview.svg)

如上图所示，BK7258 安全启动分两阶段。系统上电之后，固化在芯片中的 BL1 先对 BL2 验签，验签通过之后跳转到 BL2；
然后 BL2 对其他所有程序进行验签。

<a id="bl1"></a>

## BL1 启动流程

![8](../../../../_assets/9b1f23ba455b94f69ad7-bl1_verify_1.svg)

为支持 BL2 升级，FLASH 中设有 Primary BL2 与 Secondary BL2，并通过存放在 FLASH 中的 boot\_flag 来
指示应该优先选择哪份 BL2 进行启动。启动流程如上图所示，当优先的 BL2 验签成功时，从优先的 BL2 启动；
否则偿试对非优先 BL2 进行验签，如果验签成功，则从非优先 BL2 进行启动，并更新 boot\_flag；如果两份 BL2
均验签失败，则启动中止。

![8](../../../../_assets/775b08bb182559c6716b-bl1_verify_2.svg)

上图描述了 BL1 对单个 BL2 验签的流程（以 Primary BL2 为例）：

> - 1 \- boot\_flag 指示优先验签的 BL2 为 primary\_bl2，准备对 primary\_bl2 进行验签。
> - 2 \- BL1 先从 FLASH 固定位置读取 primary\_manifest，primary\_manifest 放在 primary\_manifest 分区，
>   其中打包了 BL1 在验签时需要的所有信息，包括加签算法，image HASH 算法，image 版本，公钥等。BL1 先
>   读出安全启动公钥，计算出公钥 HASH，然后与固化在 OTP 中的公钥 HASH 进行对比，如果相同，则继续，否则，
>   验签失败。
> - 3 \- BL1 使用第 2 步中验证合法的公钥对 primary\_manifest 进行验签。其中 manifest signature 是对除
>   manifest signature 外 primary\_manifest 中所有信息的签名。如果验签通过，则继续；否则，验签失败。
> - 4 \- BL1 使用 primary\_manifest 中指定的 HASH 算法（SHA256）对 primary\_bl2 计算 HASH，然后与 primary\_manifest
>   中的 image hash 进行比较，如果相同则继续，否则，验签失败。
> - 5 \- 如果 primary\_manifest 中 image version 不小于 OTP 中的 image version，则验签成功，否则，验签失败。

<a id="bl2"></a>

## BL2 启动流程

BK7258 BL2 为开源 MCUBOOT 1.9.0，因此验签流程保持与官方 MCUBOOT 一致。本节仅对 BK7258 配置特别点及
MCUBOOT 验签流程做概述，如果想了解 MCUBOOT 详细验签流程，或者 MCUBOOT 其他功能，如升级，防回
滚等，可参考 [MCUBOOT 官网](https://docs.mcuboot.com)。

![8](../../../../_assets/e7db11baf589e37f063c-bl2_verify.svg)

如上图所示，BL2 要验签的对象为 tfm\_s.bin 与 app.bin (即 CPU0 APP)，分别放在 tfm\_s 与 cpu0\_app 两个
FLASH 分区中，构建系统加签步骤为：

> - 首先对 tfm\_s.bin/app.bin 进行 AES 加密，加 CRC，形成 tfm\_s\_crc\_aes.bin/cpu0\_app\_crc\_aes.bin。
> - 然后将 tfm\_s\_crc\_aes.bin/cpu0\_app\_crc\_aes.bin 放置在 partition 中，并增加相应的 padding。
> - 接着使用 MCUBOOT 加签工具对合并且 padding 后的 image（见上图浅绿色部分）进行加签。

备注

BK7258 MCUBOOT 加签特别点是不能简单地合并两个 BIN 之后加签，必须先增加 padding，然后再
合并，这是因为需要考虑 FLASH CRC，增加 padding 的目的是确保 BIN 的起始地址落在 FLASH 的
CRC 块对齐，且 BIN Vector Table 512 字节对齐上。

MCUBOOT 的验签流程可概述如下：

> - 1 \- 首先读取 BL2 TLV 中的 IMAGE\_TLV\_PUBKEY 或 IMAGE\_TLV\_KEYHASH，与 OTP 中 PUBKEY\_HASH 对比，如果相同
>   则继续，否则验签失败。
> - 2 \- 计算合并 IMAGE 的 HASH，与 TLV 中 IMAGE\_TLV\_SHA256 对比，相同则继续，否则验签失败。
> - 3 \- 使用步骤 1 中的公钥，对 TLV 中 EXPECTED\_SIG\_TLV 进行验签，验签通过则继续，否则失败。
> - 4 \- TLV 中 IMAGE\_TLV\_SEC\_CNT 不小 NV 中的 security counter，则验签成功，否则失败。

<a id="id3"></a>

## 安全启动配置

<a id="s1"></a>

### S1 \- 生成密钥

重要

FLASH AES KEY，BL1/BL2 私钥是系统安全的保证，请妥善保管！

<a id="bk-security-boot-bl1-key"></a>

<a id="id4"></a>

#### BL1 密钥

可通过 openssl 生成 BL1 密钥对。

EC256 私钥生成方法:

```
openssl ecparam -name secp256r1 -genkey -out ec256_privkey.pem
```

EC256 公钥生成方法:

```
openssl ec -in ec256_privkey.pem -inform PEM -out ec256_pubkey.pem -pubout
```

EC521 与 EC256 类似，只需将 name 参数由 secp256r1 改成 secp521r1 即可。

备注

BL1 使用 EC521 验签的时间是 EC256 的 2 倍以上，一般建议使用 EC256。

RSA1024 私钥生成方法:

```
openssl genrsa -out rsa1024_privkey.pem 1024
```

RSA1024 公钥生成方法:

```
openssl rsa -in rsa1024_privkey.pem -inform PEM -out rsa1024_pubkey.pem -pubout
```

RSA2048 与 RSA1024 类似，只需将公钥对长度由 1024 改成 2048 即可。

这一步生成的公钥对需要配置到安全启动配置表与 OTP 中。

<a id="bk-security-boot-bl2-key"></a>

<a id="id5"></a>

#### BL2 密钥

BL2 密钥通过 ./tools/env\_tools/mcuboot\_tools/imgtool.py 生成：

```
./tools/env_tools/mcuboot_tools/imgtool.py keygen -k filename.pem -t rsa-2048
```

密钥类型还可选择 rsa-3072, ecdsa-p256, or ed25519。还可以通过 -p 选项来对 BL2 密钥进行保护，
-p 选项会提示输入一个密码。通过这种方式生成的 BL2 密钥，后续每次使用时，都要求输入一个密码。

可通过 [MCUBOOT imgtool](https://docs.mcuboot.com/imgtool.html) 进一步了解 MCUBOOT imgtool。

生成密钥之后，还需要将密钥配置到分区表与 OTP 中。可通过配置 primary\_bl2 分区中的 verify\_algorithm
来配置签名类型，配置 primary\_bl2 分区中的 pubkey 与 privkey 指定生成的公/私钥文件。

这一步生成的公钥对需要配置到安全启动配置表与 OTP 中。

**TODO: 描述将公钥集成到 MCUBOOT or 公钥 HASH 集成到 OTP 中的方法。**

<a id="flash"></a>

<a id="bk-security-boot-flash-key"></a>

#### FLASH 密钥

FLASH AES 密钥为 64 字节随机数，您可使用任意足够随机的字节作为 FLASH AES KEY，或者通过
Armino 自带工具生成：

```
./tools/env_tools/beken_packager/cmake_xts_aes genkey 64 -outfile key.txt
```

这一步生成的 FLASH AES KEY 需要配置到安全启动配置表与 OTP 中。

<a id="s2"></a>

### S2 \- 配置分区表

在分区表 partitions.csv 中配置安全启动分区，请参考 [安全启动模式分区配置](../config_tools/bk_config_partitions.md#bk-config-partitions-secureboot)。

<a id="s3"></a>

### S3 \- 安全配置

在安全配置表 security.csv 中配置安全启动选项：

> - 将 `secureboot` 设置成 TRUE
> - 如果使能 FLASH AES 加密，则将 `flash_aes_en` 配置成 TRUE，
>   并将 [步骤 S1](#bk-security-boot-flash-key) 中生成的 AES KEY 配置到 `flash_aes_key`。
> - 将 [步骤 S1](#bk-security-boot-bl1-key) 中生成的公/私钥文件配置到 `root_pubkey` 与 `root_privkey`。

详情请参考 [安全配置](../config_tools/bk_config_security.md#bk-config-security)。

<a id="s4-otp-efuse"></a>

### S4 \- 配置 OTP/EFUSE

以 Armino 构建时生成的 otp\_efuse\_config.json 文件为基础，通过 BKFIL 将下述密钥部署到 OTP 中：

> - FLASH AES KEY。
> - BL1 安全启动公钥 HASH。
> - BL2 安全启动公钥 HASH。

请参考 [OTP EFUSE 配置](../config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse) 中方法来配置上述 OTP 项。

<a id="s5"></a>

### S5 \- 烧录版本

通过 BKFIL 烧录安全启动代码。

<a id="s6"></a>

### S6 \- 使能安全启动

当版本成功烧录后，可以使能安全启动与 FLASH 加密功能。请参考 [OTP EFUSE 配置](../config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse) 中方法来配置上述 OTP 项。

重要

安全启动使能前请确保烧录的版本支持 OTA，这可通过在下载模式下进行验证。

<a id="s7"></a>

### S7 \- 使能更多安全开关

部署完 S1\~S5 之后，可打开更多安全开关，例如关闭 BL1 调试模式，禁用 SPI 等。

重要

在尚未成功在任何板子上部署某个安全启动版本前，建议先不要关闭 BL1 调试模式，通过
BL1 打印信息可更快定位安全启动失败原因。同时，也建议不要禁用 SPI，因为一旦安全启动
使能，就无法通过 UART 下载版本，这些，如果安全启动部署失败，还可通过 SPI 烧录版本。
在确认 S1\~S6 准确无误之后再关闭 BL1 调试模式，禁用 SPI 等。

备注

当使用上述步骤在某块板子上成功配置了安全启动之后，可以将步骤 S4\~S6 合并成一步，通过
BKFIL 将安全启动版本，OTP 密钥配置以及 EFUSE 安全开关使能一次性部署到板子上。通常工
厂部署量产版本时，建议使用合并步骤简化部署流程。
