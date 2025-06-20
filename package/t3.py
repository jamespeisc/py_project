print(__name__)
import  t1
import  t2
import sys

print(111111111111111111, sys.modules.keys())
print(t1.A)
print(t2.x)
print('~~~~~~~~~~~~~')
t1.A().getmodule()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for x in sys.path: # 模块的搜索顺序
    print(x)

sys.path.append('o:/')
