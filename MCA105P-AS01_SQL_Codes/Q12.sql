-- Q12
-- Create a table ticket_orders with ticket_id (Primary Key) and priority_level restricted to ENUM('Low', 'Medium', 'High').

CREATE TABLE ticket_orders (
    ticket_id INT PRIMARY KEY,
    priority_level ENUM('Low', 'Medium', 'High')
);
