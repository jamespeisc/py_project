# num1=int(input('>>>'))
# num2=int(input('>>>'))
# num3=int(input('>>>'))
#
# if num1 > num2:
#     if num1 > num3:
#         if num2 > num3:
#             print(num1,num2,num3)
#         else:
#             print(num1,num3,num2)
#     else:
#         print(num3,num1,num2)
# else:
#     if num2 > num3:
#         if num1 > num3:
#             print(num2,num1,num3)
#         else:
#             print(num2,num3,num1)
#     else:
#         print(num3,num2,num1)

# nums = []
#
# for i in range(3):
#     #nums.append(int(input('{}: '.format(i))))
#     nums.append(int(input('>>>')))
# print(nums)


# nums = [1,2,3]
# print(max(nums))

# for i in range(3):
#     #nums.append(int(input('{}: '.format(i))))
#     nums.append(int(input('>>>')))
# while True:
#     cur = min(nums)
#     print(cur)
#     nums.remove(cur)
#     if len(nums) ==1:
#         print(nums[0])
#         break


# 用sort 排序列表
# nums = []
# out = None
# for i in range(3):
#     nums.append(int(input('{}: '.format(i))))
# nums.sort(reverse=True)
# print(nums)

# nums = [1,2,3,4,5]
#
# for i in range(nums):
#     print(i)

# lst = [1, 3, 2, 0]
# length = len(lst)
# count = 0
# count_swap = 0
# for i in range(length):
#     flag = False
#     for j in range(length - 1 - i):
#         count +=1
#         if lst[j] > lst[j+1]:
#             tmp = lst[j]
#             lst[j] = lst[j + 1]
#             lst[j + 1] = tmp
#             count_swap += 1
#         # lst[j],lst[j+1] = lst[j+1],lst[j]
#     if not flag:
#         break
# print(lst)

#字符串join
# s1 = 'string'
# s2 = "string2"
# s3 = '''this is a string'''
# s5 = r"Hello\n magedu.com"  #
# s6 = 'c:\windows\nt'
# s7 = R"c:\windows\nt"
# print(s5, s7)
# sql = """select * from user where name='tom'"""
# print(sql)

#一个个字符组成的
# num = [1,2,3,4]
# print(sql[4])
#
# for i in range(len(num)):
#     print(num[i])
#     print(type(num[i]))

# for c in sql:
#     print(c)
    #print(type(c))
    #print(type(sql))
# sql2='中国'
#
# for c in sql2:
#     print(c) #输出中国
#
# print(list(sql2)) #sql2 需要可迭代
# print("-".join(sql2)) #s输出中-国
#
# lst = list(range(5))
# print(lst)
# a = '~~~'.join(map(str,lst)) #返回0~~~1~~~2~~~3~~~4，将可迭代对象连接起来
# print(a)
# print("\"".join(map(str,lst))) #用双引号隔开lst内中的元素
# print("\n".join(('a','b')))
#
# lst = ['1',['a','b'],'3']
# print("\n".join(map(str,lst)))
# #字符串+连接
# print(a+sql2)
# print("abc"*3)

#字符串分隔
# print("a b c".split()) #返回
# # ['a', 'b', 'c']
# print(map(str,[1,2,3]))#返回<map object at 0x0000016EBD2322C8>
#
# print("ab\tc")
# print("a b\tc".split())#返回['a', 'b', 'c']
# print("a b\tc".split(' '))#返回['a', 'b\tc']
#"a b\tc".split(None) = "a b\tc".split()   "a b\tc".split(sep=None)

#None 默认以尽可能多的字符分隔，如果指定了空白字符则用空白字符

# print("a    b    c".split(' '))
#
# print("---".join(','.join('abc').split(',')))#返回['a', 'b', 'c']
# print(list('abc'))
# print("a,b,c,d".split(',',2))#分隔2次
# print("a,b,c,d".rsplit(',',2))#从右边分隔2次
# print('/etc/sysconfig/network/ifcfg'.rsplit('/',1)[1])
# print('ab c\n\nde f\r\rg\rkl\r\n'.splitlines())
# print('ab c\n\nde f\r\rg\rkl\r\n'.splitlines()) #\n \r \r\n
# print('ab c\n\nde f\rg\rkl\r\n'.splitlines(True)) #保留换行符


# print("a,b,c,d".partition(',')) #仅切一刀，返回元组+分隔符，没有默认值
# print("a,b,c,d".partition('c')) #切一刀用partition

#partition(sep)->(head,sep,tail)

#upper() lower() swapcase() 大小写转换
#
# print("abc".upper().lower().split())
#
# a = input('>>>')
# if a.lower() = 'exit':
#     pass


print('abc def'.title())#返回Abc Def
print('abc def'.capitalize())#返回Abc def
print('123'.center(10,'-')) #居中---123----
print('123'.zfill(10))#填充0
print('123'.ljust(10,'-'))
print('123'.rjust(10,'-'))
print('www.magedu.com'.replace('w','p'))
print('www.magedu.com'.replace('w','p',2))#2表示替换几次，不回头
print('a b c \td\re\n123\n\n'.strip())
s = "     I am very very very sorry"
print(s.strip(' '))
print(s.strip('  overys')) #括号内为字符集
print("----")
print('a b c \td\re\n123\n\n') #print \r  光标回到起始位置
print("----")
print("a b c \tde\n123\n\n")
#s.lstrip([chars])
#s.rstrip([chars])
print(s.find('very')) #返回索引，找不到返回-1
print(s.find('lvery')) #返回索引，找不到返回-1
print(s.rfind('very',-10,-1))

print(list(enumerate(s)))

# seq = ['one', 'two', 'three']
# for temp in enumerate(seq):
#     print(temp)
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

#index 找不到抛出异常

print(len(s))
print(s.count('very'))
#s.startswith('very')
#s.endswith('very',5)

print(s.endswith('sorry',5,100)) #返回True
print('sorry'.rstrip().endswith('sorry',0,100))
#s.isalnum() 是否是字母和数字组成
#s.isalpha() 是否是字母
#s.isdecimal()是否只包含十进制数字
#s.isdigit() 是否全部数字
#s.isdentifier() 是不是字母和下划线开头，其他都是字母数字下划线
#s.islower()# 是否都是小写
#s.isupper()#是否全部大写
#s.isspace()#是否只包含空白字符


n = 6
row = [1] * n # 一次性开辟足够的空间
for i in range(n):
    offset = n -i
    z = 1  #因为会有覆盖影响计算，所以引入一个临时变量
    for j in range(1,i //2 +1): #对称性
        val= z + row[j]
        row[j],z = val, row[j]
        if i != 2* j:
            row[-j-offset] = val
    print(row[:i+1])

row  = [1,2,3,4]
print(row[:])
print(row[:-1])
