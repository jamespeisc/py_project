import threading
from threading import Thread, Lock
import time
import datetime
import logging
from multiprocessing import Process, Pool

from concurrent import futures

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    logging.info('begin')
    time.sleep(5)
    logging.info('===end===')

executor = futures.ThreadPoolExecutor(max_workers=3)

fs = []

for i in range(3):
    future = executor.submit(worker)
    fs.append(future)

for i in range(3,6):
    future = executor.submit(worker)
    fs.append(future)

while True:
    time.sleep(2)
    logging.info(threading.enumerate())
    flag = True
    for f in fs:
        logging.info(f.done())
        flag = flag and f.done()

    print('-'*30)

    if flag:
        executor.shutdown()
        logging.info(threading.enumerate())
        break