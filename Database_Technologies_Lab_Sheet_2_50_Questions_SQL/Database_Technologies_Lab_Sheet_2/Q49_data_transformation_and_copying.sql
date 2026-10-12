-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 49: Data Transformation & Copying
-- Question: Insert into employees a copy of all employees from department 10 into department 50 with modified IDs (+500).

INSERT INTO employees
    (emp_id, first_name, last_name, dept_id, salary, hire_date, is_active)
SELECT emp_id + 500, first_name, last_name, 50, salary, hire_date, is_active
FROM employees
WHERE dept_id = 10;
