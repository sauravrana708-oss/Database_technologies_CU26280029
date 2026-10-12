-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 48: Complex Group Filtering
-- Question: List customer names who have placed more than 1 order OR have a total spending sum > 1000.00.

SELECT customer_name
FROM orders
GROUP BY customer_name
HAVING COUNT(*) > 1 OR SUM(total_amount) > 1000.00;
