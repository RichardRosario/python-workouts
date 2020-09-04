class Cereal:
    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)


c1 = Cereal("Corn Flakes", "Kellogg's", '2')
c2 = Cereal("Honey Nut Cheerios", "General Mills", '3')
# print(c1)
# print(c2)

# ===================Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!”


class Point:
    """ Point class for representing and manipulating x,y coordinates. """
# dunder method to initialize

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
# str dunder method to print string

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
# add dunder methods

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)


p1 = Point(7, 6)
p2 = Point(4, 5)
print(p1)
print(p2)
print(p1+p2)
