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

printme(  name = "meimei")
# 测试