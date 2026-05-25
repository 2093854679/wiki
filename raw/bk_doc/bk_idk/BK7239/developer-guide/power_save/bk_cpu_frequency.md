# CPU时钟源说明[](#cpu "永久链接至标题")

CPU有以下时钟源：


- 40M 晶体

- 480M DPLL

CPU理论可配置4bit分频系数：

F = 480M / (1+N), N from 0 to 15

备注：
验证可稳定运行最高 240M，最低 60M；


## CPU主频切换说明[](#id1 "永久链接至标题")


- 可以根据业务需要动态的切频率来达到最优功耗,CPU主频切换相对来说比较复杂，SDK内部来实现。

[[English]](../../../../en/v2.2.1/developer-guide/power_save/bk_cpu_frequency.html "../../../../en/v2.2.1/developer-guide/power_save/bk_cpu_frequency.html")
