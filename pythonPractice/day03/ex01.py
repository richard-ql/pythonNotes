"""
    生成器
"""
import sys


li = [x ** 2 for x in range(1, 1000)]
print(li)
print(sys.getsizeof(li))

g = (x ** 2 for x in range(1, 1000))
print(g)
print(sys.getsizeof(g))

# 使用next() 和 for 迭代生成器

# while True:
#     print(next(g))

for i in g:
    print(i)
