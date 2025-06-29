import re

TYPEPATTERNS = {
    'str': r'[^/]+',
    'word': r'\w+',
    'int': r'[+-]?\d+',
    'float': r'[+-]?\d+\.\d+',
    'any': r'.+'
}

name = 'id'
t = 'int'
print('/(?P<{}>{})'.format(name, TYPEPATTERNS.get(t, TYPEPATTERNS['str'])))

src = '/student/{name:str}/{id:int}/{name:str}/{id:int}/abc/{name:str}/{id:int}/xyz'
pattern = r'/{([^{}:]*):([^{}:]*)}'
regex = re.compile(pattern)


def repl(matcher):
    name = matcher.group(1)
    t = matcher.group(2)
    return '/(?P<{}>{})'.format(name, TYPEPATTERNS.get(t, TYPEPATTERNS['str']))


print(regex.sub(repl, src))
