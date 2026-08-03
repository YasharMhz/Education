# 🌍 Environment Variables in FastAPI

This guide explains how to manage application configuration using **Environment Variables**, **`.env` files**, and **Pydantic Settings** in FastAPI.

---

# 📌 Before You Start

If you're using a virtual environment, activate it first:

```bash
source .venv/bin/activate
```

---

# 🤔 What Are Environment Variables?

Environment variables are configuration values stored **outside your application code**.

Instead of writing sensitive information directly in your source code, your application reads those values when it starts.

For example:

Your code only knows the variable name:

```text
DATABASE_URL
```

The actual value is stored in a `.env` file or provided by the operating system:

```env
DATABASE_URL=postgresql://localhost/mydb
```

---

# ❓ Why Do We Need Environment Variables?

Different environments require different configurations.

### Development

```env
DATABASE_URL=sqlite:///dev.db
```

### Production

```env
DATABASE_URL=postgresql://production-server/mydb
```

Without environment variables, you would need to edit your source code every time you deploy your application.

---

# 📦 Install `pydantic-settings`

```bash
pip install pydantic-settings
```

---

# 📁 Project Structure

```text
app/
│
├── main.py
├── config.py
└── .env
```

---

# 📝 Create a `.env` File

Example:

```env
APP_NAME=My FastAPI App
DEBUG=True
DATABASE_URL=sqlite:///database.db
SECRET_KEY=my-secret-key
```

---

# ⚙️ Create the Settings Class

**config.py**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

---

# 🔍 Understanding the Settings Class

`Settings` is similar to a Pydantic `BaseModel`.

Instead of validating API request data, it validates your application's configuration.

```python
class Settings(BaseSettings):
```

This tells Pydantic to read configuration values from your environment.

---

# 📂 What Does `env_file = ".env"` Mean?

```python
class Config:
    env_file = ".env"
```

This tells Pydantic:

> Read all configuration values from the `.env` file.

---

# 🚀 Using Settings in FastAPI

**main.py**

```python
from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def home():
    return {
        "app": settings.app_name,
        "debug": settings.debug
    }
```

Response:

```json
{
    "app": "My FastAPI App",
    "debug": true
}
```

---

# ❌ Why Not Hardcode Configuration?

### Bad Practice

```python
DATABASE_URL = "something"
SECRET_KEY = "secret"
```

Problems:

* Anyone can see your secrets.
* Changing environments becomes difficult.
* Sensitive information may accidentally be committed to GitHub.

---

### Better Practice

```python
settings.database_url
settings.secret_key
```

Configuration stays in one place and is easy to manage.

---

# 🏗 Professional Project Structure

```text
app/
│
├── main.py
│
├── core/
│   └── config.py
│
├── routers/
│   ├── users.py
│   └── auth.py
│
├── database.py
│
└── .env
```

Configuration files are usually placed inside:

```text
core/config.py
```

---

# 🌐 Environment Variables in Production

Never upload your `.env` file to GitHub.

Add it to your `.gitignore` file:

```gitignore
.env
```

Instead, production servers provide environment variables.

### Linux

```bash
export DATABASE_URL="postgresql://server/db"
```

### Docker

```yaml
environment:
  DATABASE_URL: postgres://server/db
```

Cloud providers also offer built-in environment variable management.

---

# 🛠 Adding Default Values

You can define default values inside your settings class.

```python
class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = False
```

Now, if these variables are missing from `.env`, Pydantic will use the default values automatically.

---

# 🔐 Example: Authentication Settings

Authentication usually requires values like:

```env
SECRET_KEY=random-long-string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

You can access them like this:

```python
settings.secret_key
settings.algorithm
```

---

# ⚡ Cache Your Settings

Instead of creating a new `Settings` object every time:

```python
settings = Settings()
```

Use `lru_cache`:

```python
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
```

### Why?

Without caching:

```text
Request 1 → Read .env
Request 2 → Read .env
Request 3 → Read .env
```

With caching:

```text
Application Starts
        │
Read .env Once
        │
Reuse Settings
```

This improves performance.

---

# 💉 Using Settings with Dependency Injection

FastAPI works very well with dependency injection.

```python
from fastapi import Depends

@app.get("/")
def home(settings=Depends(get_settings)):
    return {
        "name": settings.app_name
    }
```

Now your configuration is injected like any other FastAPI dependency.

---

# 🗄 Example: Database Configuration

### `.env`

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=admin
DATABASE_PASSWORD=password
DATABASE_NAME=mydb
```

### `config.py`

```python
class Settings(BaseSettings):

    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str

    class Config:
        env_file = ".env"
```

Now your database credentials are no longer hardcoded inside your application.

---

# ❌ Common Mistakes

### Hardcoding Secrets

```python
SECRET_KEY = "123456"
```

Never store secrets inside your source code.

---

### Uploading `.env` to GitHub

Never do this:

```text
github/
│
└── .env
```

Always add `.env` to your `.gitignore`.

---

### Scattering Configuration

Bad:

```python
# users.py

DATABASE_URL = "..."
```

Better:

```python
from core.config import settings
```

Keep all configuration in one place.

---

# 📚 Practice Exercise

Create the following project structure and configure FastAPI using environment variables.

```text
app/
│
├── main.py
├── config.py
└── .env
```

Try to:

* Create a `.env` file.
* Build a `Settings` class.
* Read variables from `.env`.
* Use `Depends(get_settings)` in an endpoint.
* Add `.env` to `.gitignore`.

---

# ✅ Summary

In this lesson, you learned:

* What environment variables are.
* Why `.env` files are important.
* How to use `pydantic-settings`.
* How to build a `Settings` class.
* How to inject settings using `Depends`.
* How to cache configuration with `lru_cache`.
* Best practices for production.
* Common mistakes to avoid.
