-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 42: Group Aggregations & Subqueries
-- Question: Find departments where average employee salary is greater than the global average employee salary.

SELECT dept_id, AVG(salary) AS average_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
