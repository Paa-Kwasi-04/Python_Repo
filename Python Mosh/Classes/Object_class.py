# All classes inherit from the Object class
# so all class inherit all magic methods from the object class

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


# Animal: Parent Class
# Mammal and Fish: Child or subclass
class Mammal(Animal):
    def walk(self):  # they inherit both the methods and attributes of Animal class
        print('Walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()


# Built in functions of use
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, Object))
