
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

#



# from fastapi import FastAPI,Depends
# app = FastAPI()
#
# def Authentication(
#         age :int = 18,
#         name :str = ""
# ):
#     if age < 18 :
#         return(f"{name} your age is not ok")
#     return{
#         "age":age,
#         "name":name
#     }
#
# @app.get("/users",tags=["Users"])
# def read_users(resualt = Depends(Authentication)):
#     return resualt
#
#
# @app.get("/products/{id}",tags=["Products"])
# def read_products(id: int,resualt = Depends(Authentication)):
#     return resualt

# from fastapi import FastAPI, Depends, HTTPException
# app = FastAPI()
#
# def verify_role(role: str):
#     if role != "admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Not allowed"
#         )
#     return True
#
#
#
#
# @app.get("/admin")
# def admin_access(
#     check = Depends(verify_role)
# ):
#     return {
#         "message": "Welcome admin"
#     }
#
#
# @app.get("/users")
# def users(id:int):
#     return id

# from fastapi import FastAPI
# app = FastAPI()
#
#
# students = [
#     "Ali",
#     "Sara",
#     "John",
#     "Mike",
#     "David"
# ]
#
# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     return students[student_id]

# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return user_id


# from fastapi import FastAPI, HTTPException,Depends,status
# app = FastAPI()
#
#
# def verify_role(role: str):
#     if role != "admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Not allowed"
#         )
#
#     return True
#
# # Use:
#
# @app.get("/admin")
# def admin_access(
#     check = Depends(verify_role)
# ):
#     return {
#         "message": "Welcome admin"
#     }


# from fastapi import Depends,FastAPI
# from pydantic import BaseModel
#
# def information(name:str,age:int,gender:str):
#     return {
#         "name": name,
#         "age": age,
#         "gender": gender
#     }
# def information_output(basemodel):
#     return {
#     "name": "123",
#         "age": "233",
#         "gender": "142"
#     }
#
# app = FastAPI(perfix = "client information",dependencies=[Depends(information)])
#
# @app.get("/users",response_model=information_output)
# def get_users():
#     return {
#         "message": "Welcome client"
#     }



from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel

def auth(age:int,id:int,name:str,password:str):
    if age >= 18:
        return {
            "message":"welcome"
        }

    raise HTTPException(status_code=403,detail="You are under 18")


app = FastAPI(perfix = "/client's information",dependencies=[Depends(auth)])


class Person(BaseModel):
    id: int
    name: str


@app.get("/users",response_model=Person)
def info():
    return {
        "id":1,
        "name":"fef",
        "age":18,
        "password":8585
    }


