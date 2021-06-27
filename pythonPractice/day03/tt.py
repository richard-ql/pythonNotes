from functools import wraps


def singleton(cls):
    """装饰类的装饰器"""
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        print(instances)
        return instances[cls]

    return wrapper


@singleton
class President():
    """总统(单例类)"""
    pass

@singleton
class Student():
    pass


p1 = President()
p2 = President()
s1 = Student()
s2 = Student()
