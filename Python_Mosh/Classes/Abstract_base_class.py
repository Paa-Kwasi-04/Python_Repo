from abc import ABC, abstractmethod


class InvalidOperationError(Exception):  # Creating our own exception
    pass


class Stream(ABC):  # makes the stream class abstract
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already Opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already Closed')
        self.opened = False

    @abstractmethod  # so all we do is declare it but defining it is done in each subclasses
    def read(self):  # Makes this method abstract causing all subclasses to have different implementation of the method
        pass


class FileStream(Stream):
    def read(self):  # So now all classes based of the abstract class Stream must have a read method
        print('Reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading data from a Networking')


# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstract methods
