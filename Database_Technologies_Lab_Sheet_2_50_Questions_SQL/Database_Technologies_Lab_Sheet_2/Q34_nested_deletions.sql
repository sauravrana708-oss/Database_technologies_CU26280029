-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 34: Nested Deletions
-- Question: Delete all orders placed by customers who have an order with 'Cancelled' status.

DELETE FROM orders
WHERE customer_name IN (
    SELECT customer_name
    FROM (
        SELECT customer_name
        FROM orders
        WHERE status = 'Cancelled'
    ) AS cancelled_customers
);
