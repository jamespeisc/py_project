f = open('o:/test','r+')
print(f.read().encode())
f.seek(0)
for line in f:
    print(line)

f.close()