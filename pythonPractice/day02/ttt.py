class HuantedBus:
    def __init__(self, passenger=[]):
        self.passenger = passenger

    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        self.passenger.remove(name)


bus1 = HuantedBus(['Alice', 'Bill'])
print(bus1.passenger)
bus1.pick('Charlie')
bus1.drop('Bill')
print(bus1.passenger)
bus2 = HuantedBus()
bus2.pick('Charlie')
print(bus2.passenger)
bus3 = HuantedBus()
print(bus3.passenger)
print(dir(HuantedBus.__init__))
print(HuantedBus.__init__.__defaults__)
print(HuantedBus.__init__.__defaults__[0] is bus2.passenger)
