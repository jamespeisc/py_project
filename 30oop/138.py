class Person:
    age = 3
    def __init__(self, name):
        self.name = name #和某个实例相关
        self.age = 18


tom = Person('Tom')
jerry = Person('jerry')

print(tom.name, tom.age)
print(jerry.name, jerry.age)
print(Person.age) #类变量

#实例可以继承类的属性，所有实例共享的属性和方法

print(Person.__name__)

#特殊属性

#__name__: 对象名
#__class__: 对象的类型
#__dict__: 对象的属性的字典
#__qualname__: 类的限定名

print(sorted(Person.__dict__.items()), end='\n\n') #属性字典
print(sorted(Person.__dict__), end='\n\n') #属性字典

#实例字典仅存实例本身，类属性存完整
print(type(tom).age)
#print(tom.__class__.age) 等价于 print(type(tom).age)
#类的属性保存在类的__dict__中，实例属性保存在实例的__dict__中，如果从实例访问类的属性，就需要借助__class__找到所属的类