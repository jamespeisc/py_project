from collections.abc import Callable

def a():
    pass
print(dir(a))

print(callable(a))
print(isinstance(a,Callable))
# 可调用对象：定义一个类，并实例化得到其实例，将实例像函数一样调用

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return "<Point {} {}>".format(self.x,self.y)

p = Point(4,5)
print(p)
print(p())

class Adder:
    def __call__(self, *args):
        ret = 0
        for x in args:
            ret += x
        self.ret = ret
        return  ret

adder = Adder()


print(adder(4,5,6))


class Fib:
    def __init__(self):
        self.items = [0,1,1]

    def __call__(self,n):
        l = len(self.items)
        if n <= 0:
            raise IndexError()
        elif n < len(self.items):
            return self.items[n]

        for i in range(l,n+1):
            x= self.items[i -1] + self.items[i -2]
            self.items.append(x)
        return x
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]




fib = Fib()

print(fib(5))

for i,v in enumerate(fib):
    print(i,v)