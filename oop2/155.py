class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        # return False
        return True

    def __repr__(self):
        return "{} {} {}".format(id(self), self.x, self.y)


class TriPoint:
    def __len__(self):
        return 1


#可视化


p1 = Point(4, 5)
p2 = Point(4, 500)
print(p1,repr(p1))
print('!!!!!!!!!!!!')
print(dir(p1))
print(bool(p1), bool(p2))

if TriPoint():
    print('Real IP')

# format() 和 print 函数调用 __str__ 其他调用 __repr__
#byte 后要加可迭代对象
