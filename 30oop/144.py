import random


class Randomint4:
    def __init__(self,count=5,start=1,stop=100):
        self._count = count
        self.start = start
        self.stop = stop
        self._gen = self._generate()
    def _generate(self):
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self._count)]
            #yield [random.randint(self.start, self.stop) for _ in range(self._count)] # 对应 print(r4.generate2(10))
    # def generate(self):
    #     return [next(self._gen) for _ in range(self._count)]

    def generate(self,count=10):
        if count > 0:
            self._count = count
        return next(self._gen)


r4 = Randomint4()
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<Point {}:{}>".format(self.x,self.y)
    def __repr__(self):
        return "<Point {}:{}>".format(self.x,self.y) #用这个


# points = zip(r4.generate(), r4.generate())
#
# for x in points:
#     print(x)

points = [Point(x,y) for x,y in zip(r4.generate(),r4.generate())]
# 第2种写法
points = [Point(*v) for v in zip(r4.generate(),r4.generate())]
print(points)

# for x in points:
#     print(x,'+')

for point in points:
    print("<Points {}:{}>".format(point.x,point.y))




# list(points) 迭代器仅能用一次

#print(r4.generate2(10))

class Car:
    id = 0
    def __init__(self,mark,speed,color,price=-1, **kwargs):
        self.id = self.id +1
        self.mark= mark
        self.speed = speed
        self.color = color
        self.price = price
        self.__dict__.update(kwargs) # 上下都可以
        self.properties = kwargs # 上下都可以

class CarInfo:
    cars = []
    def addcar(self, *cars):
        self.cars.extend(cars)
    def getall(self): #建议列表
        return self.cars
    def getcarbyid(self,id): #建议字典
        pass

car1 = Car('Red Flag', 100, 'red')
car2 = Car('audi', 120, 'black')
ci = CarInfo()
ci.addcar(car1,car2)


###################新整理################################


class Car:
    id = 0

    @classmethod
    def genid(cls):
        cls.id = cls.id + 1

    def __init__(self, mark, speed, color, price=-1, **kwargs):
        self.id = self.genid()
        self.mark = mark
        self.speed = speed
        self.color = color
        self.price = price
        self.__dict__.update(kwargs)  # 上下都可以
        self.properties = kwargs  # 上下都可以

    def __repr__(self):
        return "<Car {}.{}>".format(self.mark, self.color)

class CarInfo:
    cars = []
    def addcar(self, *cars):
        self.cars.extend(cars)
    def getall(self): #建议列表
        return self.cars
    def getcarbyid(self,id): #建议字典
        pass


car1 = Car('Red Flag', 100, 'red')
car2 = Car('audi', 120, 'black')

ci = CarInfo()
ci.addcar(car1,car2)

print(ci.getall())
