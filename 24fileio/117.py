import pickle
filename = 'file/117.txt'
# d = {'a':1, 'b':'abc','c': [1,2,3]}
# l = list('123')
# i = 99

x = 'a'
y = 100
z = ['abc']
m = [x,y,z]


with open(filename, 'wb') as f:
    # pickle.dump(d, f)
    # pickle.dump(l, f)
    # pickle.dump(i, f)
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(m, f)
    n = pickle.dumps(m)

with open(filename, 'rb') as f:
    for _ in range(3):
        a = pickle.load(f)

        # print(a,type(a))
    # list.append(pickle.dumps(m))
    b = pickle.loads(n)
    print(b, type(b))


x = [
    'a',
    100,
    ['abc'],
    {'a':x,'b':y,'c':z}
]
filename2 = 'file/117_2.txt'
lst = []
with open(filename2, 'wb') as f2:
    for i in x:
        lst.append(pickle.dumps(i))

with open(filename2,'rb') as f2:
    for i in lst:
        c = pickle.loads(i)
        print(c,type(c))