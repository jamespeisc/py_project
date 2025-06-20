class Animal0:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name

    def shout(self):
        print('{} shouts'.format(self.__class__.__name__))
        print('{} shouts'.format(self._name))


class Cat0(Animal0):  # 将Animal0 放在后面
    def shout(self):
        print('Miao')
    # def shout(self):
    #     print('Cat shouts')


class Dog0(Animal0):
    pass
    # def shout(self):
    #     print('Dog shouts')


a = Animal0('monster')
a.shout()
c = Cat0('garfield')
c.shout()
d = Dog0('ahuang')
d.shout()

print(d.__class__.__name__)

# 继承 包括属性和方法
# 父类 = 基类 超类
# 子类 派生类
#class 子类名(基类1，基类2(多继承))， object类市所有对象的根基类

class A:
    pass
# 等价于
class A(object):
    pass


# __base__ 类的基类
# __bases__ 类的基类元组
# __mro__ 显示方法查找顺序，基类的元组
# mro() 同上
# subclasses()

print(int.mro())
print(int.__mro__)
print(int.__base__)
print(int.__bases__)
print(int.__subclasses__())

# 访问控制 私有的都是不可以访问的 当私有变量所在的类内的方法中可以访问这个私有变量
a = A()

print(dir(a))