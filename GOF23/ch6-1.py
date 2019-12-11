# 观察者模式
class Subject:
    def __init__(self):
        self.__oberservers = []

    def register(self, oberserver):
        self.__oberservers.append(oberserver)

    def deregister(self, oberserver):
        self.__oberservers.remove(oberserver)

    def notifyAll(self, *args, **kwargs):
        for oberserver in self.__oberservers:
            oberserver.notify(self, *args, **kwargs)


class Oberserver1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: Got ", args, " from ", subject)


class Oberserver2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: Got ", args, " from ", subject)


class Oberserver3:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: Got ", args, " from ", subject)

subject = Subject()
oberserver1 = Oberserver1(subject)
oberserver2 = Oberserver2(subject)
oberserver3 = Oberserver3(subject)
subject.notifyAll("notification", "warning")
subject.deregister(oberserver3)
subject.notifyAll("remove 3")
