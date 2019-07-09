import keyword
""" 
保留字即关键字，我们不能把它们用作任何标识符名称。
Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字
"""
for i in range(len(keyword.kwlist)):
    if i%10 == 0 and i!=0:
        print(keyword.kwlist[i])
    else:
        print(keyword.kwlist[i],end=',')