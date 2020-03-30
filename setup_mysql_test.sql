-- Another script to get our MySQl server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Grant privileges to user hbnb_test
GRANT USAGE ON *.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
-- Grant priviliges to user hbnb_test ON hbnb_test_db (DATABASE)
GRANT ALL PRIVILEGES ON `hbnb_test_db`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
-- Grant SELECT to user hbnb_test on performance_schema
GRANT SELECT ON `performance_schema`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
