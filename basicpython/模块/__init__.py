# import 语句
# 模块的引入
# from…import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
# 导入模块 fib 的 fibonacci 函数
from fib import fibonacci

# from…import* 语句
# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，不宜过多使用
# 自定义模块
# 斐波那契(fibonacci)数列模块
import fibo
def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
# 深入模块
# 模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。

# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回