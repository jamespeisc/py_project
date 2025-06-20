import random


class Randomint:
    def __init__(self,start=1,stop=100,count=50):
        self.start = start
        self.stop = stop
        self.count = count
    def genint(self):
        return [random.randint(self.start,self.stop) for _ in range(self.count)]


gen1 = Randomint(1,10,5)

for i in gen1.genint():
    print(i,end=' ')

class Randomint2:
    @classmethod
    def genint2(cls,count=5,start=101,stop=200):
        return [random.randint(start,stop) for _ in range(count)]

for i in Randomint2.genint2(2,100,200):
    print(i,end=' ')

class Randomint3:
    def __init__(self,start=1,stop=100,count=50):
        self.start = start
        self.stop = stop
        self.count = count
    def genint3(self,count):
        count = self.count if count <= 0 else count
        return [random.randint(self.start,self.stop) for _ in range(count)]

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self,value):
        self._count = value


r3 = Randomint3()
r3.count=5
for i in r3.genint3(2):
    print(i)


class Randomint4:
    def __init__(self,start=1,stop=100,count=5):
        self.start = start
        self.stop = stop
        self._count = count
        self._gen = self._generate()
    def _generate(self):
        while True:
            yield random.randint(self.start,self.stop)
            #yield [random.randint(self.start, self.stop) for _ in range(self._count)] # 对应 print(r4.generate2(10))
    def generate(self):
        return [next(self._gen) for _ in range(self._count)]

    def generate2(self,count=0):
        if count > 0:
            self._count = count
        return next(self._gen)

r4 = Randomint4()
print(r4.generate())
#print(r4.generate2(10))