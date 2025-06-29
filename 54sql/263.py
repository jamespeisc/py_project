import re

pattern = r'{{([^{}]*)}}'
regex = re.compile(pattern)

d = {
    'id': 5,
    'name': 'tom',
    'age': 20
}


def repl(matcher):
    print('----------------',matcher)
    return str(d.get(matcher.group(1),''))


with open('index.html', encoding='utf8') as f:
    for line in f:
        #print(line)
        ret = regex.sub(repl, line)
        print(ret)
