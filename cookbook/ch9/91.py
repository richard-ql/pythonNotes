import time
from functools import wraps


def time_this(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('time for exec %s is : %s' %(func.__name__,end-start))
        return result
    return wrappers

@time_this
def count_down(n : int):
    """
    Count down
    :param n: int
    :return: None
    """
    print('come in count_down')
    while n > 0:
        n -= 1

# count_down(300000)
# print(count_down.__doc__)
# print(count_down.__name__)
# print(count_down.__annotations__)
count_down.__wrapped__(100000)
from inspect import signature

print(signature(count_down))
