SQLBolt Lessons 

My SQL learning notes and practice based on the first 18 lessons of
SQLBolt.

The SQLBolt tutorial starts with basic SELECT queries and gradually
moves into filtering, sorting, joins, aggregate functions, modifying
data, and changing table schemas.

Lessons Covered

Lesson

Topic

1

SELECT queries

2

Queries with constraints — Part 1

3

Queries with constraints — Part 2

4

Filtering and sorting

5

Simple SELECT review

6

Multi-table queries with JOINs

7

OUTER JOINs

8

NULL

9

Expressions

10

Aggregate functions — Part 1

11

Aggregate functions — Part 2

12

Query execution order

13

INSERT

14

UPDATE

15

DELETE

16

CREATE TABLE

17

ALTER TABLE

18

DROP TABLE

1. SELECT

SELECT is used to retrieve data from a table.

SELECT title FROM movies;

Select multiple columns:

SELECT title, director FROM movies;

Select every column:

SELECT * FROM movies;

Basic structure:

SELECT columns
FROM table;

2. WHERE

WHERE filters rows.

SELECT title
FROM movies
WHERE year = 2000;

Common comparison operators:

=       equal
<>      not equal
!=      not equal
>       greater than
<       less than
>=      greater than or equal
<=      less than or equal

3. More Constraints

AND

Both conditions must be true.

SELECT title
FROM movies
WHERE year > 2000
  AND length_minutes > 100;

OR

At least one condition must be true.

SELECT title
FROM movies
WHERE year < 2000
   OR year > 2010;

BETWEEN

Checks whether a value is inside a range.

SELECT title
FROM movies
WHERE year BETWEEN 2000 AND 2010;

IN

Checks whether a value matches one of several values.

SELECT title
FROM movies
WHERE director IN ('John Lasseter', 'Pete Docter');

LIKE

Used for pattern matching.

SELECT title
FROM movies
WHERE title LIKE 'Toy%';

% means zero or more characters.

4. Filtering and Sorting

ORDER BY

Sort results.

Ascending:

SELECT title, year
FROM movies
ORDER BY year ASC;

Descending:

SELECT title, year
FROM movies
ORDER BY year DESC;

ASC is ascending and DESC is descending.

LIMIT

Limit the number of returned rows.

SELECT title, year
FROM movies
ORDER BY year DESC
LIMIT 5;

OFFSET

Skip rows.

SELECT title, year
FROM movies
ORDER BY year DESC
LIMIT 5 OFFSET 5;

5. SELECT Review

This lesson combines the previous concepts.

Example:

SELECT city, population
FROM north_american_cities
WHERE country = 'Canada'
ORDER BY population DESC;

A query can combine:

SELECT
FROM
WHERE
ORDER BY
LIMIT
OFFSET

6. JOIN

A JOIN combines related rows from multiple tables.

Example:

SELECT movies.title, boxoffice.rating
FROM movies
JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

The important part is:

ON movies.id = boxoffice.movie_id

This tells SQL how the two tables are related.

Typical relationship:

movies.id
    |
    | matches
    v
boxoffice.movie_id

7. OUTER JOINs

A LEFT JOIN keeps every row from the left table, even if there is no matching row in the right table.

SELECT movies.title, boxoffice.rating
FROM movies
LEFT JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

This is useful when you want to find rows that do not have a match.

For example:

SELECT movies.title
FROM movies
LEFT JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE boxoffice.movie_id IS NULL;

This finds movies without a matching BoxOffice record.

8. NULL

NULL means that a value is missing or unknown.

Do not use:

WHERE director = NULL

Use:

WHERE director IS NULL;

To find values that are not NULL:

WHERE director IS NOT NULL;

9. Expressions

SQL can perform calculations inside queries.

SELECT title, length_minutes * 2 AS double_length
FROM movies;

AS creates an alias for the result.

Example:

SELECT title,
       length_minutes / 60.0 AS hours
FROM movies;

10. Aggregate Functions

Aggregate functions calculate values across multiple rows.

COUNT

Count rows:

SELECT COUNT(*)
FROM movies;

Count non-NULL values in a column:

SELECT COUNT(director)
FROM movies;

SUM

Add numeric values:

SELECT SUM(length_minutes)
FROM movies;

AVG

Calculate an average:

SELECT AVG(length_minutes)
FROM movies;

MIN

Find the smallest value:

SELECT MIN(year)
FROM movies;

MAX

Find the largest value:

