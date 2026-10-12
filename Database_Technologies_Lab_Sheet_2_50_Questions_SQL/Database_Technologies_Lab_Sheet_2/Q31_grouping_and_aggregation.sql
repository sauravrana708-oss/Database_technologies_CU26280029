-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 31: Grouping & Aggregation
-- Question: Find maximum and minimum order amounts per order status.

SELECT status, MAX(total_amount) AS max_amount,
       MIN(total_amount) AS min_amount
FROM orders
GROUP BY status;
