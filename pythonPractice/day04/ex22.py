from socket import socket, AF_INET, SOCK_STREAM
import time


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []
    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock
    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()



from functools import partial
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s1, conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    print(resp)

    # conn.__enter__() executes: connection open
    s1.send(b'GET /index.html HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    resp = b''.join(iter(partial(s1.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    print(resp)

    time.sleep(5)
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    print(resp)
