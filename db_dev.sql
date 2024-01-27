--Create a database and 3 users and grant them all the permissions.

CREATE DATABASE IF NOT EXISTS sdms_db;
CREATE USER IF NOT EXISTS alphonse@'localhost' IDENTIFIED BY 'admin01';
CREATE USER IF NOT EXISTS aboki@'localhost' IDENTIFIED BY 'admin02';
CREATE USER IF NOT EXISTS richard@'localhost' IDENTIFIED BY 'admin03';

GRANT ALL PRIVILEGES ON sdms_db.* TO alphonse@'localhost';
GRANT ALL PRIVILEGES ON sdms_db.* TO richard@'localhost';
GRANT ALL PRIVILEGES ON sdms_db.* TO aboki@'localhost';

GRANT SELECT ON performance_schema.* TO alphonse@'localhost';
GRANT SELECT ON performance_schema.* TO richard@'localhost';
GRANT SELECT ON performance_schema.* TO aboki@'localhost';

FLUSH PRIVILEGES;