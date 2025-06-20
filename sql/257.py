from wsgiref.simple_server import make_server
import urllib.parse
from webob import Request, Response
# 127.0.0.1:9000?id=1&name=tom&age=20

def simple_app(environ, start_response):
    query_string = environ.get('QUERY_STRING')
    # print(query_string)
    # d = {}
    # for item in query_string.split('&'):
    #     k, _, v = item.partition('=')
    #     d[k] = v
    # d = {k: v for k, _, v in map(lambda x: x.partition('='), query_string.split('&'))}
    # print(d)
    qs = urllib.parse.parse_qs(query_string)
    print(qs)
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)
    ret = [query_string.encode()]
    request = Request(environ)
    qs = request.query_string
    mtd = request.method
    print(qs,mtd)
    print(request.GET)
    print(request.path)
    print(request.params)
    return ret


httpd = make_server('0.0.0.0', 9000, simple_app)
try:
    httpd.serve_forever()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print('stop')
    httpd.server_close()



from webob.multidict import MultiDict

md = MultiDict()
md.add('a',1)
md.add('b',2)
md.add('b',3)
md.add('1',100)
print(md) # 返回MultiDict([('a',1),('b',2),('b',3)])
print(md.get('c',20000))
