source = {'a': {'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}

def flatmap(source,prefix=''):
    for k,v in source.items():
        if isinstance(v, (list,tuple,set,dict)):
            flatmap(v, prefix=prefix+k+'.')
        else:
            target[prefix+k] =v
flatmap(source)

print(target)

#base64 算法实现
#大端，小端
##公共子串

s1 = 'abcdefg'
s2 = 'defabcdoabcdeftw'
s3 = '1234a'
def findit(str1,str2):
    count = 0
    length = len(str1)

    for sublen in range(length,0,-1):
        for start in range(0,length - sublen +1):
            substr = str1[start:start +sublen]
            count += 1
            if str2.find(substr) > -1: #找到了
                print("count={},substrlen={}".format(count,sublen))
                return substr

print(findit(s1,s2))
print(findit(s1,s3))