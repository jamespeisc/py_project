import os.path
import pathlib
import sys
import re
# 系统向前写，自己的模块向后写
import os.path as osp
print(dir()) # 收集当前模块所有属性信息
print(__file__)
print(__name__) # 输出 __main__， 一个.py文件对应一个名称

print(osp)

# import 后放模块
# from 从模块中导入资源
from os import path # 模块
from pathlib import Path # 类
from functools import wraps # 函数
# import 找到指定的模块，加载和初始化它，生成模块对象，找不到抛出importError异常

from os.path import join as j, exists as ex,split
from pathlib import * # 导入不带下划线的成员
# from os.path import exists

print(os.path.exists)
print(getattr(os.path,'exists'))

# 自定义模块，.py文件就是一个模块

class A :
    def getmodule(self):
        print(self.__module__.__name__)
a = A()

print(11111,a)

print(dir())

# 自定义模块名规范 1，模块名就是文件名，非数字开头的字母数字和下划线的组合，不要使用系统模块名，模块名通常全小写

print(__name__)
import  t1
import  t2
print(t1.A)
print(t2.x)
print('~~~~~~~~~~~~~')
t1.A().getmodule()