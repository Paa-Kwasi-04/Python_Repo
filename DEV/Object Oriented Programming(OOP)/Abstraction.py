from Abstract_class import Vehicle


class Bike(Vehicle):
    def __init__(self, n: int, color: str):
        super().__init__(n)
        self.color = color

    def start(self):
        print('Start with kick')


class Scooty(Vehicle):
    def __init__(self, n: int):
        super().__init__(n)

    def start(self):
        print('Self start')


class Car(Vehicle):
    def __init__(self, n: int, x: int):
        super().__init__(n)
        self.no_of_gears = x

    def start(self):
        print('Start with key')
