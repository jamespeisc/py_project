from .web import Router,App
from webob import Request,Response
from .template import render

idx = Router()
@idx.route(r'^/$')

def indexhandler(request:Request):

    d = {
        'userlist' :[
            (1,'tom',20),
            (5,'jerry',23),
            (7,'sam',23)
        ]
    }
    return render('index.html',d)
py = Router('/python')

@py.get('r/{id:int}')

def pythonhandler(request:Request):
    print(request.groupdict)
    id = ''
    if request.groupdict:
        id = request.groupdict.id
# 返回json用下面的地址
    # d = {
    #     'userlist' :[
    #         (1,'tom',20),
    #         (5,'jerry',23),
    #         (7,'sam',23)
    #     ]
    # }
    # d['id'] = id
    # res = Response()
    # res.json =d
    # return res


    return '<h1><magedu.com Python/{}</h1>'.format(id)

App.register(idx,py)
