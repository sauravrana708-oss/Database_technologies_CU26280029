-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 45: Conditional Updates (CASE)
-- Question: Update employees: Increase salary by 10% if salary < 60000, else increase by 5% using a CASE expression.

UPDATE employees
SET salary = CASE
    WHEN salary < 60000 THEN salary * 1.10
    ELSE salary * 1.05
END;
