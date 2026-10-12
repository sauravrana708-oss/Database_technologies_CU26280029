-- Q16
-- Add a composite primary key to an existing table student_courses using columns student_id (INT) and course_id (INT).

ALTER TABLE student_courses
ADD PRIMARY KEY (student_id, course_id);
