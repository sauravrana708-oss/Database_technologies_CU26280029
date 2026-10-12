-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 14: Range Filtering
-- Question: Retrieve all orders placed between '2024-01-15' and '2024-01-20'.

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-01-15' AND '2024-01-20';
