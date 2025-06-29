class A:
    def __init__(self,x):
        self.x = x
        print(2,'A init')

    def __set__(self, instance, value):
        print(3, self,instance,value)

    def __get__(self,instance,owner):
        print(4, self,instance,owner)

# 上面就是描述器，必须实现 __set__ __del__ 和 __get__方法的某一个
# 描述器必须使用类属性
class B:
    x = A(1)

    def __init__(self):
        print(1,'B init')
b = B()
(B.x)

# 访问属性 实际是个类或者类的实例
