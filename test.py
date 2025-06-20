# string = 'abc'
# b = string.encode('utf-8')
# s = b.decode('utf-8')
# x= '\x00'
# print(b)
# print('************************************')

# class MyClass:
#     """A example class"""
#     x = 'abc'
#
#     def foo(self):
#         return 'My Class'
#
#
# print(MyClass.x)
# print(MyClass.foo)
# print(MyClass.__doc__)

# class Person:
#     def __init__(self,name):
#         print(name)
#     def __init__(self,age):
#         print(age)

# a = ['a','b','c','d']
# b = ['1','2','3','4']
#
# print(list(zip(a,b)))

# p = Person('tom')

# def square():
#     for x in range(4):
#         yield x ** 2
# square_gen = square()
#
#
# print(next(square_gen))

# nums = [_ for _ in sorted(range(10),reverse=False)]
# print("nums", nums)

# params = (('a', str), ('b', int))
# for n, t in params:
#     print(n,t)


# from webob.multidict import MultiDict
#
# md = MultiDict()
# md.add('a',1)
# md.add('b',2)
# md.add('b',3)
# md.add('1',100)
# print(md) # 返回MultiDict([('a',1),('b',2),('b',3)])
# print(md.get('c',20000))


# r = int(input('r='))
# print('area='+str(3.14*r*r))
# print('circumference='+str(2*3.14*r))


# f0 =1
# f1 =1
# n = 2
# for i in range(3,102):
#     fn = f0+f1
#     f0 = f1
#     f1 = fn
#     n += 1
#     if i == 9:
#         print(n)
#         print(fn)

# for i in range(1,10):
#     s=""
#     for j in range(i,10):
#         if j <4:
#             s += "{}*{}={:<2} ".format(i,j,i*j)
#         else:
#             s += "{}*{}={:<3} ".format(i,j,i*j)
#     print("{:>72}".format(s))

# lst = [1, 2, 1, 1, 'ab']
# lst.extend(range(11,16))
# print(lst)
# print(lst,lst*2)
# x = [[1,2,3]] *3
# print(x)
# x[0][1] =20
# print(x)
# from random import randrange
# #
# # for i in range(10):
# #     print(randrange(1, 6))


# t=tuple()
# print(id(t))
# t = tuple(range(5))
# print(id(t))
# t = (1,5,'abc')
# for x in t:
#     print(x)
# t1 = (1)
# print(type(t1))
# t1 = (1,)
# print(type(t1))
# t1 = ((1),)*5
# print(t1)
#
# t2 = ((1,),)*5
# print(t2)
# print(t1[0])


# fieldname='name age'
#
# field_names = fieldname.replace(',', ' ').split()
# #field_names = list(map(str,fieldname))
#
# print(field_names)

# n = 100
# lst = [2]
# for i in range(3,n,2):
#     flag = False
#     for j in lst:
#         if j > i**0.5:
#             flag = True
#             break
#         if i %j ==0:
#             flag = False
#             break
#
#     if flag:
#         lst.append(i)
# print(lst)


# nums = []
#
# for i in range(3):
#     #nums.append(int(input('{}: '.format(i))))
#     nums.append(int(input('>>>')))
# print(nums)

# s5 = r"Hello\n magedu.com"
# print(s5)
# sql = """select * from user where name='tom'"""
# print(sql)

# lst = list(range(5))
# print(lst)
# a = '~~~'.join(map(str,lst)) #返回0~~~1~~~2~~~3~~~4，将可迭代对象连接起来
# print(a)

# print("\n".join(('a','b')))
# print(list(map(str,[1,2,3])))

# print('ab c\n\nde f\r\rg\rkl\r\n'.splitlines())
# print("a,b,c,d".split(',',2))
# print('ab c\n\nde f\rg\rkl\r\n'.splitlines(True))
# print("a,b,c,d".partition(','))
# print("a,b,c,d".partition('c'))
# print('abc def'.title())
# print('abc def'.capitalize())

# seq = ['one', 'two', 'three']
# for temp in enumerate(seq):
#     print(temp)
# print("I am %05d " % (20,))
# print("I am %03s %s" % (97, 20))
# lst = ['1','a','3']
# print (",".join(lst))
#
# print(s.strip())
# #print(s.strip('Iy '))

