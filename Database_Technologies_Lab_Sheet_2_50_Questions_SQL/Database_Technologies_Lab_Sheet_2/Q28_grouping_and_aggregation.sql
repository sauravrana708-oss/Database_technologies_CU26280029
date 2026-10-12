-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 28: Grouping & Aggregation
-- Question: Calculate total salary expenditure for each department.

SELECT dept_id, SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id;
