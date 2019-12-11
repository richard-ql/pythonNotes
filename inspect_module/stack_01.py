import inspect

def debug():
    caller_name = inspect.stack()
    print(str(caller_name))
    print(f'[debug] enter: {caller_name[0][3]}')

debug()