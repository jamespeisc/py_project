import re
pattern = r'{{([^{}]*)}}'
regex = re.compile(pattern)
TYPEPATTERNS = {

}
def repl(matcher):
    print(matcher)
    return str(d.get(matcher.group(1), ''))


def parse(line: str):
    start = 0
    res = ''

    for matcher in regex.finditer(line):
        res += line[start:matcher.start()]
        name = matcher.group(1)
        # t = matcher.group(2)
        tmp = '/(?P<{}>{})'.format(name, TYPEPATTERNS.get(t, TYPEPATTERNS['str']))
        res += tmp

        start = matcher.end()
    else:
        res += line[start:]
    return res


with open('index.html', encoding='utf8') as f:
    for line in f:
        # print(line)
        ret = regex.sub(repl, line)
        print(ret)

# html 表示数据的格式
# xml 解决数据问题，用文本的方式传输数据,描述数据，用json替代

# <students>
#     <student>
#         <id>5</id>
#         <name>tom</name>
#         <age>20</age>
#     </student>
# </students>

# 动态网页数据对服务器压力大，很难缓存