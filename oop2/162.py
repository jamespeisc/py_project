class Base:
    n = 0
class Point(Base):
    z=6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __getattr__(self, item):
        return "missing {}".format(item)
    def __getattribute__(self, item): # 访问所有属性的时候都会触发函数，绝对函数的行为
        #return item
        pass

p1 = Point(4,5)
print(p1.__dict__)

# 属性查找属性 __getattribute__()/ instance.__dict__-->instance.__class__.__dict__-->继承的祖先类（直到object）的__dict__-->调用__getattr__()