def add_name(name):
    def wrapper(cls):
        cls.NAME = name
        return cls

    return wrapper


def add_name1(cls):
    cls.NAME = 'TOM'
    return cls


@add_name('tom')  # Person = add_name('tom')(Person)
# @add_name1 #Person=add_name1(Person)
class Person:
    AGE = 8


print(Person.__dict__)


#
class Person:
    def normal_function(a, b, c):
        print('normal_function')
        print(a)
        print(b)
        print(c)


Person.normal_function(1, 2, 3)


class Person:
    def normal_function(): #禁止使用
        print('normal_function')
Person.normal_function()  # 不能完成实例绑定
# Person().normal_function() 保错
print(Person.__dict__)


# 类中可以定义无参函数


class Person:

    @classmethod  # 装饰的方法就变成类方法
    def class_method(cls):  # 传入类
        print('class_method{} -> {}'.format(cls, type(cls)))
        x = cls()
        print(x, id(x))

    def __init__(self):
        print(id(self), '~~~~~~~~~~~~~~')


print(Person.__dict__)
Person.class_method()
Person().class_method()


class Person:
    @staticmethod # 可以不传参

    def static_method():
        print('static method')

print(Person.__dict__)

# 总结
# 类除了普通方法都可以调用，普通方法需要对象的实例作为第一参数
# 实例可以调用所有类中定义的方法，包括类方法，静态方法，普通方法传入实例自身，静态方法和类方法需要找到实例的类