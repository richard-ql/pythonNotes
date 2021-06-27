import gc


class X:
    def __init__(self):
        self.other = None

    def __del__(self):
        print('DEL!', self)


a, b = X(), X()
a.other = b; b.other = a
del a, b
gc.collect(); gc.collect()
print(gc.garbage)
