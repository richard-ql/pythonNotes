import inspect

def foo_bar(a:int, b:"it's b'", c:str=5) -> tuple:
    return a, b, c

print(foo_bar.__annotations__)
