# SARADC Cli[](#saradc-cli "永久链接至标题")

[[English]](../../../../../en/v2.2.1/examples/cli/saradc/saradc.html "../../../../../en/v2.2.1/examples/cli/saradc/saradc.html")


## 1、功能概述[](#id1 "永久链接至标题")

> 为了方便验证SARADC功能，SDK提供了SARADC CMD示例。SARADC CMD命令以 `adc_test` 开头，后接具体命令和参数。执行命令，返回SARADC的采样值。


## 2、代码路径[](#id2 "永久链接至标题")

> 路径: `\components\bk_cli\cli_adc.c`


## 3、cli命令简介[](#cli "永久链接至标题")

支持的命令如下:

> 1.adc_test
> :   - 功能说明
>       :   用来设置SARADC，获取采样值
>     - 命令格式
>       :   adc_test param1 adc_example
>
>           |  |  |
>           | --- | --- |
>           | param1 | adc channel |
>     - 测试用例
>       :   设置SARADC channel 3参数：`adc_test 3 adc_example`
