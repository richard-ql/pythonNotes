import os
import time
import threading

def go():
    os.system("notepad")

time_thread = threading.Timer(5, go) # 5秒后执行一次go函数
time_thread.start()
i = 0
while True:
    time.sleep(1)
    print("第" + str(i) + "秒")
    i += 1
