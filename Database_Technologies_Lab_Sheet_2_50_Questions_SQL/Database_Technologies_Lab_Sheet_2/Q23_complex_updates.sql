-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 23: Complex Updates
-- Question: Deactivate (set is_active = FALSE) all employees hired before '2021-01-01'.

UPDATE employees
SET is_active = FALSE
WHERE hire_date < '2021-01-01';
