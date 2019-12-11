# 模板方法模式
from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compilerToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compilerAndRun(self):
        self.collectSource()
        self.compilerToObject()
        self.run()

class IosCompiler(Compiler):
    def collectSource(self):
        print("Collect Swift source code")

    def compilerToObject(self):
        print("Compilling Swift code to LLVM bit code")

    def run(self):
        print("Program running on runtime environment")

ios = IosCompiler()
ios.compilerAndRun()
