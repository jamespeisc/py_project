# class A:
#     pass
# print(hash(A))
# print(hash(A()))
# print(hash(A))
# print(hash(A()))
#
# print('———————————————————————————————————————')

class A:
    def __init__(self,name='tom',age=18):
        self.name = name
        self.age = age
    def __hash__(self):
        return 1  # 实例return1
    def __repr__(self):
        return "<A name={},age={}>".format(self.name,self.age)
    def __eq__(self, other): #告诉使用者如何比较对象
        return self.age == other.age
#
# print(hash(A))
# print(hash(A('tom')))
# print(hash(A))
# print(hash(A('tom')))

#实例化后hash都相同，https://blog.csdn.net/horses/article/details/123787158

item = [A('tom',18),A('tom',18)]
print(item)
item = (A('tom',18),A('tom',18))
print(item)
item = {A('tom',18),A('jerry',18)}
print(item)
#__eq__ 对应 ==
a = A()

import collections

print(isinstance(a,collections.Hashable))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    # def __eq__(self,other):
    #     return False

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "{} {} {}".format(id(self),self.x,self.y)


A = Point(1,2)
B = Point(1,2)
print('~~~~~~~~~~~~~~~~~~~~~')
print(A==B)
print(A)
print(B)
# print(hash(A))
# print(hash(B))
