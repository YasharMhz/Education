
# Exceptions in Python
#
# Exceptions are errors that happen during program execution.
#
# They can stop our program if we don't handle them.
#
# Example:
#
# numbers = [1, 2, 3]
# print(numbers[5])
#
# This causes IndexError.


# Handling exceptions using try and except

try:
    age = int(input("Enter your age: "))
    print(age)

except ValueError as ex:
    print(ex)
    print("You entered an invalid value")


# Multiple exceptions

try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("Invalid input")


# else block
#
# else runs only when no exception happens.

try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("Invalid input")

else:
    print("No exception was thrown")



# finally block
#
# finally always executes.
#
# Usually used for cleanup operations
# like closing files or releasing resources.


try:
    file = open("content.txt")

    age = int(input("Enter your age: "))
    xfactor = 10 / age


except (ValueError, ZeroDivisionError):
    print("Invalid input")


finally:
    file.close()



# Using with statement
#
# The with statement automatically closes resources.
#
# We don't need finally manually.

try:

    with open("content.txt") as file:
        print("File opened successfully")

    age = int(input("Enter your age: "))
    xfactor = 10 / age


except (ValueError, ZeroDivisionError):
    print("Invalid input")



# Creating custom exceptions
#
# We can create our own exception classes
# by inheriting from Exception.


class InvalidOperationError(Exception):
    pass



def calculate_xfactor(age):

    if age <= 0:
        raise InvalidOperationError(
            "Age cannot be zero or negative"
        )

    return 10 / age



try:

    calculate_xfactor(0)


except InvalidOperationError as ex:

    print(ex)



# Exception vs returning None
#
# Exceptions are more expensive because
# Python has to create and handle an error object.
#
# For large applications, avoid using exceptions
# for normal program flow.


from timeit import timeit


code1 = """

def calculate_xfactor(age):

    if age <= 0:
        raise ValueError("Invalid age")

    return 10 / age


try:
    calculate_xfactor(10)

except ValueError:
    pass

"""


code2 = """

def calculate_xfactor(age):

    if age <= 0:
        return None

    return 10 / age


result = calculate_xfactor(10)

if result is None:
    pass

"""


print(
    "Code 1:",
    timeit(code1, number=10000)
)


print(
    "Code 2:",
    timeit(code2, number=10000)
)