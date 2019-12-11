# 信号量限制线程数量
import threading
import time

sem = threading.Semaphore(2) # 通过信号量限制线程最大数为2

def go_thread():
    for i in range(10):
        with sem:
            print(threading.current_thread().name, str(i) + '\n')
            time.sleep(1)

for i in range(5):
    threading.Thread(target=go_thread).start()
