import threading


num = 0
# mutex = threading.Lock()
mutex = threading.RLock() # 避免单线程死锁

class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            num += 1
            print(self.name + str(num))

            if mutex.acquire(1):
                num += 1000
                print(self.name + str(num))
                mutex.release()

            mutex.release()

for i in range(5):
    t = MyThread()
    t.start()

