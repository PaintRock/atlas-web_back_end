-- Create a trigger to decrease item quantity after adding a new order
CREATE TRIGGER order_decrease
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the ordered item in the items table
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
