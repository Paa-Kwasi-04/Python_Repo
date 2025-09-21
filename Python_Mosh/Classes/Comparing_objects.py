class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # this dunder method defines the behavior for the equality operator to your class
        # so this is how we define to instances for a class to be equal
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # this dunder method defines the behavior for the equality operator to your class
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
# so dont need to explicitly define this one also in the class, python figures out what to do for this other case
print(point < other)
