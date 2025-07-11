class Student:
    def __init__(self, name: str, rollno: int, age: int):
        self.name = name  # so this a normal public instance variable or attribute
        self._rollnum = rollno  # the one underscore shows it is now a protected instance variable
        self.__age = age  # the double underscore makes it private member

    def __repr__(self) -> str:
        return '<class Student>'

    def __show(self):  # the single underscore makes it protected and same for private
        print(f'Name:  {self.name}\tRoll number:{self._rollnum}')

    def getShowMethod(self):
        self.__show()  # this is the other method of accessing private methods

    def display(self):  # this is a public method
        print(f'Hi I am {self.name} with roll number {self._rollnum}from student class')


class Branch(Student):
    pass


b1 = Student('Koku', 10022200152, 19)
b1.display()
print(b1.name)
# print(b1._rollnum) avoid accessing protected members outside their class
# s1 = Student('kwasi', 10022200096)
# print(s1.name)
# s1.display()
# but to access private specifiers like __age you can use a method known as name mangling
# example
print(b1._Student__age)
