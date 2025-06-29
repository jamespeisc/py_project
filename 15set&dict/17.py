# num = input('>>>')
# d = {}
# for c in num:
#     if c not in d.keys():
#         d[c] =0
#     d[c] += 1
# print(d)
import random
from collections import defaultdict
# num = input('>>>')
# d = defaultdict(int)
# for c in num:
#     d[c] +=1
# print(d)
from collections import OrderedDict

lst2 = []
d = {}
for i in range(100):
    lst2.append(random.randint(-1000, 1000))
lst3 = map(str, lst2)
for c in lst2:
    if c not in d.keys():
        d[c] = 0
    d[c] += 1
print(len(d))
od = sorted(d.items())
# print(od)

word = 'abcdefghijklmnopqrstuvwxyz'
lst = []
d = {}
for i in range(100):
    first = random.choice(word)
    second = random.choice(word)
    lst.append(first + second)

for c in lst:
    if c not in d.keys():
        d[c] = 0

    d[c] += 1
od = sorted(d.items(), reverse=True)
print(len(od))
print(od)

import datetime

a = datetime.datetime.today()
b = datetime.datetime.now()
c = datetime.datetime.utcnow()
print(a, b, c)

datetime1 = datetime.datetime(2016, 12, 6, 16, 29, 43, 79043)
print(datetime1)

time = datetime.datetime.fromtimestamp(1111111111)
print(time)
# 日期格式化
# 类方法strptime(date_string,format)
# 对象方法 strftime(format)
# 字符串format函数格式化

dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")  # 返回datetime对象

print(dt)
print(type(dt))
dstr = dt.strftime("%Y-%m-%d %H:%M:%S")  # 返回字符串
print(dstr)
print(type(dstr))

print((dt - datetime.datetime.now()).total_seconds())
# datetime.timedelta(days=0,seconds=0,microsecond=0,millseconds=0,minutes=0,hours=0,weeks=0),默认是天
# total_second()

print(dt - datetime.timedelta(1))

# 列表解析
num = []
for i in range(1, 11):
    num.append(i ** 2)
print(num)

lst = [range(10)]
lst1 = list (range(10))

print(lst)
print(lst1)

a = [(i+1)**2 for i in range(10)]
print('new list', a)
b = [i for i in range(10)]
print('list',b)
nums = [sorted(range(10),reverse=True)]
num1 = list(sorted(range(10),reverse=True))

print(nums)
print(len(nums))
print(num1)
print(len(num1))
nums = [_ for _ in sorted(range(10),reverse=False)]
print("nums", nums)
# [返回值 for 元素 in 可迭代对象 if 条件]

even = [x ** 2  for x in range(10) if x % 2 ==0]
print(even)

newlist = [print(i) for i in range(10)]
print(newlist)

newlist = [i for i in range(20) if i %2 ==0 or i %3 ==0]
print(newlist)

#[expr for i in iterable1 for j in iterable2] 等价于
#ret =[]
#for i in iterable1:
#    for j in iterable2:
#        ret.append(expr)

