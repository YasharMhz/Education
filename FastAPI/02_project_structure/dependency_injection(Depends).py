
# Dependency Injection is a feature that makes FastAPI code cleaner, reusable, and easier to maintain.
# You will use it everywhere in real projects.

# What is a Dependency?
# A dependency is some code that your endpoint needs before it can run.
# Examples:
# Checking if a user is logged in
# Getting a database connection
# Checking permissions
# Validating an API key
# Getting current user information
# Instead of writing the same code in every endpoint, we create a dependency and reuse it.

# The Problem Without Dependencies
# Imagine you have many admin routes:
#
@app.get("/admin/users")
def get_users():
    # check if admin
    pass

@app.delete("/admin/users/{id}")
def delete_user(id: int):
    # check if admin
    pass

@app.put("/admin/settings")
def update_settings():
    # check if admin
    pass
#
# You repeat the same logic:
# if user.is_admin:
#     ...
# else:
#     raise HTTPException(403)
#
# This is bad.
# Solution: Depends
# FastAPI gives us:
# Depends()
# It says:
# "Before running this endpoint, run this function first."

# Simple Example:

from fastapi import FastAPI, Depends

app = FastAPI()


def common_parameters():
    return {
        "message": "Dependency executed"
    }


@app.get("/")
def home(data = Depends(common_parameters)):
    return data
#
# Flow:
# Request
#    |
#    v
# common_parameters()
#    |
#    v
# home()
#    |
#    v
# Response

# Understanding This Line
# data = Depends(common_parameters)
# means:
# "Run common_parameters() and put its result into data."


# Example: Shared Query Parameters
# Imagine many endpoints need pagination:
# ?page=1&limit=10
# Instead of repeating:
# page: int = 1
# limit: int = 10
# Create:
#
from fastapi import Depends

def pagination(
    page: int = 1,
    limit: int = 10
):
    return {
        "page": page,
        "limit": limit
    }
#
# Use it:

@app.get("/users")
def get_users(
    params = Depends(pagination)
):
    return params


@app.get("/products")
def get_products(
    params = Depends(pagination)
):
    return params
#
# Now both endpoints share the same logic.


# Dependency with Parameters
# Dependencies can accept parameters too.
# Example:

def verify_role(role: str):
    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    return True

# Use:

@app.get("/admin")
def admin_access(
    check = Depends(verify_role)
):
    return {
        "message": "Welcome admin"
    }

# yield Dependencies
# Normal function:

def dependency():
    return value

# The function ends immediately.
# With yield:
#
def dependency():

    resource = create()

    yield resource

    cleanup()
# Flow:
# Before yield
#      |
#      v
# Endpoint runs
#      |
#      v
# After yield
#
# Example:
# Open database
#       |
#       v
# Run query
#       |
#       v
# Close database

# Dependency at Router Level
# Instead of adding:
# Depends(auth)
# to every route:
router = APIRouter(
    prefix="/admin",
    dependencies=[
        Depends(auth)
    ]
)
#
# Now every endpoint automatically uses it.
# Example:
@router.get("/users")
def users():
    return []
#
# Behind the scenes:
# auth check
#     |
# users()

# Dependency Chain
# Dependencies can depend on other dependencies.
# Example:
# Endpoint
#    |
#    |
# Current User
#    |
#    |
# JWT Token
#    |
#    |
# Authorization Header
#
# FastAPI automatically resolves the chain.

# Common Uses of Depends
# 1. Authentication
# current_user = Depends(get_current_user)

# 2. Database
# db = Depends(get_db)

# 3. Permissions
# Depends(require_admin)

# 4. Pagination
# Depends(pagination)

# 5. Settings
# Depends(get_settings)


# Practice projects

# from fastapi import FastAPI,Depends,HTTPException,status
#
# app = FastAPI()
#
# def ur_score(score:int):
#     if 50 <= score <= 100:
#         return{
#             "message ":"you are available"
#         }
#     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "you are not available")
#
# @app.post("/score")
# def user_score(
#     score = Depends(ur_score)
# ):return {
#     "score": score
# }

from fastapi import Depends,FastAPI

app = FastAPI(perfix = "client information",dependencies=[Depends(information)])

def information(name:str,age:int,gender:str):
    return {
        "name": name,
        "age": age,
        "gender": gender
    }
@app.get("/users")
def get_users():
    return {
        "message": "Welcome client"
    }

