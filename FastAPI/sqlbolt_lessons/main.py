"""
SQLBolt Lessons 1–18
Practice / reference file

This file collects representative solutions and examples from SQLBolt
Lessons 1–18. The examples are written as SQL strings so the file can
be opened as a Python learning/reference file without requiring a
specific database to exist.

Source: https://sqlbolt.com/
"""

# ============================================================
# LESSON 1 — SELECT QUERIES 101
# ============================================================

lesson_1 = [
    "SELECT title FROM movies;",
    "SELECT director FROM movies;",
    "SELECT title, director FROM movies;",
    "SELECT title, year FROM movies;",
    "SELECT * FROM movies;",
]


# ============================================================
# LESSON 2 — QUERIES WITH CONSTRAINTS (PT. 1)
# ============================================================

lesson_2 = [
    "SELECT title FROM movies WHERE year = 2000;",
    "SELECT title FROM movies WHERE year > 2000;",
    "SELECT title FROM movies WHERE year <= 2000;",
    "SELECT title FROM movies WHERE year <> 2000;",
    "SELECT title FROM movies WHERE title != 'Cars';",
]


# ============================================================
# LESSON 3 — QUERIES WITH CONSTRAINTS (PT. 2)
# ============================================================

lesson_3 = [
    "SELECT title FROM movies WHERE year BETWEEN 2000 AND 2010;",
    "SELECT title FROM movies WHERE year NOT BETWEEN 2000 AND 2010;",
    "SELECT title FROM movies WHERE year < 2000 OR year > 2010;",
    "SELECT title FROM movies WHERE title LIKE 'Toy%';",
    "SELECT title FROM movies WHERE title LIKE '%Toy%';",
    "SELECT title FROM movies WHERE director IN ('John Lasseter', 'Pete Docter');",
]


# ============================================================
# LESSON 4 — FILTERING AND SORTING
# ============================================================

lesson_4 = [
    "SELECT title, year FROM movies ORDER BY year ASC;",
    "SELECT title, year FROM movies ORDER BY year DESC;",
    "SELECT title, length_minutes FROM movies ORDER BY length_minutes DESC LIMIT 3;",
    "SELECT title, year FROM movies WHERE year >= 2000 ORDER BY year ASC;",
]


# ============================================================
# LESSON 5 — SIMPLE SELECT REVIEW
# ============================================================

lesson_5 = [
    "SELECT city, population FROM north_american_cities WHERE country = 'Canada';",
    "SELECT city, latitude FROM north_american_cities "
    "WHERE country = 'United States' ORDER BY latitude DESC;",
    "SELECT city, longitude FROM north_american_cities "
    "WHERE longitude < (SELECT longitude FROM north_american_cities WHERE city = 'Chicago') "
    "ORDER BY longitude DESC;",
    "SELECT city, population FROM north_american_cities "
    "WHERE country = 'Mexico' ORDER BY population DESC LIMIT 2;",
    "SELECT city, population FROM north_american_cities "
    "WHERE country = 'United States' ORDER BY population DESC LIMIT 2 OFFSET 2;",
]


# ============================================================
# LESSON 6 — MULTI-TABLE QUERIES WITH JOINs
# ============================================================

lesson_6 = [
    "SELECT movies.title, boxoffice.rating "
    "FROM movies INNER JOIN boxoffice "
    "ON movies.id = boxoffice.movie_id;",

    "SELECT movies.title, boxoffice.domestic_sales, boxoffice.international_sales "
    "FROM movies INNER JOIN boxoffice "
    "ON movies.id = boxoffice.movie_id;",

    "SELECT movies.title, boxoffice.rating "
    "FROM movies JOIN boxoffice "
    "ON movies.id = boxoffice.movie_id "
    "WHERE boxoffice.rating >= 8.0;",
]


# ============================================================
# LESSON 7 — OUTER JOINs
# ============================================================

lesson_7 = [
    "SELECT movies.title, boxoffice.rating "
    "FROM movies LEFT JOIN boxoffice "
    "ON movies.id = boxoffice.movie_id;",

    "SELECT movies.title, boxoffice.rating "
    "FROM movies LEFT JOIN boxoffice "
    "ON movies.id = boxoffice.movie_id "
    "WHERE boxoffice.movie_id IS NULL;",
]


# ============================================================
# LESSON 8 — NULLs
# ============================================================

lesson_8 = [
    "SELECT title FROM movies WHERE director IS NULL;",
    "SELECT title FROM movies WHERE director IS NOT NULL;",
    "SELECT title, director FROM movies "
    "WHERE director IS NULL OR director = '';",
]


