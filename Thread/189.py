import threading
import logging
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMAT)

def worker():
    for x in range(100):
        time.sleep(0.5)
        #print("{} is running\n".format(threading.current_thread().name),end="")
        logging.info("{} is running".format(threading.current_thread().name))

def worker1():
    time.sleep(5)
    #print("{} is running\n".format(threading.current_thread().name),end="")
    logging.info("-----------{} is running".format(threading.current_thread().name))

for i in range(1,6):
    name="worker{}".format(i)
    if i < 5:
        threading.Thread(name=name,target=worker,daemon=True).start()
    if i == 5:
        threading.Thread(name=name,target=worker1,daemon=False).start()

print('=======fin========')

#daemon=None, 继承父线程
#daemon=False,主线程要等

# ts = []
# for i in range(1,6):
#     name='worker-{}'.format(i)
#     t=threading.Thread(target=worker,name=name,daemon=True)
#     ts.append(t)
#
# for t in ts:
#     time.sleep(1)
#     t.setDaemon(False)
#     t.start()