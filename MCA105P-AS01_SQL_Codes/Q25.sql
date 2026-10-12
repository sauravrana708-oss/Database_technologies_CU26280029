-- Q25
-- Given table inventory with columns warehouse_id (INT) and sku (VARCHAR 20), write an ALTER statement to add a composite primary key to both columns.

ALTER TABLE inventory ADD PRIMARY KEY (warehouse_id, sku);
