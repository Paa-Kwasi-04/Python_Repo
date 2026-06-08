# Property helps us define methods as attributes

class Product:

    def __init__(self, price):
        self.price = price

    @property  # defines the properties of an attribute
    def price(self):
        return self .__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self .__price = value

    @price.deleter
    def price(self):
        self.__price = None


product = Product(-50)
