-- script: create a database `hbtn_0d_usa` in MySQL server if not exists
-- create table `cities` in created database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    NAME VARCHAR(256),
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);