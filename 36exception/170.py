def foo1():
    return 1 / 0


def foo2():
    print('begin')
    try:
        foo1()
    except ZeroDivisionError as e:
        print('error', e)
    print('end')


# foo2()

def foo1():
    return 1 / 0


def foo2():
    print('begin')
    try:
        foo1()
    except IndexError as e:
        print('error', e)
    except:
        # raise
        raise RecursionError  # 匹配后又raise
        pass
    finally:
        print('end')


# foo2()

# 异常捕的时机
# 1, 立即捕获

def parse_int(s):
    try:
        pass
    except Exception as e:
        print(e)
    else:
        print('ok')


# 2 边界捕获
# 函数的异常应该抛向外层

# else 子句

try:
    ret = 1 * 0
except ArithmeticError as e:
    print(e)
else:
    print('OK')
finally:
    print('fin')


# 总结

# try:
#     语句 #运行别的代码
# except <异常类>:
#     <语句> # 捕获某种类型的异常
# except <异常类> as <变量名>:
#     <语句>  # 捕获某种类型的异常并获得对象
# else:
#     <语句>  # 如果没有异常发生

# try的工作原理
# 1，如果try中语句执行时发生异常，搜索except子句，并执行第一个匹配该异常的except子句
# 2，如果try中语句执行时发生异常，却没有匹配的except子句，异常将被递交到外层的try，如果外层不处理这个异常，
# 异常将继续向外层传递。如果都不处理该异常，则会传递到最外层，如果还没有处理，就终止异常所在的线程
# 3，如果在try执行时没有发生异常，将执行else子句中的语句
# 4，无论try中是否发生异常，finally子句最终都会执行