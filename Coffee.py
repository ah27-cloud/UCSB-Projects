#Coffee.py
from Beverage import Beverage

class Coffee(Beverage):
    def __init__(self, ounces, price, style):
        #self.ounces = int(ounces)
        #self.price = float(price)
        super().__init__(ounces, price)
        self.style = str(style)

    def getInfo(self):
        super().getInfo()
        return (f"{self.style} Coffee, {self.ounces} oz, ${self.price:.2f}")

