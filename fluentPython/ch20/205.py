def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    name = '_{}#{}'.format('quantity', quantity.counter)

    def qt_get(instance):
        if instance is None:
            return quantity
        else:
            return getattr(instance, name)

    def qt_set(instance, value):
        if value > 0:
            return setattr(instance, name, value)
        else:
            return ValueError('value must be > 0')

    return property(qt_get, qt_set)


class LineItem:
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


coconuts = LineItem('Brazilian coconut', 20, 17.95)
print(coconuts.__dict__)
print(coconuts.weight, coconuts.price)
print(getattr(coconuts, '_quantity#0'), getattr(coconuts, '_quantity#1'))
print(LineItem.weight)
