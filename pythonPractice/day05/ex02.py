import sys
import gc

gc.disable()
d = []
c = d
print(sys.getrefcount(d))
