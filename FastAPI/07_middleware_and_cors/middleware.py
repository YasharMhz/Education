from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time


app = FastAPI()


# =============================
# Basic Middleware
# =============================

@app.middleware("http")
async def log_requests(request: Request, call_next):

    # Before endpoint
    print("Request Started")

    response = await call_next(request)

    # After endpoint
    print("Request Finished")

    return response


# =============================
# Measure Request Time
# =============================

@app.middleware("http")
async def timer(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    print(f"Process time: {process_time:.4f} seconds")

    return response


# =============================
# Add Custom Response Header
# =============================

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    response.headers["X-Process-Time"] = str(process_time)

    return response


# =============================
# CORS
# =============================

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =============================
# Endpoint
# =============================

@app.get("/")
async def home():

    print("Inside Endpoint")

    return {"message": "Hello"}


# =============================
# Small Exercise
# =============================

# Create a FastAPI app with:
#
# 1. A custom middleware that prints:
#    "Request started" before the endpoint.
#    "Request finished" after the endpoint.
#
# 2. A GET /hello endpoint that returns:
#    {"message": "Hello FastAPI"}
#
# 3. CORS that only allows:
#    http://localhost:3000
#
# Try to solve the exercise yourself before
# checking the solution.


# =============================
# Exercise Solution
# =============================

from fastapi import FastAPI,middleware,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def middleware(request: Request,call_next):
    print("Request started")
    response = await call_next(request)
    print("Request finished")
    return response


@app.get("/hello")
async def hello():
    return {"message":"hello fastapi"}

