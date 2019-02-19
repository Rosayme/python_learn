# file = open("test.txt", 'r') #内置函数，可以打开一个文件
# 绝对路径 相对路径
# 同级目录下的为，相对路径
# 据对路径，如果不在同一级目录下,

# file = open("D:\JetBrains\program\\untitled\class_day04\\test_new", 'r')

# read 只读 write只写  append追加
# 非二进制文件  r  r+  w  w+  a  a+
# 二进制文件   rb rb+ wb wb+ ab ab+
"""
file = open("test.txt", 'r+', encoding='utf-8')
# r只读的方式打开
# r+读写的方式打开，写的内容会在文件后面

a1 = file.read(5)
a2 = file.read(4)   # 光标会随着改动
file.write("华华")
print(a1, a2)
"""

"""
file = open("test_1.txt", 'w+', encoding='utf-8')
# w只写，如果不存在这个file的话那么就会先新建，然后更具你的要求写入
# w只写，如果存在这个file的话，那么就会直接覆盖，重写
# w+ 读写，无论是否存在这个file，写的内容会在文件后面

a1 = file.write("护花使者")
print(file.tell())   # 获取当前光标的位置
file.seek(0, 0)  # 移动到头部
# 移动光标，seek（offset，[.from]） offset移动的偏移量
# 0：参考位置为文件开头
# 1：参考位置为当前光标所在位置
# 0：参考位置为文件结尾
# offset ：正往结束为止移动，负往文件头开始计算相对位置，从文件尾计算时就会引起异常

a2 = file.read(4)
print(a2)
"""

"""
file = open("test_1.txt", 'a+', encoding='utf-8')
file.write("sellme")
file.seek(0, 0)
print(file.read())

# a追加（只能写入），在后面追加，不可以.read
# a+ 追加（读写），如果不存在这个file的话那么就会先新建，然后根据你的要求写入,可以.read
# a+ 追加（读写），如果存在，则在后面直接写入，可以.read()
file.close()
"""

with open("test_1.txt", "r") as file:
    print(file.read())