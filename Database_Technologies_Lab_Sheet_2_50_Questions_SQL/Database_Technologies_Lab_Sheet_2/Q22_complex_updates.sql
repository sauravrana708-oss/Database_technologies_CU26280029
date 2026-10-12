-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 22: Complex Updates
-- Question: Give a 10% salary raise to all employees working in department 10.

UPDATE employees
SET salary = salary * 1.10
WHERE dept_id = 10;
