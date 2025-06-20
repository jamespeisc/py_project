import re
from webob import Request, Response
from webob.dec import wsgify
from webob.exc import HTTPNotFound,HTTPForbidden


class AttrDict:
    def __init__(self, d: dict):
        self.__dict__.update(d if isinstance(d, dict) else {})

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __repr__(self):
        return '{}'.format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


class Router:
    TYPEPATTERNS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }
    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }
    _regex = re.compile(r'/{([^{}:]+)?([^{}:]*)}')

    def parse(self, src: str):
        start = 0
        res = ''
        types = {}
        for matcher in self._regex.finditer(src):
            print(matcher)
            res += src[start:matcher.start()]
            name = matcher.group(1)
            t = matcher.group(2)
            types[name] = self.TYPECAST.get(t, str)

            tmp = '/(?P<{}>{})'.format(name, self.TYPEPATTERNS.get(t, self.TYPEPATTERNS['str']))
            res += tmp

            start = matcher.end()
        else:
            res += src[start:]
        return res, types

    def __init__(self, prefix: str = ""):
        self.__prefix = prefix
        self.__routertable = []
        self.__pre_interceptor =[]
        self.__post_interceptor=[]

    def route(self, rule, *methods):
        def wrapper(handler):
            pattern, types = self.parse(rule)
            self.__routertable.append(
                (
                    tuple(map(lambda x: x.upper(), methods)),
                    re.compile(pattern), types,
                    handler
                )
            )
            return handler

        return wrapper

    def get(self, pattern):
        return self.route(pattern, "GET")

    def post(self, pattern):
        return self.route(pattern, "POST")

    def head(self, pattern):
        return self.route(pattern, "HEAD")

    def match(self, request:Request):
        path = request.path
        if path.startswith(self.__prefix):
            for fn in self.__pre_interceptor:
                request = fn(request)
                if request is None:
                    return None

            for methods,pattern,types,handler in self.__routertable:
                if request.method.upper() in methods or not methods:
                    matcher = pattern.match(path.replace(self.__prefix,'',1))
                    if matcher:
                        print(matcher.groupdict())
                        newdict= {}
                        for k,v in matcher.groupdict().items():
                            newdict[k] = types[k][v]
                        request.groupdict=AttrDict(newdict)
                        response = handler(request)
                        return response


class App:
    ROUTERS = []
    # 全局拦截器
    PRE_INTERCEPTOR = [] # 拦截器函数
    POST_INTERCEPTOR = []

    @classmethod
    def register(cls,*routers):
        for router in routers:
            cls.ROUTERS.append(router)

    @wsgify
    def __call__(self, request:Request):
        for fn in self.PRE_INTERCEPTOR:
            request=fn(request)
            if not request:
                raise HTTPForbidden('<h1>外星人拒绝你</h1>')
        for router in self.ROUTERS:
            response = router.match(request)
            for fn in self.POST_INTERCEPTOR:
                response = fn(request,response)

            if response:
                return response
        raise HTTPNotFound('<h1>该网页被外星人劫持了</h1>')


# ip 过滤

def ip_filter(request:Request): # 仅允许127
    prefix = '127.'
    return request if request.remote_addr.startswith(prefix) else None
