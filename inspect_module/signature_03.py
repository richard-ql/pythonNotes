# 使用inspect获取到参数对象后，结合函数注解属性annotations，可以写一个很优雅的强制类型检查装饰器。
from functools import wraps
from inspect import signature


def check1(func):
    ann = func.__annotations__
    sig = signature(func)
    @wraps(func)
    def wrap(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            if k in ann:
                assert isinstance(v, ann[k]), f'param {k} Type Error: expected type {ann[k]}'
        return func(*args, **kwargs)
    return wrap

def check2(func):
    sig = signature(func)
    param_d = sig.parameters
    print(param_d)
    @wraps(func)
    def wrap(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            if k in param_d:
                print(v, param_d[k].annotation)
                assert isinstance(v, param_d[k].annotation), f'parm {k} Type Error: expected {param_d[k].annotation}'
        return func(*args, **kwargs)
    return wrap



# @check1
@check2
def add(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

add(2, 3)
