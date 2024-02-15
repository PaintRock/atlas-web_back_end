-- Create need_meeting 
DELIMITER //
CREATE VIEW need_meeting AS
SELECT name 
FROM students
WHERE score < 80 
OR last_meeting NOT NULL
OR last_meeting (NOW() - 1 month));
END;
//