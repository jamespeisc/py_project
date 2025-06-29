def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


f1 = counter(3)
f2 = counter(3)
f1 == f2  # false, 局部变量重新建立，产生的地址不同

f1() == f2()  # True


def sort(iterable, reverse=False, key=None):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            if x < y:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


# print(sort([1,2,5,4,7,6,2]))


def sort2(iterable, reverse=False, key=lambda x, y: x > y):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            flag = key(x, y) if not reverse else not key(x, y)
            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


sort2([1, 2, 5, 4, 7, 7, 2], key=lambda x, y: x < y)

a = filter(lambda x: x % 3 == 0, [1, 9, 55, 150, -3, 78, 28, 123])
for i in a:
    print(i)

set(filter(lambda x: x % 3 == 0, [1, 9, 55, 150, -3, 78, 28, 123]))

lst = list(range(10, 15))
map(lambda: 0, lst)
a = list(map(lambda x: 0, lst))
for i in a:
    print(i)


def inc(x):
    return x + 1


a = list(map(inc, lst))

list(map(lambda x: 2 * x + 1, range(5)))
dict(map(lambda x: (x % 5, x), range(500)))  # 输出{0:495,1:496,2:497,3:498,4:499}


def add(x):
    def _add(y):
        return x + y
    return _add


t = add(4)(5)

print(t)


def add(x, y, *, z=6):
    return x + y + z


def logger(fn, *args, **kwargs):
    print('before')
    ret = fn(*args, **kwargs)
    print('end')
    return ret


# print(logger(add))
logger(add, 4, 5, z=7)


# 改造后

def logger(fn):
    def _logger(*args, **kwargs):
        print('before')
        ret = fn(*args, **kwargs)
        print('end')
        return ret
    return _logger


t = logger(add)
r = t(4, 5, z=7)
r = logger(add)(4, 5, z=7)

#先进行函数计算，然后带着装饰的结果返回

def logger(fn):
    def wrapper(*args, **kwargs):
        print('begin')
        x = fn(*args, **kwargs)
        print('end')
        return x
    return wrapper


@logger
def add(x, y, z=7):  # add = logger(add)
    return x + y + z


r = add(4, 5, z=7)


# 92节
def copy_properties(src, dest):
    dest.__name__ = src.__name__
    dest.__doc__ = src.__name__


def copy_properties2(src):
    def _inner(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest
    return _inner


import datetime


def logger(fn):
    @copy_properties2(fn)  # 带参装饰器, 装饰器设置过程中包含参数
    # _inner ==>wrapper = _inner(wrapper)
    def wrap(*args, **kwargs):
        print("args={},kwargs={}".format(args, kwargs))
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        duration = datetime.datetime.now() - start
        print("function {} took {}s.".format(fn.__name__, duration.total_seconds()))
        return ret
    return wrap


# @xxx
# @yyy
@logger
def add(x, y, *, z=7):  # add = logger(add)
    """This is a function addition
    example
    """
    print("call add")
    return x + y + z


r = add(4, 5, z=6)


def add2(x, y):
    """This is a function addition
    example
    """
    a = x + y
    return x + y


print("name={}\ndoc={}".format(add.__name__, add.__doc__))
print("----------------------------------")
print(help(add))


# 包装函数把被包装函数的属性覆盖了
# 带参装饰器，它是一个函数，函数作为它的形参，返回值是一个不带参的装饰器函数 使用@functionname(参数列表)方式调用 可以看做在装饰器外层又加了一层函数
#第94章 类型注解
def add(x: int, y: int) -> int:  # int为注解，不是强制性要求，整体为函数签名

    """
    :param x:int
    :param y:int
    :return int

    """
    return x + y


print(help(add))
print(add(4, 5))
print(add('mag', 'edu'))

# inspect 模块

import inspect


def add(x: int, y: int, *args, **kwargs) -> int:  # 可变类型参数不加类型,标识符不带*
    return x + y


sig = inspect.signature(add)
parms = sig.parameters
a = parms['y']
b = parms['y'].annotation
c = parms['args']
d = parms['kwargs']
print(sig)
print(sig.parameters)
print(type(parms))
# parms['z'].annotation 返回 inspect._empty
print('-----------------------------------------------------------------')
import functools
import inspect


def check(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        keys = list(params.keys())
        values = list(params.values())
        for i, val in enumerate(args):
            if values[i].annotation is not inspect._empty and isinstance(val, values[i].annotation):
                print(keys[i], '==', val)
        for k, v in kwargs.items():
            if params[k].annotation is not params[k].empty and isinstance(v, params[k].annotation):
                print(k, "===", v)

        ret = fn(*args, **kwargs)
        return ret

    return wrapper


@check
def add(x: int, y: int = 7) -> int:
    return x + y


add(x=4, y=10)

print('----------------------------------------------------------------------------')

from functools import partial


def add(x, y):
    return x + y


newadd = partial(add, 4)  # 固定了参数x newadd = partial(add, y=5) 则固定了y，newadd为新函数，需要看签名
print(newadd(50))

newadd = partial(add, x=4)
print(inspect.signature(newadd))
# print(newadd(50))#报x已经传值
print(newadd(y=50))


def add1(x, y, z):
    return x + y + z


newadd1 = partial(add1, z=4)
print(inspect.signature(newadd1))
print(newadd1(50, 20))

print('---------------------------------------------')


def add(x, y, *args) -> int:
    print(args)
    return x + y


newadd = functools.partial(add, 1, 3, 6, 5)
print(newadd(7))
print(newadd(7, 10))
# print(newadd(9,10,y=20,x=26))#报错，x,y已经填充过
print(newadd())


def add(x, y):
    return x + y


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


newadd = partial(add, y=6)
newadd(4)



#lru_cache # args 参数会变成元组, 元组k中元素不同，则key 不同  kwargs 参数会变成有序字典

def lru_cache(maxsize=128,typed=False):
    def decorating_function(user_function):
        wrapper = _lru_cache_wrapper(user_function,maxsize,typed,_CacheInfo)
        return update_wrapper(wrapper, user_function)

@functools.lru_cache()
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) +fib(n-2)
print([fib(x) for x in range(3)])