# newlist1 = [(x,y) for x in 'abcde' for y in range(3)]
# newlist2 = [[x,y] for x in 'abcde' for y in range(3)]
# newlist3 = [{x:y} for x in 'abcde' for y in range(3)]
#
# print(newlist1)
# print(newlist2)
# print(newlist3)
#
# newlist4 = [(i,j) for i in range(7) if i >4 for j in range(20,25) if j >23]
# print(newlist4)
# newlist5 = [(i,j) for i in range(7) for j in range(20,25) if i >4 if j >23]
# print(newlist5)
# newlist6 = [i **2 for i in range(1,11)]
#
# print(newlist6)
#
# lst = [1,4,9,16,2,5,10,15]
# lstnew = [lst[i] + lst[i+1] for i in range(len(lst)) if i < len(lst) -1]
# print(lstnew)
#
# newlst = [print("{}*{}={:<3}{}".format(j,i,i*j,'\n' if i ==j else ' '),end = "")for i in range(1,10) for j in range(1,i+1)]
# newlst = [print("{}*{}={:<{}}{}".format(j,i,i*j, 1 if i ==1 else 2,'\n' if i ==j else ' '),end = "")for i in range(1,10) for j in range(1,i+1)]
#
#
# print(newlst)
# import random
# import string
#
# ['0'*(4-len(str(n)))+str(n)+'.'+''.join(['abcdefghijklmnopqrstuvwxyz'[random.randint(0,25)]]) for _ in trange(10)]) for n in range(1,101)]
# [print('{:0>4d}.{}'.format(i,"".join(random.sample(string.ascii_lowcase,10 )),end = "\n") for i in range(1,101)]
# alpha_1 = 'abcdefghijklmnopqrstuvwxyz'
# id_1 = ['{:04}.{}'.format(i,''.join([random.choice(alpha_1) for _ in range(10)])) for i in range(1,101)]
# print('\n'.join(id_1))

a = (i for i in range(5))
print(a) #输出<generator object <genexpr> at 0x000001F9DF8F5BC8>


# for A in a:
#     print(A)
l = [1,2,3,4]
# print(next(a))
# print(next(a))

# print(next(iter(l)))
# print(next(iter(l)))

# g = (str(i) for i in range(10))
# next(g)
# for x in g:
#     print(x)
#
#
# it = (print ("{}".format(i+1)) for i in range(2))
# first = next(it)
# second = next(it)
# val = first + second
# print(val)

#延迟计算
#集合解析式，立即返回一个集合
s = {(x,x+1) for x in range(10)}
l = [x1 for x1 in range(10)]
#s2 = {[x] for x in range(10)} 报错
# for i in s:
#     print(i)
# print(s)
# print(l)
# for i2 in l:
#     print(i2)
#
#
# d = {x:(1,[2]) for x in range(10)} #字典解析式
# print(d)
# #chr(数字) 转成字符
# c = chr(0x41 +10)
# print(c)
# print(type(c))
# s3 = {str(x):y for x in range(3) for y in range(4)} #输出{'0': 3, '1': 3, '2': 3} #key去重
# print(s3)
# l3 = [(x,y) for x in range(3) for y in range(4)]
# print(l3)

#{str(x):y for x in range(3) for y in range(4)} 等价于

# ret = {}
# for x in range(3):
#     for y in range(4):
#         ret[str(x)] =y

#生成器一定是迭代器
#迭代器不一定是生成器对象

b = isinstance('abc', (int,str,float))
print(b) #返回True
c = issubclass(bool,int)
print(c)

#divmod(x,y ) 等价于tuple(x //y, x%y)

#print(divmod(54321,10000)) #返回(5, 4321)

#print(sum(range(5),20))
#print(ord('中')) ord 返回字符对应的整数
g = reversed(range(5))
print(g)

for i in g:
    print(i)
r = {reversed((2,4))}
print(r)
print(type(r))
print(list(reversed("13579")))#返回['9', '7', '5', '3', '1']
#reversed 返回一个翻转元素的迭代器 reversed(seq)

for x in reversed(['c','b','a']):
    print(x)
#enumerate 迭代一个序列，返回索引数字和元素构成的二元组

for x in enumerate([2,4,6,8]):
    print(x,end=" ")#返回(0, 2) (1, 4) (2, 6) (3, 8)

#next(it,1000) #迭代完毕后，默认值为1000

a = [1]
b= [1]
b = [a,b]

for i in b:
    print("i",i)

l = list(zip(range(10),range(10))) #把多个可迭代的对象合并在一起，返回一个迭代器
l1 = list(zip(range(10),range(10),range(2),range(10))) #返回[(0, 0, 0, 0), (1, 1, 1, 1)] 以最短的为准
print(l) #返回[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
print(l1)
s= {str(x):y for x,y in zip(range(10),range(10))}

print(s) #返回{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

