
for i in range(10):
    if i & 0x01:  #为什么用16位
        continue
    print(i)
field_names=None

from collections import namedtuple

Student = namedtuple('stu','name age')
#Student = namedtuple('stu',['name','age']) ?

if isinstance(field_names, str):
    field_names = field_names.replace(',',' ').split()
field_names = i(map(str, field_names))
typename = str(typename)
lst = []
for j in lst:
    if j > i ** 0.5:
        flag = True
        break
    if i % j == 0:
        flag = False
        break
#2个if 和 if else的区别

nums = []

for i in range(3):
    nums.append(int(input('{}: '.format(i))))  #input的用法

for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill} {align}16}'.format(text, fill=align, align=align)) #报错


#d.update('5'='def')
#SyntaxError: keyword can't be an expression

s3 = {str(x):y for x in range(3) for y in range(4)} #输出{'0': 3, '1': 3, '2': 3} key 去重

def login(host='127.0.0.1',port='8080',username='wayne',password='magedu'):
    login('127.0.0.1', '80', 'pass', username='root') #TypeError: login() got multiple values for argument 'username'


sorted(lst,key=lambda x:6-x) #规则是什么
#可变参数和参数解构的区别？
#带参装饰器和无参装饰器的区别（无参装饰器中参数里外一致，带参装饰器的参数为被修饰的函数？）

class Animal:
    x = 123
    def __init__(self):
        self.y = '456'
    def shout(self):
        print('Animal shouts')

class Cat(Animal):
    x= 'abc'
    def __init__(self):
        self.y = 'xyz'
    def shout(self):
        print("Miao")
    def shout(self):   # 下面的覆盖上面的shout方法
        print('~~~~~~~~~~')
        Animal.shout(self) #为什么要加self


# thread 的 args
# 线程中全是 thread， 主线程是哪个
# python gil 多线程 单cpu  多cpu

# self.clients = {}
# self.clients[raddr] = s
# s, raddr = self.sock.accept()
# event
