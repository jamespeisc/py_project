# a = -5
# if a < 0:
#     print("negative")
# elif a < -1:
#     print("a=0")
# else:
#     print("positive")
# # 仅会进入一个分支
#
# score = 80
#
# if score < 0:
#     print('wrong')
# else:
#     if score == 0:
#         print('egg')
#     elif score <=100:
#         print('right')
#     else:
#         print('too big')


# a = input('-->')

# print(a)

# print("{1} {1}    {1}".format(1,2,3))

# a = 1

# for i in range(9):
#     a=(a+1)*2
# print(a)


# print(round(-2.51))
# print(round(-3.4))
# print(round(-3.5))
# print(round(-3.6))

# lst1 = [1,2,3,4,5]
# lst2 = lst1.copy()
# lst3 = lst1

# print(lst2 ==lst1)
# print(lst3 ==lst1)
# print(id(lst1))
# print(id(lst2))
# print(id(lst3))

# from collections import namedtuple

# nums = []
# out = None

# for i in range(3):
#     nums.append(int(input('{}: '.format(i+1))))


# print(nums)

# n = 2
# m = n**3

# print(m)


# lst = list(range(1,10))
# for i in lst:
#     print(i)
# print(type(lst))
# print(type(i))

# lst = [(i,j) for i in range(7) if i > 4 for j in range(20,25) if j > 20]

# print(lst)

# lst = [(i,j) for i in range(7) for j in range(20,25) if i > 4 if j > 20]

# print(lst)

# lst = [(i,j) for i in range(7) for j in range(20,25) if i > 4 and j > 20]

# print(lst)

# lst = [(i +1 ) **2 for i in range(10) ] 

# print(lst)

# set = {(x,) for x in range(10)}

# print(set)

# lst = sorted([1,5,2])
# print(lst)

# def foo(xyz=[]):
#     xyz.append(1)
#     print(xyz)

# foo()
# foo()



# def inc():
#     for i in range(5):
#         yield i
# print(type(inc))
# print(type(inc()))
# x = inc()
# print(type(x))
# print(next(x))

# # for m in x:
# #     print(m, '*')
# for m in x:
#     print(m,'**')


# def gen():
#     print('line 1')
#     yield 1
#     print('line 2')
#     yield 2
#     print('line 3')

#     return 3



# g = next(gen())
# # next(gen())
# # next(gen())
# # g = gen()
# next(gen())
# print(g)

# print(next(g))
# print(next(g))
# print(next(g))

# print(next(g, 'End'))


# def counter(n):
#     for x in range(n):
#         yield x

# def inc(n):
#     yield from counter(n)


# # foo = inc(10)
# foo = counter(10)

# print(next(foo))
# print(next(foo))

def add(x, y,z=5):
    return x + y + z

print(add(1,2))