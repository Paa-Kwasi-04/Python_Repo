# we can solve this problem using the c3 linearization algorithm with help from mro
class A:
    def display(self):
        print('display from A class')


class B(A):
    pass
    # def display(self):
    #     print('display from class B')


class C(A):
    def show(self):
        print('Hi from C class')

    def display(self):
        print('Display from C class')


class D(B, C):
    pass
    # def display(self):
    #     print('Display from D class')


d1 = D()
d1.display()
print(D.__mro__)
