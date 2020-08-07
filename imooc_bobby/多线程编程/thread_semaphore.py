import time
import threading

class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html : " + self.url)
        self.sem.release() # sem.release 会让semaphore计数+1

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire() # sem.acquire会让sem计数-1
            html_thread = HtmlSpider(f"https://www.baidu.com/{str(i)}", self.sem)
            html_thread.start()

if __name__=="__main__":
    sem = threading.Semaphore(value=3)
    th1 = UrlProducer(sem)
    th1.start()