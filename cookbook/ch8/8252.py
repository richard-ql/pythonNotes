"""
    阻止用户去直接实例化这个Spam类
"""
import weakref

class CacheSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam3._new(name)
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp


class Spam3:
    manager = CacheSpamManager()
    def __init__(self, *args, **kw):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

    @classmethod
    def get_spam(cls, name):
        return cls.manager.get_spam(name)


a = Spam3.get_spam('foo')
b = Spam3.get_spam('foo')
print(a is b)
a = Spam3('foo')
