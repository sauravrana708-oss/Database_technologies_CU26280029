-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 32: Subqueries
-- Question: Retrieve all employees who earn more than the average employee salary.

SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
