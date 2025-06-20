from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify
from webob.exc import HTTPNotFound
import logging
import re


# 127.0.0.1:9000?id=1&name=tom&age=20
class Router:
    ROUTERTABLE = {}

    @classmethod
    def register(cls, pattern):
        def wrapper(handler):
            cls.ROUTERTABLE.append((re.compile(pattern), handler))
            return handler

        return wrapper


@Router.register('/')  # indexhandler = Router.register('/')(indexhandler)
def indexhandler(request: Request):
    return '<h1>magedu.com Index.html</h1>'


@Router.register('/python')
def pythonhandler(request: Request):
    return '<h1>magedu.com Python.html</h1>'


# Router.register('/', indexhandler)
# Router.register('/python', pythonhandler)
def donothing(request):
    pass


class App:
    _Router = Router

    @wsgify
    def __call__(self, request: Request):
        path = request.path
        for pattern,handler in self._Router.ROUTERTABLE: #pattern是编译过的
            matcher = pattern.match(path)
            if matcher:
                response = handler(request)
                return response

        raise HTTPNotFound('<H1>该网页被外星人劫持了</h1>')


if __name__ == '__main__':

    httpd = make_server('0.0.0.0', 9000, App())
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.server_close()
