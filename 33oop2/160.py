class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}:[]".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)


p = Point(4, 5)
print(p)
print(p.__dict__)
# p.z = 10
# print(p.__dict__)
# p.__dict__['y'] = 16
# #print(p.__dict__)
#
# print(sorted(dir(p)))
# print(sorted(p.__dir__()))


setattr(p,'z',100)
setattr(p,'y',160)
setattr(Point,'X','x')
print(getattr(p,'__dict__'))
print(p)
print(p.__dict__)
print(1,getattr(p,'__dict__'))
print(2,getattr(Point,'__dict__'))
p.show()
#setattr(Point,'show',lambda self: print(self.x+ self.y))
p.show()
Point.show(self=p)
setattr(p,'show',lambda self: print(self.x +self.y))
print(3,p.__dict__)
p.show(p)

del p.show





print(hasattr(p,'x'))

class Adder:
    def __init__(self):
        self.sum = 0

    def __call__(self, *args):
        ret = 0
        for x in args:
            ret += x
        self.sum += ret

        return self.sum