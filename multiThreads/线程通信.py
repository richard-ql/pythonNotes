import threading
import time

def go_event():
    e = threading.Event()
    def f():
        e.wait() # 线程阻塞，等待e.set()激活，继续执行。
        e.clear() # 重置e.wait()
        print(threading.current_thread().name)
    threading.Thread(target=f).start()
    return e

t = go_event()
time.sleep(5)
t.set()
