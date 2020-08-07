import threading
import time

#
# def get_detail_html(url):
#     print(str(threading.currentThread().name)+" get detail html started")
#     time.sleep(2)
#     print(str(threading.currentThread().name)+" get detail html ended")
#
# def get_detail_url(url):
#     print(str(threading.currentThread().name)+" get detail url started")
#     time.sleep(4)
#     print(str(threading.currentThread().name)+" get detail url ended")
#
# if __name__=="__main__":
#     th1 = threading.Thread(target=get_detail_html, args=("",))
#     th2 = threading.Thread(target=get_detail_url, args=("",))
#     # 设置守护线程，主线程退出后会杀死守护的子线程，如果不设置守护线程，子线程在主线程结束后会继续运行。
#     # th1.setDaemon(True)
#     th2.setDaemon(True)
#     th1.start()
#     th2.start()

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(str(threading.currentThread().name) + " get detail html started")
        time.sleep(2)
        print(str(threading.currentThread().name) + " get detail html ended")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(str(threading.currentThread().name) + " get detail url started")
        time.sleep(4)
        print(str(threading.currentThread().name) + " get detail url ended")


if __name__=="__main__":
    th1 = GetDetailHtml("1")
    th2 = GetDetailUrl("2")
    # 设置守护线程，主线程退出后会杀死守护的子线程，如果不设置守护线程，子线程在主线程结束后会继续运行。
    # th1.setDaemon(True)
    th2.setDaemon(True)
    th1.start()
    th2.start()