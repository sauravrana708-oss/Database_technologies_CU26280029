-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 37: Ordering & Limits
-- Question: Retrieve the top 3 highest-paid employees.

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
