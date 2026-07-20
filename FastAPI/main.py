
# FastAPI Basics
# Let's understand it one line at a time.

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello, World!"
    }


# Explanation:
# from fastapi import FastAPI
# This imports the FastAPI class.
# It allows us to create a FastAPI application.
# app = FastAPI()
# This creates our API application.
# Think of it as creating our server.
# @app.get("/")
# This is a route decorator.
# It means:
# "When someone sends a GET request to /,
# run the function below."
#
# def home():
# This function runs whenever someone visits:
# /
# return {"message": "Hello, World!"}
# FastAPI automatically converts
# this Python dictionary into JSON.
# Client receives:
# {
#     "message": "Hello, World!"
# }


# Running FastAPI
# Terminal command:
# uvicorn Api,HttpMethods:app --reload
# Explanation:
# Api,HttpMethods
# means the Python file name.
# app
# means:
# app = FastAPI()
# --reload
# automatically restarts the server
# when you save changes.



# Path Parameters
# @app.get("/books/{book_id}")
# book_id: int means that
# the function input must be an integer.


from fastapi import FastAPI


app = FastAPI()


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {
        "book_id": book_id
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


# Reading data using Path Parameters
# The books list works like a simple database.
# We search inside the list.
# If the received book_id matches the book id,
# we return that book.


from fastapi import FastAPI


app = FastAPI()


books = [
    {"id": 1, "title": "Python Basics"},
    {"id": 2, "title": "FastAPI Guide"},
    {"id": 3, "title": "Clean Code"}
]


@app.get("/books/{book_id}")
def read_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book


# POST Method
# POST is used to add new data
# to our collection.

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


books = []


# BaseModel helps FastAPI understand
# the structure of incoming data.
# It also validates the data type.
class Book(BaseModel):
    id: int
    title: str


@app.post("/books")
def create_book(book: Book):

    # model_dump() converts the Pydantic model
    # into a Python dictionary.
    # Then we can store it inside our list.
    books.append(book.model_dump())

    return {
        "message": "Book added successfully",
        "book": book
    }


# DELETE Method
# DELETE is used to remove data
# from our collection.
from fastapi import FastAPI


books = [
    {"id": 1, "title": "python"},
    {"id": 2, "title": "json"}
]


app = FastAPI()


@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }


    return {
        "message": "Book not found"
    }



# PUT Method
# PUT is used to update existing data.
from fastapi import FastAPI
from pydantic import BaseModel


class BookUpdate(BaseModel):
    title: str


app = FastAPI()


books = [
    {"id": 1, "title": "Python"},
    {"id": 2, "title": "FastAPI"},
    {"id": 3, "title": "Flask"},
    {"id": 4, "title": "Java"},
    {"id": 5, "title": "CSS"}
]


@app.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):

    for book in books:

        if book["id"] == book_id:

            book["title"] = book_update.title

            return book


    return {
        "error": "Book not found"
    }

#Put Project
from pydantic import BaseModel
from fastapi import FastAPI
# Pydantic model for updating a book.
# It defines the structure and data types
# that the client should send.
class BookUpdate(BaseModel):
    title: str
    author: str


app = FastAPI()


# This list works like a simple database.
books = [
    {"id": 1, "title": "Python", "author": "admin"},
    {"id": 2, "title": "FastAPI", "author": "client 1"},
    {"id": 3, "title": "Flask", "author": "client 2"},
    {"id": 4, "title": "Java", "author": "client 3"},
    {"id": 5, "title": "CSS", "author": "client 4"},
    {"id": 6, "title": "JavaScript", "author": "client 5"},
    {"id": 7, "title": "CSS", "author": "client 6"},
    {"id": 8, "title": "CSS", "author": "client 7"},
    {"id": 9, "title": "CSS", "author": "client 8"},
    {"id": 10, "title": "CSS", "author": "client 9"}
]


@app.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):

    for book in books:

        if book["id"] == book_id:

            book["title"] = book_update.title
            book["author"] = book_update.author

            return book


    return {
        "message": "Book not found"
    }

# What is a Router?
# Think of a router as a mini FastAPI application.
# Main application:
# app = FastAPI()
# A specific section:
# router = APIRouter()
# A router is a container that stores
# related endpoints.

# Think of a shopping mall.
# The mall:
# app = FastAPI()
# Inside the mall:
# 📚 Book Store
# 👕 Clothing Store
# 🍔 Food Court
# Each store is like a router.
# books_router
# users_router
# orders_router
# Each router has its own responsibility.
# The main application only combines them.

# Creating a router:
# router = APIRouter()
# At first:
# Router
# (empty)
# Add endpoint:
# @router.get("/books")
# Now:
# Router
# GET /books
# Add another endpoint:
# @router.post("/books")
# Now:
# Router
# GET /books
# POST /books
# A router is simply a collection
# of related endpoints.


# app.include_router(books.router)
# Meaning:
# Add all endpoints from the books router
# into the main FastAPI application.


# Before:
# Main Application:
# app = FastAPI()
# No book endpoints exist yet.
# Books Router:
# GET /books
# POST /books
# DELETE /books/{id}
# They are separate.

# After:
# app.include_router(books.router)
# Main Application:
# GET /books
# POST /books
# DELETE /books/{id}
# Now FastAPI recognizes these routes
# and can handle incoming requests.

