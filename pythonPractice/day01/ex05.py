"""
    修改嵌套作用域变量的方法
"""


def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        nonlocal b
        b = 'world'

    bar()
    print(b)


if __name__ == '__main__':
    a = 100
    foo()
