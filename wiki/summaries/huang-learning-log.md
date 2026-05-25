# 黄国航 学习文档记录

> **Source:** [黄国航_学习文档记录.md](../../raw/Study_Note/06-职业发展/实习记录/my_doc/黄国航_学习文档记录.md)
> **TLDR:** BK7236芯片实习期间的学习日志——包括四阶段学习计划、日常工作记录（SOFTAP配网/TCP AT指令/DTIM10保活）、CLI命令速查、项目开发规范和问题记录。

## Key Points

- **四阶段学习计划**：Phase1（芯片和SDK熟悉→6天）、Phase2（5个task开发→4周）、Phase3（代码优化文档编写）、Phase4（项目总结）
- **SOFTAP配网**：创建SoftAP（SSID+密码）→手机连接→HTTP POST接收WiFi凭证→切换为STA模式连接目标AP→反馈连接状态
- **TCP UART AT指令**：UART接收AT指令→解析命令（AT+TCPCONN/AT+TCPSEND/AT+TCPCLOSE）→调用lwIP socket API→AT格式返回结果
- **DTIM10 TCP保活**：配置DTIM间隔为10（每10个Beacon唤醒检查数据）→TCP心跳保活（60s间隔发送keepalive）→Server可通过唤醒命令主动触发→平衡功耗和实时性
- **CLI命令体系**：GPIO/UART/BLE/WiFi各模块的命令速查参考
- **开发规范**：Git branch策略（main/dev/feature/fix命名约定）、commit格式、代码注释和文档规范

## Related Concepts

- [[softap-provisioning-task]] — SOFTAP配网
- [[tcp-uart-at-task]] — TCP AT指令
- [[wifi-dtim10-tcp-keepalive]] — DTIM10保活
- [[freertos-deep-dive]] — FreeRTOS学习
