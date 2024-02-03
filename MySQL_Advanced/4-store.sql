-- Create a trigger to decrease item quantity after adding a new order
CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the ordered item in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;
