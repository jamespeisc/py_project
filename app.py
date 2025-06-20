from wsgiref.simple_server import make_server
from webarch import App

if __name__ == '__main__':
    httpd = make_server('0.0.0.0',9000,App())
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.server_close()
