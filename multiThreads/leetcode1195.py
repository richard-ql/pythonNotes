import threading

# class FizzBuzz:
#     def __init__(self, n: int):
#         self.n = n
#         self.start = 1
#         self.cond = threading.Condition()
#
#     # printFizz() outputs "fizz"
#     def fizz(self) -> None:
#         while self.start <= self.n:
#             with self.cond:
#                 self.cond.wait_for(lambda: self.start > self.n or (self.start % 3 == 0 and self.start % 5 !=0))
#                 if self.start <= self.n:
#                     print('Fizz'+str(self.start))
#                     self.start += 1
#                     self.cond.notify_all()
#
#
#     # printBuzz() outputs "buzz"
#     def buzz(self) -> None:
#         while self.start <= self.n:
#             with self.cond:
#                 self.cond.wait_for(lambda: self.start > self.n or (self.start % 5 == 0 and self.start % 3 !=0))
#                 if self.start <= self.n:
#                     print('Buzz'+str(self.start))
#                     self.start += 1
#                     self.cond.notify_all()
#
#     # printFizzBuzz() outputs "fizzbuzz"
#     def fizzbuzz(self,) -> None:
#         while self.start <= self.n:
#             with self.cond:
#                 self.cond.wait_for(lambda: self.start > self.n or self.start % 3 ==0 and self.start % 5 == 0)
#                 if self.start <= self.n:
#                     print('FizzBuzz'+str(self.start))
#                     self.start += 1
#                     self.cond.notify_all()
#
#     # printNumber(x) outputs "x", where x is an integer.
#     def number(self) -> None:
#         while self.start <= self.n:
#             with self.cond:
#                 print(str(self.start))
#                 self.start += 1
#                 self.cond.notify_all()
#                 self.cond.wait_for(lambda: self.start > self.n or self.start % 3 != 0 and self.start % 5 !=0)

# class FizzBuzz:
#     def __init__(self, n: int):
#         self.n = n+1
#         self.sema_fizz = threading.Semaphore(0)
#         self.sema_buzz = threading.Semaphore(0)
#         self.sema_fb = threading.Semaphore(0)
#         self.sema_num = threading.Semaphore(1)
#
#     # printFizz() outputs "fizz"
#     def fizz(self) -> None:
#         for i in range(1, self.n):
#             if i % 3 == 0 and i % 5 !=0:
#                 self.sema_fizz.acquire()
#                 print('Fizz'+str(i))
#                 self.sema_num.release()
#
#
#     # printBuzz() outputs "buzz"
#     def buzz(self) -> None:
#         for i in range(1, self.n):
#             if i % 3 != 0 and i % 5 ==0:
#                 self.sema_buzz.acquire()
#                 print('buzz'+str(i))
#                 self.sema_num.release()
#
#     # printFizzBuzz() outputs "fizzbuzz"
#     def fizzbuzz(self,) -> None:
#         for i in range(1, self.n):
#             if i % 3 == 0 and i % 5 ==0:
#                 self.sema_fb.acquire()
#                 print('fizzbuzz'+str(i))
#                 self.sema_num.release()
#
#     # printNumber(x) outputs "x", where x is an integer.
#     def number(self) -> None:
#         for i in range(1, self.n):
#             self.sema_num.acquire()
#             if i % 3 == 0 and i % 5 !=0:
#                 self.sema_fizz.release()
#             elif i % 3 != 0 and i % 5 ==0:
#                 self.sema_buzz.release()
#             elif i % 3 == 0 and i % 5 ==0:
#                 self.sema_fb.release()
#             else:
#                 print(str(i))
#                 self.sema_num.release()

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n+1
        self.sema_fizz = threading.Event()
        self.sema_buzz = threading.Event()
        self.sema_fb = threading.Event()
        self.sema_num = threading.Event()
        self.sema_num.set()

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 !=0:
                self.sema_fizz.wait()
                print('Fizz'+str(i))
                self.sema_fizz.clear()
                self.sema_num.set()


    # printBuzz() outputs "buzz"
    def buzz(self) -> None:
        for i in range(1, self.n):
            if i % 3 != 0 and i % 5 ==0:
                self.sema_buzz.wait()
                print('buzz'+str(i))
                self.sema_buzz.clear()
                self.sema_num.set()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self,) -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 ==0:
                self.sema_fb.wait()
                print('fizzbuzz'+str(i))
                self.sema_fb.clear()
                self.sema_num.set()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self) -> None:
        for i in range(1, self.n):
            self.sema_num.wait()
            self.sema_num.clear()
            if i % 3 == 0 and i % 5 !=0:
                self.sema_fizz.set()
            elif i % 3 != 0 and i % 5 ==0:
                self.sema_buzz.set()
            elif i % 3 == 0 and i % 5 ==0:
                self.sema_fb.set()
            else:
                print(str(i))
                self.sema_num.set()

if __name__=="__main__":
    fb = FizzBuzz(15)
    th1 = threading.Thread(target=fb.fizz)
    th2 = threading.Thread(target=fb.buzz)
    th3 = threading.Thread(target=fb.fizzbuzz)
    th4 = threading.Thread(target=fb.number)
    th1.start()
    th2.start()
    th3.start()
    th4.start()
