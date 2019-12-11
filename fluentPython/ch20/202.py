class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            return setattr(instance, self.name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# coconuts = LineItem('Brazilian coconut', 20, 17.95)
# print(coconuts.__dict__)
# print(coconuts.weight, coconuts.price)
# print(getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1'))
print(LineItem.weight)
