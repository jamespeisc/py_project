import importlib

def plugin(name:str,sep='.'):
    m,_,c = name.partition(sep)
    mode_name = 't2'
    #mod = __import__(mode_name)
    mod = importlib.import_module(m) # 推荐
    print(mod)
    cls = getattr(mod,c)
    a = cls()
    a.show()
    return cls
    # print(locals()) # 当前作用域信息
    # print(globals()) # 边界为模块
if __name__ == "__main__":
    cls=plugin('t2.A')
    print(cls().show())

# 运行时，根据用户需求，找到的模块资源动态加载起来

