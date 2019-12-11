def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x+y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', ' world'), callback=print_result)

# 回调函数访问外部变量 使用类实现
class RequestHandler:
    def __init__(self):
        self.sequence = 0

    def handle(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = RequestHandler()
apply_async(add, (2, 3), callback=r.handle)
apply_async(add, ('hello', ' world'), callback=r.handle)

# 回调函数访问外部变量 使用闭包实现

def request_handler(sequence=0):
    def handle(*args):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, args))
    return handle

r = request_handler()
apply_async(add, (4, 5), callback=r)
apply_async(add, ('ni', ' hao'), callback=r)

# 回调函数访问外部变量,使用协程实现

def make_handler(sequence=0):
    while True:
        sequence += 1
        result = yield
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
handler.send(None)
apply_async(add, (7, 8), callback=handler.send)
apply_async(add, ('fei', 'chang'), callback=handler.send)
