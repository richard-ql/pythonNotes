import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        predix = cls.__name__
        index = cls.__counter
        self.name = '_{}#{}'.format(predix, index)
        cls.__counter += 1

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.name)


class Validate(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractclassmethod
    def validate(self, instance, value):
        pass


class Quantity(Validate):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('Value must be > 0')
        return value


class NonBlank(Validate):
    def validate(self, instance, value):
        result = value.strip()
        if len(result)==0:
            raise ValueError("Description can't be blank or null")
        return result


class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def sub_total(self):
        return self.price * self.weight


coconuts = LineItem('Brazilian coconut', 20, 17.95)
print(coconuts.__dict__)
print(coconuts.weight, coconuts.price)
print(getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1'))
print(LineItem.weight, LineItem.description)
