# 🚦 FastAPI Middleware & CORS

This lesson covers two important concepts when building FastAPI applications:

* **Middleware**
* **CORS (Cross-Origin Resource Sharing)**

---

# 🔹 What is Middleware?

Imagine your API is a restaurant.

Every request must pass through a door before reaching your endpoint.

That door is called **Middleware**.

```text
Client
  │
  ▼
🚪 Middleware
  │
  ▼
FastAPI Endpoint
  │
  ▼
Database
```

Likewise, every response leaves through the same door.

```text
Request
   │
   ▼
Middleware
   │
   ▼
Endpoint
   │
   ▲
Middleware
   │
   ▲
Response
```

Middleware sits between the client and your application.

---

# 🛠️ What Can Middleware Do?

Middleware can be used for many common tasks:

* 🔐 Check authentication
* 📝 Log requests
* ⏱️ Measure request time
* 📋 Add response headers
* 📦 Compress responses
* 🌐 Handle CORS
* 🚦 Rate limiting
* And many more...

---

# ❌ Without Middleware

Without middleware, a request goes directly to the endpoint:

```text
Request
   │
   ▼
Endpoint
   │
   ▼
Response
```

Example:

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

This is simple, but it becomes repetitive when you need to perform the same operation for many endpoints.

---

# ✅ With Middleware

With middleware, every request first passes through the middleware:

```text
Request
   │
   ▼
Middleware
   │
   ▼
Endpoint
   │
   ▲
Middleware
   │
   ▲
Response
```

Now we can execute common logic before and after the endpoint.

---

# ❓ Why Use Middleware?

Suppose your API has 100 endpoints:

```text
/users
/products
/orders
/login
/register
/profile
...
```

You want to print:

```text
New Request
```

every time someone calls your API.

## ❌ Bad Approach

You could manually add the logging code to every endpoint:

```python
@app.get("/users")
def users():
    print("New Request")


@app.get("/products")
def products():
    print("New Request")


@app.get("/orders")
def orders():
    print("New Request")
```

With 100 endpoints:

```text
100 endpoints
      ↓
100 repeated print statements
      ↓
Not maintainable
```

---

## ✅ Middleware Solves This

Instead of repeating the same code, we can create one middleware:

```python
@app.middleware("http")
async def log_request(request, call_next):
    print("New Request")

    response = await call_next(request)

    return response
```

Now every request automatically passes through this middleware.

---

# 🧱 Middleware Structure

The basic FastAPI middleware structure is:

```python
@app.middleware("http")
async def my_middleware(request, call_next):

    # Before endpoint

    response = await call_next(request)

    # After endpoint

    return response
```

Remember this structure:

```text
Before
   │
   ▼
Endpoint
   │
   ▼
After
```

The middleware can execute code:

1. Before the endpoint
2. While passing control to the endpoint
3. After the endpoint returns a response

---

# 🔍 Understanding `call_next`

`call_next` is one of the most confusing parts of middleware for beginners.

Suppose your endpoint is:

```python
@app.get("/")
async def home():
    return {"message": "Hello"}
```

And your middleware is:

```python
@app.middleware("http")
async def middleware(request, call_next):

    print("Before")

    response = await call_next(request)

    print("After")

    return response
```

When you visit `/`, the execution order is:

```text
Before
   ↓
Endpoint executes
   ↓
After
```

### What does `await call_next(request)` mean?

Think of it as:

> "FastAPI, continue processing this request and call the appropriate next handler."

In a simple application, this eventually leads to the endpoint being executed.

---

# ⚠️ What Happens Without `call_next`?

If you write:

```python
@app.middleware("http")
async def middleware(request, call_next):
    print("Before")
```

the request does not continue through the application because you never call:

```python
await call_next(request)
```

The usual pattern is:

```python
response = await call_next(request)

return response
```

This allows the request to continue and gives the middleware access to the response.

---

# 💻 Middleware Example

```python
from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def middleware(request, call_next):

    print("Request Started")

    response = await call_next(request)

    print("Request Finished")

    return response


@app.get("/")
async def home():

    print("Inside Endpoint")

    return {"message": "Hello"}
```

### Console Output

```text
Request Started
Inside Endpoint
Request Finished
```

This shows the exact execution order:

```text
Middleware
    │
    │ Request Started
    ▼
Endpoint
    │
    │ Inside Endpoint
    ▼
Middleware
    │
    │ Request Finished
    ▼
Response
```

---

# ⏱️ Real Example: Measure Request Time

One common use case for middleware is measuring how long a request takes.

```python
import time

from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def timer(request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()

    print(end - start)

    return response
```

Example output:

```text
0.0321
```

This means the request took approximately:

```text
0.0321 seconds
```

or about:

```text
32 milliseconds
```

---

# 📋 Add a Custom Response Header

Middleware can also modify the response before sending it back to the client.

For example, we can add a custom header containing the request processing time:

```python
import time

from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def timer(request, call_next):

    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    response.headers["X-Process-Time"] = str(process_time)

    return response
```

The response headers will contain something like:

```text
X-Process-Time: 0.0314
```

This can be useful for debugging and monitoring API performance.

---

# 🔄 Request Lifecycle

A more complete view of the request lifecycle looks like this:

```text
Client
  │
  ▼
Middleware
  │
  ▼
Authentication?
  │
  ▼
Endpoint
  │
  ▼
Database
  │
  ▲
Endpoint
  │
  ▲
Middleware
  │
  ▲
Client
```

The middleware can therefore perform operations before and after the endpoint.

---

# 🌐 What is CORS?

Now let's look at **CORS**, one of the most common issues when building web APIs.

Imagine this setup:

```text
Frontend
http://localhost:3000

        │
        │ HTTP Request
        ▼

Backend
http://localhost:8000
```

The frontend tries to call:

```javascript
fetch("http://localhost:8000/users")
```

The browser may respond with an error such as:

```text
Blocked by CORS policy
```

Why?

---

# 🌍 What is an Origin?

An **origin** consists of three parts:

```text
Protocol + Domain + Port
```

For example:

```text
http://localhost:3000
```

contains:

```text
Protocol → http
Domain   → localhost
Port     → 3000
```

---

## Different Origins

These are different origins:

```text
http://localhost:3000
http://localhost:8000
```

because their ports are different.

These are also different origins:

```text
http://example.com
https://example.com
```

because their protocols are different.

---

# 🔐 Why Do Browsers Block Cross-Origin Requests?

Browsers protect users from potentially malicious websites.

Imagine you are logged into your bank account.

A malicious website could potentially try to send requests to your bank using your browser session.

To reduce this risk, browsers enforce the **Same-Origin Policy**.

By default, a web page cannot freely access resources from a different origin.

**CORS (Cross-Origin Resource Sharing)** provides a mechanism for the server to declare which cross-origin requests are allowed.

---

# ⚙️ How FastAPI Enables CORS

FastAPI provides `CORSMiddleware` for configuring CORS.

First, import it:

```python
from fastapi.middleware.cors import CORSMiddleware
```

Then add the middleware:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Now the browser can allow cross-origin requests from:

```text
http://localhost:3000
```

---

# ⚙️ Understanding CORS Options

## `allow_origins`

Defines which origins are allowed to make cross-origin requests.

```python
allow_origins=[
    "http://localhost:3000"
]
```

You can specify multiple origins:

```python
allow_origins=[
    "http://localhost:3000",
    "https://example.com"
]
```

---

## `allow_methods`

Defines which HTTP methods are allowed.

Allow all methods:

```python
allow_methods=["*"]
```

Or specify individual methods:

```python
allow_methods=["GET", "POST"]
```

---

## `allow_headers`

Defines which request headers are allowed.

Allow all headers:

```python
allow_headers=["*"]
```

Or specify individual headers:

```python
allow_headers=["Content-Type", "Authorization"]
```

---

## `allow_credentials`

Controls whether browsers may include credentials such as cookies or HTTP authentication information in cross-origin requests.

```python
allow_credentials=True
```

### Important

When using:

```python
allow_credentials=True
```

you should use specific origins instead of allowing every origin with:

```python
allow_origins=["*"]
```

---

# 💻 Complete CORS Example

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


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


@app.get("/")
async def home():
    return {"message": "Hello"}
```

Now:

```text
http://localhost:3000
```

is an allowed origin.

Other origins are not included in the server's CORS policy.

---

# 🆚 Middleware vs CORS

| Middleware                                                     | CORS                                                              |
| -------------------------------------------------------------- | ----------------------------------------------------------------- |
| A general mechanism for processing requests and responses.     | A specific mechanism for controlling cross-origin browser access. |
| You can create your own middleware.                            | FastAPI provides `CORSMiddleware`.                                |
| Can be used for logging, timing, authentication, headers, etc. | Used to configure cross-origin browser requests.                  |
| Can run before and after the endpoint.                         | Adds CORS-related behavior and response headers.                  |

CORS itself is implemented using middleware in FastAPI:

```python
app.add_middleware(
    CORSMiddleware,
    ...
)
```

---

# 📚 Summary

By the end of this lesson, you should understand:

* ✅ What middleware is and why it is useful.
* ✅ The request → middleware → endpoint → middleware → response flow.
* ✅ How `call_next(request)` passes the request to the next part of the application.
* ✅ How middleware can measure request time.
* ✅ How middleware can add custom response headers.
* ✅ What an origin is.
* ✅ Why browsers enforce the Same-Origin Policy.
* ✅ What CORS is.
* ✅ How to configure `CORSMiddleware` in FastAPI.
* ✅ What `allow_origins`, `allow_methods`, `allow_headers`, and `allow_credentials` do.
