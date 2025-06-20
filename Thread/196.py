import threading
from threading import Thread, Lock
import time
import datetime
import logging
from multiprocessing import Process, Pool

FORMAT = '%(asctime)-15s\t [%(processName)s, %(process)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(10000000):
        sum += 1


def callback(result):
    logging.info(result)


# # 线程部分
# ts = []
#
# t = threading.Thread(target=calc)
# ts.append(t)
# t.start()
#
# t = threading.Thread(target=calc)
# ts.append(t)
# t.start()
#
# t = threading.Thread(target=calc)
# ts.append(t)
# t.start()
#
# for t in ts:
#     t.join()
# delta = (datetime.datetime.now() - start).total_seconds()
# print(delta)
## 多进程
# ps = []
#
# if __name__ == '__main__':  # 要在这句下执行
#     for i in range(5):
#         p = Process(target=calc)
#         ps.append(p)
#         p.start()
#
#     for p in ps:
#         p.join()
#     delta = (datetime.datetime.now() - start).total_seconds()
#     print(delta)

if __name__ == '__main__':

    pool = Pool(5)

    for i in range(5):
        pool.apply_async(calc, callback=callback)

    pool.close()
    pool.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
