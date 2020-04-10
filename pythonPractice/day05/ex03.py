import gc
import sys

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
a = "abc"
b = "def"
print('a refcount:', sys.getrefcount(a))  # 2
print('b refcount:', sys.getrefcount(b))  # 3

# del a
# del b
# print(gc.collect())
