# Multilevel Inheritance can lead to complexity in your class
# Limit Multilevel inheritance to at most two levels if needed

class Animal:
    def eat(self):
        print("eat")


class Bird (Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass
