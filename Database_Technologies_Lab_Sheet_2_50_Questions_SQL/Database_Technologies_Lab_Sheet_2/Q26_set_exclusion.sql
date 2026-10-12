-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 26: Set Exclusion
-- Question: List all employees who do NOT belong to departments 10 or 30.

SELECT *
FROM employees
WHERE dept_id NOT IN (10, 30);
