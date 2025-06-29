import msgpack
import json

d = dict(zip('abcde',[None,True,False,[1,'abc'],{'a':1,'b':2}]))
s1 = json.dumps(d)
b1 = msgpack.dumps(d)
print(len(s1),type(s1))
print(s1)
print(len(b1),type(b1))
print(b1)

print(msgpack.unpackb(b1))