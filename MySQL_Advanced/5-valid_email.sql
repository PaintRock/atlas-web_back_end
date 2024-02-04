-- trigger to reset the valid_email when email has changed
DELIMETER |
CREATE TRIGGER _update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
|