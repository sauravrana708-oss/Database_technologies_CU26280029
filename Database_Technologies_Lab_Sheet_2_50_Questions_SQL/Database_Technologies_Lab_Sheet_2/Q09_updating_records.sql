-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 09: Updating Records
-- Question: Change the status of order 5002 from 'Pending' to 'Shipped'.

UPDATE orders
SET status = 'Shipped'
WHERE order_id = 5002;
