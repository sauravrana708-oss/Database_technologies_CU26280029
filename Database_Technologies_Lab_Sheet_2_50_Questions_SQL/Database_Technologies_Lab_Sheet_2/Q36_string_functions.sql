-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 36: String Functions
-- Question: Display full names of employees by concatenating first_name and last_name with a space.

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;
