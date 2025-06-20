import threading
from threading import Thread, Lock, Barrier,Semaphore
import logging
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class Connection:
    def __init__(self, name):
        self.name = name


class Pool:
    def __init__(self, count: int):
        self.count = count
        self._value = count
        self.pool = [self._connect('{}'.format(i)) for i in range(count)]
        self.sema = Semaphore(count)

    def _connect(self, name):
        return Connection(name)

    def get_conn(self):
        self.sema.acquire()
        return self.pool.pop()

    def return_conn(self, conn: Connection):
        self.pool.attend(conn)
        self.sema.release()
