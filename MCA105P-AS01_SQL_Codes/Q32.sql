-- Q32
-- Convert start_date column in table projects to project_year with data type YEAR using a single DDL statement.

ALTER TABLE projects CHANGE COLUMN start_date project_year YEAR;
