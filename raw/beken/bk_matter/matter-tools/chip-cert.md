---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/matter-tools/chip-cert/index.html
sdk_family: bk_matter
chip: BK7235,BK7236,BK7256,BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="chip-cert"></a>

# 证书工具 chip-cert

chip-cert 用于处理matter的一系列证书，可以在 [这里](https://project-chip.github.io/connectedhomeip-doc/src/tools/chip-cert/README.html) 查看相关介绍。

1. 生成PAA，PAI，DAC

```
./chip-cert gen-att-cert --type a --subject-cn "Matter Development PAA 01" --valid-from "2020-10-15 14:23:43" --lifetime 7305 --out-key Chip-PAA-Key.pem --out Chip-PAA-Cert.pem
./chip-cert gen-att-cert --type i --subject-cn "Matter Development PAI 01" --subject-vid FFF1 --valid-from "2020-10-15 14:23:43" --lifetime 7305 --ca-key Chip-PAA-Key.pem --ca-cert Chip-PAA-Cert.pem --out-key Chip-PAI-Key.pem --out Chip-PAI-Cert.pem
./chip-cert gen-att-cert --type d --subject-cn "Matter Development DAC 01" --subject-vid FFF1 --subject-pid 0123 --valid-from "2020-10-15 14:23:43" --lifetime 7305 --ca-key Chip-PAI-Key.pem --ca-cert Chip-PAI-Cert.pem --out-key Chip-DAC-Key.pem --out Chip-DAC-Cert.pem
```

2. 生成测试CD

```
./chip-cert gen-cd -C credentials/test/certification-declaration/Chip-Test-CD-Signing-Cert.pem -K credentials/test/certification-declaration/Chip-Test-CD-Signing-Key.pem --out cd.bin -f 1 -V FFF1 -p 8000 -d 0016 -c "ZIG0000000000000000" -l 0 -i 0 -n 0001 -t 0
```

## 模块导航

- [快速入门](../get-started.md)
- [Matter 简介](../matter-basic.md)
- [Beken 的Matter 应用开发](../matter-examples.md)
- [从零开发Matter 新的设备类型产品](../matter-develop.md)
- [Matter 产品认证及量产流程](../matter-production.md)
- [Matter 工具](../matter-tools.md)
- [配置工具 ZAP](zap.md)
- [测试工具 chip-tool](chip-tool.md)
- [factory-data打包工具](factory-data.md)
- [Matter ota 测试](ota-provider-app.md)
- [Matter 生态配网测试](work-with-apple.md)
