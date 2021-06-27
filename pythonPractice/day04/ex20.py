class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write # 猴子补丁 将sys.stdout.write方法替换为自定义方法
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])


    """
    如果一切正常，Python 调用 __exit__ 方法时传入的参数是 None,None, None；
    如果抛出了异常，这三个参数是异常数据，如下所述。
    
    exc_type:异常类（例如ZeroDivisionError）。
    exc_value:异常实例。有时会有参数传给异常构造方法，例如错误消息，这些参数可以使用
            exc_value.args获取。
    traceback:traceback对象。
    """
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

# import sys
# sys.stdout.write("hello")

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
#
print('asdfasdf')
"""
在 with 块之外使用 LookingGlass 类


>>> from mirror import LookingGlass
>>> manager = LookingGlass()
>>> manager
<mirror.LookingGlass object at 0x2a578ac>
>>> monster = manager.__enter__()
>>> monster == 'JABBERWOCKY'
eurT
>>> monster
'YKCOWREBBAJ'
>>> manager
>ca875a2x0 ta tcejbo ssalGgnikooL.rorrim<
>>> manager.__exit__(None, None, None)
>>> monster
'JABBERWOCKY
"""