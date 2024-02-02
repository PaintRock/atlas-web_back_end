-- Create a table that can be used on any database
CREATE TABLE IF NOT EXISTS 'users' (
    'id' INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    'email' VARCHAR(255) NOT NULL UNIQUE, 
    'name' VARCHAR(255)
);