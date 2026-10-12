-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 47: Scalar Subqueries in Projection
-- Question: Find department name and total employee count using a scalar subquery in the SELECT projection list.

SELECT d.dept_name,
       (SELECT COUNT(*)
        FROM employees e
        WHERE e.dept_id = d.dept_id) AS employee_count
FROM departments d;
