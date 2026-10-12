-- Q30
-- Create a table device_logs with log_id (BIGINT Primary Key), ip_address (VARCHAR 45), and payload (LONGBLOB).

CREATE TABLE device_logs (
    log_id BIGINT PRIMARY KEY,
    ip_address VARCHAR(45),
    payload LONGBLOB
);
