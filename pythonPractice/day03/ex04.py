"""
    闭包
"""


def count():
    def f(j):
        return j ** 2
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)

