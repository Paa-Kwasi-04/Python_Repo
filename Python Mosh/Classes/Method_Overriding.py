# Method Overriding means replacing or extending a method defined in the base class

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self):  # Super() gives us access to the parent class
        # so that we can still have the age attribute without overriding parent constructor
        self.weight = 2
        super().__init__()

    def walk(self):
        print('Walk')


m = Mammal()
print(m.age)
print(m.weight)
