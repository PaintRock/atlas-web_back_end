-- Create a table 
CREATE TABLE IF NOT EXIST users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL
);