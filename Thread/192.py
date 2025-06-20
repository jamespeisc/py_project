# 线程同步，线程间协同，通过某种技术，让一个线程访问某些数据时，其他线程不能访问这些数据，直到该线程完成对数据的操作
# 不同操作系统实现的技术有所不同，有临界区，互斥量，信号量，事件等
# event 通过内部标记flag的True或False的变化来操作
import logging
import threading
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

# def worker(count=10):
#     cups = []
#     while len(cups) < count:
#         time.sleep(0.5)
#         cups.append(1)
#         logging.info(cups)
#     logging.info("I finished my job. {}".format(cups))
#
# def boss():
#
#     t = threading.Thread(target=worker)
#     t.start()
#     t.join()
#     logging.info('God job')
#
# b = threading.Thread(target=boss)
# b.start()
# b.join()
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




event = threading.Event()

def worker(count=10):
    cups = []
    while len(cups) < count:
        time.sleep(0.1)
        cups.append(1)
        logging.info(cups)
    logging.info("I finished my job. {}".format(cups))
    event.set()

def boss():
    logging.info("I am boss, I am waiting for you")
    #event.wait()
    logging.info(event.wait())
    logging.info("Good Job")

t = threading.Thread(target=worker,args=(10,))
t.start()
b= threading.Thread(target=boss,name='boss')
b.start()

print('~~~~~~~~~~~~~~~~~')

# wait 的 使用

from threading import Event, Thread

import logging

logging.basicConfig(level=logging.INFO)

def do(event:Event,interval:int):
    while not event.wait(interval):
        logging.info('do sth')

e =Event()

Thread(target=do,args=(e,3)).start()

e.wait(10)
# 可以有多个wait，event 优于sleep

class Timer:
    def __init__(self,interval,function,args=None,kwargs=None,name=None,*,daemon=None):
        self.interval= interval
        self.target = function
        self.args = args
        self.kwargs = kwargs
        self.name = name
        self.daemon = daemon
        self.event = threading.Event()
        self.thread= None
    def start(self):
        self.event.wait(self.interval)
        self.thread= threading.Thread(target=self.target,args=self.args,kwargs=self.kwargs,name=self.name,daemon=self.daemon)
        self.run()

    def canal(self):
        self.event.set()
    def run(self):
        self.thread.start()
