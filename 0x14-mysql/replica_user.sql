-- create the name of a user called, replica_user, host name set to %, and password should be as I like.
-- replica_user should have appropriate permissions to replicate the primary MySQL seerver.
-- Grant select privileges to holberton_user on mysql.user.

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY '  ';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'replica_user'@'%';
FLUSH PRIVILEGES;
