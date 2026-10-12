-- Q24
-- In the table employees, drop column email and change salary data type to DECIMAL(12,2) in a single ALTER statement.

ALTER TABLE employees
DROP COLUMN email,
MODIFY COLUMN salary DECIMAL(12,2);
