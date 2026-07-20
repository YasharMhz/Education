
# Abstract classes in Python
#
# Abstract classes are classes that cannot be instantiated directly.
# They are used as a blueprint for other classes.
#
# To create an abstract class we use:
# ABC (Abstract Base Class)
# abstractmethod


from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# ABC means:
# This class is an abstract class.
# We cannot create an object directly from this class.

class Stream(ABC):

    def __init__(self):
        self.opened = False


    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")

        self.opened = True


    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")

        self.opened = False


    # abstractmethod means:
    # Every child class that inherits from Stream
    # must implement this method.

    @abstractmethod
    def read(self):
        pass



class FileStream(Stream):

    def read(self):
        print("Reading data from a file")



class NetworkStream(Stream):

    def read(self):
        print("Reading data from a network")



# This class is not complete because
# it doesn't implement the read method.
#
# Therefore, we cannot create an object from it.

class MemoryStream(Stream):
    pass



file = FileStream()
file.open()
file.read()


network = NetworkStream()
network.open()
network.read()


# This will cause an error because
# MemoryStream does not implement read()
#
# memory = MemoryStream()


# This also causes an error because
# Stream itself is an abstract class.
#
# stream = Stream()