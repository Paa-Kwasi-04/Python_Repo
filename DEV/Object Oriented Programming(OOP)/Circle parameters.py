class Circle:
    pi = 3.142  # class object attribute

    def __init__(self, r: int):
        self.radius = r

    def area(self) -> float:
        return float(f'{self.pi * self.radius ** 2: ,.2f}')

    def circumference(self) -> float:
        return float(f'{Circle.pi * 2 * self.radius: ,.2f}')


c_1 = Circle(4)
print(c_1.area())
print(c_1.circumference())
c_2 = Circle(10)
print(c_2.area())
print(c_2.circumference())
