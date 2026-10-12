-- Q27
-- Add a column middle_name (VARCHAR 30) to employees specifically positioned right after given_name.

ALTER TABLE employees ADD COLUMN middle_name VARCHAR(30) AFTER given_name;
