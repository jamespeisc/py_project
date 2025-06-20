# class A:
#     X = 1
#
#     def __init__(self):
#         self.y = 5
#         self.z = 6
#
#     def show(self):
#         print(self.X, self.y, self.z)
#
# a = A()
#
# print(A.__dict__)
# print(a.__dict__)

class Point:
    Z = 100
    __slots__ = ('x', 'y')  # 固定后，不能增加属性

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3d(Point): pass


p1 = Point(4, 5)
p1.x = 14
# p1.z = 15
# p1.Z =2000

p2 = Point3d(4, 5)
p2.a = 2000

print(p2.__dict__)  # 无法继承父类属性
# 一旦类提供了__slots__,就就阻止实例产生__dict__；来保存实例的属性,不会影响子类

# print(p1.__slots__)
# print(Point.__dict__)
# 未实现和未实现异常
print('~~~~~~~~~~~~~~~')
print(NotImplemented)
print(type(NotImplemented))
print(NotImplementedError)
print(type(NotImplementedError))
import sys

try:
    raise NotImplementedError
except:
    print(sys.exc_info())

# NotImplemented 是个值，单值，是NotImplementedType的实例
# NotImplementedError是类型,是异常,返回type

class A:
    def __init__(self,x):
        self.x = x
    def __add__(self, other):
        pass
    def __iadd__(self, other):
        pass
    def __radd__(self, other):
        pass

print(2**3)
a = A(4)
b = A(5)
print(a+b) # 调用add 方法
a += b # 调用iadd

