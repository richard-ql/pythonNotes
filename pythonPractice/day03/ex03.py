"""
    闭包
"""


def count():
    fs = []
    for i in range(1, 3):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2 = count()
print(f1())
# print(f2())
