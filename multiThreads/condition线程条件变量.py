import threading
import time

def go1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.wait()
            cond.notify()

def go2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()

cond = threading.Condition()
threading.Thread(target=go1).start()
threading.Thread(target=go2).start()

