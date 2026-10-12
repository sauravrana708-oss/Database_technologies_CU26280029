-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 10: Updating Records
-- Question: Increase the budget of department 20 by 20000.00.

UPDATE departments
SET budget = budget + 20000.00
WHERE dept_id = 20;
