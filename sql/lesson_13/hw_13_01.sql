CREATE SCHEMA IF NOT EXISTS sql_hw_13;

USE sql_hw;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS work_shifts;
DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS rates;
DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS demand_ratio;
DROP TABLE IF EXISTS comment_pattern_to_comments;
DROP TABLE IF EXISTS comment_patterns;
DROP TABLE IF EXISTS comments;

CREATE TABLE IF NOT EXISTS customers
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    email        VARCHAR(256) NOT NULL UNIQUE,
    firstname    VARCHAR(30)  NOT NULL,
    lastname     VARCHAR(30),
    phone_number VARCHAR(12),
    rate         FLOAT
);

CREATE TABLE IF NOT EXISTS rates
(
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS cars
(
    id      INT AUTO_INCREMENT PRIMARY KEY,
    rate_id INT,
    model   VARCHAR(30),
    type    VARCHAR(30),
    FOREIGN KEY (rate_id) REFERENCES rates (id)
);

CREATE TABLE IF NOT EXISTS drivers
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    firstname    VARCHAR(30),
    lastname     VARCHAR(30),
    phone_number VARCHAR(12),
    rate         FLOAT
);

CREATE TABLE IF NOT EXISTS work_shifts
(
    id        INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    car_id    INT,
    FOREIGN KEY (driver_id) REFERENCES drivers (id),
    FOREIGN KEY (car_id) REFERENCES cars (id)
);

CREATE TABLE IF NOT EXISTS demand_ratio
(
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS comments
(
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS comment_patterns
(
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS comment_pattern_to_comments
(
    comment_id         INT,
    comment_pattern_id INT,
    FOREIGN KEY (comment_id) REFERENCES comments (id),
    FOREIGN KEY (comment_pattern_id) REFERENCES comment_patterns (id)
);

CREATE TABLE IF NOT EXISTS orders
(
    id              INT AUTO_INCREMENT PRIMARY KEY,
    driver_id       INT        NOT NULL,
    customer_id     INT        NOT NULL,
    demand_ratio_id INT        NOT NULL,
    rate_id         INT        NOT NULL,
    comment_id      INT UNIQUE NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES drivers (id),
    FOREIGN KEY (customer_id) REFERENCES customers (id),
    FOREIGN KEY (demand_ratio_id) REFERENCES demand_ratio (id),
    FOREIGN KEY (rate_id) REFERENCES rates (id),
    FOREIGN KEY (comment_id) REFERENCES comments (id)
);

