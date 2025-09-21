class Point:
    def __init__(self, x, y):  # this is an instance method
        self.x = x
        self.y = y

    @classmethod  # it is a decorat orto indicate it is a class method
    def zero(cls):  # cls like self is a reference to the class itself
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
print(Point.zero())
point.draw()
