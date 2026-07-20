
# Functions
# This file contains:
# function creation, parameters, return values,
# keyword arguments, default arguments,
# *args, **kwargs, and scope


# -----------------------------
# Creating a Function
# -----------------------------


# A function is a reusable block of code.
# We create functions using the def keyword.


def greet():

    print("hi everyone")


greet()



# -----------------------------
# Function Parameters
# -----------------------------


# Parameters allow us to pass data into functions.


def greet(first_name, last_name):

    print(f"Hi {first_name} {last_name}")


greet("Reza", "Amiri")



# -----------------------------
# Return Values
# -----------------------------


# return sends a value back from the function.


def get_greeting(first_name):

    return f"Hi {first_name}"


message = get_greeting("Reza")


print(message)



# -----------------------------
# Writing Function Result into File
# -----------------------------


def get_greeting(first_name):

    return f"Hi {first_name}"


message = get_greeting("Reza")


file = open("test.txt", "w")


file.write(message)


file.close()



# -----------------------------
# Keyword Arguments
# -----------------------------


# We can specify parameter names when calling a function.
# This makes the code more readable.


def increment(number, by):

    return number + by



print(increment(number=2, by=3))



# -----------------------------
# Default Arguments
# -----------------------------


# We can assign default values to optional parameters.
#
# Important:
# Required parameters must come before optional parameters.


def increment(number, by=2):

    return number + by



# Using default value

print(increment(number=2))


# Using custom value

print(increment(number=2, by=5))



# -----------------------------
# *args
# -----------------------------


# *args allows a function to receive unlimited positional arguments.
#
# The values are stored as a tuple.


def multiply(*numbers):

    total = 1


    for number in numbers:

        total *= number


    return total



print(multiply(1, 2, 3))



# -----------------------------
# **kwargs
# -----------------------------


# **kwargs allows us to receive unlimited keyword arguments.
#
# The values are stored as a dictionary.


def save_user(**user):

    print(user["name"])



save_user(
    id=11,
    name="Ali",
    age=20
)



# -----------------------------
# Scope
# -----------------------------


# Scope means where a variable can be accessed.
#
# Local variable:
# A variable created inside a function.
# It can only be used inside that function.
#
# Global variable:
# A variable created outside functions.
# It can be accessed from different places.


message = "z"


def greet(name):

    message = "a"



def send_email(name):

    message = "b"



print(message)



# The output is:
#
# z
#
# Because the message variables inside functions
# are local variables and cannot affect the global variable.

