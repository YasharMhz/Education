
# Generators and Unpacking Operators
# This file contains:
# generator objects, memory efficiency,
# and unpacking operators.


# -----------------------------
# Generator Objects
# -----------------------------


# A generator is an iterable object
# that produces values one at a time.
#
# Unlike lists, generators do not store
# all values in memory.
#
# They store the logic for creating values.


values = (
    x * 2
    for x in range(999)
)



for x in values:

    print(x)



# -----------------------------
# Generator vs List
# -----------------------------


# List:
#
# numbers = [x * 2 for x in range(999)]
#
# All values are created immediately
# and stored in memory.



# Generator:
#
# values = (x * 2 for x in range(999))
#
# Values are created only when needed.



# Generators are useful when:
#
# - Working with large amounts of data
# - We do not need all values at once



# -----------------------------
# Unpacking Operator *
# -----------------------------


# The * operator unpacks iterable values.


numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]


print(*numbers)



# Creating a list using unpacking


values = [
    *range(5)
]


print(values)



# Unpacking characters from a string


chars = [
    *"hello"
]


print(chars)



# Combining multiple iterables


first = [
    1,
    2
]


second = [
    3,
    4
]


values = [
    *first,
    3,
    *second,
    *"hello"
]


print(values)



# -----------------------------
# Dictionary Unpacking **
# -----------------------------


# For dictionaries we use **.


first = {
    "x": 1
}


second = {
    "x": 1,
    "y": 2
}



# Combining dictionaries


combined = {
    **first,
    **second
}



print(combined)