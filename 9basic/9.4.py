val = input('>>>')
val = int(val)
print(val)
if val >= 1000:
    if val >= 10000:
        num = 5
    else:
        num = 4
else:
    if val >= 100:
        num = 3
    elif val >= 10:
        num = 2
    else:
        num = 1
print(num)
c = val
for i in range(num):
    n = c // 10
    print(c - n*10)
    c = n