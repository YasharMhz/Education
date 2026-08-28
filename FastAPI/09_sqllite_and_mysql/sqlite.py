import sqlite3

# Connect to SQLite database

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

# Create a table

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER
)
""")

# Insert data

cursor.execute("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", ("Laptop", 1000))

cursor.execute("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", ("Mouse", 30))

cursor.execute("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", ("Keyboard", 80))

# Save changes

connection.commit()

# Read all products

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

print("All products:")

for product in products:
    print(product)

# Read specific columns

cursor.execute("SELECT name, price FROM products")

products = cursor.fetchall()

print("\nProduct names and prices:")

for product in products:
    print(product)

# Use WHERE

cursor.execute("""
SELECT * FROM products
WHERE price > 50
""")

products = cursor.fetchall()

print("\nProducts with price greater than 50:")

for product in products:
    print(product)

# Update a product

cursor.execute("""
UPDATE products
SET price = ?
WHERE id = ?
""", (1200, 1))

connection.commit()

# Delete a product

cursor.execute("""
DELETE FROM products
WHERE id = ?
""", (2,))

connection.commit()

# Show final data

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

print("\nFinal products:")

for product in products:
    print(product)

# Close the connection

connection.close()
