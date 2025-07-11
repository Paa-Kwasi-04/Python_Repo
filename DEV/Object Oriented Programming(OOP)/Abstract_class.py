from abc import ABC, abstractmethod


class Vehicle(ABC):  # Inheriting from ABC class makes Vehicle an abstract class
    def __init__(self, n: int):
        self.noOfTyres = n

    @abstractmethod  # even do this method has no definition(abstract) the abstractmethod decorator emphasizes that
    def start(self):
        pass

    def display(self):
        print('Hi I am calling from abstract class')
