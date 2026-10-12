-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 44: Offset & Ranking
-- Question: Find the third highest salary in the employees table using subqueries or OFFSET.

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
