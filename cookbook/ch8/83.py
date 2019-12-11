from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        # self.socket = None
        self.connections = []

    def __enter__(self):
        # if self.socket is not None:
        #     raise RuntimeError('socket already connected!')

        _socket = socket(self.family, self.type)
        _socket.connect(self.address)
        self.connections.append(_socket)
        return _socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.socket.close()
        self.connections.pop().close()


from functools import partial


conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp.decode('utf-8'))
