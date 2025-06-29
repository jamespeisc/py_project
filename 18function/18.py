def add(x, y):
    result = x + y
    return result


out = add('a', '5')
print(out)

print(callable(add)) #返回True,可调用的


def add(x=5,y=5):
    return x+y

print(add(6)) #y用默认值

print(add(6,y=9))
#定义函数时，缺省值向后放

def add(x,y=5):  #x 必须提供值
    return x + y
print(add(1))

def login(host='127.0.0.1',port='8080',username='wayne',password='magedu'):
    print('{}:{}@{}/{}'.format(host,port,username,password))

login()

login('127.0.0.1',80,'tom','tom')
#login('127.0.0.1','80','pass',username='root')
login('localhost',port=80,password='com')
login(port=80,password='magedu',host='www')

#可变参数,一个形参可以匹配任意个实参

def add(nums):
    sum = 0
    for x in nums:
        sum += x
    return sum

a= add([1,3,5])
print(a)

def add(*nums): #可变位置参数
    sum = 0
    for x in nums:
        sum += x
    return sum

a= add(1,3,5)
print(a)

#没有return 隐含调用return none
#b = add(nums=3) 会报错
#print(b)

#形参前使用**符号，表示可以接收多个关键字参数，收集的key和值组成一个字典

def showconfig(**kwargs):
    for k,v in kwargs.items():
        print('{}={}'.format(k,v),end=" ")

showconfig(host='127.0.0.1',port='8080',username='wayne',password='magedu')

def showconfig(username,password,*args,**kwargs):
    print('1')

def fn(*args, x,y,**kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


#如果在一个星号参数后，或者一个位置可变参数后，出现普通参数，实际上已经不是普通参数了，而是keyword-only参数

def fn(*args,x):
    print(x)
    print(args)

#fn(3,5)
#fn(3,5,7)
fn(3,5,x=7)
#def(**kwargs,x) 直接报错

def fn(*,x,y): #*表示仅允许传递2个参数，且2个参数必须是keyword-only参数
    print(x,y)
fn(x=5,y='a')

def fn(z,*,x,y): #z,x,y 必须赋值
    print(x,y)

def fn(*args,x=5):
    print(x)
    print(args)

fn()
fn(5)
fn(x=6)
fn(1,2,3,x=10)

def fn(y,*args,x=5):
    print('x={},y={}'.format(x,y))
    print(args)

fn(1,3,x=6) #x=6 要放在后面


def fn(x=5,**kwargs):
    print('x={}'.format(x))
    print(kwargs)
fn()
fn(6)
fn(x=7)
fn(x=7,y=6)
fn(y=7,x=6)

#函数参数，参数规则
#参数的一般顺序是：普通参数，缺省参数，可变位置参数，keyword-only参数(可带缺省值),可变关键字参数

def fn(x,y,z=3, *args,m=4,n, **kwargs):
    print(x,y,z,m,n)
    print(args)
    print(kwargs)

fn(1,2,n=4) #返回 1 2 3 4 4 () {}
fn(1,2,10,11,t=7,n=5) #1 2 10 4 5 (11,) {'t': 7}


def add(x,y):
    return x + y

print(add((1,2)[0],[3][0]))

t = (4,8)

add(*t) #参数解构

print(add(*t))

lst = [1,2]
print(add(*lst)) #解构

add(*{5,6})
#解构，非字典类型使用*，字典类型使用**

d = {'x':5,'y':6}
print(add(**d))
d1 = {'x1':5,'y1':6}
#print(add(**d1))
add(*d.keys())
add(*d.values())


def add(*iterable):
    result = 0
    for x in iterable:
        result += x
    return result

print(add(1,2,3))
print(add(*[1,2,4]))
print(add(*range(10)))

def fn():
    print('abc')
a = fn()
print('**********************')
print(a,type(a))

def fn(a,b,*args):
    if len(args) ==0:
        if a > b:
            max1 = a
            min1 = b
        else:
            max1 = b
            min1 = a
    else:
        for i in args:
            max1=max(a,b,i)
            min1=min(a,b,i)
    return max1, min1

print('最大值为{}，最小值为{}'.format(fn(1,2,3,4,5,6,7,8)[0],fn(1,2,3,4,5,6,7,8)[1]))

import random

def double_values(*nums):
    print(nums)
    return max(nums),min(nums)

print(*double_values(*[random.randint(10,20) for _ in range(10)]))

def trangle_point(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if i < j:
                print(' '*len(str(j)),end=' ')
            else:
                print(j,end= ' ')
            print()

print(trangle_point(12))


def show(n): #

    tail = " ".join([str(i) for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n):
        print("{:>{}}".format(" ".join([str(j) for j in range(i,0,-1)]),width))
    print(tail)
show(12)

def showtail(n):
    tail = " ".join([str(i) for i in range(n,0,-1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i,tail[i+1:])

showtail(12)


m_list =[
    [1,9,8,5,6,7,4,3,2]
]
nums = [0] + m_list[0]
sentinel, *origin = nums #哨兵位，待比较数字
count_swap = 0
count_iter = 0
length = len(nums)
for i in range(2,length):
    nums[0] = nums[i]
    j = i -1
    count_iter += 1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j-=1
            count_swap += 1
        nums[j+1]=nums[0]
print(nums,count_swap,count_iter)

def outer():
    def inner():
        print('inner')
    print('outer')
    inner()
outer()
#inner()


