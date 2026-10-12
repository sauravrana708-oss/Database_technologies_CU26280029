-- Q50
-- Write the SQL DDL statements to: (1) Create table application_logs with log_id (BIGINT Primary Key), level (ENUM('DEBUG', 'INFO', 'WARN', 'ERROR')), message (TEXT), execution_time (DOUBLE), and created_at (DATETIME), and (2) Modify the level column to VARCHAR(10).

CREATE TABLE application_logs (
    log_id BIGINT PRIMARY KEY,
    level ENUM('DEBUG', 'INFO', 'WARN', 'ERROR'),
    message TEXT,
    execution_time DOUBLE,
    created_at DATETIME
);

ALTER TABLE application_logs MODIFY COLUMN level VARCHAR(10);
