-- Create need_meeting 
DELIMITER //
CREATE VIEW need_meeting
FROM names AS students
WHERE score < 80 
AND last_meeting NOT NULL
OR last_meeting (NOW() - 1 month);
END;
//