import threading
import time


def add(x, y):
    ret = x +y
    print(ret)
    return  ret

def add1(x,y):
    print(x+y)
    print(threading.current_thread().ident)
    print(threading.current_thread(),threading.main_thread())
    print(threading.active_count())


t0 = threading.Thread(target=add, args=None)

t = threading.Thread(target=add1, args=(4, 5))
t1 = threading.Thread(target=add1, args=(4,), kwargs={'y': 6})
t2 = threading.Thread(target=add1, kwargs={'y': 7, 'x': 4})


def worker():
    counter = 0
    while True:
        print('I am working.')
        # time.sleep(1)
        counter += 1
        if counter > 10:
            break


# t = threading.Thread(target=worker) # 创建主线程，内部的worker为子线程
#t.start()  # 启动
if __name__ == '__main__':
    print('=====fin=====')
    t.start()
    t1.start()
    t2.start()
# 主线程退出，进程退出。
