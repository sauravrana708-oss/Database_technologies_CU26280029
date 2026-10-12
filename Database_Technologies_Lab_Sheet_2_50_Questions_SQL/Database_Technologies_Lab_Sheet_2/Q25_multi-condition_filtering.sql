-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 25: Multi-Condition Filtering
-- Question: Find orders that are either 'Cancelled' OR have a total_amount greater than 2000.00.

SELECT *
FROM orders
WHERE status = 'Cancelled' OR total_amount > 2000.00;
