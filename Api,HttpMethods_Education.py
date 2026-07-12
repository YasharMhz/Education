#
#
# from fastapi import FastAPI

#http methods
# | Method | Meaning              | Real-world example  |
# | ------ | -------------------- | ------------------- |
# | GET    | Read data            | View products       |
# | POST   | Create new data      | Register a new user |
# | PUT    | Update existing data | Change your profile |
# | DELETE | Remove data          | Delete a comment    |
#
# Imagine an online store.
#
# You open the products page.
#
# Your app asks:
#
# "Give me all products."
#
# That's a GET request.
#
# Python example:
#
# import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
#
# print(response.json())
#
# Nothing is changed on the server.
#
# You're only reading data.
#
# 2. POST = Create
#
# Now you create a new account.
#
# Your app sends:
#
# Name: Ali
# Email: ali@example.com
# Password: ****
#
# The server creates a new user.
#
# Python:
#
# import requests
#
# data = {
#     "name": "Ali",
#     "email": "ali@example.com"
# }
#
# response = requests.post(
#     "https://example.com/users",
#     json=data
# )
#
# The server stores this new data.
#
# 3. PUT = Update
#
# You change your email.
#
# Before:
#
# Ali
# ali@gmail.com
#
# After:
#
# Ali
# ali123@gmail.com
#
# Your app sends a PUT request to update the existing user.
#
# requests.put(
#     "https://example.com/users/1",
#     json={"email": "ali123@gmail.com"}
# )
# 4. DELETE = Remove
#
# You delete one of your comments.
#
# requests.delete(
#     "https://example.com/comments/5"
# )
#
# The server removes it.


#🔥🔥 You only need to remember one sentence:
# GET reads, POST creates, PUT updates, DELETE removes.



# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {"message": "Hello, World!"}
# Let's understand it one line at a time.
#
# Line 1
# from fastapi import FastAPI
# This imports the FastAPI class.
# Think of it like:
# "I want to use FastAPI in my project."
#
# Line 2
# app = FastAPI()
# This creates your API application.
# Think of it as:
# "I'm creating my server."
#
# Line 3
# @app.get("/")
# This is called a route.
# It means:
# "If someone sends a GET request to /, run the function below."
#
# Line 4
# def home():
#
# This function runs whenever someone visits:
#
# /
# Line 5
# return {"message": "Hello, World!"}
# FastAPI automatically converts this Python dictionary into JSON.
# The client receives:
# {
#     "message": "Hello, World!"
# }
# You didn't have to write any JSON yourself—that's one reason FastAPI is popular.

# Run your API:
#
# In your terminal:
#
# uvicorn Api,HttpMethods:app --reload
#
# Let's break it down:
#
# Api,HttpMethods → the filename (Api,HttpMethods_Education.py)
# app → the variable app = FastAPI()
# --reload → automatically restarts the server whenever you save changes


# @app.get("/books/{book_id}")
#book_id: int = vorodi functione mae ke bayad hatman integer bashe
# def get_book(book_id: int):
#     return {"book_id": book_id}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}

# from fastapi import FastAPI
#
# app = FastAPI()
#
# books = [
#     {"id": 1, "title": "Python Basics"},
#     {"id": 2, "title": "FastAPI Guide"},
#     {"id": 3, "title": "Clean Code"}
# ]
#
# @app.get("/books/{book_id}")
# def read_book(book_id: int):
#     return {"book_id": book_id}



# from fastapi import FastAPI
# app = FastAPI()
#
#books = naghshe data base ro bazi mikone
# books = [
#     {"id": 1, "title": "Python Basics"},
#     {"id": 2, "title": "FastAPI Guide"},
#     {"id": 3, "title": "Clean Code"}
# ]
#
# @app.get("/books/{book_id}")
# def read_book(book_id: int):
#     for book in books:
#yani agar book_id ke be onvane vorodi behet midam ba book["id"] yeki bood book ro return kon
#         if book["id"] == book_id:
#             return book


