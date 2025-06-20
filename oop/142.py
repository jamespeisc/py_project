class Student:

    def __init__(self,name,**kwargs):
        self._name = name
        self._scores = kwargs

    def get_score(self):
        return self._scores
    @property
    def name(self):
        return self._name

    def __del__(self):
        print('del')



tom = Student('tom',english=89,chinese=90,histroy=92)

print(tom.get_score())
# 猴子补丁

#实例的销毁

import time

tom = Student('tom')
jerry = Student('jerry')
tom1= tom

del tom #用这种，使引用计数减一，不能真正销毁，只是对象销毁的时候会自动调用它，不确定何时执行垃圾回收
print('~~~~~~~~')
time.sleep(3)
print(tom1.name)
del jerry
# 方法重载: 参数换类型
