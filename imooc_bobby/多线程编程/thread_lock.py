import threading
from threading import Lock, RLock

# RLock 可重入锁，可以lock.acquire() 多次 不会造成死锁，但是要有对应次数的lock.release()

num=10
lock = RLock() # 换成Lock()会造成死锁

def add():
    global num
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        num += 1
        lock.release()
        lock.release()

def minus():
    global num
    for i in range(1000000):
        lock.acquire()
        num -= 1
        lock.release()

th1 = threading.Thread(target=add)
th2 = threading.Thread(target=minus)

th1.start()
th2.start()
th1.join()
th2.join()
print(num)