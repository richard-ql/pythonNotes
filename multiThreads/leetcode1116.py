import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sema_z = threading.Semaphore(1)
        self.sema_e = threading.Semaphore(0)
        self.sema_o = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self) -> None:
        for i in range(1, self.n+1):
            self.sema_z.acquire()
            print(0)
            if i % 2 == 1:
                self.sema_o.release()
            else:
                self.sema_e.release()

    def even(self) -> None:
        for i in range(2, self.n+1, 2):
            self.sema_e.acquire()
            print(i)
            self.sema_z.release()

    def odd(self) -> None:
        for i in range(1, self.n+1, 2):
            self.sema_o.acquire()
            print(i)
            self.sema_z.release()

if __name__=="__main__":
    fb = ZeroEvenOdd(16)
    th1 = threading.Thread(target=fb.zero)
    th2 = threading.Thread(target=fb.even)
    th3 = threading.Thread(target=fb.odd)
    th1.start()
    th2.start()
    th3.start()
