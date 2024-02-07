-- Create a function that divides and returns the first
-- by the second number or 0 if the second number is 0
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE result DECIMAL(10, 2);
    
    -- Check if b is equal to 0
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    
    RETURN result;
END;