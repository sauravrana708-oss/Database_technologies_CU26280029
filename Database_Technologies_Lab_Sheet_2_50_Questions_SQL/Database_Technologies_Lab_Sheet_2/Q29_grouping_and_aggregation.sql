-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 29: Grouping & Aggregation
-- Question: Find the total number of employees in each department.

SELECT dept_id, COUNT(*) AS employee_count
FROM employees
GROUP BY dept_id;
