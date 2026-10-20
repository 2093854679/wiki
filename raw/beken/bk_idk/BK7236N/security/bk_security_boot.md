---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/security/bk_security_boot.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
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

BK7236N 支持传统下载模式与安全启动模式。当 EFUSE BIT(3) 为 0 时为传统下载模式，为 1 时为安全启动模式。

![8](../../../_assets/1720dbac6caa76bedb1d-bl1_overview.svg)

如上图所示，BK7236N 安全启动分两阶段。系统上电之后，固化在芯片中的 BL1 先对 BL2 验签，验签通过之后跳转到 BL2；
然后 BL2 对其他所有程序进行验签。

<a id="bl1"></a>

## BL1 启动流程

![8](../../../_assets/a5ce6b11c1ec658cea30-bl1_verify_2.svg)

上图描述了 BL1 对 BL2 验签的流程：

> - 1 \- BL1 先从 FLASH 固定位置读取boot\_flag信息，
>
> > - 如果 boot\_flag 等于0或者1 时，表示后续需要从主分区primary\_manifest 读取相应数据进行校验。
> > - 如果 boot\_flag 等于2，那么表示后续需要从恢复区recovery manifest 读取相应数据进行校验。
> >
> > > 两个分区的存储地址不同，且各自在打包时包含了BL1 在验签时需要的所有信息，包括加签算法，image HASH
> > > 算法，image 版本，公钥等。BL1 先读出安全启动公钥，计算出公钥HASH，然后与固化在 OTP 中的公钥 HASH
> > > 进行对比，如果相同，则继续，否则，验签失败。
>
> - 2 \- BL1 使用第 1 步中验证合法的公钥对 manifest 进行验签。其中 manifest signature 是对除
>   manifest signature 外 manifest 中所有信息的签名。如果验签通过，则继续；否则，验签失败。
> - 3 \- BL1 使用 manifest 中指定的 HASH 算法（SHA256）对 bl2 计算 HASH，然后与 manifest
>   中的 image hash 进行比较，如果相同则继续，否则，验签失败。
> - 4 \- 如果 manifest 中 image version 不小于 OTP 中的 image version，则验签成功，否则，验签失败。

<a id="bl2"></a>

## BL2 启动流程

BK7236N BL2 为开源 MCUBOOT 1.9.0，因此验签流程保持与官方 MCUBOOT 一致。本节仅对 BK7236N 配置特别点及
MCUBOOT 验签流程做概述，如果想了解 MCUBOOT 详细验签流程，或者 MCUBOOT 其他功能，如升级，防回
滚等，可参考 [MCUBOOT 官网](https://docs.mcuboot.com)。

![8](../../../_assets/46074eb4dbece59ef57e-bl2_verify.svg)

如上图所示，BL2 要验签的对象为 tfm\_s.bin 与 app.bin (即 CPU0 APP)，分别放在 tfm\_s 与 cpu0\_app 两个
FLASH 分区中，构建系统加签步骤为：

> - 首先对 tfm\_s.bin/app.bin 进行 AES 加密，加 CRC，形成 tfm\_s\_crc\_aes.bin/cpu0\_app\_crc\_aes.bin。
> - 然后将 tfm\_s\_crc\_aes.bin/cpu0\_app\_crc\_aes.bin 放置在 partition 中，并增加相应的 padding。
> - 接着使用 MCUBOOT 加签工具对合并且 padding 后的 image（见上图浅绿色部分）进行加签。

备注

BK7236N MCUBOOT 加签特别点是不能简单地合并两个 BIN 之后加签，必须先增加 padding，然后再
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

**描述将公钥集成到 MCUBOOT or 公钥 HASH 集成到 OTP 中的方法。**

<a id="flash"></a>

<a id="bk-security-boot-flash-key"></a>

#### FLASH 密钥

FLASH AES 密钥为 32 字节固定密钥，建议您将密钥写入到该安全工程中security.csv 中，flash\_aes\_type类型为FIXED，
flash\_aes\_key 字段后面是32字节用户输入的固定密钥，例如：

```
flash_aes_key,73c7bf397f2ad6bf4e7403a7b965dc5ce0645df039c2d69c814ffb403183fb18
```

这一步配置的 FLASH AES KEY 需要配置到安全启动配置表与 OTP 中。

<a id="s2"></a>

### S2 \- 配置分区表

在分区表 partitions.csv 中配置安全启动分区，请参考 [安全启动模式分区配置](../developer-guide/config_tools/bk_config_partitions.md#bk-config-partitions-secureboot)。

<a id="s3"></a>

### S3 \- 安全配置

在安全配置表 security.csv 中配置安全启动选项：

> - 将 `secureboot_en` 设置成 TRUE
> - 如果使能 FLASH AES 加密，则将 `flash_aes_type` 配置成 FIXED
>   并将 [步骤 S1](#bk-security-boot-flash-key) 中生成的 AES KEY 配置到 `flash_aes_key`。
> - 将 [步骤 S1](#bk-security-boot-bl1-key) 中生成的公/私钥文件配置到 `root_pubkey` 与 `root_privkey`。

详情请参考 [安全配置](../developer-guide/config_tools/bk_config_security.md#bk-config-security)。

<a id="s4-otp"></a>

### S4 \- 配置 OTP

以 Armino 构建时生成的 otp\_efuse\_config.json 文件为基础，通过 BKFIL 将下述密钥部署到 OTP 中：

> - FLASH AES KEY。
> - BL1 安全启动公钥 HASH。
> - BL2 安全启动公钥 HASH。

请参考 [OTP EFUSE 配置](../developer-guide/config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse) 中方法来配置上述 OTP 项。

<a id="s5"></a>

### S5 \- 烧录版本

通过 BKFIL 烧录安全启动代码。

<a id="s6"></a>

### S6 \- 使能安全启动

当版本成功烧录后，可以使能安全启动与 FLASH 加密功能。请参考 [OTP EFUSE 配置](../developer-guide/config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse) 中方法来配置上述 OTP 项。

重要

安全启动使能前请确保烧录的版本支持 OTA。

<a id="s7"></a>

### S7 \- 使能更多安全开关

部署完 S1\~S5 之后，可打开更多安全开关，例如关闭 BL1 调试模式，禁用 SPI 等。

重要

在尚未成功在任何板子上部署某个安全启动版本前，建议先不要关闭 BL1 调试模式，通过
BL1 打印信息可更快定位安全启动失败原因。同时，也建议不要禁用 SPI，因为一旦安全启动
使能，就无法通过 BKFIL 烧录 BL2，如果发现 BL2 有问题，还可通过 SPI 烧录版本。
在确认 S1\~S6 准确无误之后再关闭 BL1 调试模式，禁用 SPI 等。

备注

当使用上述步骤在某块板子上成功配置了安全启动之后，可以将步骤 S4\~S6 合并成一步，通过
BKFIL 将安全启动版本，OTP 密钥配置以及 EFUSE 安全开关使能一次性部署到板子上。通常工
厂部署量产版本时，建议使用合并步骤简化部署流程。
