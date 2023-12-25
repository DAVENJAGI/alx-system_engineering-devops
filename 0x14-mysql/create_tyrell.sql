-- Create a database named tyrell_corp. Within the tyrell_corp database creates a table named nexus6 and adds at least one entry to it.
-- Adds select permissions to hoberton_user.

CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 ( id INT PRIMARY KEY, first_name VARCHAR(25), last_name VARCHAR(25), SSN int(25));
GRANT SELECT ON tyrell_corp.nexus6 to 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
