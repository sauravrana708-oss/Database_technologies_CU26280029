-- Q4
-- Create a table audit_logs storing log_id (Primary Key), action (TEXT), and created_at using TIMESTAMP.

CREATE TABLE audit_logs (
    log_id INT PRIMARY KEY,
    action TEXT,
    created_at TIMESTAMP
);
