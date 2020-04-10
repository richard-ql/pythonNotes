"""
    下面是一个实现了代码块计时功能的上下文管理器例子
"""


import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))
# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1
