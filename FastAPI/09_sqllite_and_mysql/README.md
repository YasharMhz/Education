# Database Learning — SQLite & MySQL

This repository contains my notes and practice while learning relational databases with **SQLite** and **MySQL**.

At this stage, MySQL is practiced directly through the terminal. Python-to-MySQL connections will be covered later.

---

## Topics Covered

* Database fundamentals
* Tables
* Rows
* Columns
* Primary keys
* SQLite
* MySQL
* SQL
* CRUD operations
* `CREATE DATABASE`
* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `WHERE`
* `UPDATE`
* `DELETE`
* SQLite database files
* Database connection URLs

---

# 1. Database Fundamentals

A database is used to store and manage data.

A database can contain multiple tables:

```text
Database
│
├── users
├── products
├── orders
└── categories
```

A table contains rows and columns.

Example:

| id | name     | price |
| -: | -------- | ----: |
|  1 | Laptop   |  1000 |
|  2 | Mouse    |    30 |
|  3 | Keyboard |    80 |

### Database

The complete collection of data.

### Table

A collection of related data.

Example:

```text
products
```

### Column

A property of the data.

Examples:

```text
id
name
price
```

### Row

One record in a table.

Example:

```text
1 | Laptop | 1000
```

---

# 2. SQL

SQL stands for:

**Structured Query Language**

SQL is used to communicate with relational databases.

Some important SQL commands are:

```sql
CREATE
INSERT
SELECT
UPDATE
DELETE
```

---

# 3. CRUD

CRUD represents the four basic database operations.

| Operation | SQL Command |
| --------- | ----------- |
| Create    | `INSERT`    |
| Read      | `SELECT`    |
| Update    | `UPDATE`    |
| Delete    | `DELETE`    |

---

# 4. SQLite

SQLite is a lightweight relational database.

Unlike MySQL, SQLite does not require a separate database server.

The database is stored in a file.

For example:

```text
project/
├── sqlite.py
└── test.db
```

The `test.db` file is the SQLite database.

Python includes the `sqlite3` module, so it can be used without installing a separate Python database driver.

---

## SQLite Connection

```python
import sqlite3

connection = sqlite3.connect("test.db")
```

If `test.db` doesn't exist, SQLite creates it.

---

