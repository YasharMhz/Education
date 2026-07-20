# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class UserResponse(BaseModel):
#     id: int
#     username: str
#     email: str
#
#
# @app.get("/users/{id}", response_model=UserResponse)
# def get_user(id: int):
#     return {
#         "id": id,
#         "username": "john",
#         "email": "john@gmail.com",
#         "password": "secret123"
#     }
# from http.client import HTTPException

# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
#
# class BookCreate(BaseModel):
#     title: str
#     author: str
#     pages: int
#
#
# class BookResponse(BaseModel):
#     id: int
#     title: str
#     author: str
#
#
# @app.post("/books", response_model=BookResponse)
# def get_book(id:int):
#     return{
#         "id": id,
#     "title": "Clean Code",
#     "author": "Robert C. Martin",
#     "pages": 464
#     }

# from fastapi import  FastAPI
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {"message": "Hello"}


# from fastapi import FastAPI, status
#
# app = FastAPI()
#
# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "message": "User created"
#     }



