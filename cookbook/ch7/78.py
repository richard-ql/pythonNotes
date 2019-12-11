import math
from functools import partial


points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

pt = (4, 3)
"""
sorted() 方法接受一个关键字参数来自定义排序逻辑，但是它只能接受一个单个参
数的函数 (distance() 很明显是不符合条件的)。现在我们可以通过使用 partial() 来解
决这个问题：
"""
result = sorted(points, key=partial(distance, pt))
print(result)
