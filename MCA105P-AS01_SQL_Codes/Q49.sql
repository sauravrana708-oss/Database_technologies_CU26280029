-- Q49
-- Write the SQL DDL statements to: (1) Create a table sensor_readings with composite PK (sensor_id INT, recorded_at TIMESTAMP) and column reading (FLOAT), and (2) Rename sensor_readings to historical_sensor_readings.

CREATE TABLE sensor_readings (
    sensor_id INT,
    recorded_at TIMESTAMP,
    reading FLOAT,
    PRIMARY KEY (sensor_id, recorded_at)
);

RENAME TABLE sensor_readings TO historical_sensor_readings;
