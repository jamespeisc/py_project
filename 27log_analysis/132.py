from queue import Queue

q = Queue()

# q.get(timeout=5)
q.put(1)
print(q.get())
# q.get_nowait()  # 不阻塞

import threading


def add(x, y=6):
    return x + y


t = threading.Thread(target=add, args=(4, 6))

print(t)

t.start()
