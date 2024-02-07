-- script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
DELIMITER //
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 ANd last_meeting is NULL or 
last_meeting DATE_SUB(CURRENT_DATE(), last_meeting) > 30);
