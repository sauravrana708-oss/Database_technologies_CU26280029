-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 46: Correlated Subqueries & DML
-- Question: Delete employees who are inactive (is_active = FALSE) AND earn less than their department's average salary.

DELETE FROM employees
WHERE is_active = FALSE
  AND salary < (
      SELECT avg_salary
      FROM (
          SELECT dept_id, AVG(salary) AS avg_salary
          FROM employees
          GROUP BY dept_id
      ) AS dept_avg
      WHERE dept_avg.dept_id = employees.dept_id
  );
