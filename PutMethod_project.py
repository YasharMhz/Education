# from pydantic import BaseModel
# from fastapi import FastAPI
#
# class BookUpdate(BaseModel):
#     title: str
#     author: str
#
# app = FastAPI()
#
#
# books = [
#     {"id": 1, "title": "Python", "author": "admin"},
#     {"id": 2, "title": "FastAPI", "author": "client 1"},
#     {"id": 3, "title": "Flask", "author": "client 2"},
#     {"id": 4, "title": "Java", "author": "client 3"},
#     {"id": 5, "title": "CSS", "author": "client 4"},
#     {"id": 6, "title": "JavaScript", "author": "client 5"},
#     {"id": 7, "title": "CSS", "author": "client 6"},
#     {"id": 8, "title": "CSS", "author": "client 7"},
#     {"id": 9, "title": "CSS", "author": "client 8"},
#     {"id": 10, "title": "CSS", "author": "client 9"}
# ]
#
#
#
# @router.put("/books/{book_id}")
# def update_book(book_id:int,book_update:BookUpdate):
#     for book in books:
#         if book["id"] == book_id:
#             book["title"] = book_update.title
#             book["author"] = book_update.author
#             return book
#
#
#     return {"message": "book not found"}
#
#
#
#