## Creating a SQLite Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)
""")
```

This creates a table called `products`.

The table contains:

```text
id
name
price
```

---

## SQLite Primary Key

```sql
id INTEGER PRIMARY KEY
```

The primary key uniquely identifies each row.

Example:

```text
id | name
---|----------
1  | Laptop
2  | Mouse
3  | Keyboard
```

---

## SQLite INSERT

```python
cursor.execute("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", ("Laptop", 1000))
```

The `?` characters are parameter placeholders used by SQLite's Python API.

---

## SQLite SELECT

Select everything:

```sql
SELECT * FROM products;
```

Select specific columns:

```sql
SELECT name, price FROM products;
```

---

## SQLite WHERE

`WHERE` filters rows.

Example:

```sql
SELECT * FROM products
WHERE price > 50;
```

This returns products whose price is greater than 50.

---

## SQLite UPDATE

```sql
UPDATE products
SET price = 1200
WHERE id = 1;
```

This changes the price of the product with ID `1`.

---

## SQLite DELETE

```sql
DELETE FROM products
WHERE id = 2;
```

This deletes the product with ID `2`.

---

# 5. SQLite Database URL

When using SQLAlchemy later, a SQLite database can be represented with:

```text
sqlite:///test.db
```

For example:

```python
DATABASE_URL = "sqlite:///test.db"
```

This means that `test.db` is located relative to the current working directory.

For an absolute Linux path, the format uses four slashes:

```text
sqlite:////home/user/project/test.db
```

The database URL will become more important when learning SQLAlchemy.

---

# 6. MySQL

MySQL is a relational database management system.

Unlike SQLite, MySQL normally runs as a database server.

The basic architecture is:

```text
Application
     ↓
MySQL Server
     ↓
Database
     ↓
Tables
     ↓
Rows
```

At this stage, MySQL is being practiced directly through the terminal.

Python integration will be covered later.

---

# 7. Starting MySQL

On Ubuntu, MySQL can be accessed from the terminal with:

```bash
sudo mysql
```

After entering MySQL, the prompt looks like:

```text
mysql>
```

---

# 8. Creating a MySQL Database

Create a database:

```sql
CREATE DATABASE shop;
```

View available databases:

```sql
SHOW DATABASES;
```

Select the database:

```sql
USE shop;
```

---

# 9. Creating a MySQL Table

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price INT
);
```

The table contains:

```text
id
name
price
```

---

## MySQL `AUTO_INCREMENT`

```sql
id INT PRIMARY KEY AUTO_INCREMENT
```

`AUTO_INCREMENT` tells MySQL to automatically generate a new ID when inserting a row.

For example:

```text
1 → Laptop
2 → Mouse
3 → Keyboard
```

You don't need to manually provide the IDs.

---

# 10. MySQL INSERT

Insert a product:

```sql
INSERT INTO products (name, price)
VALUES ('Laptop', 1000);
```

Insert another:

```sql
INSERT INTO products (name, price)
VALUES ('Mouse', 30);
```

Insert another:

```sql
INSERT INTO products (name, price)
VALUES ('Keyboard', 80);
```

---

# 11. MySQL SELECT

Select everything:

```sql
SELECT * FROM products;
```

Select specific columns:

```sql
SELECT name, price
FROM products;
```

---

# 12. MySQL WHERE

`WHERE` filters rows.

Example:

```sql
SELECT * FROM products
WHERE price > 50;
```

Another example:

```sql
SELECT * FROM products
WHERE id = 1;
```

---

# 13. MySQL UPDATE

Update a product:

```sql
UPDATE products
SET price = 1200
WHERE id = 1;
```

The `WHERE` clause is important.

Without `WHERE`:

```sql
UPDATE products
SET price = 1200;
```

every product would be updated.

---

# 14. MySQL DELETE

Delete a product:

```sql
DELETE FROM products
WHERE id = 2;
```

Again, `WHERE` is important.

Without it:

```sql
DELETE FROM products;
```

all rows in the table would be deleted.

---

# 15. SQLite vs MySQL

| Feature                 | SQLite            | MySQL                  |
| ----------------------- | ----------------- | ---------------------- |
| Type                    | Embedded database | Database server        |
| Server required         | No                | Yes                    |
| Storage                 | Database file     | Server-managed         |
| Python module           | `sqlite3`         | Python driver required |
| Default port            | None              | `3306`                 |
| Setup                   | Very simple       | More setup             |
| Good for learning       | Yes               | Yes                    |
| Multi-user applications | Limited           | Better suited          |

---

# 16. SQLite vs MySQL Architecture

### SQLite

```text
Python
  ↓
sqlite3
  ↓
SQLite
  ↓
test.db
```

### MySQL

```text
Application
  ↓
MySQL Server
  ↓
shop
  ↓
products
```

Later, when Python-to-MySQL integration is learned, the architecture will become:

```text
Python
  ↓
MySQL Python Driver
  ↓
MySQL Server
  ↓
Database
```

---

# 17. Database URLs

A database URL describes how an application connects to a database.

A general SQLAlchemy URL looks like:

```text
dialect+driver://username:password@host:port/database
```

SQLite:

```text
sqlite:///test.db
```

MySQL will later use a format such as:

```text
mysql+driver://username:password@host:port/database
```

The exact driver and Python connection process will be covered later.

---

# 18. Current Project Structure

```text
09_sqllite_and_mysql/
│
├── sqlite.py
└── README.md
```

MySQL commands are currently documented in `README.md` and executed directly in the MySQL terminal.

Later, when Python-to-MySQL connections are learned, a `mysql.py` file can be added.



