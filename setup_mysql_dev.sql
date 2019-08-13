-- Prepare a MySQL server.
-- Check if database hbnb_dev_db exists and if not, create it.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Check if user 'hbnb_dev' exists and if not, create them.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Set password for 'hbnb_dev'.
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grant all privileges on 'hbnb_dev_db' to 'hbnb_dev'.
GRANT ALL PRIVILEGES ON `hbnb_dev_db` . * TO 'hbnb_dev'@'localhost';
-- Grant select privileges on 'performance_schema' to 'hbnb_dev'.
GRANT SELECT ON `performance_schema` . * TO 'hbnb_dev'@'localhost';
