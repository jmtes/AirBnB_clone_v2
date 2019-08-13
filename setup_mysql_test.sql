-- Prepare a MySQL server.
-- Check if database hbnb_test_db exists and if not, create it.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Check if user 'hbnb_test' exists and if not, create them.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Set password for 'hbnb_test'.
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grant all privileges on 'hbnb_test_db' to 'hbnb_test'.
GRANT ALL PRIVILEGES ON `hbnb_test_db` . * TO 'hbnb_test'@'localhost';
-- Grant select privileges on 'performance_schema' to 'hbnb_test'.
GRANT SELECT ON `performance_schema` . * TO 'hbnb_test'@'localhost';
