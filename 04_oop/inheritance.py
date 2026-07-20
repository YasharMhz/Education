
# ==========================================
# What is Inheritance?
# ==========================================

# Inheritance allows a class to reuse
# the attributes and methods of another class.
#
# The class that provides features is called:
# Parent class / Base class
#
# The class that receives features is called:
# Child class / Derived class


class Animal:

    def eat(self):
        print("eat")


# ==========================================
# Parent and Child Classes
# ==========================================


class Animal:

    def __init__(self):
        self.age = 1


    def eat(self):
        print("eat")



# Mammal inherits from Animal.
#
# It automatically receives:
# - age attribute
# - eat() method


class Mammal(Animal):

    def walk(self):
        print("walk")



class Fish(Animal):

    def swim(self):
        print("swim")



m = Mammal()


print(m.age)

m.eat()

m.walk()

# ==========================================
# super()
# ==========================================

# When a child class has its own constructor,
# the parent's constructor will not run automatically.
#
# We use super() to call the parent class methods.


class Animal:

    def __init__(self):
        print("Animal constructor")

        self.age = 1



class Mammal(Animal):

    def __init__(self):

        super().__init__()

        print("Mammal constructor")

        self.weight = 2



m = Mammal()


print(m.age)

print(m.weight)

# ==========================================
# Multilevel Inheritance
# ==========================================

# When a class inherits from another child class.
#
# Example:
#
# Animal
#    |
#    |
#  Bird
#    |
#    |
# Chicken


class Animal:

    def eat(self):
        print("eat")



class Bird(Animal):

    def fly(self):
        print("fly")



class Chicken(Bird):

    pass



chicken = Chicken()


chicken.eat()

chicken.fly()

# ==========================================
# Multiple Inheritance
# ==========================================

# A class can inherit from multiple classes.


class Employee:

    def greet(self):
        print("Employee greet")



class Person:

    def greet(self):
        print("Person greet")



class Manager(Employee, Person):

    pass



manager = Manager()


manager.greet()

# ==========================================
# Method Resolution Order (MRO)
# ==========================================

# When multiple classes have the same method,
# Python needs to decide which method to use.
#
# Python follows the order of inheritance.


class Employee:

    def greet(self):
        print("Employee greet")



class Person:

    def greet(self):
        print("Person greet")



class Manager(Employee, Person):

    pass



manager = Manager()


# Employee is written first,
# so Python searches Employee first.

manager.greet()



# We can see the search order with:

print(Manager.mro())

