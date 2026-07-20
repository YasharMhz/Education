
# Working with file paths using pathlib
#
# pathlib is a built-in Python module
# for working with file and directory paths.
#
# It provides an object-oriented way
# instead of using normal strings.



from pathlib import Path



# Creating a Path object


path = Path("ecommerce/__init__.py")



# Checking if path exists


print(path.exists())



# Checking if path is a file


print(path.is_file())



# Checking if path is a directory


print(path.is_dir())



# Getting file information


# Full file name

print(path.name)



# File name without extension

print(path.stem)



# File extension

print(path.suffix)



# Parent directory

print(path.parent)



# Absolute path

print(path.absolute())



# Creating a new path


path2 = path.with_name("file.txt")

print(path2)



path3 = path.with_suffix(".txt")

print(path3)



# Creating a directory


# folder = Path("ecommerce2")
# folder.mkdir()



# Removing a directory


# folder = Path("ecommerce2")
# folder.rmdir()



# Renaming a file or directory


# folder = Path("ecommerce2")
# folder.rename("ecommerce")



# Listing files and directories


path = Path("ecommerce")


for item in path.iterdir():

    print(item)



# Finding files with specific extension


py_files = [
    p for p in path.glob("*.py")
]


print(py_files)



# Searching recursively inside folders
#
# rglob searches inside all subdirectories.


all_python_files = [
    p for p in path.rglob("*.py")
]


print(all_python_files)



# Deleting a file


# file = Path("test.txt")
# file.unlink()



# Getting file statistics


file = Path("ecommerce/__init__.py")


print(file.stat())



# Copying files using shutil


import shutil



source = Path("ecommerce/__init__.py")


target = Path("copy_init.py")



# shutil.copy(source, target)