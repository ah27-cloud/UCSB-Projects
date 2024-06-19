#testFile.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


b1 = Beverage(9, 12)
b2 = Beverage(28, 9)
b3 = Beverage(32, 11.5)

c1 = Coffee(8, 5.0, "Espresso")
c2 = Coffee(4, 3.5, "Cappuccino")
c3 = Coffee(12, 7.5, 'Latte')

f1 = FruitJuice(14, 4.5, ["Orange", "Peach"])
f2 = FruitJuice(30, 9.45, ["Pineapple", "Passion Fruit", "Mango", "Cherry"])
f3 = FruitJuice(7, 4.8, ["Grape"])

o1 = DrinkOrder()
o2 = DrinkOrder()
o3 = DrinkOrder()
o2.addBeverage(b1)
o2.addBeverage(f3)
o2.addBeverage(c2)


#TEST FUNCTIONS

def test_beverage():
    #test for __innit__
    assert b1.ounces == 9
    assert b1.price == 12
    assert b2.ounces == 28
    assert b2.price == 9
    assert b3.ounces == 32
    assert b3.price == 11.5

    #test for updateOunces and getOunces
    b1.updateOunces(11)
    assert b1.getOunces() == 11
    b2.updateOunces(26)
    assert b2.getOunces() == 26
    b3.updateOunces(40)
    assert b3.getOunces() == 40

    #test for updatePrice and getPrice
    b1.updatePrice(19.5)
    assert b1.getPrice() == 19.5
    b2.updatePrice(7.75)
    assert b2.getPrice() == 7.75
    b3.updatePrice(56.32)
    assert b3.getPrice() == 56.32

    #test for getInfo
    assert b1.getInfo() == "11 oz, $19.50"
    assert b2.getInfo() == "26 oz, $7.75"
    assert b3.getInfo() ==  "40 oz, $56.32"

def test_coffee():
    #test for __innit__
    assert c1.ounces == 8
    assert c1.price == 5
    assert c1.style == "Espresso"
    assert c2.ounces == 4
    assert c2.price == 3.5
    assert c2.style == "Cappuccino"
    assert c3.ounces == 12
    assert c3.price == 7.5
    assert c3.style == "Latte"
    
    #test for getInfo()
    assert c1.getInfo() == "Espresso Coffee, 8 oz, $5.00"
    assert c2.getInfo() == "Cappuccino Coffee, 4 oz, $3.50"
    assert c3.getInfo() == "Latte Coffee, 12 oz, $7.50"

def test_fruitjuice():
    #test for __innit__
    assert f1.ounces == 14
    assert f1.price == 4.5
    assert f1.fruits == ["Orange", "Peach"]
    assert f2.ounces == 30
    assert f2.price == 9.45
    assert f2.fruits == ["Pineapple", "Passion Fruit", "Mango", "Cherry"]
    assert f3.ounces == 7
    assert f3.price == 4.8
    assert f3.fruits == ["Grape"]

    #test for getInfo()
    assert f1.getInfo() == "Orange/Peach Juice, 14 oz, $4.50"
    assert f2.getInfo() == "Pineapple/Passion Fruit/Mango/Cherry Juice, 30 oz, $9.45"
    assert f3.getInfo() == "Grape Juice, 7 oz, $4.80"

def test_drinkorder():
    #test __innit__
    assert o1.drinks == []
    assert o3.drinks == []

    #test addBeverage
    o1.addBeverage(b2)
    assert o1.drinks ==[b2]
    o1.addBeverage(c3)
    assert o1.drinks == [b2, c3]
    o1.addBeverage(f2)
    assert o1.drinks == [b2, c3, f2]
    o2.addBeverage(c1)
    assert o2.drinks == [b1, f3, c2, c1]

    #test getTotalOrder
    assert o3.getTotalOrder() == 'Order Items:\nTotal Price: $0.00'
    assert o1.getTotalOrder() == "Order Items:\n* 26 oz, $7.75\n* Latte Coffee, 12 oz, $7.50\n* Pineapple/Passion Fruit/Mango/Cherry Juice, 30 oz, $9.45\nTotal Price: $24.70"
    assert o2.getTotalOrder() == "Order Items:\n* 11 oz, $19.50\n* Grape Juice, 7 oz, $4.80\n* Cappuccino Coffee, 4 oz, $3.50\n* Espresso Coffee, 8 oz, $5.00\nTotal Price: $32.80"