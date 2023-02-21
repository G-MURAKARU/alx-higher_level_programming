-- create database `hbtn_0d_2`
-- script: create a MySQL server user `user_0d_2` with password `user_0d_2_pwd` and granting them all privileges only on `hbtn_0d_2`
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_2;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT
    SELECT
    ON hbtn_0d_2.*
    TO 'user_0d_2'@'localhost';
