-- Q38
-- Add transaction_date (DATETIME) as the absolute first column in the financial_ledger table using ALTER.

ALTER TABLE financial_ledger ADD COLUMN transaction_date DATETIME FIRST;
