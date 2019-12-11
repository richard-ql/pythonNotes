import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_spam(cls, name):
        return cls.manager.get_spam(name)


a = Spam.get_spam('foo')
b = Spam.get_spam('foo')
print(a is b)
