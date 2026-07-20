

# Response Models

# The Problem
# Imagine a user in your database:
#
# {
#     "id": 1,
#     "username": "john",
#     "email": "john@gmail.com",
#     "password": "mypassword123",
#     "is_admin": false
# }
#
# If your endpoint returns this directly:
#
# @app.get("/users/{id}")
# def get_user(id: int):
#     return user
#
# The client receives:
#
# {
#     "id": 1,
#     "username": "john",
#     "email": "john@gmail.com",
#     "password": "mypassword123",
#     "is_admin": false
# }
#
# ❌ This is a huge security problem.
#
# Passwords should never be returned.
#
# The Solution: Response Models
#
# Create another Pydantic model for what you want to return.
#
# from pydantic import BaseModel
#
# class UserResponse(BaseModel):
#     id: int
#     username: str
#     email: str
#
# Notice:
#
# No password.
#
# Using response_model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# response_model = It means just return id , username , email
@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    return {
        "id": id,
        "username": "john",
        "email": "john@gmail.com",
        "password": "secret123"
    }
#
# Although the function returns:
#
# {
#     "id": 1,
#     "username": "john",
#     "email": "john@gmail.com",
#     "password": "secret123"
# }
#
# The client receives:
#
# {
#     "id": 1,
#     "username": "john",
#     "email": "john@gmail.com"
# }
#
# FastAPI automatically removes fields that aren't in UserResponse.


# Why Use Response Models?
# They:
# Hide sensitive data
# Validate outgoing data
# Improve Swagger documentation
# Keep responses consistent


# Response Model Example
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float


@app.get("/products/{id}", response_model=Product)
def get_product(id: int):
    return {
        "id": id,
        "name": "Laptop",
        "price": 999.99,
        "stock": 30,
        "supplier": "ABC Company"
    }

# Client receives:
# {
#     "id": 1,
#     "name": "Laptop",
#     "price": 999.99
# }
# stock and supplier are filtered out because they're not in the response model.


# Why Not Use One Model?
# You might think:
class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
# and use it everywhere.
# This is a bad idea because:
# Creating a user requires a password.
# Returning a user should never expose the password.
# Use separate models instead.


# Lists of Objects
# Suppose you return many users.
# users = [
#     {
#         "id": 1,
#         "username": "John",
#         "email": "john@gmail.com"
#     },
#     {
#         "id": 2,
#         "username": "Alice",
#         "email": "alice@gmail.com"
#     }
# ]

# Use:
# from typing import List
# @app.get("/users", response_model=List[UserResponse])
# def get_users():
#     return users

# The response will be:
#
# [
#     {
#         "id": 1,
#         "username": "John",
#         "email": "john@gmail.com"
#     },
#     {
#         "id": 2,
#         "username": "Alice",
#         "email": "alice@gmail.com"
#     }
# ]



# Practice Exercise
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int


class BookResponse(BaseModel):
    id: int
    title: str
    author: str


@app.post("/books", response_model=BookResponse)
def get_book(id:int):
    return{
        "id": id,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "pages": 464
}

