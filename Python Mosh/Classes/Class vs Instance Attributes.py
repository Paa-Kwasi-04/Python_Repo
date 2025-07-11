# But class attributes apply to all instances in the class
class Point:
    default_color = 'red'  # this is the class attribute

    def __init__(self, x, y):
        self.x = x   # these are instance attributes
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


# since we are changing the class attribute it affects all instances
Point.default_color = 'yellow'


point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10  # you can define instance attributes like this as well
point.draw()


another = Point(3, 4)
print(another.default_color)
another.draw()
