class Animal:
    x = 123
    def __init__(self):
        self.y = '456'
    def shout(self):
        print('Animal shouts', self.__class__.__name__, self.y)
    @classmethod
    def showx(cls):
        print(cls.x)

class Cat(Animal):
    x = 'abc'

    def __init__(self):
        self.y = 'xyz'

    def shout(self):
        print("Miao")

    def shout(self, x=None):  # 下面的覆盖上面的shout方法
        print('~~~~~~~~~~')
        Animal.shout(x)

    def speak(self, x=None):  # 下面的覆盖上面的shout方法
        print('~~~~~~~~~~')
        super().shout()  # 类是父类，但是self 是字类的
    @classmethod
    def showx(cls):
        print(cls.x)
a = Animal()
a.shout()
print(a.y)
c = Cat()
c.shout(a)
c.speak(a)
Cat.showx()