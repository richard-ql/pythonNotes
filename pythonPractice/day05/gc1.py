# 引用计数无法处理循环引用
import sys

class X:
    def __init__(self):
        self.other = None

a, b = X(), X()
print(sys.getrefcount(a), sys.getrefcount(b))
a.other = b; b.other = a
print(sys.getrefcount(a), sys.getrefcount(b))
del a, b
# print(sys.getrefcount(a), sys.getrefcount(b))
