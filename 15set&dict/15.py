# a=1,2,3
# print(type(a))#返回tuple
# print(a)#返回(1,2,3)
# x,y=y,x #右边先算右边为封装，左边为解构
# t1 = (1,2) #定义为元组
# t2 = 1,2 #封装为元组
# 解构，把线性结构解开

# lst=[3,5]
# first,second= lst
# print('first={} second={}'.format(first,second))
# x,y=list((2,3))
# print(x,y)
# a,b ={10,20} #集合，非线性结构
# print(a,b)
# a,b = {'a':10,'b':20}
# print(a,b)
# a,*b={10,20,30}
# print(a,b)#输出10 [20, 30]
# lst = list(range(1,101,2))
# head,*mid,tail = lst
#
# print(head,mid)
# print(tail)
#
# lst = [9,8,7,20]
#
# head,*_,tail = lst
#
# print(head,tail)
#
# _,*_,tail=lst
#
# print(_,_,tail)
#
# lst=list(range(10))
# print(lst[1],lst[3],lst[-2])
# _,a,_,b,*_,c,_=lst

# print(a,b,c)
from timeit import timeit

lst = [1, (2, 3, 4), 5]
_, a, _ = lst
*_, A = a
print(a)
print(A)
s = 'JAVA_HOME=/usr/bin'
s1 = s.split('=')
print(s1)
a, b = s1
print(a, b)
key, _, val = "JAVA_HONE=/usr/bin".partition('=')
print(val)
print(key)

# 集合
s = set(range(10))
print(s, type(s))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>

s = {}  # 字典
print(s, type(s))  # {} <class 'dict'>

s6 = {(1, 2), 3, 'a'}
type(s6)  # 返回set

# set 增加
# add(elem)
# update(*other)
# s = {1, 2, 3, 4, 5}
# s.add('abc')
# print(s)
# s.add(1)
# print(s)
# s.add(0)
# print(s)
# s.update(range(10))
# print(s)
# s.update(range(3, 7), range(5))  # 可迭代对象，'bcd' 会被拆开
# s.add('bcd')
# print(s)
# s.remove('bcd')
# print(s)
# # s.remove(11)
# s.discard(11)
# s.pop()  # 随机弹出一个元素
# s.clear()
# print(s)
# print(hash(1))
# print(hash(2))
# print(hash('1'))
# print(hash('2'))
#
# s1 = {1,2,3,4}
# s2 = {2,3,4,5}
# print(s1 | s2) #{1, 2, 3, 4, 5}
# print(s1 & s2)#{2, 3, 4}
# print(s1 -s2)#{1}
# s1-=s2
# print(s1)#{1}
# print(s1.isdisjoint(s2))
#
# s1 = {'A','B','C'}
# s2 = {'C','B','D'}
# print(s1 & s2)
#
# userid in (A|B|C|..) == False



