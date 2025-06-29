
import threading
import time


def worker():
    count = 0
    while True:
        if count > 5:
            break
        time.sleep(0.5)
        count += 1
        print(threading.current_thread().name,'------------------------------')

        #print(threading.current_thread().name, threading.current_thread().ident)
        print(threading.current_thread().name)


class MyThread(threading.Thread):
    def start(self):
        print('start~~~~~~~~')
        super().start()

    def run(self):
        print('run~~~~~~~~~~~~')
        super().run()


t1 = MyThread(name='work1',target=worker)
t2 = MyThread(name='work2',target=worker)

#t1.start()
#t2.start()

# 单cpu 同一时刻，仅有一个线程
# 一个进程中，至少有一个线程，并作为程序的入口，这个线程就是主线程，一个进程至少有一个主线程
# 线程安全
# 需要在
import threading
import logging

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMAT)

def worker():
    for x in range(100):
        #print("{} is running\n".format(threading.current_thread().name),end="")
        logging.info(1)

for i in range(1,5):
    name="worker{}".format(i)
    t = threading.Thread(name=name,target=worker)
    t.start()

# print函数线程不安全,线程执行一段代码，不会产生不确定的结果，那这段代码就是线程安全的
