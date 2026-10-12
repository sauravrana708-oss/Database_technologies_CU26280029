-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 15: Set Filtering
-- Question: Display all departments located in either 'Building A' or 'Building B'.

SELECT *
FROM departments
WHERE location IN ('Building A', 'Building B');
