import inspect

def foo_bar(a:str, b:int, c:float=5.0) -> tuple:
    return a, b, c

print(foo_bar.__annotations__)
sig = inspect.signature(foo_bar)
print(sig)
print(sig.parameters)
print(sig.parameters['a'])
print(sig.return_annotation)

# Signature.bind 将具体参数绑定到对象Signature上,获得BoundArguments对象（保存了参数信息）
args = ('foobar', 10)
kwargs = {'c': 23.4}
bound = sig.bind(*args, **kwargs)
print(bound)
print(bound.arguments['a'])
print(bound.arguments['b'])
print(bound.arguments['c'])
# 综上，使用inspect可以将函数形参和实参封装为对象，对进一步操作具有意义。
