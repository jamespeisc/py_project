class A:  # 类对象
    """Class A"""
    x = 1  # 属性

    def show(self):  # 函数定义在类中为方法
        print(self.x)  # self 类的实例的本身

    # show = lambda x: 0


# 大驼峰


# print(A())
print('-------------------------------')
print(A().show())
print('-------------------------------')
print("a.show", A().show)  # <bound method A.show of <__main__.A object at 0x0000011B70A9EBC8>>
print(A.show)  # <function A.show at 0x0000011B70EFCCA8>

# hex(id(a.show))
# hex(id(A.show))

a = A()
print(a.show())


class Person:
    def __init__(self, name):  # 前后有下划线的方法，为魔术方法，初始化方法
        print(name)


# p = Person()  # 报错
p = Person('tom')  # 输出tom
print('###########################################')
print(Person('tom'))


class Car:
    def __init__(self, mark,price):
        self.mark = mark
        self.price= price
        # print(mark)


car = Car('red flag',100)
car2 = Car('Tesla',200)
print('=============')
print(car)
print(car.mark)
print(car.price)
print(car2.mark)
print(car2.price)
#实例化是__new__方法


# 实例化 加括号

# __init__(self) 方法，可以不定义，如果没有定义会在实例化后隐式调用，作用： 对实例进行初始化


class MyClass:
    def __init__(self):
        print('init')


print(MyClass)  # 不会调用
print(MyClass())  # 调用 _init__
a = MyClass  # 调用 __init__


# __init__ 第一参数必须要有，习惯上为self __init__(self, name, age)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showage(self):
        print('{} is {}'.format(self.name, self.age))

tom = Person2('tom', 19)
jerry = Person2('jerry', 17)
tom.showage = jerry.showage
print(tom)
print(tom.showage)

print(tom.showage == jerry.showage)

print(jerry.age)

#__init__() 方法不能有返回值，只能是none


class MyClass:
    def __init__(self):
        print('self in init={}'.format(id(self)))


c = MyClass()
print('c={}'.format(id(c)))

d = MyClass()
print('d={}'.format(id(d)))