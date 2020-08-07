import time

from multiprocessing import Process, Queue, Manager

def producer(queue):
    queue.put(2)
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(f"{data}")

if __name__=="__main__":
    # queue = Queue(maxsize=10)
    # p_producer = Process(target=producer, args=(queue,))
    # p_consumer = Process(target=consumer, args=(queue,))
    # p_producer.start()
    # p_consumer.start()
    # p_producer.join()
    # p_consumer.join()

    # multiprocess.Queue()不能用于pool进程池通信
    # pool进程池的通信要使用Manager().Queue()
    queue = Manager().Queue(maxsize=10)
    p_producer = Process(target=producer, args=(queue,))
    p_consumer = Process(target=consumer, args=(queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()