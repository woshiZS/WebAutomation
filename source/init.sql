-- you can build a form on your own,just regard this file as a reference
CREATE DATABASE IF NOT EXISTS auto_fill;

-- change to auto_fill
USE auto_fill;

-- If This table exists, drop it and create a new one!
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  user_account char(50) NOT NULL,
  user_pwd char(50) NOT NULL,
  -- if or not you are at school
  user_state int(11) NOT NULL,
  user_prov char(50) NOT NULL,
  user_city char(50) DEFAULT NULL,
  user_block char(50) NOT NULL,
  PRIMARY KEY (user_account)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Finished hint
SELECT 'ok' as 'result:';