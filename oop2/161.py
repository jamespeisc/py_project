class Dispatcher:
    def __init__(self):
        pass

    def reg(self, name, fn):
        setattr(self, name, fn)

    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break
            getattr(self, cmd, lambda: print('Unknown Cmd{}'.format(cmd)))()


dis = Dispatcher()
dis.reg('ls', lambda: print('ls'))

#dis.run()


# 反射相关魔术方法

# __getattr__() __setattr__() __delattr__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        print(item, '~~~~~~~~~~~~')
        print(type(item))
        #setattr(self,item,123456)
        #print(self.z5,'++++++++++') # 循环报错
        return 123456
    def __setattr__(self, key, value): # 属性赋值的时候使用
        print('set attr')
        #setattr(self,key,value) # 循环报错
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('del {}'.format(item))


p = Point(4, 5)
print(p.x, p.y)
print(p.z1)
print(p.z2)
print(p.__dict__)
# 最终会查找 __getattr__内的设置
del p.z10 # 不会进入getattr 和 setattr
