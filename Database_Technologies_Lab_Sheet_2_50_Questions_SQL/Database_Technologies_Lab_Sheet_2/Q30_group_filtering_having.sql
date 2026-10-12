-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 30: Group Filtering (HAVING)
-- Question: Display departments that have a total salary expense exceeding 100000.00.

SELECT dept_id, SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
HAVING SUM(salary) > 100000.00;
