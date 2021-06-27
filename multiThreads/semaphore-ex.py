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


# Semaphore(0)
# 当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。也就是说参数为0，即表示调用了 acquire()。
#
# Semaphore(1)
# 当参数为 1 时，表示在 release() 状态。
#
#
#
# 同样的逻辑，使用 Lock 的速度是 32ms, 使用 Semaphore 的速度是 56 ms。因此，能使用 Lock 的时候就尽量使用 Lock。
#
# Semaphore(2)
# 当共享资源数量设置为 2 时，可以接受连续两次 acquire , 同时设定一个开关，这样就可以控制配对的输出。