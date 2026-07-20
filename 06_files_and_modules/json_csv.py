
# Working with JSON and CSV files in Python
#
# JSON and CSV are common formats
# used for storing and exchanging data.


# ==========================
# Working with JSON
# ==========================


import json
from pathlib import Path



# Python object (list of dictionaries)

users = [
    {
        "id": 1,
        "name": "Pedram",
        "age": 27
    },

    {
        "id": 2,
        "name": "Reza",
        "age": 30
    },

    {
        "id": 3,
        "name": "Nahid",
        "age": 25
    }
]



# Converting Python object to JSON
#
# json.dumps()
# converts Python objects into JSON string.


data = json.dumps(users)


print(data)



# Saving JSON data into a file

Path("users.json").write_text(data)



# Reading JSON from file


data = Path("users.json").read_text()


print(data)



# Converting JSON string back to Python object
#
# json.loads()
# converts JSON into Python objects.


users = json.loads(data)


print(users)


print(type(users))



# Accessing JSON data

for user in users:

    print(user["name"])



# ==========================
# Working with CSV files
# ==========================


import csv



# Writing data into CSV file


with open(
    "users.csv",
    "w",
    newline=""
) as csvfile:


    writer = csv.writer(csvfile)


    writer.writerow(
        [
            "id",
            "name",
            "phone"
        ]
    )


    writer.writerow(
        [
            1,
            "Ali",
            "333"
        ]
    )


    writer.writerow(
        [
            2,
            "Mehdi",
            "444"
        ]
    )


    writer.writerow(
        [
            3,
            "Sepehr",
            "555"
        ]
    )



# Reading CSV file


with open("users.csv") as file:


    reader = csv.reader(file)


    for row in reader:

        print(row)