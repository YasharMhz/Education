
# Lists
# This file contains:
# creating lists, accessing elements,
# modifying lists, list methods,
# sorting, mapping, filtering,
# comprehensions, stack and queue examples.



# -----------------------------
# Creating Lists
# -----------------------------


# Lists are collections that can store multiple values.
# They are ordered, mutable, and iterable.


numbers = [1, 2, 3, 4, "yashar", "ali"]


print(numbers)



# Iterating through a list

for number in numbers:

    print(number)



# -----------------------------
# Matrix (Nested Lists)
# -----------------------------


# A matrix is a list that contains other lists.


letters = ["a", "b", "c"]


matrix = [
    [1, 2],
    [3, 4]
]


print(letters[0])



# Creating a list with repeated values

zeros = [0] * 5


combined = zeros + letters


print(combined)



# -----------------------------
# Converting Values to Lists
# -----------------------------


# list() converts an iterable into a list.


numbers = list(range(21))


print(numbers)



chars = list("hello world")


print(chars)


print(len(chars))



# -----------------------------
# Accessing List Elements
# -----------------------------


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
]


# Changing a value using index

letters[2] = 2


print(letters)



# -----------------------------
# List Slicing
# -----------------------------


numbers = list(range(20))


# Every second element

print(numbers[::2])


# Reverse the list

print(numbers[::-1])


# Reverse with step

print(numbers[::-2])



# -----------------------------
# List Unpacking
# -----------------------------


numbers = [1, 2, 3]


first = numbers[0]

second = numbers[1]

third = numbers[2]


print(first, second, third)



# Cleaner way


first, second, third = numbers


print(first, second, third)



# Using * to collect remaining values


numbers = [
    1,2,3,4,5,6,7,8
]


first, second, *other = numbers


print(first, second, other)



first, *other, last = numbers


print(first, last, other)



# -----------------------------
# Enumerate
# -----------------------------


# enumerate() gives us both index and value.


letters = [
    "a",
    "b",
    "c"
]


for index, letter in enumerate(letters):

    print(
        f"index = {index}, letter = {letter}"
    )



# -----------------------------
# Adding Elements
# -----------------------------


letters = [
    "a",
    "b",
    "c"
]


# append() adds an element at the end

letters.append("d")


print(letters)



# insert() adds an element at a specific index


letters.insert(0, "d")


print(letters)



# -----------------------------
# Removing Elements
# -----------------------------


letters = [
    "a",
    "b",
    "c"
]


# pop() removes and returns an element.
# Without index, it removes the last element.


result = letters.pop()


print(letters)


print(result)



# Removing a specific value


letters = [
    "a",
    "b",
    "c"
]


if "d" in letters:

    letters.remove("d")


print(letters)



# del removes elements using index or slicing


letters = [
    "a",
    "b",
    "c"
]


del letters[0:3]


print(letters)



# clear removes all elements


letters = [
    "a",
    "b",
    "c"
]


letters.clear()


print(letters)



# -----------------------------
# Finding Elements
# -----------------------------


letters = [
    "a",
    "b",
    "c"
]


# index() returns the position of an element


if "b" in letters:

    print(letters.index("b"))



# count() counts how many times a value exists


letters = [
    "a",
    "a",
    "b",
    "c"
]


print(letters.count("a"))

# -----------------------------
# Sorting Lists
# -----------------------------


numbers = [
    3,
    20,
    1,
    4,
    5,
    8,
    7,
    9
]


# sort() changes the original list.
# Default order is ascending.

numbers.sort()


print(numbers)



# Sorting in descending order


numbers = [
    3,
    20,
    1,
    4,
    5,
    8,
    7,
    9
]


numbers.sort(reverse=True)


print(numbers)



# sorted() creates a new sorted list.
# It does not modify the original list.


numbers = [
    3,
    20,
    1,
    4,
    5,
    8,
    7,
    9
]


print(sorted(numbers))



# -----------------------------
# Sorting Objects with key
# -----------------------------


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]



# This function tells Python
# which value should be used for sorting.


def sort_items(item):

    return item[1]



items.sort(key=sort_items)


print(items)



# The same code using lambda


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


# lambda creates a small anonymous function.


items.sort(
    key=lambda item: item[1]
)


print(items)



# -----------------------------
# map()
# -----------------------------


# map() applies a function to every element
# and returns a map object.


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


prices = list(
    map(
        lambda item: item[1],
        items
    )
)


print(prices)



# -----------------------------
# filter()
# -----------------------------


# filter() keeps elements that match a condition.


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


filtered = list(
    filter(
        lambda item: item[1] >= 10,
        items
    )
)


print(filtered)



# -----------------------------
# List Comprehension
# -----------------------------


# List comprehension is a shorter way
# to create lists.


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]


# Similar to map()

prices = [
    item[1]
    for item in items
]


print(prices)



# Similar to filter()

filtered = [
    item
    for item in items
    if item[1] >= 10
]


print(filtered)



# -----------------------------
# zip()
# -----------------------------


# zip() combines multiple iterables together.


list1 = [
    1,
    2,
    3
]


list2 = [
    10,
    20,
    30
]


print(
    list(
        zip(
            list1,
            list2,
            "abc"
        )
    )
)



# -----------------------------
# Stack Example
# -----------------------------


# Stack follows LIFO:
# Last In First Out
#
# The last item added is the first one removed.


browsing = []


browsing.append(1)

browsing.append(2)

browsing.append(3)



# Remove the last opened page

browsing.pop()

browsing.pop()



if not browsing:

    print("disabled")



print(browsing)



# -----------------------------
# Queue Example
# -----------------------------


# Queue follows FIFO:
# First In First Out
#
# The first item added is the first one removed.


from collections import deque



queue = deque([])



queue.append(1)

queue.append(2)

queue.append(3)



# popleft removes the first item

queue.popleft()



if not queue:

    print("empty")



print(queue)