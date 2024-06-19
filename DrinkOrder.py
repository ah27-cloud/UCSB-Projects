#DrinkOrder.py
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        orderlines = '\n* '.join([i.getInfo() for i in self.drinks]) 
        totalprice = 0
        if len(self.drinks)==0:
            return (f"Order Items:\nTotal Price: ${totalprice:.2f}")
        for i in self.drinks:
            totalprice += i.price
        return (f"Order Items:\n* " + orderlines + f"\nTotal Price: ${totalprice:.2f}")

