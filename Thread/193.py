import logging
import threading
import time
from threading import Lock
from threading import Thread

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

# cups = []
# lock = Lock()
#
#
# def worker(count=10):
#     logging.info("I am working for you")
#     flag = False
#     while True:
#         lock.acquire()
#         # lock.acquire(timeout=2) 设置超时，没有拿到锁
#         # lock.acquire(blocking=false) 非阻塞
#
#         if len(cups) >= count:
#             flag = True
#             break
#         time.sleep(0.001)
#         if not flag:
#             cups.append(1)
#         # print(threading.current_thread())
#         lock.release()
#         if flag:
#             break
#
#     logging.info("I finished. cups = {}".format(len(cups)))
#
#
# for _ in range(10):
#     t = threading.Thread(target=worker, args=(1000,))
#     t.start()
#     # t.join()


# 支持上下文


class Counter:
    def __init__(self):
        self._val = 0
        self.lock = Lock()

    @property
    def value(self):
        with self.lock:
            return self._val

    def inc(self):
        self.lock.acquire()
        try:
            self._val += 1
        finally:
            self.lock.release()

    def dec(self):
        with self.lock:
            self._val -= 1


def run(c: Counter, count=100):
    for _ in range(count):
        for i in range(-50, 50):
            if i < 0:
                c.dec()
            else:
                c.inc()


c = Counter()
c1 = 10
c2 = 1000

for i in range(c1):
    Thread(target=run, args=(c, c2)).start()
while threading.active_count() > 1:
    threading.Event().wait(1)
print(c.value)


def worker(tasks):
    for task in tasks:
        time.sleep(0.001)
    if task.lock.acquire(False):
        logging.info('{} {} begin to start'.format(threading.current_thread(),task.name))
    else:
        logging.info('{} {} is working'.format(threading.current_thread(), task.name))


class Task:
    def __init__(self,name):
        self.name= name
        self.lock = threading.lock()

tasks = [Task('task-{}'.format(x)) for x in range(10)]

for i in range(5):
    threading.Thread(target=worker,name='worker-{}'.format(i),args=(tasks,)).start()

# 可重用锁
l = threading.RLock()
l.acquire()
l.acquire()

def worker(l):
    logging.info('in thread start')
    with l:
        l.acquire()
    time.sleep(5)
    logging.info('in thread')

t = threading.Thread(target=worker,args=(l,))
t.start()

threading.Event().wait(2)
logging.info('--------------')
l.acquire()
logging.info('in main')

#threading.current_thread().ident 打印线程id

#Condition 构造方法，可以传入一个Lock或Rlock对象，默认是Rlock





