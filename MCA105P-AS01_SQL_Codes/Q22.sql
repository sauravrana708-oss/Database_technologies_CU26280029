-- Q22
-- Create a table event_schedules with event_id (INT), venue_id (INT), event_date (DATE), and duration_hours (TINYINT). Make event_id and venue_id the composite primary key.

CREATE TABLE event_schedules (
    event_id INT,
    venue_id INT,
    event_date DATE,
    duration_hours TINYINT,
    PRIMARY KEY (event_id, venue_id)
);
