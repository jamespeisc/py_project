import time
import datetime
from functools import wraps, update_wrapper


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("timeit {} took {}s".format(fn.__name__, delta))
        return ret

    return wrapper


@timeit  # add = timeit(add)
def add(x, y):
    time.sleep(1)
    return x + y


add(4, 5)


def timeit2(fn, output=lambda fn, delta: print("timeit {} took {}s".format(fn.__name__, delta))):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        output(fn, delta)
        return ret

    return wrapper


@timeit2  # add = timeit(add)
def add(x, y):
    time.sleep(1)
    return x + y


add(4, 5)
print('+++++++++++++++++++++++++++++++++++++')
class TimeIt:
    def __init__(self,fn,output = lambda fn, delta: print("timeit: {} took {}s".format(fn.__name__,delta))):
        self.fn = fn
        self.output = output
    def __enter__(self):
        self.start = datetime.datetime.now()
        return
    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        self.output(self.fn,delta)
    def __call__(self, *args, **kwargs):
        pass

with TimeIt(add):
    add(5,6)

from contextlib import contextmanager

@contextmanager
def a():
    print('~~~~~~~~~~enter')
    try:
        yield 500
    finally:
        print('~~~~~~~~~~exit')

with a() as f:
    print(f)
    print('mid')