import gc

import objgraph

gc.disable()


class A(object):
    pass


class B(object):
    pass


def a1():
    a = A()
    b = B()


a1()
print(objgraph.count('A'))
print(objgraph.count('B'))
