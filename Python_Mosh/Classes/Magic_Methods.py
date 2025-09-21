# Magic(Dunder) methods are called automatically by python interpreter

class Point:
    def init_(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # it defines how an object should be represented as a string
        return f'({self.x},{self.y})'

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
