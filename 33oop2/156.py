#运算符重载指的是将运算符与类方法关联起来，每个运算符对应一个指定的内置方法
from functools import total_ordering
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __sub__(self, other):
        return self.age - other.age

    def __isub__(self, other):
        self.age = self.age - other.age
        return self
        # return Person(self.name, self.age - other.age) # 返回一个新的实例
    def __repr__(self):
        return "{}的年龄为{}".format(self.name, self.age)

tom = Person('tom')
jerry = Person('jerry',age =16)
print (tom -jerry) # = tom.__sub__(jerry)
print(jerry - tom)
jerry -= tom
print(jerry,type(jerry))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "return repr {} {} {}".format(id(self), self.x, self.y)

    def __add__(self, other):
        # self.x = self.x + other.x
        # self.y = self.y + other.y
        # return self
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x  and self.y == other.y

    def __iadd__(self, other):
        # return self.x == other.x and self.y = self.y
        return self + other

    def __gt__(self, other):
        return self.x > other.x

    def __ge__(self, other):
        return self.x >=other.x and self.y >= other.y


p1 = Point(4,4)
p2 = Point(3,3)

print(p1 + p2)

p1 += p2
print(p1)
print(p1==p2)
print(p1>p2)
print(p1 !=p2)
print(p1 <p2)
print('~~~~~~~~~~~~~~')

print(p1 >= p2)
print(p1 <= p2)

# 运算符重载应用场景，把数学符号 换成一般的操作
#__getitem__ / __setitem__ #实现 self[key]访问和设置
#__missing__ 字典和其子类使用__getitem__调用时 key不存在时执行

class A(dict):
    def __missing__(self, key):
        print('miss key={}'.format(key))
a = A()

a[1] =1
print(a[4])

class Cart:
    def __init__(self):
        self.items = []
    def __len__(self):
        return len(self.items)
    def __iter__(self):
        yield from self.items
        #return iter(self.items)

    def additem(self,item):
        self.items.append(item)
        return self
    def __add__(self, item):
        self.items.append(item)
        return self
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        self.items[index] = value
    def __str__(self):
        return "{}".format(self.items)
cart = Cart()
len(cart)
cart.additem(1)
cart.additem('abc')
for x in cart:
    print(x)
print(1 in cart)
cart[1] =1000
cart +500 +600
cart.additem(900).additem(100) # 链式编程
print(cart)