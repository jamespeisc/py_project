num = input('num is:')
numV = len(num)
print(numV)
num = int(num)
for i in range(numV):
    print(num % 10)
    num = num // 10

for i in range(5):
    if i > 2:
        break
    print(i)
else:
    print('ok')

num = 5
i = 0
while i < num:
    print('*')
    i += 1

#求100内所有奇数的和
count = 0
for i in range(0, 101):
    if not i % 2:
        continue
    count += i
print(count)

#判断学生成绩
score = int(input('score is:'))
if score > 100 or score < 0:
    print('wrong number')
elif score >= 90:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('E')

#1到5阶乘之和

count = 0

for i in range(5,0,-1):
    for j in range(i-1,0,-1):
        print(i,j)
        i *= j
    count +=i
print(count)

n = 5

for i in range(1,n+1):
    if i == 1 or i == n:
        print('* '*n)
    else:
        print('*',n*' ','*')

for i in range(1,10):
    for j in range(1,i):
        if i % j:
            print(i,j)

r = int(input('r='))
print('area='+str(3.14*r*r))
print('circumference='+str(2*3.14*r))
