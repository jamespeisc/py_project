# with open('test') as f:
#     pass
import sys


class A:
    def __init__(self,name='tom'):
        print('init')
        self._name = name


    def __enter__(self): # 它的返回值 将作为as 子句后面变量的值
        print('enter')
        return self._name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('exit')

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "my name is {}".format(self._name)
# 上下文管理，保证资源清理
with A() as a:
    #raise Exception('Wrong')
    #sys.exit(-100)
    print('mid') # 不会打印

f = A()
with f as a:
    print(f ==a)
    print(f)
    print(a)

# 实例化对象的时候，并不会调用enter，进入with语块调用 __enter__ 方法，然后执行语句体，最后离开with语句块的时候，调用 __exit__方法

f = A()

with f:
    print(f)  # 打印__str__ 输出值
    print('mid')

with A('jerry') as f:
    raise Exception('wrong')
    print(f)  # 打印jerry