-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 33: Subqueries
-- Question: Find all employees who work in departments located in 'Building A'.

SELECT *
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE location = 'Building A'
);
