
# Python Basics
# This file contains fundamental Python concepts:
# variables, strings, numbers, type conversion, operators, and conditions


import math
from itertools import product


# -----------------------------
# Printing
# -----------------------------

print("hello world")

print("**********")

print("*" * 10)


# -----------------------------
# Variables
# -----------------------------

student_count = 30

is_published = True

course_name = "python programming"


# Multi-line string
message = """
hi.
welcome
"""

print(message)


# -----------------------------
# Strings
# -----------------------------

course_name = "python programming"

# len() returns the number of characters
print(len(course_name))


# Accessing characters using index
print(course_name[1])


# Slicing strings
print(course_name[0:-1])


# Escape characters

# Using \" to write quotes inside a string
course_name = "python \" programming"

print(course_name)


# Using \\ to write a backslash
course_name = "python \\ programming"

print(course_name)


# \n creates a new line
course_name = "python \n programming"

print(course_name)


# \t creates a tab space
course_name = "python \t programming"

print(course_name)


# String concatenation
first = "coding"

last = "is cool"

full = first + " " + last

print(full)


# Formatted strings (f-string)

first = "coding"

last = "is cool"

full = f"{first} {last} neon"

print(full)


# Shorter version

print(f"{first} {last} neon")


# -----------------------------
# String Methods
# -----------------------------

course = "python programming"


# upper() converts all characters to uppercase
print(course.upper())


# lower() converts all characters to lowercase
print(course.lower())


# title() makes the first character of each word uppercase
print(course.title())


# strip() removes extra spaces from both sides
course = " python programming "

print(course.strip())


# rstrip() removes spaces from the right side
print(course.rstrip())


# lstrip() removes spaces from the left side
print(course.lstrip())


# find() returns the index of the given value
course = "python programming"

print(course.find("pyt"))


# replace() replaces one value with another
print(course.replace("pyt", "z"))


# Checking if a value exists inside a string
print("py" in course)


# Checking if a value does not exist
print("py" not in course)



# -----------------------------
# Numbers
# -----------------------------

# Integer example
# 5

# Float example
# 5.2


# Arithmetic operators

# Addition
print(10 + 3)


# Subtraction
print(10 - 3)


# Multiplication
print(10 * 3)


# Division
print(10 / 3)


# Floor division
print(10 // 3)


# Remainder
print(10 % 3)


# Power
print(10 ** 3)



# Assignment operators

x = 10

x = x + 3

print(x)


# Short form

x = 10

x += 3

print(x)


x = 10

x -= 3

print(x)


x = 10

x *= 3

print(x)


x = 10

x /= 3

print(x)


x = 10

x //= 3

print(x)


x = 10

x %= 3

print(x)


x = 10

x **= 3

print(x)



# -----------------------------
# Built-in number functions
# -----------------------------


# round() rounds a number

print(round(2.9))


# abs() returns absolute value

print(abs(-2))


# math module
# math is a built-in module that provides mathematical functions


# ceil() rounds a number up

print(math.ceil(2.8))

# -----------------------------
# User Input and Type Conversion
# -----------------------------

# input() allows us to receive data from the user

# x = input("x : ")


# Type conversion functions:
#
# int()   -> converts value to integer
# float() -> converts value to float
# bool()  -> converts value to True or False
# str()   -> converts value to string
#
# bool() returns False for:
# 0
# ""
# None
#
# Everything else becomes True


# Example:

# x = input("x : ")
# y = int(x) + 1
#
# print(type(y))
# print(type(x))
# print(y)



# -----------------------------
# Comparison Operators
# -----------------------------


print(3 > 4)

print(3 < 4)


# Greater than or equal

print(3 >= 4)


# Less than or equal

print(3 <= 4)


# Equal

print(3 == 4)


# Not equal

print(3 != 4)



# Comparing strings

# Python compares strings based on their Unicode values

print(ord("a"))

print("ali" == "mohammad")



# -----------------------------
# Conditional Statements
# -----------------------------


temperature = 10


if temperature > 30:
    print("It's warm")
    print("Drink water")

elif temperature > 20:
    print("It's nice")

else:
    print("It's cold")



# Another example

age = 14


if age >= 18:
    message = "eligible"

else:
    message = "not eligible"


print(message)



# Ternary operator

age = 16


message = "eligible" if age >= 18 else "not eligible"


print(message)



# -----------------------------
# Logical Operators
# -----------------------------

# and
# or
# not


high_income = True

good_credit = True

student = True


if not student and (high_income or good_credit):
    print("eligible")

else:
    print("not eligible")



# Chained comparison

# Age should be between 18 and 65

age = 22


if 18 <= age <= 65:
    print("eligible")



# -----------------------------
# For Loops
# -----------------------------


# range() creates an iterable object

for number in range(4):

    print("message")

    print(number)



# Printing stars

for number in range(4):

    print((number + 1) * "*")



# range(start, stop, step)
#
# start -> starting value
# stop  -> ending value (not included)
# step  -> amount of increase


for number in range(1, 10, 2):

    print(number)



# -----------------------------
# For Else and Break
# -----------------------------


# break stops the loop immediately


successful = False


for number in range(3):

    print("attempt")


    if successful:

        print("successful")

        break


else:

    print("Attempted 3 times and failed")



# Important:
# The else block runs only if the loop finishes normally.
# If break executes, else will not run.



# -----------------------------
# Nested Loops
# -----------------------------


# Outer loop runs 9 times
# Inner loop runs 3 times for each outer loop


for x in range(9):

    for y in range(3):

        print(f"{x}, {y}")



# -----------------------------
# Lists
# -----------------------------


# Lists are collections that can store multiple values.
# Lists are iterable and can contain different data types.


numbers = [1, 2, 3, 4, "yashar", "ali"]


print(numbers)


for x in numbers:

    print(x)



# -----------------------------
# While Loop
# -----------------------------


# while continues as long as the condition is True


number = 100


while number > 0:

    print(number)

    number //= 2


print("done")



# Simulating a command line program


# command = ""

# while command.lower() != "exit":

#     command = input(">>>")

#     print(command)



# Another way using break


# command = ""

# while True:

#     command = input(">>>")

#     print(command)

#     if command.lower() == "exit":

#         break


# print("done")