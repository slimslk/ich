CREATE SCHEMA IF NOT EXISTS 190224_Dmytro;
USE 190224_Dmytro;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(255) UNIQUE,
    post_index VARCHAR(10),
    country VARCHAR(20),
    city VARCHAR(20),
    street VARCHAR(30),
    created_at DATETIME

    );
CREATE TABLE IF NOT EXISTS orders (
    customer_id INT,
    created_at DATETIME,
    item_code VARCHAR(32),
    description VARCHAR(128),
    image_url VARCHAR(1000),
    price DECIMAL(8, 2) CHECK ( price >= 0 )
    );

INSERT INTO customers (first_name, last_name, email, post_index, country, city, street, created_at)
VALUES
    ('Loree', 'Schroeder', 'Loree.Schroeder@mymail.com', '46667', 'Solomon Islands', 'South Hiram', '64374 Jackie Lodge', '2022-12-31'),
    ('Zulma', 'Blick', 'Zulma.Blick@mymail.com', '78276', 'Djibouti', 'New Samual', '5744 Christian Oval', '2024-03-18'),
    ('Jimmie', 'Greenfelder', 'Jimmie.Greenfelder@mymail.com', '91619', 'Niue', 'South Catrice', '38718 Gutkowski Circle', '2013-10-01'),
    ('Herb', 'Medhurst', 'Herb.Medhurst@mymail.com', '92445', 'Antigua and Barbuda', 'Jeraldineton', '26492 Sharice Street', '2024-03-07'),
    ('Demetrius', 'Hegmann', 'Demetrius.Hegmann@mymail.com', '99461', 'Puerto Rico', 'Johnstonburgh', '9183 Carita Centers', '1992-07-10');

INSERT INTO orders (customer_id, created_at, item_code, description, image_url, price)
VALUES
    (1, '2024-02-12 12:34:32', 'CD10002', 'Play Station 5', 'http://myhost.net/images?id=199943423', 550.00),
    (1, '2024-02-18 13:45:32', 'CD12302', 'XBox Series X', 'http://myhost.net/images?id=13345943423', 420.50),
    (2, '2024-02-29 15:43:32', 'CD99002', 'Nintendo Switch', 'http://myhost.net/images?id=1995342324', 290.35),
    (2, '2024-03-01 17:21:32', 'AB10002', 'Lego N32254', 'http://myhost.net/images?id=244403343', 128.29),
    (2, '2024-03-07 11:32:32', 'MR10002', 'MacBook Pro 2024', 'http://myhost.net/images?id=54323432', 2300.99),
    (3, '2024-03-02 10:15:32', 'MR13422', 'Samsung MR134', 'http://myhost.net/images?id=75435634', 910.50),
    (4, '2024-01-04 16:23:32', 'CF54324', 'PS5 Remote control', 'http://myhost.net/images?id=653464332', 70.70),
    (5, '2024-01-25 13:13:32', 'CD86543', 'Sega Mega Drive', 'http://myhost.net/images?id=87853245', 9.99),
    (5, '2024-01-19 18:14:32', 'MR10002', 'MacBook Pro 2024', 'http://myhost.net/images?id=54323432', 2300.99),
    (5, '2024-03-01 17:21:32', 'AB10002', 'Lego N32254', 'http://myhost.net/images?id=244403343', 128.29),
    (3, '2024-02-29 20:59:32', 'CD10002', 'Play Station 5', 'http://myhost.net/images?id=199943423', 550.00);

ALTER TABLE customers
    ADD last_modified DATETIME DEFAULT NOW();

ALTER TABLE orders
    ADD discounter_price DECIMAL(8, 2) DEFAULT 0;

UPDATE orders
SET discounter_price = price * 0.9;

INSERT INTO customers (first_name, last_name, email, post_index, country, city, street, created_at, last_modified)
VALUES
    ('Edmond', 'Schulist', 'Edmond.Schulist@mymail.com', '52620-0865', 'China', 'VonRuedentown', '67340 Rodriguez Falls', '2024-01-25', NOW()),
    ('Jeffery', 'Reichert', 'Jeffery.Reichert@mymail.com', '45187', 'Libyan Jamahiriya', 'Bartellburgh', '4966 Kutch Park', '2023-04-23', NOW()),
    ('Carson', 'Miller', 'Carson.Miller@mymail.com', '98599', 'Madagascar', 'Lake Virgieton', '72417 Phillip Ports', '2024-03-06', NOW());

INSERT INTO customers (first_name, last_name, email, post_index, country, city, street, created_at, last_modified)
VALUES
    ('Leon', 'Wolff', 'Leon.Wolff@gmail.com', '63416-7519', 'Costa Rica', 'South Agustinport', '96416 Mauro Coves', '2024-01-25', NOW());

INSERT INTO customers (first_name, last_name, email, post_index, country, city, street, created_at, last_modified)
VALUES
    ('Monte', 'Stamm', 'Monte.Stamm@mymail.com', '19220', 'Morocco', 'South Agustinport', '321 Willy Path', '2024-01-25', NOW());

INSERT INTO orders (customer_id, created_at, item_code, description, image_url, price, discounter_price)
VALUES
    (9, '2024-02-12 12:34:32', 'CD10002', 'Play Station 5', 'http://myhost.net/images?id=199943423', 550.00, price * 0.8),
    (9, '2024-02-18 13:45:32', 'CD12302', 'XBox Series X', 'http://myhost.net/images?id=13345943423', 420.50, price * 0.9),
    (10, '2024-03-02 10:15:32', 'MR13422', 'Samsung MR134', 'http://myhost.net/images?id=75435634', 910.50, price * 0.85),
    (10, '2024-01-25 13:13:32', 'CD86543', 'Sega Mega Drive', 'http://myhost.net/images?id=87853245', 9.99,  price * 0.7),
    (10, '2024-01-19 18:14:32', 'MR10002', 'MacBook Pro 2024', 'http://myhost.net/images?id=54323432', 2300.99, price * 0.5),
    (11, '2024-03-01 17:21:32', 'AB10002', 'Lego N32254', 'http://myhost.net/images?id=244403343', 128.29, price * 0.9),
    (11, '2024-01-04 16:23:32', 'CF54324', 'PS5 Remote control', 'http://myhost.net/images?id=653464332', 70.70, price * 0.95),
    (11, '2024-02-12 12:34:32', 'CD10002', 'Play Station 5', 'http://myhost.net/images?id=199943423', 550.00, price * 0.8);

SELECT * FROM customers;
SELECT * FROM orders;