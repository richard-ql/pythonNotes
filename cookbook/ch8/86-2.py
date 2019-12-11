import math

class Circle:
    """
    在这里，我们通过使用 properties，将所有的访问接口形式统一起来，对半径、直
径、周长和面积的访问都是通过属性访问，就跟访问简单的 attribute 是一样的。如果
不这样做的话，那么就要在代码中混合使用简单属性访问和方法调用。
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

