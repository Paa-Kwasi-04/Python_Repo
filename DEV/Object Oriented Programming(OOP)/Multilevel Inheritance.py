class Human:
    def __init__(self, years: int):
        self.eyes = 2
        self.years = years

    def eat(self):
        print('I can eat')

    def sleep(self):
        print('I can sleep')


class Male(Human):
    def __init__(self, name: str, age):
        super().__init__(age)
        self.name = name

    def work(self):
        print('I can work')


class Boy(Male):

    def __init__(self, years, name, can_dance: bool):
        Human.__init__(self, years)
        Male.__init__(self, name, years)
        self.dance = can_dance

    def sleep(self):
        Human.sleep(self)  # super().sleep()
        print('Sleep very early')


b1 = Boy(19, 'kwasi', True)
b1.eat()
print(b1.eyes)
b1.sleep()
