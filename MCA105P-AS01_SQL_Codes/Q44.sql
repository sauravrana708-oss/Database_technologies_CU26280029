-- Q44
-- You have a table raw_data with column temp_val (VARCHAR 50). In a single ALTER command, rename column temp_val to converted_val, change its type to DECIMAL(6,3), and add column processed_at (TIMESTAMP) right after it.

ALTER TABLE raw_data
CHANGE COLUMN temp_val converted_val DECIMAL(6,3),
ADD COLUMN processed_at TIMESTAMP AFTER converted_val;
