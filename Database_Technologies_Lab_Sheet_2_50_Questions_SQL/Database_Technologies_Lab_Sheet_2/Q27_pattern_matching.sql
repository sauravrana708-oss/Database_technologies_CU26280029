-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 27: Pattern Matching
-- Question: Find all employees whose first_name contains the letter 'a' (case-insensitive).

SELECT *
FROM employees
WHERE LOWER(first_name) LIKE '%a%';
