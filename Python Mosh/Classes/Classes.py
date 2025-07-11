# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack,

class Point:
    def draw(self):
        print('Draw')


point = Point()
print(type(point))
print(isinstance(point, Point))  # to know if it is an object of a class
