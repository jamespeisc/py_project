# r = int(input('r='))
# print('area='+str(3.14*r*r))
# print('circumference='+str(2*3.14*r))

# max = 0
# count = 1
# while True:
#     num = int(input('Please input a number:'))
#     if num > max:
#         max=num
#     count+=1
#     if count >2:
#         choice = input('Continue?(Y/N):')
#         if choice == "N":
#             print(max)
#             break

# #求素数
#
# for i in range(2, 10000):
#     flag = False
#     for j in range(2,i):
#         if i % j ==0:
#             flag=True
#             break
#     if flag:
#         continue
#     else:
#         print(i,"is")

# 求质数,for-else 子句
# num = int(input('>>>'))
# for i in range(2, int(num**0.5+1)):
#     if num % i ==0:
#         print('这不是质数')
#         break
# else:
#     print('这是质数')

# 求平均值
# avvg = 0
# count = 0
# sum = 0
# while True:
#     a = int(input(">>>"))
#     count += 1
#     sum += a
#     avg = sum / count
#     if a == 0:
#         break
#     print(avg)

# 99乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,"\t", end="")
#     print("\n")

# print(help(print))

# print(1,2,sep='@')
# format函数打印
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(i,j,j*i),end='')
#     print()

# for i in range(1,10):
#     line=''
#     for j in range(1,i+1):
#         line+='{0}*{1}={2} '.format(j,i,i*j)  # 0. 1 为索引
#     print(line)

# print("{1} {1}    {1}".format(1,2,3))  什么都不写， 依次对应

# print('a={:<10}'.format(12)) #默认向右看齐:< 向左看齐

# line += '{0}*{1}={2:<2} '.format(j,i,i*j)
# c = 0
# for i in range(1,10):
#     s=""
#     for j in range(i,10):
#         if j <4:
#             s += "{}*{}={:<2} ".format(i,j,i*j)
#         else:
#             s += "{}*{}={:<3} ".format(i,j,i*j)
#     print("{:>72}".format(s))
#s += "{}*{}={:<{}} ".format(i, j, i*j, 2 if j < 4 else 3)
# 斐波那契数列
# f0 =1
# f1 =1
# print(f0)
# print(f1)
# for n in range(3,101):
#     fn = f1 +f0
#     print(fn)
#     f0 = f1
#     f1 = fn


# f0 =1
# f1 =1
# n = 2
# for i in range(3,102):
#     fn = f0+f1
#     f0 = f1
#     f1 = fn
#     n += 1
#     if i == 101:
#         print(n)
#         print(fn)


# print(2)
# for i in range(3, 100001, 2):
#     if i > 10 and i % 10 == 5:
#         continue
#     else:
#         for j in range(2, int(i ** 0.5 + 1)):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# import datetime
# start = datetime.datetime.now()
# delta = (datetime.datetime.now() - start).total_seconds()


# fn = 1
# for i in range(9,0,-1):
#     fn = 2*(fn + 1)
#     if i == 1:
#         print(fn)


# print('a={:<1}'.format(12))

for i in range(1,10):
    line=''
    for j in range(1,i+1):
        line += '{0}*{1}={2:<4}'.format(i,j,i*j)
    print(line)



