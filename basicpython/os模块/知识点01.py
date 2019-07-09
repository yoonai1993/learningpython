#!/usr/bin/env  python

# _*_ coding:utf8 _*_

import os
# getcwd() 获取当前工作路径
print(os.getcwd())

# chdir()   改变当前工作路径
print(os.getcwd())
os.chdir("test1")
print(os.getcwd())

# 返回上级目录用..
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

# makedirs（可以建递归的目录）
os.makedirs("gouguoqi/gouguoqi1")
os.chdir("gouguoqi/gouguoqi1")
print(os.getcwd())

# mkdir   新建目录，只能建一层
os.mkdir("gouguoqi")
os.chdir("gouguoqi")
print(os.getcwd())

# removedirs  删除指定目录，如果指定目录为空就删除，如果上级目录也空，也删除。
# 如果上级目录不空就不删，就像下面这个，gouguoqi目录里面有文件，则保留这个文件夹
os.removedirs("gouguoqi/gouguoqi1")

# rmdir 只能删除单级目录为空的文件夹
os.rmdir("gouguoqi")

# listdir    列出指定文件夹下面所有的文件夹和文件包括隐藏文件，以列表方式打印出来
print(os.listdir("D:\pyproject\day21模块"))

# remove   删除指定的一个文件
os.remove("gouguoqi/test.py")

# rename  修改文件夹名字或者是文件名字都可以
os.rename("gouguoqi","gouguoqinew")

# stat   查看一个文件的详细信息
# st_size=28    文件大小，单位是字节
# st_atime=1528473600  用户上一次的访问时间
# st_mtime=1528552906  用户上一次修改的时间（常用）
# st_ctime=1528552713   用户的创建文件的时间
# 这个时间是时间戳，想要转换成我们能看懂的那种格式，还得转换下，比如用户创建文件时间是1528552713 转换为字符串时间
print(os.stat("gouguoqinew/testnew"))
import time
time_local=time.localtime(1528552713)#时间戳转换为结构化时间
print(time.strftime("%Y-%m-%d %X",time_local))#将结构化时间转化为字符串时间

# sep  输出当前操作系统的路径分隔符
print(os.sep)

# linesep    输出当前操作系统的行终止符，win是\r\n   linux是\n
print(os.linesep)

# pathsep  输出用于分割文件路径的字符串win下为; linux下为:
print(os.pathsep)

# system  运行shell命令，直接显示结果
# [root@localhost python]# cat os.system.py
os.system("cd /home && ls")

# os.path.split  把路径分为2部分  1个是目录路径 1个是文件名
print(os.path.split(r"D:\pyproject\day21模块\gouguoqinew\test.py"))

# os.path.dirname 拿split分割的第一个元素
# os.path.basename 拿split分割的第二个元素
print(os.path.split(r"D:\pyproject\day21模块\gouguoqinew\test.py"))
print(os.path.dirname(r"D:\pyproject\day21模块\gouguoqinew\test.py"))
print(os.path.basename(r"D:\pyproject\day21模块\gouguoqinew\test.py"))

# os.path.exists 判断路径是否存在，存在为True，不存在为False
print(os.path.exists("D:\pyproject\day21模块\gouguoqinew"))

# os.path.isabs 如果是绝对路径就返回True，否则为False
print(os.path.isabs("D:\pyproject\day21模块\gouguoqinew\gouguoqi1"))

# os.path.isfile 判断一个文件是否存在，存在为True，否则为False
print(os.path.isfile(r"D:\pyproject\day21模块\gouguoqinew\test.py"))

# os.path.isdir  判断一个目录是否存在，存在为True，否则为False
print(os.path.isdir(r"D:\pyproject\day21模块\gouguoqinew"))

# os.path.join  路径拼接（重要常用）
a="D:\pyproject"
b="day21模块\gouguoqinew"
print(os.path.join(a, b))

# os.path.getmtime  返回path的文件或者是路径的最后修改时间，结果是时间戳
print(os.path.getmtime(r"D:\pyproject\day21模块\gouguoqinew\test.py"))
# 然后将时间戳转化为结构化时间，在转化为字符串时间
time_local=time.localtime(1528601360.0)#时间戳转换为结构化时间
print(time.strftime("%Y-%m-%d %X",time_local))#将结构化时间转化为字符串时间
