# import logging
#
#
# a = logging.getLogger('foo')
# b = logging.getLogger('bar')
# print(a is b)
# c = logging.getLogger('foo')
# print(a is c)

import weakref

class Spam:
    def __init__(self, name):
        self.name = name

_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a1 = get_spam('foo')
a2 = get_spam('bar')
a3 = get_spam('foo')

print(a1 is a2)
print(a1 is a3)
