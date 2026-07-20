
# Sets
# This file contains:
# creating sets, removing duplicates,
# and performing set operations.



# -----------------------------
# Creating Sets
# -----------------------------


# A set is an unordered collection
# of unique values.
#
# Sets:
# - do not have indexes
# - do not allow duplicate values
# - are mutable


numbers = [
    1,
    1,
    3,
    4,
    5,
    4,
    7,
    7
]


# Convert list to set
# to remove duplicate values.


first = set(numbers)


second = {
    1,
    5
}


print(first)

print(second)



# -----------------------------
# Adding Elements
# -----------------------------


# add() adds a new element.
# Adding an existing value has no effect.


second.add(6)

second.add(6)


print(second)



# -----------------------------
# Removing Elements
# -----------------------------


# remove() deletes an element.
#
# If the element does not exist,
# it raises an error.


second.remove(1)


print(second)



# -----------------------------
# Set Length
# -----------------------------


print(len(second))



# -----------------------------
# Set Operations
# -----------------------------


first = {
    1,
    3,
    4,
    5,
    7
}


second = {
    5,
    6,
    7
}



# Union
#
# Returns all unique elements
# from both sets.


print(
    first | second
)



# Intersection
#
# Returns elements that exist
# in both sets.


print(
    first & second
)



# Difference
#
# Returns elements that exist
# in the first set but not in the second.


print(
    first - second
)



# Symmetric Difference
#
# Returns elements that exist
# in either set, but not both.


print(
    first ^ second
)