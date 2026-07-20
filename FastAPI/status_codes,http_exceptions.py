from fastapi import  FastAPI

# The status code tells the client whether the request succeeded or failed.

# | Code | Meaning               | When to Use                                 |
# | ---- | --------------------- | ------------------------------------------- |
# | 200  | OK                    | Request succeeded                           |
# | 201  | Created               | Resource created                            |
# | 204  | No Content            | Deleted successfully                        |
# | 400  | Bad Request           | Invalid request                             |
# | 401  | Unauthorized          | Login required                              |
# | 403  | Forbidden             | No permission                               |
# | 404  | Not Found             | Resource doesn't exist                      |
# | 422  | Validation Error      | Invalid request body (FastAPI handles this) |
# | 500  | Internal Server Error | Server-side bug
# |
# You don't need to memorize all of them today. Focus on:
# 200
# 201
# 404
# 422


# Default Status Code
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello"}

# FastAPI automatically returns:
#
# 200 OK
# Returning 201 Created
#
# Creating a resource should return 201.
#
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created"
    }
#
# Response:
#
# 201 Created
#
# Using the status module is clearer than writing numbers directly.
#
# Instead of:
#
# status_code=201
#
# Prefer:
#
# status_code=status.HTTP_201_CREATED
#
# It's easier to read and less error-prone.


# HTTPException
# Suppose someone requests:
# /users/100
# But user 100 doesn't exist.
# Returning:
# {
#     "message": "User not found"
# }
# with status 200 is incorrect because the request actually failed.
# Instead:
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 1,
        "name": "John"
    }

# Request:
# /users/10
# Response:
# 404 Not Found
# {
#     "detail": "User not found"
# }

# How raise Works
# raise HTTPException(...)
# Immediately stops the function.
# Example:
@app.get("/test")
def test():

    print("Before")

    raise HTTPException(
        status_code=404,
        detail="Error"
    )

    print("After")

# Output:
# Before
# "After" is never printed because execution stops when the exception is raised.


# Dynamic Example
# Let's simulate a database.
users = {
    1: "John",
    2: "Alice",
    3: "Bob"
}

# Endpoint:

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user_id,
        "name": users[user_id]
    }

# Request:
# /users/2
# Response:
# {
#     "id": 2,
#     "name": "Alice"
# }

# Request:
# /users/100
# Response:
# 404
# {
#     "detail": "User not found"
# }
# Custom Error Messages
# You can return any message.

# raise HTTPException(
#     status_code=404,
#     detail="Book not found"
# )

# or

# raise HTTPException(
#     status_code=403,
#     detail="You don't have permission"
# )

# or

# raise HTTPException(
#     status_code=401,
#     detail="Invalid username or password"
# )


# Validation Errors (422)
# Remember:
# class User(BaseModel):
#     name: str
#     age: int

# Request:
# {
#     "name": "John",
#     "age": "abc"
# }

# You don't need to write validation code.
# FastAPI automatically returns:
# 422 Unprocessable Entity
# with details explaining what went wrong.
# This is one of the biggest advantages of using Pydantic.


# Multiple Status Codes
# A route can return different status codes depending on the outcome.

@app.get("/users/{id}")
def get_user(id: int):

    if id == 1:
        return {
            "id": 1,
            "name": "John"
        }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

# Possible responses:
# Situation	Status
# User exists	200
# User missing	404


# Combining Everything

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{id}")
def get_user(id: int):

    if id >= len(users):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[id]


# Practice Exercise
# Create a simple in-memory book API:
# books = {
#     1: "Clean Code",
#     2: "Python Crash Course"
# }
# Endpoint 1
# GET /books/{book_id}
# If the ID exists:
# {
#     "id": 1,
#     "title": "Clean Code"
# }
# Otherwise:
# raise HTTPException(
#     status_code=404,
#     detail="Book not found"
# )
# Endpoint 2
# POST /books
# Use:
# status_code=status.HTTP_201_CREATED

from fastapi import  FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()

class Books_form(BaseModel):
    id : int
    title : str


books = {
    1: "Clean Code",
    2: "Python Crash Course",
    3: "Python's basics",
    4: "JavaScript"
}

@app.get("/books/{book_id}")
def read_book(book_id: int):
    if book_id == 1:
        return{
            "id": 1,
            "title": "Clean Code"
        }

    raise HTTPException(status_code=404,detail="Book not found")

@app.post("/books",status_code=status.HTTP_201_CREATED)
def create_book(book: Books_form):
    if book.id in books:
        raise HTTPException(status_code=404,detail="This book is already exist")
    return book

