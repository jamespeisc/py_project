
import re
s = '''bottle\nbag\nbig\napple'''
print (re.sub('b', 't', s, count =1))
print('*****************************')
print(s)
regex = re.compile('b\w+')
regex.sub('t', s, count =1)
print (re.subn('b\w', 't', s, count=1)) #subn 显示替换的次数， 同sub返回一个元组(new_string, number_of_subs_made)
s1 = "a  \t*(b"
print(re.split(' ', s1))
s2 = '''01 bottle
    02 bag
03   big1
100  able'''

print(re.findall('\s+', s2))
print (re.split('\s+', s2))
re.split('\s+\d+\s+', " " + s2)
matcher = re.match('b(\w)+', s)
matcher.groups()
matcher = re.match('(b)(\w)+', s)
matcher.groups()
matcher = re.match('(b)(\w)+\n(b\w+)', s)
matcher.groups()
matcher.group(1)
matcher.group(2)
matcher = re.match('b\w+\n(?P<g2>b\w+)', s)
matcher.group(1)
print(matcher.group('g2')) # 命名分组通过名称访问
type(matcher.groups())
matcher.groupdict()
#配置邮件
([a-zA-Z0-9-\.]+)@([\w-\.]+\.[\w-]+)
([a-zA-Z0-9-\.]+)@([\w\.]+)
#test@hot-mail.com
#v-ip@magedu.com
#web.manager@magedu.com.cn
#super.user@google.com
#a@w-a-com
#b01@v-ip.com


