import pickle


def show():
    print(123)


class AAA:
    aaaa = 'ABC'

    def __init__(self):
        self.tttt = 'abc'


a1 = AAA()
print(a1.tttt)

filename = 'file/117_3.txt'
with open(filename, 'wb') as f:
    b = pickle.dumps(a1)
    print(b)
with open(filename, 'rb') as f:
    b1 = pickle.loads(b)
    print(b1)
    # print(b1.tttt)
