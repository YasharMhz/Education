
# Dictionaries
# This file contains:
# creating dictionaries, accessing values,
# iterating through dictionaries,
# and dictionary/set comprehensions.



# -----------------------------
# Creating Dictionaries
# -----------------------------


# Dictionary stores data as:
#
# key : value
#
# Unlike lists, dictionaries do not use indexes.
# We access values using keys.


point = {
    "x": 1,
    "y": 2
}



# Accessing value using key

print(point["x"])



# Changing a value

point["x"] = 10



# Adding a new key/value pair

point["z"] = 20



# Removing a key

del point["x"]



print(point)



# -----------------------------
# get() Method
# -----------------------------


# get() returns a value using a key.
#
# If the key does not exist,
# it returns None by default.
#
# We can provide a default value.


print(
    point.get("z", 3)
)



# -----------------------------
# Iterating Dictionaries
# -----------------------------


# items() returns both key and value.


for key, value in point.items():

    print(key, value)



# -----------------------------
# Dictionary Comprehension
# -----------------------------


# Comprehension provides a shorter
# way to create collections.


# List comprehension

values = [
    x * 2
    for x in range(5)
]


print(values)



# Set comprehension


values = {
    x * 2
    for x in range(5)
}


print(values)



# Dictionary comprehension


values = {
    x: x * 2
    for x in range(5)
}


print(values)