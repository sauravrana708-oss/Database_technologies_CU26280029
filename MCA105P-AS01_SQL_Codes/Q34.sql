-- Q34
-- Change column content in document_store to doc_body while maintaining its LONGTEXT type.

ALTER TABLE document_store RENAME COLUMN content TO doc_body;
