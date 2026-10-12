-- Q23
-- Modify the employees table to add two new columns in a single DDL statement: hire_date (DATE) and is_active (BOOLEAN).

ALTER TABLE employees
ADD COLUMN hire_date DATE,
ADD COLUMN is_active BOOLEAN;
