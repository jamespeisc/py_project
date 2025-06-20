import json
d = dict(zip('abcde',[None,True,False,[1,'abc'],{'a':1,'b':2}]))
print(json.dumps(d))

s = json.dumps(d)
print(s,type(s))

s1 = """{"a": null, "b": true, "c": false, "d": [1, "abc"], "e": {"a": 1, "b": 2}}"""
d1 = json.loads(s1)
print(d1)
print('#############')
filename = 'file/118_1.txt'

with open(filename,'r+') as f:
    d2 = json.load(f)
    print(d2)