-- Q6
-- Create a table system_settings with setting_id (SMALLINT Primary Key), setting_key (VARCHAR 50), and setting_value (VARCHAR 100).

CREATE TABLE system_settings (
    setting_id SMALLINT PRIMARY KEY,
    setting_key VARCHAR(50),
    setting_value VARCHAR(100)
);
