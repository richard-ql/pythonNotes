import threading
import time

# 为了合理利用资源，必须n个线程一起执行
bar = threading.Barrier(2) # 必须凑2个线程才可以执行

def sever():
    print(threading.current_thread().name, "start")
    time.sleep(5)
    bar.wait()
    print(threading.current_thread().name, "end")

for i in range(3):
    threading.Thread(target=sever).start()
