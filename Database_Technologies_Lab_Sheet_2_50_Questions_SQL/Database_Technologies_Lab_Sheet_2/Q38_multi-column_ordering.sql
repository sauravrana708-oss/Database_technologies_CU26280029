-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 38: Multi-Column Ordering
-- Question: List employees sorted by department ID ascending, then by salary descending.

SELECT *
FROM employees
ORDER BY dept_id ASC, salary DESC;
