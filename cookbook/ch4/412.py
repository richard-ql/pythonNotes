from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for i in chain(a, b):
    print(i)
