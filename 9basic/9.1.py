#
# print('Please input a')
# a = int(input('-->'))
# print('Please input b')
# b = input('-->')
# b = int(b)
# if a > b:
#     print('a is bigger than b')
# else:
#     print('b is bigger than a')
# #
# print(max(a,b,100))

print('please input a num')

num = int(input('-->'))

if num // 10000 > 0:
    print('5位数')
elif num //1000 >0:
    print('4位数')
elif num //1000>0:
    print('3位数')
elif num //100 >0:
    print('2位数')
else:
    print('个位数')


flag = 10
while flag:
    print(flag)
    flag -= 1

# while True:
#     print(input())
#     break
