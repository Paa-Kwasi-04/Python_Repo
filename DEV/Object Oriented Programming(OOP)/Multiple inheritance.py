class Human:
    def __init__(self, years: int):
        self.eyes = 2
        self.nose = 1
        self.age = years

    def eat(self):
        print('I can eat')

    def work(self):
        print('I can work')


class Male():
    def __init__(self, name: str):
        self.name = name

    def flirt(self):
        print(f'I can flirt')

    def work(self):
        print('I can code')


# so the order in which the base names are written is important
# since if the parent classes of a given base class have the same method
# the method of the first parent can be accessed by the child class

class Boy(Human, Male):
    def __init__(self, name: str, age: int, lang: str):
        Male.__init__(self, name)
        Human.__init__(self, age)
        self.lang = lang

    def sleep(self):
        print('I can sleep')

    def work(self):
        print('I can test')


boy_1 = Boy('name', 19, 'french')
boy_1.work()
print(boy_1.age)
print(boy_1.lang)

# the solution for the problem above
Male.work(boy_1)  # calls the work method of Male class for the object boy_1
Human.work(boy_1)
# Keep in mind the MRO of a class(Method Resolution Order)
print(Boy.mro())
