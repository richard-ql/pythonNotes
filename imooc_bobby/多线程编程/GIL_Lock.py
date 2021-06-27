# GIL 会根据执行的字节码行数以及时间片释放GIL
# GIL 遇到IO操作的时候主动释放GIL锁
import threading

num=10

def add():
    global num
    for i in range(1000000):
        num += 1

def minus():
    global num
    for i in range(1000000):
        num -= 1

th1 = threading.Thread(target=add)
th2 = threading.Thread(target=minus)

th1.start()
th2.start()
th1.join()
th2.join()
print(num)
