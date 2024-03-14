-- Script to create the table force_name with id and name columns
-- The name column is set to not allow null values

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

