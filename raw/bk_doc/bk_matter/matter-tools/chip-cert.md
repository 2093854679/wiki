# 证书工具 chip-cert[](#chip-cert "永久链接至标题")

[[English]](../../../../en/v2.0.1/matter-tools/chip-cert/index.html "../../../../en/v2.0.1/matter-tools/chip-cert/index.html")

chip-cert 用于处理matter的一系列证书，可以在 [这里](https://project-chip.github.io/connectedhomeip-doc/src/tools/chip-cert/README.html "https://project-chip.github.io/connectedhomeip-doc/src/tools/chip-cert/README.html") 查看相关介绍。

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
