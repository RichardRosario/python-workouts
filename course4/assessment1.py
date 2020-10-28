# 1------Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price.

class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

# 2 ====Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked.


class AppleBasket:
    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity = self.apple_quantity + 1

    def __str__(self):
        return 'A basket of {} {} apples.'.format(self.apple_quantity, self.apple_color)


testOne = AppleBasket("red", 5)
print(testOne)
testOne.increase()
print(testOne)


# 3 ==== Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt.

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amt = amount

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)


t1 = BankAccount("Bob", 100)
print(t1)
