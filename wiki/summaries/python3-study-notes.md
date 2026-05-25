# Python3学习笔记

> **Source:** [Python3学习笔记.md](../../raw/Study_Note/01-编程语言/Python3学习笔记/Python3学习笔记.md)
> **TLDR:** Python3系统学习笔记，涵盖解释器安装、基本语法、数据类型、控制流、函数（参数传递/闭包/装饰器/生成器/迭代器）、数据结构（列表/字典/集合/元组）、模块和包管理。

## Key Points

- **基础语法**：动态类型、缩进定义代码块、变量无类型（对象有类型）；数字/字符串/列表/元组/字典/集合
- **函数进阶**：位置参数→默认参数→可变参数（*args/**kwargs）→关键字参数；`lambda`匿名函数；`yield`生成器惰性求值
- **装饰器**：本质是高阶函数，`@decorator`语法糖；无参装饰器（两层嵌套）和有参装饰器（三层嵌套）；`functools.wraps`保留元信息
- **闭包**：函数内部定义函数，内部函数引用外部变量；用于数据隐藏和工厂函数
- **面向对象**：类、继承、多态、`@property`、`@staticmethod`、`@classmethod`；`__init__`/`__str__`/`__len__`魔法方法
- **模块系统**：`import`机制、`sys.path`搜索路径、`__name__ == "__main__"`惯用法、包（含`__init__.py`的文件夹）
- **异常处理**：`try/except/else/finally`；自定义异常；上下文管理器（`with`语句）

## Related Concepts

- [[c-language-basics]] — C与Python的对比
