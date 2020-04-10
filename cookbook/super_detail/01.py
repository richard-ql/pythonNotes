class A:
    def x(self):
        print('run A.x')
        super().x()
        print(self)


class B:
    def x(self):
        print('run B.x')
        print(self)


class C(A, B):
    def x(self):
        print('run C.x')
        super().x()
        print(self)

print(C.mro())
C().x()
