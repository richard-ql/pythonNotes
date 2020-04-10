"""
    修改全局作用域变量的方法
"""


def foo():
    global a
    a = 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)
