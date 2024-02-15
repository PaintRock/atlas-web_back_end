-- Create need_meeting 
DELIMITER //
CREATE VIEW need_meeting AS
SELECT name, score, IFNULL(last_meeting, 1) AS ISNULL_last_meeting
FROM students
WHERE (score < 80 OR last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
END;
//