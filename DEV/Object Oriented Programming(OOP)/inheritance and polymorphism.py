class Animal:

    def __init__(self, name: str, age: int, num_legs: int):
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __repr__(self):
        return '<class \'Animal\'>'

    def __str__(self):
        return f'Name:{self.name}'

    def talk(self):
        return f'{self.name} can\'t talk yet'


class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str):
        # takes common attributes and pass to the parent(super) class
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = 'Dog'

    def __str__(self) -> str:
        return f'{self.type}: {self.name}, Breed: {self.breed}'

    def talk(self):
        return f'{self.name} says wolf'

    def sniff(self, item: str):
        return f'{self.name} is sniffing out {item}'


a1 = Animal('bob', 20, 4)
print(a1.talk())
d1 = Dog('tom', 4, 4, 'german shepherd')
print(d1)
print(d1.talk(), d1.sniff('ball'))

# checks if a class inherits from another class
print(isinstance(d1, Animal), isinstance(d1, Dog))


























