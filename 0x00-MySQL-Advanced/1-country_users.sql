-- create table users

CREATE TABLE users IF NOT EXISTS(
    id INT AUTO-INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT ENUM('US')
);