-- Q48
-- Modify file_metadata schema in one ALTER statement: Change file_id from INT to BIGINT, alter file_path to TEXT, and drop column checksum.

ALTER TABLE file_metadata
MODIFY COLUMN file_id BIGINT,
MODIFY COLUMN file_path TEXT,
DROP COLUMN checksum;
