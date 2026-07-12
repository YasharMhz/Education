
# Path Parameters in FastAPI
# @app.get("/books/{book_id}")
# book_id: int means the input parameter
# must be an integer.

from fastapi import FastAPI

app = FastAPI()


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# Path Parameters in FastAPI
# @app.get("/books/{book_id}")
# book_id: int means the input parameter
# must be an integer.

from fastapi import FastAPI

app = FastAPI()


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# POST Method
# POST is used to add new data to our collection.
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


books = []


# BaseModel helps FastAPI understand
# the structure of incoming data.
class Book(BaseModel):
    id: int
    title: str


@app.post("/books")
def create_book(book: Book):

    # Convert Pydantic object into a dictionary
    # and save it inside the list.
    books.append(book.model_dump())

    return {
        "message": "Book added successfully",
        "book": book
    }


# DELETE Method
# DELETE removes an item from our data collection.
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
from pydantic import BaseModel
from fastapi import FastAPI


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


# What is a Router?
# Think of a router as a mini FastAPI application.
# The whole application:
# app = FastAPI()
# A specific section:
# router = APIRouter()
# A router is a container that holds
# related endpoints.
# Example:
# Shopping Mall:
# app = FastAPI()
# Stores:
# books_router
# users_router
# orders_router
# Each router has its own responsibility.
# The main application only combines them together.


# Creating an empty router:
# router = APIRouter()


# Adding endpoints:
# @router.get("/books")
# Router now contains:
# GET /books
# @router.post("/books")
# Router now contains:
# GET /books
# POST /books


# The router is simply a collection
# of related endpoints.


# app.include_router(books.router)
# Meaning:
# "Add all endpoints from books router
# into the main FastAPI application."


# Before:
# Application:
# app = FastAPI()
# No book endpoints exist yet.
# Books Router:
# GET /books
# POST /books
# DELETE /books/{id}

# After:
# app.include_router(books.router)
# Application:
# GET /books
# POST /books
# DELETE /books/{id}
# Now FastAPI knows these routes.


