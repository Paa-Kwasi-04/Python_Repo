class Human:
    def __init__(self, years: int):
        self.eyes = 2
        self.nose = 1
        self.years = years

    def eat(self):
        print('I can eat')

    def work(self):
        print('I can work')


class Male(Human):
    def __init__(self, name: str, age):
        super().__init__(age)
        self.name = name

    def work(self):
        # So the super function helps you access
        # the attributes and methods of the base class of a given class
        super().work()  # or Human.work(self)
        print(f'I can code and I am {self.years} years old')





kwasi = Male('kwasi', 18)
kwasi.eat()
kwasi.work()
print(kwasi.eyes)
