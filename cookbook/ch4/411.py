xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 100, 101]

for x, y in zip(xpts, ypts):
    print(x, y)

for i in zip(xpts, ypts):
    print(i)

from itertools import zip_longest

for x, y in zip_longest(xpts, ypts, fillvalue=0):
    print(x, y)
