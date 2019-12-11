class Person:
    def __init__(self, first_name):
        """
        你可能还会问为什么 __init__() 方法中设置了 self.first_name
        而不是 self._first_name 。在这个例子中，我们创建一个 property 的目的就是在设置
        attribute 的时候进行检查。因此，你可能想在初始化的时候也进行这种类型检查。通
        过设置 self.first_name ，自动调用 setter 方法，这个方法里面会进行参数的检查，
        否则就是直接访问 self._first_name 了
        :param first_name:
        """
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError('Expected a string object')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("can't delete attribute")