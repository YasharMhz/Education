# SQLAlchemy From Scratch

My SQLAlchemy learning notes and practice.

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM) that allows Python applications to communicate with relational databases.

## What I Learned

### 1. What is SQLAlchemy?

SQLAlchemy is a Python library used to work with relational databases.

It can be used with databases such as:

* SQLite
* MySQL
* PostgreSQL

Basic structure:

```text
Python
   ↓
SQLAlchemy
   ↓
Database
```

---

## 2. ORM

ORM stands for:

**Object Relational Mapping**

It allows Python classes and objects to represent database tables and rows.

```text
Python                  Database

Class       ───────→    Table
Object      ───────→    Row
Attribute   ───────→    Column
```

Example:

```python
class User(Base):
    __tablename__ = "users"
```

The `User` class represents the `users` database table.

---

## 3. Installation

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

---

## 4. Engine

The Engine is SQLAlchemy's connection point to the database.

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
```

For SQLite:

```text
sqlite:///test.db
```

The database URL tells SQLAlchemy which database to use and where it is located.

---

## 5. DeclarativeBase

SQLAlchemy models inherit from a base class.

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

Models then inherit from `Base`.

```python
class User(Base):
    ...
```

---

## 6. Model

A model is a Python class that represents a database table.

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
```

This represents a table similar to:

```text
users

id | name | age
---|------|----
```

---

## 7. Creating Tables

```python
Base.metadata.create_all(engine)
```

This tells SQLAlchemy to create the tables defined by the models if they do not already exist.

---

## 8. Session

A Session is used to perform database operations.

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    ...
```

The session is used for operations such as:

* Adding data
* Reading data
* Updating data
* Deleting data

---

# CRUD

CRUD stands for:

* Create
* Read
* Update
* Delete

## Create

```python
user = User(name="Ali", age=20)

session.add(user)
session.commit()
```

---

## Create Multiple Records

```python
user1 = User(name="Ali", age=20)
user2 = User(name="Sara", age=25)

session.add_all([user1, user2])
session.commit()
```

---

## Read

Modern SQLAlchemy uses `select()` for queries.

```python
from sqlalchemy import select

users = session.execute(
    select(User)
).scalars().all()
```

Then:

```python
for user in users:
    print(user.id, user.name, user.age)
```

---

## Filtering

```python
users = session.execute(
    select(User).where(User.age == 20)
).scalars().all()
```

This is similar to:

```sql
SELECT * FROM users
WHERE age = 20;
```

---

## Get by Primary Key

```python
user = session.get(User, 1)
```

This gets the user whose primary key is `1`.

---

## Update

```python
user = session.get(User, 1)

if user:
    user.age = 21
    session.commit()
```

---

## Delete

```python
user = session.get(User, 1)

if user:
    session.delete(user)
    session.commit()
```

---
---

# Relationships

## ForeignKey

A Foreign Key connects a column in one table to a column
in another table.

Example:

```python
user_id: Mapped[int] = mapped_column(
    ForeignKey("users.id")
)


# Important SQLAlchemy Concepts

```text
Engine
  ↓
Database connection

Base
  ↓
Parent class for models

Model
  ↓
Represents a database table

Session
  ↓
Performs database operations

Mapped
  ↓
Describes a mapped Python attribute

mapped_column
  ↓
Defines a database column

select()
  ↓
Creates a SELECT query

commit()
  ↓
Saves changes to the database
```

---

# Project Structure

```text
sqlalchemy/
│
├── main.py
├── README.md
└── test.db
```
