def count(n):
    while True:
        yield n
        n += 1

"""
>>> c = count(0)
>>> c[10:20]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
>>> from itertools import islice
>>> for x in islice(c, 10, 20):
...     print(x)
...
10
11
12
13
14
15
16
17
18
19
"""

