line = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" 
"Mozilla/5.0 (compatible; EasouSpider; +https://www.easou.com/search/spider.html)"'''


CHARS = set(" \t")


def makekey(line: str):
    start = 0
    skip = False
    for i, c in enumerate(line):
        if not skip and c in '"[':
            start = i + 1
            skip = True
        elif skip and c in '"]':
            skip = False
            yield line[start:i]
            start = i + 1
            continue
        if skip:
            continue
        if c in CHARS:
            if start == i:
                start = i + 1
                continue
            yield line[start:i]
            start = i + 1
    else:
        if start < len(line):
            yield line[start:]


print(list(makekey(line)))

datestr = '19/Feb/2013:10:23:29 +0800'
import datetime


def convert_date(datestr: str):
    return datetime.datetime.strptime(datestr, '%d/%b/%Y:%H:%M:%S %z')


convert_date = lambda datestr: datetime.datetime.strptime(datestr, '%d/%b/%Y:%H:%M:%S %z')

print(convert_date(datestr))


# print(dt, type(dt))

def getrequest(request: str):
    return request.split()  #返回列表list
get_request = lambda x: x.split()

names = ('remote','-','-','datatime','protocol','status','size','-','useragent')

ops = (None,None,None,convert_date,get_request,int,int,None,None)

for x in zip(names,ops,makekey(line)):  #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    print(x)


d = {name: data if op is None else op(data) for name,op,data in zip(names,ops,makekey(line))}

print(d)