import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = []
stop = False
# 使用select完成http请求
class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf-8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80)) # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册到selector
        # register 3个参数 文件描述符，事件，回调函数
        selector.register(fileobj=self.client.fileno(), events=EVENT_WRITE, data=self.connected)

def loop():
    # 事件循环不停的请求socket的状态并调用对应的回调函数
    # select本身是不支持register模式的
    # socket状态变化后的回调函数是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            callback = key.data
            callback(key)
    # 回调+事件+select(poll/epoll)

if __name__ == "__main__":
    fetcher = Fetcher()
    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time()-start_time)
