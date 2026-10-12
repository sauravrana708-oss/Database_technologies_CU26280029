-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 16: Pattern Matching
-- Question: Find all employees whose last_name starts with the letter 'S'.

SELECT *
FROM employees
WHERE last_name LIKE 'S%';
