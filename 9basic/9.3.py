num = 12345
if num // 10000 > 0:
    print('5位数')
    print ('万位数为', num //10000)
    print('千位数为', (num - num // 10000 * 10000) // 1000)
    print('百位数为', (num - num // 1000 * 1000) // 100 )
    print('十位数为', (num - num // 100 * 100) // 10)
    print('个位数为', num % 10)
elif num // 1000 > 0:
    print('4位数')
    print('千位数为', num // 1000)
    print('百位数为',(num - num // 1000 * 1000) // 100)
    print('十位数为', (num - num // 100 * 100) // 10)
    print('个位数为', num - num // 10 * 10)
elif num // 100 > 0:
    print('3位数')
    print('百位数为', num // 100)
    print('十位数为', (num - num // 100 * 100) //10)
    print('个位数为', num - num // 10 * 10)
elif num // 10 > 0:
    print('2位数')
    print('十位数为', num // 10)
    print('个位数为', num - num // 10 * 10)
else:
    print('个位数')
    print(num)


val = input('>>>')
val = int(val)
print(val)
if val >= 1000:
    if val >=10000:
        num = 5
    else:
        num = 4
else:
    if val >=100:
        num = 3
    elif val >=10:
        num = 2
    else:
        num = 1
    print(num)
    c = val
    for i in range(num):
        n = c //10
        print(c - n*10)
        c = n


