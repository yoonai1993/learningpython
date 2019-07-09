#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
# age设置默认值
def printme (name, age = 35):
    "打印任何传入的字符串"
    print("Name:", name)
    print("Age:", age)
    return
# 调用printme函数
# 使用关键字参数允许函数调用时参数的顺序与声明的不一致
printme( age = 28, name = "talor swift")
# 默认参数值
printme(  name = "meimei")
# 不定长参数
def printinfo( arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70, 60, 50)