class Animal:
    x = 123


class Cat(Animal):
    x = 'cat'


class Dog(Animal):
    x = 'dog'


print(Cat.mro())
print(Cat.__mro__)


class Carfield(Dog, Cat, int):  # 按照顺序
    pass


print(Carfield.mro())
print(Carfield.x)


# word 和 pdf 都指向 document类 Document类是所有文档类的抽象基类。 word和pdf是Document的子类
# 抽象类不允许实例化
class Document:
    def __init__(self, content):
        self.content = content

    def print(self):
        raise NotImplementedError('抽象基类没有实现')


class Word(Document): pass


class Pdf(Document): pass


def printable(cls):
    cls.print = lambda self: print(self.content)
    return cls


@printable  # PrintableWord=printable(PrintWord) 右侧
class PrintableWord(Word): pass

# 装饰器另外一种写法
#
# def myprint():
#     pass
#
#
# def printable(func, cls):
#     cls.print = func
#     return cls
#
#
# def printable(cls):
#     def _print(self):
#         print(self.content)
#
#     cls.print = _print
#     return cls



# @printable(myprint)
# class PrintableWord(Word): pass

pw = PrintableWord('test string')
pw.print()

# 抽象类，下面报错
# word = Word('test word')
# word.print()


#mixin 写个新类，多继承

class Document:
    def __init__(self,content):
        self.content = content

class Word(Document):pass

class Pdf(Document):pass

class PrintableMixin:
    def print(self):
        print(self.content,'Mixin')

class PrintableWord(PrintableMixin,Word): pass
print(PrintableWord.__dict__)
print(PrintableWord.mro())
pw = PrintableWord('test string')
pw.print()

class SuperPrintableMixin(PrintableMixin):
    def print(self):
        print('~' * 20)
        super().print()
        print('~' * 20)

class PrintableWord(PrintableMixin,Word):pass
print(PrintableWord.__dict__)

# 本质上是多继承实现，体现的是组合的设计模式

