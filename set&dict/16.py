lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
length = len(lst)
for i in range(length):
    x = lst[i]
    maxindex = i
    for j in range(i + 1, length):
        if lst[j] > lst[maxindex]:
            maxindex = j
    if i != maxindex:
        lst[i], lst[maxindex] = lst[maxindex], lst[i]
print(lst)

d = dict()
print(d)
d = {}
print(d)
d = dict(a=1, b=2)
print(d)  # 返回{'a': 1, 'b': 2}

d = dict(([1, 'a'], [2, 'b']))
print(d)  # 返回{1: 'a', 2: 'b'}
d = {'a': 10, 'b': 20, 'c': None, 'd': [1, 2, 3]}
print(d)
d = dict.fromkeys(range(5))
print(d)
d = dict.fromkeys(range(5, 10), [0, 1, 2, 3, 4])
print(d)
print(id(d[5]), id(d[6]))
d[5] = 'abc'
# d[key],通过key找到值
print(d)
print(d.get(6))
# 找不到，不报错，get(key,[,default])
d.setdefault(100)
print(d)
d.setdefault(101, 'abc')
print(d)
d.update({5: 'bcd'})
d.update(red=1)
d.update((('red', 2),))
d.update({'red': 3})
d.pop(5)
d.popitem()  # 随机弹出一个
k, v = d.popitem()
print(k, v)
print(d)

# b =[6]
# d= {'b':[6]}
# del b #删除了引用
# print(d)
#
# b =d['b']
# del b[0]

# for i in d:
# #for i in d.keys()
#     print(i)
#     print(i,":",d[i])
# print(d)
#
# d[('d',300)] =300
# print(d)
#
# for key in d.keys():
#     print (key)
#     print(d[key])
# print('************************************')
#
# for value in d.values():
#     print(value)
# print(len(d))
# for i in range(len(d)):
#     print(d.keys(),d.values())
# for key,value in d.items():
#     print(key,value)

for item in d.items():
    print(item)
for item in d.items():
    print(item[0], item[1])

for k, _ in d.items():
    print(k)
for _, v in d.items():
    print(v)
print('-------------')
print(d.keys)

lst = []
for k in d.keys():
    print(k)
    lst.append(k)
print('############')
for k in lst:
    d.pop(k)
    print('d', d)
# while len(d):
#     d.popitem()
#     print(d)

# defaultdict

import random

d = {}
for c in 'abcde':
    for i in range(random.randint(1, 5)):
        if not d.get(c):
            d[c] = []
        d[c].append(i)
print(d)

import  random

from collections import defaultdict
d = defaultdict(list)
for c in 'abcde':
    for i in range(random.randint(1, 5)):
        d[c].append(i)
print(d)
#有序字典
from collections import OrderedDict
od = OrderedDict(a=1,b=2,c=3)
print(od)# 输出OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od[100] =100
print(od)

