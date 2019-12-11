class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News: ", self.__latestNews


from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__=="__main__":
    new_publisher = NewsPublisher()
    for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscriber(new_publisher)
    print("\nSubscribers: ", new_publisher.subscribers())
    new_publisher.addNews("Hello world")
    new_publisher.notifySubscribers()

    print("\nDetached: ", type(new_publisher.detach()).__name__)
    print("\nSubscribers: ", new_publisher.subscribers())

    new_publisher.addNews("my second news")
    new_publisher.notifySubscribers()
