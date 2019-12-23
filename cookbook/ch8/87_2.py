class A:
    def spam(self):
        print('A.spam')
        super().spam()


class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass


c = C()
print(c.spam())
