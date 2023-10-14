-- create a table users with constraints applied on id and email columns

CREATE TABLE users IF NOT EXISTS(
    id INTEGER AUTO-INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
)