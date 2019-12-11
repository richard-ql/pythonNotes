class Date:
    """
        关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增
    加新的属性。尽管使用 slots 可以达到这样的目的，但是这个并不是它的初衷。__slots__
    更多的是用来作为一个内存优化工具。
    """
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
