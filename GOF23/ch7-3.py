# 命令行模式
from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock =stock

    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class StockTrade:
    def buy(self):
        print("You will buy stock")

    def sell(self):
        print("You will sell stock")

class Agent:
    def __init__(self):
        self.__order_queue = []

    def placeOrder(self, order):
        self.__order_queue.append(order)
        order.execute()

if __name__=="__main__":
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buy_stock)
    agent.placeOrder(sell_stock)
