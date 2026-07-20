
# Working with files in Python
#
# Python provides built-in functions
# to create, read, write and manage files.


# Opening a file
#
# open() creates a connection between Python
# and the file.


# Modes:
#
# "r" = read
# "w" = write (creates a new file or overwrites existing file)
# "a" = append (adds data to the end of file)
# "x" = create a new file


file = open("example.txt", "w")

file.write("Hello Python")

file.close()



# Reading from a file

file = open("example.txt", "r")

content = file.read()

print(content)

file.close()



# Reading line by line

file = open("example.txt", "r")


for line in file:
    print(line)


file.close()



# Writing multiple lines

file = open("example.txt", "w")


file.write(
    "Python\n"
    "FastAPI\n"
    "Backend Development"
)


file.close()



# Appending data
#
# append does not delete old data.
# It adds new content at the end.


file = open("example.txt", "a")

file.write(
    "\nDatabase"
)


file.close()



# Using with statement
#
# The with statement automatically closes
# the file after finishing.


with open("example.txt", "r") as file:

    content = file.read()

    print(content)



# Reading a specific amount of characters

with open("example.txt") as file:

    content = file.read(10)

    print(content)



# Reading all lines as a list

with open("example.txt") as file:

    lines = file.readlines()

    print(lines)



# Writing a list of strings into a file

languages = [
    "Python\n",
    "Java\n",
    "JavaScript\n"
]


with open("languages.txt", "w") as file:

    file.writelines(languages)



# Checking if a file exists

from pathlib import Path


path = Path("example.txt")


if path.exists():

    print("File exists")

else:

    print("File does not exist")



# Deleting a file

# path.unlink()



# File information

print(path.name)

print(path.stem)

print(path.suffix)

print(path.stat())