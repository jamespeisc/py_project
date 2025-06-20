import math
import json
import msgpack
import pickle
class Shape:
    @classmethod
    def area(self):
        raise NotImplementedError('基类未实现')


class Triangle(Shape):
    @classmethod
    def area(cls, a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(Triangle.area(4, 5, 6))


class Shape:
    @property
    def area(self):
        raise NotImplementedError('基类未实现')


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(Triangle(4, 5, 6).area)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r * self.r * math.pi



class SerializableMixin:

    def dumps(self,m='json'):
        if m =='json':
            return json.dumps(self.__dict__)
        elif m == 'msg':
            return msgpack.dumps(self.__dict__)
        else:
            return pickle.dumps(self.__dict__)
class SerializableCircleMixin(SerializableMixin,Circle):pass

c= SerializableMixin(4)
print(c.area)
print(c.dumps())

c = Circle(4)



json.dumps(c.__dict__)