# print("I am %3c " % (97,))
# print("{:>10c}".format(97))
#
# print("{:^10b}".format(97))
#
# print("0b{0:*<20b}".format(97))

# print('{2},{0},{1},{1}'.format('a', 'b', 'c'))
#
# print('{2},{0},{1},{1}'.format(*'abc'))

# coord = (3, 5)
# print('X:{0[0]},Y:{0[1]}'.format(coord))
# print('X:{},Y:{}'.format(coord[0], coord[1]))

# print('int:{1:d},hex:{0:x},bin:{0:b}'.format(42,100))
# import datetime
# d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# print(d)
# d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H-%M-%S}'.format(d))
# for align,text in zip('<^>',['left','center','right']):
#     print('{0:{fill}{align}16}'.format(text,fill=align,align=align))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(i,j,j*i),end='')
#     print()
# print('{:*^30}'.format('centered'))


# b3 = b'http://c.biancheng.net/python/'
# print("b3: ", b3)
# print(b3[0])
# print(b3[7:22])
# b5 =b'C\xe8\xaf\xad\xe8\xa8\x80\xe4\xb8\xad\xe6\x96\x87\xe7\xbd\x918\xe5\xb2\x81\xe4\xba\x86'
# print(b5.decode())
#
# print(b'a'.decode())
# print('a'.encode())
# print(bytes('a'))

# b1 = bytes(10)
# print(b1)
# print(type(b1))
# print('-------------')
# print('1111111111111',b'\x41'.decode())
#
#     # bytes 通过 decode函数转为 str类型
# s1 = b1.decode()
# print("s1:",s1)
# print(type(s1))
#
# print('a'.encode())
# print(bytes(b'abc')[-2])
# print(b'\x00\x00\x00\x00'.decode())
# print(bytes(4))
# a,b = {'a':10,'b':20}
# print(a,b)

# lst = list(range(1,10,2))
# head,*mid,tail = lst
#
# print(head,mid)
# print(tail)
#
# lst=[1,(2,3,4),5]
# _,a,_=lst
# print(a)

#
# s='JAVA_HOME=/usr/bin'
# s1=s.split('=')
# a,b=s1
# print(a,b)
#
# key,_,val="JAVA_HONE=/usr/bin".partition('=')
# print(val)
# print(key)
# s0 = []
# s1 = set()
# s2 = ()
# s3 = {}
#
# print(type(s0))
# print(type(s1))
# print(type(s2))
# print(type(s3))


# import psutil
#
# # 获取CPU使用率
# cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
#
# # 获取内存使用率
# mem = psutil.virtual_memory()
# mem_percent = mem.percent
#
# # 获取磁盘使用率
# disk = psutil.disk_usage('/')
# disk_percent = disk.percent
#
# # 打印监控结果
# print('CPU使用率：{}%'.format(cpu_percent))
# print('内存使用率：{}%'.format(mem_percent))
# print('磁盘使用率：{}%'.format(disk_percent))




# d = {"a":1,"b":2}
# print(d["a"])
# for item in d.items():
#     print(item[0],item[1])
# for k,_ in d.items():
#     print(k)

# d = {}
# d[1] = "a"
# for c in ["a","b"]:
#     for i in range(5):
#         d[c].append(i)
# print(d)
# import random
# print(random.randrange(10))

import datetime
# a = datetime.datetime.today()
# b = datetime.datetime.now()
# c = datetime.datetime.utcnow()
# print(a, b, c)
import time

# datetime1 = datetime.datetime(2016, 12, 6, 16, 29, 43, 79043)
# print(datetime1)
#
# dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")  # 返回datetime对象
# print(dt)
# print(type(dt))
#
# #print(dt.strptime("21/11/06 16:30","%Y-%m-%d %H:%m:%S"))
#
# print("{0:%Y}/{0:%m}/{0:%d} {0:%H}:{0:%M}:{0:%S}".format(dt))

