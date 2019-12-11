# 现实世界的命令行模式
from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()

class Recevier:
    def action(self):
        print("Recevier action")

class Invoker:
    def command(self, cmd):
        self.cmd =cmd

    def execute(self):
        self.cmd.execute()


if __name__=="__main__":
    recv = Recevier()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
