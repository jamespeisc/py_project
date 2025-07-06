# f = open("D:/py_project/fileio/python.txt",encoding='UTF-8')

# print(f.tell())
# # print(f.read())
# # print(f.tell())
# print(f.seek(1))
# print(f.read())
# # print(f.tell())
# f.close()
#
# f = open("D:/py_project/fileio/python.txt",mode='rb')
#
# print(f.read(0).decode())

# f = open("D:/py_project/fileio/python.txt",mode='ra')  # open 返回文件操作对象
# print(f.read())

#windows 默认 gbk
# f.tell() 查看偏移量
# 字符 写入模式： 
# 
# r 缺省的，表示只读打开 
# w 只写打开，并覆盖
# x 创建并写入一个新文件，不存在创建 若存在 抛异常
# a 写入打开 如果文件存在则追加
# b 二进制模式
# t 缺省的文本模式
# + 读写打开一个文件，给原来只读 只写 方式提供提供缺失的都或者写能力

# #print(f.write('啊'))  返回1  为字符
# f = open('test3','rb')
# f.read()
# f.close()

# f = open('test3','w')
# # f.write('啊'.encode())
# f.write('啊')
# f.close()

# f = open('test3', 'r')

# print(f.read(1))

# f.close()

# f.seek(0) 指针偏移量移动到开头  操作的字节偏移量