-- this is a sql script that creates a user holberton_user on web servers at localhost that allows access to server
-- user has permission to check primary/replica status of the database
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