SELECT MAX(year)
FROM movies;

11. GROUP BY and HAVING

GROUP BY

GROUP BY creates groups of rows with the same value.

Example:

SELECT director, COUNT(*) AS movie_count
FROM movies
GROUP BY director;

This means:

Put movies with the same director together, then count the movies in each group.

SUM with GROUP BY

SELECT director,
       SUM(length_minutes) AS total_minutes
FROM movies
GROUP BY director;

Here SUM() calculates the total separately for each director.

HAVING

HAVING filters groups after GROUP BY.

SELECT director,
       COUNT(*) AS movie_count
FROM movies
GROUP BY director
HAVING COUNT(*) >= 2;

WHERE vs HAVING

WHERE filters individual rows:

WHERE year > 2000

HAVING filters groups:

HAVING COUNT(*) >= 2

12. Order of Query Execution

A useful conceptual order is:

1. FROM / JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT / OFFSET

For example:

SELECT director,
       SUM(boxoffice.domestic_sales + boxoffice.international_sales)
           AS total_sales
FROM movies
JOIN boxoffice
    ON movies.id = boxoffice.movie_id
GROUP BY director
ORDER BY total_sales DESC;

The database first creates the joined data, then groups it, calculates the selected expressions, and finally sorts the result.

13. INSERT

INSERT adds new rows.

INSERT INTO movies
    (title, director, year, length_minutes)
VALUES
    ('Toy Story 4', 'Josh Cooley', 2019, 100);

You can also insert into specific columns:

INSERT INTO mytable (name, age)
VALUES ('John', 21);

Multiple rows can be inserted:

INSERT INTO mytable (name, age)
VALUES
    ('John', 21),
    ('Sarah', 22);

14. UPDATE

UPDATE changes existing rows.

UPDATE movies
SET director = 'John Lasseter'
WHERE title = "A Bug's Life";

You can update multiple columns:

UPDATE movies
SET title = 'Toy Story 3',
    director = 'Lee Unkrich'
WHERE title = 'Toy Story 8';

Important

Be careful with UPDATE.

This:

UPDATE movies
SET director = 'John Lasseter';

can update every row in the table because there is no WHERE.

A good habit is to test the condition first:

SELECT *
FROM movies
WHERE title = 'Toy Story 2';

Then perform the update.

15. DELETE

DELETE removes rows.

DELETE FROM movies
WHERE title = 'Toy Story 3';

Again, be careful with the WHERE clause.

This:

DELETE FROM movies;

removes all rows from the table.

16. CREATE TABLE

CREATE TABLE creates a new table and defines its schema.

Example:

CREATE TABLE IF NOT EXISTS mytable (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
);

The columns have data types:

id       -> INTEGER
name     -> TEXT
age      -> INTEGER
email    -> TEXT

PRIMARY KEY identifies each row.

17. ALTER TABLE

ALTER TABLE changes an existing table's structure.

For example, add a column:

ALTER TABLE mytable
ADD COLUMN phone TEXT;

You can also provide a default value:

ALTER TABLE mytable
ADD COLUMN country TEXT DEFAULT 'Unknown';

The DEFAULT value is used when a value is not explicitly supplied.

18. DROP TABLE

DROP TABLE removes the table itself, including its structure.

DROP TABLE IF EXISTS movies;

And:

DROP TABLE IF EXISTS boxoffice;

DELETE vs DROP

This difference is very important:

DELETE FROM movies;

removes rows but keeps the table.

DROP TABLE movies;

removes the table itself.

Think of it like:

DELETE
  ↓
table remains
rows disappear


DROP
  ↓
table disappears
rows + table structure disappear

SQL Cheat Sheet

Command

Purpose

SELECT

Retrieve data

FROM

Choose the table

WHERE

Filter rows

AND

Require multiple conditions

OR

Allow alternative conditions

LIKE

Pattern matching

IN

Match values from a list

BETWEEN

Filter a range

ORDER BY

Sort results

LIMIT

Limit results

OFFSET

Skip results

JOIN

Combine tables

LEFT JOIN

Keep all left-table rows

IS NULL

Find missing values

COUNT()

Count

SUM()

Add values

AVG()

Average

MIN()

Minimum

MAX()

Maximum

GROUP BY

Create groups

HAVING

Filter groups

INSERT

Add rows

UPDATE

Modify rows

DELETE

Remove rows

CREATE TABLE

Create a table

ALTER TABLE

Change a table

DROP TABLE

Delete a table