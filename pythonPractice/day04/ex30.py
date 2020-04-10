"""
@contextmanager
这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创
建类去实现管理器协议了

在使用 @contextmanager 装饰的生成器中，yield 语句的作用是把函
数的定义体分成两部分：yield 语句前面的所有代码在 with 块开始时
（即解释器调用 __enter__ 方法时）执行， yield 语句后面的代码在
with 块结束时（即调用 __exit__ 方法时）执行
"""
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reversed_write(text):
        original_write(text[::-1])
    sys.stdout.write = reversed_write
    yield "Job"
    sys.stdout.write = original_write

with looking_glass() as what:
    print("Alice, Kitty and Snowdrop")
    print(what)

print('asdfasdf')

"""
以上示例有一个严重的错误：如果在 with 块中抛出了异常，Python 解
释器会将其捕获，然后在 looking_glass 函数的 yield 表达式里再次
抛出。但是，那里没有处理错误的代码，因此 looking_glass 函数会
中止，永远无法恢复成原来的 sys.stdout.write 方法，导致系统处
于无效状态
"""
