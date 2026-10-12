-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 20: Basic Aggregation
-- Question: Calculate the average total_amount of all orders.

SELECT AVG(total_amount) AS average_order_amount
FROM orders;
