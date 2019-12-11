import threading
import queue
import time
import random

class creatorThread(threading.Thread):
    def __init__(self, index, myqueue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = myqueue

    def run(self):
        while True:
            time.sleep(1.5)
            num = random.randint(0, 1000000)
            self.queue.put("input 生产者: " + str(self.index) + "肉夹馍" + str(num) )
            print("input 生产者: " + str(self.index) + "肉夹馍" + str(num) )

        self.queue.task_done()

class consumerThread(threading.Thread):
    def __init__(self, index, myqueue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = myqueue

    def run(self):
        while True:
            time.sleep(3)
            item = self.queue.get()
            if item is None:
                break
            print("消费者" + str(self.index) + ": 购买" + item )

        self.queue.task_done()

myqueue = queue.Queue(10) # 0代表无限容量，10代表最大容量
for i in range(3):
    creatorThread(i, myqueue=myqueue).start()

for i in range(8):
    consumerThread(i, myqueue=myqueue).start()
