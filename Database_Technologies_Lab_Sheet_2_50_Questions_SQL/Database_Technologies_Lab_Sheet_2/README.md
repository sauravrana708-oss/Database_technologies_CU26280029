# Database Technologies — Lab Sheet 2 (MCA105P)

This folder contains one `.sql` file for each of the 50 questions from Database Technologies Lab Sheet 2.

## Contents
- `Q01_...sql` through `Q50_...sql`
- Every file contains the full question as an SQL comment followed by its SQL answer.
- The queries are written for MySQL.

## Reference tables
The lab sheet uses these tables:
- `employees`
- `departments`
- `orders`

See the original Lab Sheet 2 PDF for the reference sample datasets and column definitions.

## How to use
1. Open MySQL Workbench or your SQL editor.
2. Select the database containing the `employees`, `departments`, and `orders` tables.
3. Open the required question's `.sql` file.
4. Run the query.

## Important notes
- Some questions modify or delete records. Use a practice database and reset the sample data when needed.
- Q01, Q02, Q03, Q21, and Q49 use example IDs; change them if those IDs already exist.
- Q34 uses a derived-table subquery for compatibility with MySQL's target-table restrictions.
- Q44 returns the third distinct-highest salary.
