class Point:
    def __init__(self, x, y):  # it is a constructor for creating new objects of any class
        self.x = x   # self if the basic parameter of each method in a class and a reference to the current point object
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
point.draw()
