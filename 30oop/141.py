class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age  # 隐藏属性

    def showage(self):  # __showage 私有方法
        print(self.__age)

    def growup(self, i=1):
        if 0 < i < 100:
            self.__age += i
        else:
            raise Exception()


print(Person.__dict__)



tom = Person('tom', 20)
tom._name = 'jerry'
print(tom._name)
tom.showage()
tom.__age = 2000
print(tom.__age)
print(tom._name)
tom._Person__age = 30000
tom.showage()
print(tom.__dict__)


# 私有属性，使用双下划线的属性名，就是私有属性，
# _类名__变量名

# _变量名: 保护变量,让编程者自己保护，内部使用的，不要轻易使用和覆盖
# 单下划线只是开发者之间的约定，解释器不做任何改变
# 双下划线的方法是私有方法，解释器会改名，改名策略和私有变量相同，_类名__方法名
# 方法变量都在类的__dict__ 中可以找到
# 成员= 属性 + 方法
# #  属性装饰器

class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def getage(self):
        print(self.__age)

    def setage(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter  # 必须用age 这种格式
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        print('delete age')


# x = property(getage,setage,None,'x property')

tom = Person('tom', 20)

print(tom.age)
tom.age = 30
print(tom.age)


class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age

    x = property(getage, setage, None, 'x property')
    x = property(lambda  x:x.__age)


tom = Person('tom', 20)
print(tom.x)
tom.x = 50
print(tom.x)

