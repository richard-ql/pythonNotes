class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('Expected a string')
        self._name = val

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPersona(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
print(s.name)
s1 = SubPersona('ql')
print(s1.name)
