from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item

its = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(its):
    print(x)
