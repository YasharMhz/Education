
# Modules in Python
#
# A module is a Python file that contains
# functions, classes, and variables.
#
# Modules help us organize our code
# and reuse it in different files.



# Example:
#
# Imagine we have a file called:
#
# sales.py
#
# Inside sales.py:
#
# def calc_tax():
#     pass
#
# def calc_interest():
#     pass
#
#
# We can use these functions
# inside another file by importing them.



# Import specific functions from a module
#
# from module_name import function_name


from sales import calc_interest, calc_tax



calc_interest()

calc_tax()



# Import everything from a module
#
# This imports all functions and variables
# from the module.
#
# It is usually not recommended in large projects
# because it can create naming conflicts.


from sales import *



calc_interest()

calc_tax()



# Import the whole module
#
# This keeps the module namespace clear.


import sales



sales.calc_interest()

sales.calc_tax()



# Example:
#
# Without namespace:
#
# calc_tax()
#
#
# With namespace:
#
# sales.calc_tax()
#
#
# The second approach is clearer
# because we know where the function comes from.



# Importing standard library modules
#
# Python has many built-in modules.


import math


print(math.sqrt(25))



# Importing with an alias
#
# We can rename a module while importing.


import datetime as dt


now = dt.datetime.now()


print(now)