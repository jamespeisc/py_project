import bisect


def get_grade(*scores,breakpoints =[60,70,80,90], grades='EDCBA'):
    for score in scores:
        index = bisect.bisect(breakpoints,score)
        print(index)
        print(grades[index])
        print (grades[index])
get_grade(60,65,70,78)

print(get_grade.__name__)
print(get_grade.__module__)
#__class__ #__bases__ #__doc__ #__mro__ # __dict__

#__dir__ 返回类或者对象的所有成员名称列表

#print(get_grade.__dir__()) #返回属性列表
class A :pass
print(dir())
print(sorted(dir(get_grade)))
print(sorted(dir(A)))
print(__file__)

#魔术方法
#__init__: 初始化
#__del__ :
