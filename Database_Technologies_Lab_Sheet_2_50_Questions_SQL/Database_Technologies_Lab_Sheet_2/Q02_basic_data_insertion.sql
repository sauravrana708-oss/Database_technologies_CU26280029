-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 02: Basic Data Insertion
-- Question: Insert a new department 'Quality Assurance' located in 'Building B' with a budget of 250000.00 into departments, setting dept_id to 60.

INSERT INTO departments (dept_id, dept_name, location, budget)
VALUES (60, 'Quality Assurance', 'Building B', 250000.00);
