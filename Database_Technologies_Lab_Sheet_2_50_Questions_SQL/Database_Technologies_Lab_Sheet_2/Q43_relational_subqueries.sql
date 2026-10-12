-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 43: Relational Subqueries
-- Question: Display employee details for employees who belong to departments with a budget > 300000.00.

SELECT *
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM departments
    WHERE budget > 300000.00
);
