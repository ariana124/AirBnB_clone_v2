-- This script will prepare our MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Grant privileges to user hbnb_dev
GRANT USAGE ON * . *
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant priviliges to user hbnb_dev ON hbnb_dev_db (DATABASE)
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant SELECT to user hbnb_dev on performance_schema
GRANT SELECT ON `performance_schema`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
