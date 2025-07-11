class A:
    def display(self):
        print('display from A class')


class B(A):
    def display(self):
        print('display from class B')


class C:
    def show(self):
        print('Hi from C class')


class D(B, C):
    def display(self):
        print('Display from D class')


d1 = D()

