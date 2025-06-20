import sys


def foo1(b,b1=3):
    print("fool1 called",b,b1)

def foo2(c):
    foo3(c)
    print("foo2 called",c)

def foo3(d):
    print("foo3 called",d)

def main():
    print("main called")
    foo1(100,101)
    foo2(200)
    print("main ending")

main()

def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)
for i in range(3):
    print(fib(i),end=' ')
fib(2)
print()
print(sys.getrecursionlimit())

import datetime
start = datetime.datetime.now()
pre = 0
cur =1
print (pre,cur, end= ' ')
n = 3

for i in range(n -1):
    pre, cur = cur, pre + cur
    print(cur, end =' ')
delta = (datetime.datetime.now() - start).total_seconds()
print()
print(delta)


import datetime
n =3
start = datetime.datetime.now()
def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)

for i in range(n):
    print(fib(i),end='')
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)


pre = 0
cur = 1
print(pre,cur, end =' ')

#优化

pre =0
cur =1
print(pre,cur)
def fib(n,pre=0,cur=1):
    pre,cur = cur, pre + cur
    print(cur,end=' ')
    if n ==2:
        return
    fib(n-1, pre,cur)

fib(5)

#间接递归


print('111111111111111')
def jiecheng(n):
    return 1 if n < 2 else n * jiecheng(n-1)
a=jiecheng(5)
print(a)

# lst =[]
# input = input('>>>')
# for i in input:
#     lst.append(int(i))
#     lst.sort(reverse=True)
# print(lst)


def fn(n):
    return 1 if n == 10 else (fn(n+1)  + 1) * 2
a = fn(1)

print(a)



def factorial(n,mul =1):
    mul *=n
    if n ==1:
        return mul
    return factorial(n -1,mul)

# def jc(n):
#     n = 5
#     def jc1():
#         n *= n-1
#         return n
#     return jc1
#
#a = jc(5)
# print(a)



num = 1234

def revert(num, target=[]):
    if num:
        target.append(num[len(num) -1])
        revert(num[:len(num)-1])
    return target




a=(lambda x:x**2)(4)#4为调用

print(a)
#使用lambda关键字来定义匿名函数，参数列表不需要小括号，冒号是用来分割参数列表和表达式的，不需要使用return，表达式的值就是匿名函数返回值，lambda只能写在一行上，称为单行函数
#用途，在高阶函数传参时，使用lambda表达式，往往能够简化代码

def inc():
    for i in range(5):
        yield i
print(type(inc))
print(type(inc())) #查看返回值类型

x = inc()  #一定是个迭代器
print(type(x))
print(next(x))
for m in x:
    print(m,'*')
for m in x:
    print(m,'**')


def gen():
    print('line1')
    yield 1
    print('line2')
    yield 2
    print('line3')
    return 3
next(gen())
next(gen())
g= gen()
print(next(g))
print(next(g))
print(next(g,'End'))


def counter():
    i =0
    while True:
        i +=1
        yield i
def inc(c):
    return next(c)
c = counter()
print(inc(c))
print(inc(c))

def inc():
    def counter():
        i =0
        while True:
            i +=1
            yield i
    c = counter()
    return lambda : next(c)
foo = inc()
print(foo())
print(foo())

#等价于

def inc():
    def counter():
        i = 0
        while True:
            i+=1
            yield 1
    c = counter()

    def _inc():
        return next(c)
    return _inc

foo = inc()
print(foo())
print(foo())
print(foo())

#生成器的应用

def fib():
    x=0
    y=1
    while True:
        yield y
        x,y = y, x+y
foo = fib()
for _ in range(5):
    print(next(foo))
for _ in range(100):
    next(foo)
print(next(foo))

#协程，用户空间运行
# yield from

def inc():
    for x in range(1000):
        yield x
foo = inc()
print(next(foo))
print(next(foo))
print(next(foo))

#等价于

def inc():
    yield from range(1000)

foo = inc()
print(next(foo))
print(next(foo))
print(next(foo))

def counter(n):
    for x in range(n):
        yield x

def inc(n):
    yield from counter(n)

foo =inc(10)
print(next(foo))
print(next(foo))
