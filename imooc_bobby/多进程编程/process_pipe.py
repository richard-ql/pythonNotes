import time
from multiprocessing import Process, Pipe

def producer(pipe):
    pipe.send(2)
    time.sleep(2)

def consumer(pipe):
    print(pipe.recv())


if __name__=="__main__":
    # Pipe 只适用于2个进程间的通信，性能优于multprocess.Queue()
    recevie_pipe, send_pipe = Pipe()
    p_producer = Process(target=producer, args=(send_pipe,))
    p_consumer = Process(target=consumer, args=(recevie_pipe,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()