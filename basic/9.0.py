# a = int(input('please input a:'))
# b = int(input('please input b:'))
# c = int(input('please input c:'))
# if a < b:
#     if b < c:
#         print('c is the max number')
#     else:
#         print("b is the max number")
# else:
#     if a > c:
#         print('a is the max number')
#     else:
#         print('c is the max number')
# num = 5
# for i in range(num):
#     if i == 0 or i == num -1:
#         print('*' * num)
#     else:
#         print('*',' '*(num-2),'*')

a = 1
sum = 0
for i in range(1,6):
    a = i*a
    print(a)
    sum = sum +a
print(sum)

