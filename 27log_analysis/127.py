import re

s = '''bottle\nbag\nbig\napple'''
for i,c in enumerate(s,1):
    print((i-1, c), end='\n' if i%8 ==0 else ' ')
print()
print(re.match('b',s))
regex = re.compile('bo')
print(regex.match(s)) #从开头匹配
regex = re.compile('bag')
print(regex.match(s))
print(regex.match(s, 8))
print(regex.match(s, 8, 11)) #<re.Match object; span=(8, 11), match='bag'>
print(regex.match(s, 8, 10)) #返回none
print(re.search('c', s))
regex = re.compile('a')
print(regex.search(s,9,16))

##总结re.match 必须从头开始匹配,re.search 不用从头开始匹配，依然返回match对象

print(re.fullmatch('b.*',s,re.S)) #single line,可以全匹配

#re.fullmatch(('bag', s, re.M)) #不能匹配
print('_________________')
regex = re.compile('bag')
print(regex.fullmatch(s, 8, 11)) #可以匹配

print(re.findall('b\w', s)) #返回['bo', 'ba', 'bi']

print(re.finditer('b\w',s)) #返回<callable_iterator object at 0x000001ECC4D84308>

for x in re.finditer('b\w', s):
    print(x)


print('\a')
