-- Q37
-- Create a table financial_ledger with entry_id (BIGINT Primary Key), debit (DECIMAL 15,4), and credit (DECIMAL 15,4).

CREATE TABLE financial_ledger (
    entry_id BIGINT PRIMARY KEY,
    debit DECIMAL(15,4),
    credit DECIMAL(15,4)
);
