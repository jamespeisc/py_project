class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom = Person('tom')
jerry = Person('Jerry', 20)

Person.age = 30

print(Person.age, tom.age, jerry.age)  # 输出 30, 18,20
print(Person.height, tom.height, jerry.height)  # 全是170
jerry.height = 175
print(Person.height, tom.height, jerry.height)  # 170 170 175


# 类的属性可以修改


class Person2:
    AGE = 3
    height = 170

    def __init__(self, name):
        self.name = name
        self.age = self.AGE
        self.AGE = 100

print(tom.age)
print(tom.AGE)
print(tom.__class__.AGE #输出为3，类的字典没变
tom2 = Person2('Tom')

print(tom2.age)
#
