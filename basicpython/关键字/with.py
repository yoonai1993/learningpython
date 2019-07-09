# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# 以上这段代码执行完毕后，就算在处理过程中出问题了，文件f总是会关闭。