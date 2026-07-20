
# random_module.py

import random


# -----------------------------
# 1. Generate random numbers
# -----------------------------

random_number = random.randint(1, 10)

print("Random integer:", random_number)


# randint includes both start and end values
# Example: random.randint(1, 10)
# can return 1 and can return 10


# -----------------------------
# 2. Generate random float
# -----------------------------

random_float = random.random()

print("Random float:", random_float)


# random.random()
# returns a float number between 0.0 and 1.0


# -----------------------------
# 3. Random range
# -----------------------------

random_range = random.randrange(1, 20, 2)

print("Random range:", random_range)


# randrange(start, stop, step)
# works like range()
# but returns one random value


# -----------------------------
# 4. Choose random item
# -----------------------------

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

random_language = random.choice(languages)

print("Random language:", random_language)


# choice()
# selects one random item from iterable


# -----------------------------
# 5. Choose multiple random items
# -----------------------------

students = [
    "Ali",
    "Reza",
    "Sara",
    "Yashar",
    "Mina"
]

selected_students = random.sample(students, 3)

print("Selected students:", selected_students)


# sample()
# selects multiple unique items
# without changing original list


# -----------------------------
# 6. Shuffle a list
# -----------------------------

cards = [
    "Ace",
    "King",
    "Queen",
    "Jack"
]

random.shuffle(cards)

print("Shuffled cards:", cards)


# shuffle()
# changes the original list order


# -----------------------------
# 7. Random password generator example
# -----------------------------

characters = "abcdefghijklmnopqrstuvwxyz123456789"

password = ""

for i in range(8):
    password += random.choice(characters)

print("Generated password:", password)