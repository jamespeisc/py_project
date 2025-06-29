def outer():
    def inner():
        print('inner')
    print('outer')
    inner()
outer()
#inner()

x = 5
def show():
    #x += 1
    print(x)
show()

def outer1():
    o=65
    def inner():
        print("inner {}".format(o))
        print(chr(o))

    print("outer {}".format(o))
    inner()
outer1()

def outer2():
    o=65
    def inner():
        o=97
        print("inner {}".format(o))
        print(chr(o))

    print("outer {}".format(o))
    inner()
outer2()


x =5
def foo():
    x =1
    y= x+1
    x= x+1
    print(x)
foo()


z=5
def foo():
    global z #变成全局变量
    z +=1
    print(z)
foo()

#使用global 关键字变量，将foo内的x声明为使用外部的全局作用域定义的x
#全局作用域中必须有x的定义

def counter():
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc
foo = counter()
print(type(foo))
print(foo(),foo())
# c=100
# print(foo())
#内部函数用到了外部的变量
#nonlocal
#局部定义域不算global


def counter():
    count = 0
    def inc():
        nonlocal  count
        count += 1
        return count
    return inc
foo = counter()

print(foo())
print(foo())


#默认值的作用域

def foo(xyz=1): #局部变量

    print(xyz)
foo()
foo()
#print(xyz)

def foo(xyz=[]):
    xyz.append(1)
    print(xyz)
foo()#[1]
foo()#[1,1]#把默认值放到函数特殊属性中
#print(xyz) #报错

def foo(xyz=[],m=5,n=6):
    xyz.append(100)
    print(xyz)


print('def1', foo.__defaults__)
print('fooid',foo(),id(foo))
print('def2',foo.__defaults__)
print('fooid2',foo(),id(foo))
print('def3',foo.__defaults__)
#函数没有变，调用它的属性__defaults__使用元组保存所有默认值
#xyz默认值是引用类型，引用类型的元素变动，并不是元组的变化

def foo(w,u='abc',z=123):
    u='xyz'
    z=789
    print(w,u,z)
print(foo.__defaults__)
foo('magedu')
print(foo.__defaults__)
#属性__defaults__中使用元组保存所有默认值，它不会因为在函数体内使用了它而发生改变

def foo(xyz=[],u='abc',z=123):
    xyz=xyz[:]
    xyz.append(1)
    print(xyz)
foo()
print(foo.__defaults__)
foo()
print(foo.__defaults__)
foo([10])
print(foo.__defaults__)
foo([10,5])
print(foo.__defaults__)


def foo(xyz=None,u='abc',z=123):
    if xyz is None:
        xyz=[]
    xyz.append(1)
    print(xyz)
foo()
print(foo.__defaults__)
foo()
print(foo.__defaults__)
foo([10])
print(foo.__defaults__)
foo([10,5])
print(foo.__defaults__)


def foo(xyz=None,u='abc',z=123):
    if xyz is None:
        xyz =[]
    xyz.append(1)
    return xyz

lst = foo()
a=foo(lst)
print(a)

#第一种方法，使用影子拷贝创建一个新的对象，永远不能改变传入的参数
#第二种方法，通过值的判断灵活的选择创建或者修改传入对象，使用None这个不可变的值作为默认参数

def foo(xyz=[],u='abc',z=123):
    xyz.append(1)
    return xyz
print(foo(),id(foo),foo.__defaults__)

def foo(xyz=[],u='abc',z=123):
    xyz.append(1)
    return xyz
print(foo(),id(foo),foo.__defaults__)

del foo()
print(foo(),id(foo),foo.__defaults__)
