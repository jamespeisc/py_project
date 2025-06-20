# import math
# print(bool(""))
# print(math.floor(2.5),math.floor(-2.5)) #输出2 -3
# print(math.ceil(2.5),math.ceil(-2.5)) #输出3，-2
# print(int(3.6),int(2.5),int(1.4)) #输出 3 2 1
# print(int(-3.6), int(-2.5), int(-1.4)) #输出 -3，-2，-1
# print(round(2.1),round(2.5),round(13.5))
# #round 规则：4舍六入 5取偶，离它最近的偶数
# #round 规则：4舍六入 5取偶，离它最近的偶数
# #round 规则：4舍六入 5取偶，离它最近的偶数
# print(round(-2.5), round(-2.5001),round(-2.6))#输出 -2 -3 -3
# print(7//2, 7//-2,-7//2, -(7//2)) #输出 3，-4, -4,-3,复数除法用floor
# print(2//3,-2//3,-1//3) #输出0 -1，-1
# # round() 四舍六入五取整  floor() 向下取整，ceil 向上取整
# #int() 取整数部分，truncate
# #//整除且向下取整
# #print(max(1,2,3,4))
# #print(min(range(5)))#返回0
# #print(bin(12)) 输出0b1100
# #print(hex(12)) 输出0xc
# #print(hex(0b1100)) 输出 0xc
# #print(math.pi) 返回3.141592653589793
# #print(type('a')) #返回类型<class 'str'>，非字符串
# # print(isinstance(123,int)) #前面的是不是后面的实例
# # print(isinstance(1.1,(tuple,str,float)))
# # print(type(1+False)) #返回int
# # print(type(1+False+1.1)) #返回float
# # print(1+False) #返回1
# #隐式类型转换

lst1 = list()
lst2 = []
lst3 = [2, 6, 9, 'ab']
lst4 = list(range(5))

print(lst1, lst2, lst3, lst4)
for i in lst4:
    print(i)
print(lst3[0], lst3[0])
# print(lst4[-6])

lst = [1, 2, 1, 1, 'ab']
# print(lst[1])
# print(lst.index(2))
# index(value,[start,[stop]])
# lst.index(1,-5,-1) #注意方向

print(lst.count(1))

# 时间复杂度 index和count的时间复杂度都是O(1)
# 列表元素的修改
# lst[1]='a'
# print(lst)
# lst.append(700) #返回none
# print(lst)
# lst.insert(0,'a')
# print(lst)
# append和insert 返回None，表明原地修改

# lst.insert(1000,'abc')
# print(lst)
#
# print(lst.insert(10000,'abd'))
# print(lst)
# print(lst[4],lst[5])
# #extend 添加可迭代对象,原地修改
# lst.extend(range(11,16))
# print(lst)
# print(lst + list(range(21,26)))#返回新列表，原列表不变
# print(['a1','b1']*5)

# print(lst,lst*2)

# x = [[1,2,3]] *3
# print(x)
# x[0][1] =20
# print(x)
# 简单类型
# 复杂类型，引用类型

# y = [1]*5
# y[0] =6
# y[1] =7
#
# print(y)
#
# y.remove(6)
# y.pop(0)
# print(y)
# r = reversed(lst)
#
# print(list(r))
#
# lst.reverse()
# print(lst)
# for i in reversed(lst):
#     print(i)
#
# print([3,4] in [1,2,[3,4]])