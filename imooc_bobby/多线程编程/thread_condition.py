import threading

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            print(f"{self.name} : 在")
            self.cond.notify()
            self.cond.wait()

            print(f"{self.name} : 好的")
            self.cond.notify()
            self.cond.wait()

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫")
        self.cond = cond

    def run(self):
        with self.cond:
            print(f"{self.name} : 小爱同学")
            self.cond.wait()
            self.cond.notify()


            print(f"{self.name} : 我们来对古诗吧")
            self.cond.wait()
            self.cond.notify()


if __name__=="__main__":
    condition = threading.Condition()
    th1 = TianMao(condition)
    th2 = XiaoAi(condition)
    th1.start()
    th2.start()
