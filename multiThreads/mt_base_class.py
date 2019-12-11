import threading
import time

mutex = threading.Lock()
num = 0
class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            for i in range(1000000):
                num += 1
        mutex.release()
        print(num)

my_thread = list()
for i in range(5):
    th = MyThread()
    th.start()
    my_thread.append(th)
for t in my_thread:
    t.join()
print("game over")
