# 占位符 %s %d
# repr()
import datetime

# print("I am %05d " % (20,))  # 以 % 为分隔符 返回I am 00020
# print("I am %03c " % (97,))  # 返回I am   a
# print("I am %03s " % (97,))  # 返回I am  97
# print("I am %03s %s" % (97, 20))  # 只能单一对象
# print("%3.2f%%,0x%x,0X%02X" % (89.7654, 10, 15))  # 输出89.77%,0xa,0X0F  .2表示精度 %%表示转义
# print("%010.2f%%,0x%x,0X%02X" % (89.7654, 10, 15))  # 输出0000089.77%,0xa,0X0F
# print("I am %-20d" % (20,))  # -表示左对齐
# format 函数
# "{} {xxx}".format(*args, **kwargs) —> str
# args是位置参数，是一个元组
# kwargs是关键字参数，是一个字典
# 花括号表示占位符
# {} 表示按照顺序匹配的位置参数，{n}表示取位置参数索引为n的值
# {xxx}表示在关键字参数中搜索名称一致的
#
# {{}}表示打印花括号

# print("{0}{1}".format(2, 1))  # 输出21
# print("{:>10}".format(97))  # 右对齐，输出        97
# print("{:>10x}".format(97))  # 输出61,16进制
# print("{:>10c}".format(97))  # 输出61,16进制
# print("{:^10b}".format(97))  # 输出61,16进制^居中对齐
# print("0b{0:*<100b}".format(97))  # *为填充
# print('{2},{0},{1}'.format('a', 'b', 'c'))  # 输出c,a,b
# print('{2},{0},{1},{1}'.format(*'abc'))  # *表示解构
# print('{a},{b}'.format(a='A', b='B'))
# coord = (3, 5)
# print('X:{0[0]},Y:{0[1]}'.format(coord))
# print('X:{},Y:{}'.format(coord[0], coord[1]))
#
# print('int:{0:d},hex:{0:x},bin:{0:b}'.format(42))
# print('{:,}'.format(1234567890))  # 加个千位分隔符
# print('{:.2%}'.format(19 / 22))
# d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H%M%S}'.format(d))
#
# for align, text in zip('<^>', ['left', 'center', 'right']):
#     print('{0:{fill} {align}16}'.format(text=text, fill=align, align=align)) #报错


# print('Please input a num')
# num = input('>>>')
# print('num的位数为',len(num))
# lst = list(num)
# lst1 =[]
# for l in lst:
#     if l not in lst1:
#         lst1.append(l)
#
# for i in lst1:
#     print(i,num.count(i))
# lst = list(num)
# for i in reversed(lst):
#     print(i)
#
# print(lst[3])
# length=len(num)
# lst = [0] *10
# for i in range(1,length +1):
#     print(num[-i],end='')
#     lst[int(num[-i])] += 1
# print()
# nums = []
# for i in range(5):
#     nums.append(input('...'))
# length = len(nums)
# for j in range(length):
#     print('数字{:5} 有{}位数'.format(nums[j],len(nums[j])))
# nums_int = list(map(int,nums))
#nums_int.sort()
#print(nums_int)
# length=len(nums_int)
# for s in range(length):
#     for i2 in range(length-1-s):
#         if nums_int[i2+1] > nums_int[i2]:
#             nums_int[i2],nums_int[i2+1] = nums_int[i2+1],nums_int[i2]
# print(nums_int)


#print('中'.encode()) #返回b'\xe4\xb8\xad'
#print(b'\xe4\xb8\xad'.decode())#返回中
#print('a'.encode())
#encode(encoding='utf-8',errors='strict')->bytes
#bytes.decode(encoding="utf-8",errors="strict")
#bytearray.decode(encoding="utf-8",errors="strict")
#print(b'a'.decode())
#bytes(int)
#print(bytes(97).decode())
#print(b'\xe4\xb8\xad'.decode())#输出中
#print(b'0 *'.decode())#输出0 *
#bytes
#b'abcdef'.replace(b'f',b'k')
#b'abc'.find(b'b')
#bytes.fromhex(string) #string必须是2个字符的16进制的形式
#print(bytes.fromhex('6162 09 6a 6b00').decode())
#'abc'.encode().hex()#返回16进制的字符串
#b'abcdef'[2]返回字节对应的数，int类型
# print(bytearray(b'abc')[-1]) #返回99
# print(bytes(b'abc')[-1])#返回99
# print(bytes(b'abc')[-2])#返回99
# a=bytearray(b'abc')
# print(a)
# a[-2]=100
# print(a)

# print('www.magedu.com'[4:10]) #返回magedu
# print('www.magedu.com'[4:50])
# a = 'www.magedu.com'
# b=a[:]
#
#

#print('www.magedu.com'[4:10:2]) #[start,stop.step]

# print(bytearray(b'www.magedu.com')[4:10])#返回bytearray(b'magedu')
# print(tuple('www.magedu.com')[-10:10])#返回('m', 'a', 'g', 'e', 'd', 'u')
# print(list('www.magedu.com')[-10:-4])#返回['m', 'a', 'g', 'e', 'd', 'u']
# print('www.magedu.com'[::-1])#返回moc.udegam.www