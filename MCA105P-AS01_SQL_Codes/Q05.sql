-- Q5
-- Write a DDL query to create a table products with product_id (Primary Key), product_name (VARCHAR 50), and is_available using BOOLEAN.

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    is_available BOOLEAN
);
