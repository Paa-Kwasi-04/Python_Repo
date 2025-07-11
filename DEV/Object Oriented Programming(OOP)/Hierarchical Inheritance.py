class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def showDetails(self):
        print(f'name: {self.name}, age: {self.age}')

    def eat(self):
        print('I can eat')


class Male(Human):
    def __init__(self, name: str, age: int, job: str):
        super().__init__(name, age)
        self.job = job

    def sleep(self):
        print('I can sleep whole day')


class Female(Human):

    def work(self):
        print('I can code')


f_1 = Female('Abena', 20)
f_1.eat()
f_1.work()
m_1 = Male('Kwasi', 21, 'Doctor')
m_1.eat()
m_1.sleep()
f_1.showDetails()
