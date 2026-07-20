
# ==========================================
# Classes and Objects
# ==========================================

# A class is a blueprint for creating objects.
#
# An object is an instance of a class.
#
# Every method inside a class needs a parameter
# called self by convention.
#
# self refers to the current object.


class Point:

    def draw(self):
        print("draw")


# Creating an object from the Point class

point = Point()


# isinstance() checks whether an object
# is created from a specific class.

print(isinstance(point, Point))

# ==========================================
# Constructor (__init__)
# ==========================================

# The __init__ method is a special method
# that runs automatically when an object is created.
#
# We use it to initialize object attributes.


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def info(self):
        print(f"Point {self.x}, {self.y}, {self.z}")


point = Point(7, 8, 9)

point.info()
# ==========================================
# Instance Attributes
# ==========================================

# Instance attributes belong to each object separately.
#
# In this example:
# x, y, and z are instance attributes.
#
# Every object has its own values.


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point1 = Point(7, 8, 9)
point2 = Point(1, 5, 8)


print(point1.x)
print(point2.x)

# ==========================================
# Class Attributes
# ==========================================

# Class attributes belong to the class itself.
#
# They are shared between all objects.
#
# If an object changes this attribute,
# Python creates a new attribute only for that object.


class Point:

    default_color = "red"


    def __init__(self, x, y):
        self.x = x
        self.y = y



point = Point(7, 8)
another = Point(1, 5)


# Changing the attribute for each object

point.default_color = "blue"
another.default_color = "green"


print(point.default_color)
print(another.default_color)


# Accessing the class attribute directly

print(Point.default_color)

# ==========================================
# Class Methods and Factory Methods
# ==========================================

# @classmethod creates a method that belongs
# to the class instead of an object.
#
# The first parameter of a class method is cls.
#
# cls refers to the class itself.


class Point:

    default_color = "red"


    def __init__(self, x, y):
        self.x = x
        self.y = y


    @classmethod
    def zero(cls):
        return cls(0, 0)


    def info(self):
        print(f"Point({self.x}, {self.y})")



# Factory method creates an object
# in another way.

point = Point.zero()

point.info()

# ==========================================
# Magic Methods
# ==========================================

# Magic methods are special methods
# that have double underscores.
#
# Examples:
#
# __init__
# __str__
# __eq__
# __add__
#
# They allow Python to define
# how objects should behave.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"Point({self.x}, {self.y})"



point = Point(1, 2)


# Python automatically calls __str__()
# when we print an object.

print(point)

# ==========================================
# Comparing Objects
# ==========================================

# By default, Python compares objects
# by their memory address.
#
# We can change this behavior
# using magic methods.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Equal operator (==)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    # Greater than operator (>)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y



point = Point(7, 6)

another = Point(2, 1)


print(point == another)

print(point > another)

# ==========================================
# Operator Overloading
# ==========================================

# Operator overloading allows us to define
# how operators work with our objects.
#
# For example:
# +
# -
# ==
#
# We can customize their behavior
# using magic methods.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"Point({self.x}, {self.y})"


    # This method changes the behavior
    # of the + operator.

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )



point = Point(1, 2)

another = Point(2, 1)


result = point + another


print(result)

# ==========================================
# Custom Data Structures
# ==========================================

# Python allows us to create our own
# data structures.
#
# In this example, we create a class
# that counts words.


class BagOfWords:

    def __init__(self):
        self.words = {}


    # Add a word and increase its count.

    def add(self, word):
        self.words[word.lower()] = (
            self.words.get(word.lower(), 0) + 1
        )


    # Allows accessing objects like a dictionary.
    #
    # Example:
    # document["python"]

    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)


    # Allows changing values like a dictionary.
    #
    # Example:
    # document["python"] = 10

    def __setitem__(self, word, count):
        self.words[word.lower()] = count


    # Allows using len(object)

    def __len__(self):
        return len(self.words)


    # Makes the object iterable.

    def __iter__(self):
        return iter(self.words)



document = BagOfWords()


document.add("python")
document.add("Python")
document.add("python")


print(document.words)


document["python"] = 10


print(document["python"])

print(len(document))

# ==========================================
# Encapsulation
# ==========================================

# Encapsulation means hiding the internal
# details of an object.
#
# We can make attributes private by adding
# two underscores before their names.


class BagOfWords:

    def __init__(self):
        self.__words = {}


    def add(self, word):
        self.__words[word.lower()] = (
            self.__words.get(word.lower(), 0) + 1
        )


    def __getitem__(self, word):
        return self.__words.get(word.lower(), 0)


    def __len__(self):
        return len(self.__words)



document = BagOfWords()


document.add("Python")
document.add("Python")


print(document["python"])

print(len(document))


# Python internally changes:
#
# __words
#
# into:
#
# _BagOfWords__words
#
# This prevents direct access in normal usage.

# ==========================================
# Properties
# ==========================================

# Properties allow us to control access
# to attributes.
#
# They are commonly used for validation.


class Product:

    def __init__(self, price):
        self.price = price


    # Getter

    @property
    def price(self):
        return self.__price


    # Setter

    @price.setter
    def price(self, value):

        if value < 0:
            raise ValueError(
                "Price cannot be negative"
            )

        self.__price = value



product = Product(5)


print(product.price)


product.price = 10

print(product.price)

