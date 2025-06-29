#第97节
cmds = {}

def reg(cmd):
    def _reg(fn):
        cmds[cmd] = fn
        return fn
    return _reg
@reg('mag')
def mag(): #mag = reg('mag')(mag)
    print('magedu')
@reg('py')
def py():
    print('python')
@reg('ls')
def ls():
    print('我是ls的结果')

print('-------------------------------------------')

import inspect
from collections import OrderedDict

def cache(fn):
    local_cache = {}
    def wrapper(*args, **kwargs):
        key=tuple()
        sig = inspect.signature(fn)
        params = sig.parameters
        keys = params.keys()
        values = params.values()
        params_dict = OrderedDict()
        #位置参数
        for i, val in enumerate(args):
            k = keys[i]
            params_dict[k] = val
        params_dict.update(kwargs)
        #关键字参数
        for k,v in sorted(kwargs.items()):
            params_dict[k] =v
        #缺省值
        for k,param in params.items():
            if k not in params_dict.keys():
                param_dict[k]= param.default
        return tuple(params_dict.items())



        # for item in sorted(kwargs.items()):
        #     key += item #(x,4,y,5,z,6)
        #查询和缓存
        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]
    return wrapper
@cache
def add(x,y,z):
    return x +y + z
add(4,5,z=6)
add(4,5,6)



reg('mag',mag)
reg('py',py)
reg('ls',ls)

def dispatcher():
    def default_func():
        print('未知命令')
    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            break
        cmds.get(cmd, default_func)()
print(cmds)
dispatcher()