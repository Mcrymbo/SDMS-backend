/*Create a database and 3 users and grant them all the permissions. */

CREATE DATABASE IF NOT EXISTS sdms_db;
USE sdms_db;
CREATE USER IF NOT EXISTS alphonse@'localhost' IDENTIFIED BY 'sdms_pwd';
CREATE USER IF NOT EXISTS aboki@'localhost' IDENTIFIED BY 'sdms_pwd';
CREATE USER IF NOT EXISTS richard@'localhost' IDENTIFIED BY 'sdms_pwd';

GRANT ALL PRIVILEGES ON sdms_db.* TO alphonce@'localhost';
GRANT ALL PRIVILEGES ON sdms_db.* TO richard@'localhost';
GRANT ALL PRIVILEGES ON sdms_db.* TO aboki@'localhost';

GRANT SELECT ON performance_schema.* TO alphonce@'localhost';
GRANT SELECT ON performance_schema.* TO richard@'localhost';
GRANT SELECT ON performance_schema.* TO aboki@'localhost';

FLUSH PRIVILEGES;