# dt1 = datetime.datetime.now()
# time.sleep(2)
# dt2 = datetime.datetime.now()
# ts = (dt2 -dt1).total_seconds()
# ts2 = (dt2 -dt1)
#
# print(ts)
# print(ts2)
#
# nums = [list(range(10))]
# num1 = [range(10)]
# num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num1:
#     print(i)
# # print(nums)
# # print(len(num1))
#
# a = [(i +1) **2 for i in range(10)]
# print(a)

# newlist1 = [(x,y) for x in 'abcde' for y in range(3)]
# newlist2 = [[x,y] for x in 'abcde' for y in range(3)]
# newlist3 = [{x:y} for x in 'abcde' for y in range(3)]
# print(newlist1)
# print(newlist2)
# print(newlist3)
# import random
# import string
# it = (print ("{}".format(i+1)) for i in range(2))
# first = next(it)
# second = next(it)
# print(first)
# print(second)

# i = [1,2,3,4]
#
# print(next(iter(i)))
# print(next(iter(i)))

# d = {x:(1,[2]) for x in range(10)} #字典解析式
# print(d)
# x,y = (1,2)
#
# print(x,y)
#
# print(ord('中'))
#
# g = reversed(range(5))
# for i in g:
#     print(i)

# for x in enumerate([2,4,6,8]):
#     print(1,x,end=" ")
#     print()
#     print(x)
#
# def add(*nums): #可变位置参数
#     sum = 0
#     for x in nums:
#         sum += x
#     return sum
#
# x=add(a=1)
# print(x)

# def fn(*args,x=5):
#     print(x)
#     print(args)
#     print('---')
#
# fn()
# fn(5)
# fn(x=6)
# fn(1,2,3,x=10)

# def fn(y,*args,x=5):
#     print('x={},y={}'.format(x,y))
#     print(args)
#
# fn(1,3,x=6)


# def counter():
#     c = [0]
#     def inc():
#         c[0] += 1
#         return c[0]
#     return inc
# foo = counter()
#
#
# print(type(foo))
# print(foo(),foo(),foo())

# def foo(xyz=[],m=5,n=6):
#     xyz.append(100)
#     print(xyz)
#
#
# print('def1', foo.__defaults__)

# print([x for x in (lambda *args: map(lambda x:(x+1,args),args)) (*range(5))])
#
#
# def counter(base):
#     def inc(step=1):
#         nonlocal base
#         base += step
#         return base
#     return inc
# f1 = counter(3)
# f2 = counter(3)
#
# print(f1())
# print(f2())
#
# import inspect
# def add(x:int,y:int,*args,**kwargs) ->int: #可变类型参数不加类型,标识符不带*
#     return x + y
# sig = inspect.signature(add)
# parms = sig.parameters
# a=parms['y']
# b=parms['y'].annotation
# c= parms['args']
# d= parms['kwargs']
# print(add.__annotations__)
# print(sig)
# print(sig.parameters)
# print(a,b,c,d)
# print(type(parms))


#
# f = open("test2.txt")
# print(f.read())
# f.close()

# f = open('test3.txt','r+')
# f.read(1)
# f.write('\n123455')
# f.close()
# f = open("new_file.txt", "w+")
# f.write('new file')
# f.close()
# f = open("new_file.txt", "r")
# print(f.read())
# f.close()
# f = open("new_file.txt", "a")
# f.write('new file2')
# f.close()

# f = open("new_file3.txt", "r+")
# print(f.tell())
# f.close()

# from pathlib import Path
#
#
# p = Path('/etc/a/b/c/t.txt')
# # print (len(p.parents))
# # #
# # for i in p.parents:
# #     print(i)
# #
# for x in p.parents[len(p.parents) -1].iterdir():
#     print(x.is_dir())
# # print (p.parents[4])

# y = filter(lambda x:x%3==0,[1,2,3,4,5,6])
# print(y)
# for i in y:
#     print(i)

# names = ['dwdw', 'Avf', 'rfegbn', 'Dqssqve ', 've n', 'Bfern', 'Zfer']
# result = filter(lambda x: x.startswith('r'),names)
# for name in result:
#     print(name)


result = map(lambda x: x*x,[y for y in range(10)])
print (result)
for i in result:
    print(i,end=" ")


