-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 24: Multi-Condition Filtering
-- Question: Retrieve all active employees (is_active = TRUE) who earn more than 60000.00.

SELECT *
FROM employees
WHERE is_active = TRUE AND salary > 60000.00;
