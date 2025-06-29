import inspect
from functools import partial


class A:
    @classmethod  # 非数据描述器
    def foo(cls):
        pass

    @staticmethod  # 非数据描述器
    def bar():
        pass

    @property  # 数据描述器
    def z(self):
        return 5

    def getfoo(self):  # 非数据描述器
        return self.foo

    def __init__(self):  # 非数据描述器

        self.foo = 100
        self.bar = 200


class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print('static method get')
        return self.fn


class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, cls):
        print('class method get')
        return partial(self.fn, cls)


class A:
    @StaticMethod  # s_mtd = StaticMethod(s_mtd)
    def s_mtd():
        print('static method')

    @ClassMethod
    def c_mtd(cls):  # c_mtd =ClassMethod(c_mtd)
        print('{}class method'.format(cls))


A.s_mtd()
A.c_mtd()


class Person:

    def __init__(self, name: str, age: int):
        params = ((name, str), (age, int))
        if not self.checkdata(params):
            raise TypeError()
        self.name = name
        self.age = age

    def checkdata(self, params):
        for n, t in params:
            if not isinstance(n, t):
                # raise TypeError('{} {}'.format(n,t))
                return False
        return True


print(inspect.signature(Person))
print(inspect.signature(Person).parameters)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
class TypeCheck:
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("{} {}".format(self.key, self.type))
        instance.__dict__[self.key] = value








class Person:
    name = TypeCheck('name', str)
    age = TypeCheck('age', int)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p1 = Person('tom', 20)
# p2 = Person('jerry','21')
p2 = Person('jerry',21)
print(p1.__dict__)
print(p2.__dict__)
print(p1.name,p1.age)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

class TypeCheck:
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("{} {}".format(self.key, self.type))
        instance.__dict__[self.key] = value

def typeassert(cls):
    print(inspect.signature(cls))
    params = inspect.signature(cls).parameters
    print(params)
    for name,param in params.items():
        #print(name,param)
        if param.annotation != param.empty:
            setattr(cls,name,TypeCheck(name,param.annotation))
    return cls

class TypeAssert:
    def __init__(self,cls):
        self.cls = cls
    def __call__(self, name, age):
        params = inspect.signature(self.cls).parameters
        for name,param in params.items():
            #print(name,param)
            if param.annotation != param.empty:
                setattr(self.cls,name,TypeCheck(name,param.annotation))
        print('~~~~~~~',self.cls.__dict__)
        return self.cls(name,age)


@TypeAssert
#@typeassert
class Person:
    # name = TypeCheck('name', str)
    # age = TypeCheck('age', int)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# p1 = Person('tom', 20)
# # p2 = Person('jerry','21')
# p2 = Person('jerry',21)
# # print(p1.__dict__)
# # print(p2.__dict__)
# # print(p1.name,p1.age)

print(Person.__dict__)
p1 = Person('tom', 20)
print(p1.name,p1.age)
# print(p1.__dict__)