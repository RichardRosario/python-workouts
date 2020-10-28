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

    def halfway(self, target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)

# str dunder method to print string

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
# add dunder methods

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)


p1 = Point(7, 6)
p2 = Point(4, 5)
# print(p1)
# print(p2)
# print(p1+p2)

# =========================
# instances as return values
# methods to get the midpoint between two points

mid = p1.halfway(p2)
# print(mid)

# #=========================

# sorting list of instances


class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
# print("-----sorted by price, referencing a class method-----")

for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

    # print("---- one more way to do the same thing-----")
    # using lambda
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)

    # =================


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1):
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + \
                    (" "*(int(self.x) - 1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())
