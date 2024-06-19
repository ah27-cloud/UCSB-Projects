#FruitJuice.py
from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        #self.ounces = int(ounces)
        #self.price = float(price)
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        super().getInfo()
        fruit_list = '/'.join(self.fruits)
        return (f"{fruit_list} Juice, {self.ounces} oz, ${self.price:.2f}")