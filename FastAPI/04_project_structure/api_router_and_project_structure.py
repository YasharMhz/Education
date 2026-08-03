#
#
# Imagine you have a large application with:
# Users
# Products
# Orders
# Authentication
# Payments
#
# If everything is inside one file:
# main.py
# Eventually it becomes:
# 3000+ lines 😱
# That's why FastAPI provides APIRouter.
#
# What is APIRouter?
# Think of APIRouter as a mini FastAPI application.
# Instead of putting every route in main.py, you group related routes.
# Example:
# Users routes
#     |
#     +--> GET /users
#     +--> POST /users
#     +--> PUT /users/{id}
#
# Products routes
#     |
#     +--> GET /products
#     +--> POST /products
#
# Auth routes
#     |
#     +--> POST /login
#     +--> POST /register
#
# Each group lives in its own file.


# Step 2: Create a Router
# users.py

# from fastapi import APIRouter
# router = APIRouter()
# @router.get("/")
# def get_users():
#     return {"users": []}
#
# @router.post("/")
# def create_user():
#     return {"message": "User created"}
#
# Notice:
# We don't write:
# app = FastAPI()
# Instead:
# router = APIRouter()

# Step 3: Include Router in main.py

# from fastapi import FastAPI
# from routers.users import router
#
# app = FastAPI()
#
#app.include_router(router) = means all routers define for router add to app
# app.include_router(router)
#

# Now the routes from users.py become part of your application.
# What Happens?
# When someone requests:
# GET /
# FastAPI looks inside the router and finds:
# @router.get("/")

# Problem
# Both Users and Products would use:
# "/"
# That creates conflicts.
# Router Prefix
# Use a prefix.
#
# from fastapi import APIRouter
#
# router = APIRouter(
#     prefix="/users"
# )
#
# Now:
# @router.get("/")
# becomes:
# GET /users
# and
# @router.post("/")
# becomes:
# POST /users
# Much cleaner.
# Complete Example:
# users.py

# from fastapi import APIRouter
#
# router = APIRouter(prefix="/users")
#
#
# @router.get("/")
# def get_users():
#     return {"message": "All users"}
#
#
# @router.get("/{user_id}")
# def get_user(user_id: int):
#     return {"id": user_id}
# main.py
# from fastapi import FastAPI
# from routers.users import router
#
# app = FastAPI()
#
# app.include_router(router)
#
# Available endpoints:
# GET /users
# GET /users/10

# Multiple Routers:
# products.py

# from fastapi import APIRouter
#
# router = APIRouter(prefix="/products")
#
#
# @router.get("/")
# def get_products():
#     return {"products": []}
# main.py
# from fastapi import FastAPI
#
# from routers.users import router as users_router
# from routers.products import router as products_router
#
# app = FastAPI()
#
# app.include_router(users_router)
# app.include_router(products_router)
#
# Now you have:
# GET /users
# GET /products

# Tags:
# Swagger groups routes by tags.
#tags = organized all end point for example book = get , post someting like that (in fastapi site)
#
# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )
#
# Swagger UI:
# Users
# -------
# GET /users
# POST /users
#
# Products
# ---------
# GET /products
# POST /products
#
# Much nicer than one long list.
# Router-Level Responses
# You can define common settings once.
#
# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )
#
# Every route inherits those settings.
#
# Why Use Routers?
# Instead of:
# main.py
#
# GET users
# POST users
# DELETE users
#
# GET products
# POST products
# DELETE products
#
# GET login
# POST login
#
# GET orders
# POST orders
#
# ...
#
# You organize by feature:
# routers/
# users.py
# products.py
# orders.py
# auth.py
#
# Finding code becomes much easier.
# Production Project Structure
#
# As your application grows, you'll typically organize it like this:
# app/
# │
# ├── main.py          # Entry point
# │
# ├── routers/
# │   ├── users.py
# │   ├── auth.py
# │   ├── products.py
# │   └── orders.py
# │
# ├── schemas/
# │   ├── user.py
# │   ├── product.py
# │   └── order.py
# │
# ├── models/
# │   ├── user.py
# │   └── product.py
# │
# ├── services/
# │   ├── user_service.py
# │   └── auth_service.py
# │
# ├── database.py
# │
# └── config.py