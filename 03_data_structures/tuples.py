
# Tuples and Arrays
# This file contains:
# tuple creation, tuple operations,
# unpacking, and arrays.



# -----------------------------
# Tuples
# -----------------------------


# Tuple is an ordered collection.
# The main difference from lists:
# Tuples are immutable (cannot be changed).


point = 1, 2


print(type(point))



# A tuple with one element needs a comma


point = 1,


print(type(point))



# Combining tuples


point = (1, 2) + (3, 4)


print(point)



# Converting a list into a tuple


my_list = [
    1,2,3,4,5,6,7,8
]


print(tuple(my_list))



# -----------------------------
# Tuple Unpacking
# -----------------------------


point = (
    1,
    2,
    3
)


x, y, z = point


print(x, y, z)



# -----------------------------
# Immutable Nature of Tuples
# -----------------------------


# Tuple values cannot be changed.


point = (
    1,
    2,
    3
)


# This causes an error:
#
# point[0] = 10



# Use tuples when:
#
# - Data should not accidentally change
# - You need a fixed collection of values



# -----------------------------
# Swapping Variables
# -----------------------------


x = 10

y = 20



# Python internally uses tuple unpacking


x, y = y, x



print("x =", x)

print("y =", y)



# -----------------------------
# Arrays
# -----------------------------


# Arrays are useful when storing
# many values of the same type.
#
# Unlike lists, arrays require
# all elements to have the same data type.


from array import array



numbers = array(
    "i",
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
    ]
)



print(numbers)