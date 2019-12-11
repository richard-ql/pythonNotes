class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise ValueError('expected a string')
        self._first_name = value

    def delete_first_name(self):
        raise AttributeError("can't delete attribute")

    name = property(get_first_name, set_first_name, delete_first_name)


