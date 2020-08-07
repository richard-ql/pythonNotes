"""
内部类对象

1 内部类对象的创建依赖于外部类对象；
2 内部类对象持有指向外部类对象的引用。
"""


class Outter:
    name = None

    def __init__(self, name):
        self.name = name

    def a(self):
        # innerObj = Outter.Inner(self)
        innerObj = self.Inner(self)
        innerObj.test()

    def b(self):
        pass

    class Inner:
        out = None

        def __init__(self, out=None):
            self.out = out

        def test(self):
            print(self.out.name)


if __name__ == "__main__":
    t = Outter("char")
    t.a()
