from functools import wraps
from inspect import signature

def param_info(func):
    sig = signature(func)
    for param in sig.parameters.values():
        print(param.name)
        print('--default', param.default)
        print('--kind', param.kind)

def sample(a, b, *args, c, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

print('<sample>')
print(param_info(sample))

def safe_param(func):
    ok_args = False
    ok_kwargs = False

    list_params = []
    keyword_params = set()

    sig = signature(func)
    for param in sig.parameters.values():
        if param.kind == param.VAR_POSITIONAL:
            ok_args = True
        elif param.kind == param.VAR_KEYWORD:
            ok_kwargs = True
        elif param.kind in [param.POSITIONAL_OR_KEYWORD]:
            list_params.append(param.name)
        elif param.kind in [param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY]:
            keyword_params.add(param.name)

    def get_default_value(param_name):
        original = sig.parameters[param_name]
        no_default = original.default is original.empty
        return None if no_default else original.default

    @wraps(func)
    def wrap(*args, **kwargs):
        if not ok_args:
            args = args[:len(list_params)]
        if not ok_kwargs:
            temp = {k: v for k, v in kwargs.items() if k in keyword_params}
            kwargs = temp
        if len(args) < len(list_params):
            not_set_list_params = list_params[len(args):]
            for param in not_set_list_params:
                if param in kwargs:
                    continue
                kwargs[param] = get_default_value(param)
        not_set_keyword_params = keyword_params - set(list_params) - set(kwargs.keys())
        for param in not_set_keyword_params:
            kwargs[param] = get_default_value(param)
        return func(*args, **kwargs)
    return wrap

safe_sample = safe_param(sample)
print('\n<safe_sample>')
param_info(safe_sample)

safe_sample(1,2,3,4,5,6,7, d=10)
sample(1,2,3,4,5,6,7, d=10)
