-- script: create a database `hbtn_0d_usa` in MySQL server if not exists
-- create table `states` in created database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id)
);