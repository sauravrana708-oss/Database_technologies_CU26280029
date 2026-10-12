-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 03: Basic Data Insertion
-- Question: Insert a new order for customer 'Delta Retail' dated '2024-01-28' worth 2100.00 with status 'Pending' into orders.

INSERT INTO orders (order_id, customer_name, order_date, total_amount, status)
VALUES (5006, 'Delta Retail', '2024-01-28', 2100.00, 'Pending');
