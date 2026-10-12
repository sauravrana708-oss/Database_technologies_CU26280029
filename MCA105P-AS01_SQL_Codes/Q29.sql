-- Q29
-- Create a table user_accounts with user_id (BIGINT Primary Key), account_type (ENUM('Standard', 'Premium', 'Admin')), and created_timestamp (TIMESTAMP).

CREATE TABLE user_accounts (
    user_id BIGINT PRIMARY KEY,
    account_type ENUM('Standard', 'Premium', 'Admin'),
    created_timestamp TIMESTAMP
);
