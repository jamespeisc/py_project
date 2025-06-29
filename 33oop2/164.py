# self 指代当前实例，调用者
# instance 是owner的实例
# owner 是属性的所属的类

class A:
    def __init__(self):
        self.a1 = 'a1'
        print(2,'A init')

    def __set__(self, instance, value):
        print(3, self,instance,value)
        instance.__dict__['x'] = value


    def __get__(self,instance,owner):
        print(4, self,instance,owner)
        return instance.__dict__['x']

class B:
    x = A()

    def __init__(self):
        print(1,'B init')

b =B()
b.x=1000
print('2222')
print(b.x)
print(b.__dict__)
print(B.__dict__)
print(A.__dict__)

#如果仅实现了 __get__,就是非数据描述符，同时实现了 __get__, __get__ 就是数据描述符
