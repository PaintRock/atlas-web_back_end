-- Create need_meeting 
DELIMITER //
CREATE VIEW need_meeting AS
SELECT name 
FROM students
WHERE score < 80 
AND last_meeting IS NULL
OR (last_meeting < (CURRENT_DATE() - 1 month));
END;
//