import logging
import threading
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class A:
    def __init__(self):
        self.x = 0


a = A()
global_data = threading.local()
global_data.x = 100


def worker(o):
    o.x = 1000  #使用内部x，不用上面全局x
    for _ in range(100):
        time.sleep(0.001)
        o.x += 1

    logging.info(o.x)


for i in range(5):
    threading.Thread(target=worker, args=(global_data,)).start()

while threading.active_count() > 1:
    time.sleep(1)

print(global_data.x)

# 堆里数据共享
# thread local 本质，thread.local 实例处于不同的线程中，就从大字典中找到当前线程相关键值对中的字典，覆盖threading.local实例中的__dict__,
# 这样就可以在不同的线程中，安全的使用线程独有的数据，做到了线程间数据隔离，如同本地变量一样安全
