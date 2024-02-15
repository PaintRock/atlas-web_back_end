-- Create need_meeting 
DELIMITER //
CREATE VIEW need_meeting AS
SELECT name 
FROM students
WHERE score < 80 
AND last_meeting NULL
OR last_meeting (CURDATE() - 1 month);
END;
//