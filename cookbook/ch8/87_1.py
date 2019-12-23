class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, item, value):
        if item.startswith('_'):
            super().__setattr__(item, value)
        else:
            setattr(self._obj, item, value)

