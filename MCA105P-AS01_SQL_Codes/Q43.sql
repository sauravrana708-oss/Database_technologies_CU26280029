-- Q43
-- Redesign existing table clients in a single ALTER statement: drop its current primary key, add region_code (CHAR 3), and set (client_id, region_code) as the new composite primary key.

ALTER TABLE clients
DROP PRIMARY KEY,
ADD COLUMN region_code CHAR(3),
ADD PRIMARY KEY (client_id, region_code);
