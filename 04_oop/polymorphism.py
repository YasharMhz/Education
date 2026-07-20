
# ==========================================
# What is Polymorphism?
# ==========================================

# Polymorphism means:
#
# "Many forms"
#
# It allows different objects to respond
# to the same method call in different ways.
#
# Example:
#
# Different objects can have a draw()
# method, but each one implements it differently.

# ==========================================
# Same Interface, Different Behavior
# ==========================================


class TextBox:

    def draw(self):
        print("Drawing a TextBox")



class DropDownList:

    def draw(self):
        print("Drawing a DropDownList")



def draw_controls(controls):

    for control in controls:
        control.draw()



textbox = TextBox()

dropdown = DropDownList()


draw_controls([
    textbox,
    dropdown
])

# ٍExplain : Both classes have the same method:
#     draw()
# But each class has a different implementation.
# The function does not care about the object type.
# It only cares that the object has a draw() method.

# ==========================================
# Polymorphism with Inheritance
# ==========================================


class Animal:

    def speak(self):
        pass



class Dog(Animal):

    def speak(self):
        print("Woof")



class Cat(Animal):

    def speak(self):
        print("Meow")



def make_sound(animals):

    for animal in animals:
        animal.speak()



dog = Dog()

cat = Cat()


make_sound([
    dog,
    cat
])

#explain : Dog and Cat inherit from Animal.
# Both classes override the speak() method.
# The same function:
#     make_sound()
# works with different objects.

# ==========================================
# Duck Typing
# ==========================================

# Duck typing means:
#
# "If an object behaves like something,
# we can use it like that thing."
#
# Python focuses on behavior,
# not the actual type.
#
# Famous example:
#
# If it walks like a duck
# and talks like a duck,
# it is treated like a duck.


class TextBox:

    def draw(self):
        print("TextBox")



class DropDownList:

    def draw(self):
        print("DropDownList")



def draw(controls):

    for control in controls:
        control.draw()



textbox = TextBox()

dropdown = DropDownList()


draw([
    textbox,
    dropdown
])

#The difference between Inheritance and Duck typing :
# Inheritance:
# _ Uses a parent_child relationship
# _ Classes share behavior through inheritance
# Example :
# Dog -> Animal

# Duck Typing :
# - No inheritance required.
# - Only behavior matters.
# - If an object has the required method, it can be used.


