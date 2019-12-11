import sys

class ClosureInstance:
    def __init__(self, _locals=None):
        if _locals is None:
            _locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in _locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def stack():
    items = []
    def push(val):
        return items.append(val)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


from timeit import timeit

s = stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
s1 = Stack2()
print(timeit('s1.push(2);s1.pop()', 'from __main__ import s1'))

