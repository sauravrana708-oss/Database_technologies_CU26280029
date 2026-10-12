-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 41: Advanced Subqueries & DML
-- Question: Increase salary by 15% for employees working in the department with the highest budget.

UPDATE employees
SET salary = salary * 1.15
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    ORDER BY budget DESC
    LIMIT 1
);
