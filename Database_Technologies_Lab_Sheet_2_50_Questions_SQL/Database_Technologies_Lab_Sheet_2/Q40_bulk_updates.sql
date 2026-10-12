-- Database Technologies Lab Sheet 2
-- Course Code: MCA105P
-- Question 40: Bulk Updates
-- Question: Update all orders with amount under 200.00 to have status 'Cancelled'.

UPDATE orders
SET status = 'Cancelled'
WHERE total_amount < 200.00;
