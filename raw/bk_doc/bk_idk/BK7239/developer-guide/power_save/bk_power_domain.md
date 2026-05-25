# 电源域说明[](#id1 "永久链接至标题")


## 电源域说明[](#id2 "永久链接至标题")


### 初识电源域[](#id3 "永久链接至标题")

整个开发板分为三类电源域：
:   - 板级的电源域

    - 模拟部分电源域

    - 数字部分电源域


---

数字部分分为两个大的电源域：
:   - Aon电源域

    - Digital Core电源域


### Digital Core电源域[](#digital-core "永久链接至标题")

Digital Core电源域下各个业务模块有自己单独的电源域。各个业务可以根据自己的工作场景来决定上电还是下电，这样功耗控制很灵活，不同的产品形态达到最优功耗。

[[English]](../../../../en/v2.2.1/developer-guide/power_save/bk_power_domain.html "../../../../en/v2.2.1/developer-guide/power_save/bk_power_domain.html")
