-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 35: NULL Handling
-- Question: Find all employees whose last_name is NULL (if any exists).

SELECT *
FROM employees
WHERE last_name IS NULL;
