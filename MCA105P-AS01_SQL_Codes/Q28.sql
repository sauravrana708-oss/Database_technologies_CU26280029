-- Q28
-- Create a table geolocations with location_id (INT Primary Key), latitude (DECIMAL 9,6), and longitude (DECIMAL 9,6).

CREATE TABLE geolocations (
    location_id INT PRIMARY KEY,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);
