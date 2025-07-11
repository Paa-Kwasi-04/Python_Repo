# here encapsulation actually achieves abstraction using the access specifiers
class Student:
    def __init__(self, name: str, rollno: int, age: int):
        self.name = name  # so this a normal public instance variable or attribute
        self._rollnum = rollno  # the one underscore shows it is now a protected instance variable
        self.__age = age  # the double underscore makes it private member

    def __repr__(self) -> str:
        return '<class Student>'

    def get_age(self):  # this is using a getter
        return self.__age

    def set_age(self, new_age: int):    # this is using a setter
        self.__age = new_age

    def __show(self):  # the single underscore makes it protected and same for private
        print(f'Name:  {self.name}\tRoll number:{self._rollnum}')

    def display(self):  # this is a public method
        print(f'Hi I am {self.name} with roll number {self._rollnum}from student class')


class Branch(Student):
    pass


b1 = Student('Koku', 10022200152, 19)
b1.display()
print(b1.name)
print(b1.get_age())
b1.set_age(34)
print(b1.get_age())

