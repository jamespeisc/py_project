# list = [37,99,73,48,40,49,25,99,51]
# length = len(list)
#
# for m in range(length):
#     flag = False
#     for n in range(length -m - 1):
#         if list[n] > list[n+1]:
#             list[n],list[n+1] = list[n+1],list[n]
# print(list)

origin = [37, 99, 73, 48, 40, 49, 25, 99, 51]
# nums = [20,40,41]
# origin.extend(nums)
# print(sorted(origin))
# #for x in (20,40,41):
sorted_list = sorted(origin)

for x in (41,):
    for i, v in enumerate(sorted_list):
        if v > x:
            break
    sorted_list.insert(i, x)
print(sorted_list)
# 二分必须是排序的
origin = [37, 99, 73, 48, 40, 49, 25, 99, 51]
sorted_list = sorted(origin)
print(list(enumerate(sorted_list)))


def bi_insert_sort(origin, num):
    ret = origin[:]
    low = 0
    high = len(origin)

    while low < high:
        mid = (low + high) // 2

        if num < ret[mid]:
            high = mid
        else:
            low = mid + 1
    print(low)

for x in (20,40,41):
    print(x,bi_insert_sort(sorted_list,x))

import bisect
for x in (20,40,41,50,100):
    print(x,bisect.bisect(sorted_list,x))
# 二分前提是有序，否则不可以二分
#二分查找算法的时间复杂度O(log n)
def get_grade(score):
    breakpoints =[60,70,80,90]
    grades='EDCBA'

    index = bisect.bisect(breakpoints,score)
    print(index)
    print(grades[index])
    return grades[index]

def get_grade(*scores,breakpoints =[60,70,80,90], grades='EDCBA'):
    for score in scores:
        index = bisect.bisect(breakpoints,score)
        print(index)
        print(grades[index])
        print (grades[index])
get_grade(60,65,70,78)
