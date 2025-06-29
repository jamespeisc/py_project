class A:  # 类对象
    """Class A""" #类属性
    x = 1  # 属性

    def show(self):  # 函数定义在类中为方法
        print(self.x)  # self 类的实例的本身


# 大驼峰,首字母大写

class Person:
    def __init__(self, name):
        print(name)

print(A) #<class '__main__.A'>
print(A.x)#1
print(A.show)#<function A.show at 0x000001E8AB12D678>
print(A.__doc__)
#print(A.show())#报错
print(A().show()) #A()实例化
A().show()