from contextlib import contextmanager

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

"""
>>> items = [1, 2, 3]
>>> with list_transaction(items) as working:
... working.append(4)
... working.append(5)
...
>>> items
[1, 2, 3, 4, 5]
>>> with list_transaction(items) as working:
... working.append(6)
... working.append(7)
... raise RuntimeError('oops')
>>> items[1 2 3 4 5]
"""