#ejraye methode post(ezafafe kardane chizi be liste kolie ma)

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# books = []
#
#(BaseModel) = az in estefade mikonim ke fastAPI befahmataesh
#class Book(BaseModel):
#id: int = yani id bayad int bashe
#     id: int
#title: str = yani title bayad str bashe
#     title: str
#
#
# @app.post("/books")
# def create_book(book: Book):
#
#model_dump = az in methord be in dalil estefade mikonim ke vorodi ke ma az karbar migirim be soorate Pydantic
#va ma bayad Pydantic ro be dic tabdil konim va daroon liste asli save konim
#     books.append(book.model_dump())
#     return{
#     "message": "Book added successfully",
#     "book": book
#     }


#ejraye methode delete(hazf kardane chiz az liste asli)
# from fastapi import FastAPI


# books =[
#     {"id" : 1 ,"title" : "python"},
#     {"id" : 2 ,"title" : "json"}
# ]
#
# app = FastAPI()
#
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             books.remove(book)
#             return {"message": "Book deleted successfully"}
#     return {"message": "Book not found"}




#ejraye methode put
# from pydantic import BaseModel
# from fastapi import FastAPI


# class BookUpdate(BaseModel):
#     title: str
#
#
# app = FastAPI()
#
#
# books = [
#     {"id": 1, "title": "Python"},
#     {"id": 2, "title": "FastAPI"},
#     {"id": 3, "title": "Flask"},
#     {"id": 4, "title": "Java"},
#     {"id": 5, "title": "CSS"},
#     {"id": 6, "title": "JavaScript"},
#     {"id": 7, "title": "CSS"},
#     {"id": 8, "title": "CSS"},
#     {"id": 9, "title": "CSS"},
#     {"id": 10, "title": "CSS"}
# ]
#
#
#
# @app.put("/books/{book_id}")
# def update_book(book_id: int, book_update: BookUpdate):
#     for book in books:
#         if book["id"] == book_id:
#             book["title"] = book_update.title
#             return book
#
#     return {"error": "Book not found"}
#
#
#
#

# What is a Router?
#
# Think of a router as a mini FastAPI application.
#
# The whole application:
#
# app = FastAPI()
#
# The books section:
#
# router = APIRouter()
#
# It's like saying:
#
# "I'm creating a small container that will hold all the book endpoints."
#
# Think of a shopping mall
#
# Imagine a shopping mall.
#
# The mall is:
#
# app = FastAPI()
#
# Inside the mall are different stores.
#
# 📚 Book Store
#
# 👕 Clothing Store
#
# 🍔 Food Court
#
# Each store is like a router.
#
# books_router
# users_router
# orders_router
#
# Each one has its own responsibilities.
#
# The mall doesn't know how each store works.
#
# It just contains them.
#
# So what is this?
# router = APIRouter()
#
# It creates an empty router.
#
# At first:
#
# Router
#
# (empty)
#
# Then you add endpoints.
#
# @router.get("/books")
#
# Now the router contains:
#
# Router
#
# GET /books
#
# Then:
#
# @router.post("/books")
#
# Now it contains:
#
# Router
#
# GET /books
# POST /books
#
# The router is simply a collection of related endpoints.
#


# Now the important line
# app.include_router(books.router)
#
# Let's read it like English.
#
# app
#
# means
#
# "My whole application"
#
# include_router(...)
#
# means
#
# "Add this router to my application."
#
# So:
#
# app.include_router(books.router)
#
# means:
#
# "Take all the endpoints inside books.py and make them part of my application."
#
# Visual example
#
# Before this line:
#
# app = FastAPI()
#
# Application:
#
# Application
#
# (no endpoints)
#
# Books router:
#
# Books Router
#
# GET /books
# POST /books
# DELETE /books/{id}
#
# They are separate.
#
# When you write:
#
# app.include_router(books.router)
#
# FastAPI does something like:
#
# Application
#
# GET /books
# POST /books
# DELETE /books/{id}
#
# It copies those routes into the application.
#
# Now the app knows about them.
#
#
