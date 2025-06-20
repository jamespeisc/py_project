from wsgiref.simple_server import make_server
import urllib.parse
from webob import Request, Response
from webob.dec import wsgify


# 127.0.0.1:9000?id=1&name=tom&age=20

def simple_app(environ, start_response):
    request = Request(environ)
    method = request.method
    print(request.GET)
    print(request.POST)
    print(request.path)
    print(request.params)

    res = Response()
    print(res.status_code)
    res.body = '<h1>magedu</h1>'.encode()
    return res(environ, start_response)



# 用了装饰器后，即可用下面的
@wsgify
def app(request: Request) -> Response:
    return Response(b'<h1>magedu.com</h1>')

class App:
    def __init__(self):
        pass
    @wsgify
    def __call__(self,request:Request):
        return Response(b'<h1>magedu.com</h1>')

if __name__ == '__main__':

    #httpd = make_server('0.0.0.0', 9000, app)
    httpd = make_server('0.0.0.0', 9000, App())
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.server_close()
