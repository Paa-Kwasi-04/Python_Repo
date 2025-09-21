# And it helps is the base classes have absolutely no methods or attributes in common
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # Multiple Inheritance
    pass


manager = Manager()
manager.greet()  # checks if Manager class has greet method, then checks its base classes in the other they were listed