# ============================================================
# LESSON 9 — QUERIES WITH EXPRESSIONS
# ============================================================

lesson_9 = [
    "SELECT title, length_minutes * 2 AS double_length FROM movies;",
    "SELECT title, year + 10 AS future_year FROM movies;",
    "SELECT title, length_minutes / 60.0 AS hours FROM movies;",
]


# ============================================================
# LESSON 10 — AGGREGATE FUNCTIONS (PT. 1)
# ============================================================

lesson_10 = [
    "SELECT MAX(year) FROM movies;",
    "SELECT MIN(year) FROM movies;",
    "SELECT AVG(year) FROM movies;",
    "SELECT SUM(length_minutes) FROM movies;",
    "SELECT COUNT(*) FROM movies;",
    "SELECT COUNT(director) FROM movies;",
]


# ============================================================
# LESSON 11 — AGGREGATE FUNCTIONS (PT. 2)
# ============================================================

lesson_11 = [
    "SELECT director, COUNT(*) AS movie_count "
    "FROM movies GROUP BY director;",

    "SELECT director, SUM(length_minutes) AS total_minutes "
    "FROM movies GROUP BY director;",

    "SELECT director, COUNT(*) AS movie_count "
    "FROM movies GROUP BY director HAVING COUNT(*) >= 2;",
]


# ============================================================
# LESSON 12 — ORDER OF EXECUTION
# ============================================================

lesson_12 = """
SELECT director,
       SUM(boxoffice.domestic_sales + boxoffice.international_sales) AS total_sales
FROM movies
JOIN boxoffice
    ON movies.id = boxoffice.movie_id
GROUP BY director
ORDER BY total_sales DESC;
"""

# Conceptual execution order:
# FROM / JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT
# -> ORDER BY -> LIMIT / OFFSET


# ============================================================
# LESSON 13 — INSERTING ROWS
# ============================================================

lesson_13 = [
    "INSERT INTO movies (title, director, year, length_minutes) "
    "VALUES ('Toy Story 4', 'Josh Cooley', 2019, 100);",

    "INSERT INTO boxoffice (movie_id, rating, domestic_sales, international_sales) "
    "VALUES (15, 8.7, 340000000, 270000000);",
]


# ============================================================
# LESSON 14 — UPDATING ROWS
# ============================================================

lesson_14 = [
    "UPDATE movies SET director = 'John Lasseter' "
    "WHERE title = \"A Bug's Life\";",

    "UPDATE movies SET year = 1999 "
    "WHERE title = 'Toy Story 2';",

    "UPDATE movies "
    "SET title = 'Toy Story 3', director = 'Lee Unkrich' "
    "WHERE title = 'Toy Story 8';",
]


# ============================================================
# LESSON 15 — DELETING ROWS
# ============================================================

lesson_15 = [
    "DELETE FROM movies WHERE year < 2000;",
    "DELETE FROM movies WHERE title = 'Toy Story 3';",
    "DELETE FROM movies WHERE director = 'John Lasseter';",
]


# ============================================================
# LESSON 16 — CREATING TABLES
# ============================================================

lesson_16 = """
CREATE TABLE IF NOT EXISTS mytable (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
);
"""


# ============================================================
# LESSON 17 — ALTERING TABLES
# ============================================================

lesson_17 = [
    "ALTER TABLE mytable ADD COLUMN phone TEXT;",
    "ALTER TABLE mytable ADD COLUMN country TEXT DEFAULT 'Unknown';",
]


# ============================================================
# LESSON 18 — DROPPING TABLES
# ============================================================

lesson_18 = [
    "DROP TABLE IF EXISTS movies;",
    "DROP TABLE IF EXISTS boxoffice;",
]


# ============================================================
# QUICK REFERENCE
# ============================================================

quick_reference = """
SELECT      -> retrieve data
WHERE       -> filter rows
AND / OR    -> combine conditions
LIKE        -> pattern matching
IN          -> match one of several values
BETWEEN     -> range filtering
ORDER BY    -> sort results
LIMIT       -> limit number of rows
OFFSET      -> skip rows
JOIN        -> combine related tables
LEFT JOIN   -> keep all rows from the left table
IS NULL     -> find NULL values
COUNT       -> count rows/values
SUM         -> add numeric values
AVG         -> calculate average
MIN / MAX   -> smallest/largest value
GROUP BY    -> create groups for aggregation
HAVING      -> filter groups
INSERT      -> add rows
UPDATE      -> modify rows
DELETE      -> remove rows
CREATE TABLE -> create a table
ALTER TABLE  -> change a table structure
DROP TABLE   -> remove a table and its structure
"""


